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

For right regular odd n-bipyramid, outward facet normals have horizontal directions at edge midpoint angles and vertical ±c/h, c=cos(pi/n). With ξ_j=cos(φ-α_j), k=(c/h)|u_z|/||u_h||, the generic silhouette count equals # {j:|ξ_j|<k}+2I(k<max ξ_j)+2I(k<max(-ξ_j)). The two antipodally closest mesh rays are opposite in sign, giving positive-probability support 4,...,n+2 and S=4 iff k<min|ξ|. Reduced angle δ uniform on [0,pi/(2n)] with min|ξ|=sin δ, independent z=|u_z| uniform [0,1]; integration yields P4=(2n/pi)[asin(q)-asin(q cos(pi/(2n)))], q=h/sqrt(h²+c²) and fixed-h asymptotic pi h/(4n)+O_h(n^-3). For n5 the ordered five threshold levels integrate to the given four g_j inverse-sine masses, summing to 1; P7 is prior work. Independent sphere-sampling of 80,000 directions for each n=5,7,9,11 agreed with the exact minimum probability and observed all supported shadow counts.

## originality

PASS

Earlier published exact maximal-shadow probability for the same odd bipyramid family supplies P(S=n+2), specifically n5 P7, which is credited and not claimed. Glisse–Lazard 2007 and Black–Criado 2024 bound average silhouette size/expected shadows for broad classes, not the minimum atom or complete pentagonal distribution. Resultary shows other polytope-specific angular laws but no matching odd-bipyramid minimum formula. Older contour-analysis manuscripts may hide equivalent formulas.

## value

PASS

The smallest silhouette is a canonical extreme for a fixed polytope and random direction. A closed n-family minimum probability with inverse-order asymptotic and full count support, together with all four atoms for the classical seven-vertex pentagonal bipyramid, gives an independently reusable geometric shadow benchmark distinct from the previously known maximum atom.

The dated certificate retains the supplied scientific assessment, sources and limitations.
