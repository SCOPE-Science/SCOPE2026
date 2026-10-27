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

# Finite checks and proof boundaries

The self-contained `verify.py` script uses only the Python standard library. Run it with `python3 verify.py` to check every order \(6\le n\le20\). It constructs graph adjacency from the four cyclic step neighbors and computes all distances using breadth-first search; for each unordered pair it separately checks all potential strong resolvers by the geodesic equality. It constructs the mutual-maximal-distance graph directly, enumerates all selected subsets of the predicted minimum cardinality and verifies equality with the explicit basis families. For orders \(6\le n\le15\) it also independently rejects all smaller sizes using the geodesic test.

The script reconstructs one-replacement adjacency for the actual minimum bases and verifies its number of vertices, degree sequence, edge count, connectedness, and exact graph diameter. Orders \(6,10,14,18\) verify the perfect-matching/transversal-to-hypercube cases; the other eleven orders verify cycle exchange graphs. The program prints `ALL_VERIFY_OK` only if every comparison succeeds.

The infinite assertion is mathematical and rests on the general strong-resolving-graph equivalence, cyclic-distance analysis, exhaustive independent-set structure proofs and direct one-replacement comparisons in `RESULT.md`. Finite enumeration alone does not certify arbitrary larger orders. No independent audit or external verification is asserted.
