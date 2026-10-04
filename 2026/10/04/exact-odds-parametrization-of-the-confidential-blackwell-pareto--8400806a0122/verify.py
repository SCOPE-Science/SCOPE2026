import math


def h2(t):
    if -1e-14 <= t <= 0.0:
        return 0.0
    if 1.0 <= t <= 1.0+1e-14:
        return 0.0
    if not 0.0 < t < 1.0:
        raise ValueError('entropy argument outside [0,1]')
    return -t*math.log2(t) - (1.0-t)*math.log2(1.0-t)


def psi(t):
    return -math.log(t)/math.log1p(t)


def y_from_x(x):
    target = 1.0/psi(x)
    lo, hi = 1e-14, 1.0-1e-14
    for _ in range(180):
        mid = (lo+hi)/2.0
        if psi(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def rates_from_xy(x, y):
    d = 1.0+x+y
    r1 = (1.0+y)/d * h2(y/(1.0+y))
    r2 = (1.0+x)/d * h2(x/(1.0+x))
    return r1, r2


def weight_from_xy(x, y):
    lx = -math.log(x)
    return lx/(lx+math.log1p(y))


def objective(a, b, c, w):
    A = (a+c)*h2(c/(a+c)) if a+c else 0.0
    B = (a+b)*h2(b/(a+b)) if a+b else 0.0
    return w*A + (1.0-w)*B


def solve_x_for_weight(w):
    lo, hi = 1e-12, 1.0-1e-12
    for _ in range(160):
        mid = (lo+hi)/2.0
        y = y_from_x(mid)
        wm = weight_from_xy(mid, y)
        if wm > w:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def main():
    phi = (1.0+math.sqrt(5.0))/2.0
    x0 = 1.0/phi
    assert abs(psi(x0)-1.0) < 2e-14
    r1, r2 = rates_from_xy(x0, x0)
    target = math.log2(phi)
    assert abs(r1-target) < 2e-14 and abs(r2-target) < 2e-14

    for x in (0.01, 0.1, x0, 0.9, 0.99):
        y = y_from_x(x)
        assert 0.0 < y < 1.0
        assert abs(psi(x)*psi(y)-1.0) < 2e-10
        w = weight_from_xy(x, y)
        e1 = w*math.log1p(y) + (1.0-w)*math.log(x)
        e2 = (1.0-w)*math.log1p(x) + w*math.log(y)
        assert abs(e1) < 2e-10 and abs(e2) < 2e-10

    # Direct coarse-grid checks of the original support optimization.
    for w in (0.25, 0.5, 0.75):
        x = solve_x_for_weight(w)
        y = y_from_x(x)
        a = 1.0/(1.0+x+y)
        b, c = a*x, a*y
        exact = objective(a,b,c,w)
        best = -1.0
        N = 121
        for i in range(N):
            aa = i/(N-1)
            for j in range(N-i):
                bb = j/(N-1)
                cc = 1.0-aa-bb
                best = max(best, objective(aa,bb,cc,w))
        assert exact + 1e-12 >= best
        assert exact-best < 2e-4

    y_small = y_from_x(1e-5)
    e1 = rates_from_xy(1e-5, y_small)
    y_large = y_from_x(1.0-1e-5)
    e2 = rates_from_xy(1.0-1e-5, y_large)
    assert e1[0] > 0.99999 and e1[1] < 1e-4
    assert e2[1] > 0.9999 and e2[0] < 0.02
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
