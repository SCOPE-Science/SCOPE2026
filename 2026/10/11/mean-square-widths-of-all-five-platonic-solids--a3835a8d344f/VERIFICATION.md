---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For a centered centrally symmetric regular unit-edge polyhedron, w(u)=2h(u); each vertex-normal cell is a congruent spherical q-gon where the supporting radial vertex v has |v|=R, sinδ=1/(2R), and polar boundary tanθ_b(ψ)=tanδ/cosψ for |ψ|≤π/q. Integrating cos²θ on q sectors yields I_q=(q/3)[2π/q−2 asin(sin(π/q)cosδ)+2 sin²δ sin(π/q)cosδ / sqrt(1−sin²(π/q)cos²δ)]. The normalized moment equals N R² I_q/π. Substituting known (N,q,R) for cube, octahedron, icosahedron, and dodecahedron reproduces their exact table rows; for dodecahedron N=20, q=3, R²=3(3+√5)/8, sin(π/3)cosδ=cos(π/5), 4R²sin²δ=1, giving (3+√5)/2 + (10/π) sqrt(1+2/√5). Independently computed this exact normal-cell numeric expression 6.99919371325595 and separately integrated the actual twenty dodecahedral vertex support values in 60,000 deterministic directions to 7.4e−7. Tetrahedron is correctly separated (not centrally symmetric) and attributed to Finch exact formula. Reviewed supplied verify.py; its finite quadratures do not prove the equality outside the analytic integration.

## originality

PASS

Best-of-knowledge original completion of the natural five-solid second-moment table, centered on the previously unlocated explicit dodecahedral evaluation and a uniform normal-cell calculation for the four symmetric solids. Finch fully establishes tetrahedron and cube values, while Kabluchko–Litvak–Zaporozhets establish the crosspolytope/octahedron moment framework; a distinct co-published Resultary record supplies the icosahedron alone. Those components are credited and do not imply the dodecahedron moment: its N=20,q=3 and golden-ratio angular simplification require the new argument. No prior full-table or dodecahedral constant was found in targeted width, projected-length, Feret and caliper terminology searches; this bounded negative search is not a priority proof.

## value

PASS

An exact complete classification over the five canonical Platonic solids is a naturally motivated mathematical target, and the dodecahedral second width moment is a previously unlocated intrinsic random-projection invariant. The elementary golden-ratio expression and reusable normal-cell method close a genuine table gap. A natural self-contained exact invariant can be valuable without proving any additional general polytope theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
