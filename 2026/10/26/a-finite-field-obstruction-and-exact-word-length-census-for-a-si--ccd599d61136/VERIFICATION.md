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

The standalone verifier uses only the Python standard library. It enumerates all 81 elements of the algebra, derives all eight idempotents, performs breadth-first closure under every right idempotent multiplication, stores and replays a minimal word for every reachable element, and asserts the nine-element complement and the exact word-length counts. The structural obstruction for the eight pure vectors and the scalar obstruction for \(2\mathbf1\) are also proved in `RESULT.md`. Scope is limited to this finite algebra; no independent audit or external certification is claimed.
