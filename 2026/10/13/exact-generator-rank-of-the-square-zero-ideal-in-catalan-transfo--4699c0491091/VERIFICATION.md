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

## Reproduction
Run `python3 checker.py` in the directory containing the embedded files. Successful execution prints `VERIFY_OK`. The checker directly constructs all Catalan maps for \(3\le n\le8\), filters the square-zero maps, composes every pair, and compares with the factorization criterion. For \(9\le n\le11\) it enumerates the square-zero maps using an independently constructed suffix parametrization and checks all pairwise products. The binomial count and integer recurrence are compared across these cases and beyond. Python 3 standard library only.

## Proof versus computation
The general theorem uses the explicit two-factor factorization proof, combinatorial count, formal generating functions, and nilpotent semigroup argument in `RESULT.md`. Finite enumeration cannot establish the claim for infinitely many sizes. No external audit has been performed. The novelty comparison leaves the unavailable 2023 dissertation and partial publisher previews as residual bibliographic risks.
