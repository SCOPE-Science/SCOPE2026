---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For G=w²+wq+b in characteristic 2, G_w=q and G_{y_i}=wq_{y_i}+b_{y_i}. Direct substitution confirms the listed representative and its two incident companion curves lie in the Jacobian singular set. Normal expansion along the curve L yields Q_t=w²+w((t+1)x0+x1+t x2)+(t+1)x0x1; independently differentiated its polar matrix and computed determinant t²(t+1)². Thus for finite t≠0,1 its polar form is nondegenerate; at t=0 Q_0=(w+x0)(w+x1). The third special point t=∞ and all fifteen curves follow from the cited S6 geometry. This proves local normal-tangent statements along the specified stratum, NOT exhaustion of the global singular scheme.

## originality

PASS

Dolgachev provides the explicit characteristic-two weighted equation and 15-curve fixed-locus configuration, but the ambient Jacobian derivative and transverse polar-rank jump are further claims. Characteristic-zero Coble singular results are not adequate substitutes for characteristic-two local tangent geometry.

## value

PASS

Locating and classifying a natural transverse singularity-type jump at the incidence points of the canonical Cremona–Richmond configuration is a geometrically meaningful local invariant for the characteristic-two fourfold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
