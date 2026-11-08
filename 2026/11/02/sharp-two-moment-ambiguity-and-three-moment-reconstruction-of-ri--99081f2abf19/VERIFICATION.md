---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a smooth embedded ring-torus surface R>r>0, sampling density on the meridian is [1+(r/R)cos theta]/2pi, not uniform theta. Independent pair chord D=|X-Y| has m2=2(R²+2r²), m4=(12R^4+52R²r²+39r^4)/2, m6=(40R^6+312R^4r²+516R²r^4+187r^6)/2, obtained from radial A and covariance tensors with central symmetry. The scale-free K(x) increases until x=2/13 then decreases; K(x)=K(y) for x!=y is equivalent to y=(4-9x)/(52x+9), giving exact multiplicity and feasible K range. T(x)=J(x)-6K(x) has derivative 3(51x²+8)/[16(1+2x)^4]>0 and decreasing derivative with inf 59/432 at x=1, proving optimal inverse Lipschitz constant 432/59. Explicit rational ambiguity witness x=1/16,y=55/196 was independently checked. Fresh symbolic independent checks verify K,J,T derivatives and distinct m6. The Hölder 1/2 boundary follows sqrt x; claims concern first three consecutive even chord moments only.

## originality

PASS

Tu–Fischbach derive forward radial volume-distance distributions for balls, not area-sampled nonconvex ring-torus inverses. Lellouche–Souris provide a generic convolution approach and examples for rectangles, balls and hyperspheres, but their inspected indexed full text does not identify this surface-torus two-to-one K involution or sharp third-moment stability. Generic shape moments can compute forward polynomials, not by themselves settle the noninjective/injective boundary.

## value

PASS

The inverse question how many low even chord-distance moments determine a two-parameter ring torus is geometrically natural. The second/fourth moments have a strict twofold ambiguity over an explicit interval and a nontrivial aspect involution; the sixth gives exact uniqueness plus an optimal inverse stability coefficient. That is an independently useful inverse-geometric classification, not mere moment tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
