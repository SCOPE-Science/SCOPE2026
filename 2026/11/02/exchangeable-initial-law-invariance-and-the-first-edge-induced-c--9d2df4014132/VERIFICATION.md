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

# Reproducibility checks

The independent-rate-one-clock voter model's transient generator satisfies the first-step equations reproduced in RESULT.md. The proof of the four-site affine identity uses the coalescing-walk genealogy, hypergeometric initial-state probabilities, and the fact that the first backward coalescence time is exponential with rate four.

Execute `python3 verify.py` in the directory containing the package. Python 3.9 or newer is sufficient; the script uses only the standard library. It enumerates all 64 four-vertex simple graphs, selects all 38 connected labeled graphs, reduces them to six isomorphism classes using all permutations, solves the 14-state transient system over rational numbers for each, and compares exact averages and single-edge increments. It also checks all connected labeled three-vertex graphs and their nontrivial conditional expected times.

Observed reproducible checks on the supplied program: all exact rational equations solved; all 38 four-site conditional identities matched; six isomorphism classes and six single-edge transition types matched; both and only both positive increments reproduced; three-site comparison equality verified. No floating-point calculation supports the theorem. The code tests finitely many unweighted undirected graphs: general weighted-directed universality relies on the analytical proof and was not separately certified by finite enumeration.

Independent audit has not been performed. The historical-priority assessment is limited to the cited source materials and explicit scholarly comparisons, not a global uniqueness guarantee.
