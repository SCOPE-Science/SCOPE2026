# Independent mathematical audit — 2026-10-01

## Final claim

Sharp pointwise-reversal threshold for stabilized CN/AB Allen-Cahn stepping

## Correctness — PASS

PASS. For homogeneous states the Laplacian vanishes and the scheme rearranges to a positive scalar factor times the two-level Adams-Bashforth reaction bracket. Thus the increment changes sign exactly when three times g at the exact starter equals g at the initial state, where g is the cubic positive-branch reaction function. The exact starter is strictly increasing and g is unimodal, so there is one crossing on the decreasing branch. Solving the exact-flow relation gives the stated threshold, and differentiation shows the crossing is transverse. The same calculation gives the general over-extrapolation law. The repository verifier and recorded output were inspected; for initial value one half they reproduce the sharp dimensionless threshold 1.48082061672206, below the cited sufficient value 1.58902691517397.

## Originality — PASS

PASS to the best of current knowledge. The 2026 Li-Wang paper is the exact motivating source and its indexed material establishes large-step wrong-signed increments and perturbative persistence. Searches for an exact if-and-only-if CN/AB crossing and the general over-extrapolation law returned the audited record as the exact match; a later record on auxiliary-energy shifts concerns different schemes. The full Li-Wang text was not retrievable in this run, so theorem-level noncoverage remains an explicit residual risk.

### equivalent_formulations

Searches: stabilized CN AB Allen Cahn exact reversal threshold pointwise monotonicity exact starter; CNAB exact first reversal threshold cubic level crossing

Evidence: The exact semantic search returned the audited record; no earlier exact threshold formula was located.

Reasoning: The scalar level-crossing formulation is equivalent to the first-increment sign threshold; no inspected prior result states that equality boundary.

### broader_coverage

Searches: arXiv:2609.19023 pointwise monotonicity Allen Cahn large step reversal; stabilized Crank Nicolson Adams Bashforth phase field

Evidence: The motivating paper gives large-step reversal context, while earlier CN/AB work studies stability and error properties.

Reasoning: A sufficient reversal certificate does not mechanically imply the exact onset or its general extrapolation law.

### exact_database_or_table

Searches: published mathematical record semantic search CNAB threshold

Evidence: No natural table/database exists for this continuous threshold, and no earlier exact record was found.

Reasoning: The exact-search task is theorem comparison rather than table lookup.

### claim_vs_prior_implication

Searches: Li Wang 2609.19023 reversal threshold; Li Wang Allen Cahn critical step size

Evidence: Available indexed statements establish a large-step failure but do not force the exact cubic crossing boundary.

Reasoning: The audited scalar reduction computes a sharp boundary rather than merely substituting parameters into a prior closed formula.

## Scientific value — PASS

PASS. Determining the exact onset of a qualitative failure in a widely used stabilized second-order phase-field integrator is a motivated sharp-boundary result. It replaces a conservative sufficient certificate by an if-and-only-if threshold, shows stabilization cannot move that first homogeneous sign reversal, and isolates over-extrapolation as the mechanism.

## Source inspections

- **Pointwise Monotonicity of the Allen-Cahn Flow and Dynamical Limitations of Energy-Stable Schemes** — https://arxiv.org/abs/2609.19023. Material read: Abstract and indexed result material; full text retrieval was unavailable during this audit. Assessment: PLAUSIBLE_PRIMARY_SOURCE_WITH_ACCESS_LIMITATION. Evidence: Available material establishes the large-step reversal phenomenon and perturbative context but does not expose an exact if-and-only-if threshold formula.
- **Stabilized Crank-Nicolson/Adams-Bashforth Schemes for Phase Field Models** — https://doi.org/10.4208/eajam.200113.220213a. Material read: Bibliographic and indexed result context. Assessment: BACKGROUND_SCHEME_ANALYSIS. Evidence: The earlier work concerns stabilized scheme analysis rather than the audited exact first-reversal boundary.

## Limitations and residual risks

The if-and-only-if threshold assumes the exact homogeneous starter and classifies only the first post-starter increment. The nonhomogeneous extension is perturbative rather than a universal sharp threshold. The general extrapolation statement concerns homogeneous over-extrapolated reaction forcing multiplied by a positive update factor.

- The full text of the extremely recent Li-Wang preprint was not retrievable in this run, leaving a bounded theorem-level originality risk.
- The sharp threshold concerns only the first increment after the exact starter, not arbitrary later steps or arbitrary spatial data.

## Disposition

**passed**
