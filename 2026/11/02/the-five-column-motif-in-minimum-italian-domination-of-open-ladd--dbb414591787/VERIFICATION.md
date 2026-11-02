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

# Reproducible certificate

The standalone `verify.py` uses only Python's standard library. Execute `python3 verify.py`. It checks the explicit nine-by-nine potential against every one of the \(729\) possible column triples, including all relevant end-column inequalities, and reconstructs the exact twelve-state, sixteen-arrow equality graph. It then matches the number of tight walks with the length-\(1,2,5\) composition recurrence for \(2\le n\le63\), independently recomputes all minimum Italian functions by unrestricted finite-state dynamic programming for \(2\le n\le60\), and exhaustively applies the original graph-neighbour rule to every ternary labelling for \(2\le n\le6\). All listed checks succeeded. The proof for every length relies on finite certificate inequalities, telescoping, and the graph decomposition, not on finite numerical extrapolation.

The verification is reproducible computational evidence and an internal consistency check, not an external independent audit. The certificate covers open two-row ladders only; it does not determine the full weight polynomial or resolve all historical-priority questions.
