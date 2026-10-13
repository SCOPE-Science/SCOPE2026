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

The package includes `verify.py`, which uses exact rational arithmetic to reproduce the minimal PCOMR counterexample and to test the structural grade-gap invariant on an independent nonstationary example.

The critical checks are:

1. the characteristic mapping satisfies the multichoice normalization \(H(0)=0\);
2. the initial vector satisfies every PCOMR equation;
3. the EAIE coordinates from Definition 2.1 are exactly zero in the witness;
4. the two top-grade excesses are exactly equal, hence Definition 4.2 makes every coordinate stationary for any admissible learning rate;
5. the stationary point is distinct from the EAIE;
6. in a separate rational example, \(x_{m,k}-x_{m,d_m}\) is unchanged by one correction step for every lower grade.

No floating-point approximation, exhaustive search, or external certificate is used. The checker does not attempt to validate unrelated theorems in the source or any prior record.
