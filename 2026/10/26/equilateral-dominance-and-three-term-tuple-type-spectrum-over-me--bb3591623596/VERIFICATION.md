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

# Finite verification and boundaries

Run `python verify_star_metric.py` from this directory using Python 3 standard libraries only. The program enumerates all labelled core metrics for arities one through four and independently enumerates full finite metric extensions for arities one through three with up to two leaves, and arity four with zero leaves. It recomputes the three largest spectral bases, exact multiplicities, and the all-leaf-count formula at arity two, including its first five values. `verify_output.txt` contains the recorded successful program output.

For the general theorem the executable does not enumerate all arities or leaf counts. The proof of the leaf-factorization bijection and the strict spectral-base bounds appears in `RESULT.md`. The code and this report have been checked in a self-review only; independent scientific audit has not been performed.
