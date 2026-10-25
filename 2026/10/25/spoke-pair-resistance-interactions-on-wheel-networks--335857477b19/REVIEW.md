# Scientific review

## Correctness — PASS

The theorem has explicit graph conventions, exact rank-two updating, and periodized Green-kernel formulas. The proof checks every denominator via positive definiteness on the zero-sum subspace. Strict discrete convexity yields monotone wheel Green correlations and the single sign change. Direct rational evaluations prove the five small boundary cases, while an explicit exact geometric-series bound handles every larger wheel. The first-negative asymptotic follows from a uniform expansion at logarithmic separation, not experimental extrapolation. `verify.py` independently checked 222 exact finite identities and comparisons; these are corroboration, not an infinite proof.

## Originality — PASS, with residual risk

The closest mathematical input is Carmona, Mitjana and Monsó, *Effective resistances and Kirchhoff Index in subdivision networks* (arXiv:1609.04642v1): its Section 5 computes wheel Green kernels but studies subdivision networks rather than two deleted hub spokes. Gago's 2016 non-complete-wheel work treats equally spaced retained spokes. These sources supply powerful background but do not establish the general interaction-sign phase transition, adjacent maximizer, or asymptotic crossover. The Gago full paper could not be inspected completely; an equivalent unindexed result remains possible. General rank-two update algebra and the wheel's unperturbed Green kernel are not claimed as new.

## Value — PASS

The wheel is a natural hub-and-ring fault-tolerant network. The result separates compounding from compensating two-link damage with a sharp network-size boundary, locates all worst spoke pairs, and quantifies the crossover distance on expanding wheels. It is a natural complete sign classification for the specified failure family, with an exact finite evaluation rule and a nontrivial asymptotic scale.

## Limits

Only pairs of spokes and unit conductances are treated; rim failures and heterogeneous networks are outside scope. The precise integer crossover is given by a closed sign test, not by a simpler universal floor formula. Historical uniqueness is not established and one plausible source remained only partially accessible. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
