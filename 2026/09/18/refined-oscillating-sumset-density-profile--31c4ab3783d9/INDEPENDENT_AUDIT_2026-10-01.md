# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-31c4ab3783d9`

## Correctness — PASS

The refinement follows from exact counting rather than a finite experiment. Leonetti's construction already places the mixed and new-new sums inside the union of the \(r\) one-coordinate-deleted CRT constraint sets. A residue lies in that union exactly when at least \(r-1\) coordinates satisfy their local conditions, so one period has density \(\prod_i\eta_i+\sum_j(1-\eta_j)\prod_{i
e j}\eta_i\). Taking \(\eta_i	o2\delta\), together with the vanishing endpoint-period error, gives \(r(2\delta)^{r-1}-(r-1)(2\delta)^r\). Substituting \(\delta=lpha^{1/r}\) and optimizing \(ar+L/r+\log r\) at the displayed quadratic critical point gives the stated small-\(lpha\) upper envelope; Kneser's lower bound \(2lpha\) then forces logarithmic exponent one. Independent CRT enumeration reproduced the package's 315-residue sample exactly.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_profile.py
- artifacts/verify-output.txt
- Leonetti arXiv:2609.20206 scope information
- Kneser's lower bound

### Correctness risks

- The result is an upper envelope, not the true asymptotic size of \(\Lambda(lpha)/lpha\).

## Originality — PASS

Fresh semantic searches in the current published corpus returned the audited theorem as the only exact density-profile match. The motivating Leonetti result is described as using the weaker separate-union bound; the audited theorem gains a strict fixed-parameter improvement by exact CRT union counting and then extracts a new optimized profile exponent. No located current theorem or database entry supplies that exact coefficient or the logarithmic-profile conclusion.

### equivalent_formulations

Searches:
- Resultary: oscillating sumset density lower upper profile Leonetti exact CRT union
- Resultary: Lambda alpha sumset lower density upper density one logarithmic exponent one

Evidence:
- The audited record was the only exact theorem-level match among the returned published findings.

Reasoning:
The search included the extremal-profile formulation and the original-construction formulation.

### broader_coverage

Searches:
- Leonetti arXiv:2609.20206
- Bienvenu arXiv:2502.09438
- Hegyvári–Hennecart–Pach arXiv:1902.02512

Evidence:
- The accessible source descriptions concern the original Ruzsa density question and broader simultaneous-density realizability, not an exact-union coefficient matching the audited formula.

Reasoning:
The broader density-realizability literature does not mechanically imply the optimized small-density envelope.

### exact_database_or_table

Searches:
- current Resultary published findings and density-sequence databases

Evidence:
- No exact table of \(\Lambda(lpha)\) or the refined CRT coefficient was located.

Reasoning:
The statement is an infinite constructive bound, not extraction from a finite table.

### claim_vs_prior_implication

Searches:
- comparison of Leonetti's stated bound with the exact CRT union

Evidence:
- The audited coefficient is strictly smaller for every admissible positive parameter because overlap among the union pieces is counted exactly.

Reasoning:
The improved profile is not a corollary of merely knowing the earlier looser upper bound; it uses additional overlap structure already present in the construction.

### source_inspections
- **On a question of Ruzsa about densities of sumsets** — https://arxiv.org/abs/2609.20206. Trigger: Primary construction being refined. Material read: Accessible abstract/metadata and the theorem statement as reproduced in the audited package; full arXiv/OA text was not obtainable in this run and the authorized download route was unavailable. Method: Scope and theorem-bound comparison; no whole-document exclusion was inferred from unavailable text. Assessment: The accessible evidence is consistent with the weaker published bound but leaves an access-related originality risk. Evidence: The audited proof identifies overlap among the exact CRT sets rather than changing the construction.
- **Realisability of simultaneous density constraints for sets of integers** — https://arxiv.org/abs/2502.09438. Trigger: Closest broad density-profile literature named by the package. Material read: Accessible bibliographic/scope information. Method: Problem-scope comparison. Assessment: Relevant broader context; no decisive implication of the audited asymptotic profile was located. Evidence: Its scope is simultaneous realizability of density data rather than this exact extremal upper envelope.
- **Assigned profile verifier** — artifacts/verify_profile.py. Trigger: Exact CRT count and asymptotic bookkeeping. Material read: Complete source and saved output. Method: Line-by-line inspection plus independent enumeration. Assessment: Correctly verifies the finite combinatorial identity used by the proof. Evidence: The direct and formula counts both equal 315 for the sample period.

### checked_sources

- https://arxiv.org/abs/2609.20206
- https://arxiv.org/abs/2502.09438
- https://arxiv.org/abs/1902.02512
- artifacts/verify_profile.py
- current Resultary density-profile searches

### residual_risks

- Leonetti cites an unpublished Ruzsa manuscript on the same question; no public identifier or full text was available.
- The motivating preprint is recent and its full text could not be inspected through the attempted access routes in this run.

## Scientific value — PASS

The theorem strictly improves a recent quantitative construction for every admissible parameter pair and turns the improvement into a natural extremal-profile statement. Pinning down the exact logarithmic exponent of the least lower double-sumset density is a meaningful boundary result even though the multiplicative gap remains open.

### Value sources

- Leonetti's oscillating construction
- Kneser's universal lower bound
- audited exact CRT overlap count

### Value risks

- The result does not determine the sharp multiplicative asymptotic.

## Limitations

- The true order of \(\Lambda(lpha)/lpha\) remains open.
- An unpublished Ruzsa manuscript is a genuine inaccessible-source risk.
- Originality is best-of-knowledge because the motivating preprint is recent and full primary text was unavailable in this run.

## Disposition

**PASSED**
