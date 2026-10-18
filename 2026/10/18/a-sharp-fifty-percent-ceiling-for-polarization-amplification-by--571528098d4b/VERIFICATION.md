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

# Verification evidence and limitations

Run `python verify.py` with Python 3 and SymPy installed. The packaged program checks exact rational graph Laplacians, a four-vertex connected witness, the formal characteristic-polynomial identity, exact mean and determinant preservation, and the six-by-six clique-moment formulas by direct inversion of twelve-by-twelve matrices for five distinct positive weights. It reports `PASS: 881 symbolic, exact rational, and finite-graph checks` on successful execution.

Critical infinite statements are supported by the proof in `RESULT.md`: spectral positivity of the resolvent, rank-one update, a two-variable polynomial certificate, and a limiting eigen-decomposition. Exact finite computations verify formulas at finitely many points and cannot alone prove the universal bound or strict inequality at every finite graph.

The literature comparison distinguishes prior single-edge change formulas from the asserted sharp uniform relative bound. Residual risk of broader unindexed equivalent results remains. This record contains only self-review; no independent audit was performed.
