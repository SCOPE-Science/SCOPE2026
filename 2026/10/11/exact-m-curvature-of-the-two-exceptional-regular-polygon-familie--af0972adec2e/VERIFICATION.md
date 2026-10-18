---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For each N=12r-2>=10 or N=12r+2>=14, d(t)=(1-t)v0+t v1 (0<=t<=1/2) represents all boundary difference vectors. Since N≡2 (mod4), h_P((-d2,d1))=cos(pi/N). The source identifies two LP-active-line regimes, with exact angles A,B,B2 (minus) or A,A2,B (plus), switch t_-/t_+ and explicit positive quadratic coefficients. In both cases the first quadratic is convex with equal height at t=0 and the switch; the second has positive curvature and stationary derivative at t=1/2, so it decreases over the second interval. These support-line vertices lie in the corresponding polygon edges, and the normals lie in the positive cones of the active edge normals. Independently reconstructed the LP directly from all 2N inequalities for 16 side counts N=10..194 and 26 equally spaced t each; maximal normalized height agrees with each proposed closed trigonometric R_N to numeric tolerance <1e-12. The analytic active-line formulas plus elementary cosine/sine bounds over 0<a<=pi/10 or pi/14 establish the all-N conclusions; the finite replay is diagnostic only. The formulas agree at N=10 with (7-3sqrt5)/2; limits 1-sqrt3/2 and monotonicity give uniqueness of P10 among the two families.

## originality

PASS

Analytic closed family evaluation is stronger than the prior qualitative computer result. The known decagon value is explicitly excluded from the novel contribution, and its earlier Git publication was verified.

## value

PASS

The two residue classes are the precise ones singled out in the literature as exceptional; an all-family analytic formula supplies exact quantitative behavior, the disk limit, and a proof of comparative decagon extremality where only a computer assertion had appeared.

The dated certificate retains the supplied scientific assessment, sources and limitations.
