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
# Verification

`python3 verify.py` uses only Python's standard library. It enumerates all switching/complement bit configurations that fix the graph induced by the individually named base, and all resulting orbits on binary adjacency vectors, for base sizes 0–7. It independently tests finite full edge-action profiles on tuples of lengths 1–5. It confirms exact small cases, the strict three-parameter profile separation, and tail equalities on 2–99. The saved execution transcript ends `ALL_CHECKS_PASS`. The unrestricted result is established in `RESULT.md` by the symbolic finite-field orbit argument and the Rado graph's extension and homogeneity properties, not by the bounded experiments.

No independent audit has been carried out. The closest original 1991 paper was not available in full text, so overlap with uninspected material remains possible.
