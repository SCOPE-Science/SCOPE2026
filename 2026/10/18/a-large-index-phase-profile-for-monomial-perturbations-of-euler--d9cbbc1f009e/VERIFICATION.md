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

# Reproducibility and mathematical limits

Run `python check.py` with Python 3, from the folder containing this document, `RESULT.md`, and the script. The script requires only the standard library and prints `CHECKS_PASS` upon successful completion. It evaluates 975 exact coefficient equalities by independently inverting the Euler pentagonal denominator and summing weighted separator-block compositions using partition-coefficient dynamic programming. It also performs 36 numerical root/profile checks at several indices and eight fixed-weight asymptotic comparisons. The script was executed successfully from these actual files.

Proof-level verification is in RESULT.md: the dominant-pole analysis, bivariate implicit derivatives, eta modular formula, positive-root squeeze, and fixed-weight Taylor expansion establish the infinite statements. The code is a finite regression test, **not** an exhaustive or infinite certificate. Large-index results follow in the order of limits first \(n\to\infty\), then \(j\to\infty\). No simultaneous-limit approximation or external audit is established.
