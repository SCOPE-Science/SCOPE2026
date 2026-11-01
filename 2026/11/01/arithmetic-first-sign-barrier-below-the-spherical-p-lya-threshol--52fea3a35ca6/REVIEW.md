# Self-review

## Correctness — PASS

The assertion is a first-index asymptotic, not a finite-index certification. The proof defines the Legendre coefficient with unambiguous positive normalization, derives two competing contributions of orders \(L^{-3}\) and \(L^{-\delta-3/2}\), and controls both uniformly for \(\delta\in[5/4,3/2]\) using localized Legendre singularity estimates. The origin term has sign \(+\delta\vartheta^{\delta-1}\) (the normalized Legendre projection of the local \((1-x)^{1/2}\) term), and the cutoff term has the written gamma amplitude and phase. Strict positivity at the boundary exponent comes from Lu's Theorem 3.5, independently of numerical tests. The exponential lower fence covers every degree, including finitely many small ones; the upper fence uses bounded-gap recurrence of rotations, not an unproved equidistribution rate. Exact arithmetic-residue classification was independently enumerated in the checker. Numeric quadrature remains supplementary.

## Originality — PASS, with residual risks

Lu (2024/2025) and the positive Gegenbauer Pólya literature give the threshold positivity but not the location of the first failure below it. Sidi (2011, Theorem 4.2) provides fixed-parameter expansions, including the two applicable types of singularity; the new statement couples a moving exponent with an exponentially large index and calculates a rational-angle phase obstruction. Beatson–zu Castell–Xu (2011/2014) formulates the all-degree sign criterion but contains neither a phase-dependent onset law nor this exponential constant. Ge's 2026 full-text work concerns Euclidean-to-spherical failures for different kernels. No equivalent or broader first-negative-degree theorem was located in the scientific comparisons documented in `AUDIT.json`.

The closest potentially dominating source is Sidi: the present proof adds parameter-uniform control and the two-sided arithmetic first-index optimization rather than renaming the fixed-parameter coefficient expansion. Unindexed work on such simultaneous limits may already exist. Global novelty has not been certified.

## Value — PASS

The index is the first harmonic degree at which a standard compactly supported spherical covariance kernel loses spectral positivity. The exact scale determines how difficult finite-degree testing becomes near the known sharp exponent, and the discontinuous rational-angle resonance identifies precisely when phase locking delays detection. The result has an infinite family of exact arithmetic distinctions and a natural sharp boundary, not a selected small numerical case.

## Scope and limits

This is a fixed-angle, two-dimensional, first-failure asymptotic. The derivation supplies no effective error bars at a prescribed positive exponent deficit and is not uniform in the cutoff endpoints. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
