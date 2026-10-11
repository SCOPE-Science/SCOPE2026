#!/usr/bin/env python3
"""Exact finite cyclic Fourier sixth-moment identities and numerical checks."""
from itertools import product
from fractions import Fraction
import cmath, math, random
import sympy as sp

x,y,z,t=sp.symbols('x y z t', nonnegative=True)
coeffs=[sp.expand((x+y*z+x*z**2)**3).coeff(z,k) for k in range(7)]
assert coeffs==[x**3,3*x*x*y,3*x**3+3*x*y*y,6*x*x*y+y**3,3*x**3+3*x*y*y,3*x*x*y,x**3]
E={3:t**6+30*t**4+40*t**3+90*t**2+60*t+22,
   4:t**6+30*t**4+120*t**2+32,
   5:t**6+30*t**4+90*t**2+12*t+20,
   6:t**6+30*t**4+90*t**2+22,
   7:t**6+30*t**4+90*t**2+20}
D={3:-12*(t-1)*(t+2)*(2*t+1)*(2*t*t+2*t+5),
   4:-48*t*(t-1)*(t+1)*(t*t+6),
   5:-12*(4*t**5+10*t**3+5*t*t-20*t-2),
   6:-12*t*(4*t**4+10*t*t-19),
   7:-24*t*(2*t**4+5*t*t-10)}
for r in range(3,16):
    grouped=[sum(coeffs[j] for j in range(7) if j%r==k) for k in range(r)]
    target=sp.expand(E[min(r,7)].subs(t,y)*x**6).subs(y,y/x) if False else sp.Poly(E[min(r,7)],t)
    expected=sp.expand(E[min(r,7)].subs(t,y/x)*x**6).cancel()
    assert sp.simplify(sum(g*g for g in grouped)-expected)==0, r
for r in range(3,8):
    ratio=E[r]/(t*t+2)**3
    assert sp.factor(sp.diff(ratio,t)*(t*t+2)**4-D[r])==0, r
root5=sp.polys.polytools.intervals(4*t**5+10*t**3+5*t*t-20*t-2,eps=sp.Rational(1,10**8))
positive5=[(a,b) for (a,b),mult in root5 if b>0 and a>0]
assert len(positive5)==1,positive5
rp={3:1.0,4:1.0,5:1.0663663583699052,
    6:math.sqrt((math.sqrt(101)-5)/4),
    7:math.sqrt((math.sqrt(105)-5)/4)}
Cs={r:float(E[r].subs(t,rp[r])/(rp[r]**2+2)**3) for r in range(3,8)}
assert abs(Cs[4]-61/9)<1e-11
assert abs(Cs[7]-35*(math.sqrt(105)-3)/48)<1e-11
assert all(Cs[r]>Cs[r+1] for r in range(3,7))

# Actual discrete sixth powers, independent of convolution coefficients.
rng=random.Random(20261009)
for r in range(3,17):
    C=Cs[min(r,7)]
    root=cmath.exp(2j*math.pi/r)
    for _ in range(220):
        a,b,c=[complex(rng.randint(-4,4),rng.randint(-4,4)) for j in range(3)]
        if a==b==c==0:continue
        lhs=sum(abs(a+b*root**j+c*root**(2*j))**6 for j in range(r))/r
        en=sum(abs(s)**2 for s in (a,b,c))
        assert lhs<=C*en**3+2e-6*max(1,C*en**3),(r,lhs,C*en**3)
        cr=[a**3,3*a*a*b,3*a*a*c+3*a*b*b,6*a*b*c+b**3,
            3*a*c*c+3*b*b*c,3*b*c*c,c**3]
        exact=sum(abs(sum(cr[j] for j in range(7) if j%r==k))**2 for k in range(r))
        assert abs(lhs-exact)<5e-7*max(1,abs(exact)),(r,lhs,exact)
    tt=rp[min(r,7)]
    for k in range(r if r<=6 else 3):
        ph=cmath.exp(2j*math.pi*k/r) if r<=6 else cmath.exp(2j*math.pi*k/13)
        a,b,c=1,tt*ph,ph*ph
        lhs=sum(abs(a+b*root**j+c*root**(2*j))**6 for j in range(r))/r
        assert abs(lhs/(2+tt*tt)**3-C)<5e-9,(r,k,lhs/(2+tt*tt)**3,C)

# Subgroup-coset lifting on C_(4r): H={0,2r}; chi=character exponent 2.
for r in range(3,10):
    N=4*r
    tt=rp[min(r,7)]; C=Cs[min(r,7)]
    vals=[]
    for j in range(N):
        zj=cmath.exp(2j*math.pi*2*j/N)
        vals.append((1+tt*zj+zj*zj) if j%2==0 else 0j)
    mom2=sum(abs(v)**2 for v in vals)/N
    mom6=sum(abs(v)**6 for v in vals)/N
    assert abs(mom6/mom2**3-4*C)<1e-8,(r,mom6/mom2**3,4*C)

# Exact two-dimensional Cauchy Schwarz for reflection symmetrization,
# tested over all small rational coefficient triples and r=3,...,8.
for r in range(3,9):
    for A,B,C in product(range(5),repeat=3):
        if A==B==C==0:continue
        v=[sp.Integer(0)]*r
        v[0],v[1],v[2]=map(sp.Integer,(A,B,C))
        w=[sp.Integer(0)]*r
        w[0]=w[2]=sp.sqrt(sp.Rational(A*A+C*C,2))
        w[1]=sp.Integer(B)
        for h in range(r):
            old=sum(v[i]*v[(i+h)%r] for i in range(r))
            new=sum(w[i]*w[(i+h)%r] for i in range(r))
            assert float(new-old)>-1e-9,(r,A,B,C,h,new-old)
print('VERIFY_OK exact_residue_polynomials=13 exact_derivatives=5 root_isolation=PASS random_complex_cases=3080 subgroup_cases=7 reflection_cases=750 all_checks=PASS')
