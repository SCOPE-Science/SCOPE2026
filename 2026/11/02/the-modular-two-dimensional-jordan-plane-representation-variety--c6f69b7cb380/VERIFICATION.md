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

# Verifiable computations and scope

Run `python3 verify_jordan_plane.py` using only the Python standard library. The program independently constructs the multiplication of each two-by-two matrix, forms the four scalar equations from the original condition, and, for each possible second matrix, row-reduces the linear commutator equation for the first matrix. It compares the resulting counts with the closed formula over seven finite fields: orders 2, 3, 5, 7, 4, 8 and 9. Fields of orders 4, 8 and 9 are constructed as polynomial-field extensions, not as invalid modular arithmetic on integers. The same program also exhaustively checks all pairs of matrices over fields of orders 2 and 3, independently of row reduction. Exact observed output is in `verification_output.txt`.

The symbolic component proof, absolute irreducibility argument, intersection description and singular-locus argument are written in `RESULT.md`; no finite run establishes these universal statements. No independent mathematical audit or external certification was performed.
