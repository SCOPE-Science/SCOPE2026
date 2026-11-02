---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In the ideal homogeneous Glover–Balmer step-response model K_i(t)=erfc(alpha_i/sqrt(t)), exact pulse superposition yields D_NF−D_FN=Q[G(z)−G(rz)] with z=alpha_1/sqrt(Delta), r=d_2/d_1>1, and G(z)=erfc(z/sqrt(2))−2erfc(z). G has a unique strict maximum at sqrt(3 log 2), since G′=(4e^(−z²)−sqrt(2)e^(−z²/2))/sqrt(pi). For each r>1, G(z)−G(rz) switches exactly once on (z0/r,z0), where its derivative is positive; hence the optimal order reverses once. Implicit differentiation gives strictly decreasing z_r versus r, and the limits bound Delta_c/alpha_1² between 1/(3log2) and 1/z_p². Independently checked the superposition and sign at sample durations for five r-values; finite tests supplement the analytic proof.

## originality

PASS

The Glover–Balmer kernel, intermittent pumping superposition and stream depletion factor methods are classical. The assessed result is the precise two-well equal-duration endpoint objective and its strict single ordering reversal with universal limiting constants; best-of-knowledge no exact prior coverage identified.

## value

PASS

A physically motivated scheduling order can invert with pumping duration even with equal discharge and fixed spatial well locations. The complete two-policy one-switch theorem and sharp dimensionless bounds provide a usable exact optimization criterion within an explicit aquifer model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
