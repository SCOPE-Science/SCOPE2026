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

# Verification record

Run `python3 verify_cube_vertex_law.py` from the same directory. The program is standalone and uses only the Python standard library. It executed successfully and checked: 80 exhaustively enumerated simple face-adjacency walks; exactly 24 integer unfolding-distance classes; four affine-inequality corner tests for each class; exact rational even moments; numerical midpoint-rule comparison with the analytic CDF at seven radii; and support endpoints.

The proof that exhaustive walks are sufficient, and the analytic area integrations, appear in `RESULT.md`. The midpoint-rule calculations are finite sanity checks, not substitutes for those proofs. No external independent mathematical validation has occurred.
