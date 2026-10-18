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
Run `python check_helm.py` beside this document. The program uses exact rational Machin bounds for \(\pi\), alternating cosine enclosures and polynomial interval arithmetic to certify the five small integer orders in the proof. When NumPy is available it also verifies the full stochastic transition matrix and SLEM for each integer \(5\le n\le110\), 106 graph orders. All checks succeeded in the supplied environment.

The infinite-order conclusions follow from the spectral decomposition, monotonic comparison, stationary equation, explicit feasibility estimates, and radial/Fourier inequalities of RESULT.md. Finite tests do not certify arbitrary orders, and no independent audit has been performed.
