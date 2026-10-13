# Self-review

## Correctness

PASS. The total population is a state-dependent quantity, so differentiating the exponential normalized incidence contributes to every costate. Direct Hamiltonian differentiation gives the six corrected equations stated in the finding. It also gives the quarantine coefficient \((\lambda_1-\lambda_2)u_3\), not the printed \((\lambda_1-\lambda_3)u_3\). A terminal expansion proves that the omitted recovered-costate incidence term is genuinely active.

## Originality

PASS. Pontryagin epidemic control is prior methodology. The accepted result is the source-specific correction of Theorem 6.2 and its terminal-time consequence. Exact source, adjoint/costate, population-normalization, erratum, and historical-overlap searches found no equivalent published correction.

## Value

PASS. The source says its iterative numerical method solves the optimality system and uses the result to produce Figure 7 and the reported optimal media/quarantine strategy. A wrong adjoint system breaks that certification, so the correction is materially relevant to reproducibility rather than a cosmetic notation change.

## Closest literature and limitations

Yan and Zou provide a primary example of Pontryagin quarantine/isolation control in a different SARS model. It does not contain the normalized exponential incidence whose state derivatives are omitted here.

Unavailable implementation code could have silently used corrected equations, and the corrected Figure 7 trajectories have not been recomputed.

Self-review: passed. Independent audit: not yet performed.
