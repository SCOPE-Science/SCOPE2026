---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

From the exact Deuchert–Li canonical ideal-Bose right-tail exponent, the Bose integral equals Gamma(alpha)[Li_{alpha+1}(z)−zeta(alpha+1)] at z=e^s. The source normalization bc^alpha=L alpha Gamma(alpha) zeta(alpha) gives prefactor r/zeta(alpha); strict convexity of the source exponent makes the fugacity equation Li_alpha(z)=zeta(alpha)[1−(1−r)eta/r] the unique global saddle on 0<eta<r/(1−r). Envelope and implicit derivatives yield J'=−(1−r)log z>0 and J''=(1−r)^2 zeta(alpha)/(r Li_{alpha−1}(z))>0. The eta upper endpoint has finite cost r*zeta(alpha+1)/zeta(alpha) and infinite slope; z=e^{-t} polylogarithm expansions give the three constants at alpha<2, alpha=2, alpha>2. Independent high-precision inversions at alpha=1.5,2,3 with r=0.4, eta=0.15 reproduced positive J,J',J''; the analytic expansion, not finite checks, establishes all alpha.

## originality

PASS

The primary Deuchert–Li theorem gives the infimum and strict-convex saddle integral (Theorem 1(b), equation 1.10, proof around 2.44–2.50), not the explicit inverse-polylogarithm rate and local phase diagram. Chatterjee–Diaconis examines canonical fluctuations, not this fixed-deviation rate; other interacting Bose-gas LDPs have different observables. Same-claim Resultary hit was excluded as circular evidence. Residual risk: thermodynamic fugacity literature may contain an equivalent parametrization.

## value

PASS

Identifies a natural structural transition at spectral exponent alpha=2 between anomalous power, logarithmically softened quadratic, and quadratic small-right-tail rate geometry, and the finite-cost/infinite-slope boundary where the parent theorem warns of nonuniversal exact-threshold behavior. These motivated shapes extract more than a restatement of the variational infimum and may guide comparisons with canonical fluctuation regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
