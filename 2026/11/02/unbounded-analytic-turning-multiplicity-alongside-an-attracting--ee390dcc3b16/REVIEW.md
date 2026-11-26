# Independent mathematical audit

## correctness

PASS

With u=x(1−x), the numerator of W, up to a positive constant, is a positive-leading quadratic with negative discriminant. The modulation factor is at least 1/100, so P_L is strictly increasing analytic with the two infinite endpoint limits; its analytic inverse yields the continuous interval self-map with b as the only interior fixed point. At b the cosine is exactly 1, and P'_L(b)>a, giving 0<F'_L(b)<1. On the stated J, the rational derivative bound gives W decreasing and (199/100)W>a, while W/100<a. In the rescaled interval mJ there are at least L−2 whole integer-to-integer intervals. Each supplies one crest–trough and one trough–crest sign change of P'_L−a; analyticity separates the sign-changing zeros, and the positive denominator of F'_L preserves their signs. The cosine contribution to P_L is O(1/m) on each interior compact set by integration by parts, giving local uniform convergence of the maps by monotone inversion. The divergent lower derivative bound gives uniform endpoint control, so each fixed iterate converges uniformly as well. A fresh exact rational replay (python3 /workspace/checks/turning_certificate.py) checked the sign bounds and enclosed F_0^2([0.9559,0.956]) in [0.99063318,0.99063510] and F_0^6 of the same interval in [0.72464629,0.72724910]. It uses a series with an explicit geometric tail bound for the logarithm in the closed form of P_0, monotone rational bisection and interval subdivision, not point sampling. The strict ordering persists for all sufficiently large L. The period-three criterion for F_L^2 gives least F_L-period 3 or 6 and thus positive entropy. Summing the potential increments over a finite interior cycle gives the exact centroid b. The endpoints are fixed but not subject to that identity; there is no claimed explicit entropy cutoff, exact critical-point count or estimate of basin measure.

## originality

PASS

The nonoscillatory map, including the particular parameters, the attracting interior fixed point and positive entropy, is in Bielawski et al. Periodic centroids are also prior in this class of learning maps. The supported distinct contribution is unbounded strict turning-point multiplicity within an explicit fixed-parameter analytic FTRL family while preserving an attracting interior equilibrium, a non-power-of-two period for all sufficiently large frequencies and the exact centroid constraint.

## value

PASS

The construction shows that the regularizer constraints and the coexistence of an interior attractor with interval chaos impose no uniform finite bound on modality, even at the same game parameters and amplitude. The analytic oscillations are a controlled way to increase turns without losing the strict dynamical obstruction or changing the orbit means. This distinguishes the geometry of the maps from the persistence of their dynamics, without claiming entropy grows with frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
