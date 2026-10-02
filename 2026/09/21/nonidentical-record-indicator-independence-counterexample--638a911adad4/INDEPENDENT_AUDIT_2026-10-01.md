# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260921-638a911adad4`

## Correctness — PASS

The counterexample is exact. For independent \(X_1,X_3\sim U(0,1)\) and \(X_2\sim U(0,a)\), direct integration gives the stated marginals and the joint event \(X_1<X_2<X_3\). Subtraction yields covariance \(a(a-1)(a-3)/12\) for \(0<a\le1\) and \((1-a)/(6a^2)\) for \(a\ge1\), so dependence is positive below one and negative above one. In independent coordinate products the joint and marginal event probabilities raise to the \(d\)th power, preserving the sign of dependence. The source preprint's claimed factorization fails because the block record events share random boundary observations; the paper's displayed proof indeed factors such events as if they were independent.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_exact.py
- Lo–Babou arXiv:2602.20416 full text

### Correctness risks

- The result refutes a universal non-iid claim but does not characterize all non-identical sequences with independent record indicators.

## Originality — PASS

The February 2026 preprint continues to state universal independence for independent, non-identically distributed observations, and its proof contains the shared-boundary factorization fault addressed by the example. Fresh searches by arXiv identifier, title, counterexample, correction, and record-indicator terminology found no public erratum or earlier exact counterexample. Classical iid and \(F^\alpha\) results are narrower valid subclasses and do not cover the correction.

### equivalent_formulations

Searches:
- web query: arXiv:2602.20416 counterexample correction record indicators
- web query: "Independence of the indicator functions of record values for Multivariate independent data" correction
- Resultary query: nonidentical independent observations record indicators counterexample

Evidence:
- The primary preprint still states the universal non-iid independence claim.
- No located correction or prior exact one-parameter sign-changing counterexample was found.

Reasoning:
The distinction between iid, \(F^\alpha\)-schemes, and arbitrary independent non-identical observations was kept explicit.

### broader_coverage

Searches:
- classical record-indicator independence literature
- Nevzorov \(F^\alpha\) schemes
- Lo–Babou 2026

Evidence:
- Classical iid and structured \(F^\alpha\) theorems are compatible with the counterexample because the scale family is outside those assumptions except at \(a=1\).

Reasoning:
Valid structured independence theorems do not imply the false universal extension.

### exact_database_or_table

Searches:
- current Resultary record-theory findings
- arXiv-identifier searches

Evidence:
- No exact correction database entry or later Resultary record covering this counterexample was found.

Reasoning:
The claim is an analytic counterexample, not a finite table result.

### claim_vs_prior_implication

Searches:
- line-by-line implication check against the source's factorization argument

Evidence:
- The two record indicators depend on the common intermediate observation; the source's factorization of separated index blocks does not justify independence when the defining events share random endpoints.

Reasoning:
The explicit family directly falsifies the theorem rather than merely challenging its proof.

### source_inspections

- **Independence of the indicator functions of record values for Multivariate independent data** — https://arxiv.org/abs/2602.20416. Trigger: Primary source containing the disputed universal theorem. Material read: Full accessible arXiv text around the theorem and the factorization step used in the independence proof. Method: Primary proof inspection plus direct counterexample substitution. Assessment: The universal theorem is false under its stated non-iid assumptions. Evidence: The source claims independence without identical distributions; the exact three-variable family has nonzero covariance.
- **Assigned exact verifier** — artifacts/verify_exact.py. Trigger: Piecewise covariance and product-extension checks. Material read: Complete source and saved output. Method: Exact rational replay. Assessment: Correct corroboration. Evidence: The verifier reproduces \(5/96\) at \(a=1/2\), zero at \(a=1\), and \(-1/24\) at \(a=2\), and checks the dimension-lift sign.

### checked_sources

- Lo–Babou arXiv:2602.20416 full text
- current Resultary record-theory search
- classical iid and \(F^\alpha\) record literature
- assigned exact verifier

### residual_risks

- A later or poorly indexed correction to the recent preprint could exist; none was located in current searches.

## Scientific value — PASS

A three-observation continuous counterexample directly corrects a stated universal theorem and pinpoints the exact probabilistic error. The sign-changing family and all-dimensional product lift make the failure structural rather than a one-off numerical example.

### Value sources

- disputed 2026 universal theorem
- assigned exact family

### Value risks

- The work does not attempt a replacement characterization of every non-iid independence scheme.

## Limitations

- Classical iid and structured \(F^\alpha\) independence results remain valid.
- The contribution is a correction and counterexample, not a full classification.
- Originality is best-of-knowledge for a recent and still-changing preprint.

## Disposition

**PASSED**
