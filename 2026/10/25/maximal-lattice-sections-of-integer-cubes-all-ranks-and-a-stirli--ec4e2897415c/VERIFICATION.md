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

# Verification of the cubical maximal-section count

The complete analytic proof is contained in `RESULT.md`. In particular, the injective coordinate-projection argument, full-grid equality condition, integer-affine coefficient classification, no-double-counting signed-block rule, and Stirling-number identity establish the theorem for all integers \(d\ge2\), \(k\ge1\), and \(1\le\ell\le d-1\).

The accompanying standard-library file `verify_maximal_grid_flats.py` checks ten small triples by enumerating affine spans using exact rational reduced-row-echelon representation, comparing all distinct winning flats to the proposed formula. It also verifies 231 independent parameter identity comparisons. The successful local output ends with `CUBICAL_MAXIMAL_FLATS_OK exhaustive_cases=10 formula_identities=231`.

These finite computations do not certify the infinite parameter domain, which is proved analytically. No third-party or independent scientific validation has been performed. Historical-priority limitations are discussed in `REVIEW.md`.
