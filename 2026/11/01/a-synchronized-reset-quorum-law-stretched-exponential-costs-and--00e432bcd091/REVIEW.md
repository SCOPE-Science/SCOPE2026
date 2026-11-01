# Scientific review: synchronized Brownian quorum

## Correctness — PASS

For every \(N\) and \(r\), reflection principle gives \(F(t)\), renewal gives \(q_N\) and the mean exactly. Uniform logarithmic \(F(t)\) expansion, global \(e^{-b/\sqrt t}\) bound and compact Laplace-principle localization establish the fixed-rate \(N^{2/3}\) constant. Maximal first-passage Frechet convergence, its exponential transform, compact-uniform convergence, and explicit uniform small- and large-clock barriers prove convergence of global minima; no unproved optimizer uniqueness is used. The embedded pure-Python verifier reproduces distinct finite-size checks.

The limiting optimizing clock is an **argmin set**; uniqueness is neither needed nor claimed. A full Brownian renewal identity and two distinct asymptotic scalings have been proved with explicit uniform tail control. The finite numerical checks cannot replace the limiting proofs.

## Originality — PASS, qualified

On a genuine different objective (a full quorum completed within one random epoch, with progress lost between common resets), the exact N-dependent renewal functional is distinct from first-arrival and recorded-rank reset theory. Source and claim-level primary literature comparisons found no mathematically stronger directly covering \(N^{2/3}\) fixed-rate cost and global \(N^{-2}\) rate optimization. General restart/extreme-value theory could subsume components and the closest 2026 rank-paper full text was unavailable, so priority remains qualified.

The nearest compared primary sources are Biroli, Majumdar and Schehr, arXiv:2303.18012 (first-hit common resets); Vatash et al., arXiv:2609.23542 (ranked arrivals with progress recorded); Evans and Majumdar, arXiv:1102.2704 (one-walker renewal); and the recent first-passage-triggered resetting gas (doi:10.1209/0295-5075/ae3f4f). No known record directly covers the present full-population quorum with erased progress, fixed-rate N-scaling and global optimal-clock scaling. **Priority risk:** stronger generalized restart-maxima results and inaccessible full manuscript text of arXiv:2609.23542. Search absence does not certify novelty.

## Value — PASS

The strict, progress-erasing all-searchers-within-one-reset-epoch task is a natural synchronized quorum/parallel completion objective. It exhibits a singular design distinction: any fixed common reset rate costs \(\exp(\mathrm{const}\cdot N^{2/3})\), but a globally optimized clock of order \(N^{-2}\) reduces the best achievable mean to order \(N^2\) with an explicit universal variational constant. This is a meaningful exact population-scale optimization and boundary, not merely a numerical benchmark or renaming of one-searcher renewal theory.

## Limits and verification

The theory assumes independent Brownian searchers between common Poisson resets, perfect absorption within an epoch, total erasure of progress at resets, and no overhead. The exact finite-N expression, fixed-rate large-N limit, scaled-rate limit and convergence of globally optimized costs are proved. The standalone script is supplemental numerical reproduction.

Self-review: passed. Independent audit: not yet performed.
