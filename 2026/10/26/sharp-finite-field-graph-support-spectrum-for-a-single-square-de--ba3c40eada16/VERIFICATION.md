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

# Verification of the graph-support theorem

Run `python3 verify_profiles.py` using Python 3.8 or later from the directory containing the checker. The script requires only the standard library. It checks every nonzero dependency ratio in the prime fields of orders 2, 3, 5, 7 and 11; computes projective lines and nonisotropic orthogonal orbits; enumerates all invertible two-column orthogonal frames; calculates their exact projected graph-support profiles for extremal witnesses in dimensions three, four and five; and exhaustively checks natural-basis block rigidity in dimension three over the fields of orders two and three. The actual run returned:

`VERIFY_OK; 339 projective/support consistency checks; full 3x3 field-2/3 basis exhaustive`

These finite tests cannot establish the theorem for untested fields or dimensions. The general proof in `RESULT.md` establishes the projective involution count, classification of every admissible basis, orbit separation, and the matching extremal construction for arbitrary prime powers.
