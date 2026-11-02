# Scientific review

## Correctness — PASS

The unitary Zak transform diagonalizes the complete indexed Gabor system, and the two-term tent-spline Zak polynomial has a common frequency minimizer and maximizer for every offset. Its minimum is four times the sum of squared intrinsic circle distances, so both constants are optimal. A circular energy below \(a/4\), with \(0<a<1/4\), puts all points into one short lifted arc. The lifted sample variance is then an ordinary quadratic form in \(m-1\) independent uniform differences with determinant \(1/m\). An exact ellipsoid volume gives the probability formula, and layer-cake integration gives the moment cutoff; these are infinite-parameter proofs, not extrapolations from finite tests.

The standalone deterministic `CHECK.py` was run against the staged version of the new mathematical claim and returned 3360 passing assertions. These checks concern rational phase tuples, the full two-shift sharp formula, and convergence of the explicitly sampled Zak multiplier to the proven minimum. They do not certify the probability law independently.

## Originality — PASS under inspected evidence

Raj and Sivananthan (arXiv:2503.20259v1) provide a general random-periodic Zak method and nonoptimal probabilistic bounds for sufficiently many translation classes. They do not calculate the sharp lower frame bound for the triangular window or its exact probability distribution. Buck et al. (arXiv:2603.16986v1) study finite Gram sections on single rectangular lattices rather than unions of random translation cosets. The 2016 frame-set literature for compactly supported windows also treats rectangular lattices, without a distribution for these random cosets. Comparisons included aliases involving exact Gabor bounds, circular variance, multi-coset shifts, and condition-number tails, not merely matching paper titles. The distinct random-periodic probability law and its \(m=4\) finite-mean threshold were not found in the inspected claims.

**Residual risk:** An older result in random multisets on the circle or nonlattice sampling may implicitly contain this exact formula. A related 2026 nonlattice obstruction paper was available only at abstract level; no full-text negative conclusion is claimed. Searches establish best-known overlap assessment rather than certified uniqueness.

## Value — PASS

The result provides an exact deterministic stability measure and a sharp probability of catastrophic near-degeneracy, not only existence. Its distinction between almost-sure existence for two shifted classes and finite mean condition number only from four classes onward is a natural sampling-design consequence. The constants hold for every integer \(m\ge2\), with no asymptotic or numerical fit; the random small-ball identity holds on an explicit nontrivial open interval.

## Limits and closest literature

The fixed tent window and unit-frequency modulation are essential. The distribution formula is exact for \(0<a<1/4\), and the general condition-number tail for \(K>4m\); no full distribution is claimed for higher \(m\). The primary source comparisons are Raj--Sivananthan (2025), Buck--Frederick--Okoudjou--Stangl (2026), and Christensen--Kim--Kim (2016). External independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
