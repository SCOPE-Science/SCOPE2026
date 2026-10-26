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

# Reproduction and logical limits

Use Python 3 standard library to run `python verify_pisv.py` from this package. The code verifies exact polynomial identities with rational coefficients, exact stability boundary values at \(\lambda=1/10\), two interior neutral points at \(\lambda=1/9\), and 50,000 rational sample evaluations straddling the sharp transition. The reported success message is `PISV_EXACT_CHECKS_OK 50015`.

The proof of the full real-axis claim is the exact quadratic factorization and discriminant sign analysis in `RESULT.md`. Finite rational sampling is not used to infer an infinite-domain theorem, and failures or numerical timeouts are not treated as impossibility evidence.

Source equation: Koellermeier and Samaey, arXiv:2210.08302v2, Eq. (96). Observed prior work is distinguished by the explicit parameter-sharp interval characterization; independent publication-priority verification and independent scientific audit have not been performed.
