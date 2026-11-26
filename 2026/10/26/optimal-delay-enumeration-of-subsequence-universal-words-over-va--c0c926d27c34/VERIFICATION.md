---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The greedy completing letters give an absent subsequence when there are too few arches. A prefix before the kth arch has exact completion deficit q(k-r)-s, so when slack is zero only missing symbols are feasible; with positive slack all are feasible. The ordered missing-symbol list and its LIFO undo preserve lexicographic child order without inspecting forbidden letters. Between complete outputs the DFS uses at most two monotone depth segments, with O(1) work per edge except at arch resets. Each reset can be charged to q letters on a path, and at most k<=n/q lists coexist; writing the word fits the O(n) bound. The k=0, q=1, n=0 and empty-family branches are consistent. The constant-time infeasibility test can compare k with floor(n/q) to avoid a large product.

## originality

PASS

The strongest directly comparable paper gives an O(nq)-delay enumerator after O(nkq) preprocessing for the same family and separately asks for O(n) delay. The frozen theorem supplies the requested explicit uniform bound, with inexpensive initialization and no rank table. The other inspected algorithms or distributions have different inputs or models and do not dominate this guarantee.

## value

PASS

This resolves a stated enumeration-delay question, reaching the linear cost of materializing a word even over growing alphabets. The simultaneous linear initialization for feasible positive k and linear memory make the result useful in the intended streaming setting; it is not a fixed-q rephrasing or an amortized-only bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
