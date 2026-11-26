# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md, proof steps 1–4. Translation/centering preserves the zero moments. In cosine coordinates E[u]=0 and E[u²]=1/2, hence the nonnegative quadratic certificate excludes all shorter arcs and forces precisely the three equal masses at equality (unit total mass). For existence, the two internal grid radii bracket arccos(−1/(2 cos R)); for odd D the stated tangent factorization follows by expanding (1+√3 y)(1−3y²)−(1+y²)² and using 0≤y≤2−√3. For the small nondivisible orders 5,7,8,10,11 an allowed internal q in [N/3,N/2] can be chosen as 2,3,4,5,4 respectively, giving an upper bracket ≤π/2; N=4 has four equal masses and 3-divisible orders use the center. For N≥12 the step 2π/N gives the same nonnegative-cosine upper bracket. The Lagrange formulas evaluate the degree-two moment functional with nonnegative masses (strictly positive at the endpoints); equal radii use the separately valid two-cosine rule. Reflection kills the sine moments, and affine pruning in R⁴ gives at most five bins. Dropping an endpoint would contradict the lower bound. More precisely the Parseval identity is the frame operator (equivalently the three-row Gram matrix), not the Gram matrix indexed by bins. The bundled mpmath pre-pruning test was inspected, not executed or relied upon.

## originality

PASS

The complete fixed-grid attainment result is distinct on the evidence inspected. The rounded lower bound already follows from Tan–Zhang's continuous positive-measure lemma, with the same dual quadratic in degree two; their equality case gives the divisible-order rule and uniqueness as well. Do not credit those as new. Generic support compression is standard. The distinct contribution is attainment of the rounded lower bound for nondivisible grids with a constructive small support inside the optimal interval. The older three-site cardinality result compares the same moment constraints but not this localization constraint.

## value

PASS

Exact positive Parseval sampling in a minimal consecutive frequency window is meaningful separately from minimizing the number of measurements. Constructively closing the integer-grid gap for every N is a nontrivial localization result, with at most five adjustable bins and exact endpoint occupancy; no claim of minimum support within the window or higher-order scope is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
