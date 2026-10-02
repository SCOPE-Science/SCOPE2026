# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-23a37c2c63fd`

## Correctness — PASS

The all-rate theorem is mathematically correct under the stated reversibility and growth-weighted assumptions. Detailed balance symmetrizes the mutation generator, and the spectral bound becomes a generalized Rayleigh quotient. Because every growth rate strictly increases with substrate and the maximizing quotient is positive, the denominator strictly decreases for the same maximizer, proving strict substrate monotonicity at every positive mutation intensity. The equilibrium threshold then follows from Perron–Frobenius. At the critical dilution value, the left Perron functional is nonincreasing and its zero-derivative set contains no nonzero-biomass invariant trajectory, while the stated mass bound gives precompactness; LaSalle yields global attraction and the auxiliary substrate inequality yields stability. The mutation-strength derivative and large-rate harmonic-mean limit follow from the symmetric quotient and the one-dimensional reversible kernel. Independent numerical reproduction matched every threshold number in the stored diagnostic output.

### Sources
- assigned RESULT.md
- artifacts/verify.py
- artifacts/verify-output.txt
- independent NumPy reproduction of the source example

### Risks
- The theorem requires irreducible reversible mutation and the special growth-weighted exchange form; it does not cover general substrate-dependent exchange matrices.

## Originality — PASS

The motivating chemostat paper's public abstract advertises only a positive small-perturbation stability threshold in the general theory, and fresh semantic searches found no published theorem giving strict substrate Perron monotonicity for every mutation rate together with the exact all-rate equilibrium threshold and critical-equality washout stability for this reversible growth-weighted class. Altenberg's reduction principle supports the mutation-intensity monotonicity component but does not imply the substrate-threshold theorem.

### equivalent_formulations

Searches:
- growth-weighted mutation chemostat all rate threshold reversible
- Perron root substrate monotonicity chemostat mutation every epsilon

Evidence:
- The exact semantic match was the audited result; no equivalent external theorem was located.

Reasoning:
Equivalent formulations via spectral bound, mutation-selection matrices, and washout threshold were searched.

### broader_coverage

Searches:
- Global stability of perturbed chemostat systems Alvarez-Latuz Bayen Coville
- reduction phenomenon resolvent positive operators mixing

Evidence:
- The source paper publicly states a small-perturbation global-stability theorem and supplements it with steady-state/numerical studies; reduction-principle literature controls mixing intensity, not the whole audited substrate theorem.

Reasoning:
These broader sources do not imply all four audited conclusions as a package.

### exact_database_or_table

Searches:
- chemostat mutation threshold tables and Section 4.2 numerical values

Evidence:
- The package reproduces the source example numerically, but no database/table establishes strict monotonicity for the continuum of substrate values and all mutation intensities.

Reasoning:
Finite numerical curves are not a proof of the all-rate theorem.

### claim_vs_prior_implication

Searches:
- claim versus source small-rate result and general reduction phenomenon

Evidence:
- The audited Rayleigh-quotient argument removes the small-rate restriction under reversibility and adds critical-threshold global asymptotic stability.

Reasoning:
Neither inspected prior statement mechanically yields those strengthened conclusions.

### source_inspections

- **Global stability of perturbed chemostat systems** — https://arxiv.org/abs/2501.08011. Trigger: Motivating primary source and closest model. Material read: Primary abstract and public scope information; direct full-text retrieval through the audit web route was unavailable. Method: Scope and implication comparison. Assessment: The public source states global stability below a positive perturbation threshold and numerical/steady-state analyses; it does not publicly state the audited all-rate reversible theorem. Evidence: The abstract explicitly phrases the main stability theorem as holding below a positive perturbation threshold.
- **Resolvent positive linear operators exhibit the reduction phenomenon** — https://doi.org/10.1073/pnas.1113833109. Trigger: Broad prior result on decrease of spectral growth under mixing. Material read: Public abstract/scope. Method: Theorem-scope comparison. Assessment: Relevant to mutation-strength monotonicity, not covering the substrate-monotonicity and equilibrium/stability theorem. Evidence: The reduction phenomenon concerns how mixing intensity changes the spectral bound.
- **Assigned reversible diagnostic** — artifacts/verify.py. Trigger: Numerical corroboration of the source example and symmetrization. Material read: Complete source and complete stored output. Method: Code inspection plus independent numerical reproduction. Assessment: All displayed threshold values and the harmonic limit reproduce; diagnostics are not used as the infinite proof. Evidence: Independent values match to the printed precision.

### checked_sources

- arXiv:2501.08011
- DOI:10.1016/j.nonrwa.2025.104509
- Altenberg 2012 reduction principle
- arXiv:2110.09582
- Resultary semantic search
- assigned proof and artifacts

### residual_risks

- The final journal/HAL revision of the motivating paper was not inspected in full in this run.
- Lobry 2013 Section 4.2, cited by the motivating paper as related, was not available in full and remains a historical overlap risk.

## Scientific value — PASS

Removing a mutation-rate restriction in a natural reversible class, giving an exact coexistence/washout threshold for every rate, and resolving the critical equality case are meaningful dynamical results. The harmonic-limit formula also gives interpretable structure for the source model. This is not merely a numerical extension.

### Sources
- motivating chemostat model
- reversible Markov-generator spectral theory

### Risks
- The coexistence equilibrium's all-rate stability is deliberately not claimed.

## Limitations

- Scope requires growth-weighted reversible irreducible mutation and strictly increasing growth functions.
- No all-rate coexistence-stability claim is made.
- Originality is best-of-knowledge because two related full-text sources were not available in the audit route.

## Disposition

**PASSED**
