#!/usr/bin/env python3
"""Finite deterministic checks of analytic trigonometric and stochastic-generator identities."""
import math
pi=math.pi
N=0
for i in range(1,30):
    x=2*pi*i/31
    for j in range(1,30):
        y=2*pi*j/31
        actual=(math.cos(x)-math.cos(y))**2+(math.sin(x)-math.sin(y))**2
        expected=4*math.sin((x-y)/2)**2
        assert abs(actual-expected)<1e-12
        N+=1
print('CIRCULAR_DIFFERENCE_QUADRATIC_VARIATION_PASS',N)
for j in range(1,60):
    x=2*pi*j/61
    sine=math.sin(x/2)
    # g(z)=log sin(z/2): g''=-1/(4 sin(z/2)^2)
    gen=4*sine*sine*(-.25/(sine*sine))
    coeff=math.sqrt(8)*sine*(.5*math.cos(x/2)/sine)
    assert abs(gen+1)<1e-12
    assert abs(coeff-math.sqrt(2)*math.cos(x/2))<1e-12
    # h(z)=log tan(z/4): drift=tanh(h(z)), diffusion=sqrt(2)
    transformed_drift=4*sine*sine*(-math.cos(x/2)/(4*sine*sine))
    u=math.log(math.tan(x/4))
    assert abs(transformed_drift-math.tanh(u))<1e-12
print('POISSON_AND_LAMperti_TRANSFORM_PASS',59)
for x in (.4, 1.4, pi, 5.7):
    for eps in (.05, .1, .2):
        if eps>=min(x,2*pi-x): continue
        mean=math.log(math.sin(x/2)/math.sin(eps/2))
        var=2*mean-(x-eps)*(2*pi-eps-x)/4
        p=(x-eps)/(2*pi-2*eps)
        assert mean>0 and var>0 and 0<p<1
        terminalvar=p*(2*pi-eps-x)**2+(1-p)*(eps-x)**2
        assert abs(terminalvar-(x-eps)*(2*pi-eps-x))<1e-12
print('EXACT_EXIT_MOMENT_ALGEBRA_PASS',12)
print('INFINITE_TIME_AND_LIMIT_STATEMENTS_REQUIRE_ANALYTIC_PROOF')
