# Scientific assessment

## Correctness: PASS
The two one-sided ideal dimensions are independently obtained as sums of leading and trailing corner ranks. Strict upper triangularity gives a sharp upper bound for each leading rank; deleting rows gives the matching lower bound for trailing ranks. Endpoint equality forces precisely the first \(r\) superdiagonal pivots and the vanishing of all lower rows. A two-stage sequence of nonattacking rook moves gives every intermediate integer while preserving matrix rank. Reflection-transposition gives the negative endpoint. The finite-field counts follow from an explicit product of punctured lines and affine coordinates. The standalone checker exhaustively verified thirteen finite cases, including \(\mathbb F_4\); the proof itself is valid for arbitrary fields.

## Originality: PASS with residual risk
The closest inspected result is Rahimi-Alangi–Yahaghi (2015), whose Corollary 2.5 already supplies the row/column characterizations of principal one-sided ideals of triangular matrix rings and hence the underlying profile formulas; that ingredient is explicitly credited. Their Theorem 2.6 characterizes which one-sided nest submodules are principal, but neither result provides the **sharp fixed-rank difference between the two one-sided ideal dimensions**, the full interval of attainable gaps, or the complete equality loci and their finite-field sizes. Further comparisons inspected Arias-Castro–Diaconis–Stanley (2004) on superclass orbits, Yip (2013) on rank/Jordan-type rook counts, and Ferraz–Polcino Milies–Taufer (2017) on ideals of full semisimple matrix rings. Search comparisons found no statement containing the package theorem. The prior nest-module classification or superclass theory may yield the new extrema by an additional nontrivial argument; this is a genuine residual priority risk.

## Value: PASS
The mismatch between principal left and right module dimensions is a natural structural measure of one-sided asymmetry in a standard hereditary finite-dimensional algebra. This result obtains the exact sharp quadratic scale, a complete fixed-rank attainable spectrum over every field, and a geometric classification and finite-field census of *all* sharp generators. It is not a recalculation of a usual matrix-rank or Jordan-type table; those individual invariants cannot distinguish the two one-sided ideal dimensions.

## Limits
Counts for nonextremal gap fibers and extensions to general pattern subalgebras are not claimed. Full independent priority and proof audits have not occurred.

Self-review: passed. Independent audit: not yet performed.
