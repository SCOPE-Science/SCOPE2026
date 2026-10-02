# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-c45dc5ae3e3c`

## Correctness — PASS

For negative \(t\), the Chebyshev substitution \(1-2t=\cosh u\), \(y=nu/2\) turns the only potentially negative range exactly into \(\delta-\sinh^2(y/n)(1-\sinh^{2(d-1)}y)\), so the displayed maximum is both necessary and sufficient. The logarithmic-derivative comparison gives a unique interior maximizer. Monotonicity in odd multiplicity, convergence to the source floor, the \(\beta_d/n^2\) bound and the \(\kappa_d\) limit follow from elementary monotonicity, convexity and uniform convergence. Because only the additive constant is changed, the source certificate degree is unchanged. The inspected verifier reproduces the constants but is not used as the proof.

### Correctness sources

- assigned RESULT.md and artifacts/verify_floor.py
- Henrion–Safey El Din arXiv:2609.20544

### Correctness risks

- Sharpness is only within the source's Chebyshev ansatz, not among all Positivstellensatz certificates.

## Originality — PASS

The source paper introduces the Chebyshev desingularization and an \(O(r^{-2})\) theorem but, in the inspected public descriptions and current searches, no source states the exact multiplicity-dependent minimum floor, its worst-multiplicity envelope, or the \(\beta_d\) and \(\kappa_d\) refinements. Resultary returns only the audited record for this exact claim.

### equivalent_formulations

Searches:
- Resultary query for multiplicity-sharp Chebyshev moment-SOS floor
- web search for arXiv:2609.20544 and Chebyshev boundary degeneracy

Evidence:
- No matching independent theorem was located.

Reasoning:
Equivalent formulations as a minimum additive floor for the fixed Chebyshev ansatz and as the induced proof constant were searched.

### broader_coverage

Searches:
- Henrion–Safey El Din universal univariate \(O(r^{-2})\) theorem
- earlier univariate quadratic-module literature

Evidence:
- The broader theorem fixes the rate exponent and uses a multiplicity-blind floor.

Reasoning:
A universal rate theorem does not imply the exact ansatz-level optimal floor for each finite odd multiplicity.

### exact_database_or_table

Searches:
- exact constants \(\delta_{n,d}\), \(\beta_d\), \(\kappa_d\)

Evidence:
- No prior table or database of these constants was located.

Reasoning:
The constants arise from a new one-dimensional optimization, not a known numerical table.

### claim_vs_prior_implication

Searches:
- implication comparison with the source floor \(\varepsilon_n\)

Evidence:
- The source floor is an upper envelope; the audited argument proves strictly smaller exact floors for each fixed finite odd multiplicity.

Reasoning:
The source bound does not mechanically imply the sharp finite-multiplicity value.

### source_inspections
- **Convergence rate of the moment-SOS hierarchy for univariate polynomial optimization** — https://arxiv.org/abs/2609.20544. Trigger: Direct source of the Chebyshev recovery primitive. Material read: Public abstract and detailed secondary page describing the Chebyshev construction; direct arXiv full text was unavailable through the web route used. Method: Source-scope and formula comparison against the assigned proof. Assessment: Supplies the universal rate mechanism, not the audited exact floor refinement. Evidence: The public abstract says boundary degeneracies affect constants but gives no multiplicity-sharp constant.
- **Assigned multiplicity verifier** — artifacts/verify_floor.py. Trigger: Finite-n and asymptotic constants. Material read: Complete source plus recorded output. Method: Line-by-line inspection; constants cross-checked against the analytic formulas. Assessment: Corroborates the exact one-variable optimization and asymptotic constants. Evidence: The computed \(\kappa_d\), \(\beta_d\), finite floors and minimizing residuals agree with RESULT.md.

### checked_sources

- arXiv:2609.20544
- Resultary semantic search
- assigned RESULT.md and verifier

### residual_risks

- The source is very recent, so simultaneous unindexed refinements remain possible.
- Full primary source text was not retrievable in this run.

## Scientific value — PASS

The result gives a sharp method-level constant law for a natural multiplicity parameter that the source theorem explicitly leaves inside an opaque constant. It yields strict improvements without increasing degree and quantifies how low multiplicity changes the certificate cost.

### Value sources

- source moment-SOS theorem
- audited exact Chebyshev floor

### Value risks

- The global \(r^{-2}\) exponent is unchanged.

## Limitations

- Optimality is ansatz-specific.
- Propagated moment-SOS constants remain proof-dependent.
- No multivariate extension is claimed.

## Disposition

**PASSED**
