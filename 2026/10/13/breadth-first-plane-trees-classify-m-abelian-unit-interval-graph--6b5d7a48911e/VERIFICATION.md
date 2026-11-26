---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The area inequalities are equivalent to 0≤p_i<i and nondecreasing p_i; these parent-index conditions give a rooted tree whose children's blocks, traversed by queue in increasing parent order, yield exactly labels 0,…,n. Conversely breadth-first labelling yields those conditions and hence the unique area sequence. The earlier nonneighbors of i are exactly 1,…,p_i, so the maximum independent size ending at i is 1+max_{0≤j≤p_i} b_j, with b_0=0. The nested prefixes make b_i nondecreasing, giving b_i=1+b_{p_i} and equality with the breadth-first depth. The greedy partition starting each next block at the first vertex t with p_t≥ the previous start indeed has clique blocks; its starts form an independent set, giving a matching certificate of optimality without a connectedness assumption. The bounded-height plane-tree recurrence H_h=1/(1−zH_{h−1}), H_0=1, gives the stated continuants. For m=1,2,3, the positive-degree coefficients follow by recurrence/partial fractions, with the third denominator (1−z)(1−3z) and the second the odd Fibonacci recurrence. n=0 is used only as the height-zero generating-function seed. The height claim concerns the contour of the new tree, not the original area-sequence path or an unlabeled graph class. Own replay: python3 /workspace/review_replay.py 1, enumerating the area sequences from Dyck words, independently counting all consecutive cut choices and independent subsets, and checking that the image equals the separately enumerated plane trees through n=7. The supplied script and saved transcript through n=9 were inspected but not executed. Nonmaterial environment note: int.bit_count() requires Python ≥3.10, not 3.8 as stated in the frozen replay instructions.

## originality

PASS

No credit is assigned to the Catalan/plane-tree bijection in isolation, the bounded-height enumerator, or the m=1 graph count. The distinct assertion in the original finding is that this explicit breadth-first construction transports two graph invariants to tree height and therefore gives uniform unweighted enumeration in Alexandersson–Leite's ordered m-Abelian classes. Neither the prior weighted bounce definition nor the inspected proper-interval/canonical Dyck encodings state that identity; the precise relation to bounce-composition length is recorded below.

## value

PASS

This gives the unweighted cardinality of a recently defined ordered graph family for all m and identifies exactly which graph invariant becomes height under the map. The equality with optimal consecutive clique partition also supplies an explicit witness, not merely a count. It recovers a known boundary case and makes the unweighted count accessible to standard height methods, without claiming progress on the weighted peak questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
