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

The finite verification program `verify.py` reconstructs orbit compatibility directly from the original Hamming metric for all cube dimensions \(4\le n\le8\), checking every unordered pair of orbit labels. For \(4\le n\le6\), Bron--Kerbosch enumeration independently verifies the complete family of maximal simplices. It checks face vectors and computes mod-two simplicial boundary ranks through dimension three for \(4\le n\le8\). The printed output ends with `VERIFY_OK`.

The proof (in `RESULT.md`) is uniform in dimension and integer-valued: geometric fixed points are the orbit-union complex, each base-cube edge contributes one PL three-sphere, all incident edge spheres share a contractible tetrahedron at each endpoint, and the resulting graph of spheres has precisely the one- and three-sphere summands claimed. Mod-two finite experiments alone do not certify integral homotopy; they serve only as independent finite corroboration. Full-text priority comparisons to two relevant 2026 preprints remain incomplete because authorized source access was unavailable.
