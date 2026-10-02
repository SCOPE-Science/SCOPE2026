# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-f27e4f47727b`

## Correctness — PASS

The determinant-trace obstruction follows directly from the actual eight-dimensional model. The primary preprint's equations show the feed-forward ordering, so the Jacobian is block lower triangular with four \(2\times2\) diagonal blocks. At positive biomass in reactor one, the equilibrium relation gives \(\mu=\alpha D_1\), hence positive determinant forces \(\mu'>0\) and strictly negative trace. At positive biomass in reactor two, the balance \(0=\alpha D_2(x_0-x)+\mu x\) gives \(r=x_0/x\in[0,1]\), \(\delta=\alpha D_2r\), \(q=-k\mu'x\), and exactly \(\operatorname{tr}=q-D_2-\delta\), \(\det=D_2(\delta-\alpha q)\). Thus \(\det>0\) implies \(q<D_2r\) and \(\operatorname{tr}< -D_2(1-r+\alpha r)<0\); conversely trace zero gives a strictly negative determinant. Zero-biomass blocks are triangular. Therefore no diagonal block, and hence no full Jacobian, can carry a nonzero purely imaginary pair.

### Correctness sources

- Hmidhi–Fekih-Salem, arXiv:2604.18903, model equations, Table 3, Proposition 5 and Remark 1
- assigned RESULT.md
- independent symbolic determinant/trace reconstruction

### Correctness risks

- This excludes local Hopf bifurcation from equilibria only; it does not exclude globally created periodic orbits.

## Originality — PASS

The 2026 primary preprint explicitly retains a separate trace condition for the relevant coexistence equilibria and states that locating Hopf bifurcations and limit cycles remains open. Fresh exact-title, model-specific and determinant/trace searches found no prior statement that positive determinant automatically forces negative trace in this distinct-removal serial AM2 system. The 2025 equal-removal-rate serial analysis concerns the reducible special case and does not cover this identity.

### equivalent_formulations

Searches:
- exact search for serial AM2 distinct removal no-Hopf theorem
- determinant-positive trace-negative search for the second-reactor block
- semantic search for the trace-indeterminate equilibria

Evidence:
- The audited record was the only exact published-finding match located.

Reasoning:
Equivalent formulations as absence of nonzero purely imaginary eigenpairs and redundancy of the source trace condition were checked.

### broader_coverage

Searches:
- Hmidhi–Fekih-Salem arXiv:2604.18903
- 2025 equal-removal serial AM2 analysis
- related chemostat Hopf literature

Evidence:
- The 2026 source leaves the Hopf question open; the 2025 work treats equal removal rates and a reducible setting; structurally different chemostats may have Hopf bifurcations.

Reasoning:
None of these broader sources implies the distinct-rate determinant-trace identity.

### exact_database_or_table

Searches:
- equilibrium/stability tables in the source paper

Evidence:
- Table 3 and Proposition 5 retain both determinant and trace conditions rather than tabulating the audited simplification.

Reasoning:
The source table is evidence that the implication was not already encoded there.

### claim_vs_prior_implication

Searches:
- comparison of source Remark 1 with the audited equilibrium-balance identity

Evidence:
- Remark 1 says determinant can be positive while trace sign appears undetermined; the audited algebra shows this regime cannot occur in the stated model.

Reasoning:
The new implication closes rather than restates the prior analysis.

### source_inspections
- **AM2 model with a series configuration of interconnected chemostats and distinct removal rates** — https://arxiv.org/abs/2604.18903. Trigger: Exact source model and stated open Hopf/stability case. Material read: Full accessible HTML through the model equations, assumptions, Table 3, Proposition 5, Remark 1, and conclusion. Method: Primary full-text equation and stability-condition inspection. Assessment: The source leaves the trace sign/Hopf question open and provides the equations from which the new identity is derived. Evidence: Remark 1 explicitly says positive determinant can coexist with apparently undetermined trace sign; the conclusion lists Hopf/limit cycles as open.
- **Analysis of Anaerobic Digestion Model With Two Serial Interconnected Chemostats** — https://doi.org/10.1007/s11538-025-01475-5. Trigger: Closest prior serial-AM2 analysis. Material read: Abstract and bibliographic scope. Method: Primary-literature scope comparison. Assessment: Treats the earlier equal-rate serial setting; it does not cover the distinct-rate eight-dimensional obstruction. Evidence: The 2026 paper describes it as the particular identical-dilution-rate case.
- **Assigned RESULT.md** — assigned record RESULT.md. Trigger: Complete no-Hopf derivation. Material read: Complete file. Method: Independent algebraic reconstruction against the primary ODEs. Assessment: The block formulas and inequalities are correct. Evidence: Substitution into the second-reactor \(2\times2\) block gives exactly the stated trace and determinant.

### checked_sources

- https://arxiv.org/abs/2604.18903
- https://doi.org/10.1007/s11538-025-01475-5
- assigned RESULT.md
- fresh model-specific semantic search

### residual_risks

- The result is source-specific and does not imply no-Hopf behavior for chemostat models with feedback, flocculation, delay, or other non-triangular couplings.

## Scientific value — PASS

The theorem closes the Hopf part of an explicit open problem in the source model and removes a redundant local-stability condition for the difficult coexistence equilibria. The determinant-trace identity is a source-specific structural lemma with direct use in the model's stability classification.

### Value sources

- arXiv:2604.18903, Proposition 5, Remark 1 and conclusion
- the audited second-reactor balance identity

### Value risks

- No claim of global convergence or exclusion of nonlocal periodic orbits is made.

## Limitations

- The theorem is local to equilibrium bifurcation and does not exclude globally generated periodic orbits.
- It depends on the feed-forward serial AM2 architecture.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
