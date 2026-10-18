"""Exact and finite-field checks for the cubic symmetric permanent singular schemes."""
from itertools import product
from math import comb, factorial
import sympy as s

a,b,c,d,e,f=s.symbols('a b c d e f')
P=a*b*c+a*f**2+b*e**2+c*d**2+2*d*e*f
x=(a,b,c,d,e,f)
grad=tuple(s.diff(P,z) for z in x)
assert grad == (b*c+f**2,a*c+e**2,a*b+d**2,2*c*d+2*e*f,2*b*e+2*d*f,2*a*f+2*d*e)

# Exact odd-characteristic affine-chart elimination, over Z[1/2].
sub={a:1,b:-d**2,c:-e**2,f:-d*e}
assert tuple(s.expand(v.subs(sub, simultaneous=True)) for v in grad)==(
    2*d**2*e**2,0,0,-4*d*e**2,-4*d**2*e,0)
assert s.expand(P.subs(sub, simultaneous=True)) == -2*d**2*e**2
# Characteristic two: eliminate b,c; f=de+u leaves a square-zero parameter.
u=s.Symbol('u')
sub2={a:1,b:d**2,c:e**2,f:d*e+u}
assert s.Poly(s.expand(grad[0].subs(sub2, simultaneous=True)),u,d,e,modulus=2)==s.Poly(u**2,u,d,e,modulus=2)
assert all(s.Poly(s.expand(grad[i].subs(sub2, simultaneous=True)),u,d,e,modulus=2).is_zero for i in (1,2,3,4,5))
assert s.Poly(s.expand(P.subs(sub2, simultaneous=True)),u,d,e,modulus=2)==s.Poly(u**2,u,d,e,modulus=2)

# Hilbert polynomial of a (2,2,2) complete intersection, and conormal twist.
T=s.Symbol('T', integer=True)
HP=s.expand(sum((-1)**j*comb(3,j)*s.prod(T+5-2*j-i for i in range(5))/factorial(5) for j in range(4)))
assert s.simplify(HP-(4*T**2+2))==0
assert s.simplify(((2*T+2)*(2*T+1)+(2*T-1)*(2*T-2))/2-HP)==0

# Exhaustive affine finite-field points, divided by q-1 for projective orbits.
for q in (2,3,5):
    singular=0
    for vals in product(range(q),repeat=6):
        if not any(vals): continue
        aa,bb,cc,dd,ee,ff=vals
        deriv=(bb*cc+ff*ff,aa*cc+ee*ee,aa*bb+dd*dd,
               2*(cc*dd+ee*ff),2*(bb*ee+dd*ff),2*(aa*ff+dd*ee))
        if all(v%q==0 for v in deriv):
            p=(aa*bb*cc+aa*ff*ff+bb*ee*ee+cc*dd*dd+2*dd*ee*ff)%q
            assert p==0
            singular+=1
    assert singular%(q-1)==0
    projective=singular//(q-1)
    expected=q*q+q+1 if q==2 else 3*q
    assert projective==expected,(q,projective,expected)

# Generic ordinary transverse node of an odd-characteristic conic:
# Hessian has corank two in affine coordinates (the radial and curve directions).
H=s.hessian(P,x)
H0=H.subs({a:0,b:1,c:-1,d:0,e:0,f:1})
assert H0.rank()==4
for q in (3,5,7):
    mat=[[int(H0[i,j])%q for j in range(6)] for i in range(6)]
    def rank_mod(mat,p):
        mat=[r[:] for r in mat]; t=0
        for j in range(len(mat[0])):
            pivot=next((i for i in range(t,len(mat)) if mat[i][j]%p),None)
            if pivot is None:continue
            mat[t],mat[pivot]=mat[pivot],mat[t]
            inv=pow(mat[t][j]%p,-1,p)
            mat[t]=[(v*inv)%p for v in mat[t]]
            for i in range(len(mat)):
                if i!=t:
                    fac=mat[i][j]
                    mat[i]=[(v-fac*w)%p for v,w in zip(mat[i],mat[t])]
            t+=1
        return t
    assert rank_mod(mat,q)==4
print('VERIFY_OK odd_conics=3 embedded_vertices=3 char2_K3_carpet=complete_intersection_2_2_2 generic_hessian_rank=4 finite_fields=2,3,5')
