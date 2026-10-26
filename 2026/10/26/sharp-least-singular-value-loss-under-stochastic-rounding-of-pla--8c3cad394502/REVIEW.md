# Scientific review

## Correctness — PASS

The proof reconstructs the entire sixteen-outcome signed-Bernoulli quantization law. Its cases yield the exact squared least-singular-value distribution, from which both expected squared singular value and the singularity probability follow. Completion of the square proves the sharp global relative-loss constant with unique equality input. Differentiation of the fixed-norm loss and strict monotonicity of an explicit rational function establish the exact orientation bifurcation and both extremizer regimes. The accompanying `verify_rounding.py` checked the symbolic identities, 121 rational cases, 1,000 direct-SVD cases and six orientation values. Its finite checks are supporting evidence, not substitutes for the proofs.

## Originality — PASS (provisional)

The closest studied work is Ma, Yu and Drineas, arXiv:2606.00312, whose spectral improvement theorems impose dimensional and spectral/rank requirements absent in this two-by-two equal-spectrum setting. Earlier Dexter et al., arXiv:2403.12278, examine tall-and-thin matrices; Boutsikas et al., arXiv:2303.03547, treat deterministic perturbation estimates. The inspected material does not contain the exact independent-rounding sixteen-outcome law, sharp relative degradation or symmetry-breaking orientation threshold. Focused semantic database queries using the golden-ratio constant, rank-loss probability, planar rotations and orientation transition found no dominating mathematical result; nearby results on SOAP or spectral filters concern different operators. Searches cannot certify uniqueness, and equivalent specialized treatments remain a residual risk.

## Value — PASS

Stochastic rounding is promoted as a spectral regularizer in recent numerical analysis. Its behavior for the smallest nontrivial square, initially perfectly conditioned matrix family is therefore a meaningful boundary test rather than a cosmetic example. The finding quantifies a 30.9% maximal relative loss in expected squared minimum singular-value energy, an exact 9/16 rank-collapse chance at the worst input, and an orientation-design phase transition. This clarifies why broad unconditional regularization inferences are unsafe and shows that the coordinate orientation affects rounding stability. It is not asserted to establish a high-dimensional or practical floating-point counterexample.

## Residual limits

The entire claim is confined to independent unit-cell entrywise stochastic rounding, squared singular values, and the stated scale restriction for orientation optimization. Bibliographic priority outside the inspected papers and database remains uncertain. Independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
