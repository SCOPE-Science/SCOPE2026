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

# Reproducibility and limits

Run the standalone exact finite-field checker with `python3 verify_e3.py`. Its target is the reduced-support and Hessian-rank predictions for the nine pairs \((p,n)\) listed in RESULT.md; it exhaustively enumerates prime-field vectors in each small test case. Successful execution yields `VERIFY_OK`. No finite enumeration alone establishes the asserted scheme-theoretic theorem for arbitrary algebraically closed fields or unbounded \(n\). The general proof uses the common quadratic, two-block elimination, full-rank projective Hessian, Euler/binomial identities, and Serre's criterion. Independent audit has not been performed.
