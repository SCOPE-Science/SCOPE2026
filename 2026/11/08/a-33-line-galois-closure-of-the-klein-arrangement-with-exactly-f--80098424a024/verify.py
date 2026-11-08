"""Exact integral determinant certificate for the 21 Klein lines.
No libraries beyond the Python standard library are required.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, comb

Z=(0,0); O=(1,0); N=(-1,0); W=(0,1)
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-2*b*d,a*d+b*c-b*d)
def norm(x):
    a,b=x
    return a*a-a*b+2*b*b
def det(a,b,c):
    return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))
def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))
V=[(O,Z,Z),(Z,O,O),(W,O,N),(W,N,O),(Z,N,O),
   (O,W,N),(W,N,N),(N,O,W),(W,O,O),(N,W,O),
   (N,N,W),(O,Z,O),(N,W,N),(O,W,O),(N,Z,O),
   (O,N,W),(O,O,W),(Z,Z,O),(N,O,Z),(O,O,Z),(Z,O,Z)]
assert len(V)==21
pairs=list(combinations(range(21),2))
assert len(pairs)==210
pair_id={e:i for i,e in enumerate(pairs)}
parent=list(range(len(pairs)))
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i
def union(a,b): parent[root(a)]=root(b)

for i,j in pairs:
    minors=cross(V[i],V[j])
    g=0
    for u in minors: g=gcd(g,norm(u))
    assert g>0 and g&(g-1)==0, (i,j,g)

hist=Counter(); zero=0
for tri in combinations(range(21),3):
    d=det(*(V[i] for i in tri))
    n=norm(d)
    if n==0:
        assert d==Z
        zero+=1
        edges=[pair_id[t] for t in combinations(tri,2)]
        union(edges[0],edges[1]); union(edges[1],edges[2])
    else:
        assert n&(n-1)==0, (tri,n,d)
        hist[n]+=1
assert zero==112
assert sum(hist.values())==comb(21,3)-112
assert hist=={1:169,2:228,4:271,8:320,16:156,32:70,64:4}, hist
classes=defaultdict(list)
for i,edge in enumerate(pairs): classes[root(i)].append(edge)
assert Counter(map(len,classes.values()))=={3:28,6:21}
perline={i:Counter() for i in range(21)}
for edges in classes.values():
    on=set(t for edge in edges for t in edge)
    k=len(on)
    assert k in (3,4) and len(edges)==comb(k,2)
    for i in on: perline[i][k]+=1
assert all(perline[i]=={3:4,4:4} for i in range(21)), perline
assert 28*comb(3,2)+21*comb(4,2)==comb(21,2)

def modtwo(v,root):
    a,b=v
    return (a+b*root)%2
def normalize(p):
    pos=next(i for i,c in enumerate(p) if c)
    return p  # only nonzero scalar in F2 is 1
for root2,expected in [(0,6),(1,7)]:
    special=[normalize(tuple(modtwo(c,root2) for c in v)) for v in V]
    assert all(any(x for x in v) for v in special)
    assert len(set(special))==expected,(root2,special)
print('VERIFY_KLEIN_GOOD_REDUCTION_OK',
      'triple_determinants=1330','zero=112','norm_hist='+str(sorted(hist.items())),
      'triple_points=28','quadruple_points=21',
      'characteristic_two_distinct_lines=6,7')

# The arithmetic Galois closure: all Klein lines and their quadratic conjugates.
def conj(u):
    a,b=u
    return (a-b,-b)
C=V[:]
for v in V:
    z=tuple(conj(t) for t in v)
    if z not in C and tuple(neg(t) for t in z) not in C:
        C.append(z)
assert len(C)==33
from math import isqrt
BAD={2,3,7,11}
pair_bad=set()
for i,j in combinations(range(len(C)),2):
    g=0
    for u in cross(C[i],C[j]): g=gcd(g,norm(u))
    assert g>0
    d=g
    for p in BAD:
        while d%p==0: d//=p; pair_bad.add(p)
    assert d==1,(i,j,g,d)
triple_bad=set();zero_triples=0
for i,j,k in combinations(range(len(C)),3):
    n=norm(det(C[i],C[j],C[k]))
    if n==0:
        zero_triples+=1
        continue
    d=n
    for p in BAD:
        while d%p==0: d//=p; triple_bad.add(p)
    assert d==1,(i,j,k,n,d)
assert zero_triples==280
assert triple_bad==BAD,(triple_bad,pair_bad)

def profile(p=None,omega=None):
    """Exact projective line and concurrence counts, no finite-field point census."""
    def zero(u):
        if p is None:return u==Z
        if omega is None:return u[0]%p==0 and u[1]%p==0
        return (u[0]+omega*u[1])%p==0
    n=len(C)
    lineparent=list(range(n))
    def find(arr,i):
        while arr[i]!=i:
            arr[i]=arr[arr[i]]
            i=arr[i]
        return i
    def merge(arr,i,j):arr[find(arr,i)]=find(arr,j)
    for i,j in combinations(range(n),2):
        if all(zero(a) for a in cross(C[i],C[j])):
            merge(lineparent,i,j)
    reps=sorted(set(find(lineparent,i) for i in range(n)))
    pairs2=list(combinations(reps,2))
    ids={ab:i for i,ab in enumerate(pairs2)}
    par=list(range(len(pairs2)))
    n_dep=0
    for tr in combinations(reps,3):
        if zero(det(*(C[i] for i in tr))):
            n_dep+=1
            ps=list(combinations(tr,2))
            merge(par,ids[ps[0]],ids[ps[1]])
            merge(par,ids[ps[1]],ids[ps[2]])
    loc=defaultdict(list)
    for i,pr in enumerate(pairs2):loc[find(par,i)].append(pr)
    h=Counter(); local={r:Counter() for r in reps}
    for edges in loc.values():
        lines={v for ab in edges for v in ab}
        t=len(lines)
        assert len(edges)==t*(t-1)//2,(p,omega,len(edges),t)
        h[t]+=1
        for i in lines:local[i][t]+=1
    return (len(reps),n_dep,dict(sorted(h.items())),
            dict(Counter(tuple(sorted(z.items())) for z in local.values())))

PROFILES={
    (None,None):(33,280,{2:120,3:52,4:27,6:6}),
    (3,None):(33,472,{2:24,3:4,4:27,5:24,6:6}),
    (7,3):(21,112,{3:28,4:21}),
    (11,4):(33,460,{2:48,3:40,4:15,6:18}),
    (11,6):(33,460,{2:48,3:40,4:15,6:18}),
    (2,0):(7,7,{3:7}),
    (2,1):(7,7,{3:7}),
}
for (p,omega),(lines,dependent,h) in PROFILES.items():
    got=profile(p,omega)
    assert got[:3]==(lines,dependent,h),((p,omega),got)
assert profile(3,None)[3] == {((2,2),(4,3),(5,4),(6,1)):24,
                                ((3,2),(4,5),(5,2),(6,1)):6,
                                ((4,2),(5,4),(6,2)):3}
print('VERIFY_KLEIN_GALOIS_CLOSURE_OK','lines=33','generic='+str(PROFILES[(None,None)][2]),
      'bad_primes='+str(sorted(triple_bad)),'special_profiles=2,3,7,11')
