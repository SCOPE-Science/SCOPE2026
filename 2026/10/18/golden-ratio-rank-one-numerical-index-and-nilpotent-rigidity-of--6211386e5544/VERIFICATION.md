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
# Verification notes

The finite-dimensional theorem is proved by the closed incidence array in RESULT.md, the exact reduction of the numerical-radius supremum to vertices and dual supports, dihedral normalization of two boundary parameters, and five exhaustive dual-edge inequalities. The unique equality configuration in the reduced sector gives all signed dihedral extremizers, and the incidence zeros verify square-zero behavior.

To reproduce the supporting tests, use Python 3 and SymPy and execute `python checker.py` in the directory containing the delivered scientific files. The standalone checker returned `PASS 895 checks; exact incidence, polynomial identities, finite samples`. Its exact symbolic tests include all 100 supporting-functional/primal-vertex incidence entries and the critical golden-ratio polynomial identities. Random tests use a fixed seed and serve only as consistency checks, not as a proof of a continuum claim. The proof requires no finite extrapolation, spectral numerical fit, or unaudited external certificate.

Only the real regular decagonal plane and rank-one operators are covered. The unrestricted numerical index is taken from Martín–Merí, Theorem 5, DOI 10.1080/03081080600628323. A publication-priority comparison beyond the named historical source texts cannot be certified by these mathematical calculations. Independent mathematical and bibliographic validation have not been performed.
