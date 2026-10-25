---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For the six-mononomial smooth toric hexagon over Z, the vertex chart has normalized sections (1,u,v,uv²,u²v,u²v²). Hasse order-2 binomial derivatives form an integral 6x6 jet matrix. Independently constructed the entire matrix using binomial coefficients and enumerated all 36 signed 5x5 minors: exactly 18 nonzero, all monomials, and the ideal is exactly (2u²,uv,2v²) because the generators occur among the minors; determinant 0. For 2 invertible this specializes to (u,v)² in each of six vertex charts, so six length-three points total length18; in characteristic2 to (uv), the reduced hexagonal toric boundary, rank3 at vertices/rank4 along nonvertex boundary/rank5 on dense torus. The six boundary lines give degree6, arithmetic genus1 and Hilbert polynomial 6d; differing fiber Hilbert polynomials show nonflatness. Exact characteristic2 rank tests (0,0),(0,1),(1,0),(1,1) gave 3,4,4,5. Toric symmetry and gluing are justified by the six lattice vertices rather than finite-field sampling.

## originality

PASS

Best-of-knowledge mathematical implication assessment, comparing identical objects/parameters and stronger results rather than title similarity; known preliminary counts, matrix formulas and examples are credited, not treated as new.

## value

PASS

Positive-characteristic degeneration of a classical defective toric osculating map is a natural geometric phenomenon: an exact integral Fitting ideal detects a sharp change in dimension, reducedness and Hilbert polynomial at p=2. This is a motivated scheme-theoretic refinement of a known complex rank profile, potentially useful in degeneracy and toric jet theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
