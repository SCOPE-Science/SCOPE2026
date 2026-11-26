# Independent mathematical audit

## correctness

PASS

The price bound gives ηΣw_i≤1, so every diagonal of P is nonnegative; off-diagonals are nonnegative and row sums are one. The leaf recurrence for L^k e₀ produces negative monic degree-k evaluations at w_i with zero constant term and common lower coefficients. Eliminating earlier powers yields the weighted Vandermonde; replacing L by I−ηL multiplies the Krylov determinant by (−η)^d, then squaring gives the Gramian determinant. Fewer columns cannot give full rank. Compactness and the existence of a distinct positive allocation exclude all collisions and zero weights at a maximum. Swapping a dearer larger conductance reduces cost, and rescaling up strictly increases the positive homogeneous determinant. On the reverse-priced ordered chamber, the log of the unsquared objective is strictly concave, since the log w_i part has negative-definite Hessian and the log gaps are concave. Thus stationarity suffices and gives uniqueness up to tied-price permutations, including the one-spoke case. Pairing the weighted first-order terms gives λB=d. For equal prices the Laguerre ODE gives the same stationarity equations after scaling by B/[c m(m+1)], and the monic root product and discriminant give the stated maximum. In the two-leaf case the stationarity numerator in t=w₂/w₁ is −c₂t²+2(c₁+c₂)t−c₁, yielding the stated root t>1. Fresh checks passed exact-rational Gramian identities through m=6 including a zero-weight case, Laguerre identities through degree 6, and an exact unequal-price KKT example at m=3; the equal-price two-leaf value is 1/108. The frozen checker was inspected but not run.

## originality

PASS

The exact hub Laplacian Krylov factor is explicitly covered by a prior indexed observability result, and the stated discrete Gramian factor follows immediately by symmetry, triangular change of powers and squaring. The equal-price root equilibrium and discriminant are classical. The whole all-price theorem is not covered by those inputs: its distinct contribution is globally solving the conductance design for arbitrary linear prices, eliminating other order chambers and characterizing the unique reverse-priced solution. Sensor-location optimization at fixed weights, the classical equal-price root identity, and Vandermonde conditioning do not give that conclusion.

## value

PASS

The arbitrary price vector is a natural constraint for conductance design. A determinant factor alone leaves many disjoint positive chambers; the inverse price assignment and strict uniqueness reduce the global problem to a single exact system without combinatorial search. That operational mathematical reduction is the valuable part, independently of the known Krylov and Laguerre factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
