#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt

def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def propagator(mu, lam):
    a=1-mu
    M12=[[a,lam,0],[lam,a,0],[0,0,a]]
    M23=[[a,0,0],[0,a,lam],[0,lam,a]]
    return matmul(M23,M12)

def power_rho(M, iters=2000):
    x=[1.0,1.0,1.0]
    for _ in range(iters):
        y=[sum(float(M[i][j])*x[j] for j in range(3)) for i in range(3)]
        s=max(abs(v) for v in y)
        x=[v/s for v in y]
    y=[sum(float(M[i][j])*x[j] for j in range(3)) for i in range(3)]
    return max(y[i]/x[i] for i in range(3) if abs(x[i])>1e-14)

# Exact determinant identity at eigenvalue 1:
# det(P-I) = [(a-1)^2(a+1)-a lambda^2] *
#            [(a-1)(a+1)^2-a lambda^2].
for mu in [Fraction(i,20) for i in range(1,20)]:
    a=1-mu
    for lam in [Fraction(j,20) for j in range(0,21)]:
        P=propagator(mu,lam)
        Q=[[P[i][j]-(1 if i==j else 0) for j in range(3)] for i in range(3)]
        lhs=det3(Q)
        rhs=((a-1)**2*(a+1)-a*lam*lam)*((a-1)*(a+1)**2-a*lam*lam)
        assert lhs==rhs, (mu,lam,lhs,rhs)

# The physical critical square is exact. Compare with aggregate threshold square.
for mu in [Fraction(i,100) for i in range(1,100)]:
    a=1-mu
    l2=mu*mu*(2-mu)/(1-mu)
    agg2=2*mu*mu
    assert l2 > agg2
    # At the formal threshold the first determinant factor is zero.
    assert (a-1)**2*(a+1)-a*l2 == 0
    # The other factor is strictly negative.
    assert (a-1)*(a+1)**2-a*l2 < 0

# Numerical Perron replay at representative physically admissible recovery values.
for mu in [0.1,0.25,0.5]:
    lc=mu*sqrt((2-mu)/(1-mu))
    ra=power_rho(propagator(mu,lc*(1-1e-7)))
    rb=power_rho(propagator(mu,lc*(1+1e-7)))
    assert ra < 1 < rb, (mu,lc,ra,rb)
    lagg=mu*sqrt(2)
    assert lc > lagg

# At mu=1/4, values used in the report.
mu=Fraction(1,4)
l2=mu*mu*(2-mu)/(1-mu)
assert l2==Fraction(7,48)
assert 2*mu*mu==Fraction(1,8)

# Minimality of node count within the two-distinct-single-edge-snapshot class.
# A simple graph on 2 vertices has exactly one possible edge; on 3 vertices
# any two distinct edges meet at one vertex and are isomorphic to 12,23.
edges2=[(0,1)]
edges3=[(0,1),(0,2),(1,2)]
assert len(edges2)==1
assert len(edges3)==3
for e,f in [(edges3[i],edges3[j]) for i in range(3) for j in range(i+1,3)]:
    assert len(set(e)&set(f))==1

print("VERIFY_OK")
print("determinant_grid_checks",19*21)
print("threshold_ratio_grid_checks",99)
print("mu_quarter_temporal_lambda_squared", l2)
print("mu_quarter_aggregate_lambda_squared", Fraction(1,8))
print("minimal_nodes",3)
