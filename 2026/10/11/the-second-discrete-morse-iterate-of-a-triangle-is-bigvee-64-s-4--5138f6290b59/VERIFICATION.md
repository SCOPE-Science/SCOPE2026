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

# Reproducible checks
Run `python3 verify.py` followed by `python3 verify_homology.py`; both require only Python 3.9+ standard-library modules.

The first executable rebuilds the triangle-cycle first iterate and checks a graph isomorphism with the triangular prism; enumerates every valid acyclic vertex-edge incidence assignment; independently re-enumerates rooted forests; verifies all 828 matching pairs and checks that every one of the 6,606 oriented Hasse incidences participates in an acyclic directed graph. It computes the signed integral boundary of the 67 critical four-cells against the three critical three-cells, and checks that columns zero, seventeen and twenty-eight are exactly the three unit basis vectors.

Expected first output:
`VERIFY_OK faces=1727 f_vector=[18, 126, 428, 705, 450] incidences=6606 pairs=828 critical=[1, 0, 0, 3, 67] unit_columns=(0, 17, 28) homotopy=wedge_64_S4`

The second executable independently reconstructs the complex using undirected forests with a designated root for each component, then performs exact bitwise Gaussian elimination over \(\mathbb F_2\) on every simplicial boundary matrix.

Expected second output:
`HOMOLOGY_OK faces=1727 ranks=[17, 109, 319, 386] reduced_F2_Betti=[0, 0, 0, 0, 64]`

The acyclic-matching certificate, exact integral attaching degrees and elementary homotopy-theoretic argument yield a homotopy statement. The independent mod-two ranks corroborate but do not by themselves prove this conclusion. Only the specified finite complex is covered. No external/independent audit or publication certification is implied.
