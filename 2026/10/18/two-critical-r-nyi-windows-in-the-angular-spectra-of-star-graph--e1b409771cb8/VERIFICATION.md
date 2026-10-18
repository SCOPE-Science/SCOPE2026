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

The equations are proved for every dimension and allowed simplex-size cutoff by a combinatorial partition of all strict coordinate-order chambers, followed by elementary uniform factorial/binomial estimates and Riemann sums.

For a finite independent check, run `python3 checker.py` (Python standard library only). It enumerates every strict ranking of the hub and leaves up to six leaves, evaluates the Minkowski-summand winners directly at each permitted cutoff, compares the resulting distinct vertices and chamber multiplicities with the stated formulas, and checks exact rational collision probabilities. It also performs finite numerical checks of both asymptotic crossover functions.

Finite enumeration cannot prove the claims for arbitrary dimensions or the limiting behavior; the latter follows from the proof. No independent audit has been performed.
