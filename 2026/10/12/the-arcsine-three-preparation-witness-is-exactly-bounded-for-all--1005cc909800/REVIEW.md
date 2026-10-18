# Independent mathematical audit

## correctness

PASS

Every qubit binary POVM observable is O=aI+t n.sigma with |a|+t<=1; the correlations are a+t n.r. For each preparation, the two measured Bloch-vector projections can be preserved by a pure Bloch representative, including the third with only one relevant projection. The angular function h(theta)=asin(a+t cos(theta)) satisfies -1<=hprime<=0 because t^2(1-c^2)<=1-(a+tc)^2 follows from |a|+t<=1, including endpoints by continuity. Maximal spherical distance between two polar angles is min(theta1+theta2,2pi-theta1-theta2); 1-Lipschitz monotonicity pushes the three-point estimate to theta1+theta2=pi. The scalar bound asin(a+tc)+asin(a-tc) <= pi/2+asin(a-t) follows for a>=0 by monotonicity in c and c=1, and for a<=0 by bounding the left side by 2asin(a)<=0. Applied with the second observable geodesic-Lipschitz and reversed observables, this yields |Q|<=3pi/2. Explicit projective measurements give correlations (1/sqrt2,1/sqrt2,1/sqrt2,-1/sqrt2,-1), reaching equality. Independent fresh random 20,000 scalar triples passed and sharpness checked numerically; this sampling is not the universal proof.

## originality

PASS

Gallego et al original Eq.(8) explicitly describes exactly this J3<=3pi/2 as backed only by strong numerical evidence; the current all-POVM Bloch-sphere proof resolves that analytic assertion. Subsequent dimension-witness papers employ different state-discrimination or determinant tests; none of the accessible statements implies the precise five-term arcsine inequality. Full texts of two later comparators could not be fetched, leaving a stated indexing/access risk.

## value

PASS

This proves a sharp, explicitly conjectural bound needed to use a seminal nonlinear dimension witness, including biased qubit measurements and mixed states. The analytic one-Lipschitz spherical mechanism is substantive and not an isolated numerical adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
