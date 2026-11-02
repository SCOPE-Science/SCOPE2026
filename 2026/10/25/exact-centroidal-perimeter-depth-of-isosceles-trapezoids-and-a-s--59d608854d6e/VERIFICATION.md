---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For B>b>0,h>0, the area centroid is (0,ch) with c=(B+2b)/(3(B+b)), and perimeter 2(B+b+L), L=sqrt((B-b)^2+h²). Reflecting lines about the symmetry axis partitions all unoriented centroidal chords into (i) leg/leg, (ii) bottom/leg, (iii) bottom/top incidence ranges using exact thresholds t_L=ch/B, t_R=(1-c)h/b. In the leg/leg regime the sum of relative intersection heights strictly decreases with slope squared, so minima occur at endpoints or at the horizontal upper arc U=2b+2(1-c)L. In the corner regime, the centroid ray intercept relation a/z+v/w=1 with a=B-(B-b)c and v=cL gives F(z)=z+vz/(z-a), z in [a/(1-c),2B], with F''=2av/(z-a)^3>0 and constrained minimizer z*=clamp(a+sqrt(av)); the complement has its minima at endpoints and is not better. The bottom/top regime is monotone and contributes a shared endpoint. Hence exact displayed min{U,F(z*)} formula and complete horizontal/corner equality classification. Both candidates exceed P/4 for B>b>0, and B=1,b=1/k,h=k tends to 1/4 strictly from above. An independent boundary-line-intersection checker evaluated 8000 directions over 80 nondegenerate sample shapes; that does not replace the complete three-regime proof.

## originality

PASS

The nearest full primary 2026 article derives center-ray splitting for triangles, not genuine trapezoids. A related published isosceles-trapezoid geometric dilation theorem optimizes the length of half-perimeter chords, mathematically a different functional from shortest boundary-perimeter arcs of area-centroidal lines. The closed all-parameter profile, minimizing directions and strict sharp 1/4 infimum are not implied by either comparison. Priority may exist under perimeter Winternitz/centroidal boundary-depth aliases.

## value

PASS

The centroidal perimeter Winternitz invariant is geometrically motivated, and isosceles trapezoids are the first symmetric four-vertex family beyond triangles. The all-shape formula, exact competing optimizer types and sharp unattained 1/4 boundary are substantive geometric classification, not a random restricted numerical cut.

The dated certificate retains the supplied scientific assessment, sources and limitations.
