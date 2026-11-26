---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Re-audited the replacement RESULT.md. The frozen Finding misleadingly says ordinary kernel-sign indicators attain the operator norm: for any row of signed mass one and absolute mass R, its largest absolute output on indicators is (R+1)/2, strictly smaller than the maximizing norm in this problem. The repaired statement explicitly distinguishes signed ±1 inputs for the norm from indicators for the one-sided extrema. Decomposing the affine range into the two layer indicators and centered coordinate contrasts gives contrast covariance H/[n(n−1)] and the two stated kernel rows. Only disjoint pair–pair entries can change sign within a layer; n=3 has none. The increasing/decreasing row functions cross uniquely at the uniform-atom weight. The conditional Bernoulli ratio and stationary, strictly log-concave determinant check also hold. No change to the supporting computation was needed.

## originality

PASS

The surviving claim is the full signed-row norm law and unique minimization over positive exchangeable singleton/pair weights. The determinant result is covered and retained only as comparison; the uniform unsigned-incidence formula is standard matrix algebra and not claimed separately. The inspected literature and comparable catalogue records do not yield the signed-row dependence or uniqueness for this objective.

## value

PASS

This solves a natural one-parameter robustness-design problem on the first two nonzero Boolean layers. The full formulas locate both the disjoint-entry sign threshold and the actual worst-row transition, identify the unique minimax design, and quantify sharp nonpositivity for bounded inputs. The value is the weighted behavior and unique optimum, not the single uniform benchmark or the determinant comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
