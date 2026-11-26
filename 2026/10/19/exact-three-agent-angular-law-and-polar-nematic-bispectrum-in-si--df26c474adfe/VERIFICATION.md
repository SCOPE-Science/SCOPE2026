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

The event that all labels refresh and none copies during a fixed interval gives a common product-uniform component and unique stationarity. Rotation kills nonneutral modes and label exchange lets us follow charges at any distinct sites. For m=2 or 3 active labels and total charge zero, condition backward on the latest event touching an active label: its label is uniform among the active labels and its rate splits into refresh a and copy c. Refresh kills a nonzero charge; copying onto itself or one of N−m inactive sites (N−m+1 choices) preserves the active correlation with parity factor Γ; copying onto any of the other m−1 active sites merges their charges. At m=2 the merger gives 1, so R=cΓ/[N(a+c)−c(N−1)Γ]. At m=3 all initial charges are nonzero, so the merged two-site term is the R of the untouched charge; the denominator is 3(a+c)−c(N−2)(Γ_r+Γ_s+Γ_t)/N≥3a+6c/N. Equation (57) of the frozen proof sums over label positions with multiplicity, as made explicit by its expanded Eq. (61) expression; equal exponents must not be deduplicated. In the all-even sector this yields E_N. In the mixed sector the numerator is (2c/N)q[R_e+c(q+1)/(Nω+cq)]; the bracket is positive even at q=−1. The pair denominators are positive including p=0,1. Taking limits gives the stated N⁻² scale for all-active neutral triples (pair modes carried by zero indices instead have order at most N⁻¹). Fourier uniqueness gives the joint law. In the empirical cubic sum, coincidence of the two +1 indices contributes R_e, while either +1 with −2 contributes R_o; the factors in the collision identity follow by counting labeled indices. An exact test at N=3,a=1,c=3,p=0 gives M_N=−1/13 but raw cubic expectation 46/351>0.

## originality

PASS

The signed-copy parity factor, even-mode independence from the alignment mixture, microscopic dynamics and moment/lineage methods are prior. The supported distinct result is the full, explicit finite-N three-distinct-label Fourier law with its signed mixed coefficient and the exact relationship to the raw cubic empirical statistic. Zheng's microscopic equation is exact, while the displayed mode-space Fokker–Planck equation is a second-order large-N expansion; neither the latter equation nor existing broadcast-voter duality supplies the frozen signed stationary solution.

## value

PASS

The first genuine three-agent marginal reveals a signed polar–nematic coupling invisible to separate polar and nematic second moments. Its reduction of the full angular Fourier law to two three-body constants is structural, not a single-mode sample. The exact collision formula matters for interpreting a measured or simulated empirical bispectrum: it can have the opposite sign to the three-distinct-agent moment, even in the frozen finite model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
