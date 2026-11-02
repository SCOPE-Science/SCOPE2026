#!/usr/bin/env python3
"""Independent finite checks for commuting and mutually annihilating interval translations."""
from math import prod

def matrices(n):
    out=[]
    for ell in range(1,n+1):
        for a in range(1,n-ell+2):
            for c in range(1,n-ell+2):
                # matrix row i has its 1 in column i+c-a
                out.append(tuple((i,i+c-a) for i in range(a,a+ell)))
    return out

def compose(x,y):
    yy=dict(y)
    return frozenset((i,yy[j]) for i,j in x if j in yy)

def expected_z(n):
    return n*(n-1)*(n+1)*(n+2)*(n*n+n-1)//30

for n in range(1,11):
    m=matrices(n)
    assert len(m)==sum(t*t for t in range(1,n+1))
    z=cp=pc=0
    for x in m:
        for y in m:
            xy=compose(x,y); yx=compose(y,x)
            if not xy and not yx: z+=1
            if xy==yx:
                cp+=1
                if xy:pc+=1
    z_formula=expected_z(n)
    assert z==z_formula,(n,z,z_formula)
    assert cp == z+pc
    print(f'n={n} nonzero={len(m)} zerozero={z} comm_nonzero={pc} commuting_total_including_zero={cp+2*len(m)+1} commuting_fraction={(cp+2*len(m)+1)/(len(m)+1)**2:.8f}')
print('VERIFY_OK: all ten small n; independent direct partial-map composition and exact zerozero count')
