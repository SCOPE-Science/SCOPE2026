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

# Reproducibility checks

Running `python verify.py` with `numpy` and `scipy` checks the normalized beta cell masses, 12 left/right \(N=3\) convolution asymptotic comparisons at ratio 1/5, strictly unequal amplitudes, and a separate quadrature check of the critical \(N=2\) logarithmic slope. These comparisons executed without assertion failures.

The proof is analytic: force cancellation, stationary one-filter density, beta convolution, and Young's inequality. Finite numerics do not prove the infinite statement or publication priority. Assumptions and critical limiting cases are given in RESULT.md. Independent audit has not been performed.
