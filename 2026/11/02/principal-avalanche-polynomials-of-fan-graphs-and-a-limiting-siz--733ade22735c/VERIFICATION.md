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

# Reproduction and limits

The following two supplied, standalone code artifacts use Python and SymPy. Run them from the extracted package root, for example `python checks/direct_burning.py` and `python checks/transfer_identity.py`.

`checks/direct_burning.py` enumerates all stable path-height configurations and all possible addition sites for \(2\le n\le9\). It uses an independent sink-burning test and a direct discrete stabilization, and matches every avalanche-polynomial coefficient from the generating function. Its success marker is `DIRECT_BURNING_STABILIZATION_PASS`.

`checks/transfer_identity.py` constructs the full exact rational transfer matrices for the marked maximal saturated run and symbolically verifies both the marked-run and avalanche generating functions, as well as recurrent-count normalization. Its success marker is `EXACT_TRANSFER_MATRIX_IDENTITY_PASS`.

The exact algebraic calculation certifies the stated rational identity for the implemented finite-state transition system. Its interpretation for arbitrary path length relies on the combinatorial proof of the recurrent-word condition and saturated-run lemma in `RESULT.md`. Exhaustive enumeration through size nine is supporting evidence, not an infinite proof. No independent scholarly audit was performed.
