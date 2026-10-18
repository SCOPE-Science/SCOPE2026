# Scientific review

## Correctness — PASS
The half-circle Fourier kernel has even-lag zeros and odd-lag squared magnitude \(1/(\pi^2d^2)\). Taking traces gives \(D(\Omega)=N/4-(2/\pi^2)E(\Omega)\), with the correct normalization. The inductive graph inequality holds at every finite odd-distance cutoff because every \(N\)-vertex induced graph contains a vertex of degree at most \(\min\{r+1,\lfloor N/2\rfloor\}\), precisely the incremental edge count of the interval. Positive summation of these inequalities yields the global optimum. The first cutoff proves the component penalty, and the two-point example proves optimality of its uniform coefficient. No numerical sample is used as an infinite proof.

## Originality — PASS (bounded, historical priority unverified)
The comparison is between implications, not titles. Mayeli's Proposition 4.1 implies the trace identity, and the box model gives order-sharp logarithmic bounds, but neither implies the global comparison across *all* cardinality-constrained spatial supports or its equality and component penalty. The cited Cayley-graph results concern asymptotic/other generating sets, not these simultaneous exact odd-distance induced-edge inequalities. Targeted semantic mathematical-record and bibliographic searches identified no stronger covering statement. An unindexed discrete rearrangement theorem could subsume the key lemma; that is the primary residual risk. No independent originality certification has been made.

## Value — PASS
The mathematical gap is a shape optimization for a spectral concentration invariant, not another evaluation of a known interval. The theorem determines the best possible trace defect for arbitrary sample geometry at every cardinality, identifies the unique optimal geometry and quantifies the cost of fragmentation with a sharp universal constant. The parity-sensitive simultaneous edge bound is reusable for arbitrary nonincreasing nonnegative odd-distance interaction kernels. These distinctions are motivated by the operator's eigenvalue-plunge interpretation and are not merely a parameter substitution.

## Closest literature and limits
Mayeli (arXiv:2609.12226), Section 4 and Section 9; Barber–Erde (arXiv:1707.04411); Strachan–Swanepoel (arXiv:2503.09591); Briggs–Wells (arXiv:2402.14087). The theorem is restricted to a half-torus band, fixed finite spatial cardinality and the trace defect. It does not claim eigenvalue-wise monotonicity or optimality for arbitrary bands.

Self-review: passed. Independent audit: not yet performed.
