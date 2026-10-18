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

# Reproducible finite verification

Run `python3 verify_equivariant_k2n.py` with a standard Python 3 interpreter. It enumerates faces from the graph-edge partial matching definition and discards directed cycles by exhaustive DFS. It independently computes action permutations on primitive incidence pairs, orientation signs on every invariant simplex, and the reduced Lefschetz trace. Conjugacy-class representatives cover all partitions of each \(n\) from \(2\) through \(6\), for both left-swap values. The exact predicted character is checked in all \(56\) cases.

The augmented-face counts observed for \(n=2,3,4,5,6\) are respectively \(45,216,945,3888,15309\). The separate exact mod-two chain reduction tests all reduced Betti numbers for \(n=2,3,4,5\): only degree \(n\) survives with rank \(n^2-1\). The script prints `VERIFY_OK` only after every assertion succeeds. The arbitrary-\(n\) character formula follows from the source theorem and the universal signed-orbit proof, not from the finite checks. This package does not perform independent human audit or certify an integral lattice decomposition.
