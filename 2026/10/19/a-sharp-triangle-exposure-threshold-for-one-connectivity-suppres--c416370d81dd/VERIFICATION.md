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

The single supplied `verification.py` requires Python 3 and SymPy (`python verification.py`). It evaluates exact symbolic equations and sign coefficients, including the odds-transform identity, equilibrium derivative identity, and exact rational factorization of the two-crossing example. It verifies the sharp algebraic threshold and positive square-root coefficient. The example's lower crossover is bracketed by the exact fractions \(159/1000\) and \(160/1000\). Four finite pairs of equilibrium roots test degree ordering at prescribed rational distrust values, and two near-threshold samples corroborate the square-root expansion.

**Observed outcome:** the test completed with `PASS: exact identities, coefficient constraints, threshold, isolating interval, and four degree-order tests` on the local Python/SymPy installation. Sample outputs include the sharp normalized triangle threshold \(6.059325123261312\ldots\) and opening coefficient \(0.2714527704130632\ldots\).

**Proof limits:** the all-parameter two-root bound uses Descartes' rule, and the threshold uniqueness and square-root law follow analytically from an attained double root and Taylor expansion. No bounded collection of computer tests establishes these infinite-domain claims. The script neither tests stochastic finite networks nor supplies an independent mathematical audit.
