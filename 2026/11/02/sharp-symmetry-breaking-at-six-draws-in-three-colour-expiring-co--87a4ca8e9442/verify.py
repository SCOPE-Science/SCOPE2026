"""Exact symbolic checks for three-colour expiring-window entry probabilities.

Requires Python 3.10+ and SymPy 1.12+.  Run: python verify.py
These calculations reproduce algebra used in the accompanying analytic proof;
positivity for arbitrarily large window lengths rests on the stated induction.
"""
from itertools import product
from sympy import symbols, expand, factor, Rational, diff, simplify, Poly, nroots

x, y, z, a, t, m = symbols('x y z a t m', real=True)
p = (x, y, z)
e2 = x*y + x*z + y*z
e3 = x*y*z
checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def flux(M):
    return sum(p[i]*(1-p[i])*((1-p[i])**(M-1)-sum(p[j]**(M-1) for j in range(3) if j != i)) for i in range(3))

# Independently enumerate all length-(M+1) words and compare each coefficient
# after imposing x+y+z=1; stationarity is not an approximation.
for M in range(3, 7):
    enumerated = 0
    count = 0
    for w in product(range(3), repeat=M+1):
        if len(set(w[:M])) < 3 and len(set(w[1:])) == 3:
            term = 1
            for i in w:
                term *= p[i]
            enumerated += term
            count += 1
    check(expand((enumerated-flux(M)).subs(z,1-x-y)) == 0, f'window enumeration {M}')
    check(count > 0, f'entry count {M}')
    print(f'M={M}, independent entry words={count}')

# Exact elementary-symmetric reductions, using the probability normalization.
forms={
 3:4*e3,
 4:6*e3*(1-e2),
 5:2*e3*(4-7*e2-3*e3),
 6:5*e3*(2*e2**2-5*e2-3*e3+2),
}
for M, target in forms.items():
    check(expand((flux(M)-target).subs(z,1-x-y))==0, f'symmetric formula M={M}')

# Derive three Schur-concavity pair-exchange certificates for M<=5.
for M,target in forms.items():
    if M>5: continue
    exchange = simplify((diff(target,x)-diff(target,y))/(x-y))
    known={3:-4*z,4:-6*z*(1-e2-x*y),5:-2*z*(4-7*(e2+x*y)-6*e3)}[M]
    check(expand((exchange-known).subs(z,1-x-y))==0,f'exchange certificate M={M}')

# Exact uniform Hessian and induction for every integer M>=6.
u=Rational(1,3)
C=lambda M: (3*2**(M-2)*M*(M-5)-12*M*M+42*M-18)/3**M
for M in range(3,20):
    f=flux(M).subs(z,1-x-y)
    # tangent displacement (x,y,z)=(1/3+t,1/3-t,1/3)
    expr=expand(f.subs({x:u+t,y:u-t}))
    coefficient=expand(expr).coeff(t,2)
    check(simplify(coefficient-C(M))==0,f'quadratic coefficient M={M}')
q = 3*2**(m-2)*m*(m-5)-12*m*m+42*m-18
check(simplify(q.subs(m,6)-90)==0,'base induction')
difference=simplify(q.subs(m,m+1)-2*q)
check(simplify(difference-(3*2**m*(m-2)+12*m*m-66*m+48))==0,'induction difference')

# Complete M=6 stationary-point reduction.
F=forms[6]
Fe2=5*e3*(4*e2-5)
Fe3=5*(2*e2**2-5*e2-6*e3+2)
check(expand((diff(F,x)-diff(F,y)+(x-y)*(Fe2+z*Fe3)).subs(z,1-x-y))==0,'two-coordinate derivative')
Fa=factor(F.subs({x:a,y:a,z:1-2*a}))
expected=-10*a*a*(2*a-1)*(9*a**4-9*a**3+10*a*a-5*a+1)
check(simplify(Fa-expected)==0,'equal-pair polynomial')
Q=42*a**4-40*a**3+35*a*a-15*a+2
check(simplify(diff(Fa,a)+10*a*(3*a-1)*Q)==0,'equal-pair derivative')
check(simplify(diff(Q,a,2)-2*(252*a*a-120*a+35))==0,'quartic strict convexity')
check(Q.subs(a,0)>0 and Q.subs(a,Rational(1,3))<0 and Q.subs(a,Rational(1,2))>0,'isolating opposite signs')
R=3*a**4-2*a**3+6*a*a-5*a+1
check(simplify((Fe2+z*Fe3).subs({x:a,y:a,z:1-2*a})-10*(1-2*a)*R)==0,'transverse coefficient')
check(R.subs(a,Rational(1,3))<0 and R.subs(a,Rational(1,2))<0,'negative convex endpoints')
check(simplify(diff(R,a,2)-12*(3*a*a-a+1))==0,'transverse strict convexity')
roots=[float(v) for v in nroots(Q) if abs(float(v.as_real_imag()[1])) < 1e-10]
roots.sort()
check(len(roots)==2 and .2<roots[0]<.25 and (1/3)<roots[1]<.5,'stationary point root isolation')
print('a_* (two equal lower probabilities):',format(roots[0],'.15f'))
print('competing saddle:',format(roots[1],'.15f'))
print('max M=6:',format(float(Fa.subs(a,roots[0])),'.15f'))
print('uniform M=6:',str(Fa.subs(a,Rational(1,3))))
print(f'PASS {checks} independent exact-symbolic assertions')
