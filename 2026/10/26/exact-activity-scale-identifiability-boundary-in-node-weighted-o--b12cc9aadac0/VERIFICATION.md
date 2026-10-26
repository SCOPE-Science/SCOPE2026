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

Run `python verify.py` with Python 3 and no third-party packages. This checks the complete enumeration of connected labeled bipartite graphs of at most six vertices by a direct weight formula and a separately conditioned edge-mixture formula. It verifies invariance for complete bipartite graphs; it produces explicit rational witnesses for noncomplete graphs using variations of a missing neighbor's weight. Additional checks test a four-vertex path, a six-cycle's exceptional balanced profile, and a nonuniformly weighted complete bipartite graph.

Observed output: `CERTIFICATE_OK: 465 exact graph/edge checks across connected bipartite graphs up to six vertices plus examples`.

The proofs for *all* graph sizes and *all* positive real weights require the algebraic mixture identity, connectedness of the edge relation, and a nonzero-polynomial argument, all presented in `RESULT.md`. The finite enumeration cannot prove those general statements. The test does not validate empirical opinion models or establish publication priority. No independent scientific audit has been performed.
