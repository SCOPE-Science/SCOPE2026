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

# Reproduction and mathematical scope
Execute `python3 verify_petersen_independence.py` with Python 3 and its standard library. Its independent generation of the Petersen graph as disjoint two-subsets gives 261 and 381 augmented faces at cutoffs two and three. It checks all 870 and 1350 oriented Hasse incidences, all 130 and 187 matched pairs, complete acyclicity, signed integral Morse boundary matrices, and the exact boundary/projections of the 25-simplex integral cycle. The resulting inclusion coefficient is +1. `verification_output.txt` records the actual execution.

The proof of homotopy type uses standard discrete-Morse equivalence and cellular cancellation after the verified exact integer matrices. Complete finite enumeration is rigorous here because the underlying graph has only ten vertices. The checker does not establish novelty, generalized behavior, or independent verification.
