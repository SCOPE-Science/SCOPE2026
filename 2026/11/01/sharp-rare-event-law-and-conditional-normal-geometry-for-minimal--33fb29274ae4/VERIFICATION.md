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

Execute `python VERIFY.py` using the Python standard library. The code checks the exact Dirichlet and gamma mixture moments as rational identities across 43 values of the auxiliary dimension, enumerates cube edges and checks minimal-vertex/dominance equivalence on seeded generic directions, and numerically corroborates the probability factor and conditional residual coordinate behavior using independent importance sampling. The successful observed marker is `ALL_RARE_MINIMAL_CUBE_SECTION_CHECKS_PASSED`.

The proof of the infinite-dimensional statements and the two-term asymptotic appears in `RESULT.md`; finite checks alone cannot establish the full claim. Absolute probability checks directly include dimension four, where the known exact probability is \(1/3\). The source-level historical comparison is limited by the unavailable full text of arXiv:2510.09265; published novelty is not independently certified.
