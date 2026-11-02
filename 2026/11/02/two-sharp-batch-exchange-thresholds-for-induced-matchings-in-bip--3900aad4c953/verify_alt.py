"""Independent maximum-clique formulation; no reliance on claimed optimum classification.
Run: python3 verify_alt.py
"""
from itertools import combinations
from collections import Counter

def analyze(m,n):
    edges=[]
    for i in range(m):
        for j in range(n):
            edges += [((0,i),(2,i,j)),((1,j),(2,i,j))]
    E=len(edges)
    incident={}
    for u,v in edges:
        incident.setdefault(u,set()).add(v)
        incident.setdefault(v,set()).add(u)
    # Compatibility means the four endpoints form exactly two isolated edges.
    comp={i:set() for i in range(E)}
    for i,(u,v) in enumerate(edges):
        for j in range(i+1,E):
            a,b=edges[j]
            if len({u,v,a,b})==4 and b not in incident[u] and a not in incident[u] and a not in incident[v] and b not in incident[v]:
                comp[i].add(j);comp[j].add(i)
    max_size=0
    maxima=[]
    # Enumerate all maximal cliques in edge compatibility graph, by Bron-Kerbosch.
    def rec(R,P,X):
        nonlocal max_size,maxima
        if not P and not X:
            if len(R)>max_size:
                max_size=len(R);maxima=[frozenset(R)]
            elif len(R)==max_size:maxima.append(frozenset(R))
            return
        if len(R)+len(P)<max_size:return
        pivot=max(P|X,key=lambda u:len(comp[u]&P)) if (P or X) else None
        for v in list(P-(comp[pivot] if pivot is not None else set())):
            rec(R+[v],P&comp[v],X&comp[v])
            P.remove(v);X.add(v)
    rec([],set(range(E)),set())
    assert max_size==m+n-2,(m,n,max_size)
    assert len(maxima)==m*n,(m,n,len(maxima))
    # Rebuild exchange metrics WITHOUT identifying cliques by coordinates.
    distances=Counter()
    for a,b in combinations(maxima,2):distances[len(a-b)]+=1
    want=Counter()
    want[m] += m * (n*(n-1)//2)
    want[n] += n * (m*(m-1)//2)
    want[max_size] += (m*(m-1)//2)*(n*(n-1)//2)*2
    # When m==n or max_size==m, Counter adds overlapping costs.
    assert distances==want,(m,n,distances,want)
    print('ALT_MAX_CLIQUE_OK',m,n,'opt',max_size,'count',len(maxima),'distance_multiplicities',sorted(distances.items()))

if __name__=='__main__':
    for dims in [(3,3),(3,4),(4,3),(3,5),(4,4)]:analyze(*dims)
    print('ALT_INDEPENDENT_CERTIFICATE_OK')
