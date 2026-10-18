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

Density c=1+alpha(1-2u)(1-2v)+beta(1-3u^2)(1-3v^2) integrates to rho=alpha/3+3beta/4. At t=(9-sqrt(57))/24 positivity of c(t,1) gives global rho<=1/[3(1-2t)]=(sqrt57-3)/12. At alpha*=-3+7sqrt57/19 and beta*=1-sqrt57/19, c(u,1)=6beta*(u-t)^2, the lower v=0 edge is concave with positive endpoints, and for min(u,v)<=1/sqrt3 the density is concave in the other variable with nonnegative endpoints. Both u,v>1/sqrt3 give c>=1+alpha*>0. Equality forces an interior tangency on v=1, hence derivative=0 and unique parameter pair. Independently reproduced radical/tangency identities with SymPy; finite grids do not prove global positivity.

## originality

PASS

2026 Alawady et al. give the exact same polynomial density and rho expression but constrain to |alpha|<=1/2, |beta|<=1/8; their 25/96 correlation maximum is box-restricted. Their assertion that the rectangle is necessary for copula validity fails, as the present explicitly positive edge-tangent parameter beta*=0.6026 lies outside it. Classic FGM 1/3 max is a one-term subfamily. Historical Kimeldorf-Sampson 1975 polynomial construction original, but archival extraction is degraded, which remains a material priority risk.

## value

PASS

Sharp analytic optimization across the full genuine positivity domain corrects an overly restrictive claimed necessary condition in a live probabilistic model, explicitly determines an otherwise unknown maximal rank-dependence and unique parameters, and crosses the FGM cap. No claim of general nonuniform marginal Pearson bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
