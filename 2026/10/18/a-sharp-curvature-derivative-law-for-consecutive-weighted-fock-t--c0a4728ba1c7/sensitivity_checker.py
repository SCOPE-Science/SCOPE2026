"""Finite, reproducible checks of adjacent radial Fock moment sensitivities.

Only local moment quadrature and elementary identities are tested; the
uniform asymptotic theorem is proved analytically in RESULT.md.
"""
import math

A = 0.125
PERIOD = 2.0 * math.pi


def g(s):
    return 1.5 + A * math.sin(s)


def dg(s):
    return A * math.cos(s)


def inverse_phase(u):
    s = (u - math.log(1.5)) / 2.0
    for _ in range(12):
        s -= (2 * s + math.log(g(s)) - u) / (2 + dg(s) / g(s))
    return s


def tail_phi(r):
    s = math.log(r)
    return 0.75 * r * r + A * r * r * (2 * math.sin(s) - math.cos(s)) / 5


def predicted(k):
    s = inverse_phase(math.log(k + 0.5))
    return 2.0 / math.sqrt(math.pi) * math.sqrt(g(s)/(2*g(s)+dg(s)))


def measured(k):
    s = inverse_phase(math.log(k + 0.5))
    rk = math.exp(s)
    assert rk > math.exp(4) + 12, 'Moment calculation needs only periodic tail'
    hmax = (2*k+1)*math.log(rk) - 2*tail_phi(rk)
    n = 1600
    dr = 24/n
    weights = []
    for i in range(n+1):
        r = rk - 12 + dr*i
        h = (2*k+1)*math.log(r) - 2*tail_phi(r)
        w = math.exp(h - hmax) * (1 if i==0 or i==n else 4 if i%2 else 2)
        weights.append((r*r,w))
    Z = sum(w for _,w in weights)
    m = sum(t*w for t,w in weights)/Z
    delta = sum(abs(t/m-1)*w for t,w in weights)/Z
    return math.sqrt(k+1)*delta


def main():
    count=0
    for k in (30000, 40000, 65000, 100000, 170000, 250000, 400000, 600000, 900000):
        got = measured(k)
        want = predicted(k)
        assert abs(got-want) < 0.20/math.sqrt(k), (k,got,want)
        count+=1
    for s in (0, .3, .7, 1.4, 2.1, 3.5, 4.8, 5.9):
        u=2*s+math.log(g(s))
        assert abs(inverse_phase(u)-s)<1e-13
        assert abs(predicted(int(math.exp(u+2*PERIOD*3)))-predicted(int(math.exp(u+2*PERIOD*4))))<0.0006
        count+=2
    print('PASS:',count,'finite exact-likelihood / centered-moment / phase diagnostic groups')

if __name__=='__main__':
    main()
