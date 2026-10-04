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

The exact verification artifact is `verify.py`. It uses only Python's standard-library `fractions.Fraction` type. It reconstructs the two elimination polynomials, builds Sturm sequences by exact Euclidean division, counts all real roots, verifies the stated rational isolating intervals, checks which roots lie on the correct sign quadrant, and checks exact signs of the transverse scalar at representative equilibria.

Run:

`python3 verify.py`

Expected output:

`VERIFY_OK`

The decimal transition coordinates in the finding are not used as proof. The proof is the exact Jacobian formula together with the rational elimination, Sturm root counts, and sign arguments. The four axis equilibria are not verified by a Jacobian because the vector field is nondifferentiable there. No numerical trajectory is used to prove any infinite-time statement.
