"""Reproduce finite numerical checks for isotropic chord-statistic reconstruction.
All formulas and proofs are contained in RESULT.md. Python 3 standard library only.
"""
import math

PI = math.pi


def shape_invariants(a, b, angle):
    assert a >= b > 0 and 0 < angle <= PI / 2
    h = b * math.sin(angle)
    mean = PI * a * b * math.sin(angle) / (2 * (a + b))
    J = (PI / 2 - angle) * math.cos(angle) + math.sin(angle)
    slope = J / ((a + b) * math.sin(angle))
    return mean, slope, h


def inverse(mean, slope, h):
    alpha = 2 * mean / (PI * h)
    q = slope * h / (1 - alpha)
    if not (0.5 - 1e-12 <= alpha < 1.0 and 1.0 - 1e-12 <= q < PI / 2):
        raise ValueError('Not a nondegenerate parallelogram signature')
    alpha = max(alpha, 0.5)
    q = max(q, 1.0)
    lo, hi = 0.0, PI / 2
    for _ in range(85):
        mid = (lo + hi) / 2
        J = (PI / 2 - mid) * math.cos(mid) + math.sin(mid)
        if J > q:
            lo = mid
        else:
            hi = mid
    angle = (lo + hi) / 2
    s = h / ((1 - alpha) * math.sin(angle))
    return alpha * s, (1 - alpha) * s, angle


def S_quad(a, b, delta, t, n=240000):
    C = a * b * math.sin(delta)
    accum = 0.0
    for k in range(n):
        theta = PI * (k + 0.5) / n
        A = a * abs(math.sin(theta))
        B = b * abs(math.sin(theta - delta))
        if t * max(A, B) < C:
            accum += A + B - 2 * A * B * t / C
    return (PI / n) * accum / (2 * (a + b))


def J_quad(delta, n=200000):
    return PI / n * sum(abs(math.sin(PI * (i+.5)/n)*math.sin(PI * (i+.5)/n - delta)) for i in range(n))


def close(x, y, tol=1e-8):
    if abs(x-y)>tol*max(1,abs(x),abs(y)):
        raise AssertionError((x,y))


if __name__ == '__main__':
    shapes = [(1,1,PI/2),(2,1,PI/2),(3,1,.7),(4,3,1.1),(2,1,.2),(1,1,.4),(10,1,1.5)]
    for a,b,delta in shapes:
        mu,kappa,h=shape_invariants(a,b,delta)
        aa,bb,dd=inverse(mu,kappa,h)
        close(a,aa)
        close(b,bb)
        close(delta,dd)
        J=(PI/2-delta)*math.cos(delta)+math.sin(delta)
        close(J,J_quad(delta),1e-9)
        for t in [0.13*h,0.5*h,0.999*h]:
            close(S_quad(a,b,delta,t),1-kappa*t,2e-9)
        eps=0.0001*h
        loss=(1-kappa*(h+eps))-S_quad(a,b,delta,h+eps)
        assert loss>1e-4, (a,b,delta,loss)
        # The leading nonanalytic deficit is governed by global maxima of transverse width.
        multiplicity=2 if a==b else 1
        cusp=multiplicity*(a-b*math.cos(delta))/(a+b)*math.sqrt(2/h)
        assert abs(loss/(cusp*math.sqrt(eps))-1)<.065, (a,b,delta,loss/(cusp*math.sqrt(eps)))
    # Exact feasibility boundaries: rectangles have q=1, square has alpha=1/2,q=1.
    for a,b in [(1,1),(3,1),(2.5,2)]:
        mu,kappa,h=shape_invariants(a,b,PI/2)
        close(kappa*h/(1-2*mu/(PI*h)),1)
    # Right-angle inverse has optimal square-root conditioning.
    for eps in [0.01,0.004,0.001]:
        angle=PI/2-eps
        q=(PI/2-angle)*math.cos(angle)+math.sin(angle)
        assert abs((q-1)/(.5*eps**2)-1)<1e-3
    print('ALL_INVERSE_AND_FEASIBILITY_CHECKS_PASSED')
    print('ALL_CHORD_QUADRATURE_AND_CUSP_CHECKS_PASSED')
    print('ALL_CHECKS_PASSED')
