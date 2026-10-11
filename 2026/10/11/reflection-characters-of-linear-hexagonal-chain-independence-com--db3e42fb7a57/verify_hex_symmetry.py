"""Independent finite checks for symmetry traces of linear hexagonal chains.

Usage: python3 verify_hex_symmetry.py
No dependencies beyond the Python standard library.
"""
from itertools import combinations
from functools import lru_cache

def graph(n):
    vertices = [(r,c) for r in range(2) for c in range(1,2*n+2)]
    edges = {frozenset(( (r,c),(r,c+1))) for r in range(2) for c in range(1,2*n+1)}
    edges |= {frozenset(((0,c),(1,c))) for c in range(1,2*n+2,2)}
    return vertices, edges

def act(v,n,a,b):
    r,c = v
    return (r^a, (2*n+2-c if b else c))

def quotient(n,a,b):
    V,E=graph(n)
    seen=set(); orbits=[]
    for v in V:
        if v in seen:continue
        o=frozenset((v,act(v,n,a,b)));seen.update(o)
        if len(o)==2 and o in E:continue
        orbits.append(o)
    adj=[]
    for i,o in enumerate(orbits):
        mask=0
        for j,p in enumerate(orbits):
            if i!=j and any(frozenset((v,w)) in E for v in o for w in p):
                mask|=1<<j
        adj.append(mask)
    return adj,orbits

def indep_at_minus_one(adj):
    @lru_cache(None)
    def f(mask):
        if mask==0:return 1
        i=(mask&-mask).bit_length()-1
        rest=mask^(1<<i)
        return f(rest)-f(rest&~adj[i])
    return f((1<<len(adj))-1)

def expected(n,a,b):
    if a==b==0:return 2
    if a==1 and b==0:return 0
    if a==0 and b==1:return 2*((-1)**(n//2)) if n%2==0 else 0
    if a==b==1:return 2*((-1)**((n+1)//2)) if n%2 else 0
    raise AssertionError()

def direct_fixed_face_trace(n,a,b):
    # Enumerate *all* independent subsets of the ORIGINAL graph, not orbit graph.
    V,E=graph(n); N=len(V)
    ids={v:i for i,v in enumerate(V)}
    adj=[0]*N
    for e in E:
        u,v=tuple(e);i,j=ids[u],ids[v]
        adj[i]|=1<<j;adj[j]|=1<<i
    perm=[ids[act(v,n,a,b)] for v in V]
    # sign in reduced augmented Lefschetz trace, including empty (-1)^(-1).
    trace=-1
    for S in range(1,1<<N):
        if any((S&(1<<i)) and (S&adj[i]) for i in range(N)):continue
        if any(bool(S&(1<<i))!=bool(S&(1<<perm[i])) for i in range(N)):continue
        slots=[i for i in range(N) if S>>i&1]
        permuted=[perm[i] for i in slots]
        inversions=sum(permuted[i]>permuted[j] for i in range(len(slots)) for j in range(i+1,len(slots)))
        trace+=(-1)**(len(slots)-1+inversions)
    return (-1)**n*trace

def verify():
    total=0
    for n in range(1,15):
        for a,b in ((0,0),(1,0),(0,1),(1,1)):
            adj,orbits=quotient(n,a,b)
            actual=(-1)**(n+1)*indep_at_minus_one(adj)
            assert actual==expected(n,a,b),(n,a,b,actual)
            total+=1
    # independent method: brute force original fixed simplices and orientation signs
    direct=0
    for n in range(1,5):
        for a,b in ((0,0),(1,0),(0,1),(1,1)):
            actual=direct_fixed_face_trace(n,a,b)
            assert actual==expected(n,a,b),(n,a,b,actual)
            direct+=1
    print(f'VERIFY_OK {total} orbit-graph evaluations (n=1..14) and {direct} direct signed fixed-face enumerations (n=1..4)')

if __name__=='__main__':verify()
