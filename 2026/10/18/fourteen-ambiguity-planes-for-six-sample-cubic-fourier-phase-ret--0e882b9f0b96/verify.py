#!/usr/bin/env python3
"""Exact finite-dimensional certificate for six-root cubic phaseless Hermite sampling.

Requires Python 3 and sympy. Contains only scientific verification, no external inputs.
"""
import itertools
import sympy as sp
I=sp.I
sqrt=sp.sqrt

def H(a,b,t,y):
    return sp.Matrix([[3*a+8*b,2*sp.conjugate(t),0,-I*y],
        [2*t,-4*a-9*b,-3*sp.conjugate(t),0],
        [0,-3*t,a,sp.conjugate(t)],[I*y,0,t,b]])

def zero(q):return sp.simplify(sp.expand(q))==0

def check(h):
    assert h==h.conjugate().T
    assert zero(sp.trace(h))
    for J in itertools.combinations(range(4),3):
        assert zero(h.extract(J,J).det()),('3minor',J)
    assert zero(h.det())
    assert not zero(sp.trace(h*h))

p=(sqrt(3)+I)/2
q=(-sqrt(3)+I)/2
kappa=(-21-sqrt(57))/48
r=sp.simplify(kappa*(4+9*kappa)/4)
s=sp.simplify(-(27*kappa**2+72*kappa**3)/4)
assert r.is_positive and s.is_positive
reps=[('01',H(0,0,0,1))]
for sign in (-1,1): reps.append((f'0b{sign}',H(0,1,0,sign*2*sqrt(2))))
for sign in (-1,1): reps.append((f'a0{sign}',H(1,-sp.Rational(4,9),0,sign*2*sqrt(5)/9)))
for j,z in enumerate((p,I,q)):
    y=-sp.Rational(2,3)*(1 if j!=1 else -1)
    reps.append((f'off{j}',H(0,0,z,y)))
for sign,phases in [(-1,(p,q,-I)),(1,(sp.conjugate(p),I,sp.conjugate(q)))]:
    for j,z in enumerate(phases):
        reps.append((f'branch{sign}_{j}',H(1,kappa,sqrt(r)*z,sign*sqrt(s))))
assert len(reps)==14
for name,h in reps:
    check(h)
    print('CHECKED_RANK_TWO',name)

# For traceless Hermitian rank two, h^2 is a positive scalar times the
# orthogonal projection onto the two-dimensional range. Distinct ranges
# can be checked by their normalized h^2.
projectors=[sp.simplify(2*h*h/sp.trace(h*h)) for _,h in reps]
for i,j in itertools.combinations(range(len(reps)),2):
    Delta=projectors[i]-projectors[j]
    assert any(not zero(t) for t in Delta),('duplicate ranges',i,j)
print('DISTINCT_RANGES',len(reps))

# The four principal minors in the general five-real-dimensional kernel.
a,b,u,v,y=sp.symbols('a b u v y',real=True)
T=u+I*v
K=H(a,b,T,y)
F=[sp.factor(K.extract([j for j in range(4) if j!= i],[j for j in range(4) if j!=i]).det()) for i in range(4)]
assert zero(F[0]-a*(-4*a*b-9*b*b+4*(u*u+v*v)))
assert zero(F[1]-(3*a*a*b+8*a*b*b-3*a*(u*u+v*v)-a*y*y-8*b*(u*u+v*v)))
assert zero(F[2]-(-12*a*a*b-59*a*b*b+4*a*y*y-72*b**3-4*b*(u*u+v*v)+9*b*y*y))
assert zero(F[3]-(-12*a**3-59*a*a*b-72*a*b*b-31*a*(u*u+v*v)-72*b*(u*u+v*v)))
R=b*(4*a+9*b)/4
assert zero(sp.expand(F[3]).subs(v*v,R-u*u)+sp.Rational(3,4)*(4*a+9*b)*(4*a*a+21*a*b+24*b*b))
print('ELIMINATION_IDENTITIES_OK')

# Independently form the twelve real measurement equations on all sixteen
# Hermitian entries, and verify the claimed five-dimensional kernel.
D=sp.symbols('d0:4',real=True)
G=sp.zeros(4)
unknown=list(D)
for j in range(4):
    G[j,j]=D[j]
for j in range(4):
    for k in range(j+1,4):
        x,z=sp.symbols(f'x{j}{k} z{j}{k}',real=True)
        unknown.extend((x,z))
        G[j,k]=x+I*z
        G[k,j]=x-I*z
root=(1+I*sqrt(3))/2
equations=[]
for m in range(6):
    w=sp.expand(root**m)
    f=sp.Matrix([1,w,w**2,w**3])
    df=sp.Matrix([0,1,2*w,3*w**2])
    equations.extend([sp.re(sp.expand((f.conjugate().T*G*f)[0])).expand(complex=True),
                      sp.re(sp.expand((df.conjugate().T*G*df)[0])).expand(complex=True)])
A,_=sp.linear_eq_to_matrix(equations,unknown)
assert A.rank()==11
for pa,pb,pt,py in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,I,0),(0,0,0,1)]:
    M=H(pa,pb,pt,py)
    for m in range(6):
        w=sp.expand(root**m)
        f=sp.Matrix([1,w,w**2,w**3])
        df=sp.Matrix([0,1,2*w,3*w**2])
        assert zero(sp.expand_complex((f.conjugate().T*M*f)[0]))
        assert zero(sp.expand_complex((df.conjugate().T*M*df)[0]))
print('MEASUREMENT_KERNEL_DIMENSION_FIVE_OK')


# On the nonzero diagonal branch, determinant is D0+12*y*Im(t^3),
# and D0^2 equals 144*s*r^3 when 4+21*k+24*k^2 = 0.
k=sp.symbols('k',real=True)
rr=k*(4+9*k)/4
ss=-(27*k*k+72*k**3)/4
D0=sp.expand(-12*k-59*k*k-72*k**3+12*rr+4*ss+28*k*rr+9*k*ss+4*rr*rr+9*rr*ss)
assert zero(sp.rem(D0*D0-144*ss*rr**3,4+21*k+24*k*k,k))
assert zero(sp.simplify(D0.subs(k,kappa)-12*sqrt(s)*r**sp.Rational(3,2)))
print('DETERMINANT_DISCRIMINANT_OK')

# A central explicit pair P=1+i z^3, Q=1-i z^3 has the same value and
# derivative magnitudes at all sixth roots, but is not projectively equal.
for j in range(6):
    z=sp.exp(I*sp.pi*j/3)
    assert zero(sp.expand_complex((1+I*z**3)*sp.conjugate(1+I*z**3)-(1-I*z**3)*sp.conjugate(1-I*z**3)))
    assert zero((3*I*z**2)*sp.conjugate(3*I*z**2)-(-3*I*z**2)*sp.conjugate(-3*I*z**2))
print('EXPLICIT_AMBIGUITY_OK')
print('ALL_EXACT_CHECKS_PASSED')
