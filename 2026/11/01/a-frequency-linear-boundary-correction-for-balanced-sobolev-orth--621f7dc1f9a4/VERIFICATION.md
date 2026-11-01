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

Reproduce the finite checks by running `python3 check.py` with the Python 3 standard library. The checker independently builds exact monomial Gram matrices, solves the monic minimization equations over rational numbers, and compares the results against the Schur-pivot formula in 120 cases; it also performs 12 finite asymptotic consistency tests. The expected final line is `EXACT_GRAM_VS_SCHUR 120 ASYMPTOTIC_FINITE_TESTS 12 PASS`.

The infinite asymptotic proof is in RESULT.md, steps 1–4. Finite tests do not certify the asymptotic remainder, and numerical convergence is not used as proof. The statement assumes fixed \(m\), \(a\), and \(\lambda\) with \(|a|<1/2\) and \(\lambda>0\). Independent audit has not been performed.
