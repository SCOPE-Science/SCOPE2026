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
# Verification

The claim was re-derived from the map rather than inferred from numerical trajectories.

1. First-moment invariance was checked as \(m=a+Rc\), where \(c=\int g u(g)\,d\mu\) and \(|u(g)|=1\).
2. Second-moment invariance was checked as \(q=a^2+R^2q+2aR\operatorname{Re}c\).
3. Eliminating \(c\) gives \((1-R^2)q=2a\operatorname{Re}m-a^2\).
4. The packaged symbolic checker verifies that subtracting \(|m|^2\) from this relation is exactly equivalent to the completed-square disk formula.
5. The equality case was checked from \(V=\int|g-m|^2\,d\mu\): \(V=0\) if and only if \(\mu\) is a point mass, and invariance then requires a fixed point.

The result is not a numerical extrapolation and does not rely on finite-orbit convergence. Its stated scope is limited to compactly supported invariant probability measures. No existence, uniqueness, ergodicity, mixing, or physical-measure assertion is made.
