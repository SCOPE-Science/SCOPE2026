# Independent mathematical audit — 2026-10-01

## Final claim assessed

Sharp harmonic stability phase diagram for low-cost UBU integrators

## Correctness — PASS

PASS. The three deterministic harmonic-mode matrices were reconstructed from the displayed schemes and checked with the real two-by-two Jury criterion. Symbolic simplification independently reproduces the determinant and all three Jury factors: for LC-UBU only the negative-one boundary remains and gives the hyperbolic-cotangent threshold; for LCT-UBU the second condition forces the strict friction barrier and the third gives the stated rational threshold; for LCP-UBU the third condition gives the sharp rational threshold while the determinant condition is weaker. Differentiation gives the stated minima, and the large-friction limits follow directly from the exact boundary equations. The saved 30,000-point eigenvalue replay agrees but is not used as the proof.

## Originality — PASS

PASS to the best of current knowledge. The primary 2026 ULMC source was inspected in full-text method and analysis sections; it introduces LC-UBU, LCT-UBU and LCP-UBU but does not state a Jury/Schur phase diagram, the Taylor friction barrier, the Padé minimum, or the three stiff-friction asymptotics. Published-record search returned this record as the exact match. General stochastic-Verlet linear analysis establishes the diagnostic methodology but does not mechanically imply these new source-specific threshold formulas without deriving the new matrices and applying the criterion.

### equivalent_formulations

Searches: Resultary: LC-UBU LCT-UBU LCP-UBU harmonic Schur stability Taylor friction barrier Pade; arXiv:2609.20713 full-text search for stability/Jury

Evidence: No earlier equivalent threshold record was returned. The source defines the same schemes but does not state the harmonic Schur region in the inspected text.

Reasoning: Equivalent formulations as spectral-radius, Jury, and harmonic absolute-stability criteria were compared.

### broader_coverage

Searches: Linear Analysis of Stochastic Verlet-Type Integrators for Langevin Equations; general Langevin harmonic stability

Evidence: General linear-analysis methodology predates the source schemes.

Reasoning: A generic criterion does not itself contain the new amplification matrices or their exact source-specific thresholds; those formulas require a fresh derivation.

### exact_database_or_table

Searches: Resultary exact semantic search for S_E S_T S_P thresholds

Evidence: No database/table is natural for a parameterized stability region; no earlier exact record was found.

Reasoning: The relevant exact comparison is theorem-level rather than tabular.

### claim_vs_prior_implication

Searches: arXiv:2609.20713; Journal of Statistical Physics 193 linear stochastic Verlet analysis

Evidence: The primary source supplies convergence results but not these stability boundaries; the generic prior literature supplies tools only.

Reasoning: Neither inspected source mechanically yields the final threshold functions without source-specific algebra.

## Scientific value — PASS

PASS. The exact phase diagram materially distinguishes three newly proposed schemes that share the same formal convergence class: one gains a friction-expanded curvature window, one has a hard friction-step barrier, and one has a finite Padé limiting window. These boundaries are directly useful for selecting stable steps on stiff quadratic modes and are more than a routine single-instance check.

## Source inspections

- **A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New** — https://arxiv.org/abs/2609.20713. Material read: Full-text method definitions and convergence-analysis sections, with targeted searches for harmonic stability, Schur/Jury and covariance terms. Assessment: PRIMARY_SOURCE_NOT_COVERING_PHASE_DIAGRAM. Evidence: The schemes and Wasserstein rates are present, but the inspected source does not give the exact harmonic stability regions.
- **Linear Analysis of Stochastic Verlet-Type Integrators for Langevin Equations** — https://doi.org/10.1007/s10955-025-03553-3. Material read: Bibliographic and theorem-context material located by targeted literature search. Assessment: GENERAL_METHOD_NOT_SOURCE_SPECIFIC_COVERAGE. Evidence: It supplies broad stochastic-Verlet linear analysis, not the newly introduced LC-UBU/LCT-UBU/LCP-UBU threshold formulas.

## Limitations and residual risks

Exact for quadratic potentials and the affine Gaussian harmonic chain; it is not a nonlinear stability or invariant-bias theorem.

- A generic rational-integrator paper in another parameterization could contain an equivalent threshold after a nontrivial recasting; none was located.
- The theorem is exact only for quadratic mean/finite-second-moment stability.

## Disposition

**passed**
