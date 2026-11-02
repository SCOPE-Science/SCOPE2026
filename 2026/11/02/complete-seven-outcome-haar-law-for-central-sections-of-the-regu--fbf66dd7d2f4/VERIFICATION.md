---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

Execute `python3 verify_snub_sections.py` with Python 3.10 or later; no nonstandard packages are required. The checker implements exact arithmetic in the cubic field, a rational isolator for the unique real root in \((0,1)\), exhaustive supporting-facet inequalities over all 2024 vertex triples, two-facet edge reconstruction, all 276 normal-circle pair intersections, and exact cyclic adjacency checks of local wedge rays. It independently recomputes the 482 chamber sign patterns, side-count classification, 1824 corner incidences, the seven exact spherical-area coefficients, and area normalization. A separate seeded Gaussian-orientation simulation of 150,000 directions tests the numerical law only.

The exact arithmetic checks passed, including the root-bracket proof, 32 triangular and six square facets, 60 edges, 204 two-circle and 12 four-circle concurrence axes, 482 chambers, sidedness support 12–18, and 1824 local corner incidences. The seven exact probability expressions sum to one, and their weighted mean agrees with the independent 60-edge Crofton expression. Numerical estimates are diagnostics, not proofs. No independent human audit is asserted.
