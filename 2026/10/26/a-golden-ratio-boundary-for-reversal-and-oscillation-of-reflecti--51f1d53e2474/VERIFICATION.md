---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The two-state generator (Lf)_A=D f_A″+r[f_R(-ux)-f_A(x)], (Lf)_R=b[f_A(x)-f_R(x)] is exact. The contraction |u|<1 at successive reset times guarantees the unique stationary second-moment state. Balance yields active weight rho/(1+rho), active second moment 2Dp_A/[r(1-u²)], resting second moment (u²/rho)M_A and C(0)=2D/r*(rho+u²)/[(1+rho)(1-u²)]. The conditional mean semigroup has matrix [[-1,-u],[rho,-rho]], giving normalized ODE c″+(1+rho)c′+rho(1+u)c=0 and initial c′(0)=-h with h=rho(1+u)/(rho+u²). I independently verified its characteristic polynomial and factored identity (h-s_fast)(h-s_slow)=rho u(1+u)²[rho-u(1-u)]/(rho+u²)². For negative discriminant the damped nonzero sinusoid has infinitely many simple zeros spaced π/omega. In real-spectrum region, sign of slow-mode coefficient decides exactly one crossing; factor sign plus boundary u²+u=1 identifies the unique one-crossing strip rho0<rho≤rho_- when 0<u<u*. At the double root solution e^-kτ(1+(k-h)τ) handles transitions without numerical extrapolation. Near rho0 the vanishing slow amplitude is linear with positive eigenvalue gap 1-u-u², giving log[1/(rho-rho0)]/(1-u-u²)+O(1). All distinctions use dimensionless τ=rt.

## originality

PASS

Best-of-knowledge original full two-time stationary covariance sign-phase diagram for the combined reflection and refractory-rest model. Negative rescaling and refractory periods each have prior treatments separately, but inspected primary sections do not state the joint model’s exact zero classification.

## value

PASS

Stationary sign reversals induced solely by intermittent reflection and rest are a natural dynamical correlation phenomenon. The exact no-reversal/one-reversal/infinite-reversal phase diagram identifies a sharp golden-ratio boundary and critical divergence without deterministic oscillations; this is a substantive structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
