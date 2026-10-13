# Self-review

## Correctness — PASS
The claim is proved for every integer \(n\ge2\), \(1\le d\le n\), and every allowed pair of unit directions. Exact Haar projector moment (6) follows from a rank-\(d\) idempotent identity and uniformity on the orthogonal complement. The Fourier telescoping inequality holds for every integer frequency and every circle separation; Haar stationarity transfers its integrated inequality to a fixed pair. Dominated convergence, with a pointwise Lipschitz majorant, proves optimality. The exact ball slice calculation proves the claimed optimization interpretation. The expected rate transfer uses the stated comparison-ball assumptions and the original source Proposition 3 and Theorem 1 without changing their geometric factor. `verify.py` passes exact-rational and seeded finite diagnostics; these are not substituted for the analytic proof.

## Originality — PASS, with residual risk
The motivating primary preprint [1], including its appendices on norm-difference moments, determinant bounds, the ball-oracle factorization and the expected-rate proof, was compared statement by statement. Its Proposition 1 gives a nonsharp factor four above the optimal contraction; Proposition 7 gives the smaller \((d-1)/(96(n-1))\) coefficient. The 2024 normalized spherical-projection theorem [2] concerns expected projected geodesic angle rather than the unnormalized weighted section-oracle efficiency. Indexed mathematical-result comparisons returned Haar moment bounds in sparse subspace descent, not this exact Frank–Wolfe efficiency coefficient. Classical Fourier/Parseval and projector identities are acknowledged as known ingredients. An unindexed equivalent source or previously unnoticed stronger formulation remains possible; search absence is not uniqueness proof.

## Value — PASS
The exact coefficient resolves the uniform expected ball-oracle factor left as an interval in a 2026 method, identifies the first positive subspace dimension \(d=2\), gives matching optimization examples, and strengthens the source's squared norm-difference estimate by a factor of four. It is a genuinely stronger, computable approximation guarantee used directly in the source's expected open-loop analysis. It does not purport to settle algorithmic lower bounds outside the ball, nor to improve independent short-step or tail estimates.

## Scientific limits
The sharpness is a limiting worst case; it is not asserted that a separated angle realizes the infimum. The rate transfer uses all regularity assumptions of [1]. Only indexed/public and inspected sources were compared, so originality has residual publication-coverage risk. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
