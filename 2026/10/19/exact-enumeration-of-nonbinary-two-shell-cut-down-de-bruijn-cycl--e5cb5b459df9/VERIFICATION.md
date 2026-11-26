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

For m=n−1 and r=q−1 the exact overlap graph is balanced with degrees r, q, and 1 on weights 0,1,2. Zero appends lead to the root from every vertex, hence by balance every nonisolated vertex belongs to one strongly connected component. Each rotation class has a unique Euler edge sequence beginning at the labelled edge 0^m1, so the fixed-first-edge BEST count has no extra division. Each weight-two vertex's outgoing choice is forced and its zero path reaches a one-color vertex. On deleting the root row and column, elimination along these paths preserves the tree count: one-color index i can shift forward with its color unchanged or reflect to m−1−i in any of r colors. The operator on zero-sum colors is a triangular shift with diagonal q in each of q−2 directions; the constant-color block is the reflected index tree operator with weights 1 and r. Any reflected choice at i≥floor(m/2) traps the closed interval [m−1−i,i]; all assignments reflecting only at lower indices strictly progress to the root. Thus the remaining determinant is q^floor(m/2). This includes m=1, where colored self-loops must be subtracted and the index block determinant is 1. Combining the determinant and BEST gives the stated product. The number of distinct windows is n(q−1)+C(n,2)(q−1)² and a shorter period would repeat a window. Fresh depth-first enumeration by unused labelled windows independently matches 12, 432, 5184, 6912 at the four stated pairs; finite checks supplement the proof.

## originality

PASS

On available evidence the distinct claim is the nonbinary all-span count, not existence or the binary specialization. The later, strongly overlapping ≤2 enumeration is explicitly related by the zero-loop factor; this near equivalence is not evidence that it preceded the frozen finding.

## value

PASS

After known existence, the enumeration of every cycle in the first genuinely nonbinary low-shell family is a natural additional invariant. The uniform factorial and exponential factors distinguish labelled outgoing orders from the colored tree obstruction over all spans and alphabets; obtaining them requires a graph-specific evaluation, not just applying an existence theorem or a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
