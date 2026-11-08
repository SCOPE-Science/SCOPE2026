---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS. Reconstructed reflected Brownian motion with generator D dxx, uniform initial position, Robin boundary rate kappa_n during windows delta_n<=min(T/4,L^2/(4D)), fixed period and positive free-reflection mixing gaps. In dimensionless form the pulse removal p(d,k)=E[1-exp(-k L_d)] has mean local time E L_d=d and second moment 2 int_0^d(d-s)H_s(0,0)ds<=3d^(3/2); Cauchy-Schwarz gives p>=kd/(1+3k sqrt d)>=1/4 min(kd,sqrt d). Reflection-principle boundary hitting and 1-exp(-x)<=x give p<=4 min(kd,sqrt d). Every inter-pulse reflecting heat kernel for gap g>=g0>0 has uniform positive lower and finite upper density bounds, so conditional pulse loss lies between m p_n and M p_n. Positivity of the infinite survival product is equivalent to summability of p_n, producing the sharp iff sum min(kappa_n delta_n/L,sqrt(D delta_n)/L)<infinity; rescaling checked. For one pulse the half-line Robin boundary transform yields F(z)=2/sqrt(pi)-(1-exp(z^2)erfc(z))/z; Gaussian round-trip estimates give uniform exponentially small finite-interval correction as stated. Independent Robin-Neumann spectral series versus half-line erfcx on five (duration,rate) pairs found agreement at short pulses and verified finite envelope; this numerical work does not prove the all-sequence theorem. The power-law criterion is exact exponent algebra p<=2 and q>=p-1.

## originality

PASS

Best-of-knowledge, theorem/implication-based comparison of relevant primary literature; a failed search by itself does not prove historical priority. Closest known published results address different parameters/objects or only more general frameworks.

## value

PASS

PASS. The model is a natural time-dependent reactive-boundary diffusion with intermittent windows and positive mixing gaps. The sharp necessary-and-sufficient sequence criterion identifies a diffusion-limited exposure cap, in particular survival with divergent total integrated reactivity, extending the prior one-sided finite-integral observation. The exact pulse crossover and sharp p/q exponents provide independently reusable analytic facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
