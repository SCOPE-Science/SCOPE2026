# Independent mathematical audit

## correctness

PASS

Reconstructed exact P1 edge matrices M_e=ℓ[[2,1],[1,2]]/6 and K_e=[[1,−1],[−1,1]]/ℓ; hence M=ℓ(2D+A)/6 is SPD, K=(D−A)/ℓ positive semidefinite with constant null vector. The complete M-orthogonal generalized eigenbasis has eigenvalues 0,3/ℓ²,12/ℓ², including p=1 or q=1. Its exact projector formula yields positive opposite-part offdiagonals, same-part offdiag π_j 6x(6θx−1)/[(1+3θx)(1+12θx)], and diagonals governed by F_m=m+[m(15θ−3)−3]x+18θ[1−2m(1−θ)]x². This proves x≥1/(6θ) is necessary for positive x and that F_m≥0 suffices when m≥2. At the boundary F_m=3m(3θ−1)/(2θ), derivative 3[m(9θ−5)+1]; the θ<1/3 concavity, exact θ=1/3 factorization, θ∈(1/3,1−1/(2m)) unique positive root and θ≥1−1/(2m) positive coefficients establish every open/closed endpoint and isolated step; t=0 is identity and θ=0 forbids positive t. For θ=1/2, m=2 upper=(1+√3)/3 and large-m upper→2/3. Independently verified the same-part polynomial and diagonal polynomial with SymPy, boundary value/derivative/factorization symbolically, and 495 additional exact rational direct matrix inversions/projector comparisons/row sum and sign tests for p,q≤4, six θ values and several rational steps. The 2,952 source self-check cases are not counted as independent tests. The proof, not finite enumeration, establishes the infinite domain.

## originality

PASS

Best-of-knowledge priority assessment for complete if-and-only-if θ phase diagram on single-element-per-edge consistent-mass equilateral Kirchhoff K_{p,q}, m≥2, NOT for the known general theta-method resolvent identity or previously studied K_{2,2} CN subcase. Fresh Resultary searches plus materially read full primary texts show CHV 2015 proves important general conditional theta-positivity structure under H^{-1}>0 Dirichlet invertibility and Li–Huang sufficient FEM bounds; these do not imply the zero-mode biclique halfline θ≥1−1/(2m), explicit m-controlled finite root and isolated θ=1/3 step. Arioli–Benzi establishes graph FEM but not the sharp time-step sign diagram. Published Markov CN resolvent return theorem has a generator hypothesis violated by −M^{-1}K. No observed covering stronger theorem or exhaustive table, with explicit residual risk of unindexed prior specializations.

## value

PASS

On a natural branched wire network with Kirchhoff junctions and consistent P1 mass, exact entrywise step positivity guarantees the nodal maximum principle for arbitrary nonnegative initial nodal values. The phase diagram is a useful complete sharp design rule across all p,q (including stars with one singleton part) and every θ∈[0,1], not just a textbook sufficient M-matrix criterion: there is an isolated positive step θ=1/3,x=1/2, a bounded safe window for 1/3<θ<1−1/(2m), and an unbounded safe halfline at/above the sharp topology-dependent θc(m). The upper end R_m(θ) is explicit and shows dependence only on larger part size, with meaningful m=2 versus m→∞ contrast. It exhibits non-monotonicity in step size and why generic coefficientwise restrictions miss admissible steps; a researcher using meshed network diffusion could need these exact bounds. Though specialized, this is a motivated full natural-family classification, not an arbitrary finite table or renaming of a general abstract theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
