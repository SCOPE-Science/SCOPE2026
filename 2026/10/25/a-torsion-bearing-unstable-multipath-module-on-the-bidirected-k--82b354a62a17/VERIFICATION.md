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

# Verification of integer multipath homology

Run `python3 checker.py` with Python 3.9 or newer and no third-party packages. The checker constructs each boundary from the actual ordered faces, tests every face deletion, checks the chain condition after each unimodular cancellation, and reduces the single residual boundary over the integers. Its output reports, for \(n=4\), 71 unit cancellations in dimension three, 65 in dimension two, 15 in dimension one, and one in the augmentation, leaving one remaining differential with gcd two. It separately computes the original unreduced mod-two and mod-three ranks, confirming the coefficient-sensitive ranks.

As a separate arithmetic cross-check, integer Smith normal form of the original matrices \(\partial_0,\partial_1,\partial_2,\partial_3\) yields respectively nonzero diagonal factors \((1)\), \((1^{15})\), \((1^{65})\), \((1^{71},2)\). This is a direct check, not an independent audit or a claim of external certification. The interpretation as an unstable dynamical module follows the cycle-closure definition in the cited 2022 paper. The result is exact for \(n\in\{1,2,3,4\}\) only; no higher-parameter theorem is certified.
