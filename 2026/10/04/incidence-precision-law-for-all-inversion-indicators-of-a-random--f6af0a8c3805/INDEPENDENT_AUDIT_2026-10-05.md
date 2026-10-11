# Independent mathematical audit

## correctness

PASS

Each comparison has variance one quarter. Disjoint pair comparisons are independent, while the two shared-index orientations have joint probabilities one third and one sixth, giving covariances \(\pm1/12\); these are exactly the off-diagonal entries of \(B^\top B/12\). For the oriented incidence matrix, \(BB^\top=nI-J\), so \(Q=B^\top B\) satisfies \(Q^2=nQ\). Direct multiplication gives the proposed inverse, and the rank of \(B\) gives eigenvalue \(n\) of \(Q\) with multiplicity \(n-1\) and zero on the cycle space, yielding spectrum and determinant. Equal precision diagonals and the standard residual-correlation identity give \(\pm1/(n-1)\). An independent exact enumeration of small permutations in this audit matched the covariance identity. The packaged VERIFICATION.md was also inspected; its finite replay is supplementary to the analytic proof.

## originality

PASS

The closest permutation-statistics source uses the same iid-continuous comparison representation to study the scalar inversion count, while random-permutation-graph papers aggregate the same edge indicators into degree and graph statistics. The inspected statements do not form or invert the complete edge-indicator covariance. Resultary and targeted searches found no prior theorem combining the incidence covariance, no-fill-in precision, cut/cycle spectrum and all-pairs residual correlations. Residual risk remains in older ranking, social-choice, tournament or Hodge-decomposition literature under different notation.

## value

PASS

Pairwise comparisons are the atomic variables behind inversion counts, Kendall-type statistics and permutation graphs. The theorem gives their complete finite second-order geometry and an unusual exact self-sparsity property: conditioning linearly on every other comparison creates no inverse-covariance fill-in. The cut/cycle spectrum and explicit residual correlations make this a natural reusable benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
