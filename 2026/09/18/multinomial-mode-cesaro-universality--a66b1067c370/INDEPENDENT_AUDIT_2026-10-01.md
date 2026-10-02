# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-a66b1067c370`

## Correctness — PASS

Janson's Jefferson seat-excess limit supplies a bounded limiting displacement law, so weak convergence upgrades to every polynomial moment. Substitution into Elezović's Bernoulli-polynomial coefficient formula gives the all-order Cesàro law. The displayed generating-function cancellation is algebraically correct. The conditional-uniform moment calculation for \(Q_2=c_2+c_1^2/2\) yields the stated dependence on \(A_1\) and \(A_2\); the package's 300000-step computation is only a numerical check, not the proof.

### Correctness sources

- Elezović, arXiv:2609.20229
- Janson, arXiv:1110.6369
- assigned RESULT.md and artifacts/check_low_order.py
- later 2026-09-19 SCOPE derivation of the logarithmic law

### Correctness risks

- The theorem assumes the generic rational-independence regime and asserts Cesàro rather than pointwise convergence.

## Originality — PASS

The all-order logarithmic law is now also stated in a later published SCOPE record, which explicitly treats that component. The audited record is strictly richer: it also gives the polynomial transfer law and an explicit second-order multiplicative coefficient \(\overline Q_2\) whose dependence on \(\sum p_i^{-1}\) and \(\sum p_i^{-2}\) proves the first loss of universality. No inspected source covers that full final package.

### equivalent_formulations

Searches:
- Resultary semantic search for multinomial modal Cesàro laws
- Elezović multinomial mode expansion
- Janson Jefferson seat excess

Evidence:
- A later SCOPE result reproduces the universal logarithmic coefficient law but explicitly does not claim multiplicative-coefficient universality.
- No inspected source states the audited \(Q_2\) formula.

Reasoning:
The final claim includes the joint polynomial transfer and the nonuniversal \(Q_2\) law, not only the log-coefficient theorem.

### broader_coverage

Searches:
- Janson's general divisor-method limit law
- Elezović complete local expansion

Evidence:
- Those two sources provide the probabilistic and asymptotic ingredients separately.

Reasoning:
They do not state the combined \(Q_2\) heterogeneity formula; deriving it requires joint second moments of the seat-excess functional.

### exact_database_or_table

Searches:
- older apportionment moment papers by Schwingenschlögl–Drton and Heinrich–Pukelsheim–Schwingenschlögl

Evidence:
- No exact table/database entry for \(\overline Q_2\) was located in the searches used by this audit.

Reasoning:
This is not a known-table recomputation; it is a derived mixed-moment formula.

### claim_vs_prior_implication

Searches:
- comparison with the 2026-09-19 SCOPE log-coefficient theorem

Evidence:
- That later theorem covers only the universal logarithmic coefficients and explicitly says products require joint moments.

Reasoning:
It does not imply the displayed multiplicative \(Q_2\) formula, so the full audited result is not covered.

### source_inspections
- **Universal Cesàro law for all logarithmic coefficients at multinomial modes** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-multinomial-mode-cesaro-log-coefficients--69879bbdb548. Trigger: Closest published SCOPE overlap. Material read: Complete RESULT.md. Method: Full theorem and limitation comparison. Assessment: Covers the logarithmic component only; it explicitly leaves multiplicative coefficients outside its theorem. Evidence: Its limitation says products of different \(c_j\) require joint moments.
- **Multinomial probabilities near the mode: integer modes and the complete local expansion** — https://arxiv.org/abs/2609.20229. Trigger: Primary fixed-p modal expansion. Material read: Public abstract/metadata; direct arXiv full-text retrieval failed in this run. Method: Primary-source scope comparison. Assessment: Supplies the local coefficient expansion and Jefferson identification, not the audited on-slice joint-moment calculation. Evidence: The abstract advertises the complete Bernoulli-polynomial local expansion.
- **Asymptotic bias of some election methods** — https://arxiv.org/abs/1110.6369. Trigger: Primary Jefferson seat-excess limit law. Material read: Public abstract/metadata. Method: Primary-source scope comparison. Assessment: Supplies the limiting seat-excess law, not the multinomial \(Q_2\) coefficient formula. Evidence: The abstract studies asymptotic distributions and means for divisor methods.

### checked_sources

- later SCOPE logarithmic-law result
- arXiv:2609.20229
- arXiv:1110.6369
- DOI 10.1016/j.spl.2006.04.014
- assigned package

### residual_risks

- Older apportionment joint-moment literature remains the main residual originality risk.
- Primary full texts for Elezović and Janson were not retrievable through the available arXiv route during this run.

## Scientific value — PASS

The theorem resolves a stated on-slice averaging problem, gives an all-orders structural law, and identifies exactly where universality first breaks after exponentiation. The \(Q_2\) term is a motivated diagnostic for the actual modal probability expansion.

### Value sources

- Elezović fixed-p expansion
- Janson apportionment law
- audited \(Q_2\) formula

### Value risks

- The result is restricted to generic fixed probability vectors.

## Limitations

- The logarithmic component is currently duplicated by a later published record; acceptance rests on the richer full final claim, especially the \(Q_2\) heterogeneity statement.
- Older apportionment moment literature remains residual risk.
- The numerical checker is corroborative only.

## Disposition

**PASSED**
