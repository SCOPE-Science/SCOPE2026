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

# Reproducible verification

Run `python3 verify.py` (Python 3 standard library only) in this directory; expected output is in `verify_output.txt`.

The checker independently constructs induced subgraphs by graph adjacency and breadth-first component search, rather than using the theorem's shortcut for the original membership predicate. It tests the exact equivalent support rule on all vertex subsets for each finite graph, constructs the tier simplicial model from the maximum-tier face rule, and verifies every dominated-vertex coface extension before deletion. It then verifies that the remaining faces are exactly the appropriate simplex skeleton and calculates the full reduced mod-two Betti vector directly by bitset Gaussian elimination on simplicial boundaries.

As an independent algebraic cross-check, it traverses every within-part group element for the test configurations, computes the signed permutation trace on each simplicial chain group of the original complex, uses the independently known nonequivariant one-degree homology concentration, and checks that the averaged top-homology trace is the predicted sphere rank of the orbit quotient.

Output: `VERIFY_OK parameter_cases=203 original_accepted_faces_including_empty=7013 tier_nonempty_faces=4353 dominated_coface_checks=1482 group_elements_checked=3557`.

**Limits.** Checks cover two and three parts of sizes at most three, and four parts of sizes at most two, with threshold up to four and at most the total number of vertices. Mod-two homology is not an integral homotopy certificate. The proof in RESULT.md is the general, integral argument; no infinite conclusion is drawn from finite enumeration. No independent audit has occurred.
