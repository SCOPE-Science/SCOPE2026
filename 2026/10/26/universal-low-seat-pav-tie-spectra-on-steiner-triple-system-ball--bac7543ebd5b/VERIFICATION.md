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
# Verification and limits

The embedded script `verify_sts_thiele.py` (Python standard library only) builds four explicit designs and checks every pair of points lies in exactly one triple. It enumerates every committee of sizes 3, 4, and 5 for orders 7, 9, and two nonisomorphic 15-point designs, comparing induced-block multiplicities to the universal formulas; it also independently evaluates raw PAV scores with exact `fractions.Fraction` arithmetic and checks the derived identity. Six-seat histograms use exhaustive enumeration of all 5,005 subsets of each 15-point point set.

Expected six-seat results: Bose counts at levels 0,1,2,3,4 are (315,2100,2170,420,0); projective binary-space counts (420,1680,2800,0,105). The checker also compares all two-point coverage counts to one. The integer and rational checks require no floating-point tolerances.

The theorem for every admissible order and every relevant Thiele weight is established analytically using incidence counts; the finite computations independently verify only the named examples, and do not constitute a proof for all orders. No broader electoral model, additional voting rules or independent validation is asserted.
