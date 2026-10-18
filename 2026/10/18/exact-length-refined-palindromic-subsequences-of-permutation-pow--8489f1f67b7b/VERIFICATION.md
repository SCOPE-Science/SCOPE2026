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

The complete proof is in `RESULT.md`. Running `python3 check_spectrum.py` with the standard library produces the embedded `verification_output.txt`. It passed all exhaustive position-subsequence tests for 17 small parameter cells, all letter permutations in nine test classes, and independent interval-DP versus closed-form and recurrence comparisons for 138 additional cells. The output terminates with `ALL_CHECKS_PASSED 17 brute force base cases, 9 relabeling classes, 138 independent interval-DP cases`.

The independent interval recurrence adds `1` for a single central letter, `1` for a doubled central letter when both ends occur, and recursively counts inner palindromes using the first and last occurrence of the same letter; this verifies **distinct words**, not embeddings. The proof of all parameter values relies instead on the exact greedy-period lemma and its mirrored-adjacency count. No code run can rule out equivalent unpublished research. An independent scientific audit has not been performed.
