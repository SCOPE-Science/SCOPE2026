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

The analytic proof is in `RESULT.md`. The bundled `verify.py` performs exact coefficient checks for the two algebraic identities used there: the closed rational form of the two-step map and the complete factorization of its displacement numerator. It also computes the Taylor series at the fixed point using exact rational arithmetic and checks that the quadratic term vanishes and the cubic coefficient is \(-4/3\).

The checker is not an exhaustive orbit computation and is not used to infer convergence from samples. Global convergence follows from the exact sign factorization and monotonicity; the asymptotic amplitude follows from the reciprocal-square increment argument.

The theorem is restricted to positive points of the 2+2 projective ray. It does not certify full Gibbs uniqueness at zero temperature; that full model is known to be non-unique at \(q=d+1=4\).
