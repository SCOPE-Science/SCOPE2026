---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Use the published exact planar formula c^tr(K)=1+max_u d_K(u)w_K(u_perp)/area(K), not a finite polygon enumeration. D=(K−K)/2 preserves widths and has 2rho_D=d_K; hence J=4rho_D(u)h_D(u_perp). For symmetric regular N-gon circumradius R and a=π/N, in an edge-normal angular chamber 0≤θ≤a, rho=R cos(a)/cosθ. If N≡2(mod4), perpendicular support h=R cosθ, J=4R²cos a constant. If 4|N, h=R cos(a−θ), product strictly increases from 4R²cos²a to 4R². Even P_m has D=P_m. Odd P_m has D regular 2m-gon of radius cos(π/(2m)); use 2m≡2(mod4). Divide the three maxima by area(P_m)=m sin(2π/m)/2. This proves all formulas for every m≥3; small cases m=3,4 give 3, m=5 gives (10+sqrt5)/5. Finite numerical sweep 3..40 is only a diagnostic; independent values m3,4,5,6,8,10,12,19,20,37 checked.

## originality

PASS

The prior paper establishes the general reduction and the cases m=3,4,5, posing a broader all-m extremal question. Known Radon curves imply directional constancy for appropriate families. The present exact residue-class value and nonconstant 4k directional endpoints for every regular polygon are not implication-given by the general formula without the separate full support/radial calculation. Narrow novelty retained with explicit prior coverage of special cases.

## value

PASS

Regular polygons are the explicitly posed candidate extremizers in a published polygonal convex-hull problem. Exact all-m benchmark values, a full directional phase split by m modulo four and the limit 1+4/pi give usable targets for the still-open minimization problem; they are geometrically motivated by Radon versus non-Radon behavior. This finite-parameter family is independently useful without proving the global extremal conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
