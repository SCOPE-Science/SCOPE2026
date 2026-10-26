# Self-review

## Correctness — PASS

The stated model is exactly the symmetric three-mode model with positive rates, a target detecting only in the diffusive mode, and complete resets to the starting position and starting mode. The first-arrival transforms are the published equations (22) and (25), evaluated at the reset rate, and the Poisson renewal expression is the published equation (35). Subtraction factors as two decaying exponentials whose coefficients are determined by the polynomial evaluations \(P(h)<0\) and \(P(K)\). The former establishes ordered positive decay exponents; the latter gives the **necessary-and-sufficient**, diffusion-to-ballistic-rate-independent boundary \(v^2=D(q+r)\). The crossing's uniqueness is proved by an increasing exponential ratio. At each extreme of the permissible reset-rate window, the smaller coefficient vanishes with a proved power, yielding the two stated logarithmic divergence coefficients. The included script passed symbolic identities and numerical sanity checks; numerical tests are not the infinite proof.

## Originality — PASS, with risk

Flaquer-Galmés, Campos and Méndez (2024) give both exact initial-mode Laplace first-arrival transforms and a large-distance asymptotic ratio. The complete primary manuscript, its figures and relevant formulas were compared. The existing paper does not state the unique global distance crossover, universal switching-rate-independent threshold, or reentrant reset-rate window with two logarithmic endpoints. The 2011 intermittent-search and 2020 resetting reviews establish general context and renewal theory, not the inspected model-specific conclusion. A prior related stationary-position equality uses the same parameter boundary but addresses a distinct observable; equality of spatial laws does not entail first-arrival time ordering. Since an algebraic deduction from complete published formulas may exist elsewhere, priority risk remains, as do limitations from partial access to broader reviews.

## Mathematical value — PASS

Choosing the preferred initial phase is a natural design question for a searcher whose fast relocation phase cannot detect the target. The theorem supplies a global, sharp, physically interpretable answer, including a strict single-switch property and a reentrant preference as the reset rate changes. The logarithmic divergence precisely quantifies how rapidly the ballistic advantage disappears near either endpoint, beyond selecting individual numerical parameters. No unique optimal reset rate is claimed.

## Closest literature and limits

Closest work: Flaquer-Galmés, Campos and Méndez, *Intermittent random walks under stochastic resetting*, Physical Review E 109, 034103 (2024), first preprint 2024-01-30, arXiv:2401.16849. Supporting context: Bénichou et al., Rev. Mod. Phys. 83, 81 (2011); Evans et al., J. Phys. A 53, 193001 (2020). The claims are limited to strictly positive model parameters, symmetric ballistic headings, and complete Poisson resetting; the entire set of reset rates conferring advantage need not be a single interval. An unindexed equivalent inequality and interpretation of the primary exact transforms remain priority risks.

Self-review: passed. Independent audit: not yet performed.
