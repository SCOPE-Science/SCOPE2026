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

The identities in the accompanying standard-library Python checker have been executed successfully. It verifies polynomial expansions, root separability criteria, section identities, and lattice rank/index arithmetic. The generic Mordell–Weil rank is established mathematically by applying the Oguiso–Shioda rational elliptic surface classification and the explicit field elimination; no finite enumeration is treated as proof of a rank upper bound. The section intersections use a regular local chart over infinity, and the intersection-height formula is stated in the proof.

To reproduce the arithmetic part from this directory: `python3 artifacts/verify.py`.

The exact-rank assertion is over the generic coefficient field, not every complex specialization. Independent audit has not been performed.
