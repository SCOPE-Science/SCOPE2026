---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: Actual RESULT.md at frozen Git blob 4b0e7826 gives a complete minimax width calculation from the four projected vertices (sum 0, squared sum 4); equality in the range-variance inequality requires two projections at each endpoint, giving exactly the three coordinate axes. Uniform tetrahedral barycentric Dirichlet(1,1,1,1) gives Beta(2,2) for two high vertices, so its projection has decreasing even density 3(1-z^2)/4 and centered optimum G. Facet height 4/sqrt(3), one barycentric Beta(1,3), density decreasing toward the apex, so translated optimum F at the facet. Exact symbolic independent integration and factorization found roots 8sqrt(3)-12 in (0,2) and (20sqrt(3)-12)/11 >2. All W boundaries and quantifier restrictions accounted for.

## originality

PASS

PASS best-of-knowledge: A primary full text comparison to Bakaev–Polyanskii partial-plank work and the complete Resultary Bang-core finding shows neither establishes the maximizing captured volume of a translated tetrahedral plank in the two specified symmetry orbits, nor their exact crossing. General simplex Minkowski-subtraction eroded-core optimization is a DIFFERENT functional; equality of minimum-width directions does not entail volume-capture dominance. No matching equivalent statement found, but classical simplex slice splines may give it implicitly.

## value

PASS

PASS: Partial-volume plank covering of a 3D regular simplex is a natural geometric optimization problem. A nontrivial exact interval disproves the plausible minimum-width-direction restriction when searching for the globally best single plank. It pinpoints a sharp crossover without overclaiming global optimality. Not merely a width calculation because translation-optimized volume profiles are compared.

The dated certificate retains the supplied scientific assessment, sources and limitations.
