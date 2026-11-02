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

The standalone `verify.py` enumerates the complete 84-triple determinant set for the nine branch-line coefficients. It checks a rank-six unit minor of the integral magic-sum relation matrix, the exact triple-intersection profiles (eight generically, twelve in characteristic three), pair-incidence totals, the 32-to-one lift over each triple point, and the order and transitivity of the 432 affine permutations.

It does not establish irreducibility merely by enumeration. The proof of irreducibility uses independent valuations of eight rational functions modulo squares and finite flatness. The analytic-local ordinary-double-point type follows from the nondegenerate quadratic equation for each triple branch crossing, valid because the characteristic is odd. No characteristic-two claim is made.

Expected command and output:

`python3 verify.py`

`VERIFY_OK: 84 integer triples; 8/12 branch triples; 256/384 nodes; affine group 432; monomial subgroup 110592`

Only self-review of the presented work has taken place. Independent audit and external validation have not been performed.
