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

# Reproduction and limits

Execute `python3 verify_face_enumerator.py` using only Python 3's standard library. The script generates every strong matching induced by a vertex permutation for \(3\le n\le8\), takes every subset of those matchings, enumerates the independent cyclic compatibility rule, and compares the resulting cardinality-distribution against both transfer-matrix traces. The program also checks the top-dimensional face coefficient \(n(n-1)\) and the exact periodic Euler formula for selected lengths through \(n=100\).

The checks were executed against the included script and passed. Their finite scope is **not** presented as a proof of the all-length formula. The proof relies on the independent orientation/filtration bijection and cyclic-transfer counting, as specified in `RESULT.md`. No individual homology groups or homotopy types are computed or inferred from the Euler characteristic.
