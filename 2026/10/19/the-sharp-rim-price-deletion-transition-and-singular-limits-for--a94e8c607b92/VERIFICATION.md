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

# Reproduction and limits

Run `python3 wheel_price_verify.py` with Python 3 and no external dependencies. The program constructs wheel Laplacians, computes exact rational inverses of \(L+\mathbf1\mathbf1^{\mathsf T}/(n+1)\), checks direct and Fourier traces, verifies finite critical derivatives and optimum roots, and tests the stated asymptotic formulas. It reported `Checks passed: 187` in this package. Results involving trigonometric functions and limits use floating-point tolerances; finite matrix calculations use exact rational arithmetic. The exact threshold, global uniqueness, and all-order asymptotic identities require the proof in `RESULT.md` and are not inferred from test counts. The independent-audit status in the JSON front matter is `not_performed`.
