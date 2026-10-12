"""Exact verification of an integer-matrix SCRK row-choice reversal.
Run: python verify.py  (requires sympy)
"""
import sympy as sp

A = sp.Matrix([[-2, -1, 3], [-1, 0, -3], [0, -2, 1]])
assert A.det() == 17
assert A*A.T == sp.Matrix([[14,-7,5],[-7,10,-3],[5,-3,5]])
rows = A.rows
values = []
for i in range(rows):
    a = A.row(i).T
    P = sp.eye(3)-a*a.T/a.dot(a)
    j,k = [h for h in range(rows) if h != i]
    u = P*A.row(j).T
    v = P*A.row(k).T
    aa,bb,d = u.dot(u), v.dot(v), u.dot(v)
    p=sp.factor(aa/(aa+bb)); q=1-p
    z=sp.factor(d*d/(aa*bb))
    T=P-u*u.T/aa
    U=P-v*v.T/bb
    assert T*T==T and U*U==U and T*U*T==z*T and U*T*U==z*U
    a2=sp.factor(p*p+p*q*z); b2=sp.factor(q*q+p*q*z)
    M1=p*T+q*U
    M2=p*p*T+p*q*(T*U*T)+p*q*(U*T*U)+q*q*U
    assert M2==a2*T+b2*U
    assert sp.trace(M1)==1 and sp.trace(M2)==a2+b2
    assert sp.simplify((sp.trace(M1)**2-sp.trace(M1*M1))/2-p*q*(1-z))==0
    assert sp.simplify((sp.trace(M2)**2-sp.trace(M2*M2))/2-a2*b2*(1-z))==0
    L1=sp.simplify((1+sp.sqrt(1-4*p*q*(1-z)))/2)
    L2=sp.simplify((a2+b2+sp.sqrt((a2-b2)**2+4*a2*b2*z))/2)
    rho=sp.simplify((1+sp.sqrt((p-q)**2+4*p*q*z*z))/2)
    assert sp.simplify(sp.det(sp.Matrix([[p,p*z],[q*z,q]])-sp.eye(2)*rho))==0
    values.append((L1,L2,rho))
    print('row',i+1,'p',p,'z',z,'L1',L1,'L2',L2,'rho',rho)

def inside_with_exact_sqrt(expr,low,high):
    # For these positive real quadratic radicals, the inequalities are decidable.
    assert bool(sp.simplify(expr-low)>0), (expr,low)
    assert bool(sp.simplify(high-expr)>0), (expr,high)

# Rational strict enclosures, not merely decimal floating approximations.
for (L1,L2,rho), (u1,v1,u2,v2,u3,v3) in zip(values,[
    (6767,6768,4521,4522,6692,6693),
    (7900,7901,5642,5643,7162,7163),
    (7337,7338,4479,4480,6107,6108),
]):
    inside_with_exact_sqrt(L1,sp.Rational(u1,10000),sp.Rational(v1,10000))
    inside_with_exact_sqrt(L2,sp.Rational(u2,10000),sp.Rational(v2,10000))
    inside_with_exact_sqrt(rho,sp.Rational(u3,10000),sp.Rational(v3,10000))
assert values[0][0]<values[2][0]<values[1][0]
assert values[2][1]<values[0][1]<values[1][1]
assert values[2][2]<values[0][2]<values[1][2]
print('VERIFY_OK')
