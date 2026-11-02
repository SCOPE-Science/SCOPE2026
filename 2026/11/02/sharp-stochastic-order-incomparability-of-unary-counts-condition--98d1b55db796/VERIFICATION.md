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

Run `python3 verify.py` next to this document with Python 3.10 or later. The program uses only the standard library. It constructs independent rooted ordered plane tree objects through 11 vertices and checks degree-conditioned unary frequencies. It also evaluates the exact forest and unary-degree formulas for all \(2\le n\le44\) and every eligible root degree, checks the support gap, exact extreme tail ratios and endpoint. Observed output: `PASS: 26310 exact checks`.

The analytic proof uses the classical generalized cyclic lemma and binomial identities, with no numerically inferred infinite claims. The script establishes only the stated finite checks; it is not an independent scientific audit.
