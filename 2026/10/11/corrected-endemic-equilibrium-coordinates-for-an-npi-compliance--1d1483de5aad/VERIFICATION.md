---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

From original printed system (1), stationarity gives S_n=(1-rho)pi/(L+theta+mu), then S_y=(rho pi+theta S_n)/(epsilon L+mu), E=L(S_n+epsilon S_y)/(sigma_n+sigma_y+mu), with I_n,I_y,J,R determined by a triangular chain. Independently coded symbolic substitution verifies all seven residuals exactly zero and the two displayed nontrivial rational formulas. The source Eq. (7) S_n produces residual -(1-rho)pi theta/(L+mu), and its downstream formulas leave all other formal residuals zero. All assumptions on nonzero denominators are explicit. A separate exact positive fully force-consistent example was constructed with lambda=1 and beta=2960/147, confirming the correction matters at an actual model equilibrium.

## originality

PASS

The exact source prints a nonstationary endemic vector, while the proposed complete correction comes from solving that source system (1). Primary PDF comparison and targeted current DOI/title/erratum searches did not locate a separate published correction. The Resultary hit for the exact claim is the same submitted result mirrored publicly, not prior independent coverage. Broader recent mpox models use different compartment structures. Priority is best of knowledge only.

## value

PASS

This is a complete repair of the exact stationary coordinates behind an explicitly stated and subsequently stability-analyzed endemic equilibrium in a published seven-compartment NPI-compliance model, not merely a harmless symbol rename. The source introduces theta as an actual susceptible-class transfer and Appendix A uses its stationarity contribution, while Eq. (7) omits it. For any positive theta and rho<1 the printed vector is nonstationary; the corrected triangular seven-coordinate family identifies the necessary base point before any stability, bifurcation or intervention analysis. The result is independently useful for readers checking the published analytic model and has a concrete positive exactly consistent example. It does not overclaim downstream theorem invalidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
