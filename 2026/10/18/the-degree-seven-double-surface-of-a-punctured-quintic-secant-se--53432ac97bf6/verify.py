"""Reproducible exact checks for the omitted-quadratic monomial-quintic secant.
Scientific content only. Requires sympy >= 1.12. Execute: python verify.py.
Finite-field tests corroborate, but do not replace, the symbolic proof.
"""
import itertools
from math import prod
import sympy as s

a,b,c,d,e,y=s.symbols('a b c d e y')
vars=(a,b,c,d,e)
H=s.Matrix([[a,b,y,c],[b,y,c,d],[y,c,d,e]])
f=[s.expand(H[:,t].det()) for t in itertools.combinations(range(4),3)]
assert len(f)==4
F=s.cancel(s.resultant(f[1],f[2],y)/(a*d-b*c))
assert s.Poly(F,*vars).total_degree()==6
assert len(s.Poly(F,*vars).terms())==13
G1=b*e**2+c**2*e-2*c*d**2
G2=a*e**2+b*d*e-2*c**2*d
G3=d*(a*e+b*d)-c*(b*e+c**2)
w,z=s.symbols('w z')
sub={a:w-b*d+2*c*c*d, b:z+c*(2*d*d-c)}
# Perform sequential substitutions to avoid ambiguity in triangular coordinate change.
form=s.expand(F.subs(e,1).subs(a,w-b*d+2*c*c*d).subs(b,z+c*(2*d*d-c)))
assert s.factor(form-(c-d**2)*(w**2+2*c*z**2)+z**3)==0
assert s.factor(F.subs(e,0))==s.factor(4*a*c*c*d**3-b*b*d**4-4*b*c**3*d*d+c**6)
# Gradient on the infinite hyperplane.
assert s.factor(s.diff(F,a).subs(e,0)-4*c**2*d**3)==0
assert s.factor(s.diff(F,b).subs(e,0)+2*d*d*(b*d*d+2*c**3))==0
assert s.factor(s.diff(F,c).subs({e:0,d:0})-6*c**5)==0
# Affine graph and determinantal boundary equations.
A=c*d*(3*c-2*d**2)
B=c*(2*d*d-c)
assert all(s.expand(G.subs({a:A,b:B,e:1}))==0 for G in (G1,G2,G3))
assert s.expand(e*G3-d*G2+c*G1)==0
# Verify the full parametrization of the secant curve: two affine points and weights.
t,u,L,M=s.symbols('t u L M')
sec={a:L+M,b:L*t+M*u,c:L*t**3+M*u**3,d:L*t**4+M*u**4,e:L*t**5+M*u**5}
assert s.expand(F.subs(sec))==0
# Generic slice: one of the two defining cubics and another general cubic give exactly seven points.
f1=s.expand(G1.subs(e,1));f2=s.expand(G2.subs(e,1));
H1=A+2*B+3*c+5*d+7;H2=2*A+3*B+5*c+7*d+11
GB=s.groebner([H1,H2],d,c,order='lex')
assert len(GB.polys)==2
upoly=next(p for p in GB.polys if p.as_expr().free_symbols=={c})
assert s.Poly(upoly.as_expr(),c).degree()==7
assert s.gcd(upoly.as_expr(),s.diff(upoly.as_expr(),c))==1
# Generic transverse quadratic at (c,d)=(2,0): h=2, Hessian in (w,z) nonsingular.
Hess=s.hessian((c-d**2)*(w**2+2*c*z**2)-z**3,(w,z))
assert s.det(Hess.subs({w:0,z:0,c:2,d:0}))==64
# Independent finite-field singular support checks.
terms=[[ (int(coeff),powers) for powers,coeff in s.Poly(q,*vars).terms()]
       for q in [F]+[s.diff(F,v) for v in vars]+[G1,G2,G3]]
def pe(poly,point,p):
    return sum(coeff*prod(pow(x,n,p) for x,n in zip(point,powers)) for coeff,powers in poly)%p
def projective_points(p):
    for pos in range(5):
        for rest in itertools.product(range(p),repeat=4-pos):
            yield (0,)*pos+(1,)+rest
for prime,expect in ((5,36),(7,64),(11,144)):
    n_sing=n_D=0
    for point in projective_points(prime):
        sing=all(pe(q,point,prime)==0 for q in terms[:6])
        lies=all(pe(q,point,prime)==0 for q in terms[6:])
        assert sing==lies, (prime,point,sing,lies)
        n_sing+=sing;n_D+=lies
    assert (n_sing,n_D)==(expect,expect)
print('VERIFY_OK: sextic resultant, coordinate normal form, graph, boundary, degree-seven slice, transverse Hessian, and finite fields 5,7,11')
