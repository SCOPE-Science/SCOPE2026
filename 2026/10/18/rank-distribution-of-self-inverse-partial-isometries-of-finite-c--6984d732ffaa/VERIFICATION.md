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
# Reproducibility and verification

Run `python3 checks/verify.py` from the root directory containing the accompanying files. The checker uses only the Python standard library, prints six `METRIC_OK` lines for \(4\le n\le9\), four `EXTENSION_OK` lines for \(4\le n\le7\), nine `DIHEDRAL_OK` lines for \(4\le n\le12\), then `VERIFY_OK`.

The first route enumerates every domain and every permutation of that domain, checks its square directly, then verifies cycle-graph distances for every unordered pair. It does not assume the published dihedral-extension theorem. The second route enumerates restrictions of all rotations and reflections, removes duplicate partial maps, and directly compares each map with its inverse. A third check constructs every partial injection, tests the graph metric directly, and compares the resulting entire monoid with all dihedral restrictions for \(4\le n\le7\); this independently corroborates the structural lemma on bounded cases. Both enumerators compute rank coefficients independently of the closed polynomial arithmetic.

The universal proof is in `RESULT.md`: the only cited non-elementary premise is the published dihedral restriction and rank-three extension lemma in Fernandes–Paulista [1]. The finite enumerations cover bounded cycle sizes only; they do not prove all-parameter uniqueness or a universal counting identity. No separate external audit or independent validation has been performed.
