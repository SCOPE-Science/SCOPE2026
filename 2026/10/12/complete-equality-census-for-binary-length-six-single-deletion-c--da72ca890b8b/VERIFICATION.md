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

The bundled `verify.py` is a standalone Python standard-library replay. It rebuilds the length-six binary one-deletion shadows from the definition, constructs the compatibility graph, and enumerates every maximal clique by an exact Bron--Kerbosch recursion with pivoting. It then directly checks each maximum code, the four explicit complement/reversal symmetries, the seven VT syndrome-class sizes, the uniqueness of the maximum VT class, and the common intersection.

Expected key output: `VERIFY_OK`, `maximum 10`, `maximum_codes 9`, `orbit_sizes 1,1,1,2,2,2`, `vt_sizes 10,9,9,9,9,9,9`, `vt_maximum_codes 1`, and census SHA-256 `082cb965d2fdf3639d1e269042c7b0beb4c6fc31317c3158df3d0ef89093582b`.

Limit: this verifies only the finite binary length-six claim. It does not establish any statement for other lengths or identify the full automorphism group of the deletion-confusability graph.
