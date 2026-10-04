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

The universal argument is algebraic. Before support activation, the soft-threshold input satisfies the exact scalar affine recurrence and has closed form \(b(1-(1+\rho)^{-j})/\rho\). The first active index is therefore the least integer for which the strict threshold is crossed. At that index the scaled dual variable becomes exactly \(\lambda/\rho\); the positive active sign then persists, and subtracting the fixed point reduces every later split-variable error to multiplication by \(\rho/(1+\rho)\).

The included `verify.py` uses only exact rational arithmetic. It checks representative parameter triples, including a threshold-equality case, against the closed-form first-activation rule and replays the geometric recurrence for multiple later steps. It also verifies the explicit witness \(b=2\), \(\lambda=1\), \(\rho=1\), where \(z^1=0\), \(z^2=1/2\), and \(z^{2+n}=1-2^{-(n+1)}\) on the tested exact indices. These finite checks do not prove the universal statement; the proof in `RESULT.md` does.

The verification does not test arbitrary initialization, over-relaxation, adaptive penalties, or multivariate Lasso. Independent audit has not been performed.
