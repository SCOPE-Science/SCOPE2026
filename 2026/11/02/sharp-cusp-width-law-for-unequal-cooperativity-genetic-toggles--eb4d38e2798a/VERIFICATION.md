---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the abstract dimensionless ODE, eliminate the first nullcline on 0<x<α to obtain β=B_α(x). Its endpoint limits are +∞ and 0. For pq≤1 the derivative is strictly negative. Otherwise its sign can change only above (pq−1)^(−1/q), where its numerator factors into a positive factor times α−F(x). F diverges at both ends of its domain, decreases then increases about its unique minimum α_c, and is greater than x there, so its two roots for α>α_c lie in the domain of B_α. This gives the stated counts. The Jacobian trace is −2 and its determinant has the opposite sign to B_α′, giving the two attracting outer equilibria and the intervening saddle. At either ordinary fold, B_α″≠0; changing coordinates locally to (x,ẋ) shows a nonzero quadratic center-manifold term (the acceleration on ẋ=0 is a smooth nonzero factor times β−B_α(x)). Hence the zero-eigenvalue fold equilibrium is not asymptotically stable, consistent with the open interval. At the cusp only the claimed linear type is needed. α_c is the infimum of the rates admitting two stable equilibria, not an attained minimum; the precise scope in RESULT.md lines 36–45 is clear on this point. For ε=α−α_c>0, differentiate F′ at its minimum to get D>0, expand the exact factored derivative uniformly on the O(√ε) layer as K(ε−Ds²/2)+O(ε^(3/2)), and integrate. The endpoints are ±√(2ε/D)+O(ε) relative to x_c; the derivative remainder integrates to O(ε²) and replacing the endpoints by the leading ones costs no more. The fixed-x change gives the displayed shared slope; the two integrals give opposite (2/3)K√(2/D) terms. Setting p=q=2 yields D=6 and K=1. This is a replay of RESULT.md lines 49–89, for fixed exponents only. The inspected verification record reports 337 finite rational/numerical assertions; the supplied script was not executed and these assertions do not prove the asymptotic law.

## originality

PASS

Pass concerns the explicit coordinate-dependent leading width and balance-line coefficients for all fixed positive p,q with pq>1. It does not credit the model, the bistability/cusp classification where already established, or the generic three-halves exponent. The full accessible broad Hill-switch preprint was consulted, improving on the frozen access note; it gives substantial parameter-set coverage but not the same full exponent range or local quantitative result.

## value

PASS

A fixed-coordinate width is a natural quantitative invariant of this established planar model: it answers how quickly the three-equilibrium region opens in the original coordinates, which a canonical cusp shape does not quantify. The explicit exponent-dependent prefactor and first-order center slope, across nonsymmetric as well as symmetric cases, are the useful content; the generic exponent and equilibrium counts alone would not support this assessment. The result is mathematical and not an experimental calibration or a practical engineering claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
