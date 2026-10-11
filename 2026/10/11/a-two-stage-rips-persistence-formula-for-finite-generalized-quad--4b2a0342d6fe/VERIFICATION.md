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

# Verification of the incidence-metric Rips formula

Use `python3 verify.py` with the supplied Python standard-library-only source. It constructs the symplectic generalized quadrangles over the prime fields with two and three elements from projective isotropic vectors and lines, then exhaustively computes both incidence-graph shortest-path metrics. No externally installed mathematical packages are required.

The replay enumerates maximal cliques of the scale-two graph independently of the proposed closed-star facets. It verifies their exact equality, traverses the face poset, and performs *every* prescribed elementary pair deletion after testing that the deleted face has exactly one coface. The remainder is checked against the original incidence graph, rather than against a Betti number alone.

At scale three the checker verifies all cross-type and within-type pair distances, independently enumerates maximal cliques on each side, and checks the exact join decomposition. Over the binary field it constructs the full boundaries in each side and calculates reduced homology via exact bit-vector elimination. The finite cases return point/line-side reduced first Betti ranks 16 and 81 and zero otherwise; the symbolic join theorem gives third ranks 256 and 6561. The actual replay output is retained in `verification_output.txt`.

This is a finite reproducibility check, *not* a computational proof of the arbitrary-order claim. The general result rests on the explicit all-order free-face matching and incidence-geometric projection arguments given in `RESULT.md`. The classification does not assert anything about weighted incidence graphs, generalized hexagons, or unpublished independent validation.
