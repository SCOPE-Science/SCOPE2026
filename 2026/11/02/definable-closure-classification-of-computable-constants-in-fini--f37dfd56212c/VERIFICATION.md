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

The finite checker `checker.py`, run with Python 3's standard library, returned:

`ALL_CHECKS_OK pure_sizes=1..6 directed_binary_models=530 undirected_4_models=64 finite_event_instances=490`

The proof of the result has four independent steps: the effective search for uniquely definable constants, the finite-group orbit/definability correspondence, the measurable fiberwise automorphism with a noncomputable-measure event, and the pure-set stabilizer calculation. The checker corroborates only finite group and event identities; it does not prove noncomputability or any infinite computable-presentation assertion. An independent audit has not been performed.
