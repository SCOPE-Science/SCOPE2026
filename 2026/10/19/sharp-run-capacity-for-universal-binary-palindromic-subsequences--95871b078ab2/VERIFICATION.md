---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In any subsequence embedding, the host-run indices of the first positions of successive pattern runs strictly increase. Equality of total run counts forces the first letters to agree. For odd k the two alternating palindromes have k runs and opposite first letters; for even k, reflecting an alternating half gives k−1 runs (only the middle pair merges), again with both first letters possible. The resulting lower bound is 2 ceil(k/2), including k=1,2. For (0011)^m, deleting the initial 0 gives 01(10 01)^(m−1) and a residual 1, and deleting the final 1 gives 001(10 01)^(m−1); these each have 2m−1 complete binary blocks. Appending 01 for the odd witness adds one complete block to the corresponding truncated decompositions, leaving only the same possible residual 1. The k=1 endpoint check requires zero blocks. Such blocks embed the remaining k−1 symbols individually, because a palindrome can use the initial 0 or the final 1 according to its common endpoint letter. The witnesses have the stated runs and length 2k, which is necessary by the two constant palindromes. Inverting the run bound gives capacity at most 2 floor(r/2); for odd r>1, appending 0 to the preceding even-run witness adds exactly one run. Constant words give capacity zero at r=1. For unrestricted universality the two alternating patterns need k+1 runs; k+1 alternating host runs of length k realize any pattern by assigning its first run to host run 1 or 2 and successive runs in order.

## originality

PASS

Credit the sharp arbitrary-host run minimum and its simultaneous attainment with the shortest length, not the arch lemma or the separate 2k minimum. The strongest inspected overlap is an exact census of shortest hosts in the identical palindrome-subsequence class, refined by ordinary arch index, not by runs; the supported distinct result is the uniform run extremum and fixed-run capacity.

## value

PASS

Runs measure the number of alternating blocks needed to realize a universal host independently of its length. The exact even-order saving despite retaining all constant and maximal-run palindromes, along with simultaneous shortest length, quantifies what restricting the test language buys. This is a structural extremum for all orders, not a new proof of the standard arch lemma or merely a shortest-length tally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
