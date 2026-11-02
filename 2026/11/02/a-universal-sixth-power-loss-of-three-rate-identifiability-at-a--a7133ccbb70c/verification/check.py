"""Exact recovery and asymptotic checks for homogeneous triadic SIS inference.

Run with Python 3.10 or newer; uses only the standard library.
The asymptotic experiment is supplementary to the analytic proof.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def row(x, h):
    return [-h*x, h*x*(1-x), h*x*x*(1-x)]


def solve(m, rhs):
    base = det3(m)
    assert base != 0
    ans = []
    for j in range(3):
        b = [list(v) for v in m]
        for i in range(3):
            b[i][j] = rhs[i]
        ans.append(det3(b)/base)
    return ans


def next_state(x, d, b, k, h):
    return x + h*x*(-d + (1-x)*(b+k*x))


def exact_checks():
    # Independent direct expansion of the determinant on a small rational grid.
    points = [F(j,11) for j in range(1,11)]
    count = 0
    for i in range(7):
        for j in range(i+1,9):
            for l in range(j+1,10):
                a,b,c = points[i],points[j],points[l]
                h = F(2,7)
                actual = det3([row(z,h) for z in (a,b,c)])
                expected = h**3*a*b*c*(a-b)*(a-c)*(b-c)
                assert actual == expected < 0
                count += 1
    # Exact parameter recovery from four observations in two fold examples.
    for beta, kappa, h, x0 in [(F(1),F(4),F(1,10),F(3,4)),
                              (F(1,2),F(3,2),F(1,8),F(2,3))]:
        delta = (kappa+beta)**2/(4*kappa)
        r = (kappa-beta)/(2*kappa)
        assert x0 > r and h*(delta+beta+kappa)<1
        x = [x0]
        for _ in range(3):
            x.append(next_state(x[-1],delta,beta,kappa,h))
        assert x[0] > x[1] > x[2] > x[3] > r
        M = [row(z,h) for z in x[:3]]
        y = [x[j+1]-x[j] for j in range(3)]
        recovered = solve(M,y)
        assert recovered == [delta,beta,kappa]
        assert det3(M)>0
    return count


def asymptotic_check():
    with localcontext() as ctx:
        ctx.prec = 65
        beta=D(1); kappa=D(4); delta=D(25)/16
        h=D(1)/10; r=D(3)/8; x=D(3)/4
        results = []
        for t in range(1,60001):
            if t in (1000,10000,60000):
                y=x-h*kappa*x*(x-r)**2
                z=y-h*kappa*y*(y-r)**2
                det=h**3*x*y*z*(x-y)*(x-z)*(y-z)
                scaled=det*D(t)**6
                results.append((t,scaled))
            x=x-h*kappa*x*(x-r)**2
        target=D(2)/(kappa**3)
        assert abs(results[-1][1]/target-1)<D('0.03')
        return target, results


if __name__ == '__main__':
    n = exact_checks()
    target, values = asymptotic_check()
    print('exact Vandermonde identities checked:',n)
    print('exact recovery at both fold parameter choices: PASS')
    print('predicted limit for t^6 det(Phi_t):',target)
    for t,value in values:
        print(f' t={t:5d}: t^6 det(Phi_t)={value:.20f}')
    print('analytic asymptotic numerical cross-check: PASS')
