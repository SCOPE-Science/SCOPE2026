# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-b46608125d84`

## Correctness — PASS

The principal counterexamples and closure statement reconstruct directly. A bounded rational function on \((-\infty,0]\) has a finite limit at \(-\infty\), and uniform limits preserve that property. The compactifying change \(y=-x/(1-x)\) converts continuous functions with a finite endpoint limit to \(C([0,1])\), so Weierstrass approximation gives simultaneous convergence for any finite family using the common denominator \((1-x)^n\). For \(e^{ix}\), two subsequences tending to target values \(1\) and \(-1\) force uniform error at least one for every rational approximant, attained by zero. For \(g(z)=e^z\sin(e^{-z})\), the \(2n+2\) alternating samples at \(x_k=-\log((k+1/2)\pi)\) force at least \(2n+1\) zeros of the real part of a hypothetical better type-\((n,n)\) approximant; its real-part numerator has degree at most \(2n\), a contradiction. The slit plane is simply connected whereas the ordinary exterior disk is not, so the criticized conformal normalization is also incompatible with the stated domain.

### Correctness sources

- assigned RESULT.md
- Al-Mohy, Mathematics 13 (2025), 3985
- elementary compactification/zero-count reconstruction

### Correctness risks

- The argument concerns uniform rational approximation on the whole negative ray; it does not dispute the paper's numerical tables for the specific phi-functions.

## Originality — PASS

Fresh searches located the 2025 source article and the later scalar phi-function approximation result, but no correction, erratum, or prior source giving these two explicit entire counterexamples or the stated finite-limit algebraic lower bound. The elementary compactification closure characterization may be classical and is not treated as the originality-bearing part; the substantive new content is the concrete failure of the published no-assumptions geometric theorem and the quantitative endpoint counterexample.

### equivalent_formulations

Searches:
- exact search for \(e^{ix}\) negative-ray rational error one
- search for \(e^z\sin(e^{-z})\) rational approximation lower bound
- search for corrections to Al-Mohy Mathematics 13 (2025) 3985

Evidence:
- No prior correction or matching explicit counterexample was located.

Reasoning:
Equivalent formulations in terms of best type-\((n,n)\) uniform error and common-denominator geometric approximation were checked.

### broader_coverage

Searches:
- Al-Mohy 2025 shared-pole theorem
- Schmelzer arXiv:2609.14489 on fixed phi-functions

Evidence:
- Al-Mohy is the theorem being corrected; the later scalar result concerns the favorable phi-functions rather than arbitrary analytic functions sharing a denominator.

Reasoning:
Neither supplies the audited obstruction as prior coverage.

### exact_database_or_table

Searches:
- rational-approximation tables for the two entire examples

Evidence:
- No relevant exact table or database entry was located.

Reasoning:
The claims are theorem/counterexample statements rather than table lookups.

### claim_vs_prior_implication

Searches:
- comparison with the published no-assumptions theorem and scalar Halphen-rate results

Evidence:
- The audited examples contradict the general hypothesis level while leaving special phi-function rates compatible.

Reasoning:
The prior theorems do not imply the contradiction; they motivate it.

### source_inspections
- **Shared-Pole Carathéodory–Fejér Approximations for Linear Combinations of phi-Functions** — https://doi.org/10.3390/math13243985. Trigger: Published theorem whose general hypothesis level is tested. Material read: Open-access article material including abstract, method/conclusion, and the theorem context used by the record. Method: Primary-source statement and domain comparison. Assessment: The article claims a shared-pole framework/geometric behavior on the negative axis; no correction addressing the audited obstructions was found. Evidence: The paper is the direct target of the no-assumptions critique.
- **The `1/9'-problem for the phi-functions** — https://arxiv.org/abs/2609.14489. Trigger: Closest newer scalar best-approximation result for the intended special functions. Material read: Current abstract/scope in search results. Method: Primary-source scope comparison. Assessment: Special-function scalar rates do not cover arbitrary analytic families with one shared denominator. Evidence: The target class is much narrower than the theorem disproved here.
- **Assigned RESULT.md** — assigned record RESULT.md. Trigger: Contains complete elementary proofs of both counterexamples. Material read: Complete file. Method: Independent line-by-line mathematical reconstruction. Assessment: Both lower-bound arguments and the compactification closure theorem check directly. Evidence: The degree count for the real part is at most \(2n\), while the alternating sample argument forces \(2n+1\) zeros.

### checked_sources

- https://doi.org/10.3390/math13243985
- https://arxiv.org/abs/2609.14489
- assigned RESULT.md
- fresh semantic and correction searches

### residual_risks

- The qualitative closure characterization itself is elementary and may be classical; the audit does not claim priority for that isolated lemma.
- A later correction not indexed by the searched sources remains a residual possibility.

## Scientific value — PASS

The result identifies a real hypothesis failure in a recent general approximation theorem, gives exact and quantitative entire-function counterexamples, and separates qualitative endpoint compactness from geometric convergence. That materially clarifies what a repaired shared-denominator theorem must assume.

### Value sources

- Al-Mohy 2025 shared-pole theorem
- the exact \(e^{ix}\) obstruction
- the finite-limit \(\Omega(1/n)\) obstruction

### Value risks

- It does not determine the optimal simultaneous common-pole rate for the intended phi-functions.

## Limitations

- The elementary closure theorem is not claimed as novel by itself.
- The result does not refute the reported numerical approximation performance for the phi-functions.
- Originality is best-of-knowledge and no published correction was found in the fresh search.

## Disposition

**PASSED**
