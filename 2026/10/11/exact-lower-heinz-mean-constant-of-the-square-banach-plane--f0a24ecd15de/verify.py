import math


def M(nu, a, b):
    if nu == 0.0 or nu == 1.0:
        return (a + b) / 2.0
    if a == 0.0 or b == 0.0:
        return 0.0
    return (a**nu * b**(1.0-nu) + a**(1.0-nu) * b**nu) / 2.0


def norm_inf(z):
    return max(abs(z[0]), abs(z[1]))


def check():
    nus = [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]
    grid = [i / 100.0 for i in range(-100, 101)]
    boundary = []
    for t in grid:
        boundary.extend([(1.0,t),(-1.0,t),(t,1.0),(t,-1.0)])
    for nu in nus:
        target = (2.0**nu + 2.0**(1.0-nu)) / 2.0
        x0 = (1.0, 0.0)
        vals = []
        for y in boundary:
            A = norm_inf((x0[0]+y[0], x0[1]+y[1]))
            B = norm_inf((x0[0]-y[0], x0[1]-y[1]))
            vals.append(M(nu,A,B))
            assert max(A,B) <= 2.0 + 1e-12
            assert min(A,B) <= 1.0 + 1e-12
        assert abs(max(vals)-target) < 1e-12
        for a in [i/100.0 for i in range(101)]:
            x=(1.0,a); y=(1.0,-1.0)
            A=norm_inf((x[0]+y[0],x[1]+y[1]))
            B=norm_inf((x[0]-y[0],x[1]-y[1]))
            assert M(nu,A,B) + 1e-12 >= target
    assert abs((2**0.5+2**0.5)/2-math.sqrt(2)) < 1e-12
    assert abs((2**0+2**1)/2-1.5) < 1e-12
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
