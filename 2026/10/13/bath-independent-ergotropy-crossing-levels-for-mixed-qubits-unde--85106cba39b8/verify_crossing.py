"""Check the finite-temperature generalized-amplitude-damping qubit crossing identities."""
from fractions import Fraction as F
from math import sqrt, log, isclose
from random import Random

def ergo(z,b,eta,q):
    w=-eta+q*(z+eta)
    return w+sqrt(w*w+q*b)

def crossing(z1,b1,z2,b2,eta):
    e=(b2-b1)/(2*(z1-z2))
    q=e*(e+2*eta)/(2*e*(z1+eta)+b1)
    return e,q

# Certified exact equality of the two inverse equations, with rational states.
z1,b1,z2,b2=F(3,5),F(1,25),F(0),F(1,4)
e=(b2-b1)/(2*(z1-z2))
assert e==F(7,40)
for eta in (F(1),F(1,2),F(1,5),F(0)):
    q1=e*(e+2*eta)/(2*e*(z1+eta)+b1)
    q2=e*(e+2*eta)/(2*e*(z2+eta)+b2)
    assert q1==q2 and 0<q1<1
    for z,b in ((z1,b1),(z2,b2)):
        w=-eta+q1*(z+eta)
        assert e*(e-2*w)==q1*b
        assert e-w>=0
        assert (e-w)**2==w*w+q1*b
    if eta==1:assert q1==F(203,320)

rng=Random(3491)
crossings=0
for j in range(12000):
    z1=rng.uniform(-1,1)
    z2=rng.uniform(-1,1)
    b1=rng.random()*(1-z1*z1)
    b2=rng.random()*(1-z2*z2)
    eta=rng.random()
    E1=ergo(z1,b1,eta,1.)
    E2=ergo(z2,b2,eta,1.)
    if abs(E1-E2)<1e-9: continue
    if E1<E2: z1,b1,z2,b2,E1,E2=z2,b2,z1,b1,E2,E1
    predicted=b1<b2
    if predicted:
        e,q=crossing(z1,b1,z2,b2,eta)
        assert e>0 and 0<q<1
        qhot=crossing(z1,b1,z2,b2,0.0)[1]
        qcold=crossing(z1,b1,z2,b2,1.0)[1]
        assert 0<qhot<q<qcold<1 if 0<eta<1 else 0<qhot<qcold<1
        assert isclose(ergo(z1,b1,eta,q),e,rel_tol=1e-8,abs_tol=1e-9)
        assert isclose(ergo(z2,b2,eta,q),e,rel_tol=1e-8,abs_tol=1e-9)
        assert ergo(z1,b1,eta,q/2)<ergo(z2,b2,eta,q/2)
        assert ergo(z1,b1,eta,(1+q)/2)>ergo(z2,b2,eta,(1+q)/2)
        crossings+=1
    else:
        # Independent grid inequality, including near equilibrium.
        for q in (1,0.8,0.5,0.1,0.01,0.0001):
            assert ergo(z1,b1,eta,q)>=ergo(z2,b2,eta,q)-1e-12
print('VERIFY_OK',crossings,'crossing pairs, 12000 physical-state trials; four exact rational bath cases')
