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

The attached `artifacts/verify.py` uses the standard Python library alone. From the 16 binary vertices it reproduces the 32 graph edges, 208 independent triples and 64,670 nonempty simplices, including all 208 facets. It constructs the complete oriented Hasse diagram (513,248 covers), exhaustively topologically sorts its 64,670 nodes, and finds 32,270 matching pairs with one critical vertex and 129 critical ten-simplices. All face vectors, stage counts, four-cycle counts and dual Euler computations are asserted in the checker. It enumerates all 384 automorphisms and independently compares every class trace using both the total-cut complex and its small Alexander dual. `VERIFY_OK` indicates every finite assertion was met.

The matching and trace calculations are exhaustive for this one graph. They do not prove a uniform result for all hypercubes, determine a canonical equivariant basis, or constitute a separate independent review.
