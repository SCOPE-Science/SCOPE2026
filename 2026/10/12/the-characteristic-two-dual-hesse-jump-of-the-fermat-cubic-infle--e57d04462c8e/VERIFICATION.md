---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Over any geometric field of p≠3, the Fermat cubic gradient (3X^2,3Y^2,3Z^2) never vanishes projectively; each of the nine lines X+ζ^aY, etc. has cubic restriction Z^3, hence exactly one distinct smooth flex triple-contact point. Three pencils have centers off the cubic. Mixed-pencil concurrent triple determinant is 1+ζ^(a+b+c); for odd p≠3, -1 is never a cube root of unity, so 27 distinct cross-pair ordinary double points plus 3 pencil triples and 9 cubic tangencies =39. In p=2, exactly nine mixed triples replace 27 doubles, giving 12 line triples and nine tangencies=21 support points, the 9_4/12_3 dual-Hesse incidence. Frobenius on ζ gives F_p-rational counts p=2:7, odd p≡1 mod3:39, odd p≡2 mod3:9. No four lines concurrent; cross intersections off cubic. Universal determinant proof, supplemented by inspection of source finite-field verifier; characteristic3 rightly excluded (nonreduced divisor), and singular scheme/Tjurina not counted.

## originality

PASS

Classical dual-Hesse realization in characteristic two and characteristic-zero Fermat cubic flex arrangement are known. Kühne-Szemberg-Tutaj-Gasińska 2024 §2.2 identifies the unique 9-line Steiner triple configuration and its field realizability by a root of x^2-x+1; Talar 2023 has the 27-node/3-triple/9-flex characteristic-zero count. Neither independently states the complete p≠3 specialization of this fixed integral union of the Fermat cubic and nine specific tangents, nor its rational geometric singular-support counts 7/39/9. Best-of-knowledge positive for that combined arithmetic divisor classification only, with strong prior-line-incidence coverage explicitly excluded from novelty.

## value

PASS

Good reduction versus characteristic-two collision for a concrete degree-12 Fermat flex divisor is a natural geometric arithmetic boundary: 27 ordinary nodes merge in nine triples while flex contact remains. All-prime singular-support and rational-point counts can be reused when studying integral arrangements and characteristic-dependent singularity schemes; this is more than recomputation of abstract dual-Hesse incidences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
