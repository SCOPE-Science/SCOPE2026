#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

# Exact arithmetic in Q(zeta_5), basis 1,z,z^2,z^3, z^4=-(1+z+z^2+z^3).
def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def neg(x): return tuple(-t for t in x)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    tmp=[Fraction(0) for _ in range(7)]
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            tmp[i+j]+=a*b
    # z^5=1, so reduce exponents >=5 first.
    for k in range(6,4,-1):
        if tmp[k]:
            tmp[k-5]+=tmp[k]
            tmp[k]=0
    # reduce z^4=-(1+z+z^2+z^3)
    t=tmp[4]
    if t:
        for i in range(4): tmp[i]-=t
        tmp[4]=0
    return tuple(tmp[:4])
def scale(q,x): return tuple(Fraction(q)*t for t in x)
def Z(n):
    n%=5
    if n<4:
        a=[Fraction(0)]*4; a[n]=Fraction(1); return tuple(a)
    return tuple(Fraction(-1) for _ in range(4))
ZERO=(Fraction(0),)*4
ONE=Z(0)

def evalP(coeff,i,j):
    a,b,c,d=coeff
    return add(add(a,mul(b,Z(i))),add(mul(c,Z(j)),mul(d,Z(i+j))))

def zeros(coeff):
    return {(i,j) for i in range(5) for j in range(5) if evalP(coeff,i,j)==ZERO}

def q(n): return scale(n,ONE)
z=Z(1); z2=Z(2); z3=Z(3)
minus1z=neg(add(ONE,z))
witness={
0:(q(1),q(-2),q(-2),q(4)),
1:(q(-2),q(-1),q(1),q(2)),
2:(minus1z,minus1z,minus1z,z3),
3:(minus1z,q(-1),z3,add(z2,z3)),
4:(minus1z,add(z,z3),add(ONE,z3),minus1z),
5:(q(1),q(-1),q(-2),q(2)),
9:(q(1),q(-1),q(-1),q(1)),
}
for expected,coef in witness.items():
    assert all(t!=ZERO for t in coef)
    zz=zeros(coef)
    assert len(zz)==expected,(expected,zz)
    print(f"witness_zero_count={expected} zeros={sorted(zz)}")

# Cross-ratio equality without division. A permutation sigma of five roots is
# Möbius-induced iff it preserves CR(0,1;2,j) for j=3,4.
def cross_equal(a,b,c,d,A,B,C,D):
    left=mul(mul(sub(a,c),sub(b,d)), mul(sub(A,D),sub(B,C)))
    right=mul(mul(sub(A,C),sub(B,D)), mul(sub(a,d),sub(b,c)))
    return left==right
pts=[Z(i) for i in range(5)]
valid=[]
for sig in permutations(range(5)):
    ok=True
    for j in (3,4):
        if not cross_equal(pts[0],pts[1],pts[2],pts[j],
                           pts[sig[0]],pts[sig[1]],pts[sig[2]],pts[sig[j]]):
            ok=False; break
    if ok: valid.append(sig)
assert len(valid)==10,len(valid)
for sig in valid:
    rot=any(all(sig[i]==(i+t)%5 for i in range(5)) for t in range(5))
    ref=any(all(sig[i]==(t-i)%5 for i in range(5)) for t in range(5))
    assert rot or ref,sig
print(f"mobius_permutations={len(valid)}")
print("VERIFY_OK")
