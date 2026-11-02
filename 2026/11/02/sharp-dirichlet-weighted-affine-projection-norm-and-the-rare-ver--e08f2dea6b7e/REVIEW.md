# Scientific review: sharp Dirichlet-weighted affine projection norm

## Correctness — PASS
The stated domain is the full barycentric simplex with strictly positive real Dirichlet parameters. The moment-matrix inverse is explicitly reconstructed, and the real affine kernel is verified to reproduce constants. Absolute-value convexity and a positive-measure sign change show that only vertices can maximize; gamma-process conditional Jensen proves strict ordering by the smallest Dirichlet parameter. Incomplete beta integration gives the exact constant. Fixed-total extrema and both asymptotic regimes follow from bounded-negative-part, beta-moment and gamma-moment arguments. The bundled standard-library checker passed 360 integer parameter profiles and the additional exact rational tests documented in `VERIFICATION.md`. The real-parameter and infinite-dimensional steps depend on the proof, not finite enumeration.

## Originality — PASS, qualified
The complete published uniform-simplex result is a covered specialization and is expressly excluded from the novelty claim. Aktaş and Xu (arXiv:1111.2994v1) establish weighted Jacobi simplex polynomial structures; Palombi and Toti (arXiv:1407.7404v2) develop Dirichlet-weighted Galerkin expansions and discuss positivity. Direct inspection of the relevant primary sections and targeted database comparisons did not reveal the all-positive-parameter exact operator norm, strict smallest-shape-parameter vertex rule, sharp fixed-total weight design or differing concentration limits. Equivalence in older Jacobi-kernel or finite-element literature remains a priority risk; lack of search hits is not itself a novelty proof.

## Mathematical value — PASS
The sharp stability and positivity-loss constant is a natural invariant of weighted affine least-squares projection. The result completely solves its parameter dependence, including which simplex vertices control the worst case, the unique least-amplifying distribution for fixed total concentration, an unattained but sharp opposite envelope, and a finite-versus-linear high-dimensional stability transition. These features motivate the precise invariant and do not merely restate the known uniform specialization.

## Limitations and comparison
The theorem covers one Dirichlet-weighted simplex, degree-one real orthogonal projection, and the induced maximum norm only. No classification of higher-degree projectors, arbitrary measures, or globally coupled finite-element operators is claimed. The closest known exact result is the unweighted uniform-simplex case; the two inspected primary papers address broader weighted polynomial methodology but different theorems. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
