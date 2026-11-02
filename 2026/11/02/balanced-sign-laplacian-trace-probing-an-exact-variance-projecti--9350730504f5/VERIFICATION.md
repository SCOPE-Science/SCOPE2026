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

Running `python3 verify.py` requires only the Python standard library. The archived verifier uses exact rational arithmetic and a fixed pseudo-random seed, enumerating the complete balanced-sign support for all sampled weighted graphs and exhaustively checking the 4- and 6-vertex simple-graph classes.

Observed execution result: `PASS: 3434 exact assertions; 600 random weighted graphs; 200 additive weighted graphs; exhaustive simple graphs n=4,6`.

Critical algebraic checkpoints are the balanced pair moment \(-1/(n-1)\), the distinct-index fourth moment \(3/[(n-1)(n-3)]\), the incidence Gram matrix \((n-2)I+\mathbf1\mathbf1^\top\), and the complete binary-potential rigidity step. Finite enumeration tests examples, not every dimension; the theorem's generality rests on the written proof. Independent scientific validation and external assessment have not been performed.
