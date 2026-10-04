---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The theorem is proved symbolically in `RESULT.md`. The accompanying `verifier.py` is a finite regression checker.

It enumerates every connected threshold creation string of orders \(2\) through \(10\), constructs the graph directly from the creation rule, and for every positive integer \(k\) up to the order tests every subset \(S\) against the definition
\[
|N(v)\cap S|\ge k\qquad\text{for every vertex }v.
\]
It separately evaluates the claimed criterion
\[
|S\cap B_p|\ge k\quad\text{and}\quad |S|\ge k+1,
\]
compares the complete size histogram with the closed binomial formula, and tests that inclusion-minimal feasible sets are exactly those of size \(k+1\).

Exact replay output:

`VERIFY_OK graphs=511 subset_k_checks=3378744 coefficient_checks=47102 minimal_checks=344405 max_order=10`

The computation checks finite instances only. It does not certify the infinite theorem, which rests on the universal-neighborhood proof in `RESULT.md`. No external solver or unverified certificate is used.
