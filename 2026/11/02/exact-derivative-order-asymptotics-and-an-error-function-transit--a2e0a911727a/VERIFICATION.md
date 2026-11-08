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

For every fixed sigma>0 and every upper/lower nonvertex boundary pole of the specified disk-union domain, differentiating the pole gives the exact P_n times two Laplace integrals with R_t=x²/[2((x-t)²+b²)] and gamma prefactor P_n~sqrt(pi)/(2 Gamma(sigma)^2)n^(2sigma-5/2). On 1/4<a<3/4 both t=a,1-a have endpoint R=1, slopes 16t-4, giving n^(2sigma-7/2) and the claimed pair of constants. On straight segments only the nearer t has an interior Gaussian R=1 at x=2a, giving n^(2sigma-3), and at junction its half-Gaussian gives pi*8^sigma/(16 Gamma(sigma)^2). The exact rational cap/straight expressions with a=1/4+eta/sqrt(n) yield a dominated erfc(4eta) transition uniformly on compact eta; separate far endpoint stays O(1/n). Cone comparison gives Bergman threshold sigma<1, while p-series yields cap trace threshold sigma<5/4 and straight/junction sigma<1. Independent adaptive quadratures of exact original-energy integrals at n=1800, sigma=1.1, a in {.1,.25,.4,.6,.75,.9} gave normalized asymptotic ratios .99996,.99596,.99815,.99815,.99596,.99996. These finite tests do not prove n→∞. Domain vertices 0 and 1, arbitrary holomorphic inputs, global eta uniformity explicitly excluded.

## originality

PASS

PASS on the resolved individual-order asymptotic coefficients and the erfc circle-line boundary window, not on the already published simple-pole failure of the one-diagonal norm test. Hartmann–Orsoni supply exactly the same domain, original one-diagonal functional and a midpoint simple-pole finite-energy counterexample, plus the two-diagonal characterization; read Section 3 Propositions 3.1–3.3 and Section 4. The underlying Aikawa–Hayashi–Saitoh infinite-sector identity is acknowledged. Neither supplies the above order-resolved location-dependent constants or moving junction transition in inspected text. The sharp sigma cutoff on the cap is implied by the new exponent and not counted separately. Generic Laplace endpoint saddle theory is method rather than prior covering of this domain calculation.

## value

PASS

The boundary of the finite disk-union domain forces a genuine change from endpoint to interior tangency. The exact n-exponent, positive coefficient and erfc double-scaling window quantify a nontrivial failure mode of finite-interval derivative-energy recognition. The result distinguishes the cap from straight sides and resolves a natural mathematical transition of the cited operator; neither generic formula naming nor an arbitrary numerical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
