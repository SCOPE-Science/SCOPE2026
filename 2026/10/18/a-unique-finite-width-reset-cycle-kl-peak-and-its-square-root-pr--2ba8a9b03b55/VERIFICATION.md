---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

An Ornstein–Uhlenbeck cold-Gaussian reset evolves a variance ratio rho=1+a(1-exp(-lambda t)), and its endpoint Jeffreys divergence is f_a(x)=a^2(1-exp(-x))^2/[2(1+a(1-exp(-x)))]. Independent renewal averaging leads to periodic H_a(q)=q f_a(1/q) and Poisson G_a(q)=E[f_a'(Y/q)] with Y unit exponential. The periodic elasticity h(x)=x/(exp x-1)*(2+a z)/(1+a z) decreases strictly from 2 to 0, yielding one optimizer. For Poisson, log f_a'(exp u) is strictly concave: write f_a'(x)=(a/2)exp(-x)(1-(1+a z)^-2), and compose the increasing concave log of the latter factor with increasing concave log(z(exp u)); log-time marginalization by Prekopa proves log-concavity in log q. Analyticity and vanishing tails rule out a flat maximizer, giving uniqueness for each a>0. As a grows, controlled expectation J_a(q)=E[(1+a z(Y/q))^-1], J_a=O(log a/sqrt a) at q~sqrt a, gives q_per/sqrt a ->1/sqrt2, q_pois/sqrt a ->1 and maximum rates a/2-sqrt(a/2)+o(sqrt a), a/2-sqrt a+o(sqrt a). Fresh independent quadrature and numerical optimization for a=16,400,10000 confirmed positive gaps and approach to the predicted coefficients; finite optimizations do not establish global uniqueness.

## originality

PASS

Best-of-knowledge novelty of the specified final mathematical claim, not of standard foundations; see four direct scientific comparisons and material primary-source reading with residual risks.

## value

PASS

Optimal resetting of an exactly specified finite-width Gaussian information reward is a natural well-posed optimization problem. Proving exactly one global optimum for two different renewal protocols at every nonzero reset width and a sharp nonzero protocol gap is a meaningful asymptotic comparison, not merely evaluating a Gaussian KL formula. The distinction from hardware-inclusive dissipation is explicit and essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
