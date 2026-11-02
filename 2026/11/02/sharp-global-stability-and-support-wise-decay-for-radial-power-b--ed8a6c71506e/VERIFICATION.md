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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and the standard library. The test script reconstructs the exact dual-step relation numerically, solves its strictly monotone radial inverse by Newton iteration, and exercises 1,920 dimension/exponent/stepsize contractions, 12 axial boundary and extinction cases, three asymptotic coordinate constants, and four orbits on both sides of the axial boundary. The checks passed when assembled. Each test is finite and floating-point; no numerical run replaces the proof for all \(p>2\) and all dimensions.

To reconstruct the analytical argument, note the strict inequalities in RESULT.md's Proof section, the axial scalar inequality including the equality case, and the dual-variable inverse-power telescoping limit. The only external mathematical background required is elementary continuity, compactness, a Taylor expansion at one and Cesàro averaging. The reference literature establishes the Bregman-gradient framework, not any claimed independent audit.
