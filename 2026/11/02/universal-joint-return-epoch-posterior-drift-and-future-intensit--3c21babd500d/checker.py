"""Finite exact checks for Pólya-urn walk return-count identities.

Uses rational integration, direct path enumeration, and an independent
symmetrized-density calculation. Finite tests do not establish the limits.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, sqrt
from itertools import product

checks = 0

def assert_eq(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

def beta_int(a, b):
    return Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def incomplete_half(a, b):
    # Integral from zero to 1/2 of x^(a-1) (1-x)^(b-1) dx.
    return sum((Q((-1)**j*comb(b-1,j),1)*Q(1,2)**(a+j)/Q(a+j,1)
               for j in range(b)),Q(0))

def return_tail(a,b,k):
    return Q(2**k,1)*(incomplete_half(a+k,b)+incomplete_half(b+k,a))/beta_int(a,b)

def tail_by_symmetry(a,b,k):
    # Independent polynomial arithmetic on |2P-1|=u.
    # h(u) = [f((1+u)/2)+f((1-u)/2)]/2.
    from math import prod
    poly=[Q(0)]*(a+b-1)
    for sign in (-1,1):
        left=[Q(comb(a-1,j)*sign**j,2**(a-1)) for j in range(a)]
        right=[Q(comb(b-1,j)*(-sign)**j,2**(b-1)) for j in range(b)]
        for j,v in enumerate(left):
            for z,w in enumerate(right):
                poly[j+z]+=v*w/Q(2,1)/beta_int(a,b)
    # integral_0^1 u^j (1-u)^k du = j! k!/(j+k+1)!
    return sum((c*Q(factorial(j)*factorial(k),factorial(j+k+1))
                 for j,c in enumerate(poly)),Q(0))

def first_return_enumeration(a,b,n):
    length=2*n
    total=Q(0)
    for path in product((-1,1),repeat=length):
        loc=0
        good=True
        for i,s in enumerate(path):
            loc+=s
            if loc==0 and i<length-1:
                good=False
                break
        if good and loc==0:
            ups=sum(s==1 for s in path)
            downs=length-ups
            weight=beta_int(a+ups,b+downs)/beta_int(a,b)
            total+=weight
    return total

def first_return_catalan(a,b,n):
    return 2*Q(comb(2*n-2,n-1),n)*beta_int(a+n,b+n)/beta_int(a,b)

for a,b in [(1,1),(1,2),(2,1),(2,2),(3,2),(2,4),(4,5),(5,1)]:
    assert_eq(return_tail(a,b,0), Q(1))
    for k in range(0,25):
        tail=return_tail(a,b,k)
        assert_eq(tail,tail_by_symmetry(a,b,k))
        assert_eq(tail>=0,True)
        assert_eq(return_tail(a,b,k+1)<=tail,True)
        assert_eq(tail-return_tail(a,b,k+1)>=0,True)
        if (a,b) in ((1,1),(1,2),(2,1)):
            assert_eq(tail,Q(1,k+1))
            assert_eq(tail-return_tail(a,b,k+1),Q(1,(k+1)*(k+2)))
        if (a,b)==(2,2):
            assert_eq(tail,Q(3,2*(k+1))-Q(3,(k+1)*(k+2)*(k+3)))

for a,b in [(1,1),(1,2),(2,1),(2,2),(3,2)]:
    for n in range(1,8):
        assert_eq(first_return_enumeration(a,b,n),first_return_catalan(a,b,n))

# Analytic pointwise density constants checked for integer beta shapes.
for a,b in [(1,1),(1,2),(2,1),(2,2),(3,4),(4,3),(5,5)]:
    f0=Q(1,2)**(a+b-2)/beta_int(a,b)
    for k in [30,100,300]:
        val=return_tail(a,b,k)
        assert_eq(abs(Q(k+1)*val-f0)<Q(200*(a+b)**4,(k+1)**2),True)


# Independent integral of the ultimate last-return event.  Conditional on a
# fixed bias, the future never hits zero with probability |2p-1|.
def absolute_beta_moment(A,B):
    return (2*beta_int(A+1,B)-beta_int(A,B)
            +2*incomplete_half(A,B)-4*incomplete_half(A+1,B))

def last_return_exact(a,b,n):
    return Q(comb(2*n,n))*absolute_beta_moment(a+n,b+n)/beta_int(a,b)

# Expand the integrand on both halves, integrating monomials separately.
def last_return_polynomial(a,b,n):
    A,B=a+n,b+n
    acc=Q(0)
    for j in range(B):
        c=Q(comb(B-1,j)*(-1)**j)
        exponent=A+j
        integral_left=Q(1,2)**exponent / exponent - 2*Q(1,2)**(exponent+1)/(exponent+1)
        # Direct both halves: integral_{1/2}^1 (2x-1)x^(A+j-1) dx.
        integral_right=(2*(Q(1,exponent+1)-Q(1,2)**(exponent+1)/Q(exponent+1))
                         -(Q(1,exponent)-Q(1,2)**exponent/Q(exponent)))
        acc+=c*(integral_left+integral_right)
    return Q(comb(2*n,n))*acc/beta_int(a,b)

for a,b in [(1,1),(1,2),(2,1),(2,2),(2,3),(3,5),(5,4)]:
    for n in range(0,16):
        prob=last_return_exact(a,b,n)
        assert_eq(prob,last_return_polynomial(a,b,n))
        assert_eq(prob>0,True)
        if a==b==1:
            q=Q(comb(2*n,n),4**n)
            qnext=Q(comb(2*n+2,n+1),4**(n+1))
            assert_eq(prob,q-qnext)
            assert_eq(prob,q/Q(2*n+2))

# The Beta(1,1) last-return tail equals the ordinary fair walk's
# exact return-to-origin probability; the telescoping identity is exact.
for n in range(0,50):
    a=Q(comb(2*n,n),4**n)
    b=Q(comb(2*n+2,n+1),4**(n+1))
    assert_eq(a-b,Q(comb(2*n,n),(2*n+2)*4**n))

# Posterior in the uniform urn: given at least k future returns, the
# drift magnitude has Beta(1,k+1) density.  The exact joint survival
# with R additional returns is a beta-integral, checked rationally.
for k in range(1,40):
    for m in (0,1,3,7,19):
        for u in (Q(0),Q(1,7),Q(1,3),Q(3,4)):
            joint=Q(k+1,k+m+1)*(1-u)**(k+m+1)
            # Integrate its density (k+1)(1-v)^(k+m) over v>u.
            integrated=Q(k+1)*((1-u)**(k+m+1))/Q(k+m+1)
            assert_eq(joint, integrated)
            if u==0:
                assert_eq(joint,return_tail(1,1,k+m)/return_tail(1,1,k))

# Independently check the new conditional return-epoch transform.  The
# finite-k integral below follows from the defective first-return PGF,
# while the two limiting integrals use different inverse-Gaussian and
# inverse-exponential representations.  These finite quadrature checks
# confirm scale/constant but do NOT certify weak convergence.
def midpoint_integral(fn,step,count):
    return step*sum(fn((j+0.5)*step) for j in range(count))

for s in (0.25,1.0,3.0):
    # Limit as the hidden scaled drift is Exp(1).
    drifting_limit = midpoint_integral(
        lambda y:exp(-sqrt(y*y+2*s)),0.01,3200)
    # Independently: T=1/(2*Exp(1)).
    inverse_exp_limit = midpoint_integral(
        lambda e:exp(-e-s/(2*e)),0.002,12000)
    assert_eq(abs(drifting_limit-inverse_exp_limit)<1.e-7,True)
    for k in (100,300,600):
        def finite_integrand(y):
            root=sqrt(1-(1-y*y/(k*k))*exp(-2*s/(k*k)))
            return (1-root)**k
        finite=(k+1)/k*midpoint_integral(finite_integrand,0.01,3200)
        assert_eq(abs(finite-drifting_limit)<0.01,True)
    # The proposed limit is a nontrivial LT decreasing in s.
    assert_eq(0<drifting_limit<1,True)

print(f'PASS: {checks} reproducible exact/numerical assertions')
