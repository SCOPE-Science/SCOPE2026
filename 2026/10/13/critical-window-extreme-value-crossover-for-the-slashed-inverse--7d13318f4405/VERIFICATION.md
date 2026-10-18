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

Independently integrating inverse-Rayleigh density gives F_X(x)=exp(-theta/x^2); conditioning on Y~Beta(q,1) gives the exact survival 1-exp(-a)+a^{q/2}Gamma(1-q/2,a), a=theta/z^2. For q=2+2w/L, L=log(1/a), eta=w/L, singular integral on [a,1] is exactly L Phi(w). The analytic remainder R(eta) has R(0)=-EulerGamma and uniform bounded derivative near zero; its lower cutoff produces only O(a), yielding S=a[L Phi(w)+1-EulerGamma exp(-w)+O_K(1/L)]. With q_n=2+2kappa/log n and b_n=sqrt(theta n log n), expansion of L=log n+log log n+2log x yields the stated two-term nS, the Fréchet-type limit exp(-Phi(kappa)/x^2), and bounded compact uniform error. Independent 60-digit incomplete-gamma calculation at z=10^22 and w=-1,0,1 checked scaled two-term remainders 0.0263, 3.4e-19, 0.00362 respectively; finite values corroborate analytic estimates.

## originality

PASS

The source authors give a fixed-q slashed inverse-Rayleigh survival distribution and regular variation, but their Proposition 8 does not establish the moving q=2+O(1/log z) critical bridge with Euler-constant correction or triangular-array maximum coefficient. Product-tail theorems for fixed laws do not immediately imply this exact double scaling.

## value

PASS

An explicit uniform crossover across a heavy-tail exponent boundary determines nonstationary maxima and provides a quantitative 1/log n correction that fixed-parameter extreme-value theory cannot supply. This is a motivated singular asymptotic window of a published law, not just another numerical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
