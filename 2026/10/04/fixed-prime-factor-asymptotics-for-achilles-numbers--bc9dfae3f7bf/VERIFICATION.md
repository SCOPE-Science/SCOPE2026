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

The symbolic proof is the primary evidence. It checks the exact Achilles criterion in prime-exponent coordinates, identifies the unique leading signature family, applies the fixed-order Landau theorem on a polylogarithmically uniform range, uses absolute convergence of the prime/exponent weights, and bounds every other exponent pattern at lower order.

`verify.py` is a finite corroboration. It generates powerful integers through the unique square-cube representation with squarefree cube part, reconstructs prime exponents, and tests the Achilles condition directly. At the configured bound of `100000000` it must reproduce the published aggregate count `10553` from OEIS A052486. It also prints exact counts by number of distinct prime factors and the subcounts having the principal signature.

The verifier does not establish an infinite asymptotic, does not certify literature originality, and is not a substitute for the symbolic remainder estimates.
