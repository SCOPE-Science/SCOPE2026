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

# Verification and reproducibility

Run `python3 check.py` in this directory. The script enumerates idempotent matrices commuting with the specified Alexander operator, counts all translations in their kernels, and compares image dimensions with independently evaluated elementary-divisor formulas; nine cases pass. Three additional exact-image enumerations verify that every image of a specified cardinality receives the predicted number of retractions. It also checks the quandle homomorphism equation for every set map on two small connected quandles; two cases pass. The expected marker is `ALL_EXACT_CHECKS_PASSED 9 linear cases + 3 image-fiber cases + 2 full quandle cases`.

These finite enumerations do not establish the general formulas. The proof in `RESULT.md` provides the all-dimensional affine-map lemma, invariant-factor splitting, automorphism count and per-image complement-graph classification. The computations use exact modular integer arithmetic and rational integer products, without external libraries. Independent mathematical validation was not performed.
