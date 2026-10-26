"""Exact polynomial certificate for the three-agent bi-layer voter dynamics.
Standard library only; independent of linear-equation solvers.
"""
from itertools import product

D = (754, 998, 473, 94, 6)  # increasing powers in gamma
N = {
    (0,1,0,2): (688,999,516,114,8),
    (0,1,1,1): (886,996,387,54,2),
    (0,1,2,0): (1112,965,234,14,0),
    (0,2,0,1): (1574,1995,903,168,10),
    (0,2,1,0): (1844,2090,668,48,0),
    (1,0,0,2): (418,904,751,234,18),
    (1,0,1,1): (566,981,612,154,12),
    (1,0,2,0): tuple(D),
    (1,1,0,1): (1376,1998,1032,228,16),
    (1,1,1,0): (1696,2013,807,128,6),
    (2,0,0,1): (1150,2029,1185,268,18),
    (2,0,1,0): tuple(2*x for x in D),
}
assert len(N)==12

def val(s):
    if s in N: return N[s]
    if s[0]+s[1]==3: return tuple(3*x for x in D)
    if s[2]+s[3]==3: return (0,)*5
    raise AssertionError('Unclassified state')

def changes(s):
    # State vector is (A+,A-,B+,B-). For each ordered focal/speaker
    # pair multiply rates by 6; this common factor cancels from harmonicity.
    for u in range(4):
        if not s[u]: continue
        for v in range(4):
            n=s[u]*(s[v] - (1 if u==v else 0))
            if n<=0: continue
            # First layer: copy tolerance, independent of opinion.
            dest=(u//2)*2+(v%2)
            if dest!=u:
                t=list(s);t[u]-=1;t[dest]+=1
                yield tuple(t), (n,0)
            # Second layer: copy a different opinion; switch to tolerant.
            if u//2!=v//2:
                dest=2*(v//2)
                t=list(s);t[u]-=1;t[dest]+=1
                yield tuple(t), ((n,0) if (u%2)==0 else (0,n))

def poly_harmonic(s):
    r=[0]*6
    fs=val(s)
    for t,(r0,r1) in changes(s):
        ft=val(t)
        for j in range(5):
            r[j]+=r0*(ft[j]-fs[j])
            r[j+1]+=r1*(ft[j]-fs[j])
    return tuple(r)

for s in N:
    assert poly_harmonic(s)==(0,)*6,(s,poly_harmonic(s))
# Main inequality in the positive gamma interval:
# P(A consensus)-2/3=(1-gamma)*(66+65gamma+22gamma^2+2gamma^3)/(3D)
main=N[(0,2,0,1)]
diff=tuple(main[j]-2*D[j] for j in range(5))
assert diff==(66,-1,-43,-20,-2)
# multiplication (1-gamma)*(66+65g+22g^2+2g^3)
p=[66,65,22,2]
c=[p[0]]+[p[j]-p[j-1] for j in range(1,4)]+[-p[-1]]
assert tuple(c)==diff
# gamma=1 is the ordinary voter model:
assert sum(main)==2*sum(D)
# zero-side endpoint:
from fractions import Fraction
assert Fraction(main[0],3*D[0])==Fraction(787,1131)
assert Fraction(787,1131)-Fraction(2,3)==Fraction(11,377)
print('PASS: all twelve harmonic equations as polynomial identities')
print('PASS: absorption boundary values, strict majority gain factorization')
print('PASS: classical gamma=1 and gamma->0+ boundary fractions')
