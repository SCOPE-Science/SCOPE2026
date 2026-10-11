from fractions import Fraction
import random, cmath

# Exact algebraic checks for the local zero-sum sixth-moment lemma.
def alpha(m):
    return Fraction((m-1)**5 + 1, m**3 * (m-1)**2)

def two_value_ratio(m, r):
    # r copies of a and m-r copies of -b, normalized to squared l2 mass 1.
    a2 = Fraction(m-r, r*m)
    b2 = Fraction(r, m*(m-r))
    return r*a2**3 + (m-r)*b2**3

newton_checks = 0
for x in range(-4,5):
    for y in range(-4,5):
        for z in range(-4,5):
            e1=x+y+z; e2=x*y+x*z+y*z; e3=x*y*z
            lhs=x**6+y**6+z**6
            rhs=(e1**6-6*e1**4*e2+6*e1**3*e3+9*e1**2*e2**2
                 -12*e1*e2*e3-2*e2**3+3*e3**2)
            assert lhs == rhs
            newton_checks += 1

discrete_checks = 0
for m in range(2,201):
    best=max(two_value_ratio(m,r) for r in range(1,m))
    assert best == alpha(m)
    assert two_value_ratio(m,1) == alpha(m)
    assert two_value_ratio(m,m-1) == alpha(m)
    poly=m**4-5*m**3+10*m**2-10*m+5
    assert alpha(m)*m*m == Fraction(poly,(m-1)**2)
    discrete_checks += m-1

# Numerical stress tests are regression checks only; the proof is analytic.
rng=random.Random(74243)
random_checks=0
max_excess=-1.0
for m in range(2,21):
    a=float(alpha(m))
    for _ in range(300):
        z=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(m-1)]
        z.append(-sum(z))
        s2=sum(abs(w)**2 for w in z)
        if s2 == 0:
            continue
        ratio=sum(abs(w)**6 for w in z)/(s2**3)
        max_excess=max(max_excess,ratio-a)
        assert ratio <= a + 2e-12
        random_checks += 1

# Equality vectors and Fourier-scale constants.
equality_checks=0
for m in range(2,81):
    z=[m-1]+[-1]*(m-1)
    ratio=Fraction(sum(abs(w)**6 for w in z), sum(abs(w)**2 for w in z)**3)
    assert ratio == alpha(m)
    for k in range(1,16):
        N=k*m
        K6six=Fraction(k*k*(m**4-5*m**3+10*m**2-10*m+5),(m-1)**2)
        assert K6six == alpha(m)*N*N
        equality_checks += 1

print(f"VERIFY_OK newton_exact={newton_checks} two_value_exact={discrete_checks} random_zero_sum={random_checks} equality_scale={equality_checks} max_random_excess={max_excess:.3e}")
