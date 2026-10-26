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

# Verification notes

The accompanying `verify_reset_site.py` is fully standalone and uses only the Python 3 standard library. Executing `python3 verify_reset_site.py` produced `PASS: 7159 independent deterministic comparisons` and displayed the critical dimensionless values \(1.46571535194729\) for \(\kappa_*\) and \(0.537080373233492\) for \(r_*L^2/(4D)\).

The program compares two separately implemented formulas: inclusion-exclusion of reset hitting means and Linn–Lawley's asymmetric reflected-interval formula (38). It also checks the rational change of variable, polynomial identities and unique positive root, factorization of boundary-minus-midpoint costs, finite-difference gradients, selected limiting cases and grid exclusion of off-center minima. All checks passed on the executed interpreter.

The infinite claims follow analytically from the fact that the derivative polynomial has a negative leading coefficient and positive constant coefficient, hence exactly one positive zero, where the derivative switches positive to negative. This ensures there are no interior strict minima. The exact sign factor of the endpoint comparison completes the global classification, not any finite parameter grid.

No computer-assisted infinite certificate, independent audit, external certification or uniqueness claim for models beyond the specified assumptions has been performed. The mean formula itself and fixed-midpoint reset-rate optimization are explicitly recognized as existing literature.
