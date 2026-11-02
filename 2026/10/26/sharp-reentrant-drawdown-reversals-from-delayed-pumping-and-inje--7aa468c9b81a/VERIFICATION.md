---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Differentiate E1(c/t): exp(-c/t)/t. The drawdown derivative has the sign of Phi_tau(t)-lambda, with Phi=(t-tau)/t exp(-a/t+b/(t-tau)). Its log derivative numerator is Q(t)=(tau+a-b)t²-tau(tau+2a)t+a tau², with Q(tau)=-b tau² and discriminant tau²(tau²+4ab). This proves monotonic or one-minimum regimes and sharp two-strict-extrema threshold. Envelope differentiation at the stationary t_m yields sign determined by b-(t_m-tau); evaluating log Phi derivative at t=tau+b gives the unique delay peak b/a at tau=a-b for a>b. Exact t witnesses establish the 2/0/2 pattern for (a,b,lambda)=(4,1,0.1); independent symbolic discriminant and numerical root checks passed.

## originality

PASS

Theis superposition is classical and derivative zero solutions can be computed routinely. The assessed new claim is the global strict-extrema classification and reentrant delay envelope for a nearer delayed positive injection well with a smaller rate, which are not in the accessible primary materials. Closest full publisher articles inaccessible, so priority is qualified.

## value

PASS

The sharp phase diagram and 2-to-0-to-2 reappearance under a single delay parameter expose a non-monotone identifiable feature of two-well transient interference; this may matter for interpreting pumping/recharge time courses within the idealized model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
