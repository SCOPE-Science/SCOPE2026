# Mathematical review — quadratic rigidity at a rank-two singular Euclidean four-simplex

## Correctness (PASS)
The ten squared triangular areas are explicit quadratic Heron polynomials in the ten squared edge lengths. At the stated positive-definite right-simplex Gram matrix, the computed Jacobian has rank eight by a nonzero minor and two independent right and left null vectors. Exact projection onto the left kernel produces the two homogeneous quadratic forms \(t(2s+t)/8\) and \(s(s+2t)/8\). Their displayed sum-of-squares identity is strictly positive away from the origin; decomposition into kernel and a complementary space upgrades this to a local quadratic lower bound for the full map. A Euclidean kernel path has an exactly quadratic area defect, proving optimality of the exponent. The included reproducible symbolic checker verifies these calculations. The local compactness argument, not computation alone, establishes the infinite statement.

## Originality (PASS, with bibliographic risk)
Mohar–Rivin (arXiv:0901.3284) study codimension-two face volume Jacobians at regular simplices and a different singular nonuniqueness example. Gaifullin (arXiv:1310.3417) gives generic algebraic information about the same type of areas. Zhang (arXiv:2307.15817, 2023) poses continuous Euclidean face-volume rigidity and gives pseudo-Euclidean constructions. These sources do not establish a locally rigid rank-two Jacobian singularity with the explicit sharp quadratic stability estimate. An equivalent unindexed earlier singular-case computation remains possible; the accessible Gaifullin theorem statements, rather than every proof and appendix, were compared.

## Mathematical value (PASS)
A nondegenerate Euclidean simplex with a two-dimensional infinitesimal area-preserving space but an isolated actual area fiber is a substantive second-order rigidity example. The same calculation supplies a sharp inverse stability exponent, giving a quantitative geometric obstruction directly linked to the motivating literature rather than a merely formal nullity computation.

## Scope and limitations
The result is local at a specified labeled right four-simplex, not global or generic. Exact certificates concern the polynomial Jacobian and quadratic obstruction; finite checker output does not constitute an infinite proof. No external independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
