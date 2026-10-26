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

# Mathematical verification

The derivation of the resolvent formula is analytic. The key standalone checks involve the exact triangular singular norm, the unique logarithmic-derivative zero \(x=1/\sqrt6\), the threshold identity, both parameter endpoints and the source-independent exterior maximum-modulus principle. There is no appeal to exhaustive sampling to establish an infinite continuum statement.

Run `python3 verify_ritt.py` with Python 3 standard library. The script checks algebraic threshold matching, predicted maximizing boundary values against directly calculated matrix singular norms for 1,000 parameter values, 181,000 finite angular inequalities, and supplementary exterior values. Expected final marker: `RITT_FORMULA_SUPPLEMENTARY_CHECKS_OK 182968`.

The independent scientific audit remains unperformed. The script does not settle publication priority, higher-dimensional cases or any inaccessible literature.
