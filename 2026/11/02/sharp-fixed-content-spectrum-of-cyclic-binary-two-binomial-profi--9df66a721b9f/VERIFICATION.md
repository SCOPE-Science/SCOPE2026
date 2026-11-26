---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification

Reconstruct the proof in `RESULT.md` using the height identity \(h_i=(p+q)B_i-qi\), the congruence classes modulo \((p+q)/\gcd(p,q)\), deletion of a balanced window using normalized heights \(h_i/\gcd(p,q)\), the arithmetic-progression upper witness and adjacent-swap continuity. The normalization makes the retained increments identical when the content and gcd are both reduced by deleting a balanced window.

Run `python3 checker.py` alongside `RESULT.md` with the unchanged included script. The enumerator checks all 32,738 nonconstant binary strings of lengths 2 through 14. It builds the rotations and computes the scattered pair profiles independently of the height formula to cross-check the profile count. The height computation tests individual collisions against arc counts. It also checks the bounds, the lower equality case and complete fixed-content attainment at these lengths, plus lower and upper witnesses and balanced windows for 9,801 positive content pairs. No finite test substitutes for the quantified proof.

Chuan's moment statistic is affine-equivalent to the `01` count at fixed content. Its complete paper was not available for comparing cardinality theorems; the comparison does not establish historical priority.
