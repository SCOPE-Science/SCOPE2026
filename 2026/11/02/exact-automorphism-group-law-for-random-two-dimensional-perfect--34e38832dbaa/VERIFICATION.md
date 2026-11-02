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

# Computational verification

Run `python3 verify.py` with Python 3.9 or newer. The script has no third-party dependencies, constructs each finite field from an explicit monic irreducible polynomial, exhaustively enumerates invertible structure matrices, enumerates all candidate monomial automorphisms, and directly tests the defining algebra homomorphism identities. It counts both the full sample and the simple subpopulation, then compares with the closed formulas. It additionally calculates the Burnside orbit count from the histogram and compares against the published dimension-two class formula.

The ten completely enumerated fields are \(q=2,3,4,5,7,8,9,11,13,16\), including extension fields and both characteristic types. The final expected line is `VERIFY_OK`. This enumerates only those ten fields and is not an infinite proof; the symbolic classification in `RESULT.md` supplies the arbitrary finite-field argument. The full census covers every invertible matrix in the tested dimensions; a partial search would not provide such a check. Nothing in the script establishes mathematical priority or independent certification.
