"""Independent polygon-clipping checks for the exact regular-hexagon plank profile.

Run with Python 3: python verify_hexagon.py
The theorem and proofs are in RESULT.md. Sampled tests do not establish
uniqueness or infinite-parameter optimality; those follow analytically.
"""
import math
import random

SQ3 = math.sqrt(3)
AREA = 3*SQ3/2
VERTICES = [(math.cos(k*math.pi/3), math.sin(k*math.pi/3)) for k in range(6)]


def polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    return abs(sum(p[0]*q[1] - p[1]*q[0]
                   for p,q in zip(vertices, vertices[1:] + vertices[:1])))/2


def clip_halfplane(vertices, normal, threshold):
    # Retain points with dot(normal,x) <= threshold.
    result = []
    for p,q in zip(vertices, vertices[1:] + vertices[:1]):
        a = p[0]*normal[0] + p[1]*normal[1] - threshold
        b = q[0]*normal[0] + q[1]*normal[1] - threshold
        if a <= 1e-14:
            result.append(p)
        if a*b < -1e-14:
            t = a/(a-b)
            result.append((p[0] + t*(q[0]-p[0]),
                           p[1] + t*(q[1]-p[1])))
    return result


def geometric_fraction(width, theta):
    n = (math.cos(theta), math.sin(theta))
    poly = clip_halfplane(VERTICES, n, width/2)
    poly = clip_halfplane(poly, (-n[0], -n[1]), width/2)
    return polygon_area(poly)/AREA


def cap_formula_fraction(width, theta):
    s=width/2
    a=math.cos(theta)
    b=math.cos(math.pi/3-theta)
    c=math.cos(math.pi/3+theta)
    if s <= c:
        excluded = 3*SQ3/4 - SQ3*s/a
    elif s <= b:
        excluded = SQ3/4*((a+b-s)**2/(a*b)-1)
    else:
        excluded = SQ3/4*(a-s)**2/(b*c)
    return 1-2*excluded/AREA


def claimed_profile(width):
    if not 0 < width < SQ3:
        raise ValueError('must have 0 < width < sqrt(3)')
    if width <= SQ3/2:
        return 4*width/(3*SQ3)-width**2/9, math.pi/6
    if width <= 1:
        u=3*(1-width**2)/(width**2+math.sqrt(4*width**2-3))
        return (1+width**2)/3, math.atan(u/SQ3)
    if width <= 1.5:
        return 1-(2-width)**2/3, 0.0
    return 2/3+width**2/9, math.atan(math.sqrt(4*width**2-9)/3)


def run():
    rng=random.Random(199726)
    assert abs(polygon_area(VERTICES)-AREA)<1e-13
    widths=[SQ3/2, 1.0, 1.5, 0.01, SQ3-0.001]
    widths += [SQ3*rng.random()*0.999 for _ in range(1200)]
    checks=0
    for w in widths:
        value,theta=claimed_profile(w)
        assert 0 <= theta <= math.pi/6+1e-14
        assert abs(geometric_fraction(w,theta)-value)<2e-12, (w,theta,value)
        for _ in range(10):
            t=rng.random()*math.pi/6
            assert abs(geometric_fraction(w,t)-cap_formula_fraction(w,t))<2e-12, (w,t)
            assert geometric_fraction(w,t)<=value+2e-12, (w,t,value)
            checks+=1
    # The profile is continuously joined at all three exact thresholds.
    def f1(w): return 4*w/(3*SQ3)-w*w/9
    def f2(w): return (1+w*w)/3
    def f3(w): return 1-(2-w)**2/3
    def f4(w): return 2/3+w*w/9
    assert abs(f1(SQ3/2)-f2(SQ3/2))<2e-15
    assert abs(f2(1)-f3(1))<2e-15
    assert abs(f3(1.5)-f4(1.5))<2e-15
    print('PASS: independent planar clipping and cap formula on',checks,'competitor angles')
    print('PASS: optimum predictions across all four regimes and three joins')
    print('NOTE: all-parameter optimality is proved analytically in RESULT.md')

if __name__=='__main__':
    run()
