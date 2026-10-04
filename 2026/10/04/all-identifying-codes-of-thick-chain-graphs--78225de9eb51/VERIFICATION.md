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

The packaged `verify.py` was executed after its final bytes were written. It constructs chain graphs using adjacency \(A_iB_j\) exactly when \(j\le i\), checks every subset against the closed-neighborhood identifying-code definition, and compares the result with the theorem and coefficient formula.

Replay command: `python verify.py`

Observed output: `VERIFY_OK profiles=58 subset_checks=323488 coefficient_checks=650 max_order=14`

The checked profiles use \(p\le3\), class sizes in \(\{2,3\}\), total order at most \(14\), plus complete-bipartite profiles \(K_{a,b}\) with \(2\le a,b\le5\) and order at most \(12\). This is finite corroboration only; the infinite statement rests on the proof in `RESULT.md`.
