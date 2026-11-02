"""Exact finite sanity checks for controllability of triangular graphs.

All checks are over finite fields and integer combinatorics, and do not
substitute for the all-dimensional analytic proof.
"""
from itertools import combinations
from math import comb, factorial
from fractions import Fraction

PRIME = 1000003

def rank_mod(rows, ncols, p=PRIME):
    a = [[v % p for v in row] for row in rows]
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                v = a[i][col]
                a[i] = [(x - v * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == ncols:
            break
    return rank

def inc_row(n, e):
    row = [0]*n
    row[e[0]] = row[e[1]] = 1
    return row

def odd_unicyclic_components(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    unseen = set(range(n))
    for root in range(n):
        if root not in unseen:
            continue
        seen = {root}; stack = [root]; unseen.remove(root)
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w); seen.add(w); stack.append(w)
        edge_ct = sum(len(adj[v]) for v in seen)//2
        if edge_ct != len(seen):
            return False
        colors = {}
        bipartite = True
        for start in seen:
            if start in colors: continue
            colors[start] = 0; todo=[start]
            while todo:
                v=todo.pop()
                for w in adj[v]:
                    if w not in colors:
                        colors[w]=1-colors[v];todo.append(w)
                    elif colors[w]==colors[v]:
                        bipartite = False
        if bipartite:
            return False
    return True

def predicted(n, F):
    if n < 5:
        raise ValueError('only n>=5')
    if not odd_unicyclic_components(n, F):
        return False
    if n == 6 and len(F)==6:
        degrees = [0]*n
        for u,v in F:
            degrees[u]+=1;degrees[v]+=1
        # Here every degree two and two connected triangles is forced.
        if degrees == [2]*n:
            return False
    return True

def pbh_direct(n, chosen_controls):
    edges = list(combinations(range(n),2))
    m=len(edges); U=set(chosen_controls)
    # Laplacian of the line graph K_n, assembled without using incidence
    L=[[0]*m for _ in range(m)]
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and len(set(e)&set(f))==1:
                L[i][j]=-1; L[i][i]+=1
    for lam in (0,n,2*n-2):
        mat=[]
        for i in range(m):
            row=[L[i][j]-(lam if i==j else 0) for j in range(m)]
            row += [int(i==j) for j in chosen_controls]
            mat.append(row)
        if rank_mod(mat,m+len(chosen_controls)) < m:
            return False
    return True

def exact_egf_count(n):
    """Count spanning odd-unicyclic-component graphs via the EGF."""
    t=[Fraction(0)]+[Fraction(k**(k-1),factorial(k)) for k in range(1,n+1)]
    def multiply(a,b):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]
    power=[Fraction(1)]+[Fraction(0)]*n
    C=[Fraction(0)]*(n+1)
    for ell in range(1,n+1):
        power=multiply(power,t)
        if ell>=3 and ell%2:
            C=[C[k]+power[k]/(2*ell) for k in range(n+1)]
    E=[Fraction(1)]+[Fraction(0)]*n
    for k in range(1,n+1):
        E[k]=sum(j*C[j]*E[k-j] for j in range(1,k+1))/k
    count=E[n]*factorial(n)
    assert count.denominator==1
    return count.numerator

def direct_kalman(n, chosen_controls):
    """Build the full discrete Kalman matrix independently modulo PRIME."""
    edges=list(combinations(range(n),2))
    m=len(edges); k=len(chosen_controls)
    L=[[0]*m for _ in range(m)]
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and len(set(e)&set(f))==1:
                L[i][j]=-1
                L[i][i]+=1
    X=[[int(i==j) for j in chosen_controls] for i in range(m)]
    K=[[] for _ in range(m)]
    for _ in range(m):
        for i in range(m): K[i].extend(X[i])
        X=[[sum(L[i][j]*X[j][t] for j in range(m))%PRIME for t in range(k)] for i in range(m)]
    return rank_mod(K,k*m)==m

def run():
    checks=0
    # Explicit sharp construction in small orders.
    for n in range(3,12):
        edges=list(combinations(range(n),2))
        if n>=5:
            chosen=[i for i,(u,v) in enumerate(edges) if u!=0 and v!=0 and (u,v)!=(1,2)]
            assert len(chosen)==comb(n,2)-n
        elif n==4:
            chosen=[i for i,(u,v) in enumerate(edges) if u!=0]
            assert len(chosen)==3
        else:
            chosen=[0,1]
        assert pbh_direct(n,chosen)
        if n<=6:
            assert direct_kalman(n,chosen)
            checks+=1
        if n>=5:
            white=set(edges)-set(edges[i] for i in chosen)
            # Every chosen edge shares each endpoint with a distinct white edge.
            assert all(sum(len(set(edges[i])&set(e))==1 for e in white)>=2 for i in chosen)
            checks+=1
        checks+=1
    summaries={}
    # Exhaustive sharp-cardinality census for 5,6. Compare independent
    # direct incidence/PBH spectral conditions and graph cycle classification.
    for n in (5,6):
        edges=list(combinations(range(n),2))
        m=len(edges); count_good=0;count_pseudo=0;count_direct=0
        for I in combinations(range(m),n):
            F=[edges[i] for i in I]
            Iset=set(I)
            U=[edges[i] for i in range(m) if i not in Iset]
            B_F = [inc_row(n,e) for e in F]
            # Full column independence of F, from the signless incidence.
            bf_rank=rank_mod(B_F,n)
            a_rank=rank_mod([inc_row(n,e) for e in U]+[[1]*n],n)
            pbh=bf_rank==n and a_rank==n
            pred=predicted(n,F)
            assert pbh==pred,(n,F,pred,bf_rank,a_rank)
            count_pseudo+=odd_unicyclic_components(n,F)
            count_good+=pred
            checks+=1
            # Independently form and check entire line-graph PBH matrix on
            # every fifty-th candidate, including some rare exceptions.
            if count_direct%50==0 or (n==6 and odd_unicyclic_components(n,F) and not pred):
                chosen=[i for i in range(m) if i not in Iset]
                assert pbh_direct(n,chosen)==pred,(n,F)
                checks+=1
            count_direct+=1
        summaries[n]=(count_good,count_pseudo)
    assert summaries[5]==(162,162),summaries
    assert summaries[6]==(2520,2530),summaries
    for n,count in [(5,162),(6,2530),(7,45615),(8,937440)]:
        assert exact_egf_count(n)==count
        checks+=1
    # 6-vertex exceptional configuration and the explicit successful family.
    n=6; e=list(combinations(range(n),2))
    F={(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)}
    chosen=[i for i,x in enumerate(e) if x not in F]
    assert not pbh_direct(n,chosen)
    assert not direct_kalman(n,chosen)
    checks+=2
    # Finite sampling in 7,8 to stress graph classification; no exhaustive
    # all-dimensional claim is inferred from this test.
    for n in (7,8):
        edges=list(combinations(range(n),2));m=len(edges)
        for t in range(600):
            # deterministic shuffle without importing external packages
            import random
            rr=random.Random((n<<20)+t)
            Iset=set(rr.sample(range(m),n))
            F=[edges[i] for i in sorted(Iset)]
            U=[edges[i] for i in range(m) if i not in Iset]
            bf=rank_mod([inc_row(n,e) for e in F],n)==n
            ar=rank_mod([inc_row(n,e) for e in U]+[[1]*n],n)==n
            assert (bf and ar)==predicted(n,F)
            checks+=1
    print('VERIFY_OK',checks,'finite_check_groups', 'sharp_census',summaries)

if __name__=='__main__':
    run()
