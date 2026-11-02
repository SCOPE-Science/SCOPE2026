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

# Reproduction and verification

The standalone `verify.py` is executable with Python 3, NumPy and SymPy (`python verify.py`). In the recorded run, it passed exact rational arithmetic for the four-patch activation values, the rational allocation \((21,20,6,0)/47\), the eigenvalue \(96/47\), and 18,375 random feasible-budget comparisons across sizes \(2\) through \(8\) and dispersed mixing levels. The random seed is fixed to 20261026. The verification program and instructions are embedded in the same package.

The universal theorem has an analytical proof in `RESULT.md`: positive-semidefinite trace inequality for concentration, rank-one secular equation for high mixing, strict concavity with global KKT optimality, and a monotone cutoff equation. Neither the finite numerical tests nor the printed pass message substitutes for this proof. The experiments cannot certify novelty or imply a theorem for arbitrary dispersal, finite stochastic persistence, or capped habitat capacities.
