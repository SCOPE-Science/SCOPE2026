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

# Reproducibility and verification

The mathematical proof is in `RESULT.md`. Run the self-contained Python 3 script `python3 threshold_diameter_checker.py`; it requires no third-party libraries or datasets. The reproducible finite diagnostics include 4,000 random row-stochastic-matrix pointwise Dini inequalities, 1,500 exact two-node saturation instances, nine critical-time inverse-square diagnostics (three initial values at three times), and four supercritical fixed-point/root-derivative checks. An observed `PASS` means only that those finite diagnostics ran successfully.

The infinite-time theorem is not certified by simulation. Its independent analytic ingredients are the exact row-diameter identity for a stochastic matrix, the centered logistic secant maximum, scalar comparison for absolutely continuous solutions, the invariant two-node antisymmetric manifold, and the scalar quadratic/concavity arguments. The proof does not require a separately stored computation or externally generated certificate.

The primary motivating preprint was inspected in its available HTML full-text representation, including its weak-feedback theorem and later heterogeneous-cusp conclusions. The key Gaubert–Qu literature was inspected at its row-coefficient and nonlinear-consensus sections. A matching prior theorem outside those inspected sources is not categorically excluded. Independent mathematical validation and independent audit have not been performed.
