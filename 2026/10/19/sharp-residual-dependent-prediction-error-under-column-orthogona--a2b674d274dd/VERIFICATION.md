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
# Verification and reproducibility
The correctness argument is a complete algebraic proof based on the thin QR decomposition, positive spectral contraction, a sharp one-variable maximization, and explicit rank-one attainment. Exact statements, hypothesis boundaries, and the distinction between prediction-energy and coefficient norms appear in `RESULT.md`.

Run `python3 checks/verify.py` with Python 3 and its standard library. In the recorded execution it produced `PASS: 48 sharp rank-one cases; 1200 randomized feasible matrices`. The script deliberately uses an orthonormal-coordinate representation to test the invariant expression, then computes its errors from normal equations by partial-pivot Gaussian elimination. Its checks are finite numerical stress tests, not a proof of the universal result.

A second numerical suite (not required for replay) independently used QR factorizations, least-squares solves, condition numbers up to \(10^6\), and 120 extremizer/1,200 feasible random perturbation instances. These experiments do not establish novelty, independent audit, or applicability to arbitrary matrix perturbations. The 2016 and several classical projection-related sources remain partial-access literature risks.
