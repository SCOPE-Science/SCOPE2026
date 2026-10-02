# Independent audit — SCOPE-20260917-c0e67940f3c0

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the adaptive bioelectric model, differentiating the instantaneous voltage-coupling energy adds a conductance-work term; the published two-term full-model balance is therefore only valid in the fixed-conductance and zero-extra-forcing specialization, and an explicit two-cell state has zero voltage velocity but positive energy derivative from conductance adaptation.

## Correctness

**PASS** — Differentiating the stated energy with time-dependent symmetric conductances gives the extra one-half sum of conductance derivatives times squared voltage differences exactly. Substitution of the voltage equation yields the claimed balance. A fresh numerical evaluation of the two-cell analytic state at x=1.49 reproduces G=0.01794, essentially zero voltage derivatives, positive conductance derivative 0.0003125799754, and positive energy derivative 0.001387917607. The sign argument is analytic as x approaches the bistable voltage magnitude from below.

Residual risks:
- The result concerns the displayed instantaneous energy and continuous-time dynamics; it does not rule out another composite Lyapunov function or cover discrete morphology events.

## Originality

**PASS** — The source-specific correction was compared against the 2026 Cortés-Poza paper and its model repository. The paper's adaptive conductance law and later full-model energy discussion coexist with a displayed two-term derivative that omits the chain-rule conductance work. Targeted published-results search found only the audited correction. The generic chain rule itself is not claimed as new; novelty is the identified model-specific correction and counterexample.

### equivalent_formulations

Searches: Resultary semantic search: adaptive conductance Lyapunov energy derivative conductance work term bioelectric morphogenesis Cortes-Poza; Web searches for the paper title plus conductance work, energy correction, erratum

Evidence: The exact published-results hit is the audited record; no published erratum or equivalent correction was located.

Reasoning: Equivalent language such as time-varying coupling work or parameter-work was included in the search scope.

### broader_coverage

Searches: Cortés-Poza 2026 Journal of Mathematical Biology full article webpage; Public implementation at commit 2b53a08fe096394496b482cecef39b695b500ed7

Evidence: The paper supplies the adaptive law and fixed-G theorem but does not include the missing conductance-work term in the cited full-model balance.

Reasoning: Generic Lyapunov theory does not by itself publish this model-specific correction.

### exact_database_or_table

Searches: Search for the nominal numerical state G=0.01794 and positive energy derivative with the source model

Evidence: No prior exact counterexample record was found.

Reasoning: The key claim is a symbolic identity and explicit state, not a database fact.

### claim_vs_prior_implication

Searches: Direct comparison of the source's fixed-conductance theorem, adaptive conductance equation, and later energy-rate formula

Evidence: The fixed-G theorem remains valid; extending its derivative identity to evolving G without an extra chain-rule term is not justified.

Reasoning: The audited correction follows mathematically from the source equations but is not stated by the source and changes the interpretation of full-model dissipativity.

### Source inspections

- **A hybrid mathematical framework for morphogenesis and regeneration** — https://doi.org/10.1007/s00285-026-02459-2
  - Trigger: Direct source whose full-model energy balance is corrected
  - Material read: Accessible full article webpage: adaptive conductance definition, fixed-conductance Lyapunov result, Eq. 39 energy-rate discussion, and later adaptive-G energy discussion
  - Method: full-text web inspection
  - Assessment: SOURCE_CONTAINS_OMISSION
  - Evidence: The displayed full-model derivative omits the conductance-work chain-rule term while G is allowed to evolve.
- **bioelectricity public implementation** — https://github.com/YuririaCP/bioelectricity/tree/2b53a08fe096394496b482cecef39b695b500ed7
  - Trigger: Parameterization and sigmoid/conductance implementation
  - Material read: Repository state identified by the record and compared with the explicit analytic state
  - Method: source-code comparison
  - Assessment: CONSISTENT
  - Evidence: Nominal parameters used by the counterexample match the inspected package statement.
- **Exact conductance-work correction to an adaptive bioelectric Lyapunov balance** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-adaptive-conductance-energy-work-term--c0e67940f3c0
  - Trigger: Exact published-results hit
  - Material read: Title and summary
  - Method: semantic published-results search
  - Assessment: SELF_MATCH
  - Evidence: Exact same correction.

Originality residual risks:
- A contemporaneous erratum or unindexed correction could exist; none was found in the current searches.

## Value

**PASS** — Correcting a published full-system energy identity materially changes what is structurally certified about dissipativity. The explicit stationary-voltage counterexample shows that adaptive coupling alone can inject energy and identifies the precise work term any full-model Lyapunov argument must control. This is a motivated model-level correction, not an arbitrary algebra exercise.

Residual risks:
- The correction does not show that nominal published trajectories actually increase this energy, and it does not settle existence of another Lyapunov functional.

## Scientific limitations

- The fixed-conductance Lyapunov theorem is not challenged.
- The result does not rule out a different composite Lyapunov function or cover discrete hybrid events.

## Disposition

**PASSED**

This audit is not peer review or external certification.
