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

# Reproducibility and limits

From the directory containing `verify_full.py`, run `python3 verify_full.py`. The checker uses Python 3 standard-library modules only; no downloaded data files or external solvers are needed. It builds candidate simple labeled graphs, determines distances from adjacency without using the theorem, exhaustively scans vertex-color assignments, and searches all canonical set partitions for the broadcast condition. It then separately constructs the independent-set and inclusion-maximal-independent-set size counts and verifies each predicted integer coefficient value \(F_{G,k}(t)\).

The recorded output is embedded as `verification_output.txt` and states: PASS for \(65\) graph instances, \(1,594\) evaluations and \(440,702\) raw vertex-color assignments. Every qualifying labeled graph on orders \(2\) through \(4\) is covered; order \(5\) uses a deterministic subset of \(34\) diameter-two labeled graphs, so it is not an exhaustive order-five census. The script tests \(t\in\{1,\ldots,n+1\}\) and every \(k\in\{1,\ldots,n\}\) for each graph. Running the verifier is a finite reproducibility check, not a proof for unbounded order, a certification of novelty, or an independent scientific audit.

The infinite theorem relies on the explicit rootless-block lemma, exact injective-counting decomposition, and formal falling-factorial coefficient comparison proved in `RESULT.md`. The full motivating preprint is not available in this package and was not completely inspected; no stronger originality assurance is asserted.
