"""Exact finite diagnostic for complete-bipartite social-comparison cancellation.
This program is supplementary; the theorem follows from the accompanying proof.
No third-party packages are required.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def p_matrix(neighbors):
    n=len(neighbors)
    return [[Q(int(j in neighbors[i]),len(neighbors[i])) for j in range(n)] for i in range(n)]


def connected(neighbors):
    todo=[0]; seen={0}
    while todo:
        for v in neighbors[todo.pop()]:
            if v not in seen:
                seen.add(v); todo.append(v)
    return len(seen)==len(neighbors)


def complete_bipartite(neighbors):
    n=len(neighbors); side=[None]*n; side[0]=0; todo=[0]
    while todo:
        v=todo.pop()
        for u in neighbors[v]:
            if side[u] is None: side[u]=1-side[v]; todo.append(u)
            elif side[u]==side[v]: return False
    if any(v is None for v in side): return False
    return all((j in neighbors[i])==(side[i]!=side[j])
               for i in range(n) for j in range(n) if i!=j)


def cancellation_property(neighbors):
    P=p_matrix(neighbors)
    return all(P[i]==P[k] for nbr in neighbors for i,k in combinations(nbr,2))


def score_data(neighbors,x,b,c,lambdas):
    P=p_matrix(neighbors); n=len(neighbors)
    u=[-c*x[i]+b*sum(P[i][j]*x[j] for j in range(n)) for i in range(n)]
    s=[u[i]+lambdas[i]*sum(P[i][j]*u[j] for j in range(n)) for i in range(n)]
    return u,s


def main():
    graph_count=0; count_by_n=[]; passing=[]
    for n in range(2,7):
        E=list(combinations(range(n),2)); conn_count=0; good=0
        for mask in range(1<<len(E)):
            nb=[set() for _ in range(n)]
            for e,(i,j) in enumerate(E):
                if mask>>e & 1:
                    nb[i].add(j); nb[j].add(i)
            if not connected(nb): continue
            conn_count+=1
            test=cancellation_property(nb)
            expected=complete_bipartite(nb)
            assert test==expected,(n,mask)
            good+=test
        count_by_n.append((n,conn_count,good))
        graph_count+=conn_count
    assert graph_count==1+4+38+728+26704,graph_count
    # Complete profile classification, including nonuniform and zero profiles.
    # Exact coefficient identity for all donation-game costs and benefits:
    # lambda_i P_i = lambda_k P_k for every pair competing at one vacancy.
    lambda_cases=0
    for n in range(2,6):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            nb=[set() for _ in range(n)]
            for e,(i,j) in enumerate(edges):
                if (mask>>e)&1: nb[i].add(j); nb[j].add(i)
            if not connected(nb): continue
            P=p_matrix(nb); bi=complete_bipartite(nb)
            for ls in product((-1,0,1),repeat=n):
                actual=all(all(ls[i]*P[i][v]==ls[k]*P[k][v]
                               for v in range(n))
                           for nbr in nb for i,k in combinations(sorted(nbr),2))
                if bi:
                    side=[None]*n; side[0]=0; todo=[0]
                    while todo:
                        v=todo.pop()
                        for u in nb[v]:
                            if side[u] is None:
                                side[u]=1-side[v];todo.append(u)
                    expected=all(ls[i]==ls[k] for i in range(n)
                                 for k in range(n) if side[i]==side[k])
                else:
                    expected=not any(ls)
                assert actual==expected,(n,mask,ls)
                lambda_cases+=1
    # Every state, every competitor pair, for two unequal partwise parameters:
    side=[0,0,1,1,1]
    nb=[{j for j in range(5) if side[i]!=side[j]} for i in range(5)]
    lambdas=[Q(13,7) if side[i]==0 else Q(-11,5) for i in range(5)]
    for x in product((0,1),repeat=5):
        for b,c in [(Q(2),Q(3)),(Q(5,3),Q(7,4))]:
            u,s=score_data(nb,x,b,c,lambdas)
            for j,nbr in enumerate(nb):
                for i,k in combinations(sorted(nbr),2):
                    assert s[i]-s[k]==u[i]-u[k]
    # Four-vertex path: at a mixed-strategy vacancy the comparison term matters.
    path=[{1},{0,2},{1,3},{2}]; x=(1,0,0,0)
    u,s=score_data(path,x,Q(1),Q(1),[Q(1)]*4)
    assert (u[0],u[2])==(Q(-1),Q(0))
    assert (s[0]-s[2])-(u[0]-u[2])==Q(1,4)
    # Necessity bridge in the actual donation game: varying cost c detects row P.
    # For any distinct P rows, the coefficient of -c in (Pu)_i-(Pu)_k
    # is -(P_i-P_k)x, nonzero for some binary basis strategy x.
    print('VERIFY_OK graph classification:',count_by_n,
          '; K_2,3 all 32 states exact cancellation; P4 mixed-strategy witness 1/4; exact-profile cases',lambda_cases)

if __name__=='__main__':main()
