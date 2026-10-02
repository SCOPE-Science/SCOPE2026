# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-b8f8144d73bc`

## Correctness — PASS

The exact Casoratian was independently regenerated from the recurrence and checked through index 69. Bachmann's full 17-page primary paper was inspected and confirms the recurrence, the positive double-binomial formula, and the limit \(C_n/A_n	o\zeta(3)/7\). The dominant double sum has a unique strictly concave saddle at \((3/4,3/4)\), giving \(A_n=(2\sqrt6/(3\pi^2))64^n n^{-2}(1-29/(48n)+O(n^{-2}))\); once the standard lattice-Laplace expansion supplies an inverse-power expansion, substitution into the exact recurrence fixes the first correction. Combining it with the Stirling expansion of the Casoratian gives the \(1-35/(48n)\) quotient-error correction, and summing the positive increments yields the exact positive series and linear-form asymptotic.

### Correctness sources

- assigned RESULT.md
- independent exact recurrence/Casoratian computation
- Bachmann, arXiv:2609.18271 full text
- current earlier same-day leading-constant Resultary theorem

### Correctness risks

- No irrationality-measure improvement follows.
- The saddle computation uses standard multivariate Laplace asymptotics rather than a formal proof certificate.

## Originality — PASS

A same-day published theorem already gives the leading equivalent \((\sqrt2\pi^3/84)64^{-n}\), so that leading constant is not originality-bearing in the final assessment. The audited final claim survives because it additionally gives the explicit \(1/n\) correction, the two-term linear-form asymptotic, and the exact positive series whose partial sums are \(7C_n/A_n\). Fresh searches using the correction coefficients \(29/48\) and \(35/48\), the exact series, and the linear-form formulation returned no covering theorem.

### equivalent_formulations

Searches:
- Resultary searches for AESZ-28, the exact correction coefficients, the linear form, and the positive zeta series

Evidence:
- A same-day record covers only the leading equivalent and leading \(A_n\) asymptotic.
- No searched record contains the audited first corrections or exact positive series.

Reasoning:
Equivalent formulations through the quotient error, the Casoratian increment tail, and the linear form were compared.

### broader_coverage

Searches:
- Bachmann arXiv:2609.18271 full text
- same-day `SCOPE-sharp-aesz28-apery-limit-convergence--fdd653cbbbb0`

Evidence:
- Bachmann proves the qualitative Apéry limit and exact recurrence framework.
- The same-day record proves the leading error constant but stops before the audited \(1/n\) corrections and exact zeta series.

Reasoning:
The final two-term asymptotic is strictly stronger than the leading equivalent.

### exact_database_or_table

Searches:
- Calabi–Yau AESZ database entry 28
- current Resultary Apéry-limit findings

Evidence:
- The database records the operator/solution data but not the audited asymptotic corrections.

Reasoning:
No database table implies the new coefficients.

### claim_vs_prior_implication

Searches:
- statement comparison with the same-day leading-constant theorem

Evidence:
- That theorem's proof uses the same saddle and Casoratian but does not compute the first correction or state the exact positive telescoping series.

Reasoning:
The leading theorem is partial current coverage, not full implication of the final claim.

### source_inspections

- **A q-recurrence for a finite Apéry limit** — https://arxiv.org/abs/2609.18271. Trigger: Primary source proving the underlying Apéry limit. Material read: Full 17-page primary paper through the recurrence construction, limit proof, arithmetic endpoint results, and references. Method: Primary full-text theorem search and comparison. Assessment: Not covering the sharp two-term convergence law. Evidence: The paper proves \(C_n/A_n	o\zeta(3)/7\) but does not give the audited \(64^{-n}\) first-correction expansion.
- **Sharp exponential constant for the AESZ 28 Apéry limit** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-sharp-aesz28-apery-limit-convergence--fdd653cbbbb0. Trigger: Near-exact same-day published match. Material read: Complete RESULT.md. Method: Full theorem-and-proof implication comparison. Assessment: PARTIAL COVERAGE only. Evidence: It proves the leading equivalent and leading \(A_n\) asymptotic, but not the \(1/n\) corrections or exact positive series.

### checked_sources

- Bachmann arXiv:2609.18271 full text
- same-day leading-constant Resultary theorem
- current Resultary correction-coefficient searches
- assigned RESULT.md and verifier

### residual_risks

- Bachmann cites a Sato–Tasaka manuscript in preparation; its full contents remain unavailable and are the strongest residual originality risk.

## Scientific value — PASS

The surviving contribution is a sharp two-term quantitative law for a natural new Apéry limit, together with an exact positive series representation tied to the rational approximants. Exact first corrections and the linear-form scale are natural invariants of this recurrence and materially sharpen the currently published leading equivalent.

### Value sources

- Bachmann's AESZ-28 Apéry limit
- same-day leading-constant theorem
- audited first-correction theorem

### Value risks

- The result is specific to AESZ-28 and does not by itself improve irrationality measures.

## Limitations

- The leading \(64^{-n}\) constant is already covered by a same-day published result; originality rests on the first corrections, linear form, and exact series.
- The inaccessible Sato–Tasaka manuscript remains a residual risk.
- No irrationality-measure claim is made.

## Disposition

**PASSED**
