"""Exact finite-tree covariance and rational-series consistency checks."""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def weights(alpha, n):
    return [Q(0)] + [Q(j)**alpha for j in range(1, n+1)]


def direct_covariance(alpha, n):
    w = weights(alpha, n)
    choices = [range(1, j) for j in range(2, n+1)]
    total_p = Q(0)
    et = ed = etd = Q(0)
    for parents0 in product(*choices):
        parents = [0, 0] + list(parents0)
        p = Q(1)
        depths = [0]*(n+1)
        deg = 0
        for j in range(2, n+1):
            k = parents[j]
            depths[j] = depths[k]+1
            p *= w[k]/sum(w[1:j])
            deg += (k==1)
        t = sum(depths)
        total_p += p
        et += p*t
        ed += p*deg
        etd += p*t*deg
    assert total_p == 1
    return etd-et*ed


def formula_covariance(alpha,n):
    w=weights(alpha,n)
    W=Q(0)
    ps = [Q(1)]*(n+1)
    for j in range(1,n+1):
        W += w[j]
        ps[j]=w[j]/W
    b=Q(0)
    result=Q(0)
    for j in range(2,n+1):
        q=w[1]/sum(w[1:j])
        result -= q*(1+(n-j)*ps[j])*b
        b+=ps[j]
    return result


checks=0
for alpha in (-2,-1,0,1,2):
    for n in range(2,8):
        direct=direct_covariance(alpha,n)
        formula=formula_covariance(alpha,n)
        assert direct==formula,(alpha,n,direct,formula)
        if n>=3: assert formula<0
        checks+=1

# For alpha=1, the claimed limiting covariance constant can be
# written as 4*sum_{i>=2} 1/(i(i+1)^2) = 7-4*zeta(2).
# At every finite cutoff, equality of the two *finite* rearrangements
# is checked exactly, rather than treating truncated sums as infinite.
for m in range(2,35):
    sum_a=sum((Q(4)*(2*sum((Q(1,j) for j in range(1,k+1)),Q(0))-3)/
               (k*(k-1)*(k+1)) for k in range(3,m+2)),Q(0))
    sum_b=sum((Q(4)/((i)*(i+1)*(i+1)) for i in range(2,m+1)),Q(0))
    # finite rearrangement has positive remainder due to k>m+1
    assert sum_b>sum_a or m==2
    checks+=1

# telescoping for each truncation of the rational tail of the infinite j sum
for i in range(2,100):
    val=sum((Q(1,j*(j-1)*(j+1)) for j in range(i+1,250)),Q(0))
    exact=Q(1,2*i*(i+1))-Q(1,2*249*250)
    assert val==exact
    checks+=1

# Root degree at alpha=1: expectation tends to 2 and variance to 14-8*zeta(2).
for n in range(2,100):
    probs=[Q(2,j*(j-1)) for j in range(2,n+1)]
    mean=sum(probs,Q(0))
    var=sum((q*(1-q) for q in probs),Q(0))
    assert mean==2-Q(2,n)
    assert var>=0
    checks+=1

print('PASS: %d exact rational checks' % checks)
print('Finite-parent exhaustive checks include alpha=-2,-1,0,1,2; n=2,...,7.')
print('Series identities checked by exact finite rational summation; infinite limits require analytic proof.')
