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

The Tutte–Coxeter graph was independently reconstructed as the Levi incidence graph on 15 duads and 15 synthemes (30 vertices,45 edges, cubic, girth eight). Enumerated exactly 90 simple 8-cycles and 1125 vertex-disjoint unordered pairs. For the unordered two-particle Abrams deleted-product CW complex, independently enumerated 435 vertices,1260 edges,900 squares; checked integral cellular d1*d2=0 and all signed 64-square torus products are d2-cycles. S6 on six labels divides pairs into orbits (45,360,360,360) with bridge profiles (0,empty),(2,(2,4)),(2,(2,4)),(2,(3,3)), and mod-2 torus ranks (35,89,89,90). The distinguished 360-pair (3,3) orbit contains a deterministically selected 90x90 integer coordinate minor with exact determinant -1 (independent check); hence its 90 cycles span a primitive rank-90 sublattice L in Z^900. The separately recomputed mod-101 boundary rank is 810; 90 independent cycles force characteristic-zero rank <=810, so rank ker(d2)=90. Because ker(d2) is primitive in Z^900 and L primitive rank90, the inclusion L subset ker(d2) is equality, proving integral basis. Other individual orbits fail integral generation by their strict mod-2 rank deficiency. Rank modulo 101 is used only as a rational-rank bound, never as integral saturation proof.

## originality

PASS

Best-of-knowledge comparison on actual final mathematical statement for Integral Tutte–Coxeter two-particle H2 basis from a single octagon-pair orbit. Four distinct implications were checked, including known covering numeric/special-case portions that are explicitly excluded from the originality claim. Sources and access limits are detailed below.

## value

PASS

The exceptional Tutte–Coxeter cubic eight-cage is a canonical nonplanar test for whether geometric cycle-product tori span configuration-space H2 integrally, and the result isolates exactly which natural shortest-cycle orbit works. Integer unit-minor and characteristic-zero rank together answer a genuinely integral generation question that rational or modular Betti counts cannot settle. The other three orbit failures sharpen the geometric characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
