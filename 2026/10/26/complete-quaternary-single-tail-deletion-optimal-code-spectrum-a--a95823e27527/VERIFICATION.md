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

# Verification record

The attached `verify.py` constructs the deletion outputs directly for every nonempty partial permutation ending in one fixed letter, with the remaining letters distinct. It exhaustively examines all \(2^{16}=65{,}536\) possible subsets for the four-letter case and rejects each conflicting subset by direct intersection of output sets. The maximum local size is \(7\), and exactly \(54\) local codebooks attain it. Its complete optimal length-profile distribution agrees with the closed polynomial in `RESULT.md`.

A structurally separate dynamic program counts subsets by independently combining rooted subtrees with one-child-at-most constraints and compares every coefficient of the local independence polynomial against exhaustive search for alphabet sizes \(2,3,4\). The program also evaluates the recurrence at sizes \(5,6\), without claiming direct enumeration at those sizes. Independent terminal-letter components and the complete analytic equality-case classification imply the fourth-power global count; an exhaustive search of every global codebook is unnecessary and was not performed.

The verifier outputs `VERIFY_OK` after all checks. The finite checks are additional evidence for the exact arithmetic; the proof of the general recurrence and all global extremal conclusions is analytic. No independent external audit has been performed.
