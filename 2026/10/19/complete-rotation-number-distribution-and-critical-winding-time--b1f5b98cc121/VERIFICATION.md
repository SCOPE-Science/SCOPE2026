---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

# Scope of the checks

The finite standard-library program `verify.py` compares direct polygon areas against the area polynomial at 36 distinguished levels, and tests the smallest resonance and finite samples of the large-resonance asymptotic. These tests did not examine rotation numbers between adjacent distinguished levels and cannot validate affine interpolation there.

The corrected off-node relation is checked symbolically in `RESULT.md`: the area per unit leaf-coordinate interval has total mass \(4t(1-hq)\), and the image of the first corner vertex advances one arc of mass \(qtd\). The exact ratio, not affine interpolation, gives the rotation number. The example at \(K=3, r=1/14\) distinguishes the formulas. The proof gives the full area pushforward, moment cutoff, and resonant asymptotic independently of finite numerical tolerances.
