---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The proof in `RESULT.md` uses the explicit witness at \(t=a\) for failure, and controls a neighborhood of zero, a compact interval away from zero and the uniform tail to establish strict sub-Gaussianity near the two endpoint weights. The sparse proxy comparison is analytic.

The optional `python verify.py` uses only the standard library. It computes the exact second and fourth moments at the excluded weight for selected amplitudes, checks the MGF witness numerically, and compares a proxy lower estimate against \(a^2/(2\log(2a^4))\). The sample does not certify the full real-amplitude range, the endpoint intervals, or global optimality of a numerical tilt.
