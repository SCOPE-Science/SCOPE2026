import math, random

def profile(n, theta):
    t = math.tan(theta)
    return (1.0/math.cos(theta))/((1.0+math.sqrt((n-2)/n)*t)*(1.0-t/math.sqrt(n*(n-2)))**(n-2))

def ratio(n, theta, v):
    k = math.sqrt((n-1)/n)*math.tan(theta)
    p = 1.0
    for x in v:
        p *= 1.0-k*x
    return (1.0/math.cos(theta))/p

def equality_vector(n):
    a = 1.0/math.sqrt((n-1)*(n-2))
    b = -math.sqrt((n-2)/(n-1))
    return [b]+[a]*(n-2)

rng = random.Random(20261003)
for n in range(3, 11):
    theta0 = math.atan(math.sqrt((n-2)/n))
    for frac in (0.05, 0.2, 0.5, 0.9):
        theta = frac*theta0
        eq = equality_vector(n)
        assert abs(sum(eq)) < 1e-12
        assert abs(sum(x*x for x in eq)-1.0) < 1e-12
        assert abs(ratio(n, theta, eq)-profile(n, theta)) < 2e-12
        q = 1.0/math.sqrt(n*(n-1))
        assert all(-q*math.cos(theta)+x*math.sin(theta) < 0 for x in eq)
        for _ in range(1500):
            z = [rng.gauss(0.0, 1.0) for _ in range(n-1)]
            mean = sum(z)/(n-1)
            z = [x-mean for x in z]
            norm = math.sqrt(sum(x*x for x in z))
            if norm < 1e-14:
                continue
            z = [x/norm for x in z]
            if all(-q*math.cos(theta)+x*math.sin(theta) < 0 for x in z):
                assert ratio(n, theta, z) + 2e-11 >= profile(n, theta)
print('VERIFY_OK')
