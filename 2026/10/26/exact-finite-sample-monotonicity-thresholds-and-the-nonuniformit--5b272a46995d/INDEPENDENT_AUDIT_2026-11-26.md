# Independent mathematical audit

## correctness

PASS

Verified every finite cutoff by exact symbolic inversion in slope coordinates, independently of the supplied checker. For B the first-difference matrix, E the first-difference matrix on slopes, and D=EB, the induced jump map is (I+lambda B B^T E^T E)^(-1). Complete factorizations through n=6 agree; in particular the six-point entries (0,2) and (0,4) together exclude every 0<lambda<(14+sqrt(181))/15, not just parameters at which the corner is negative. For n=4 only the pair of reflected corners can be negative. Nonnegative jumps of total mass at most one prove the sharp defect; exact differentiation gives numerator 1-12lambda-92lambda^2 and peak (3-2sqrt(2))/8. The small-strength expansion on the first jump and the positive affine fit slopes at the large-strength limit apply at each fixed n>=4. The infinite kernel has zero second moment and mass one, forcing a negative coefficient, and the finite residual is exponentially small at the four boundary indices. The repair fixes the indexing: at row i the forward difference of the smoothed centered step is k_(i+1), or the difference from i-1 to i is k_i. The theorem is unchanged mathematically. Read frozen VERIFICATION.md and verify.py without executing that script.

## originality

PASS

The exact output-order thresholds through n=6 and the sharp four-point defect survive; none is stated in the strongest inspected comparisons. The original broad barrier is an immediate consequence of prior asymptotic filter-weight results once tested on a centered binary step. The repaired RESULT and scientific notes retain its direct proof only as context and credit that coverage. Distinctness is not based on inaccessible papers or a search miss.

## value

PASS

Output order is a natural shape guarantee for unconstrained smoothing distinct from a data-range or TV bound. The sizes are the first nontrivial lengths admitting and then restoring monotonicity, not an arbitrary census slice. Exact sharp restoration cutoffs and the worst negative slope supply concrete guarantees and a defect benchmark for that operator; the application does not depend on claiming the prior-covered asymptotic obstruction as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
