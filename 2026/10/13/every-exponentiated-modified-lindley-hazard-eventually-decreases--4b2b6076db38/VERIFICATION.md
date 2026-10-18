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

With u=theta x and a=1/(1+theta), the original modified-Lindley baseline has s0=e^(−u)(1+a u e^(−u)) and f0=theta e^(−u)[1+a(2u−1)e^(−u)]. It follows exactly that h0/theta=[1+a(2u−1)e^(−u)]/[1+a u e^(−u)]=1+a(u−1)e^(−u)+O(u²e^(−2u)). Raising the baseline CDF to alpha>0 multiplies h0 by M_alpha(s0)=alpha s0 (1−s0)^(alpha−1)/[1−(1−s0)^alpha]=1−(alpha−1)s0/2+O(s0²). Thus h/theta=1+[a(u−1)−(alpha−1)/2]e^(−u)+O(u²e^(−2u)) and the explicitly differentiated exact analytic formula gives d(h/theta)/du=[a(2−u)+(alpha−1)/2]e^(−u)+O(u²e^(−2u)). Since the u e^(−u) term dominates, h approaches theta FROM ABOVE and h′<0 eventually for every theta,alpha>0. The two scaled limits are theta/(1+theta) and −theta²/(1+theta). At alpha>1, the small-x hazard behaves as const*x^(alpha−1), giving increasing hazard near x=0; at alpha=1, h′(0+)=theta²(2theta+3)/(1+theta)²>0. Thus alpha>=1 has at least one interior local maximum. Independent high-precision 70-digit direct evaluation at u=25,35 for three parameter pairs confirmed exact normalized correction and strictly negative far-tail derivative; numerical tests are not the proof of eventuality.

## originality

PASS

Sarhan et al (AIMS Mathematics 11(1), 2026, DOI 10.3934/math.2026093) define EXACTLY this EML law in formulas (2.1)-(2.4). Their Section 2.2 discusses the effect of exponent alpha on hazard and displays curves approaching the terminal level but does not give the signed right-tail correction, derivative scaled limit, theorem of eventual decrease for all alpha or interior maximum for alpha>=1. Indeed its plotted x-windows can conceal the extremely late turnaround. Lehmann exponentiation is standard and the multiplier itself not novel, but the exact base-specific (u-1)e^(-u) correction, competition with alpha and terminal derivative law are not stated in inspected source. No covering general theorem for this exact pair and rate was found in searches. The 2021 source of the baseline modified Lindley distribution was not fully accessed; since it has alpha=1 only, it could imply the baseline special case, but cannot alone prove the all-alpha result.

## value

PASS

For a new reliability/survival family, distinguishing eventual decrease from apparently monotone-increasing plots determines its qualitative hazard shape. Showing that alpha>=1 necessarily entails at least one interior maximum for ANY theta, and providing the signed, parameter-uniform leading terminal coefficient, is a substantive model-specific asymptotic correction relevant to reliability characterization, not a purely numeric plotting artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
