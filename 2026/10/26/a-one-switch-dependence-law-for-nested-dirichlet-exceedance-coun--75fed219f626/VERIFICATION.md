---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For d≥2, 2≤k≤d, α>0 and 0<r≤s<1, expanding k paired indicators gives Cov(N(r),N(s))=k p(s)[1−k p(r)+(k−1)q_r(s)], q_r(s)=P(X_1>r | X_2>s). Dirichlet neutrality gives X1=(1−X2)Y, Y~Beta(α,(d−2)α), conditional on X2 for d≥3; d=2 has deterministic Y=1. The tail h_r(z)=P(Y>r/(1−z)) is decreasing and zero for z≥1−r. Conditioning on X2>s yields continuous strictly decreasing q_r(s) on (0,1−r), then zero. The unique r0 with kp(r0)=1 lies at most 1/2; at r<r0 the bracket is positive at s=r from Var N(r)>0, negative at 1−r, and strictly decreasing, so it has exactly one zero s*∈(r,1−r). At r>r0 it remains positive; at r=r0 it vanishes only for s≥1−r. α=1 simplex integration gives the stated polynomial covariance and b=((k(1−r)^{d−1}−1)/(k−1))^(1/(d−1)), s*=1−r/(1−b). Independent exact arithmetic reproduces d=4,k=2,r=1/10,s=7/10 covariance −2183/250000 and boundary/positive examples. Uniform n-point 1D spacings have Dirichlet(1^n+1) law, giving K_n=1+N with d=n+1,k=n−1; the fixed c,β scaled covariance follows by first-order binomial expansions. No higher-dimensional or random-sample-size assertion.

## originality

PASS

Joag-Dev and Proschan (1983) negative association covers different-coordinate indicator pairs but not the sign of two nested counts sharing coordinates, where diagonal positive contributions compete. The 2011 Decreusefond–Ferraz primary full text derives one-threshold component counts under Poisson-distributed points, not a fixed-n joint two-radius covariance reversal. The present precise general-α strict monotone one-switch criterion and fixed-n geometric-graph corollary were not among the inspected primary statements. Equivalent older spacing-process identities remain a substantive priority risk, not proof of novelty by absent search hits.

## value

PASS

Despite N(s)≤N(r) on every realization, their covariance can be strictly negative; the exact condition E N(r)>1 and unique threshold is a natural unexpected dependence boundary. It is a full classification over thresholds for all symmetric positive Dirichlet parameters, with an explicit geometric graph consequence and thermodynamic sign transition β*(c)=(e^c−1)/c. This is a useful structural result, not an arbitrary enumerated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
