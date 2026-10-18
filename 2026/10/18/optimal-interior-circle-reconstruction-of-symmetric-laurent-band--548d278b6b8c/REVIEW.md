# Scientific assessment: optimal annular Laurent-band circle reconstruction

## Correctness — PASS

Angular orthogonality gives an exact diagonal singular-value decomposition, not a sampling heuristic. Strict positivity of the variance of \(\log t\) gives strict convexity of \(\log m(s)\). Thus the least singular value lies at \(j=\pm N\), and its unique maximum occurs at their crossing radius. On either side of that radius every nontrivial squared-condition-number competitor has the same strict derivative sign, proving the *same* radius is uniquely optimal for condition number. Exact annular moments and a uniform exponential tail for the remaining indices establish the sharp leading constant. The included numerical checker exercises these formulas but is not used as an infinite proof. The theorem assumes \(0<a<b\) fixed, \(N\ge1\), angular probability measure, and area-probability Bergman norm.

## Originality — PASS, with residual bibliographic risk

The motivating annular Bergman paper by Douglas–Kim (arXiv:0902.1794v1) concerns reducing subspaces of multiplication operators, not optimally conditioned interior traces. Błocki's annulus-kernel notes use the orthogonal Laurent basis for reproducing kernels, rather than extremal recovery radii. Trefethen's analytic-continuation analysis uses bounded-analytic-function norms and three-circle bounds; it does not imply the finite Hilbert-space singular-value minimax or the precise leading coefficient. The closest indexed harmonic Bergman circle-trace result optimizes the upper trace norm for a nonnegative disk frequency band at a fixed radius, not the two-sided annular inverse norm and condition number. The nearby classical Laurent-projection minimax problem is in a different supremum-norm projection setting. A broader general Hilbert radial sampling theorem or an unlocated treatment of this exact model could still subsume the result. A negative search is not uniqueness proof.

## Value — PASS

A single-circle observation determines every Laurent coefficient in a finite band, but its recovery cost varies exponentially with the observation radius. The theorem gives an actionable, unique balancing radius that simultaneously optimizes two distinct inverse-problem criteria, a complete finite-cutoff condition formula, and an exact exponential ill-conditioning law including the \(N^{-1/2}\) correction and its prefactor. The eventual dominant pole mode identifies the mechanism determining the upper spectral edge. These are natural quantities for annular analytic continuation and inverse sampling rather than an arbitrarily chosen coefficient slice.

## Scope and limitations

Only complete angular data on a single circle, symmetric Laurent exponents, and a fixed annulus are covered. The asymptotics are not uniform in a collapsing annulus. Independent checking beyond the analytic derivation and the reported finite tests remains desirable. An unidentified stronger radial sampling result is the principal novelty risk.

Self-review: passed. Independent audit: not yet performed.
