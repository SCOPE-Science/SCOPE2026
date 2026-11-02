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

The actual standalone program is `checks/verify.py`, which uses only Python 3 standard-library modules. Run it by executing `python3 checks/verify.py` from the package root. The observed terminal line was `VERIFY_OK`.

The checker independently generates every binary palindrome and deletion descendant at half-lengths \(1\le m\le8\). It compares all pairs' shadow intersections to the predicted alternating-tail graph, verifies odd-graph tree connectedness and edge counts, computes optimal independent-set sizes and counts via a rooted-tree recursion, and checks against the closed formula. The even palindromes are verified to have no conflicting pair at all tested lengths. A direct codebook enumeration through \(m=4\) verifies all maximum-codebook counts without the tree dynamic program.

Recorded odd-length optimal code sizes for \(m=1,2,3,4,5,6,7,8\): `1, 2, 4, 8, 16, 32, 64, 128`.

Recorded corresponding maximum-codebook counts: `2, 3, 8, 60, 3456, 11612160, 132090377011200, 17175244766164688547348480000`.

These checks are finite and cannot establish an all-length claim by themselves. The all-length justification is the deletion-alignment lemma, the recursive graph isomorphism, the perfect-matching bound, the bipartition construction, and the optimizer-count induction in `RESULT.md`. The proof does not require a numerical optimizer, external package or third-party file.
