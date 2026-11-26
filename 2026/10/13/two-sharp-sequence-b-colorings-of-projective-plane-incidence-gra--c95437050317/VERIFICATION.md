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

I recomputed the incidence graph and tested every supplied color and every vertex with a separate checker, python /workspace/checks/4.py <frozen certificates.json>. For F4 the nonzero labels were multiplied as powers of a generator of order three and added by XOR. The reconstructed graphs have (26,52) and (42,105) vertices and edges, all degrees 4 and 5 respectively, no color conflicts, and exactly the stated dominating-vertex pairs in each color. Any dominating vertex in a proper k-coloring needs k-1 neighbors, proving the matching upper bound. Each pair of points has exactly one common line, excluding 4-cycles; example 6-cycles from the check are [0,17,1,13,4,14] and [0,26,1,21,5,22] in the respective labelings. The two-sided breadth-two expansion from an edge in a d-regular girth-six graph gives the order bound 2(1+(d-1)+(d-1)^2), attained here. This checks these two instances only, not all colorings or field orders.

## originality

PASS

The two explicitly certified sharp instances are supported as distinct after full-text inspection of the motivating paper and statement-level comparison of the closest indexed results. The broad property is conjectured already, and its definition and degree bound are not new.

## value

PASS

These are minimum-order regular degree-four and degree-five girth-six examples, at the first degrees outside the known cubic case. The explicit proper colorings attain the degree bound with two dominating vertices per color, settling the motivating conjecture on two structurally natural boundary instances. The certificates are useful benchmarks and do not assert a general girth-six theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
