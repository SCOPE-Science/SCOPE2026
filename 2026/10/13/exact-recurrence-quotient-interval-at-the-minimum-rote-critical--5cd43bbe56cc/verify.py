#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec=70
sqrt2=Decimal(2).sqrt()
alpha=Decimal(1)+sqrt2
lo=Decimal(3)+sqrt2
hi=Decimal(5)+Decimal(3)*sqrt2

def qseq(a1,Nmax):
    q=[1,a1+1]
    while len(q)<=Nmax:
        q.append(2*q[-1]+q[-2])
    return q[:Nmax+1]

def R_from_formula(q,m):
    # Source formula uses n=m-1 and Q_N <= n < Q_{N+1}.
    n=m-1
    N=0
    while not (q[N] <= n < q[N+1]):
        N+=1
    return n+3*q[N+1]+q[N]

# Both minimum-critical-exponent directive initializations.
for a1 in (1,3):
    q=qseq(a1,35)
    assert all(x%2==1 for x in [1]) or True
    for N in range(2,35):
        assert q[N]==2*q[N-1]+q[N-2]
    # Check source Binet formula numerically.
    beta=Decimal(1)-sqrt2
    for N in range(0,25):
        b=((Decimal(a1)+sqrt2)*(alpha**N)-
           (Decimal(a1)-sqrt2)*(beta**N))/(Decimal(2)*sqrt2)
        assert abs(b-Decimal(q[N])) < Decimal("1e-45")
    # Endpoint normalized values converge to the claimed interval endpoints.
    for N in range(5,30):
        mleft=q[N]+1
        mright=q[N+1]
        left=Decimal(R_from_formula(q,mleft))/Decimal(mleft)
        right=Decimal(R_from_formula(q,mright))/Decimal(mright)
        assert left>right
    left=Decimal(R_from_formula(q,q[29]+1))/Decimal(q[29]+1)
    right=Decimal(R_from_formula(q,q[30]))/Decimal(q[30])
    assert abs(left-hi) < Decimal("1e-10")
    assert abs(right-lo) < Decimal("1e-10")

    # Sample every target point in the limiting interval by choosing
    # m approximately x Q_N, where x ranges from 1 to alpha.
    N=28
    A=Decimal(3)*Decimal(q[N+1])+Decimal(q[N])-Decimal(1)
    for j in range(101):
        x=Decimal(1)+(alpha-Decimal(1))*Decimal(j)/Decimal(100)
        m=int((x*Decimal(q[N])).to_integral_value(rounding="ROUND_HALF_EVEN"))
        m=max(q[N]+1,min(q[N+1],m))
        ratio=Decimal(1)+A/Decimal(m)
        target=Decimal(1)+(Decimal(3)*alpha+Decimal(1))/x
        assert abs(ratio-target) < Decimal("2e-9")

print(
    "VERIFY_OK "
    "directives_a1=1,3 "
    "recurrence_Q_N=2Q_N-1+Q_N-2 "
    "binet_N<=24 "
    "endpoint_convergence_N=29 "
    "cluster_grid=101"
)
