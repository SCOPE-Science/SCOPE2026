# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-defb12bcd300`

## Correctness — PASS

Conditioning on \(s=\operatorname{rank}U\) gives the displayed Gaussian-binomial likelihood for each target rank. The likelihood strictly decreases with target rank. Full-row-rank targets have mass \(p_{k,r}(q)q^{-kn}\). For every deficient target, the rank-\(k-1\) contribution alone has likelihood ratio at least \(q^{n-r}p_{k-1,r}(q)>1\), including \(k=1\). Hence the deficit set against uniformity is exactly the full-row-rank stratum, whose total uniform mass is \(p_{k,n}(q)\), proving the exact TV identity. The row/column privacy identity follows from translation invariance under uniform input. The lower and upper rank-surplus bounds are valid, so for fixed field size leakage vanishes exactly when \(r-k	o\infty\). Exhaustive small-field enumeration in the assigned verifier reproduces six exact cases but is only corroboration.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_exact_tv.py
- Cohen--D'Oliveira--Sprintson arXiv:2609.18876, Theorem 3

### Correctness risks

- The result assumes independent uniform factors and uniform inputs.
- No analogous exact law is claimed for rank-ball masks or nonuniform factors.

## Originality — PASS

The primary masking paper proves only the coupling upper bound \(d_{TV}\le1-p_{k,r}(q)\), using the full-row-rank event of the row-restricted factor. It does not identify the sign of every pointwise likelihood deviation or the exact multiplicative factor \(p_{k,n}(q)\), and therefore does not imply the iff rank-surplus threshold. Fresh semantic searches found no earlier privacy theorem with this exact formula. Generic finite-field factorization counts are prior ingredients, but the exact masking leakage identity and threshold were not located.

### equivalent_formulations

Searches:
- Resultary search for exact total variation of \(UV\) and low-rank factor masks
- rank-conditioned random-matrix product likelihood search

Evidence:
- The exact audited theorem was the only matching published finding returned.
- The distribution can equivalently be described by target-rank likelihoods, which the proof computes explicitly.

Reasoning:
Equivalent formulations through random matrix products and row-individual-security leakage were both checked.

### broader_coverage

Searches:
- Cohen--D'Oliveira--Sprintson Theorem 3
- rectangular low-rank masking privacy records

Evidence:
- The primary theorem gives only \(1-p_{k,r}\) and then \(q^{k-r}/(q-1)\) as upper bounds.
- Other masking records concern maximal correlation or differential privacy rather than this exact TV law.

Reasoning:
Existing broader privacy results do not imply equality or the exact threshold.

### exact_database_or_table

Searches:
- finite-field matrix-factorization rank-count literature
- current published masking records

Evidence:
- Standard rank/factorization counts can recover ingredients in the likelihood formula.
- No inspected database/table states \(p_{k,n}(1-p_{k,r})\) as the protocol leakage or its iff asymptotic threshold.

Reasoning:
This is not accepted as novel merely because of a new count; novelty is in the exact privacy statement and its consequences.

### claim_vs_prior_implication

Searches:
- direct implication check from Theorem 3 of arXiv:2609.18876

Evidence:
- A coupling upper bound cannot determine which points are overweight or underweight.
- The audited rank-likelihood monotonicity supplies the missing converse and exact deficit mass.

Reasoning:
The exact TV equality is strictly stronger than the cited source theorem and is not mechanically implied by it.

### source_inspections

- **Low-Rank Masking for Single-Server Matrix Multiplication** — https://arxiv.org/abs/2609.18876. Trigger: Primary source of the Low-Rank Factors individual-security bound. Material read: Complete five-page paper, including Theorem 3 and its proof. Method: Full theorem/proof comparison. Assessment: NOT COVERING the exact TV identity. Evidence: The proof conditions on full row rank only to construct an upper-bound coupling and states \(d_{TV}\le1-p_{k,r}\).
- **Assigned exact-TV verifier** — artifacts/verify_exact_tv.py. Trigger: Package finite checks. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct exhaustive corroboration for six small cases. Evidence: The script exactly matches \(p_{k,n}(1-p_{k,r})\) in all tested cases.

### checked_sources

- https://arxiv.org/abs/2609.18876
- artifacts/verify_exact_tv.py
- Resultary exact-TV and masking searches

### residual_risks

- Generic matrix-product factorization formulas may be folklore under different notation; no source was found connecting them to this exact masking leakage theorem.

## Scientific value — PASS

The theorem turns an approximate individual-security guarantee into an exact finite-parameter law and matching converse. The resulting iff condition \(r-k	o\infty\) identifies the true design threshold for a canonical masking method, which is a natural protocol parameter boundary rather than a routine recomputation.

### Value sources

- Cohen--D'Oliveira--Sprintson individual-security theorem
- audited exact likelihood analysis

### Value risks

- The theorem is confined to the uniform factor sampler and total variation.

## Limitations

- Uniform independent factors and uniform inputs are required.
- No exact formula is claimed for rank-ball masks, correlated inputs, or other privacy metrics.
- Originality is best-of-knowledge with generic factorization-count folklore as residual risk.

## Disposition

**PASSED**
