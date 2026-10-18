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

The standalone Python 3 checker `verify_heawood_equivariant.py` was executed from its actual supplied path with no third-party dependencies, and the resulting JSON output was saved as `heawood_equivariant_check.json`.

The checker reconstructs the seven-point Fano incidence graph, all \(24\) perfect matchings, \(2201\) nonempty perfect-matching faces and \(3461\) nonempty ordinary matching faces. It replays independent edge-toggle discrete-Morse matchings with \(1092\) and \(1722\) pairs, respectively, and exhaustively topologically sorts the directed Hasse graphs with \(8736\) and \(14574\) incidences. The resulting critical cells are one vertex plus \(16\) two-cells, and one vertex plus \(16\) four-cells, proving the sphere-wedge premises.

It generates all \(336\) graph automorphisms from invertible binary three-dimensional matrices and point-line polarity. For every automorphism and for both complexes, two independently coded exact integer Lefschetz trace formulas (signed fixed faces and admissible unions of edge permutation cycles) agree. All eight character-type rows, including the sign-twist identity, were verified.

These are complete finite verifications for the stated complexes. The result does not classify other incidence graphs or establish an integral lattice isomorphism, and independent mathematical auditing has not been performed.
