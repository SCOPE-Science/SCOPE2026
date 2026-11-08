---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fixed real 0<tau<1, p sufficiently large, projective reduction plus anticommutation with quarter-turn and power-sum majorization reduce the global operator norm to a nonnegative slope s in [0,1]. On [tau,1] the derivative sign is governed by H_p(s)=s^(p-1)-tau-(1+tau s^(p-1))*((s-tau)/(1+tau s))^(p-1). The three stated eventual inequalities give H_p monotonicity, one zero s_p>s0=tau^(1/(p-1)), and exactly two maximizing real projective lines. Mean-value expansion yields displacement s_p-s0~s0(1+tau^2)*rho_p^(p-1)/(tau*(p-1)); since the single-row quotient U_p has a stationary maximum at s0, its logarithmic loss is lower order than rho_p^p/p. Thus nu_p/R_p-1~rho_p^p/p and lim p*(nu_p-R_p)/rho^p=(1+tau)*tau^((1+tau^2)/(1-tau^2)). The Xu–Liu Lp conclusion is conditional on their published exact identity. Independent numerical optimizer checks for several tau and finite p corroborate the root and strict lower-bound gap; double precision ceases to resolve exponentially tiny gaps, and is not relied on for the limit.

## originality

PASS

Xu–Liu arXiv:2610.03050 proves the underlying geometric-to-matrix norm identity but gives no inspected sharp high-p exponentially-small coefficient or eventual maximizing-ray classification. Other skew James/Banaś–Frączek/hexagonal results concern other spaces or skew-parameter regimes. Resultary operator-norm search returned adjacent large-p Hilbert and James topics, not this fixed-tau matrix problem. Historic two-by-two induced p-norm asymptotics remain plausible.

## value

PASS

The row-Hölder bound is a canonical exact benchmark for an induced matrix p-norm. Quantifying its beyond-all-algebraic-orders strict defect and the exponentially displaced optimizer, with a closed tau-dependent coefficient, is a motivated sharp singular asymptotic for skew Schäffer constants, not merely a benchmark recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
