"""Independent finite checks for the regular-tetrahedron random shadow-diameter law.

Run with Python 3; uses only the standard library. Finite checks are not a proof.
"""
import math
import random

PI = math.pi
LOW = 3/math.sqrt(10)
V = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
V = [tuple(c/(2*math.sqrt(2)) for c in p) for p in V]

def direct_projected_diameter(u):
    best = 0.0
    for i in range(4):
        for j in range(i):
            diff = [V[i][k]-V[j][k] for k in range(3)]
            dot = sum(diff[k]*u[k] for k in range(3))
            d2 = sum(v*v for v in diff)-dot*dot
            best = max(best, d2)
    return math.sqrt(best)

def reduced_diameter(u):
    a, b, c = sorted(map(abs,u))
    m = min(b-a,c-b)
    return math.sqrt(1-m*m/2)

def cdf(d):
    if d <= LOW: return 0.0
    if d >= 1.0: return 1.0
    r = math.sqrt(2*(1-d*d))
    zmax = math.sqrt((1-2*r*r)/3)-r
    def arc(z):
        x = r/math.sqrt(2*(1-z*z))
        y = (z+r)/math.sqrt(1-z*z)
        return max(0.0, math.acos(min(1,max(-1,x)))-PI/4-
                   math.asin(min(1,max(-1,y))))
    # Composite midpoint quadrature is independent of the continuous proof.
    N = 16000
    h = zmax/N
    return (12/PI)*h*sum(arc((i+0.5)*h) for i in range(N))

def main():
    rng = random.Random(19173)
    sample = []
    for _ in range(30000):
        x,y,z = (rng.gauss(0,1) for k in range(3))
        norm=math.sqrt(x*x+y*y+z*z)
        u=(x/norm,y/norm,z/norm)
        d = direct_projected_diameter(u)
        assert abs(d-reduced_diameter(u))<5e-14
        sample.append(d)
    print('DIRECT_SIX_EDGE_PROJECTION_AGREEMENT_OK',len(sample))
    for d in [0.951,0.96,0.975,0.99,0.999]:
        theoretical = cdf(d)
        empirical = sum(v<=d for v in sample)/len(sample)
        assert abs(empirical-theoretical)<0.018
        print('NUMERICAL_CDF_AGREEMENT_OK', d, round(theoretical,7),round(empirical,7))
    for e in [1e-6,1e-7]:
        actual=(1-cdf(1-e))/math.sqrt(e)
        assert abs(actual/(6*math.sqrt(2))-1)<0.006
    for e in [1e-4,3e-5]:
        actual=cdf(LOW+e)/e**2
        assert abs(actual/(150*math.sqrt(5)/PI)-1)<0.003
    print('BOTH_SHARP_ENDPOINT_ASYMPTOTICS_OK')
    u=(2/math.sqrt(5),1/math.sqrt(5),0)
    assert abs(direct_projected_diameter(u)-LOW)<1e-14
    assert cdf(LOW)==0 and cdf(1)==1
    print('EXACT_MINIMIZING_DIRECTION_AND_SUPPORT_OK')
    print('ALL_RANDOM_TETRAHEDRON_SHADOW_DIAMETER_CHECKS_OK')

if __name__=='__main__': main()
