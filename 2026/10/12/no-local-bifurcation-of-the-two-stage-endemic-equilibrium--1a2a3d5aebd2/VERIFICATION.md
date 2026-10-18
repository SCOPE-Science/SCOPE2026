---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

At the strictly positive endemic equilibrium beta*S*=x1 and q=beta*I1*>0. Reconstructed the actual four-by-four Jacobian J with rows (-(mu+q),-x1,0,alpha), (q,0,0,0), (0,gamma1,-x2,0), (0,theta1,theta2,-alpha-mu). Its characteristic polynomial is monic quartic; independent sympy exact expansion from primitive positive parameters gives all-positive coefficients A1..A4 and Hurwitz Delta2, Delta3, with Delta2 36 monomials and Delta3 331 monomials, each coefficient strictly positive. Routh-Hurwitz therefore proves all four roots strictly in left half-plane for EVERY interior positive parameter set admitting endemic equilibrium. This is local, not global, and excludes interior local Hopf/zero crossings only.

## originality

PASS

The actual four-dimensional waning-immunity/stage-specific mortality Jacobian and full positive-parameter Hurwitz conclusion are not contained in the inspected 2026 motivating article, whose endemic global convergence is conditional on additional Lyapunov inequalities. Röst--Tekeli 2020 treats constant-population SIS stage chains, while Guo--Li--Shuai 2012 treats broader staged progression under hypotheses not shown to cover this feedback system. Positive best-of-knowledge originality is for unconditional LOCAL equilibrium stability, not endemic-existence or global dynamics.

## value

PASS

An unconditional local stability theorem for a specific published two-stage endemic equilibrium settles whether parameter variation can create a local Hopf instability, directly clarifying numerical stability seen beyond a restrictive global Lyapunov sufficient condition; the epidemiological model and stability question are intrinsically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
