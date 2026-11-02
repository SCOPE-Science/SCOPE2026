---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Ordered rotation phases modulo 2pi/n give m circular spacings g_j summing L=2pi/n, and direct polar integration of the nearest supporting tangent proves A=n sum tan(g_j/2) and H=sec(max g_j/2)-1, including ties. Sample-anchored circular spacings have Dirichlet(1,...,1) representation L E_j/S from iid Exp(1). Cubic tan expansion yields A-pi=(pi^3/(3n^2m^2)) overline(E^3)/bar(E)^3 plus a fifth-power remainder with L2 norm O(m^-4); exact Dirichlet tenth mixed moments justify centering and variance scaling. Delta influence psi(E)=E^3-18E+12 has exact factorial-moment variance 360 (independently recomputed), hence m^5 Var(A) limit 40pi^6/n^4. The maximum exponential minus log m converges to standard Gumbel. Characteristic-function factorization with maximum cutoff log m+t shows the joint normal sample means and extreme converge independently, tail weighted moments O((log m)^3/m^(3/2)) negligible. Normalized H differs by o_p(1). Proved fixed n, m tends to infinity; simulations alone not used to justify asymptotics.

## originality

PASS

The sharp constants for the randomly rotated regular polygon and simultaneous independence of its area/maximum-error fluctuations were not established by closest published same-geometry expected-area result or disk and inscribed-polygon analogues. Generic exponential-spacing sum/maximum asymptotic-independence literature is relevant and could subsume the probabilistic lemma, so novelty is a specific complete geometric instantiation rather than a wholly new probability mechanism.

## value

PASS

Area and worst-direction Hausdorff discrepancy quantify distinct natural geometric approximation criteria. Exact normalization plus independent joint Gaussian/Gumbel limits and 40pi^6/n^4 variance answer a concrete question about typical-versus-extreme errors, beyond rephrasing generic asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
