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

The exact density calculation uses the joint \(\operatorname{Dirichlet}(2,2,1)\) law and the change of variables \(d=v-u\), \(t=u+v\); its Jacobian is \(1/2\). Exact polynomial integration proves \(\Pr(D>\delta)=\tfrac12(1-\delta)^3(1+\delta)\) for the complete interval \(0\le\delta\le1\).

The attached standalone `check.py` performs rational evaluations of the unfactored versus factored polynomial at all reduced or unreduced fractions of denominator at most thirty, checks density normalization, verifies exact benchmark tails, and independently samples five exponential weights for an empirical posterior check. It can be run using `python check.py`; the observed empirical values are reproducible to Monte Carlo tolerance via the fixed random seed.

No finite enumeration is treated as an infinite proof. The exact posterior limit follows instead from Dirichlet aggregation, independence and concentration. This is a Bayesian, prior-dependent result and requires strict distinct first-choice shares. An independent audit has not been performed.
