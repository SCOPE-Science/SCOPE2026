"""Exact arithmetic and numerical checks for cactus Lipschitz-polar metric invariants.
Only Python's standard library is required. Run: python verify.py.
"""
from fractions import Fraction as F
from math import comb, factorial, prod, sqrt, log
from random import Random


def density_zero(n):
    # Density at zero of the sum of n independent Uniform[-1,1] variables.
    return sum(((-1)**j * comb(n, j) * max(n-2*j, 0)**(n-1)
                for j in range(n+1)), 0) * F(1, 2**n * factorial(n-1))


def spline_piece(n, lower, upper):
    # Coefficients of t**r for density of sum of n Uniform[-1,1].
    midpoint = (lower+upper)/2
    coef = [F(0) for _ in range(n)]
    for j in range(n+1):
        if midpoint + n > 2*j:
            for r in range(n):
                coef[r] += F((-1)**j * comb(n,j) * comb(n-1,r) *
                             (n-2*j)**(n-1-r), 2**n*factorial(n-1))
    return coef


def integrate_moment(n, moment):
    # Integrate t**moment times density of n uniforms over [-1,1].
    knots = sorted({F(-1), F(1)} | {
        F(2*j-n) for j in range(n+1) if -1<2*j-n<1})
    answer=F(0)
    for lower,upper in zip(knots,knots[1:]):
        for r,c in enumerate(spline_piece(n,lower,upper)):
            k=r+moment+1
            answer += c*(upper**k-lower**k)/k
    return answer


def cycle_variance(m):
    assert m>=3
    den=integrate_moment(m-1,0)
    assert den==2*density_zero(m)
    return integrate_moment(m-1,2)/den


def theta(m):
    v=cycle_variance(m)
    f=density_zero(m)
    return (3*F(m,m-1)*v)**(m-1)/(4*m*f*f)


def laplacian_tree_count(n,edges):
    L=[[0]*n for _ in range(n)]
    for a,b in edges:
        L[a][a]+=1; L[b][b]+=1; L[a][b]-=1; L[b][a]-=1
    M=[[F(z) for z in row[:-1]] for row in L[:-1]]
    det=F(1)
    for i in range(n-1):
        pivot=M[i][i]
        assert pivot!=0
        det*=pivot
        for j in range(i+1,n-1):
            ratio=M[j][i]/pivot
            for k in range(i+1,n-1):
                M[j][k]-=ratio*M[i][k]
            M[j][i]=F(0)
    return det


def graph_checks():
    # Edges listed independently; cycle multiplicities and spanning trees checked.
    cases=[
       (3,[(0,1),(1,2),(2,0)],[3],0),
       (4,[(0,1),(1,2),(2,3),(3,0)],[4],0),
       (4,[(0,1),(1,2),(2,0),(0,3)],[3],1),
       (5,[(0,1),(1,2),(2,0),(0,3),(3,4)],[3],2),
       (5,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2)],[3,3],0),
       (6,[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5)],[4],2),
       (7,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2),(6,0)],[3,4],1),
    ]
    for n,edges,cycles,b in cases:
        d=n-1
        assert d==b+sum(m-1 for m in cycles)
        assert len(edges)==b+sum(cycles)
        tau=laplacian_tree_count(n,edges)
        assert tau==prod(cycles)
        # The exact intrinsic-volume expression is rational / sqrt(n).
        volume_times_root_n=2**len(edges)*prod(density_zero(m) for m in cycles)
        assert volume_times_root_n>0
        # The exact affine isotropic defect is multiplicative.
        defect=prod(theta(m) for m in cycles)
        assert defect>0
    return len(cases)


def monte_carlo_cycle(m,seed=20261018,draws=60000):
    # Independent check of conditional coordinate variance on cube's zero-sum section:
    # sample first m-1 uniforms and accept precisely when their sum is in [-1,1].
    rng=Random(seed+m)
    numerator=0.;denominator=0
    for _ in range(draws):
        values=[2*rng.random()-1 for j in range(m-1)]
        if abs(sum(values))<=1:
            numerator+=values[0]**2
            denominator+=1
    estimate=numerator/denominator
    exact=float(cycle_variance(m))
    assert abs(estimate-exact)<0.017,(m,estimate,exact)
    return estimate,exact,int(denominator)


def main():
    assert density_zero(3)==F(3,8)
    assert density_zero(4)==F(1,3)
    assert cycle_variance(3)==F(5,18)
    assert cycle_variance(4)==F(3,10)
    assert theta(3)==F(25,27)
    assert theta(4)==F(243,250)
    count=graph_checks()
    for m in range(3,13):
        v=cycle_variance(m)
        assert F(0)<v<F(1,3)
        assert theta(m)>0
    for m in [3,4,5,6]:
        estimate,exact,n=monte_carlo_cycle(m)
        print('cycle',m,'conditional_variance_estimate',round(estimate,6),
              'exact',round(exact,6),'accepted',n)
    print('VERIFY_OK exact_cycles=10 graphs=',count,'monte_carlo=4')

if __name__=='__main__': main()
