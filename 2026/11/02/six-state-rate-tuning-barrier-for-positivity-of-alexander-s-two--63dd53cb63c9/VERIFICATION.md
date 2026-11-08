---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The 0,-u,-uz spectral decomposition of the reversible star generator gives every endpoint entry as a combination of r(w),r(zw) with w=uh and z=1+mv/u. From gamma=1-1/sqrt2, exact scalar r(x) has unique global minimum -eta at w*=4+3sqrt2; F(x)=(1-r(x))/x is positive and strictly decreasing, forcing all distinct-state offdiagonal entries strictly positive. For u=v and m<=4, the lower diagonal bound (1-m*eta)/(m+1)>0. For m>=5 and z>3+2sqrt2 a hub diagonal at zw=w* is negative; for z below or equal, every leaf diagonal at w=w* is <= (297-211sqrt2)/(98m)<0. The latter radical is exact negative. Decay to rank-one strictly positive stationary projector proves return of positivity for large h. Independent SymPy exact identities and 50 ratio/dimension witness cases reproduced the signs; the unbounded quantifier relies on the inequalities.

## originality

PASS

Alexander's actual two-stage method and standard SSP/absolute-monotonicity barriers are prior. Neither the Kocsis–Németh optimal-SDIRK comparison nor general Markov positivity theorem inspected gives the existential small-star rate tuning or universal m>=5 obstruction for THIS method; qualified historical specialty overlap remains.

## value

PASS

The sharp five-leaf (=six-state) impossibility threshold, explicit two-case all-rate counterexample and small-star safe construction answer a natural integrator-specific Markov positivity boundary, not a routine numeric recheck of the general SSP barrier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
