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

The quotient group generators are transverse translations by a,b and the half-turn screw by h. Even screw powers give shortest pure-translation displacement min(a,2h). For odd powers the shortest based displacement is sqrt(h^2+dist(2x,aZ)^2+dist(2y,bZ)^2). Uniform-volume sampling makes the folded distances independent uniforms U,V on [0,a/2],[0,b/2], proving L^2=min(a^2,4h^2,h^2+U^2+V^2). Area integration of the quarter disk clipped to [0,a/2]x[0,b/2] proves the CDF including cap atom. Exact fourth moments yield Var(U^2+V^2)=(a^4+b^4)/180. Differentiating Var(min(Q,q)) gives 2 Pr(Q>q)(q-E min(Q,q))>0 on the interior support, and q(h)=min(3h^2,a^2-h^2) peaks at h=a/2. The equality plateau q>= (a^2+b^2)/4 exists iff b/a<=sqrt2, with the stated exact interval; h>=a makes variance zero.

## originality

PASS

PASS qualified for the complete rectangular half-turn pointwise squared-injectivity law together with its exact optimal spatial variance and bifurcation at b/a=sqrt2. Cosmic Topology Part I already gives the half-turn group and a cylindrical nearest-clone exclusion condition in eqs. (4.1)-(4.2), from which portions of the CDF can be inferred; those are credited, not new. The inspected paper does not state the cap-dependent probability law, exact spatial variance, or aspect-ratio-dependent unique/plateau height optimizer. No broader covering result found in the targeted published searches.

## value

PASS

PASS: pointwise injectivity, unlike global systole, varies with observer position in an inhomogeneous flat manifold; its complete distribution and maximal squared-loop-length variance quantify a natural geometric observable. The sharp b/a=sqrt2 transition changes the structure of maximizing geometries, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
