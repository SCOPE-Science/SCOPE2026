---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The printed twelve additive diffusion coefficients combine, by independent Brownian coordinates, to sigma_sum*dW where sigma_sum^2=sum sigma_i^2>0. Reading the actual twelve drift equations and the supplied labelled-cancellation verifier gives dT=(Pi-mu*T-pi_p*S_f)dt+sigma_sum*dW. Couple with Y solving dY=(Pi-mu*Y)dt+sigma_sum*dW and Y(0)=T0; integrating factors give T(t)-Y(t)=-pi_p*exp(-mu*t)*integral_0^t exp(mu*s)*S_f(s)ds. On every path nonnegative to t, S_f>=0 and T(t)>=0 imply Y(t)>=0. But Y(t) is Gaussian with mean m_t=T0 exp(-mu*t)+(Pi/mu)(1-exp(-mu*t)) and variance sigma_sum^2(1-exp(-2mu*t))/(2mu)>0 for any t>0; therefore P(exit positive orthant by t)>=Phi(-m_t/sqrt(v_t))>0. The later source Ito terms sigma_i^2 X_i^2 and sigma_i X_i dB_i are multiplicative, different from printed Eq.(24). Gaussian positivity analytically, not floating-point tail rounding, is decisive.

## originality

PASS

The observation that constant additive Brownian noise obstructs positive invariance is standard; the scoped finding is a source-specific exact twelve-compartment cancellation with a quantitative Gaussian lower bound and the primary text’s additive-versus-multiplicative mismatch. Inspected the primary Eq.(24) and later calculations, compared distinct state-dependent SIS source, and searched the exact model title/DOI and OU exit aliases; no prior publication of this exact corrective result found.

## value

PASS

The explicit positive exit-probability bound formally refutes a stated global positivity theorem for a currently published epidemiological model; this matters for interpreting downstream stationary and extinction assertions and is more than a generic noise warning or numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
