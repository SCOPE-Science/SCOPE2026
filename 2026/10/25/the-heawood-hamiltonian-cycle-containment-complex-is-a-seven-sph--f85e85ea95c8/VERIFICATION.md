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

# Verification notes

Run `python heawood_hamilton_verify.py` using Python 3.9+; only the standard library is used. This executes a **complete** search of Hamiltonian cycles from a fixed root, an independent perfect-matching search, full face enumeration, an exact staged face–coface matching, and an exhaustive directed Hasse-graph acyclicity test. A successful run emits exactly the included `verification_output.txt`, ending in `VERIFY_OK`.

A mask encodes the 21 graph edges in ascending line-index then point-index order. The only critical nonempty masks are 1 (one vertex) and 674086 (eight vertices, hence a seven-cell). Acyclicity is verified by orienting matched incidences lower-to-upper and all others upper-to-lower, and checking a complete topological sort over all nonempty faces. This verifies the hypothesis of the standard discrete Morse reduction theorem. The top cell's attaching map is null because its lower skeleton is a point, so the result is a seven-sphere.

The exact full directed incidence check validates a finite complex, not an infinite parametric claim. The checker does not establish that the theorem has not been published before; originality is assessed separately and remains subject to the documented bibliographic access limits.
