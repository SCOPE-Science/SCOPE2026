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

## Reproducible checks

Run `python verify.py` with Python 3 and SymPy in a directory containing this file. `VERIFY_OK` means that the code successfully checked a symbolic factor identity and independent exact rational orbit computations; it does not constitute a separate external audit.

The exact verifier derives every 3-cycle with two independent methods, checks the six permutations on 55 positive-product, strictly increasing rational triples, confirms the strict sign and factorization, and reproduces a concrete rational example. Symbolic simplification verifies the numerator identity with no floating-point approximation. Large-parameter rational examples also check the predicted ratio scaling, while the proof in `RESULT.md` establishes its asymptotic limit for all real parameters along the specified family.

## Limitations

Finite samples by themselves would not prove a universal sign; the mathematical proof is the explicit factorization in `RESULT.md`. Only the exact claims listed there are assessed. The source comparison does not rule out an inaccessible or unindexed equivalent theorem. Independent audit remains unperformed.
