"""Independent finite numerical corroboration of the sharp angle-profile formulas.

Only Python's standard library is required. This is not an infinite proof.
"""
import math


def bisect(fun, lo, hi, iterations=120):
    vlo = fun(lo)
    vhi = fun(hi)
    assert vlo <= 0 <= vhi, (lo, hi, vlo, vhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if fun(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


u = bisect(lambda z: z**4 + z**3 - 1, .8, 5/6)
tcrit = 1 / (2*u*u)
thetacrit = math.acos(tcrit)
assert .81917 < u < .81918
assert 41.831 < math.degrees(thetacrit) < 41.832


def ratio(a, b):
    assert 0 < a <= b <= 1 and a+b > 1
    return max(a/b, b, 1/(1+b*b-a*a))


def F(theta):
    t = math.cos(theta)
    C = 1/(2*t)
    if theta <= thetacrit:
        b = math.sqrt(C)
    elif theta < math.pi/3 - 1e-12:
        b = bisect(lambda z: z**4-z*z+2*t*z-1, math.sqrt(C), 1)
    else:
        b = 1
    return b


for j in range(1, 601):
    theta = (math.pi / 3) * j / 601
    b = F(theta)
    a = math.sqrt(1+b*b-2*b*math.cos(theta))
    assert a <= b + 1e-11 and a+b > 1
    assert abs(ratio(a, b)-b) < 2e-10, (j, a, b, ratio(a,b))
    min_angle = math.acos((1+b*b-a*a)/(2*b))
    assert abs(min_angle-theta) < 2e-8, (theta,min_angle)
    C = 1/(2*math.cos(theta))
    for k in range(1, 121):
        test_b = C+(1-C)*k/121
        test_a = math.sqrt(1+test_b**2-2*test_b*math.cos(theta))
        assert ratio(test_a,test_b) >= b - 2e-10
        # Raising the shortest side cannot lower the optimum.
        for step in (.05,.5,.95):
            a2=test_a+step*(test_b-test_a)
            if a2+test_b > 1+1e-12:
                assert ratio(a2,test_b) >= ratio(test_a,test_b) - 1e-12

s = math.sin(thetacrit)
left = u*s/(2*tcrit)
right = 2*u*s/(4*u**3-2*u+2*tcrit)
assert right > left and (right-left) > .16
print('angle transition (degrees):', math.degrees(thetacrit))
print('threshold fraction:', u)
print('left derivative:', left)
print('right derivative:', right)
print('test: passed')
