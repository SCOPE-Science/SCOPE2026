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

Run `python3 verify.py` using Python 3.9 or later; only standard-library modules are used. The expected final line is `VERIFY_OK 16 exhaustive clique-cover and homology checks`. The script independently builds all cliques from metric adjacency for 16 parameter triples covering the sharp boundary and subsequent circumferences, compares against the proposed carrier decomposition and computes reduced homology by exact binary elimination. The complete mathematical proof uses an all-parameter collapse and degree-one attaching maps; the finite checks do not prove any untested instance. No independent audit or validation has been performed.
