"""Exact algebraic checks for the full-branch triangular tent map.
Requires SymPy. It verifies polynomial identities and finite lag formulas,
not the general martingale CLT or publication priority.
"""
import sympy as s
x,y,u,v=s.symbols('x y u v', real=True)
q=s.Matrix([x-1,y-s.Rational(1,3)])
left=s.Matrix([x+y,x-y]); right=s.Matrix([2-x+y,2-x-y])
a=s.Matrix([(u+v)/2,(u-v)/2]); b=s.Matrix([2-(u+v)/2,(u-v)/2])
assert s.simplify(left.subs({x:a[0],y:a[1]}, simultaneous=True)-s.Matrix([u,v]))==s.zeros(2,1)
assert s.simplify(right.subs({x:b[0],y:b[1]}, simultaneous=True)-s.Matrix([u,v]))==s.zeros(2,1)
for row in (left,right):
    assert s.expand(row[0]-row[1]-2*y)==0
assert (left.jacobian([x,y]).det(),right.jacobian([x,y]).det())==(-2,2)
def integral(z):
    return s.simplify(s.integrate(s.integrate(z,(y,0,x)),(x,0,1)) +
        s.integrate(s.integrate(z,(y,0,2-x)),(x,1,2)))
def P(f):
    f=s.sympify(f)
    expr=(f.subs({x:a[0],y:a[1]}, simultaneous=True)+f.subs({x:b[0],y:b[1]}, simultaneous=True))/2
    return s.expand(expr.subs({u:x,v:y}, simultaneous=True))
assert integral(1)==1
assert integral(x)==1 and integral(y)==s.Rational(1,3)
assert P(1)==1
assert s.expand(P(q[0]))==0
assert s.expand(P(q[1])-(q[0]-q[1])/2)==0
C=s.simplify(s.Matrix(2,2,lambda i,j:integral(q[i]*q[j])))
assert C==s.diag(s.Rational(1,6),s.Rational(1,18))
pows=[q]
for n in range(1,25):
    prev=pows[-1]
    powers=s.Matrix([P(prev[0]),P(prev[1])])
    pows.append(powers)
    assert s.expand(powers[0])==0
    assert s.expand(powers[1]-(-s.Rational(1,2))**(n-1)*(q[0]-q[1])/2)==0
    lag=s.Matrix(2,2,lambda i,j:integral(powers[i]*q[j]))
    expected=s.Matrix([[0,0],[(-s.Rational(1,2))**(n-1)/12,(-s.Rational(1,2))**n/18]])
    assert lag==expected
    print('lag',n,lag.tolist()) if n in (1,2,3,24) else None
Sigma=C+s.Matrix([[0,s.Rational(1,18)],[s.Rational(1,18),-s.Rational(1,27)]])
assert Sigma==s.Matrix([[s.Rational(1,6),s.Rational(1,18)],[s.Rational(1,18),s.Rational(1,54)]])
assert Sigma.det()==0 and Sigma*s.Matrix([1,-3])==s.zeros(2,1)
H=x-y
for row in (left,right):
    assert s.expand(H-(H.subs({x:row[0],y:row[1]},simultaneous=True))-(x-3*y))==0
print('PASS inverse branches, full-branch Jacobians, invariant moments, exact transfer, 24 lag covariances, rank-one Green-Kubo, and sharp coboundary identity')
