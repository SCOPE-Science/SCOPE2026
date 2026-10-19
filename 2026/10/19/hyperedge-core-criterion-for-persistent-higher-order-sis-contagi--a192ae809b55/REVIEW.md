# Scientific review

## Correctness
PASS. The equilibrium support identity follows exactly from positivity of each hyperedge coefficient. A half-density subsolution and monotone fixed-point iteration construct equilibria on every Boolean fixed support at the same explicit rate. The decreasing peeling sequence bounds every empty-core trajectory with a rigorous polynomial-times-exponential envelope. Invariance and step-size boundaries are checked. The finite checker is supplementary, not an infinite proof.

## Originality
PASS, with residual literature risk. The primary full-text arXiv versions of Liang–Cui–Liu (2024, Sections 2, 3, 6, 9.8) and Cui et al. (2023, Theorems 3 and 8) describe related tensor SIS models but use spectral transmission thresholds, irreducibility or positive entire-state equilibria. The present necessary-and-sufficient rate-independent *hyperedge support-core* criterion for arbitrary reducible directed networks and the simultaneous realization of all exact supports are not implications of those stated conditions. Indexed research records and topical literature searches found epidemic-threshold and support-adjacent studies but no covering theorem. The final 2026 journal version and wider monotone Boolean network literature remain possible risks.

## Value
PASS. Deciding whether any infection can persist at any rate is a natural network-intervention task, fundamentally distinct from estimating a reproduction number at one rate. The theorem gives a combinatorial exact criterion, a finite pruning algorithm independent of unknown rates, an explicit sufficiency scale for every possible endemic support, and a global extinction bound when the core vanishes. All parts follow from a single structural proof rather than isolated parameter cases.

## Limits and closest work
The model intentionally excludes pairwise infection; small pairwise terms can change the criterion. The high-rate bound is not sharp. The work proves existence but not attraction of endemic equilibria. The mean-field conclusions do not directly transfer to stochastic extinction times. Relevant original results are Liang, Cui and Liu (2024), Proposition 8 and Proposition 9; Cui et al. (2023), Theorems 3 and 8; Higham and de Kergorlay (2021), spectral extinction thresholds.

Self-review: passed. Independent audit: not yet performed.
