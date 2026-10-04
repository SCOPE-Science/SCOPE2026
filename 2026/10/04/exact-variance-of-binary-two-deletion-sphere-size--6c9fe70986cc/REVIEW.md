# Review

## Correctness
PASS. The proof is all-parameter. The published two-deletion run formula is reconstructed from deletion assignments and singleton-run collisions. For a uniform binary word, the boundary vector is independent Bernoulli\((1/2)\); after substitution, the sphere size is a quadratic polynomial. Its complete Walsh spectrum has \(m\) equal linear coefficients \((m-1)/4\) and \(\binom m2\) quadratic coefficients of magnitude \(1/4\), so orthogonality yields \(\operatorname{Var}(B_n)=(n-1)(n-2)(2n-3)/32\). The bundled exhaustive checker verifies every binary center through \(n=12\) but is not used as the infinite proof.

## Originality
PASS. The closest direct source, Swart and Ferreira, gives the per-word cardinality formula for exactly two deletions but no variance. Pham--Goyal--Kiah study deletion-ball maxima and intersections, and Alon et al. study the nonregular deletion graph and triangle sparsity. Targeted searches under variance, second moment, deletion sphere, deletion ball, and distinct-subsequence aliases found no exact random-center variance. Residual risk remains for unindexed or differently phrased derivations.

## Value
PASS. The number of distinct deletion outputs is a fundamental local statistic of deletion channels. At radius two, its exact variance quantifies how strongly local ambiguity varies across binary centers and gives the precise fluctuation scale \(n^{3/2}/4\). This is a natural global invariant of the nonregular deletion geometry, not a routine isolated parameter computation.

The main limitation is scope: uniform binary inputs and exactly two deletions only. No higher-radius, nonbinary, or full-distribution theorem is claimed.

Same-model review: passed. Independent audit: not yet performed.
