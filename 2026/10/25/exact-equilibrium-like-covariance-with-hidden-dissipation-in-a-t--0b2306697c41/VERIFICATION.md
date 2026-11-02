---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: Checked the unique stationary solution from positive stiffnesses, the 2x2 linear systems for state-resolved second moments u_i=D(b+k)/(2ab+k(a+b)), D(a+k)/(2ab+k(a+b)), and covariance C(t)=u^T exp(t[[-a-k,k],[k,-b-k]])1. Its characteristic ODE has L=a+b+2k, P=ab+k(a+b), initial C(0)=D L/[2ab+k(a+b)] and C'(0)=-D. Enforcing one exponential yields the exact factor (ab-k^2)(4ab-(a+b)^2)=0; distinct a,b force ab=k^2 and conversely uniqueness of the ODE gives the asserted entire covariance. Independently recomputed the 4th-moment generator inverse and the positive cumulant 3D^2(a-b)^2(4ab+3k(a+b)+2k^2)/[(2ab+k(a+b))^2(4ab+k(a+b))] using SymPy, and verified factorization exactly. Prior published joint entropy formula Sigma=k(a-b)^2/[4ab+2k(a+b)] reduces algebraically to stated identity. AM-GM and a->infty with b=k^2/a establish positivity, calibration and unboundedness. Claim is covariance-only, not full OU law.

## originality

PASS

PASS best-of-knowledge: Alston–Cocconi–Bertrand 2022 investigates the very same two-state switched positive-stiffness harmonic trap and gives the state moments and physical entropy formula, both acknowledged as prior. The new result is sharp if-and-only-if cancellation of one covariance mode at kappa=sqrt(ab) for every lag and exact positive fourth-cumulant entropy calibration. The inspected full primary source does not state the combined criterion; general Markov-modulated OU methods could admit an equivalent specialization elsewhere, an explicit residual risk.

## value

PASS

PASS: Stationary autocovariance/power spectrum is an important equilibrium diagnostic. A positive, arbitrarily dissipative physical model with exactly equilibrium two-point correlations is a sharp identifiability counterexample; the kurtosis formula provides an exact higher-order diagnostic for the self-review, not just qualitative non-Gaussianity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
