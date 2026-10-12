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

# Reproducibility of the pentagon–cycle equality census

Run `python3 artifacts/verify.py` from the result directory. No nonstandard packages are required. The verifier tests all independent one-column masks of the five-cycle (eleven masks), builds the exact compatibility relation across adjacent second-coordinate columns, and counts cyclic compatible assignments using integer transfer aggregation. It checks the coefficient for code size \(n\) against the closed binomial expression for each integer \(4\le n\le22\), and also compares with independent exhaustive cyclic state-list enumeration for \(4\le n\le8\). In those brute-force checks, the maximum cardinality is found to be \(n\). It exits with `VERIFY_OK` only when all equalities hold.

Additionally, `python3 artifacts/check_graph.py` directly constructs the full confusability graph from modular vertex pairs and enumerates maximal cliques in its complement for \(6\le n\le9\). It reports counts \(350,70,1600,360\) and ends with `GRAPH_VERIFY_OK`; this does not use the column-mask transition construction.

These finite tests do not prove the formula at untested values. The all-length proof is the zero/double-column counting argument, equality shift-by-two rigidity, and the resulting explicit bijection from maximum codes to either five-cycle closed walks or independent-pair assignments. In particular the unbounded statement does not rely on any numerical extrapolation, heuristic search, or external certificate. The complete Hales (1973), Sonnemann–Krafft (1974), and Vesel (1998) texts were not accessible during the literature comparison, leaving bibliographic—not mathematical—uncertainty.
