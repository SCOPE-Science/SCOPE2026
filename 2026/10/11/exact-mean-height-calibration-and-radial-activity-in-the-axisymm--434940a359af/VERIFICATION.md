---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

From the exact vector field, Rdot=2R(z−beta), so stationary antiderivative tests on compact support with R bounded away from zero yield E[z|R]=beta; z-test primitives yield E[(1+rho*z)R|z]=G(z). Their orthogonal decompositions give Var(z)=E[(Rdot/R)^2]/4 and Var((1+rho*z)R)=Var(G(z))+E[zdot^2]. Under 1+rho*beta !=0 and G(beta)/(1+rho*beta)>0 the zero-variance support is exactly the rotating circle. Checked exact parameter specialization R*=3557/3525. A polynomial/rational checker does not prove stationary conditional quantifiers, which follow analytically.

## originality

PASS

PASS on the concrete model-wide conditional identities and variance/equality classification, not on the long-known torus existence or its bifurcations. Older papers are about normal-form torus and chaos rather than the claimed invariant-measure regression law; comparable modern stationarity calibrations involve other vector fields. Search-limited priority remains acknowledged.

## value

PASS

Two nontrivial conditional constraints hold for every compact off-axis stationary state and force an exact mean-height calibration plus variance/radial-speed identity; the natural invariant is motivated by Langford torus radial breathing and distinguishes all noncircular recurrence from its circular orbit. Not merely renaming a known torus or computing one numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
