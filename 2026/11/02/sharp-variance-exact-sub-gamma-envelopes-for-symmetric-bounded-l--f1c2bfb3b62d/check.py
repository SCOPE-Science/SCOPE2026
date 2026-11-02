"""Independent finite checks of a sharp symmetric bounded-jump sub-gamma envelope.

Run: python3 check.py. The asymptotic and global analytic arguments are in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial

checks = 0

def verify(condition):
    global checks
    assert condition
    checks += 1

def bounds_hyperbolic(t, n=35):
    assert t >= 0
    c = sum((t ** (2*k) / factorial(2*k) for k in range(n+1)), Q())
    s = sum((t ** (2*k+1) / factorial(2*k+1) for k in range(n+1)), Q())
    cnext = t**(2*n+2) / factorial(2*n+2)
    snext = t**(2*n+3) / factorial(2*n+3)
    cratio = t*t / ((2*n+3)*(2*n+4))
    sratio = t*t / ((2*n+4)*(2*n+5))
    verify(cratio < 1 and sratio < 1)
    return (c, c+cnext/(1-cratio)), (s, s+snext/(1-sratio))

def sign_enclosure(t):
    (cl, cu), (sl, su) = bounds_hyperbolic(t)
    al, au = cl-1, cu-1
    lo = t**3*sl - t*t*au - 2*au*au
    hi = t**3*su - t*t*al - 2*al*al
    verify(lo < hi)
    return lo, hi

# These strictly signed rational enclosures certify an interior optimizer bracket.
lo, hi = sign_enclosure(Q(382237, 100000))
verify(lo > 0)
lo, hi = sign_enclosure(Q(382238, 100000))
verify(hi < 0)

# Exact coefficient identity used to prove strict monotonicity of A/B.
for n in range(1, 201):
    a = Q(2, factorial(2*n+2))
    b = a + sum((Q(2, factorial(2*j+2))*Q(2, factorial(2*(n-j)+2)) for j in range(1,n)), Q())
    C = Q(4**(n+2)-4, (2*n+3)*(2*n+4)) - 1
    verify(b/a == C)
    verify(C > 0)
    if n >= 2:
        prev = Q(4**(n+1)-4, (2*n+1)*(2*n+2))-1
        verify(C/n > prev/(n-1))

# Positivity of the polynomial in the exact coefficient-ratio recursion.
for n in range(1,301):
    q = 4*n*(2*n+3)*(2*n+4)-(n+1)*(2*n+5)*(2*n+6)
    verify(q == 8+(n-1)*(12*n*n+42*n+38))
    verify(q > 0)

# Taylor enclosure for the hyperbolic normalized remainder and its mixture.
def r_bounds(z):
    if z == 0:
        return Q(1), Q(1)
    (cl, cu), _ = bounds_hyperbolic(z)
    return 2*(cl-1)/(z*z), 2*(cu-1)/(z*z)

for z in [Q(k,4) for k in range(1,21)]:
    rl, ru = r_bounds(z)
    verify(rl >= 1 and rl < ru)
    for alpha in [Q(0),Q(1,4),Q(1,2),Q(3,4)]:
        al, au = r_bounds(alpha*z)
        verify(au < ru or alpha==0 and au == 1)
        for eta in [Q(1,4),Q(1,2),Q(3,4)]:
            ml = (1-eta)*rl+eta*al
            mu = (1-eta)*ru+eta*au
            verify(ml>1 and mu<ru)

print('PASS: %d exact rational assertions' % checks)
print('optimizer root is in (3.82237,3.82238) from signed rational Taylor bounds')
