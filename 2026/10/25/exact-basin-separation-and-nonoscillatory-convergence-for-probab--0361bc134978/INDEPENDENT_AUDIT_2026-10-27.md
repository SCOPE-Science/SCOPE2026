# Independent mathematical audit

## correctness

PASS

For each integer m>=1, 0<delta<=1, b_j>=0 and sum_j b_j<=1, F(x)=(1-delta)x+(1-x)sum_j b_j x^j maps [0,1] to itself and has finitely many fixed points (positive ones are roots of (1-x)G(x)=delta, G=P(x)/x). At a positive fixed point r, delta=(1-r)G(r), P(r)=rG(r), 1-delta-P(r)=1-G(r)>=0. Since P is nondecreasing, for x>=r the difference F(x)-r >= (x-r)(1-G(r))>=0; for x<=r the reverse upper bound <=0 holds. Thus fixed points cannot be crossed; within each root-free interval F(x)-x has constant strict sign, so orbits are monotone, bounded and converge to a neighboring fixed point. The rightmost gap drifts left since F(1)-1=-delta. The claimed irrational bistable roots and exact basins follow from F(x)-x=-x(19x²-18x+3)/20 at delta=1/5,b1=1/20,b2=19/20. Explicit F'(1)=-1/5 shows the one-step map need not be increasing; the logistic two-cycle at b1=16/5 is deliberately outside the probability condition. Rechecked exact factorization and rationally sampled barriers independently; neither grid nor existing checker proves all m.

## originality

PASS

The all-order polynomial homogeneous specialisation possesses a shared invariant-equilibrium barrier even without a monotone update. Closely related hypergraph-SIS work supplies physical admissibility and sufficient heterogeneous stability/basin claims, not this unconditional exact homogeneous partition. Pairwise exponential/contact SIS maps have different incidence and often one endemic equilibrium. A classical scalar order-dynamics result may encode the same no-crossing criterion, so priority remains qualified.

## value

PASS

Discrete time higher-order SIS contagion has meaningful competing endemic and disease-free equilibria; the theorem globally partitions basins and prohibits numerical oscillations on the full separate probability-admissible coefficient range. Its nonmonotone bistable example separates that conclusion from usual global monotone-map theorems and from a stronger small-step assumption. This is a structural all-m result, not a routine local-stability calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
