"""Reproduce numerical checks for a two-patch antiphase seasonal growth theorem.

Pure Python standard library. These tests supplement, rather than replace,
the analytic Volterra-convolution proof given in RESULT.md.
"""
import math
import random


def matmul(x, y):
    return (x[0]*y[0]+x[1]*y[2], x[0]*y[1]+x[1]*y[3],
            x[2]*y[0]+x[3]*y[2], x[2]*y[1]+x[3]*y[3])


def expm2(a):
    """Independently evaluate a 2x2 exponential by Taylor/scaling-squaring."""
    norm = max(abs(a[0])+abs(a[1]), abs(a[2])+abs(a[3]))
    scale = max(0, math.ceil(math.log2(norm))) + 2 if norm > 0 else 0
    q = 2**scale
    z = tuple(v/q for v in a)
    ans = (1., 0., 0., 1.)
    term = ans
    for k in range(1, 110):
        term = tuple(v/k for v in matmul(term, z))
        ans = tuple(x+y for x,y in zip(ans, term))
        if max(map(abs, term)) < 1e-17:
            break
    else:
        raise AssertionError('Taylor convergence')
    for _ in range(scale):
        ans = matmul(ans, ans)
    return ans


def formula_lambda(r,h,g,t,d):
    """t=half-period, h=half the migration-rate sum, d=half difference."""
    minus = math.sqrt(max(0.,h*h+g*g-2*g*d))
    plus = math.sqrt(max(0.,h*h+g*g+2*g*d))
    def sinhc(z):
        return math.sinh(z)/z if abs(z) > 1e-12 else (1. + z*z/6.)
    c = (math.cosh(minus*t)*math.cosh(plus*t)
         + (h*h-g*g)*t*t*sinhc(minus*t)*sinhc(plus*t))
    # Protect only against machine precision near the one-way endpoint.
    return r-h+math.acosh(max(1.,c))/(2*t)


def direct_lambda(r,h,g,t,d):
    a, b = h+d, h-d
    first = (t*(r+g-a),t*b,t*a,t*(r-g-b))
    second = (t*(r-g-a),t*b,t*a,t*(r+g-b))
    m = matmul(expm2(second),expm2(first))
    disc = math.hypot(m[0]-m[3],2*math.sqrt(max(0.,m[1]*m[2])))
    rho = (m[0]+m[3]+disc)/2.
    return math.log(rho)/(2*t)


def main():
    rng = random.Random(1379011)
    numeric = 0
    for _ in range(2400):
        h = rng.uniform(.12,2.3)
        g = rng.uniform(.12,2.3)
        t = rng.uniform(.04,2.1)
        d = rng.uniform(-h,h)
        r = rng.uniform(-1.,1.)
        got = formula_lambda(r,h,g,t,d)
        independent = direct_lambda(r,h,g,t,d)
        assert math.isclose(got, independent, rel_tol=1.5e-9, abs_tol=3e-10), (r,h,g,t,d,got,independent)
        numeric += 1

    ordered = 0
    for _ in range(950):
        h = rng.uniform(.15,2.0)
        g = rng.uniform(.2,2.0)
        t = rng.uniform(.05,2.5)
        r = rng.uniform(-.7,.7)
        vals = [formula_lambda(r,h,g,t,h*z/10.) for z in range(11)]
        # The product ab decreases as d increases on this half-interval.
        assert all(x > y-5e-11 for x,y in zip(vals, vals[1:])), (h,g,t, vals)
        assert abs(vals[-1]-r)<2e-10
        assert vals[0]>r
        ordered += 1

    # A sharp degree-of-bias viability transition with negative mean growth.
    h=g=1.; t=2.; r=-.2
    edges=[(0.,2.),(.5,1.5),(1.,1.),(1.5,.5),(2.,0.)]
    expected_signs=[-1,-1,1,-1,-1]
    computed=[]
    for (a,b),sign in zip(edges,expected_signs):
        v=formula_lambda(r,h,g,t,(a-b)/2)
        computed.append(v)
        assert (v>0)-(v<0)==sign, (a,b,v)

    # Equality of source-rate degeneracy and zero-seasonality boundaries.
    for _ in range(100):
        h=rng.uniform(.1,2.)
        t=rng.uniform(.1,2.)
        d=rng.uniform(-h,h)
        r=rng.uniform(-1.,1.)
        assert abs(formula_lambda(r,h,0.,t,d)-r)<1e-9
    print('PASS: 2,400 independent matrix-exponential comparisons')
    print('PASS: 950 ordered migration-rate families and one-way endpoints')
    print('PASS: sharp sample viability signs: '+', '.join(f'{v:.9f}' for v in computed))
    print('PASS: 100 zero-seasonality equalities (excluded from strict theorem)')
    print('Note: numerical tests do not prove the infinite-parameter theorem.')

if __name__=='__main__':
    main()
