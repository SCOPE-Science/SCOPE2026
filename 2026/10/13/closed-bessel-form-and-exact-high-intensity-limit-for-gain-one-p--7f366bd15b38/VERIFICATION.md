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

Start with the published unit-gain average fidelity F=(2I0(2zeta))^-1 sum_{m,n>=0}(zeta/2)^(m+n)(m+n)!/(m!² n!²), nonnegative and absolutely convergent for zeta>=0. At k=m+n, Vandermonde yields sum_m k!/(m!²(k-m)!²)=binom(2k,k)/k!, so the series becomes 1F1(1/2;1;2zeta). The Euler integral and t=(1+cos(theta))/2 give e^zeta I0(zeta), proving the exact Bessel quotient. Standard large-positive-x I0(x)~exp(x)/(sqrt(2pi x))*(1+1/(8x)+9/(128x²)+225/(3072x³)+...) then gives F=2^-1/2*(1+1/(16zeta)+25/(512zeta²)+491/(8192zeta³)+...), tending to 1/sqrt2 from above and eventually above 2/3. Independent mpmath rectangular double-series truncation agreed with Bessel quotient at zeta=0,0.5,1.2,4; independent symbolic rational division confirmed the three coefficients. Valid only at gain g=1.

## originality

PASS

Gábris–Agarwal 2006 derives the gain-one double series, a numerical maximum near 0.75884, and a qualitatively nonclassical high-intensity plateau, but not its exact special-function reduction or value 1/sqrt2. The Kummer integral, Vandermonde identity and Bessel asymptotics are textbook tools credited as prior. The relevant claim is their new application to the exact original teleportation protocol, extracting a previously unstated plateau and positive approach correction. The earlier Wu–Li–Wang–Xu study uses a distinct pair-coherent teleportation protocol. Unindexed equivalent summations remain a risk.

## value

PASS

The exact asymptotic average teleportation fidelity is a physically natural target-invariant, and the source previously left its high-intensity value qualitative and its expression as a double numerical sum. The source-specific closed Bessel quotient gives the exact stable plateau 1/sqrt2, its approach direction and positive corrections, and the eventual 2/3 benchmark exceedance without new numerical optimizations. Although the summation uses classical identities, recovering the exact interpretation for the published protocol supplies a motivated useful fact, not an arbitrary table value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
