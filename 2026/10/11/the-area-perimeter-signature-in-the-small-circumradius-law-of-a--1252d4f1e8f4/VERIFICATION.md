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

The six-variable circumcircle parametrization x_j=c+r u(θ_j) has Jacobian |det|=2 area(T_θ) r³ for ordered noncollinear triples. Integrating over centers c for which all three points lie in K gives area(K⊖r T). For fixed C² boundary with curvature bounded away from zero, signed tubular normal coordinates show area(K⊖rT)=A−r∫∂K h_T(n) ds+O_K(r²), uniformly over unit-disk-contained triangles T; no requirement that the circle itself lies in K. Independent SymPy integration gives ∫sin a J(a) da=3π/8 and ∫sin²a J(a) da=8/9, yielding E[area(T)]=3/(2π), E[area(T)perimeter(T)]=64/(3π²). Rotation averaging using Cauchy’s perimeter formula gives angular integrals 24π² and 512P/3. Integrating r³ and r⁴ yields the two coefficients with O_K(t⁶). Fixed-area isoperimetric P≥2√(πA), strictly for nondisks, gives eventual strict comparison, with K-dependent cutoff. The proof is analytic; finite Jacobian spot-check or Monte Carlo not substitutes.

## originality

PASS

Best-of-knowledge: closest 2026 paper Bakó-Szabó–Besau–Fodor advertises disk circumradius distribution for r≥1, which is not the small-r regime, and Le Caër 2018 full arXiv primary text explicitly separates contained circumcircles from protruding ones and focuses on contained class. A related 2016 Affentranger formula studies probability that entire circumference lies within unit ball. None of the material actually read gives the universal curved-body t⁴/t⁵ area-perimeter expansion. The full text of the plausible 2026 paper could not be accessed in this run and is explicitly retained as an important originality risk rather than pronounced fully noncovering.

## value

PASS

A natural random-triangle statistic encodes the first two Euclidean intrinsic volumes in its low-radius tail, giving a new local stochastic isoperimetric comparison and an exact universal boundary correction. This is a structural all-shape asymptotic, not a small-case coefficient chosen without motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
