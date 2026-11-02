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

The standalone `verify.py` was run in the same directory as the mathematical result. It returned:

`VERIFY_OK digit_cells=373 direct_vs_digits=4095 exact_group_counts=33 index_congruences=600 group_order_13=144 determinant=-37`

The finite checks evaluate all one-digit argument tables for primes \(3,5,7,11,13\), enumerate the generated finite groups, verify the base-13 primitive-root matrix, directly compare \(4095\) coefficient-sum and digit-factor evaluations, compare \(33\) exact multinomial counts with a separate \(12\times12\) dynamic program, and check \(600\) indices against every argument modulo \(13\).

The exact character asymptotic and all-index criterion rely on the proof in `RESULT.md`, not on the finite checks. This record contains no independent validation.
