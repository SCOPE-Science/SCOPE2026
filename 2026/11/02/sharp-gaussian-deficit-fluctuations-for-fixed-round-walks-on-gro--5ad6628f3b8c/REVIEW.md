# Self-review

## Correctness

**PASS.** The exact stage-count recursion is established using the independent uniform stage draws; its mean and covariance propagate by a telescoping multiplicative factor. The conditional variance expansion has the leading coefficient \(q y(1-y)\) for an unseen fraction \(y\), and \(y\to1/(q+1)\) in \(L^2\). The bounded-increment triangular martingale has its predictable quadratic variation converging to \(q^2/((q+1)^2(2q+1))\) and satisfies Lindeberg. The exact two-round variance was confirmed through independent exact recurrences and enumerations (961 checks). No inference from finite tests to the infinite theorem is made.

## Originality

**PASS, qualified.** The 2020 preprint and full published treatment of Kijima--Shimizu--Shiraga give mean bounds for this growing-complete-graph model and explicitly identify concentration as further work; their text contains no sharp constant-duration variance or Gaussian theorem. The earlier subexcedant-function Eulerian law and weak-excedance-set representation fully cover the \(q=1\) case and are excluded from the novelty claim. Fixed-type coupon-collection CLTs are not directly the growing-type model. Current literature and accessible research-record searches found no implication-equivalent result for fixed \(q\ge2\), but broad occupancy martingale literature remains a priority risk.

## Value

**PASS.** The sharp positive variance constant and Gaussian limit answer a motivated distributional fluctuation question left beyond the expectation-only theory, at every fixed number of moves per newly arrived vertex. Exact temporal covariance detects the persistence exponent \(q+1/2\), and an exact finite-size two-round variance provides a checkable boundary case. The result is a complete, natural fixed-duration fluctuation theorem rather than a tiny numerical improvement.

## Literature and limitations

The closest primary source is Kijima--Shimizu--Shiraga, arXiv:2008.10837, with freely readable full manuscript and later full journal article. Beyene et al. (2023) and Visontai (2013) already imply the one-round permutation identities. The argument assumes a complete graph with uniform self-loop transitions and fixed integer duration; it does not establish an error rate in the Gaussian approximation or analogous results for arbitrary growing graphs. Historical priority and independent audit remain unresolved.

Self-review: passed. Independent audit: not yet performed.
