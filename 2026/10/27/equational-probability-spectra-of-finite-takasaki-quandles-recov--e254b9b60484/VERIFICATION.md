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

# Reproducible verification and limits

Run `python verify.py` with Python 3.9+ and no third-party dependencies. The actual completed output ended `VERIFY_OK 15` and listed every tested direct-product group and its order, spectrum size, and exponent.

For each tested group the script: (1) computes the closure of binary-term first coefficients under \(2b-a\) modulo the group exponent and checks that every residue occurs; (2) directly evaluates every ordered pair of generated two-variable term functions on every ordered pair of group elements, checking the claimed torsion-cardinality probability; (3) compares the resulting set with the claimed spectrum; and (4) reconstructs prime-power cyclic multiplicities from the unordered spectrum. Tests included cyclic orders 2, 3, 4, 6, 8 and 9; elementary groups; mixed groups; and distinct groups of the same order.

The infinite-family theorem rests on the affine-term induction, Bézout image calculation, two-variable coefficient generation, and elementary-divisor reconstruction in `RESULT.md`. No exhaustive enumeration of arbitrary-arity terms is asserted. No independent mathematical audit has been performed.
