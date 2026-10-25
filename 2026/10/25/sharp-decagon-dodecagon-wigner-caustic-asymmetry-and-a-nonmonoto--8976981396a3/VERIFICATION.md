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

The complete proof is in `RESULT.md`. Run `python verify_wigner.py` in this directory with SymPy installed. The observed output was `EXACT_WIGNER_DECAGON_DODECAGON_OK 12 28`.

The checker enumerates all eighty and two hundred forty two-free-coordinate active-set/sign assignments using exact symbolic trigonometric and algebraic expressions. Every admissible vertex is matched to the complete displayed signed-cyclic orbits. Every orbit's quadratic area is simplified exactly, and the final normalized constants and their strict inequality are checked. Additional independent midpoint and polygon shoelace reconstructions use genuine closed interior parameter vectors.

The mathematical justification that this finite enumeration gives the global result is separate: strict convexity of the quadratic Wigner deficit forces maximizers to vertices, and an active-coordinate dimension argument proves that all vertices occur in the exhaustive finite enumeration. No random experiment or numerical tolerance is used to infer the theorem. The exact checks do not establish external originality or independent certification.
