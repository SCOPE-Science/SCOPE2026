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

# Reproduction and boundaries

Run `python3 check_permutation_evolution.py` using Python 3.9 or later; only the standard library is needed. The expected terminal marker is `CHECKER_OK`. The program works with exponent representatives for the cyclic multiplicative group of \(\mathbf F_q\). This is sufficient because each tested structure constant, monomial change-of-basis factor, and idempotent coordinate appears only in products and powers; field addition is never used in these comparisons.

The script independently enumerates monomial transformation orbits of complete spaces of labeled weighted permutations for \((q,n)=(2,1),(3,1),(3,2),(4,2),(5,2),(7,2),(4,3),(5,3),(7,3),(8,3),(4,4),(5,4)\). For all structures at \((q,n)=(3,2),(4,2),(5,3),(7,3),(8,3)\), it independently enumerates all monomial automorphisms and all solutions of \(x^2=x\) and compares them with the theoretical formulas. No finite enumeration certifies every dimension; completeness beyond these cases comes from the arguments in `RESULT.md`.

The source study examined the relevant portions of the 2013, 2022 and 2023 full texts, including their normalization, automorphism, orbit-action, and low-dimensional-count theorems. The 2020 two-permutation preprint was only available by abstract at review time. Independent audit remains unperformed.
