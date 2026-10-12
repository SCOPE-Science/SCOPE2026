# Review of Projective coarse-graining is monotone for superfidelity

## Correctness
PASS. The proof is a direct orthogonal-decomposition argument. After separating each state into its coarse-grained component and Hilbert--Schmidt-orthogonal remainder, every term in the superfidelity difference is accounted for exactly. The final inequality is one application of Cauchy--Schwarz in \(\mathbb R\oplus\mathsf H_{\mathrm{HS}}\). Projective pinching satisfies all stated hypotheses. Equality is exactly the equality case of that single Cauchy--Schwarz step.

## Originality
PASS. Mendonça et al. explicitly formulate the arbitrary-projective-measurement inequality as Eq. (29), prove only the commuting special case, and state that the noncommutative case remains to be seen while numerical evidence favors it. Targeted searches for superfidelity, projective measurement, pinching, dephasing, conditional expectation, and monotonicity found no implication-equivalent later theorem. The defining superfidelity paper does not state this projective-monotonicity result in the inspected full text. A later preservers paper was available only at abstract level and is retained as a residual risk.

## Value
PASS. The claim resolves a natural open structural question for an experimentally accessible fidelity surrogate and explains the mechanism through orthogonal coarse-graining. The extension from projective pinching to arbitrary state-preserving Hilbert--Schmidt orthogonal projections gives a reusable criterion, while the exact deficit and equality case characterize when coarse-graining changes superfidelity.

## Closest literature and limitations
The closest source is arXiv:0806.1150, Section III.D, which asks exactly the projective-measurement question. arXiv:0805.2037 defines superfidelity and establishes its upper-bound and other basic properties. The theorem here does not contradict the known failure of superfidelity monotonicity under arbitrary completely positive trace-preserving maps: orthogonal projections form a special coarse-graining class. Infinite-dimensional and selective-measurement variants are not claimed.

Self-review: passed. Independent audit: not yet performed.
