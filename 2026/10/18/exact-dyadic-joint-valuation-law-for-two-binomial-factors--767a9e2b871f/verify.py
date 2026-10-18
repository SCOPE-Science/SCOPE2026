#!/usr/bin/env python3
"""Exact elementary checks for a dyadic bivariate binomial valuation law.

Uses only the Python standard library. Run: python3 verify.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb

ZERO = {}
ONE = {(0, 0, 0): 1}

def mon(c=1, u=0, v=0, z=0):
    return {(u, v, z): c} if c else {}

def add(*polys):
    t = defaultdict(int)
    for p in polys:
        for a, c in p.items():
            t[a] += c
    return {a:c for a,c in t.items() if c}

def neg(p):
    return {a:-c for a,c in p.items()}

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    t=defaultdict(int)
    for (i,j,k),x in a.items():
        for (r,s,w),y in b.items():
            t[(i+r,j+s,k+w)] += x*y
    return {a:c for a,c in t.items() if c}

def powpoly(a,n):
    out=ONE
    for _ in range(n):out=mul(out,a)
    return out

def det(mat):
    total=ZERO
    for perm in permutations(range(len(mat))):
        inv=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        term=ONE
        for i,j in enumerate(perm):term=mul(term,mat[i][j])
        total=add(total,neg(term) if inv%2 else term)
    return total

def deriv(poly,which):
    out=defaultdict(int)
    for e,c in poly.items():
        if e[which]:
            q=list(e);q[which]-=1
            out[tuple(q)] +=c*e[which]
    return dict(out)

def uv_one(poly):
    out=defaultdict(int)
    for (a,b,c),d in poly.items():out[(0,0,c)]+=d
    return {a:v for a,v in out.items() if v}

def zpoly(*cs):
    return { (0,0,i):v for i,v in enumerate(cs) if v}

u=mon(u=1);v=mon(v=1);z=mon(z=1)
uv=mul(u,v)
M=[[ONE,ZERO,u,ZERO],
   [ONE,ZERO,ZERO,uv],
   [ONE,ZERO,ZERO,uv],
   [ZERO,v,ZERO,uv]]
f=[ONE,ONE,ONE,v]
A=[[sub(ONE if i==j else ZERO,mul(z,M[i][j])) for j in range(4)] for i in range(4)]
B=[[f[i] if j==0 else A[i][j] for j in range(4)] for i in range(4)]
D=det(A); N=det(B)
expected_D=add(ONE,neg(z),neg(mul(pw:=powpoly(z,2),u)),neg(mul(mul(uv,z),ONE)),mul(mul(uv,pw),ONE),neg(mul(mul(u,powpoly(v,2)),pw)),mul(mul(powpoly(u,2),v),powpoly(z,3)),mul(mul(u,powpoly(v,2)),powpoly(z,3)))
# Above terms include -u*z^2 and -u*v*z as separate summands.
expected_N=add(ONE,mul(u,z),neg(mul(uv,z)),mul(mul(powpoly(u,2),powpoly(v,2)),powpoly(z,2)),neg(mul(mul(powpoly(u,2),v),powpoly(z,2))),neg(mul(mul(u,powpoly(v,2)),powpoly(z,2))))
assert D == expected_D,(D,expected_D)
assert N == expected_N,(N,expected_N)

# Setting u=1 recovers the previously known marginal enumerator for Y.
def u_one(poly):
    t=defaultdict(int)
    for (a,b,c),d in poly.items():t[(0,b,c)]+=d
    return {a:v for a,v in t.items() if v}
expected_marg_num=mul(add(ONE,z),sub(ONE,mul(v,z)))
expected_marg_den=add(ONE,neg(mul(add(ONE,v),z)),
                      neg(mul(add(ONE,neg(v),powpoly(v,2)),powpoly(z,2))),
                      mul(mul(v,add(ONE,v)),powpoly(z,3)))
assert u_one(N)==expected_marg_num
assert u_one(D)==expected_marg_den

def rational_derivative(which):
    return sub(mul(deriv(N,which),D),mul(N,deriv(D,which))),powpoly(D,2)
Nu=deriv(N,0);Nv=deriv(N,1); Nuv=deriv(Nv,0)
Du=deriv(D,0);Dv=deriv(D,1);Duv=deriv(Dv,0)
Ru,Qu=rational_derivative(0)
Rv,Qv=rational_derivative(1)
Ruv=add(mul(Nuv,powpoly(D,2)),neg(mul(Nu,mul(D,Dv))),neg(mul(Nv,mul(D,Du))),neg(mul(N,mul(D,Duv))),mul(mon(c=2),mul(N,mul(Du,Dv))))
Quv=powpoly(D,3)
# Verify closed derivative generating functions by cross multiplication at u=v=1.
q2=zpoly(1,-2);qm=zpoly(-1,1);qp=zpoly(1,1)
assert mul(uv_one(Ru),powpoly(q2,2)) == mul(uv_one(Qu), z)
assert mul(uv_one(Rv),mul(mul(qm,qp),powpoly(q2,2))) == mul(uv_one(Qv),mul(zpoly(0,0,1),zpoly(-2,1)))
expect_cross_num=mul(zpoly(0,0,1),zpoly(-4,7,-2,-2,2))
expect_cross_den=neg(mul(mul(powpoly(qm,2),powpoly(qp,2)),powpoly(q2,3)))
assert mul(uv_one(Ruv),expect_cross_den) == mul(uv_one(Quv),expect_cross_num)

# Direct enumeration of coefficients, independent of carry automaton.
for L in range(0,10):
    tally=defaultdict(int)
    sx=sy=sxy=0
    for n in range(1<<L):
        x=n.bit_count()
        y=(n.bit_count() + (2*n).bit_count() - (3*n).bit_count())
        # Kummer's digit-sum form: nu_2(C(3n,n)) = s_2(n)+s_2(2n)-s_2(3n).
        if L<=8:
            val=comb(3*n,n)
            direct=(val & -val).bit_length()-1
            assert y == direct,(L,n,y,direct)
        tally[(x,y)] +=1
        sx+=x;sy+=y;sxy+=x*y
    # Independently construct the automaton enumerator P_L.
    states={(0,0):{(0,0):1}}
    for _ in range(L):
        out=defaultdict(lambda:defaultdict(int))
        for (p,c),d in states.items():
            for (ex,ey),cnt in d.items():
                for bit in (0,1):
                    cc=(bit+p+c)//2
                    out[(bit,cc)][(ex+bit,ey+cc)] += cnt
        states=out
    check=defaultdict(int)
    for (p,c),d in states.items():
        for (ex,ey),cnt in d.items():
            check[(ex,ey+(p+c)//2)] += cnt
    assert dict(tally) == dict(check),(L,tally,check)
    m=1<<L
    expected_y=Fraction(L,2)-Fraction(2,3)+Fraction(3+(-1)**L,6*m)
    expected_cov=Fraction(5*L,12)-Fraction(4,9)+Fraction(9+7*(-1)**L,36*m)
    actual_cov=Fraction(sxy,m)-Fraction(sx*sy,m*m)
    assert Fraction(sx,m)==Fraction(L,2)
    assert Fraction(sy,m)==expected_y,(L,Fraction(sy,m),expected_y)
    assert actual_cov==expected_cov,(L,actual_cov,expected_cov)
print('VERIFY_OK: exact 4x4 determinant/resolvent, rational derivatives, binary enumeration and exact moments (L=0..9)')
