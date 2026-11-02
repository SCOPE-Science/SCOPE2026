"""Exact finite checks for a two-component symmetric-link majority theorem.

The theorem for arbitrary link functions and all parameters is proved analytically
in RESULT.md; finite checks here independently test its logistic specialization.
"""
from fractions import Fraction as Q
from itertools import product

nchecks = 0

def check(test, description):
    global nchecks
    nchecks += 1
    if not test:
        raise AssertionError(f'assertion {nchecks}: {description}')


def prob(w, a_i, a_j, b_i, b_j):
    return w * a_i / (a_i + a_j) + (1 - w) * b_i / (b_i + b_j)


def cycle(w, a, b):
    return (prob(w,a[0],a[1],b[0],b[1]),
            prob(w,a[1],a[2],b[1],b[2]),
            prob(w,a[2],a[0],b[2],b[0]))

# Special exact rational strict cycle in two PL components.
w = Q(1,3)
a = (Q(100), Q(10), Q(1))
b = (Q(1), Q(2), Q(4))
pab, pbc, pca = cycle(w,a,b)
check(pab == Q(52,99), 'exact AB probability')
check(pbc == Q(52,99), 'exact BC probability')
check(pca == Q(271,505), 'exact CA probability')
check(all(x > Q(1,2) for x in (pab,pbc,pca)), 'strict cyclic majority')

# Explicit family for every nonhalf rational component weight. The positive
# k bound is deduced algebraically in the proof, not from this sampling.
for j in range(1,128):
    w = Q(j,256)
    q = 1-2*w
    t = (1-w)/q
    bound = (3-4*w)/q
    k = bound.numerator // bound.denominator + 2
    a = (Q(k*k), Q(k), Q(1))
    b = (Q(1), t, t*t)
    r1,r2,r3=cycle(w,a,b)
    check(r1 == r2, 'two adjacent probabilities coincide')
    check(r1 > Q(1,2), 'AB majority')
    check(r3 > Q(1,2), 'CA majority')
    check(t > 1 and t*t*q > 1 and t*q < 1, 'analytic parameter window')
    # Swap class labels to test the opposite unequal weight as well.
    rr=cycle(1-w,b,a)
    check(rr == (r1,r2,r3), 'class swap identity')

# Full enumeration of finite 3-alternative worth arrays for the 50:50 case.
# Ties must occur precisely when score products tie, not just generically.
values = (Q(1),Q(2),Q(3),Q(5))
for data in product(values,repeat=6):
    a, b = data[:3], data[3:]
    for i,j in ((0,1),(1,2),(0,2)):
        p = prob(Q(1,2),a[i],a[j],b[i],b[j])
        margin = p - Q(1,2)
        product_diff=a[i]*b[i]-a[j]*b[j]
        check((margin>0)-(margin<0) == (product_diff>0)-(product_diff<0),
              'product-order criterion including ties')
        exact=(a[i]*b[i]-a[j]*b[j]) / (2*(a[i]+a[j])*(b[i]+b[j]))
        check(margin==exact, 'exact mixture identity')

print(f'PASS: {nchecks} exact rational assertions; analytic universal proof is in RESULT.md')
