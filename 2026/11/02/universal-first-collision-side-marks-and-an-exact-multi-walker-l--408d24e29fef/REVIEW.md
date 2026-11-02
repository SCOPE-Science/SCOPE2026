# Scientific review

## Correctness — PASS
The collision-free process has the exact killed birth-death rates in the proof: nonmeeting cross-part transitions are \(a(n-b)/n\) and \(b(m-a)/m\); marked killing rates are \(ab/m\) and \(ab/n\). Each marked collision pair has a constant destination-side hazard ratio, justifying an independent Bernoulli mark even conditional on the pair and first-collision time. The rational checker verifies the reduction and marked Laplace identity in 6,133 finite checks, while finite-matrix perturbation proves the fixed-\(k\) exponential limit from the Ehrenfest spectral gap. Quantifiers require distinct initial positions, independent rate-one jumps, and fixed \(k\) in the asymptotic statement. A finite checker does not certify the infinite claim.

## Originality — PASS (historical-priority qualification)
Figueiredo–Iacobelli–Shneer (2019) gives two-agent complete-bipartite meeting times (Section 5.3), which cover the obvious two-agent temporal special case; that result is not claimed new. Sanders (2009) gives equilibrium mean encounter *recurrences* of many walkers, not their first-collision-time transform or its independent location-side mark. Nguyen (2022) develops scaling limits of collision measures on \(\mathbb Z\). A comparison of statements, not titles, found none of these to imply the claimed all-particle first-collision side-mark factorization and tridiagonal finite-size lifetime classification. Historical priority remains a real residual risk, not a proof of uniqueness.

## Value — PASS
This is a structural collision-location law: on an unbalanced bipartite network the less populous side can host almost all first collisions, despite individual walkers spending half their stationary time in either part. It is exact for every particle number and every distinct starting configuration, independent even of the time and identity of the first colliding pair. The all-\(k\) one-dimensional generator computes a global first-encounter law using at most \(k+1\) states instead of a configuration-space chain, and its rare-event scaling isolates the pair-count dependence. This addresses a natural measurable outcome for encounter-based particle models, not an arbitrary numerical slice.

## Closest literature, risks, and scope
- https://arxiv.org/abs/1903.09178 — two walkers and complete-bipartite meeting transforms; strongest direct comparison, temporal \(k=2\) case covered.
- https://arxiv.org/abs/0906.0810 — many-particle mean recurrence intervals for a distinguished walker, not first collision from distinct deterministic starts.
- https://arxiv.org/abs/2203.08523 — infinite-lattice collision measures, not finite biclique marks.
- Residual risk: earlier specialized probability literature could contain the mark independence or equivalent generator; no independent priority check has been performed.

Self-review: passed. Independent audit: not yet performed.
