---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For a generic normal, sorted base projections have gaps x,y and vertical separation s. Exactly five prism edges are crossed for an offset interval of length s-(s-x)_+-(s-y)_++(s-x-y)_+. Spherical normal integration transforms its positive-part terms to a difference of arctangents in projected gaps X,Y. The total intersecting plane mass is pi(P+2h) by directional width integration; hence p5=I_T(h)/[pi(P+2h)]. Counting expected edge crossings gives p3=p5+2h/(P+2h) and p4=P/(P+2h)-2p5. Local analysis at six projection-gap degeneracies gives thin deficit pi h^2 sum(1/a_i), and a uniform large-h arctangent expansion gives C(T)=sum |edge1||edge2|(sin(alpha)-alpha cos(alpha))/pi>0. Independently integrated the formula and counted all nine actual prism-edge intersections for a scalene base at h=0.2,0.7,1.8 over a 360x96 spherical grid; all agree within 5.2e-5. Also cross-checked six equilateral heights against separately derived closed form to floating error ~1e-15. These are bounded corroborations of the analytic argument.

## originality

PASS

The equilateral-base special case is covered by the separately assigned exact elementary formula, but not the arbitrary-scalene Crofton distribution and its shape-dependent asymptotic coefficients; affine deformation of a regular prism does not preserve motion-invariant random-plane measure. Classical stereology supplies mean edge counts and some sectional frequency tables, but accessible evidence did not establish this arbitrary-triangle formula. Full 1982 Voss and 1995 Ohser–Mücklich texts inaccessible, named residual risks.

## value

PASS

The exact probability law for a natural three-dimensional family of nonregular prisms gives distinct second-order thin and leading tall geometric signatures depending on triangle sides and angles. It is a motivated stereological invariant beyond a trivial mean or affine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
