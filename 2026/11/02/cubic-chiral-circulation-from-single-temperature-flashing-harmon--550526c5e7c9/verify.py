"""Exact checks for angular circulation in a two-state flashing harmonic trap.
Run with Python 3, standard library only.
"""
from fractions import Fraction as F
from itertools import product

def solve(A, rhs):
    rows = [[F(t) for t in r]+[F(rhs[i])] for i,r in enumerate(A)]
    n=len(rows)
    for k in range(n):
        piv=next(i for i in range(k,n) if rows[i][k])
        rows[k], rows[piv]=rows[piv], rows[k]
        f=rows[k][k]
        rows[k]=[v/f for v in rows[k]]
        for j in range(n):
            if j==k: continue
            q=rows[j][k]
            rows[j]=[rows[j][s]-q*rows[k][s] for s in range(n+1)]
    return [r[-1] for r in rows]

def exact_moments(a,b,c,l,T):
    p=a+b
    M=[[F(0) for _ in range(6)] for _ in range(6)]
    M[0][0]=2*a+l;M[0][3]=-l
    M[1][1]=2*b+l;M[1][4]=-l
    M[2][2]=p+l;M[2][5]=-l
    M[3][0]=-l;M[3][3]=2*a+l;M[3][5]=2*c
    M[4][1]=-l;M[4][4]=2*b+l;M[4][5]=2*c
    M[5][2]=-l;M[5][3]=c;M[5][4]=c;M[5][5]=p+l
    return solve(M,[T,T,0,T,T,0])

def theorem(a,b,c,l,T):
    p=a+b;Q=(a+l)*(b+l)
    H=p/(2*a*b)+(p+2*l)/(2*Q)
    R=p*(p+2*l)-c*c*(p+l)*H
    return -T*c**3*(a-b)*l*(p+l)/(2*a*b*Q*R)

def integral_current(a,b,c,S):
    x0,y0,z0,x1,y1,z1=S
    return (a-b)*(z0+z1)-c*(x1-y1)

checks=0
for a,b in [(F(2),F(1)),(F(3),F(1)),(F(5),F(2)),(F(2),F(2)),(F(3),F(5))]:
    for c in [F(-1),F(-1,2),F(1,4),F(1,2),F(1)]:
        if c*c>=a*b: continue
        for l,T in product([F(1,5),F(1,2),F(1),F(3),F(10)],[F(1),F(5,3)]):
            S=exact_moments(a,b,c,l,T)
            w=integral_current(a,b,c,S)
            assert w==theorem(a,b,c,l,T),(a,b,c,l,T,S,w,theorem(a,b,c,l,T))
            checks+=1

# Canonical example; algebraic exactness and two independent limit checks.
a=F(2);b=F(1);c=T=F(1)
for l in [F(1,10),F(1,3),F(1),F(7),F(100)]:
    assert theorem(a,b,c,l,T)==-l*(l+3)/(21*l**3+86*l*l+105*l+36)
    checks+=1
# Derivative numerator has one positive root by Descartes' rule and changes signs.
def poly(l): return 7*l**4+42*l**3+51*l*l-24*l-36
assert poly(F(0))<0 and poly(F(1))>0
lo=F(0);hi=F(1)
for _ in range(80):
    m=(lo+hi)/2
    if poly(m)>0: hi=m
    else: lo=m
assert abs(float((lo+hi)/2)-0.787960172311017)<1e-12
checks+=4
# Positivity proof cross-check at rational samples.
for a,b in [(F(2),F(1)),(F(3),F(5))]:
    for l in [F(0),F(1,7),F(1),F(10)]:
        p=a+b;Q=(a+l)*(b+l)
        H=p/(2*a*b)+(p+2*l)/(2*Q)
        P=2*Q*(p*(p+2*l)-a*b*(p+l)*H)
        RHS=l*(p**3+(4*a*a+6*a*b+4*b*b)*l+3*p*l*l)
        assert P==RHS and P>=0
        checks+=1
print('PASS:',checks,'exact rational assertions; canonical optimum',float((lo+hi)/2))
