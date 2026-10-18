# Scientific review

## Correctness — PASS
The optimization reduces rigorously to one positive quadratic root from the KKT equations. All marginal entries are explicit, hard-zero feasibility is characterized exactly, and TV is four identical blockwise mass changes. The uniform and strict-slack extrema follow from verified monotonicity in the two marginal parameters. The linearized full Sinkhorn sweep is derived independently and has a rank-two whitened form; two exact nonnegative squares prove the sharp spectral bound and equality conditions. The standalone numerical verifier passed 8,467 seeded rational and numerical checks. Finite checks supplement rather than prove the quantifiers.

## Originality — PASS, residual priority risk
Constrained Sinkhorn methods and hard-zero feasibility are already in Corless–Quinn–Boufelja–Shorten (2024) and Baradat–Ventre (2022). General entropic penalty rates (Weed, 2018) and Sinkhorn local Jacobian rates (Lehmann and collaborators, 2021) are prior mathematics; we do not claim these ingredients. Comparison of published technical material and the explicit one-edge exact minimax statement found no covering combined theorem. The full content of Espinosa Mena (2024) on sparse-cost Sinkhorn was not retrieved; specialized matrix-scaling literature remains a genuine publication-priority risk. No global novelty certification is asserted.

## Value — PASS
Softly enforcing a genuinely forbidden transport edge trades quantitative constraint leakage against numerical conditioning. The theorem supplies the exact all-dimensions penalty necessary and sufficient for a desired uniform TV tolerance, the sharp change in exponent at a Hall facet, and the worst attainable local full-sweep contraction factor for the same instance. This is a natural complete benchmark and an exact decision-relevant calculation, not an arbitrary finite example.

## Scope and remaining limitations
Exactly one penalized edge; remaining costs separable; positive normalized marginals; exact arithmetic. The full-sweep rate is local and does not determine global iteration counts. The source priority risk above remains open. The independent scientific audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
