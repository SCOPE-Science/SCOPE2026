#!/usr/bin/env python3
"""Exact symbolic and finite-parameter checks of quadratic star-graph tip kernels."""
import sympy as S

x,y,t=S.symbols('x y t', real=True)
q=lambda z:1-4*z+S.Rational(10,3)*z*z
K0=lambda a,b:48*a*b-60*(a*b*b+a*a*b)+80*a*a*b*b
qroots=S.solve(q(y),y)
assert qroots==[S.Rational(3,5)-S.sqrt(6)/10,S.Rational(3,5)+S.sqrt(6)/10]
Q=S.simplify(S.integrate(q(y),(y,0,qroots[0]))-S.integrate(q(y),(y,qroots[0],qroots[1]))+S.integrate(q(y),(y,qroots[1],1)))
assert S.simplify(Q-(S.Rational(1,9)+4*S.sqrt(6)/75))==0
assert S.integrate(q(y)**2,(y,0,1))==S.Rational(1,9)
for j in [1,2]:
    assert S.integrate(q(y)*y**j,(y,0,1))==0
G=S.Matrix([[S.Rational(1,3),S.Rational(1,4)],[S.Rational(1,4),S.Rational(1,5)]])
assert G.inv()==S.Matrix([[48,-60],[-60,80]])
assert S.expand(K0(x,y)-S.Matrix([[x,x*x]])[0,:].dot(G.inv()*S.Matrix([y,y*y])))==0
p=S.expand(K0(1,y)+3*t*q(y))
assert S.expand(p-(10*(2+t)*y*y-12*(1+t)*y+3*t))==0
D=S.discriminant(p,y); A=10*(2+t)
assert S.expand(D-24*(t*t+2*t+6))==0
assert S.simplify(S.integrate(p,(y,0,1))-(S.Rational(2,3)+t/3))==0
I=S.Rational(2,3)+t/3+D**S.Rational(3,2)/(3*A**2)
E=S.Integer(1)+4*S.sqrt(6)/25*(1-t+(t*t+2*t+6)**S.Rational(3,2)/(2+t)**2)
assert S.simplify(E-(I+3*(1-t)*Q))==0
assert S.simplify(E.subs(t,1)-(1+12*S.sqrt(6)/25))==0
assert S.simplify(S.limit(E,t,0)-(61+4*S.sqrt(6))/25)==0
assert S.simplify(S.limit(-S.diff(E,t),t,0)-(18+4*S.sqrt(6))/25)==0
assert S.simplify(S.Rational(5,2)-E.subs(t,S.Rational(1,2))).is_positive
assert S.simplify(E.subs(t,S.Rational(1,3))-S.Rational(5,2)).is_positive
h=(t*t+2*t+6)**S.Rational(3,2)/(2+t)**2
assert S.simplify(S.diff(h,t)-(t-1)*(t+6)*S.sqrt(t*t+2*t+6)/(t+2)**3)==0

# Independent Gram matrix inversion uses the original monomial basis,
# not the orthogonal decomposition used to derive the theorem.
checks=0
for k in list(range(1,17))+[25,40]:
    basis=[(i,r) for i in range(k) for r in (1,2)]
    n=1+len(basis)
    mat=S.zeros(n)
    mat[0,0]=k
    for a,(i,r) in enumerate(basis,1):
        mat[0,a]=mat[a,0]=S.Rational(1,r+1)
        for b,(j,s) in enumerate(basis,1):
            if i==j: mat[a,b]=S.Rational(1,r+s+1)
    inv=mat.inv()
    # kernel at first arm tip versus each source edge
    for j in range(k):
        ev=S.Matrix([1]+[int(i==0) for (i,r) in basis])
        vv=S.Matrix([1]+[y**r if i==j else 0 for (i,r) in basis])
        kernel=S.expand((ev.T*inv*vv)[0])
        expected=S.expand((K0(1,y) if j==0 else 0)+S.Rational(3,k)*q(y))
        assert S.simplify(kernel-expected)==0
        checks+=1
    # Discriminant root ordering, signed integral, reproduction and exact negativity
    tt=S.Rational(1,k)
    polynomial=S.expand(p.subs(t,tt))
    roots=S.solve(polynomial,y)
    assert len(roots)==2 and 0 < roots[0].evalf() < S.Rational(1,2) < roots[1].evalf() < 1
    exact_same=S.simplify(S.integrate(polynomial,(y,0,roots[0]))-S.integrate(polynomial,(y,roots[0],roots[1]))+S.integrate(polynomial,(y,roots[1],1)))
    assert S.simplify(exact_same-I.subs(t,tt))==0
    assert S.simplify(exact_same+3*(1-tt)*Q-E.subs(t,tt))==0
    assert S.simplify(S.integrate(polynomial,(y,0,1))+(k-1)*3*tt*S.integrate(q(y),(y,0,1))-1)==0
    assert S.N(E.subs(t,tt),40)>0
    checks+=5
print(f'PASS: symbolic kernel, signed-integral, monotonicity, limit identities; {checks} independent Gram/kernel/root identities on 18 stars.')
