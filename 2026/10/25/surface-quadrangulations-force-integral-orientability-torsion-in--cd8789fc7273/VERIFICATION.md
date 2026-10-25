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

Run `python3 quadrangulation_threecut_checker.py` with Python 3 (standard library only). The program builds the cubical sphere, the ordinary \(7\times7\) torus grid, and the twisted \(7\times7\) and \(7\times8\) Klein-bottle grids. It independently enumerates induced connected triples and tetrahedral squares, checks square uniqueness and common-neighbor bounds, explicitly removes each proposed free-face/cell pair, and validates the final complex's exact triangular faces, surface edges, extra chords, closed surface links, Euler characteristic and boundary rank modulo \(2\), \(3\), and \(5\).

Expected elementary-collapse pair counts: `12`, `196`, `196`, `224`. Expected extra chord counts: `4`, `882`, `882`, `1204`. For the toroidal case, the residual surface has second Betti number one in all three tested characteristics. For each Klein case, the surface has second Betti number one in characteristic two and zero in odd characteristics. Full test output has four `PASS` records.

These executions are finite checks of concrete cases. The proofs of the infinite-family theorem and integral two-torsion use the free-face uniqueness argument for arbitrary allowed quadrangulations, the standard integral homology of orientable/nonorientable surfaces, and combinatorial Alexander duality. No external or independent audit was performed.
