---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The exact restriction of the cone polynomial to the two-dimensional Grassmannian-chart pencil yields four coefficient equations. The nonzero (x,y) coordinates permit elimination of u,v via u=y^q w,v=-x^q w; the remaining ideal is (P w^q,w^(q+1)) over the smooth Hermitian curve, P=xy^(q²)-yx^(q²). Its zero locus equals F_(q²)-points and dP on the curve tangent is -1, so t=P is a uniformizer; exact primary decomposition (tw^q,w^(q+1))=(w^q) intersection (t,w^(q+1)) gives embedded length one, generic length q and special transverse length q+1. Norm-fiber counting gives q^3+1. Explicit finite q=2 independent F4 enumeration found six affine plus three infinite Hermitian points and verified the Frobenius polynomial vanishes; universal result follows from algebraic proof, not enumeration.

## originality

PASS

The set of generators and rational Hermitian point count are established; the assessed addition is their full nonreduced scheme local structure. Cheng 2022 thesis Sections 2.7 and 3.8 discuss Fano formalism and cones but the inspected cone passages do not give embedded local rings or q³+1 associated-point locus; 2025 smooth q-bic Fano theorems do not apply at the singular vertex. Resultary search returned related Fano schemes (e.g. nonreduced ternary-quadric common-kernel scheme of transverse length eight), not the same singular Hermitian cone local rings. An unindexed cone computation remains possible.

## value

PASS

A canonical rank-three q-bic singular cone can have an everywhere nonreduced line scheme and embedded points indexed arithmetically by the F_(q²)-rational generators. Exact completed local rings, associated-prime locus and lengths are substantive scheme-geometric invariants; they do not follow from set-theoretic counting and vary over an infinite prime-power family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
