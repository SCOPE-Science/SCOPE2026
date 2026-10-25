"""Exact finite checks for reflection traces on independence complexes of cycle--complete-graph products.
No external dependencies. The infinite-parameter proof is independent of these checks.
"""
from functools import lru_cache
from collections import defaultdict

def adjacency(m,n):
    N=m*n
    g=[0]*N
    for i in range(m):
        for a in range(n):
            v=i*n+a
            for j in ((i-1)%m,(i+1)%m):
                for b in range(n):
                    if a!=b: g[v]|=1<<(j*n+b)
    return g

def quotient_eval(m,n,axis):
    """The signed fixed-simplex sum using vertex-orbit independence."""
    g=adjacency(m,n); N=m*n
    perm=[((axis-i)%m)*n+a for i in range(m) for a in range(n)]
    assert all(perm[perm[i]]==i for i in range(N))
    unseen=set(range(N)); orbits=[]
    while unseen:
        i=min(unseen); j=perm[i]
        orb=frozenset((i,j)); orbits.append(orb);unseen.difference_update(orb)
    good=[]
    for orb in orbits:
        if not any(g[v] & (1<<w) for v in orb for w in orb):good.append(orb)
    K=len(good);h=[0]*K
    for i in range(K):
        for j in range(i+1,K):
            if any(g[v]&(1<<w) for v in good[i] for w in good[j]):
                h[i]|=1<<j;h[j]|=1<<i
    @lru_cache(None)
    def ev(mask):
        if not mask:return 1
        # Heuristic: select vertex with many neighbors in remaining graph.
        verts=[i for i in range(K) if mask>>i&1]
        v=max(verts,key=lambda x:(h[x]&mask).bit_count())
        return ev(mask&~(1<<v))-ev(mask&~(h[v]|(1<<v)))
    return ev((1<<K)-1),K

def matrix_trace(m,n,axis):
    # Reflection quotient is a folded path with free/clique endpoints.
    if m%2:
        L=(m+1)//2; first_cap=False; last_cap=True
    elif axis%2==0:
        L=m//2+1; first_cap=False; last_cap=False
    else:
        L=m//2; first_cap=True; last_cap=True
    a,b,c=1,0,0
    for j in range(L):
        cap=(j==0 and first_cap) or (j==L-1 and last_cap)
        a,b,c=a+b+c,-n*a-b,0 if cap else (n-1)*a
    return a+b+c

def direct_fixed_face_trace(m,n,axis):
    # Enumerate original independent sets for an independent check of signs.
    g=adjacency(m,n);N=len(g)
    faces=[0]
    for u in range(N):
        bit=1<<u
        faces += [f|bit for f in faces if f&g[u]==0]
    perm=[((axis-i)%m)*n+a for i in range(m) for a in range(n)]
    total=0
    for f in faces:
        moved=0;v=f
        while v:
            bit=v&-v;v-=bit;moved|=1<<perm[bit.bit_length()-1]
        if moved!=f:continue
        visited=0;orb_count=0;v=f
        while v:
            bit=v&-v;v-=bit
            if visited&bit:continue
            k=bit.bit_length()-1
            visited|=bit|(1<<perm[k]);orb_count+=1
        total+=(-1)**orb_count
    return total,len(faces)

def run_checks():
    tests=0
    for r in range(1,6):
        m=3*r
        for n in range(2,6):
            for axis in range(2 if m%2==0 else 1):
                val,K=quotient_eval(m,n,axis)
                predicted=0 if r%2 or axis%2==0 else n*(n-1)**(r//2)
                assert val==predicted,(m,n,axis,val,predicted)
                assert matrix_trace(m,n,axis)==val,(m,n,axis,'matrix')
                tests+=1
    for m,n in [(3,3),(6,3),(6,4),(9,3)]:
        for axis in range(2 if m%2==0 else 1):
            direct,faces=direct_fixed_face_trace(m,n,axis)
            val,_=quotient_eval(m,n,axis)
            assert direct==val,(m,n,axis,direct,val)
            print('direct',m,n,'axis',axis,'faces',faces,'trace',direct)
            tests+=1
    print('PASS:',tests,'finite exact trace comparisons; all checked')
if __name__=='__main__':run_checks()
