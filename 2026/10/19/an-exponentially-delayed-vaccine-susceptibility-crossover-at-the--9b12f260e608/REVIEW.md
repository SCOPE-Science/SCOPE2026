# Scientific assessment

## Correctness

**PASS.** The full six-compartment equations conserve population mass and stay nonnegative. At the critical condition \(R_0\phi=1\), the exact scalar identity \(\dot Z=1-sZ^{-\alpha}-vZ^{-\varepsilon}\) follows from the infectious balance with no approximation. Uniform bounds \(1+it\le Z\le1+t\) make all fixed-parameter limits rigorous and yield bounded convergence at rescaled exponential times. The cumulative reinfection identity subtracts *postinitial primary infections* from all postinitial infections, avoiding a mistaken initial-infection count. A standalone numerical verifier independently integrates both model formulations and checks the crossover.

## Originality

**PASS within the stated model, with residual risk.** Gutierrez and Gog (medRxiv 2025; journal 2026), whose Section 4 supplies the same leaky SIRI equations, restrict their subsequent final-size calculations to the strict \(R_0\phi<1\) regime. They do not claim the equality-line vaccination crossover. Katriel's 2010 partial-immunity model addresses the reinfection threshold without a distinct vaccinated-never-infected group; its established critical extinction conclusion is expressly acknowledged. Gomes–White–Medley's earlier vaccination/reinfection models differ in demography and immune action. Broad indexed searches did not identify this exact logarithmic-time crossover, although generalized critical-slowing results or unindexed work may cover it. Similarity searches are not proof of novelty.

## Mathematical value

**PASS.** The exact coefficient of the cumulative reinfection offset exhibits a singular dependence on whether vaccine-induced susceptibility equals or just exceeds infection-induced susceptibility. The profile quantifies how a small immunity-parameter gap produces an exponentially long transition, despite the same prevalence decay exponent. This addresses a precise and motivated gap at the equality line of a published vaccination SIRI model; neither a routine fixed-time approximation nor a mere parameter substitution yields the matched exponential-time limit.

## Boundaries and remaining risks

The statement is deterministic and conditional on exact criticality, no demographic turnover, and positive initial infectives. Finite population extinction and different reinfection immunity rules can eliminate the predicted asymptotic regime. Earlier general dynamical-systems theorems may subsume part of the universal \(1/t\) tail; that universal tail is supporting context, not a separate novelty assertion. The main unresolved originality risk is an older specialized analysis of the same two-stratum leaky SIRI crossover not indexed in the reviewed sources.

Self-review: passed. Independent audit: not yet performed.
