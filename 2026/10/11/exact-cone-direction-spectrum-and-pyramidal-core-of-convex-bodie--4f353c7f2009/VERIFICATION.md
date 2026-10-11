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

# Verification and scope

The analytic proof checks all integer dimensions \(n\ge2\) and every full-dimensional compact convex body: the extreme-point hyperplane property, isolation of each affine apex, independence of normals after locating a residual extreme point, full dimension of the common-base section, exclusion of the two forbidden counts, and all cross-polytopal witness bodies. These are proofs in ordinary finite-dimensional convexity and do not require a machine computation.

`verify_cones.py` uses exact SymPy matrix ranks to check the prescribed witness polytopes for every \(2\le n\le8\), each \(0\le k\le n-2\), and one simplex in each such dimension. It executes 35 exact integer-rank test cases and returns `VERIFY_OK exact_integer_rank_cases=35`. This finite check is not an exhaustive test of arbitrary convex bodies or dimensions.

The arXiv first-public-version stamp establishes the August 5, 2026 reference date. The cited discussion of multifold pyramids was inspected in the primary paper, but an exhaustive historical priority determination is impossible; possible unindexed equivalent arguments remain a risk. Independent audit and independent validation have not been performed.
