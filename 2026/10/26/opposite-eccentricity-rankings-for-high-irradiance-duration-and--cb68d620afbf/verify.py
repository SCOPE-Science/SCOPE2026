"""Direct quadrature checks for a fixed-semimajor-axis Kepler irradiance threshold.

Use: python verify.py. Requires Python 3 standard library only.
"""
import math
import random


def duration(e, eta):
    assert 0 <= e < 1 and eta > 1
    d = 1 - eta**(-0.5)
    if e <= d:
        return 0.0
    E = math.acos(d / e)
    return (E - e * math.sin(E)) / math.pi


def excess(e, eta):
    assert 0 <= e < 1 and eta > 1
    d = 1 - eta**(-0.5)
    if e <= d:
        return 0.0
    E0 = math.acos(d / e)
    n = 4000
    h = E0/n
    f = lambda E: 1/(1-e*math.cos(E)) - eta*(1-e*math.cos(E))
    return h/(3*math.pi) * (f(0) + f(E0) +
           4*sum(f((2*j+1)*h) for j in range(n//2)) +
           2*sum(f(2*j*h) for j in range(1,n//2)))


def direct_orbit_quadrature(e, eta, steps=12000):
    h = 2*math.pi/steps
    total_f = total_q = 0.0
    for j in range(steps):
        E = (j+.5)*h
        v = 1-e*math.cos(E)
        flux = 1/(v*v)
        weight = v/steps
        if flux > eta:
            total_f += weight
            total_q += weight*(flux-eta)
    return total_f,total_q


def main():
    rng = random.Random(472018)
    comparisons=0
    for i in range(90):
        eta = 1.02 + 8 * rng.random()
        d = 1 - eta**(-.5)
        e = d + (1-d)*(.001 + .998*rng.random())
        f,q=direct_orbit_quadrature(e,eta)
        assert abs(f-duration(e,eta)) < .0003, (eta,e,f,duration(e,eta))
        assert abs(q-excess(e,eta)) < .002, (eta,e,q,excess(e,eta))
        comparisons += 1
        optimal = math.sqrt(d)
        assert duration(optimal,eta) > duration(.5*(d+optimal),eta)
        assert duration(optimal,eta) > duration(.5*(optimal+1),eta)
        a=d+.15*(1-d)
        b=d+.85*(1-d)
        assert excess(b,eta)>excess(a,eta)
    eta=16/9
    d=1-eta**(-.5)
    assert abs(d-.25)<1e-14
    fmax=duration(.5,eta)
    assert abs(fmax-(1/3-math.sqrt(3)/(4*math.pi)))<1e-13
    vals=[(e,duration(e,eta),excess(e,eta)) for e in [.3,.5,.8,.99]]
    assert vals[0][1]<vals[1][1]>vals[2][1]>vals[3][1]
    assert all(vals[i][2]<vals[i+1][2] for i in range(len(vals)-1))
    print('PASS: 90 direct time-weighted orbital quadratures; duration/excess formulas;')
    print('90 unique-max bracketing comparisons and 90 increasing-excess comparisons.')
    print('Example eta=16/9, e*=1/2, maximum duration fraction:',format(fmax,'.15f'))
    for v in vals: print('e, duration, excess:',v)

if __name__ == '__main__': main()
