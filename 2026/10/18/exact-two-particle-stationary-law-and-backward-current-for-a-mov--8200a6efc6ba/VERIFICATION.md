---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the one-step kernel from the exponential dwell clocks and rotation by minus one. With b=(1+z²)/2, the incoming weights for targets containing 0 are z, (1−z)+z(1−z)+z²=1, or b+(1−z²)/2=1. The other target classes receive b, z²+(1−z²)/2=b, or z² (including z·z at the corner). At L=3 the three surviving equations are z, 1 and z². Counting weights gives T_L. A full tour can implement any single allowed hop with positive probability and return the frame to its starting orientation. The exclusion configuration graph is connected: reduce the separation to get an adjacent pair, and translate adjacent pairs using two successive hops. This gives uniqueness. Only the two neighbor-blocked states contribute to the signed drift, with opposite signs and weights 1 and z; their difference gives −(1−z)²/T_L. Over a full tour each fixed bond is exposed to each relative phase, so its mean current is v/L times this drift. The limits use z→0, T_L(1)=L(L−1)/2 and 1−z∼p/(2v), and B_L∼L²/4, respectively.

## originality

PASS

Pass is for the closed full two-particle stationary law and explicit finite-ring current. The moving-defect model, one-dwell dynamics, exact current identities and the qualitative backward-current observation are prior. The frozen summary should be read as saying that mean field closes the exact identities, not that all prior current relations were approximate.

## value

PASS

The full finite-ring law is a usable benchmark for closing the moving-defect correlations. It explains the sign by the unequal stationary weights of the two locally blocked configurations, quantifies the coefficient and distinguishes speed and ring-size scalings without mean field. The known qualitative direction is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
