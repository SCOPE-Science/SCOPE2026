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

For octahedron conv±e_i and E=u⊥ with u Haar-uniform up to sign, projection polarity gives (P_E O)^polar=[-1,1]^3∩E; center symmetry guarantees unrestricted inradius equals inverse farthest cube-section radius. Sorting |u| into a≥b≥c≥0 and examining cube-section vertices with two fixed signs gives R²=2+((b+c)/a)² when a≥b+c, else 2+((a-c)/b)². The competing cases satisfy the inequalities in RESULT.md, meeting continuously at a=b+c. At threshold R²≤2+s² (0≤s≤1), each branch is a simplicial cone in one positive sorted chamber, rays ((1,0,0),(1,s,0),(2,s,s)) and ((1,1,1-s),(1,1,1),(1+s,1,1)). Each determinant has absolute value s². The known solid-angle formula, multiplied by 48/(4π), yields exactly 24/π times the sum of two arctans, with stated denominators D1,D2, G(0)=0,G(1)=1 and support [1/√3,1/√2]. Smooth spherical level boundaries have measure zero. Independent double-precision cone determinant/angle checks at s∈{0,.1,.25,.5,.75,1} passed; the source exact-rational verifier independently enumerates section vertices and projected polygons, and was inspected for its sampling-vs-proof distinction.

## originality

PASS

The exact observable is the random-plane inradius of a three-dimensional crosspolytope, equivalently reciprocal circumradius of a random central cube section. The inspected primary Böröczky–Henk paper gives projected face-number expectations and probability of six vertices, not metric-radius CDF. The 2026 Abas paper studies directional widths, a distinct functional. The extremely pertinent Guédon–Litvak–Tatarko–Vritsiou 2026 paper concerns random section diameters but only its abstract was accessible: cannot make whole-document noncoverage claim. Its arXiv formats were inaccessible, OA searches located abstracts alone, and Oxford institutional access returned vpn_disconnected; do not override authentication. Best-of-knowledge no demonstrated covering theorem, with material overlap risk and Resultary outage explicitly retained.

## value

PASS

An exact complete law of a natural metric projection invariant for the smallest nontrivial regular crosspolytope gives quantiles and geometric benchmarks inaccessible from face counts alone. The analytic two-regime cube-section geometry and explicit trihedral solid angles identify a substantive distributional structure, not an arbitrary isolated sample or parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
