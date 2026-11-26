---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At the two deterministic observation times the age is positive almost surely. The future clock is independent of the stationary age; discarding paths with a new reset changes a joint CDF by at most 1-exp(-s/log N). At fixed dimensionless age a=rA, the conditional correlation is (1+s/(a log N))^(-1/2), hence (1-rho_N)log N tends to s/(2a). The conditional sample second moments have relative error O_P(N^(-1/2)); multiplying by b_N times the Gaussian maximum shows the error on the edge scale is O_P(log N/sqrt N). Conditioning the second normal on the first at b_N+v/b_N gives limiting increment mean -2 lambda_a^2 and variance 4 lambda_a^2, with lambda_a^2=s/(2a). For v>=x the first-normal rescaled density equals (N phi(b_N)/b_N) exp(-v-v^2/(2b_N^2)) and is dominated by a constant times exp(-v); integration by parts of the joint-tail intensity gives the two displayed union terms. Raising the one-pair no-hit probability to N and boundedly integrating over a gives the displayed mixture with Gumbel marginals. For finite s>0, its diagonal coefficient V_s=2 Phi(lambda_A) is nonconstant; the square of its Laplace transform at half the argument is strictly less than the transform at the argument, violating Gumbel max-stability. Inclusion-exclusion at high h and bounded Taylor expansion give chi=2-E[V_s]. Equivalently it is P(|B_A|>sqrt(s/2)) for standard Brownian motion at independent A~Exp(1); its characteristic function is 1/(1+u^2/2), giving the Laplace tail exp(-sqrt(s)). The claimed order of limits is respected throughout. Inspected the proof and numerical-check design; did not run the supplied script.

## originality

PASS

The supported contribution is the stationary common-clock temporal edge law after self-normalization, including the loss of max-stability under age mixing and the exact lag dependence of the limiting joint upper tail. Neither the underlying resetting model and stationary position mixture, nor the fixed-age Hüsler–Reiss law, nor the resulting scalar Laplace-integral identity in isolation is new.

## value

PASS

Removing the fluctuating common width would naturally suggest using a usual fixed-parameter max-stable edge law, yet stationary age still controls short-time persistence through the correlation scale. The exact non-max-stable limit and lag coefficient quantify that residual common-environment effect, distinguishing the free-edge conditional law from what a stationary two-time measurement sees. The scale and observable are motivated by the existing logarithmic Brownian edge dynamics and observable removal of one-time width fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
