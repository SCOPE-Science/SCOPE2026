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

With μ,D,r>0 and X_0~N(0,D/μ), ordinary OU and resetting to a uniformly selected past time preserve the same Gaussian one-time law, but not temporal stationarity. Set A_t=∫_0^t X_u du, y=E[A_t²], c=E[X_t A_t], v=D/μ, b=μ+r: generator and history averaging give y'=2c and c'=v−bc+(r/t)y, hence y''+by'−2r y/t=2v. Conditions y(0)=y'(0)=0 and 0≤y≤vt² establish Laplace transform Y(s)=2v/[b(p−1)s²]((1+b/s)^(p−1)−1), p=2r/b; invert to confluent hypergeometric variance formula, taking a logarithmic limit at p=1. Negative-real-axis Kummer asymptotics and the critical integral yield the exact T^−1, T^−1 logT, and T^(p−2) coefficients for r<μ, =μ, >μ. All tend to zero for finite r. Independently differentiated the exact function numerically for four parameter regimes with high precision and checked ODE residual; this corroborates but does not prove the L² limit or the asymptotic.

## originality

PASS

Qualified PASS: complete primary Boyer–Majumdar and Boyer–Evans–Majumdar works on exactly this memory mechanism derive one-time marginal relaxation and kernel extensions, not the integrated-position variance law. The earlier unconfined model measures position variance; fixed-point reset correlation papers are different renewal processes. A general non-Markov reinforcement/occupation-time theorem may imply part of this result, retained as risk.

## value

PASS

A natural finite-time and long-time statistical efficiency question is not determined by identical equilibrium one-time Gaussians for a non-Markovian memory-reset trajectory. The sharp r=μ transition and logarithmic boundary with leading constants distinguish ordinary inverse-time averaging from slow memory-driven decay, with no unsupported central limit or almost-sure claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
