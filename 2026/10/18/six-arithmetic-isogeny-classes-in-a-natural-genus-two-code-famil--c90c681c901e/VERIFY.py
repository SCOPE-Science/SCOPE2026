#!/usr/bin/env python3
"""Exact independent finite-field counts for a natural genus-two family."""
from collections import defaultdict
P=19
Q=P*P

def chi(v):
    v %= P
    if v == 0: return 0
    return 1 if pow(v,9,P)==1 else -1

def admissible(a):
    # Generic smoothness and absence of affine rational branch points.
    if a in (2, P-2): return False
    f=lambda x:(pow(x,6,P)+a*pow(x,3,P)+1)%P
    if any(f(x)==0 for x in range(P)): return False
    return 2*sum(chi(f(x)) == 1 for x in range(P))>0

def cubic_multiply(u,v):
    # F_{19^2}=F_19[w]/(w^2-2); 2 is a nonsquare modulo 19.
    return ((u[0]*v[0]+2*u[1]*v[1])%P,
            (u[0]*v[1]+u[1]*v[0])%P)

def power(u,k):
    res=(1,0)
    while k:
        if k&1:res=cubic_multiply(res,u)
        u=cubic_multiply(u,u)
        k >>= 1
    return res

def f2(a,x):
    u=power(x,3)
    v=cubic_multiply(u,u)
    return ((v[0]+a*u[0]+1)%P,(v[1]+a*u[1])%P)

def norm_chi(z):
    # In the quadratic extension, an element is a square iff its norm is a square.
    n=(z[0]*z[0]-2*z[1]*z[1])%P
    return chi(n)

a_values=[a for a in range(P) if admissible(a)]
assert a_values == [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
assert chi(2)==-1
classes=defaultdict(list)
for a in a_values:
    # Elliptic quotient E_a: w^2=(t+2)(t^3-3t+a).
    ne=P+2+sum(chi((t+2)*(t**3-3*t+a)) for t in range(P))
    tr=P+1-ne
    classes[tr].append(a)
    nc1=P+2+sum(chi(x**6+a*x**3+1) for x in range(P))
    nc2=Q+2+sum(norm_chi(f2(a,(u,v))) for u in range(P) for v in range(P))
    # Compare the two independent counting methods to the square of E's L-polynomial.
    assert nc1 == P+1-2*tr, (a,nc1,tr)
    assert nc2 == Q+1-2*(tr*tr-2*P), (a,nc2,tr)
    c=[1,-2*tr,tr*tr+2*P,-2*P*tr,P*P]
    assert sum(c)==ne*ne
    print('a=%02d E_points=%2d C(F19)=%2d C(F361)=%3d L=%s' %
          (a,ne,nc1,nc2,str(c)))
expected={-7:[7,12],-4:[5,14],-1:[9,10],2:[4,6,8,11,13,15],5:[3,16],8:[0]}
assert dict(classes)==expected, (dict(classes),expected)
assert len(classes)==6
print('TRACE_PARTITION:',dict(sorted(classes.items())))
print('VERIFY_OK')
