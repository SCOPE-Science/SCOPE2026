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

The normal sequence gives the tangent total Chern class (1+x)^10(1+y)^10/((1-(x-y)^2)(1+x+y)^10), c1=0. The Gr(2,10) Schubert-residue pairing is [x^9 y^8]((x-y)(x+y)^10Q) for codimension-six Q. Reconstructed all 11 exact coefficient integrals with separate symbolic arithmetic: H^6=1430, c2 H^4=4004, c3 H^3=-4290, c4 H^2=9350, c5 H=-15180, c6=24920, c2^2 H^2=11330, c2 c3 H=-12210, c2^3=32480, c2 c4=26720, c3^2=13200. Independent c2=x^2+8xy+y^2, c3=-10xy(x+y). HRR yields chi(O(mH))=143m^6/72+1001m^4/72+154m^2/9+2. All eleven partitions of six with part 1 interpreted H are represented; no primitive-cycle/intersection assertion.

## originality

PASS

Appendix B of Fatighenti–Mongardi already reports A(2,7), deformation-equivalent to ten hyperplane sections Gr(2,10), including Hodge numbers and Euler 24920. Bolognesi–Ciliberto–Verra addresses the geometry of this linear-section family. Neither source material examined states all eleven polarized Chern intersections; a universal residue formula implies the entries computationally but no dominating explicit sixfold table was evidenced. Best-of-knowledge table originality only, no novelty for Hodge/Euler/degree.

## value

PASS

The complete characteristic-number data of this naturally occurring Calabi–Yau sixfold, particularly intrinsic c2^3,c2c4,c3^2 and polarized mixed pairings, give concrete inputs for Hirzebruch–Riemann–Roch and topological/specialization comparisons. Although calculable by standard Grassmannian machinery, the precise complete numerical invariant is motivated and not merely arbitrary parameter fitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
