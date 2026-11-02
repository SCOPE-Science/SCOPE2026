---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed the exact held-input ODE in the two-dimensional safety-trigger counterexample, with J skew-symmetric, x(t_i+tau)=e^{h_i tau/2}R(tau)x_i, h(t_i+tau)=1-(1-h_i)e^{h_i tau}, and E_i(tau)^2=(1-h_i)[(e^{h_i tau/2}-1)^2+4e^{h_i tau/2}sin^2(tau/2)]. For rho>1, 0<sigma<1, and nonzero strictly interior x_0 (0<h_0<1), the residual changes sign before the first barrier-zero time, giving a positive trigger. The barriers decrease; if they had a positive limiting value, the bounded speed and trigger magnitude would imply a positive lower bound on each inter-event duration and each barrier decrement, contradiction. Hence h_i->0. The exact error at any fixed small delta>0 tends to 2 sin(delta/2)>0, showing first trigger tau_i->0; the local flow then gives E_i(tau_i)/tau_i->1. With c=sigma/(2rho^3), tau_i/h_{i+1}->c and h_{i+1}/h_i->1; the reciprocal increment 1/h_{i+1}-1/h_i->c. Stolz-Cesàro yields h_i~1/(ci), tau_i~1/i, and summing gives t_i~log i, log N(t)/t->1. The latter is a logarithmic event-count asymptotic, not the stronger N(t)~e^t. The divergent harmonic sum excludes finite-time Zeno accumulation. Independently calculated 20,000 exact held-flow roots, verifying positive decreasing h and i*tau_i tending near 1; finite checks corroborate but are not the asymptotic proof.

## originality

PASS

The exact controlled system, its trigger, and the qualitative lack of a uniform inter-event lower bound come directly from Taylor–Ong–Cortés–Ames. The inspected counterexample derives approach to the barrier and illustrates shrinking gaps; it does not provide the sharp reciprocal-index coefficients and logarithmic event-time law. Searches for synonymous MIET/Zeno boundary-layer asymptotics in the same model and published findings found no demonstrated stronger covering statement. Priority remains qualified because known exact equations make the asymptotic derivation accessible and an unindexed follow-up might include it.

## value

PASS

This sharp asymptotic resolves an important distinction in a canonical safety-control counterexample: infimum of inter-event gaps equals zero while events do not accumulate in finite time. The universal leading gap constant and exact barrier coefficient quantify the sampling burden, and t_i~log i distinguishes infinite-time exponential growth of counts from Zeno behavior. It is specifically motivated by the earlier counterexample and is not asserted as a general controller theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
