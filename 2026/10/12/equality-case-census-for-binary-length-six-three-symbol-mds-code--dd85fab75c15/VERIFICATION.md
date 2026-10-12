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

Run `python3 verify.py`. The verifier has no non-standard dependencies and reconstructs the complete finite problem from definitions. It verifies: \(64\) vertices; \(1{,}632\) compatibility edges; every maximal clique; an independent list of all size-\(16\) cliques; direct pairwise three-symbol distance in every maximum; all \(768\) declared isometries; the five orbits; and affine closure of each maximum.

The mathematical upper bound does not depend on exhaustive search: agreement on four consecutive coordinates forces two equal cyclic three-symbol windows, so any code with minimum three-symbol distance at least \(5\) projects injectively onto any fixed consecutive block of four coordinates and therefore has at most \(16\) words.

The computation is finite and exhaustive only for the stated exact parameter. It does not certify a classification under the unknown full isometry group, and it makes no claim for other lengths, alphabets, window widths, or distances.
