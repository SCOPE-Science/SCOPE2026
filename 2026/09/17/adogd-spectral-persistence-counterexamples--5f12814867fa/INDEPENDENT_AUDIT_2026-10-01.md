# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-5f12814867fa`

## Correctness — PASS

The two endpoint-annihilation counterexamples are exact. For a two-eigenvalue quadratic the first local-curvature value is strictly between the endpoint eigenvalues when both initial endpoint components are nonzero. A seed equal to the reciprocal of one endpoint eigenvalue kills that eigenspace in the seed step, after which the running estimator can never recover the missing endpoint and the displayed nonoptimal constant stepsize follows. The separate summable-step construction is also valid: both scalar products remain positive, so the higher mode does not vanish relatively and the local curvature cannot tend to the smallest eigenvalue. The two repairs correctly add, respectively, endpoint persistence and enough cumulative step mass. The concrete instance with endpoint eigenvalues 1 and 2 was independently recomputed and gives the stated constants.

### Sources
- assigned RESULT.md
- independent two-mode recomputation
- arXiv:2608.03546 abstract and public theorem summary

### Risks
- The audit did not obtain a separate full-text copy of the conference proceedings version; correctness is assessed against the theorem as quoted from the current preprint record.

## Originality — PASS

Fresh semantic and web searches found the audited record as the only exact counterexample/repair statement. The motivating preprint still publicly advertises convergence to the optimal constant stepsize, and no correction, erratum, endpoint-annihilation counterexample, or cumulative-step repair was located.

### equivalent_formulations

Searches:
- AdOGD endpoint eigenspace annihilation counterexample
- AdOGD Theorem 8 reciprocal eigenvalue seed
- summable steps local curvature Lemma 4

Evidence:
- The exact published-record search returned the audited finding; public search results for the source continue to describe Theorem 8 as convergence to the optimal constant stepsize.

Reasoning:
The equivalent spectral-persistence and local-curvature formulations were searched, not just the paper title.

### broader_coverage

Searches:
- adaptive gradient descent spectral identification endpoint persistence
- Barzilai-Borwein adaptive curvature estimation counterexample

Evidence:
- No broader theorem or correction was found that contains the exact two failure mechanisms and repaired hypotheses.

Reasoning:
General adaptive-gradient literature does not imply these paper-specific counterexamples.

### exact_database_or_table

Searches:
- published correction/erratum for arXiv:2608.03546 and IFAC paper

Evidence:
- No corrected theorem text or erratum was located in the inspected public records.

Reasoning:
This claim is not naturally database driven; correction status is the relevant exact-record check.

### claim_vs_prior_implication

Searches:
- comparison with Theorem 8 and lower branch of Lemma 4 as publicly summarized

Evidence:
- The source's advertised convergence claim is contradicted by the exact seed calculation, while the summable-product example targets an independent proof premise.

Reasoning:
The counterexamples are not corollaries of a located prior result.

### source_inspections

- **Pursuing Optimal Stepsize in Adaptive Gradient-Based Quadratic Optimization** — https://arxiv.org/abs/2608.03546. Trigger: The result directly audits this recent theorem. Material read: Primary-source abstract plus searchable public theorem description; direct full-text retrieval was unavailable in the audit route. Method: Statement comparison with independent algebraic reconstruction. Assessment: The public source still claims convergence to the optimal constant stepsize; no public correction was found. Evidence: The abstract states that the proposed algorithm converges to the optimal constant stepsize.
- **Assigned mathematical package** — RESULT.md. Trigger: Complete proof and exact examples under audit. Material read: Complete file from the assigned source tree. Method: Line-by-line proof reconstruction and independent numerical substitution. Assessment: Both counterexamples and the repaired theorem are internally correct. Evidence: For endpoint eigenvalues 1 and 2 the recomputed first curvature is sqrt(17/5), producing the stated nonoptimal limiting stepsizes.

### checked_sources

- arXiv:2608.03546
- public theorem-level summary of Theorem 8
- Resultary semantic search
- assigned RESULT.md

### residual_risks

- A distinct final proceedings theorem text was not obtained and could conceivably already contain a repair.
- The motivating work is recent, so an unindexed correction remains possible.

## Scientific value — PASS

Correcting a central convergence theorem of a new adaptive optimization method, isolating a separate infinite-product gap, and supplying minimal structural repairs are mathematically consequential and directly reusable. The examples are not arbitrary tiny counterexamples: they identify exactly which spectral persistence and cumulative-motion hypotheses the asymptotic argument needs.

### Sources
- motivating AdOGD theorem
- assigned counterexamples and repairs

### Risks
- The exact theorem failure occurs at exceptional reciprocal seed values, although near-exceptional seeds also create arbitrarily long finite-horizon shadowing.

## Limitations

- Assessment concerns the theorem as publicly available in the inspected source record.
- The repaired theorem is quadratic-specific.
- No computational artifact is required; the proof is exact and finite-dimensional.

## Disposition

**PASSED**
