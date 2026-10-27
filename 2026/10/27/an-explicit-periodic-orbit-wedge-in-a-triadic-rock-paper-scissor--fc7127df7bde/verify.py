"""Exact algebraic checks for a cyclic pairwise-plus-triadic replicator."""
import sympy as S

a, b, alpha, beta = S.symbols('a b alpha beta', real=True)
x, y, z = S.symbols('x y z', real=True)
u, v = S.symbols('u v')
X = S.Matrix([x,y,z])
P = S.Matrix([[0,-b-1,a+1],[a+1,0,-b-1],[-b-1,a+1,0]])
T = [
 S.Matrix([[0,-(b+1)/2,(a+1)*beta/2],[-(b+1)/2,-b-1,0],[(a+1)*beta/2,0,(a+1)*alpha]]),
 S.Matrix([[(a+1)*alpha,(a+1)*beta/2,0],[(a+1)*beta/2,0,-(b+1)/2],[0,-(b+1)/2,-b-1]]),
 S.Matrix([[-b-1,0,-(b+1)/2],[0,(a+1)*alpha,(a+1)*beta/2],[-(b+1)/2,(a+1)*beta/2,0]])]
f = [(P*X)[i]+(X.T*T[i]*X)[0] for i in range(3)]
means = sum(X[i]*f[i] for i in range(3))
phi = [S.expand((X[i]*(f[i]-means)).subs(z,1-x-y)) for i in range(2)]
J = S.Matrix(phi).jacobian([x,y]).subs({x:S.Rational(1,3),y:S.Rational(1,3)})
expected_trace = (1+4*b+beta-2*alpha-a*(3+2*alpha-beta))/9
assert S.simplify(J.trace()-expected_trace)==0

omega = (-1+S.I*S.sqrt(3))/2
A, B = a+1,b+1
K = A*(-alpha/S.Integer(3)+beta/S.Integer(6)-S.Rational(1,2) + S.I*S.sqrt(3)*(alpha/S.Integer(3)+beta/S.Integer(6)+S.Rational(1,2)))+B*(S.Rational(2,3)+S.I*S.sqrt(3))
L = A*(-(alpha+beta)/6+S.I*S.sqrt(3)*(alpha-beta)/6)+B/3
inverse = {x:(1+u+v)/3,y:(1+omega**2*u+omega*v)/3,z:(1+omega*u+omega**2*v)/3}
W = f[0]+omega*f[1]+omega**2*f[2]
assert S.simplify(S.expand_complex(S.expand(W.subs(inverse, simultaneous=True)-K*u-L*v**2)))==0
K2 = S.simplify(S.expand_complex(K*S.conjugate(K)))
L2 = S.simplify(S.expand_complex(L*S.conjugate(L)))
positive_gap=(A**2*(alpha**2+alpha*beta+4*alpha+beta+3)+A*B*(5*alpha+4*beta+7)+10*B**2)/3
assert S.simplify(K2-L2-positive_gap)==0
assert S.simplify(J.det()-K2/9)==0

# On the edge z=0, the first species' fitness is always lower than the second's.
edge_difference=-2*(b+1)*(1-x)-(a+1)*x*(1+alpha*x+beta*(1-x))
assert S.simplify((f[0]-f[1]).subs({z:0,y:1-x})-edge_difference)==0

astar=(1+4*b+beta-2*alpha)/(3+2*alpha-beta)
abound=(2*b+1-alpha)/(alpha+1)
assert S.simplify(abound-astar-2*(b+1)*(1-beta)/((alpha+1)*(3+2*alpha-beta)))==0
p={a:S.Rational(1,4),b:1,alpha:2,beta:S.Rational(1,2)}
assert astar.subs(p)==S.Rational(3,13)
assert abound.subs(p)==S.Rational(1,3)
assert astar.subs(p)<p[a]<abound.subs(p)
assert J.subs(p).eigenvals()=={-S.Rational(1,144)-S.I*19*S.sqrt(3)/16:1, -S.Rational(1,144)+S.I*19*S.sqrt(3)/16:1}
assert 2*(p[b]+1)>(p[a]+1)*(1+p[alpha])
print('EXACT_SYMBOLIC_IDENTITIES_OK')
