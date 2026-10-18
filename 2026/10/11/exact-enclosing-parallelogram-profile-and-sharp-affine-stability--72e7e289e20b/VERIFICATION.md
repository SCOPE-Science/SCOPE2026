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

Inspected frozen RESULT.md SHA 039a887f74fbda37f3c4a537696008e95a34a724 and exact algebra checker verify.py SHA 1a00da33e958f68503e2bcf41ca3b20e01cddb36. Every nondegenerate centrally symmetric convex hexagon is t+[-a,a]+[-b,b]+[-c,c]; its exact zonotope area is 4(X+Y+Z). For fixed independent outward covectors u,v, the tight enclosing parallelogram area is 4h_P(u)h_P(v)/|det(u,v)|. On the normal fan each h_P(u) is linear; for fixed v and fixed determinant sign this quotient is linear fractional and bounded below by an extremal edge-normal ray; denominator-zero boundaries diverge because P has interior. Replace u, then v of a global optimum by such rays without worsening the optimum, reducing unrestricted minimization to exactly three distinct hexagon side-pair directions. Coordinates c=αa+βb give tight Q_ab=4(X+Y)(X+Z)/X=4(T+XYZ/X²); minimizing cyclic choices picks M=max(X,Y,Z), so q=4(T+XYZ/M²). Normalizing max 1, middle s, min r gives ratio 1+rs/(1+r+s), monotone in s; sharp deficit ≥2(1-r)/(3(2+r)) realized by a=(1,0), b=(0,1), c=(-1,r), and inverse bound r≥(2-6eps)/(2+3eps). Checked bundled exact sympy/rational hull assertions and independently reconstructed the analytic minimization: sampled candidate polygons would NOT suffice for all orientation proof.

## originality

PASS

Previously published Petty inequality q≤4|P|/3 and affine-regular equality ARE covered, and fully credited. Best-of-knowledge new part is unrestricted shape-dependent exact determinant formula plus sharp affine determinant-balance stability; primary 2025 circumscribed quadrilateral paper does not expose this specialized profile in relevant accessible passages. Some older mathematically relevant material was not fully accessible, retained as risk.

## value

PASS

The exact minimum-area enclosing parallelogram is a natural affine-geometric functional; hexagons are the extremizers of Petty’s sharp bound. A complete formula across their whole nondegenerate affine moduli and a sharp quantitative stability characterization of near-extremizers answer motivated structural questions, not arbitrary parameter slices or mere rederivations of the 4/3 constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
