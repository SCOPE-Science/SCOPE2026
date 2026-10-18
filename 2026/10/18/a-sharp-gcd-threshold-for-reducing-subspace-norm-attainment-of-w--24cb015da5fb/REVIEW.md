# Review of the gcd threshold theorem

## Correctness — PASS
The exact product formula for the powers of a unilateral shift makes the norm-one eigenspace of its squared modulus explicit. Necessity comes from the reducing residue spaces of each power. Sufficiency uses the *-cyclic span of one unit-norm coordinate per residue, which intersects every nonzero reducing subspace. The arithmetic implication is proved using a missing-residue pigeonhole argument, and the converse by constructive Chinese-remainder block placement. Both directions include every positive pair of power indices. The modulus statement follows from the complementary diagonal subspace supported on deficient entries, and its converse from finite spectral support.

The finite checker exhaustively tests 900 power pairs in the arithmetic reduction and explicit sharpness witnesses in all failing pairs of indices at most 12. These tests are not a proof of the unbounded case; the analytical argument supplies that proof.

## Originality — PASS with residual risk
The September 29, 2026 Su--Zhang study defines the reducing-subspace norm-attainment and modulus subclasses, and provides a particular weighted-shift separation (Example 2.7); Sections 4–7 address perturbation properties. Its published claims do not establish a power-by-power gcd implication or the complete residue test. Gu (2018) studies reducing subspaces of weighted-shift powers but not this norm-attainment arithmetic threshold. The 2022 Ramesh--Osaka precursor was not accessible in full, so equivalent earlier statements under another presentation remain a priority risk. Related published results on the operator-norm profiles of weighted shifts do not determine attainment of the norm on all reducing subspaces.

## Mathematical value — PASS
The precise inequality \(m\geq2d-\gcd(m,d)\) is a complete, sharp law describing which powers universally transmit a structural attainment property; it has nontrivial arithmetic gaps (e.g., the fourth power does not force the third). Every negative instance admits a counterexample arbitrarily close in norm and compactly equivalent to the unilateral shift. The proof also separates attainment for all powers from attainment by their moduli. These statements connect a recent perturbation-theoretic framework to an exact, readily usable criterion, rather than merely repeating an isolated example.

## Limits
Zero weights, weights whose moduli fail to approach one, and the stronger absolute-norm-attaining class are outside the theorem. Available comparison of the original 2022 precursor was abstract-level. The finite checker cannot certify analytical completeness.

Self-review: passed. Independent audit: not yet performed.
