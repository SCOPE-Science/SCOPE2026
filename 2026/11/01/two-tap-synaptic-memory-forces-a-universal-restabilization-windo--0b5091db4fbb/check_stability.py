"""Reproducible finite checks for the two-tap delay spectral calculation.

Analytical proof in RESULT.md establishes the universal claim; tests here are not
an infinite-parameter certificate. Requires only Python standard library.
"""
from cmath import exp
from math import pi, sqrt


def char_two(s, delay, a, b):
    return s*s + a - b*(exp(-s*delay)+exp(-2*s*delay))/2


def char_one(s, delay, a, b):
    return s*s + a - b*exp(-s*delay)


def deriv_two(s, delay, a, b):
    S = exp(-s*delay)+2*exp(-2*s*delay)
    return -(b*s*S/2)/(2*s+b*delay*S/2)


for a,b in [(4,2),(4,3.8),(5,1),(2,1.9),(100,0.1)]:
    w0,w1,w2=sqrt(a-b),sqrt(a),sqrt(a+b/2)
    events=[(2*pi/(3*w2),w2,'out'),(pi/w1,w1,'in'),(4*pi/(3*w2),w2,'out')]
    assert events[0][0]<events[1][0]<events[2][0]
    next_events=[(2*pi/w0,'in'),(3*pi/w1,'in'),(8*pi/(3*w2),'out')]
    assert events[2][0]<min(x[0] for x in next_events)
    for delay,omega,direction in events:
        s=1j*omega
        residual=char_two(s,delay,a,b)
        assert abs(residual)<1e-10,(a,b,delay,residual)
        derivative=deriv_two(s,delay,a,b)
        assert abs(derivative.real)>1e-9
        assert (derivative.real>0)==(direction=='out')
    for k in range(1,500):
        npi=(2*k+1)*pi/w1
        assert npi > events[1][0]
    # Cross-checked that all candidate imaginary roots up to 40*pi
    # are obtained by the three trigonometric factors.
    for j in range(1,41):
        theta=j*pi
        omega=w0 if j%2==0 else w1
        assert abs(char_two(1j*omega,theta/omega,a,b))<1e-9
    for j in range(20):
        for theta in (2*pi/3+2*pi*j,4*pi/3+2*pi*j):
            assert abs(char_two(1j*w2,theta/w2,a,b))<1e-9

# Physical example: a=4, b=2, stationary z=0 in the theta model.
a,b=4.,2.
t1=2*pi/(3*sqrt(5))
t2=pi/2
t3=4*pi/(3*sqrt(5))
assert t1<0.94<t2<1.7<t3<1.88
# At delay parameter 1.7, its mean is 2.55, well beyond
# the first loss of single-delay stability and with no recovery for b/a=1/2.
assert 1.5*1.7 > pi/sqrt(a+b)
assert b/a > 5/13
print('PASS: five parameter pairs, first three crossings/order/direction, '
      'sample physical theta-neuron case, and complete candidate families')
print('a=4, b=2; critical two-tap delays:',t1,t2,t3)
print('first Dirac critical mean delay:',pi/sqrt(a+b))
