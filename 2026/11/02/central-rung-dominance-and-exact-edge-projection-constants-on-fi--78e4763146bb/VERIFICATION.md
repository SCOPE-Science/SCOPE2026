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

The mathematical proof is in `RESULT.md`. The independent-from-the-proof finite implementation `verify_ladder.py` uses rational inversion of the grounded full-graph Laplacian and computes every edge current for all \(2\le n\le14\). It verifies every rung and rail absolute row-sum formula, central-rung maximizers, the full induced norm recurrence, and exact projection symmetry and idempotence for \(2\le n\le9\). It separately checks the hyperbolic closed forms for \(2\le n\le30\) in double precision.

Replay command: `python3 verify_ladder.py` (Python 3 standard library only). Observed output ends in `VERIFY_OK exact and hyperbolic checks: 4448`.

Representative exact norms: \(M_3=9/5\), \(M_4=27/14\), \(M_5=39/19\), \(M_6=163/78\). These checks establish finite consistency, not all-size correctness, novelty, or independent certification. The all-size conclusions are based on the Green-function, cut-balance, row-domination and recurrence proof.
