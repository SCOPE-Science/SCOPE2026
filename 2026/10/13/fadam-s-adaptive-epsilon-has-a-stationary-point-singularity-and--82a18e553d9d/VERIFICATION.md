---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At t=1, beta2-hat=0 in printed Algorithm 1 so Fisher f1=theta0^2 even when f0=1; for 0<|theta0|<1e-6, epsilon_hat=.01|theta0| and f1^(1/2)+epsilon_hat=(1.01)|theta0|. Both clipped directions are unclipped sign(theta0)/1.01. Thus theta1=theta0-eta1/10 sign(theta0). At theta0=0 both fractions read 0/0, while on 0<|theta0|<min(1e-6,eta1/20) the squared objective increases with amplification (eta1/(10|theta0|)-1)^2 unbounded as theta0 tends to 0. Verified independently with exact fractions and the actual source equations. Only mathematical paper-form first step is covered, not safeguarded implementations.

## originality

PASS

The FAdam paper supplies exactly the bias correction and adaptive-epsilon formula but does not give the stationary-point undefined update and nonvanishing local jump. Related Resultary epsilon/stability papers concern different optimizers and do not imply this FAdam update. The observation is an algebraic consequence of a published algorithm, so discovery may be implicit/known in engineering implementations; scoped best-of-knowledge originality.

## value

PASS

A concrete source-defined singularity plus arbitrarily large relative objective amplification in a neighborhood of a strongly convex minimizer is a mathematically substantive optimizer-behavior and numerical-safety boundary. It affects whether convergence arguments for positive-fixed stabilizers can apply verbatim; the exact phenomenon is stronger than an isolated formal 0/0 notice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
