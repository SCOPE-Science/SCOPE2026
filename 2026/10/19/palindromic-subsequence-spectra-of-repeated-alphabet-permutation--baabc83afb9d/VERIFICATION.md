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

# Reproduction and limits

This package includes `tools/verify.py`, a standalone Python 3 script requiring only the standard library. Run it from the extracted package root with `python tools/verify.py`.

The script constructs the complete set of distinct subsequence words of each tested repeated-permutation host by iterating over host letters and adjoining each current subsequence with that letter. This is independent of the descent-count proof and does not count duplicate positional embeddings. It filters the resulting values for palindromicity and compares their full length histogram with the claimed binomial coefficient formulas. An additional direct greedy matcher independently tests explicitly generated palindromic candidates in bounded cases, and the program repeats the direct check for 150 alphabets with all relabeling permutations in three specified parameter families.

Actual executed output:

`ALL_REPEATED_PERMUTATION_PALINDROME_CHECKS_PASSED main_pairs 21 permutations 150 q_range 2..10 k_range 1..12`

The 21 full direct-enumeration cases are \(q=2\) with \(1\le k\le7\), \(q=3\) with \(1\le k\le5\), \(q=4\) with \(1\le k\le4\), \(q=5\) with \(1\le k\le3\), and \(q=6\) with \(1\le k\le2\). Additional algebraic boundary checks cover \(2\le q\le10\) and \(1\le k\le12\). A separate symbolic coefficient expansion of the proposed bivariate rational function was compared against the explicit binomial counts for \(q=2,3,4\) and \(1\le k\le5\); it agreed in all 15 instances.

Neither full finite enumeration nor the symbolic spot checks prove the theorem for all \(q\) and \(k\). The mathematical proof is the explicit necessary-and-sufficient block criterion followed by exact halfword counting. This check does not establish bibliographic priority or independent audit status.
