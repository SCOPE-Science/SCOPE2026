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

The definitions and depth criterion are those of Đurđev–Mudrinski. Let C_0=G and C_{i+1}=G C_i ∪ C_i G. This descending sequence is exactly the set of values at depth i: a depth-(i+1) term has a child at depth i, and any value on the other side is available as a depth-zero parameter. Thus 3-nilpotence gives C_3={0}. Failure of 3-supernilpotence gives a nonzero product in (G²)²⊆C_2 by Proposition 5.3. If two consecutive stages before C_2 were equal the recursion would stabilize, so G⊋C_1⊋C_2⊋{0}; at least four elements are needed. In the displayed table the three successive sets are {0,a,b}, {0,a}, {0}, with b²=a≠0. An independent bounded check iterated all tables with absorbing 0 (base-m digits for the (m−1)² nonzero-input cells), applied the recurrence three times, and tested C_1·C_1: orders 1,2,3 give respectively 1,2,81 tables, of which 1,1,3 are 3-nilpotent and none separates. The frozen check_minimal.py was inspected, not executed; the proof does not rely on it. This is only the two commutator notions at level 3 with absorbing zero, not a classification of all optimal tables.

## originality

PASS

The strongest inspected predecessor gives the criteria and a separation construction of order eight at level three, not the sharp minimum or the order-four construction. The lower bound alone follows promptly from the prior depth criterion; the distinct claim credited is sharpness at four, witnessed by a different multiplication table. The evidence is best-of-search, not a global priority assertion.

## value

PASS

The source establishes a real distinction between the two commutator notions at the first separating level. The exact least order is a natural boundary, not an arbitrary table truncation; the four-element witness shows how repeated operands avoid the source example's eight distinct elements while retaining the nonzero balanced product. The result gives a minimal concrete test case for the difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
