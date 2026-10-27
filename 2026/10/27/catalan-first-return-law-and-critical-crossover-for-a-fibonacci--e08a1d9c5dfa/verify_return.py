"""Reproduce exact first-return identities for a countable affine interval map.

Only Python's standard library is required.  The finite-horizon recursion is
computed directly from the affine branch images, independently of the
closed-form excursion generating function.
"""
from fractions import Fraction as Q
from math import comb, isclose, erf, exp, pi, sqrt

assertions = 0

def check(ok):
    global assertions
    assert ok
    assertions += 1

def branch_image_top(lam, j):
    lo = lam**j
    hi = lam**(j-1)
    denom = (1-lam)* (1 if j==1 else lam if j==2 else lam**2 if j in (3,4) else lam)
    return (hi-lo)/denom

def trans(lam, j, i):
    # Exact intersection of the affine image (0,top_j] with V_i.
    top = branch_image_top(lam,j)
    lo = lam**i
    hi = lam**(i-1)
    return max(Q(0), min(top,hi)-min(top,lo))/top

def core_exit(lam):
    b = 1-lam**4
    w = [(1-lam)*lam**(j-1)/b for j in range(1,5)]
    # j<=3 branch onto (0,1]; j=4 branch onto (0,lam].
    return sum(w[j-1]*lam**4/branch_image_top(lam,j) for j in range(1,5))

def hit(lam, j, k, memo):
    if k==0:
        return Q(int(j==4))
    if j<=4:
        return Q(0)
    key=(j,k)
    if key not in memo:
        memo[key]=sum((trans(lam,j,i)*hit(lam,i,k-1,memo)
                      for i in range(4,4+k)),Q(0))
    return memo[key]

def prob_direct(lam,n):
    if n==1:
        return 1-core_exit(lam)
    b=1-lam**4
    weights=[(1-lam)*lam**(j-1)/b for j in range(1,5)]
    memo={}
    return sum((sum((weights[j-1]*trans(lam,j,i) for j in range(1,5)),Q(0))
                *hit(lam,i,n-1,memo) for i in range(5,4+n)),Q(0))

def prob_closed(lam,n):
    a=core_exit(lam)
    beta=a/lam
    if n==1:
        return 1-a
    return beta * Q(comb(2*n-2,n-1), n)*lam**(n-1)*(1-lam)**n

for lam in (Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(3,4)):
    check(branch_image_top(lam,1)==1)
    check(branch_image_top(lam,2)==1)
    check(branch_image_top(lam,3)==1)
    check(branch_image_top(lam,4)==lam)
    for j in range(5,13):
        check(branch_image_top(lam,j)==lam**(j-2))
    for j in range(1,12):
        lower=1 if j<=3 else 2 if j==4 else j-1
        for i in range(1,lower):
            check(trans(lam,j,i)==0)
        for i in range(lower,lower+9):
            check(trans(lam,j,i)==(1-lam)*lam**(i-lower))
    A=core_exit(lam)
    check(A==(lam**4+lam**6-2*lam**7)/(1-lam**4))
    for n in range(1,12):
        got=prob_direct(lam,n)
        expected=prob_closed(lam,n)
        check(got==expected)
    beta=A/lam
    r_at_1=Q(1) if lam<=Q(1,2) else (1-lam)/lam
    check(1-((1-beta)+beta*r_at_1)==(Q(0) if lam<=Q(1,2) else A*(2*lam-1)/lam**2))
    if lam<Q(1,2):
        check(1+A/(1-2*lam)>1)

lam=Q(1,2)
A=core_exit(lam)
beta=A/lam
check(A==Q(1,15))
check(beta==Q(2,15))
# Tail at critical n>=1: exact central-binomial survival formula.
for n in range(1,41):
    mass=sum((prob_closed(lam,k) for k in range(1,n+1)),Q(0))
    tail=1-mass
    check(tail==beta*Q(comb(2*n,n),4**n))
    check(tail>0)

# Uniform-local-window numerical stress test. It checks the asymptotic profile,
# not an infinite proof. The proof uses a Riemann-sum limit and Stirling's law.
def survival(lam,n):
    # Numerically accumulate the subcritical or supercritical first-return mass.
    # Critical-window scaling: recurrence for Catalan first-passage coefficients.
    lam=float(lam)
    A=(lam**4+lam**6-2*lam**7)/(1-lam**4)
    beta=A/lam
    r=1-lam
    partial=0.0
    for k in range(1,n+1):
        partial+=r
        r *= (2*(2*k-1)/(k+1))*lam*(1-lam)
    return beta*(1-partial) if n>=1 else 1

for n in (400,1600,6400):
    for u in (-1.0,-0.5,0.0,0.5,1.0):
        l=0.5+u/(2*sqrt(n))
        predicted=Q(2,15)*(exp(-u*u)/sqrt(pi)+u*(1+erf(u)))
        observed=sqrt(n)*survival(l,n)
        check(abs(observed-float(predicted)) < 0.035)  # convergence is O(n^-1/2).

print('PASS:',assertions,'exact/rational and numerical assertions')
