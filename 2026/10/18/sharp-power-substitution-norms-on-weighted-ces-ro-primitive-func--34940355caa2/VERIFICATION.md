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

The included `verify.py` is stand-alone, using only Python's standard library. It verifies exact rational integral identities for the lower-support functions at two natural weight endpoints, computes quadrature upper bounds for several interval probes, checks asymptotically sharp norm ratios at the right endpoint, and checks growth for left-endpoint probes on the unbounded side.

To run: `python3 verify.py`.

The full theorem is proved by the pointwise change-of-variable estimate, the right-endpoint asymptotic, and three explicit regimes for the left-endpoint test integral. Numerical checks cannot replace these arguments. No independent mathematical audit has been performed.
