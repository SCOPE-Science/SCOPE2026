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

# Verification details

The original geometric fixed-point space is modeled by the compatible-orbit simplicial complex, with vertices at orbit barycenters. This equivalence is proved directly in `RESULT.md`.

`CHECKER.py` uses only the Python standard library. It verifies \(392\) coordinate-dihedral isometries and computes the complete orbit-compatible simplicial complexes for all \(391\) nonidentity elements. Each collapsible free-face pair is tested against the current immediate coface structure. The terminal complexes are checked as precisely two vertices, a connected cycle, a connected closed triangulated surface of Euler characteristic two with connected cyclic vertex links, or no faces. The pre-collapse Euler characteristic is separately checked by alternating sums. The published ambient \(S^3\) homotopy equivalence supplies the identity case. The exact output is in `CHECKER_OUTPUT.json`.

Results: \(1\) case of \(S^3\), \(14\) of \(S^2\), \(75\) of \(S^1\), \(182\) of \(S^0\), \(120\) empty; all \(392\) fit the predicted formulas. The largest generated nonidentity fixed orbit complex contains \(9,214\) nonempty faces.

The computations are exact finite enumeration for these parameters, not evidence for all torus sizes. No independent external scientific audit or validation has been performed.
