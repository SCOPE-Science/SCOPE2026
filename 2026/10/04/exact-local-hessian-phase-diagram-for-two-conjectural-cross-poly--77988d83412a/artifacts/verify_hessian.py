#!/usr/bin/env python3
import sympy as sp

t = sp.symbols('t', positive=True)

# Beta-integral helper for sparse candidate.
def beta_int_even(m,k,a2=sp.Integer(2)):
    # integral_0^infty t^(2m)/(t^2+a2)^k dt
    return sp.Rational(1,2)*a2**(sp.Rational(2*m+1,2)-k)*sp.beta(sp.Rational(2*m+1,2), k-sp.Rational(2*m+1,2))

I0_sparse = sp.integrate(1/(1+t**2/sp.Integer(2))**2,(t,0,sp.oo))
assert sp.simplify(I0_sparse-sp.pi*sp.sqrt(2)/4)==0
# E0 representative: g''/g = -t^4/(1+t^2/2)
IA = sp.integrate((1/(1+t**2/sp.Integer(2))**2)*(-t**4/(1+t**2/sp.Integer(2))),(t,0,sp.oo))
assert sp.simplify(IA/I0_sparse + 3)==0

# Collective sparse mode; expression is exact after tangent normalization.
n = sp.symbols('n', integer=True, positive=True)
S_collective = -4*t**4*(-2*n+t**2+6)/(n*(t**2+2)**2)
# Integrate termwise after combining with g0; result can be done by Beta values.
IB_expected = sp.pi*sp.sqrt(2)*(n-8)/(4*n)
expr = sp.factor((1/(1+t**2/sp.Integer(2))**2)*S_collective)
# Verify by decomposing numerator into t^4 and t^6 over (t^2+2)^4.
expr2 = sp.factor(expr - 16*((2*n-6)*t**4-t**6)/(n*(t**2+2)**4))
assert sp.simplify(expr2)==0
IB = sp.simplify(16/sp.Integer(1)/n*((2*n-6)*beta_int_even(2,4)-beta_int_even(3,4)))
IB = sp.simplify(sp.expand_func(IB))
assert sp.simplify(IB-IB_expected)==0
assert sp.simplify(IB/I0_sparse-(n-8)/n)==0

def dense_lambda(N):
    N=sp.Integer(N)
    b2=1/(N*(N-1))
    c2=(N-1)/N
    g=1/((1+c2*t**2)*(1+b2*t**2)**(N-1))
    # tangent h=(0,1,-1,0,...)/sqrt(2); exact log-second derivative sum
    S=(2*c2*t**2/(1+c2*t**2)
       +(N-3)*2*b2*t**2/(1+b2*t**2)
       -2*(1-2*b2)*t**2/(1+b2*t**2)
       +4*b2*t**4/(1+b2*t**2)**2)
    S=sp.factor(S)
    # Match compact closed rational form used in the proof.
    S_target=2*N**2*t**4*(N-1)*(-N**2+3*N+t**2)/((N**2-N+t**2)**2*(N*t**2+N-t**2))
    assert sp.simplify(S-S_target)==0
    I=sp.integrate(g,(t,0,sp.oo))
    J=sp.integrate(sp.factor(g*S),(t,0,sp.oo))
    return sp.factor(sp.simplify(J/I)), sp.factor(I)

expected={
    4:sp.Rational(3,68),
    5:-sp.Rational(2393,7865),
    6:-sp.Rational(5899,9762),
    7:-sp.Rational(2290207,2630733),
    8:-sp.Rational(16822403,15129624),
}
for N,e in expected.items():
    lam,I=dense_lambda(N)
    assert lam==e,(N,lam,e)
    print(f'n={N} dense_lambda={lam} I={I}')

# Exact candidate-value ratios I(q_n)/I(p_n) for n=5,6.
ratios={
    5: sp.Rational(1573,5000)*sp.sqrt(10),
    6: sp.Rational(8135,31104)*sp.sqrt(15),
}
for N,e in ratios.items():
    _,I=dense_lambda(N)
    ratio=sp.simplify(I/I0_sparse)
    assert sp.simplify(ratio-e)==0,(N,ratio,e)
    if N==5: assert ratio<1
    if N==6: assert ratio>1
    print(f'n={N} dense_over_sparse={ratio}')
print('VERIFY_OK')
