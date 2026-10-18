# Review of the nine-line realization-curve result

## Correctness

PASS. Projective-frame normalization determines the nine dual points uniquely from the eight specified flats. The 84 triple determinants reduce to the prescribed eleven zero minors and 73 allowed-factor nonzero minors. The logarithmic-derivation/Euler splitting is a two-way correspondence in degree four. A symbolic 12-by-12 minor is nonzero away from exactly the permitted parameter \(a=2\); a kernel vector and nonzero 11-by-11 minor establish the one-dimensional rank deficiency there. A universal degree-five relation from the fourfold point completes the exact dichotomy. The standalone checker reproduces the nonstandard polynomial identities. Only complex characteristic zero and the indicated labelled lattice are proved.

## Originality

PASS on the searched record, with residual literature risk. Dimca–Pokora (arXiv:2607.01985v1, Sections 3–7) establish only two discrete examples and their syzygy degrees, not a complete moduli space and a globally unique jump point. Their broader Ziegler-pair preprint (arXiv:2606.20421) recalls the two examples and analyzes other ten- and eleven-line families, not the claimed nine-line classification. Ye (arXiv:1112.4306, especially Theorem 3.9) provides nine-line realization-space irreducibility classifications, but not the explicit parameter or syzygy-jump computation. Semantic searches of published research findings for the lattice, family, parameter normalization, and syzygy jump did not return an implication covering this statement; nearest related arrangement results concerned other lattices and invariants. Undiscovered or unindexed literature remains a general risk.

## Value

PASS. The motivating 2026 counterexample distinguishes only two points with the same lattice but different values of an invariant central to a Terao-type conjecture. Giving a complete one-dimensional fixed-lattice realization moduli space and proving a **single isolated degree-four exception** answers how exceptional that failure is: the counterexample occurs at a proper, explicit jump locus rather than generically. The determinant certificate links combinatorial realization geometry to logarithmic derivations, making the full-locus result useful for studying deformations and semicontinuity, beyond repeating the two known examples.

## Boundaries and risk

No assertion is made about all line lattices, unlabelled quotient moduli, characteristic-positive specializations, full graded resolutions, or a global novelty certificate. Computational determinants are exact in rational polynomial arithmetic and reproduced in `verify.py`; the accompanying argument explains their mathematical implications. The closest three research texts were inspected materially; the most plausible residual risk is a different, poorly indexed parametrization of this same nine-line lattice.

Self-review: passed. Independent audit: not yet performed.
