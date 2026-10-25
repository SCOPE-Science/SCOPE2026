"""Supplementary checks for dual-edge Reuleaux arclength comparisons.

Finite computations illustrate the analytic inequalities; they do not prove
universal statements. Requires Python 3, scipy, sympy.
"""
import math
from scipy.integrate import quad
from sympy import symbols, sqrt, simplify

def lengths(a, b):
    q = a*a + b*b
    c = a / math.sqrt(q)
    d = b / math.sqrt(q)
    t0 = math.asin(math.sqrt(q)/2)
    ea = 2*c*quad(lambda t: math.sqrt(1-d*d*math.sin(t)**2), 0, t0, epsabs=1e-13)[0]
    eb = 2*d*quad(lambda t: math.sqrt(1-c*c*math.sin(t)**2), 0, t0, epsabs=1e-13)[0]
    ra = math.sqrt(1-b*b/4)
    rb = math.sqrt(1-a*a/4)
    ca = 2*ra*math.asin(a/(2*ra))
    cb = 2*rb*math.asin(b/(2*rb))
    return ea, eb, ca, cb

def coeff(a):
    return (6-a*a)/(4*a*a)*math.asin(a/2)-3*math.sqrt(4-a*a)/(8*a)

def run():
    A, B = symbols('A B', positive=True)
    h = sqrt(1-(A+B)/4)
    r = sqrt(1-B/4)
    c2 = A/(A+B)
    d2 = B/(A+B)
    expr = r-h*d2-c2
    target = A*B/(16*(1+r)*(r+h)*(1+h))
    assert simplify(expr-target) == 0
    n = 0
    for ia in range(1, 41):
        for ib in range(1, 41):
            a = ia/40
            b = ib/40
            ea, eb, ca, cb = lengths(a, b)
            assert ea < ca + 3e-12 and eb < cb+3e-12
            assert ea+eb > max(ca,cb)-1e-12
            assert ca+cb > ea+eb-1e-12
            assert ca-ea < b/8 + 1e-12
            assert cb-eb < a/8 + 1e-12
            n += 1
    ea, eb, ca, cb = lengths(1,1)
    assert abs(3*(ea+eb)-6.348573008355378)<1e-9
    assert abs(3*ca-3.198126379334406)<1e-9
    a=1.0
    samples=[]
    for b in [0.1,0.05,0.025,0.0125]:
        ea,eb,ca,cb=lengths(a,b)
        samples.append((b, (ca-ea)/(b*b)))
    print('midpoint identity: exact symbolic PASS')
    print('strict pair comparisons: checked',n,'parameter pairs')
    print('quadratic coefficient at a=1:',coeff(a))
    print('approach ratios:',samples)
    print('tetrahedral singular length, ellipses:',3*(lengths(1,1)[0]+lengths(1,1)[1]))
    print('tetrahedral singular length, Meissner:',3*lengths(1,1)[2])
if __name__=='__main__':
    run()
