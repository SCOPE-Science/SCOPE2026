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

# Reproducibility

Run `python3 VERIFY.py` using Python 3 and its standard library. The program reconstructs the complete two-subset vertex set, Kneser disjointness adjacency, signed Roman inequalities and label-two defenders for all integer orders 12 through 20. It also cross-checks closed-neighborhood identities and defender conditions for orders 21 through 40. Its success marker is `VERIFY_OK`. These checks are finite and the proof for every integer order at least twelve is in `RESULT.md`. No independent audit has been performed. The unresolved even-order minimum is explicitly not asserted as exact.
