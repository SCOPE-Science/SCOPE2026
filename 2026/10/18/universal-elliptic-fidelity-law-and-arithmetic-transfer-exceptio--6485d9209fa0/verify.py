"""Bounded consistency checks for the odd–odd resonance ceiling."""
from math import cos, gcd, pi, sin


def ceiling(p, q):
    low, high = 0.0, pi/q
    for _ in range(52):
        a = (low+high)/2
        b = (pi-q*a)/p
        if q*sin(b) > p*sin(a):
            low = a
        else:
            high = a
    a = (low+high)/2
    b = (pi-q*a)/p
    best = ((cos(a)+cos(b))/2)**2
    return a, b, best


def probability(p, q, theta):
    return ((cos(p*theta)-cos(q*theta))/2)**2


def main():
    pairs = [(3,5),(5,7),(7,9),(9,11),(11,17),(13,19),
             (15,23),(29,49),(99,101),(199,201),(399,401)]
    for p, q in pairs:
        assert p % 2 == q % 2 == 1 and gcd(p,q) == 1 and q*q <= 3*p*p
        a,b,peak = ceiling(p,q)
        assert a > 0 and b > 0 and peak < 1
        assert abs(p*sin(a)-q*sin(b)) < 1e-12
        u = pow(q,-1,p)
        if u % 2:
            u += p
        v = (q*u-1)//p
        assert q*u-p*v == 1 and u % 2 == 0 and v % 2 == 1
        theta = (pi*u-a)/p
        assert abs(probability(p,q,theta)-peak) < 1e-12
        if q < 30:
            grid_peak = max(probability(p,q,2*pi*k/48000) for k in range(48000))
            assert grid_peak <= peak+1e-12 and peak-grid_peak < 5e-6
        if q >= 49:
            err = abs(1-peak-pi*pi/(2*(p*p+q*q)))
            assert err*q**4 < 12
    assert probability(1,1,1.23) == 0
    print(f'PASS: {len(pairs)} odd–odd pairs and the degenerate endpoint')


if __name__ == '__main__':
    main()
