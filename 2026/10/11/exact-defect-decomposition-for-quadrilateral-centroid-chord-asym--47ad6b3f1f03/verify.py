"""Symbolic replay for the quadrilateral centroid-chord defect identity.
Requires SymPy.
"""
import sympy as s

u,v=s.symbols('u v', positive=True)
x=(1+u)/(1-u)
y=(1+v)/(1-v)
A=s.Matrix([-1,0]); B=s.Matrix([0,1]); C=s.Matrix([x,0]); Dv=s.Matrix([0,-y])
V=[A,B,C,Dv]
G=s.Matrix([(x-1)/3,(1-y)/3])

def point(i,t):
    return V[i]+t*(V[(i+1)%4]-V[i])

def chord(i,j):
    a,b=s.symbols(f'a{i}{j} b{i}{j}')
    P=point(i,a); Q=point(j,b)
    sol=s.solve(list(P+Q-2*G),(a,b), dict=True)[0]
    return s.simplify(sol[a]),s.simplify(sol[b]),s.simplify(P.subs(a,sol[a])),s.simplify(Q.subs(b,sol[b]))

def cross(P,Q): return s.expand(P[0]*Q[1]-P[1]*Q[0])
def area(poly):
    return s.simplify(sum(cross(poly[k],poly[(k+1)%len(poly)]) for k in range(len(poly)))/2)
Atot=s.simplify(area(V))
assert s.simplify(Atot+(1+x)*(1+y)/2)==0

# The four edge-pairs used in the two moduli chambers.
sol={}
for ij in [(1,2),(1,3),(0,2),(2,3)]:
    sol[ij]=chord(*ij)

# Directed boundary-side areas from the first point through successive vertices to the second.
def side_fraction(i,j,P,Q):
    assert i < j
    poly=[P] + V[i+1:j+1] + [Q]
    return s.factor(s.together(area(poly)/Atot))

f12=side_fraction(1,2,sol[(1,2)][2],sol[(1,2)][3])
f13=side_fraction(1,3,sol[(1,3)][2],sol[(1,3)][3])
f02=side_fraction(0,2,sol[(0,2)][2],sol[(0,2)][3])
f23=side_fraction(2,3,sol[(2,3)][2],sol[(2,3)][3])

D=u**2*v**2-u**2-u*v+9*u-v**2+9*v
amin=(3+u+v-u*v)*(3+u-v+u*v)/(18*(1+u))
amax=D/(18*(u+v))
a02=(u**2*v**2-u**2+u*v+9*u-v**2-9*v)/(18*(u-v))
a23=(3+u+v-u*v)*(3-u+v+u*v)/(18*(1+v))

assert s.factor(s.together(f12-amin))==0
assert s.factor(s.together((1-f13)-amax))==0
assert s.factor(s.together((1-f02)-a02))==0
assert s.factor(s.together(f23-a23))==0

rho=s.factor(s.together(amin/amax))
Bdef=17*u**2+10*u*v+6*u+9-u**2*v-9*v
rhs=(7*u-3)**2/(25*(9-u)*(1+u)) + v**2*(1-u)*Bdef/((9-u)*(1+u)*D)
assert s.factor(s.together(rho-s.Rational(24,25)-rhs))==0
assert s.factor(s.together(rho.subs(v,0)-(u+3)**2/((9-u)*(1+u))))==0

# Difference factorizations used for ordering the three chord fractions.
assert s.factor(s.together(amax-a02) - v**3*(1-u)*(1+u)/(9*(u-v)*(u+v)))==0
E=2*u**2*v-2*u**2-u*v**2+2*u*v+v**2
assert s.factor(s.together(a02-amin) - (u-1)*(v+1)*E/(18*(u+1)*(u-v)))==0
assert s.factor(s.together(a23-amin) + (u-1)*(u-v)*(v-1)*(u*v-u-v-3)/(18*(u+1)*(v+1)))==0
F=u**2*v-u**2+2*u*v**2+2*u*v+2*v**2
assert s.factor(s.together(amax-a23) - (u-1)*(v-1)*F/(18*(u+v)*(v+1)))==0

print('VERIFY_OK')
print('total_area=', s.factor(Atot))
print('rho=', rho)
print('defect_identity=', s.factor(s.together(rhs)))
