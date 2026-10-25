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

# Exact reproducibility

Run `python3 verify.py` with Python 3.10+ and the package's pinned `sympy==1.14.0` dependency. This program needs no external inputs. It enumerates all 1404 nonempty simplices, checks 486 legal elementary collapses, builds the original signed 540-triangle rational coboundary system, and computes its three-dimensional cocycle quotient via a 26-edge spanning-tree gauge. It verifies the action of symbol and coordinate generators on that quotient and then checks signed Lefschetz traces for every element of the 1296-element symmetry group. Every printed conjugacy class is tested for character constancy and matches the complete 22-class table. It separately checks all 27 ternary translations and the absence of nontrivial fixed simplices.

The original packaged execution succeeded and concluded `VERIFY_OK_TERNARY_NEIGHBORHOOD_FULL_SYMMETRY_CHARACTER`; `verify_output.txt` contains the generated output. This is an exact finite verification for the specified complex, not an extrapolation to larger Hamming graphs. Finite enumeration and exact linear algebra do not establish novelty or independently certify publication claims. The character is rational; integral module structure and higher equivariant topology are not determined.
