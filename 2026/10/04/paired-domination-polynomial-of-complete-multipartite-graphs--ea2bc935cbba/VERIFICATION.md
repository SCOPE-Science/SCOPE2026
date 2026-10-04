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
# Verification

The proof is symbolic. The packaged `verify.py` is an independent finite regression check. It enumerates every sorted positive part-size tuple of total order at most 9 with at least two parts, constructs the corresponding complete multipartite graph, and tests every vertex subset. For each subset it checks domination directly and perfect matching by recursive exact search, then compares the outcome with the theorem's balance criterion. It also compares brute-force coefficient counts with the closed coefficient formula, checks the exact support endpoint, and verifies that the quadratic coefficient equals the number of edges.

Finite enumeration does not establish the infinite theorem; it checks boundary cases and is intended to catch parity, support, matching, and overload-counting errors.
