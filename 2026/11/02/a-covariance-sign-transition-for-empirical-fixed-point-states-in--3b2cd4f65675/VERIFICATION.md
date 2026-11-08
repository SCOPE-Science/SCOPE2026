---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Finite Ewens singleton count chain has +1 probability theta/(theta+j), -1 probability k/(theta+j), and stay otherwise. On logarithmic time, Gnedin–Stark 2022 Theorem 6 gives a stationary immigration-death process; initial j<eps*n contributes <=eps, ensuring joint weak occupation-fraction limits, and bounded fractions imply covariance limits. Stationary reversibility and thinning from X(0)=0 yield Poisson(theta(1-e^-t)) at lag t, hence E[W0 Wd] equals e^-2theta theta^d/d! integral_0^1 e^(theta u)(1-u)^d du. I_d(0)=1/(d+1), I_d strictly increasing to infinity, and I_(d+1)<I_d yield unique increasing thresholds; Gaussian upper/lower Laplace bounds at theta=d+(1+-eta)sqrt(d log d) prove sharp first-order displacement. Independent SciPy integration/bisection gave theta1=1.793282132900761, theta2=3.383634282853483, theta3=4.881277491345546.

## originality

PASS

Best-of-knowledge PASS for the exact 0-versus-d empirical occupation covariance sign threshold and its d+sqrt(d log d) scale. Gnedin–Stark establish the process limit and empirical occupancy framework; the stationary immigration–death transition is classical, but the sign crossings and sharp large-d phase location were not given by inspected prior theorem statements.

## value

PASS

The empirical occupation fractions are natural observables for Ewens growth precisely because they fluctuate rather than converge almost surely. Their 0-versus-d covariance changing from negative to positive despite pointwise mutual exclusion is a motivated nontrivial phase phenomenon. A full ordered family of exact thresholds and the sqrt(d log d) displacement are specific reusable facts, not a routine finite sample or a restatement of the classical Poisson queue kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
