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

The symbolic proof uses only the explicit lifted Hasse-edge formula for the regular coloring cover and Stong beat-point deletion. The packaged `artifacts/verify.py` independently checks the concrete projective-plane application.

The verifier reconstructs the 13-point height-two poset, solves the admissibility equations over \(\mathbf F_2\), chooses a cocycle outside the coboundary subspace, builds the connected double cover, and checks that immediate upper/lower Hasse degrees are preserved on every sheet. It then confirms zero beat points in both spaces, the base \(f\)-vector \((13,36,24)\), the cover \(f\)-vector \((26,72,48)\), closed-surface edge incidence, cycle vertex links, and Euler characteristics \(1\) and \(2\).

The computation certifies only this concrete application. The all-cover core-scaling statement is proved symbolically in RESULT.md. No claim is made for nonregular or infinite-sheeted covers.
