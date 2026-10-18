# Review of periodic-jitter frame recovery

## Correctness

**PASS.** The infinite-dimensional step is a standard, explicitly stated Riesz bound for normalized Hardy kernels on the distinct powered Carleson nodes. Splitting all time samples into residue classes gives a two-sided bound by a direct sum of finite Vandermonde forms. The proof separately checks powered-node interpolation, finiteness of nonsingleton fibers, uniform scalar normalizations, necessity and sufficiency of fiber ranks, availability of a finite period, and the simple-zero separation of aliased nodes under positive jitter. Lagrange denominators prove the lower-frame exponent; annihilation of low Taylor moments within a maximal collision cluster proves the matching upper estimate. Finite diagnostics supplement but do not certify the infinite argument.

## Originality

**PASS on accessible evidence, with residual publication-priority risk.** The closest 2026 source proves universal-offset stability below an angular threshold and demonstrates **failure** of unjittered powers beyond it. A remark observes unjittered stability in the absence of power collisions. These facts do not imply finite-fiber recovery or its singular-value exponent once collisions actually occur. The 2025 predecessor concerns positive spectra and the July 2026 block-diagonal paper concerns Jordan blocks and nonnegative-spectrum sampling. Targeted mathematical-record and literature searches identified no exact periodic micro-jitter rank theorem. The related Kadec-type sampled-group-orbit perturbation result presupposes an original frame, unlike this repair of an incomplete orbit. A differently phrased multi-channel interpolation result could still overlap, so independent priority assessment remains appropriate.

## Value

**PASS.** The large-step failure exhibited in the motivating paper is not an intrinsic density obstruction for any **fixed** Stolz Carleson spectrum: a deterministic, arbitrarily small, bounded periodic offset resolves all finitely many aliased spectral clusters. The theorem supplies a necessary-and-sufficient criterion for every periodic offset design, an exact minimum-period test and quantifies the exact stability cost in terms of the highest collision multiplicity. This converts a sharp uniform non-recovery boundary into a constructive spectral-dependent recovery principle. It does not claim uniform design across all spectra or optimal numerical constants.

Self-review: passed. Independent audit: not yet performed.
