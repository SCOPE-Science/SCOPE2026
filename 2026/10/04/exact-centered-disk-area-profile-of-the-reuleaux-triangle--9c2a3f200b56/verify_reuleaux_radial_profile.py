#!/usr/bin/env python3
import math


def exact_area(w, r):
    d = w / math.sqrt(3.0)
    rin = w - d
    total = 0.5 * (math.pi - math.sqrt(3.0)) * w * w
    if r <= 0.0:
        return 0.0
    if r <= rin:
        return math.pi * r * r
    if r >= d:
        return total
    ca = (w*w - d*d - r*r) / (2.0*d*r)
    cb = (d*d + w*w - r*r) / (2.0*d*w)
    ca = max(-1.0, min(1.0, ca))
    cb = max(-1.0, min(1.0, cb))
    alpha = math.acos(ca)
    beta = math.acos(cb)
    lune = r*r*alpha - w*w*beta + d*r*math.sin(alpha)
    return math.pi*r*r - 3.0*lune


def exact_derivative(w, r):
    d = w / math.sqrt(3.0)
    rin = w - d
    if r < 0.0 or r > d:
        return 0.0
    if r <= rin:
        return 2.0*math.pi*r
    if r >= d:
        return 0.0
    ca = (w*w - d*d - r*r) / (2.0*d*r)
    ca = max(-1.0, min(1.0, ca))
    alpha = math.acos(ca)
    return 2.0*r*(math.pi - 3.0*alpha)


def radial_boundary(w, theta):
    d = w / math.sqrt(3.0)
    vals = []
    for j in range(3):
        phi = theta - 2.0*math.pi*j/3.0
        c = math.cos(phi)
        s = math.sin(phi)
        rad = w*w - d*d*s*s
        vals.append(d*c + math.sqrt(max(0.0, rad)))
    return min(vals)


def numeric_area(w, r, n=240000):
    # Polar-area quadrature: 1/2 integral min(r, rho_K(theta))^2 dtheta.
    total = 0.0
    dt = 2.0*math.pi/n
    for k in range(n):
        th = (k + 0.5)*dt
        rr = min(max(r, 0.0), radial_boundary(w, th))
        total += 0.5*rr*rr*dt
    return total


def main():
    widths = [0.7, 1.0, 2.3]
    worst = 0.0
    for w in widths:
        d = w/math.sqrt(3.0)
        rin = w-d
        test_r = [0.0, 0.25*rin, rin, rin + 0.1*(d-rin), rin + 0.35*(d-rin),
                  rin + 0.7*(d-rin), d-1e-7*w, d, 1.2*d]
        for r in test_r:
            ex = exact_area(w, r)
            nu = numeric_area(w, r)
            err = abs(ex-nu)
            worst = max(worst, err/(w*w))
            assert err <= 2.5e-5*w*w + 2e-10, (w,r,ex,nu,err)
        # Check analytic derivative against centered finite differences away from breakpoints.
        for frac in [0.15, 0.35, 0.55, 0.75, 0.9]:
            r = rin + frac*(d-rin)
            h = 2e-6*w
            fd = (exact_area(w,r+h)-exact_area(w,r-h))/(2*h)
            de = exact_derivative(w,r)
            assert abs(fd-de) <= 2e-7*w + 2e-9, (w,r,fd,de)
        # Endpoint identities.
        assert abs(exact_area(w, rin) - math.pi*rin*rin) < 1e-12*w*w
        assert abs(exact_area(w, d) - 0.5*(math.pi-math.sqrt(3))*w*w) < 1e-12*w*w
        assert abs(exact_derivative(w, d)) < 1e-12*w
    print(f"PASS: exact profile agrees with polar quadrature; worst normalized area error={worst:.3e}")

if __name__ == '__main__':
    main()
