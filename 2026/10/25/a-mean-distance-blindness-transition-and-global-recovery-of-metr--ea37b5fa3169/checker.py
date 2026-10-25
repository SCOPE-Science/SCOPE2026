"""Independent finite checks of analytic formulas for distances on a metric dumbbell.

A metric dumbbell consists of two loops joined by one bridge; length sampling
uses three consecutive edge coordinates. This script uses the Python standard
library. The theorem itself is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def conditional_integrals(a, b, c):
    """Unnormalized integrals by disjoint ordered edge-pair categories."""
    loop_aa_1, loop_bb_1 = a**3 / 4, b**3 / 4
    bridge_1 = c**3 / 3
    loop_bridge_1 = 2 * a * c * (a / 4 + c / 2) + 2 * b * c * (b / 4 + c / 2)
    loop_loop_1 = 2 * a * b * (c + (a + b) / 4)
    i1 = loop_aa_1 + loop_bb_1 + bridge_1 + loop_bridge_1 + loop_loop_1

    loop_aa_2, loop_bb_2 = a**4 / 12, b**4 / 12
    bridge_2 = c**4 / 6
    loop_bridge_2 = (2 * a * c * (a**2 / 12 + a * c / 4 + c**2 / 3)
                     + 2 * b * c * (b**2 / 12 + b * c / 4 + c**2 / 3))
    loop_loop_2 = 2 * a * b * (c**2 + c * (a+b) / 2
                              + (a**2 + b**2) / 12 + a*b / 8)
    i2 = loop_aa_2 + loop_bb_2 + bridge_2 + loop_bridge_2 + loop_loop_2
    return i1, i2


def symmetric_integrals(a, b, c):
    s, p = a+b, a*b
    i1 = (s**3 / 4 + c*s**2 / 2 + s*c**2 + c**3 / 3
          + p*(c-s/4))
    i2 = (s**4 / 12 + c*s**3 / 6 + c**2*s**2 / 2
          + 2*s*c**3 / 3 + c**4 / 6
          + p*(-s*s/6+c*s/2+c*c) + p*p/12)
    return i1, i2


def box_convolution(t, u, v):
    """Convolution of indicators of [0,u] and [0,v] at t."""
    return max(F(0), min(u, t) - max(F(0), t-v))


def pair_distance_density(t, a, b, c):
    """Continuous-density representative away from its finitely many knots."""
    L = a+b+c
    aa, bb = a/2, b/2
    numerator = (2*a*int(0<t<aa)+2*b*int(0<t<bb)
                 +2*max(F(0),c-t)
                 +4*box_convolution(t,aa,c)
                 +4*box_convolution(t,bb,c)
                 +8*box_convolution(t-c,aa,bb))
    return numerator / L**2


def exact_density_moment(k, a, b, c):
    """Integrate the piecewise-linear density exactly (k=0, 1, 2)."""
    aa, bb = a/2, b/2
    knots=sorted({F(0),aa,bb,c,aa+c,bb+c,c+aa+bb})
    total=F(0)
    for lo,hi in zip(knots,knots[1:]):
        z1=(2*lo+hi)/3
        z2=(lo+2*hi)/3
        f1=pair_distance_density(z1,a,b,c)
        f2=pair_distance_density(z2,a,b,c)
        slope=(f2-f1)/(z2-z1)
        intercept=f1-slope*z1
        # Since the knots include all jumps and changes of slope, this
        # integral is exact on each open interval.
        total+=(slope*(hi**(k+2)-lo**(k+2))/(k+2)
                +intercept*(hi**(k+1)-lo**(k+1))/(k+1))
    return total


def distance(x, y, a, b, c):
    def locate(t):
        if t < a:
            return ('a', t)
        if t < a+b:
            return ('b', t-a)
        return ('c', t-a-b)

    cat_x, pos_x = locate(x)
    cat_y, pos_y = locate(y)
    if cat_x == cat_y:
        if cat_x == 'c':
            return abs(pos_x-pos_y)
        circumference = a if cat_x == 'a' else b
        delta = abs(pos_x-pos_y)
        return min(delta, circumference-delta)
    if cat_x == 'c':
        return (pos_x if cat_y == 'a' else c-pos_x) + min(pos_y,(a if cat_y == 'a' else b)-pos_y)
    if cat_y == 'c':
        return (pos_y if cat_x == 'a' else c-pos_y) + min(pos_x,(a if cat_x == 'a' else b)-pos_x)
    return (min(pos_x, (a if cat_x == 'a' else b)-pos_x)
            + c + min(pos_y, (a if cat_y == 'a' else b)-pos_y))


def midpoint_grid_moments(a, b, c, n=260):
    length = a+b+c
    points = [length*(k+0.5)/n for k in range(n)]
    sum_1 = sum_2 = 0.0
    for x in points:
        for y in points:
            value = distance(x,y,a,b,c)
            sum_1 += value
            sum_2 += value*value
    return sum_1/n**2, sum_2/n**2


def main():
    count = 0
    for a,b,c in product((F(1),F(2),F(3),F(5),F(7)),
                         (F(1),F(2),F(4),F(7)),
                         (F(1,2),F(1),F(3),F(5))):
        assert conditional_integrals(a,b,c) == symmetric_integrals(a,b,c)
        integrated=tuple(exact_density_moment(k,a,b,c) for k in (0,1,2))
        analytic=tuple(x/(a+b+c)**2 for x in symmetric_integrals(a,b,c))
        assert integrated==(F(1),)+analytic, (a,b,c,integrated,analytic)
        assert a+b+c > 0
        s,p,L = a+b,a*b,a+b+c
        i1,i2 = symmetric_integrals(a,b,c)
        assert i1>0 and i2>0
        if c!=s/4:
            p_reconstructed = (i1-(s**3/4+c*s*s/2+s*c*c+c**3/3))/(c-s/4)
            assert p_reconstructed == p
        count += 1
    for a,b in product((F(1),F(2),F(3),F(5),F(7)),repeat=2):
        c=(a+b)/4
        i1,i2 = symmetric_integrals(a,b,c)
        s,p = a+b,a*b
        assert i1 == s**3/4+c*s*s/2+s*c*c+c**3/3
        assert i2 == (s**4/12+c*s**3/6+c*c*s*s/2+2*s*c**3/3+c**4/6 + p*s*s/48+p*p/12)
    assert symmetric_integrals(F(1),F(3),F(1))[0] == symmetric_integrals(F(2),F(2),F(1))[0] == F(85,3)
    assert symmetric_integrals(F(1),F(3),F(1))[1] == F(535,12)
    assert symmetric_integrals(F(2),F(2),F(1))[1] == F(91,2)
    for a,b,c in [(1.0,3.0,1.0),(2.0,2.0,1.0),(0.6,4.2,0.7),(3.0,4.0,2.0)]:
        L = a+b+c
        q1,q2 = midpoint_grid_moments(a,b,c)
        p1,p2 = symmetric_integrals(a,b,c)
        assert abs(q1 - p1/L**2) < 0.014, (a,b,c,'mean',q1,p1/L**2)
        assert abs(q2 - p2/L**2) < 0.035, (a,b,c,'second',q2,p2/L**2)
    print(f'PASS: {count} rational-category and full-density integral identities, 25 critical-ratio identities,')
    print('      3 exact ambiguity checks, 4 independent deterministic grid comparisons.')
    print('Limits: these are finite checks; the general result uses the analytic proof.')

if __name__=='__main__':
    main()
