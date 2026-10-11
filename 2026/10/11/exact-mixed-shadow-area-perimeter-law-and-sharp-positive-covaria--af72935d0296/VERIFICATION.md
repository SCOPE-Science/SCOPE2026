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

The analytic proof is self-contained in `RESULT.md`. Run `python3 verify.py` from the extracted package directory; the script uses only Python's standard library. It samples 180,000 Haar-uniform two-planes by orthonormalizing two independent four-dimensional Gaussian vectors, which is independent of the proof's Hodge-star sampling coordinates. The completed check printed `VERIFY_OK` and compared both key incidence averages, the exact mixed moment at three positive side-length vectors, and the exact unit-cube expression.

Reference values: common-index incidence \(1/4\); disjoint-index incidence \(\pi/16\); for the unit four-cube, mixed moment \(6+3\pi/2=10.71238898038469\ldots\) and covariance \(3\pi/2-14/3=0.04572231371802\ldots\). Finite Monte Carlo tolerances are intentionally loose to avoid falsely presenting randomized numerical agreement as a proof. The exact formulas, independence claim and sharpness are established algebraically in `RESULT.md`; no unresolved computational certificate is required. No independent external audit was performed.
