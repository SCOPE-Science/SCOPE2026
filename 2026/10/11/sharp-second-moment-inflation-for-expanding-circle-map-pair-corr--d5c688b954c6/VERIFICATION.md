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

The exact covariance identity follows from Fourier coefficients of circular interval indicators and the periodic Bernoulli polynomial; the analytic variance limit and remainder are proved in `RESULT.md`. To replay the diagnostic calculations, execute `python3 CHECK.py` from the unpacked file directory. It requires only the Python standard library and produced `PASS 153 independent rational finite checks`.

The program uses two independent exact-fraction paths: algebraic Fourier–Bernoulli covariance evaluation and geometric integration of preimage-interval overlaps. It also compares the analytic finite-sample variance sum with direct exact integration of the complete pair count over all boundary-partition intervals for selected small inputs. These tests do not establish the limit for unbounded sample sizes; the proof supplies that step. No independent audit has been performed.
