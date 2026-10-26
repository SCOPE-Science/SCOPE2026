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

# Reproducibility and scope

Run `python3 verify.py` from the same extracted folder (Python standard library only). It checks the rational inequality that forces a sign change at \(11/20\), the positive sign at \(1/2\), the negative sign at \(11/20\), and numerically bisects the exact defining equation. The exact infinite-dimensional inequalities, Dieudonne estimate, and optimality argument are proved in `RESULT.md`; finite sampling is not used as a theorem certificate.

The proof applies to all normalized holomorphic functions subordinate to \(1+(2/\pi)\arcsin z\), without any restriction to finite-degree polynomials. The exact radial-order formula is asserted for \(0\le r\le11/20\); the sharp convexity radius is universal over the class. No independent audit has been performed.
