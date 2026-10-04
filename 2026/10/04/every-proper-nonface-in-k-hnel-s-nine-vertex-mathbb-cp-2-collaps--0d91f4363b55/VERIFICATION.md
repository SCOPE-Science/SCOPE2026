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

`verify.py` reconstructs the nine-vertex complex from the two published facet seeds and the three generators of \(H_{54}\). It checks the group size, all \(36\) facets, the face vector \( (9,36,84,90,36)\), and complementarity for every nontrivial vertex bipartition.

It then visits every nonempty proper vertex set. For each face set, it verifies that the induced complex is the complete simplex. For each nonface, it loads the corresponding row of `collapse_cert.json` and replays every listed pair \( (\tau,\sigma)\). Before deleting a pair it verifies that \(\sigma\) is maximal, \(\tau\) is a codimension-one face of \(\sigma\), and \(\tau\) belongs to no other maximal simplex. The final complex must have exactly the four triangular facets of \(\partial\Delta^3\).

The certificate has exactly \(255\) entries, matching every proper nonface and no face. The checker also verifies the nonface counts by cardinality and the displayed collapse-length distribution. Because each elementary collapse is validated on the evolving complex, the proof does not rely on homology as a surrogate for simple-homotopy equivalence.

Run:

`python verify.py`

Expected final line:

`VERIFY_OK facets=36 face_vector=9,36,84,90,36 proper_faces=255 proper_nonfaces=255 nonfaces=4:36,5:90,6:84,7:36,8:9 collapse_lengths=4:0x36;5:7x90;6:18x9,19x27,20x27,21x21;7:40x36;8:72x9`

Limits: the verification is specific to the published nine-vertex combinatorial model. It certifies existence of the included collapse sequences, not uniqueness of collapse order or any statement for other triangulations.
