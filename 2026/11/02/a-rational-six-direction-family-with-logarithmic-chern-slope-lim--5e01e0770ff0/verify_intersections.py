"""Independent exact projective pair-intersection census (stdlib only)."""
from collections import Counter
from itertools import combinations
from math import comb, gcd
V=[(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1)]

def primitive(v):
    g=0
    for x in v:g=gcd(g,abs(x))
    t=tuple(x//g for x in v)
    return t if next(x for x in t if x) > 0 else tuple(-x for x in t)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def count(n):
    lines=[(a,b,-t) for a,b in V for t in range(-n,n+1)]
    incidence={}
    for (i,L),(j,R) in combinations(enumerate(lines),2):
        p=primitive(cross(L,R))
        incidence.setdefault(p,set()).update((i,j))
    hist=Counter(len(q) for q in incidence.values())
    expected={2:14*n*(n+1),3:5*n*(n+1),4:n*(n+1),
              5:n*(n+1),6:n*(n+1)+1,2*n+1:6}
    assert hist==Counter(expected),(n,hist,expected)
    assert sum(comb(m,2)*count for m,count in hist.items())==comb(len(lines),2)
    c1=9-5*len(lines)+sum((3*m-4)*c for m,c in hist.items())
    c2=3-2*len(lines)+sum((m-1)*c for m,c in hist.items())
    assert (c1,c2)==(86*n*n+62*n-13,36*n*n+24*n-4)
    return len(lines),hist,c1,c2
for n in (6,12,18,24):
    print(n, count(n))
print('INDEPENDENT_PROJECTIVE_CENSUS_OK')
