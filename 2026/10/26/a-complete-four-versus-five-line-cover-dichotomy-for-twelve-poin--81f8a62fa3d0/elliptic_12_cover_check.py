#!/usr/bin/env python3
"""Finite exact witnesses for twelve-point plane-cubic line-cover theorem."""
from itertools import product

CERT={
('C12',0): [[0,3,9],[1,4,7],[1,10],[2,4,6],[5,8,11]],
('C12',1): [[0,2,11],[1,5,7],[3,4,6],[7,8,10],[8,9]],
('C12',2): [[0,3,11],[1,6,7],[2,10],[4,5],[8,9]],
('C2xC6',0): [[(0,0),(1,2),(1,4)],[(0,1),(0,2),(0,3)],[(0,4),(1,3),(1,5)],[(0,5),(1,0),(1,1)]],
('C2xC6',1): [[(0,0),(1,0),(1,1)],[(0,1),(0,3)],[(0,2),(1,2),(1,3)],[(0,4),(1,4),(1,5)],[(0,5),(1,1)]],
('C2xC6',2): [[(0,0),(0,2)],[(0,1),(1,2),(1,5)],[(0,3),(1,2),(1,3)],[(0,4),(1,0),(1,4)],[(0,5),(1,1),(1,2)]]
}

def valid_line(L,G,T):
    if len(L)==3:
        return len(set(L))==3 and tuple(sum(p[i] for p in L)%G[i] for i in range(len(G)))==T
    if len(L)==2:
        a,b=L
        if a==b:return False
        return (all((2*a[i]+b[i])%G[i]==T[i] for i in range(len(G))) or
                all((a[i]+2*b[i])%G[i]==T[i] for i in range(len(G))))
    return False

for (kind,representative),Ls in CERT.items():
    G=(12,) if kind=='C12' else (2,6)
    T=(representative,) if kind=='C12' else (0,representative)
    sets=[[p if isinstance(p,tuple) else (p,) for p in line] for line in Ls]
    assert all(valid_line(L,G,T) for L in sets),(kind,T)
    assert set.union(*(set(L) for L in sets)) == set(product(*(range(x) for x in G)))
    assert len(Ls)==(4 if kind=='C2xC6' and representative==0 else 5)
    print('COVER_OK',kind,T,len(Ls))

q=11
for a,b,expected_2torsion in [(0,1,1),(2,0,3)]:
    assert (4*a**3+27*b*b)%q !=0
    pts=[(x,y) for x in range(q) for y in range(q) if (y*y-x*x*x-a*x-b)%q==0]
    twotorsion=sum(y==0 for x,y in pts)
    assert len(pts)+1==12 and twotorsion==expected_2torsion
    print('CURVE_OK',q,a,b,len(pts)+1,twotorsion)
print('ALL_CHECKS_PASS')
