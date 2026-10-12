"""Independent finite checks for two-uniform integrated-tail envelopes.

Uses only the Python standard library; finite checks do not prove universal claims.
"""
from fractions import Fraction
from math import sqrt


def positive_part(x):
    return max(x, 0)


def closed_rational(b, c, d):
    assert b >= c > 0 and b*b + c*c > 0 and d >= 0
    return (positive_part(b+c-d)**3 - positive_part(b-c-d)**3)/(24*b*c)


def direct_rational(b, c, d):
    # Density for S=bU+cV is 1/(2b) on [-b+c,b-c],
    # and (b+c-x)/(4bc) on [b-c,b+c].
    low = b-c
    high = b+c
    result = Fraction(0)
    left = max(d, -low)
    if left < low:
        result += ((low-d)**2-(left-d)**2)/(4*b)
    lo = max(d,low)
    if lo < high:
        # Integral (x-d)(high-x) / (4 b c) dx
        def anti(x):
            return (high+d)*x*x/2 - x*x*x/3 - d*high*x
        result += (anti(high)-anti(lo))/(4*b*c)
    return result


def direct_float(b,c,d):
    if c < 1e-12:
        return max(b-d, 0.0)**2/(4*b)
    return (max(b+c-d,0.0)**3-max(b-c-d,0.0)**3)/(24*b*c)


def low_formula(d):
    q1=1/(2*sqrt(2)); q2=1/sqrt(5); q3=1/sqrt(3)
    if d<=q1: return (sqrt(2)-d)**3/12
    if d<=q2:
        s=sqrt(d*d+3)-d
        return (s-d)**3/(12*(s*s-1))
    if d<=q3:
        b=sqrt((1+3*d*d)/2)
        return b/3-d/2
    return max(1-d,0)**2/4


def upper_formula(d):
    return max(max(1-d,0)**2/4,max(sqrt(2)-d,0)**3/12)


def run():
    n=0
    # Exact rational convolution checks, testing each support-chamber.
    for b,c in [(Fraction(3,5),Fraction(2,5)),(Fraction(7,6),Fraction(1,6)),(Fraction(1),Fraction(1))]:
        for d in [Fraction(0),Fraction(1,10),Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(5,3),Fraction(3)]:
            assert direct_rational(b,c,d) == closed_rational(b,c,d),(b,c,d)
            n+=1
    # Actual optimization against a grid of independent orientations.
    import math
    grid=[1/sqrt(2)+(1-1/sqrt(2))*j/12000 for j in range(12001)]
    strikes=[0,.01,.1,.2,.30,1/(2*sqrt(2)),.36,.40,1/sqrt(5),.46,.5,1/sqrt(3),.6,.75,.9,1,1.2,1.37,sqrt(2),1.5]
    for d in strikes:
        vals=[direct_float(b,math.sqrt(max(0,1-b*b)),d) for b in grid]
        assert min(vals)>=low_formula(d)-2e-11,(d,min(vals),low_formula(d))
        assert min(vals)<=low_formula(d)+3e-8,(d,min(vals),low_formula(d))
        assert max(vals)<=upper_formula(d)+2e-11,(d,max(vals),upper_formula(d))
        assert max(vals)>=upper_formula(d)-3e-8,(d,max(vals),upper_formula(d))
        n+=1
    # Formula joinings at the three minimum thresholds and maximum crossover.
    q1=1/(2*sqrt(2));q2=1/sqrt(5);q3=1/sqrt(3)
    for d in (q1,q2,q3):
        h=5e-8
        assert abs(low_formula(d-h)-low_formula(d+h))<h*1.5
        n+=1
    lo,hi=.3,.65
    for _ in range(90):
        mid=(lo+hi)/2
        gap=3*(1-mid)**2-(sqrt(2)-mid)**3
        if gap>0: lo=mid
        else: hi=mid
    delta=(lo+hi)/2
    assert abs(3*(1-delta)**2-(sqrt(2)-delta)**3)<1e-12
    assert 0.47<delta<0.48
    n+=1
    print(f"PASS: {n} independent rational/grid/transition checks; crossover={delta:.14f}")

if __name__=='__main__':
    run()
