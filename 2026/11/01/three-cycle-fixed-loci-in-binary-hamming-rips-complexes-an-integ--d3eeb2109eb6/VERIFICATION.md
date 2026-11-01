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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or newer; no third-party packages are required. The script reconstructs the original binary Hamming vertices, computes their actual order-three orbits, verifies that the three-bit transposition preserves those orbits, and constructs the complete fixed orbit graph using original pairwise distances. It checks every edge against the claimed six orbit-type adjacency cases.

For each \(m=0,1,2,3,4\), the script enumerates the complete flag complex, performs the exact proposed elementary free-face collapses, compares all remaining simplices against the two-cube-core-plus-bridge model, and independently computes mod-two reduced homology by exact bitset boundary reduction. The \(m=0\) case is only a boundary control; the theorem starts at \(m=1\).

The recorded successful output was:

```text
m=0 orbit_vertices=4 fvector=[4, 4] collapse_pairs=0 reduced_F2_Betti=[0, 1]
m=1 orbit_vertices=8 fvector=[8, 14, 4] collapse_pairs=4 reduced_F2_Betti=[0, 3, 0]
m=2 orbit_vertices=16 fvector=[16, 44, 32, 10] collapse_pairs=24 reduced_F2_Betti=[0, 7, 0, 0]
m=3 orbit_vertices=32 fvector=[32, 128, 160, 96, 16] collapse_pairs=112 reduced_F2_Betti=[0, 15, 0, 2, 0]
m=4 orbit_vertices=64 fvector=[64, 352, 640, 560, 192, 32] collapse_pairs=480 reduced_F2_Betti=[0, 31, 0, 18, 0, 0]
VERIFY_OK
```

The unrestricted homotopy splitting is proved in `RESULT.md` using an explicit all-parameter collapse. Finite computations do not establish arbitrary-parameter validity or integral torsion-freeness; those conclusions follow from the structural proof and the published ordinary cube Rips theorem. The complete full text of one recent relevant group-action preprint was inaccessible at review, and independent validation has not been performed.
