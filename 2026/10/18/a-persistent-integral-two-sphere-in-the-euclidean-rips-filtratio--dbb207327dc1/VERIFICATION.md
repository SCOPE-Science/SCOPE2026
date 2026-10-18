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

# Reproducibility and evidence

Both `verify_h3.py` and `collapse_sequences.json` are standalone complete files. Run `python verify_h3.py verify collapse_sequences.json` from the directory where they are extracted. The verifier uses the Python standard library and exact integer pairs for the ring \(\mathbb Z[\phi]\) with \(\phi^2=\phi+1\), not floating point. It reconstructs thirty roots, the exact eight squared-distance levels, maximal cliques and every face; checks the retained two-dimensional closed connected manifold, and replays each elementary simplicial collapse while checking that a face has one and only one remaining immediate coface. All relative target cells remain untouched. The verified pair totals are 96 at scale one, then 330, 1690 and 7802 at squared-distance 3−\(\phi\), 2 and 1+\(\phi\) respectively. The respective nonempty face totals are 362, 1022, 3742 and 15966. These exhaustive finite computations, plus the standard free-face deformation-retraction lemma and classification of closed surfaces, prove the homotopy statements for the fixed thirty-point configuration. Symmetry follows separately from orientation of the convex polytope boundary.

The limits are substantive: no scale at or after \(r=\sqrt3\) is checked or claimed; no equivariant collapse certificate or third-party independent audit is supplied. A no-match bibliographic search does not establish uniqueness.
