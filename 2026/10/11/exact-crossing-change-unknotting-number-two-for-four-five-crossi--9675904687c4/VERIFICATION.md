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
The four source Gauss codes were checked directly. For each code, crossings \(1,2,4,5\) have odd chord parity and negative sign, while crossing \(3\) is even, so \(J=-4\). Since virtual Reidemeister moves preserve \(J\) and one crossing change changes \(J\) by at most \(2\), at least two crossing changes are necessary.

`artifacts/verify_unknotting.py` independently checks the finite upper-bound certificates. It changes crossings \(1\) and \(4\), verifies the signed Gauss-code adjacency conditions for the stated type-I/type-II cancellations, and requires the final code to be empty for all four knots.

Expected output:

`VERIFY_OK knots=5.40,5.107,5.880,5.1238 odd_writhe=-4 lower_bound=2 upper_bound=2`

Limits: the script certifies only these four explicit codes. It does not enumerate all diagrams of the knot types and is not used to infer any infinite classification. The lower bound rests on Kauffman's proved odd-writhe invariance.
