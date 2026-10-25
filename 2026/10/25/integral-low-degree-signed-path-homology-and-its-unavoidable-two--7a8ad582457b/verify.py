"""Independent finite checks of the integral signed path boundary in degrees 0,1,2.
Requires Python >=3.10 and sympy. Graphs are simple, undirected, and signed.
"""
from itertools import combinations, product
from collections import deque, Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def connected(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    vis={0};queue=[0]
    for x in queue:
        for y in adj[x]:
            if y not in vis:vis.add(y);queue.append(y)
    return len(vis)==n


def girth_ge_five(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    for a,b,c in combinations(range(n),3):
        if b in adj[a] and c in adj[b] and a in adj[c]:return False
    for a,b,c,d in combinations(range(n),4):
        if (b in adj[a] and c in adj[b] and d in adj[c] and a in adj[d]) or (c in adj[a] and b in adj[c] and d in adj[b] and a in adj[d]) or (b in adj[a] and d in adj[b] and c in adj[d] and a in adj[c]):return False
    return True


def graph_cycle(n):return [(i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n)]
def bowtie_c5():
    a=graph_cycle(5)
    b=[(0,5),(5,6),(6,7),(7,8),(0,8)]
    return 9,sorted(set(a+b))

def petersen():
    es=[]
    for i in range(5):
        es.extend([tuple(sorted((i,(i+1)%5))),tuple(sorted((i,i+5))), tuple(sorted((i+5,(i+2)%5+5)))])
    return 10,sorted(set(es))

def heawood():
    lines=[{i,(i+1)%7,(i+3)%7} for i in range(7)]
    return 14,sorted((p,7+j) for j,l in enumerate(lines) for p in l)


def balanced_by_tree(n,es,sign):
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(es):adj[u].append((v,i));adj[v].append((u,i))
    phase={0:1};queue=[0]
    for u in queue:
        for v,i in adj[u]:
            if v not in phase:phase[v]=phase[u]*sign[i];queue.append(v)
    assert len(phase)==n
    return all(phase[u]*phase[v]==sign[i] for i,(u,v) in enumerate(es))


def components_cover(n,es,sign):
    adj=[set() for _ in range(2*n)]
    for i,(u,v) in enumerate(es):
        for side in (0,1):
            other=side if sign[i]==1 else 1-side
            a=2*u+side;b=2*v+other
            adj[a].add(b);adj[b].add(a)
    unseen=set(range(2*n));ncomp=0
    while unseen:
        ncomp+=1;root=unseen.pop();queue=[root]
        for x in queue:
            for y in adj[x]:
                if y in unseen:unseen.remove(y);queue.append(y)
    return ncomp


def verify_case(n,es,sign):
    assert connected(n,es) and girth_ge_five(n,es)
    lookup={e:sign[i] for i,e in enumerate(es)}
    sg=lambda u,v:lookup[tuple(sorted((u,v)))]
    adj=[set() for _ in range(n)]
    for u,v in es:adj[u].add(v);adj[v].add(u)
    # Enumerate every allowed signed 2-path in the quotient lift basis.
    # Each non-backtrack creates exactly one (nonallowed) forbidden 1-path.
    forbidden=Counter();backtracks=[];total=0
    for b in range(n):
        for a in sorted(adj[b]):
            for c in sorted(adj[b]):
                total+=1
                if a==c:
                    assert sg(a,b)*sg(b,c)==1
                    backtracks.append((a,b,c))
                else:
                    assert c not in adj[a]
                    forbidden[(a,c,sg(a,b)*sg(b,c))]+=1
    assert all(v==1 for v in forbidden.values())
    assert len(backtracks)==2*len(es)
    # Signed 2-backtrack boundaries [a,b]+sigma(ab)[b,a] are primitive
    # edgewise relations. Their full row family has rank one per edge.
    darts=[(u,v) for u,v in es]+[(v,u) for u,v in es]
    ix={d:i for i,d in enumerate(darts)}
    rel=Matrix.zeros(2*len(es),2*len(es))
    for col,(a,b,c) in enumerate(backtracks):
        rel[ix[(a,b)],col]+=1
        rel[ix[(b,a)],col]+=sg(a,b)
    # compare column span with direct edgewise relation matrix, via rank;
    # each observed column must be a signed multiple of its edge relation.
    assert rel.rank()==len(es)
    for j,(u,v) in enumerate(es):
        row1=rel.row(ix[(u,v)]);row2=rel.row(ix[(v,u)])
        assert all(row1[k]==sign[j]*row2[k] for k in range(2*len(es)))
    # Twisted cellular incidence after quotienting those backtracks.
    inc=Matrix.zeros(n,len(es))
    for j,(u,v) in enumerate(es):inc[u,j]=-1;inc[v,j]=sign[j]
    sn=smith_normal_form(inc,domain=ZZ)
    diag=[abs(int(sn[i,i])) for i in range(min(n,len(es))) if sn[i,i]!=0]
    free=n-len(diag)
    tors=[d for d in diag if d>1]
    bal=balanced_by_tree(n,es,sign)
    expected_rank0=1 if bal else 0
    expected_tors=[] if bal else [2]
    expected_rank1=len(es)-n+expected_rank0
    assert free==expected_rank0 and tors==expected_tors
    assert len(es)-len(diag)==expected_rank1
    cover_comp=components_cover(n,es,sign)
    assert cover_comp==(2 if bal else 1)
    # In the unbalanced case the anti-invariant subgroup of cover H0 is 0,
    # whereas homology of the integral anti-invariant CHAIN complex is Z/2.
    return len(es),total,len(backtracks),bal,expected_rank1,tuple(tors)


def main():
    cases=[]
    for n in (5,6,7):
        es=sorted(set(graph_cycle(n)))
        for bits in product((1,-1),repeat=len(es)):
            cases.append((f'C{n}',n,es,bits))
    n,es=bowtie_c5()
    for x in range(64):
        signs=tuple(-1 if (x>>j)&1 else 1 for j in range(len(es)))
        cases.append(('c5_bouquet',n,es,signs))
    for name, maker, patterns in [('Petersen',petersen,40),('Heawood',heawood,30)]:
        n,es=maker()
        cases.append((name,n,es,tuple([1]*len(es))))
        cases.append((name,n,es,tuple([-1]+[1]*(len(es)-1))))
        for x in range(patterns):
            signs=tuple(-1 if (((x*31+7*j*j+11*j)>> (j%5))&1) else 1 for j in range(len(es)))
            cases.append((name,n,es,signs))
    total=0;two=0;paths=0;types=Counter();balance=Counter()
    for name,n,es,sign in cases:
        m,p,b,bal,h1,tors=verify_case(n,es,sign)
        total+=1;two+=b;paths+=p
        types[(name,bal)]+=1;balance[(bal,h1,tors)]+=1
    print('TEST_OK')
    print('graphs/signings checked:',total)
    print('allowed signed two-path basis instances:',paths)
    print('backtrack relation instances:',two)
    print('by family and balance:',sorted(types.items()))
    print('by balance, first Betti rank, torsion H0:',sorted(balance.items(),key=str))
    print('Smith invariant factors and connected double cover checked for each case')
    print('VERIFY_OK')
if __name__=='__main__':main()
