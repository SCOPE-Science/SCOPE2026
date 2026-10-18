"""Reproducible checks for rank-one-factor covariance representability."""
import math
import numpy as np
import sympy as sp

checks = 0

def check(value, label):
    global checks
    assert bool(value), label
    checks += 1

# Exact stationary three-rate covariance and forced uniqueness values.
rates = [sp.Rational(1), sp.Rational(2), sp.Rational(3)]
P = sp.Matrix([[1/(rates[i]+rates[j]) for j in range(3)] for i in range(3)])
check(P == sp.Matrix([[sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,4)],
                      [sp.Rational(1,3),sp.Rational(1,4),sp.Rational(1,5)],
                      [sp.Rational(1,4),sp.Rational(1,5),sp.Rational(1,6)]]), 'stationary covariance')
check(P.det() > 0 and P[:2,:2].det() > 0, 'positive definite')
delta = sp.factor(P[0,1]*P[1,2]-P[0,2]*P[1,1])
check(delta == sp.Rational(1,240), 'strict one-factor sign defect')
v_mid_sq = P[0,1]*P[1,2]/P[0,2]
check(v_mid_sq == sp.Rational(4,15), 'forced factor square')
check(P[1,1]-v_mid_sq == -sp.Rational(1,60), 'forced negative diagonal')
S = P[0,1]+P[1,2]+P[0,2]+P[1,1]
threshold = sp.simplify((sp.sqrt(S*S+8*delta)-S)/4)
check(threshold == (sp.sqrt(991)-31)/120, 'explicit max-norm gap')
check(threshold > 0, 'positive gap')

# Leading small-time signed minor coefficient.
a,b,c,t = sp.symbols('a b c t', real=True)
def taylor_kernel(x,y,order=5):
    return sum((-1)**k*(x+y)**k*t**(k+1)/sp.factorial(k+1) for k in range(order+1))
minor = sp.expand(taylor_kernel(a,b)*taylor_kernel(b,c)-taylor_kernel(a,c)*taylor_kernel(b,b))
check(sp.simplify(minor.coeff(t,4)-(b-a)*(c-b)/12)==0, 'cubic residual leading minor coefficient')
check(sp.simplify(minor.coeff(t,5)+(b-a)*(c-b)*(a+2*b+c)/24)==0, 'next minor coefficient')

# Four-index obstruction when two distinct rates occur at least twice.
x,y = sp.symbols('x y', positive=True)
cs_defect = sp.factor(1/(2*x)*1/(2*y)-1/(x+y)**2)
check(cs_defect == (x-y)**2/(4*x*y*(x+y)**2), 'two-group tetrad factor')

# Positive Cauchy-Laplace kernel, quadrature and factor construction.
def k(rate_i,rate_j,T):
    z=rate_i+rate_j
    return -math.expm1(-z*T)/z

rng=np.random.default_rng(70227)
for q in range(1000):
    aa,bb,cc=sorted(0.05+5*rng.random(3))
    T=10**rng.uniform(-1.5,1.0)
    mm=k(aa,bb,T)*k(bb,cc,T)-k(aa,cc,T)*k(bb,bb,T)
    # Avoid subtractive-cancellation points; the proof uses integral positivity.
    if (bb-aa)*(cc-bb)*T*T > 1e-4:
        check(mm> -5e-15,'Laplace sign minor')
    x1,x2=sorted(0.05+5*rng.random(2))
    if x2-x1>0.01:
        cs=k(x1,x1,T)*k(x2,x2,T)-k(x1,x2,T)**2
        check(cs>-5e-15,'strict Cauchy-Schwarz')
    # A repeated group and one exceptional rate have a PSD diagonal-plus-rank-one representation.
    a0,b0=sorted(0.05+4*rng.random(2))
    us=rng.uniform(0.2,2.5,size=5)*rng.choice([-1,1],size=5)
    rs=[a0,a0,a0,a0,b0]
    B=np.array([[us[i]*us[j]*k(rs[i],rs[j],T) for j in range(5)] for i in range(5)])
    v=np.array([us[i]*math.sqrt(k(a0,a0,T)) for i in range(4)] +
               [us[4]*k(a0,b0,T)/math.sqrt(k(a0,a0,T))])
    D=np.diag(B-np.outer(v,v))
    check(np.all(D>=-1e-13),'nonnegative diagonal')
    check(np.linalg.norm(B-np.outer(v,v)-np.diag(D),ord='fro')<5e-13,'constructed factor')

# Midpoint single-factor approximation has O(T^3) entrywise errors.
a_vals = [0.4, 1.5, 3.1, 5.0]
u_vals = np.array([1.0,-1.3,0.9,1.8])
errs=[]
for T in [0.02,0.01,0.005,0.0025]:
    E=np.array([[u_vals[i]*u_vals[j]*k(a_vals[i],a_vals[j],T) for j in range(4)] for i in range(4)])
    v=np.array([u_vals[i]*math.sqrt(T)*math.exp(-a_vals[i]*T/2) for i in range(4)])
    errs.append(np.linalg.norm(E-np.outer(v,v),'fro'))
for n in range(3):
    ratio=errs[n]/errs[n+1]
    check(7.5<ratio<8.5, 'cubic midpoint order')
print('PASS', checks, 'checks')
print('stationary P=',P)
print('sign defect',delta, 'forced diagonal',P[1,1]-v_mid_sq)
print('lower gap',sp.N(threshold,20),'midpoint errors',errs)
