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

# Reproducibility and verification

The analytic argument is in `RESULT.md`. Run `python verify.py` (standard-library Python; no external packages).

The recorded execution completed the following checks: exact count-chain detailed balance for the connected three-site ring with positive weights \((1,2,4)\) and totals \(M=2,4,6\); equality of two independently coded formulas for the expected Gini and vacancy at multiple rational probability vectors; strict reduction under rational probability pair balancing for \(M=2,5,9\); numerical temperature ordering for four nonidentical depths at three unit totals; and the equilibrium vacancy of a six-thousand-site sample against its independently integrated Poisson-mixture prediction.

For four money units and site weights \((1,2,4)\), the exact results are \(\mathbb E G=134/343\) and \(\mathbb E V=286/1029\); at uniform weights they are \(26/81\) and \(16/81\). All exact-arithmetic assertions and numerical diagnostic tolerances in `verify.py` passed.

Finite checks do not prove strictness at every temperature, large-system weak convergence, or infinite-tail decay. Those follow from the exact mathematical steps in `RESULT.md`. No independent expert audit, formal external proof certification, or comparison against empirical economic datasets was performed. The equilibrium theorem makes no claim about the values generated after a fixed number of Monte Carlo moves.
