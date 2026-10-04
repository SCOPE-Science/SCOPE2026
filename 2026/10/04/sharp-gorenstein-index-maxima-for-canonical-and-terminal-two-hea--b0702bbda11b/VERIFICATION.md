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

The universal statement is proved symbolically from the exact Gorenstein-index formula, the Reid--Tai parameter region, and a near-corner product/divisibility analysis.

`verify_gorenstein_index_two_heavy.py` is an independent integer-arithmetic regression check. It enumerates every canonical and terminal pair for each \(2\le r\le200\), computes the Cartier index exactly, and verifies the claimed maxima, uniqueness, and terminality of the maximizer. Its executed output is:

`VERIFY_OK r=2..200; canonical and terminal maxima, equality cases, and terminality of the maximizer agree`

The finite sweep is not used to infer the infinite theorem. Independent audit has not been performed.
