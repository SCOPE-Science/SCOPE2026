---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed operation x*y=theta(xy^{-1})y on Gamma=Q8×C7. Right translations are R_{theta(y)^{-1}y} theta; the source displacement-generation premise implies Inn=R_Gamma ⋊ C6, with trivial intersection because theta fixes identity and nontrivial translations do not. Separating coprime C3/C2 actions yields (Q8⋊C3)×(C7⋊C2)=T*×D14 of order 336. T* orders 1,2,3,4,6 and D14 orders 1,2,7 exclude order12; geometric Lambda has f^6=-1 and f order12. Inspected complete 56-point permutation-enumeration code at artifacts/verify_prism_symmetry.py, including independent orbit-group model, full BFS, element orders and 336-size checks. Structural proof establishes result, not verifier output alone.

## originality

PASS

The same-order nonisomorphism comparison appears not established in inspected primary source; this is a qualified new distinction between finite-quandle intrinsic symmetry and the geometric orbit group.

## value

PASS

A natural pair of 336-element symmetry groups associated with the same geometric realization are structurally distinguished, preventing a false identification; explicit element-order invariant is useful to future quandle/geometry comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
