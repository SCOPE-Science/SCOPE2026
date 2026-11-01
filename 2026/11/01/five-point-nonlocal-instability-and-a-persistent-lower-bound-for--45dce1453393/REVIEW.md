# Self-review

## Correctness: PASS
The proof fixes the Euclidean fitting metric and the coordinate maximum norm separately. All active sets are feasible since the second-difference matrix has full row rank; strict KKT multipliers provide actual open cells. Hence the global two-input Lipschitz constant equals the maximum induced norm of finitely many orthogonal face projectors. Exact five-site row-sum enumeration gives the unique separated-curvature maximum \(11/7\), with an explicit pair of inputs and positive dual multipliers. The embedding and the alternating tridiagonal-Green limit establish monotonicity and the asymptotic lower bound for all sizes. The embedded checker completed 420 rational assertions. The full large-size constant is not claimed.

## Originality: PASS, with risks
Meyer (2008) supplies a facewise cone-projection methodology but not the exact five-site maximum-norm stability classification or alternating-curvature bound. Chen–Wellner (2014) concerns convex least-squares distributional rates rather than a deterministic two-input Lipschitz ratio. Yang–Barber (2017) concerns first-difference isotonic projection, whose norm behavior does not transfer by an isometric coordinate change. Actual primary-literature and published research-record searches found no numerical or implication-equivalent result; missing older or unindexed specialty calculations remain a residual priority risk. The full text material inspected and named comparisons are recorded in AUDIT.json.

## Mathematical value: PASS
This is a motivated minimum-size structural transition: the first opportunity for two separated zero-curvature constraints occurs with five observations and raises worst-case stability above every adjacent or globally affine active face. Its unique mid-site hotspot yields a concrete robustness obstruction; an explicit infinite family shows this is not a disappearing small-sample artifact. The exact cutoff and quantitative lower bound are useful for shape-constrained least-squares perturbation analysis, while an exact all-size classification remains open.

## Limitations
Equal spacings, unit least-squares weights, real signals, and second-difference convexity are essential to the statements. The asymptotic lower bound is not asserted sharp. Independent review is absent.

Self-review: passed. Independent audit: not yet performed.
