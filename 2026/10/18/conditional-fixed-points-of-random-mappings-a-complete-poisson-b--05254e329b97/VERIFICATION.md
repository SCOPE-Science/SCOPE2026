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

Run `python verify_fixedpoint_profiles.py` with Python 3. The script uses only the standard library. It enumerates all \(50{,}069\) functions over \(1\le n\le6\), groups them by labelled indegree vectors, and verifies the complete conditional probability distribution and all factorial moments by exact rational arithmetic. It also checks the conditional variance and four representative asymptotic factorial-moment profiles numerically, without claiming to prove the limiting theorem by computation.

## Mathematical verification boundary

The infinite statements follow from the proof in `RESULT.md`: conditional multiset sampling without replacement, uniform factorial-moment domination, compact convergence of the normalized-degree generating product, total-variation convergence, the variance-based converse, and explicit construction of all limit profiles. Numerical checks are not substitutes for those arguments. The literature comparison remains subject to incomplete access to the relevant 1990 random-mapping preprint and 2026 multiset-permutation preprint.
