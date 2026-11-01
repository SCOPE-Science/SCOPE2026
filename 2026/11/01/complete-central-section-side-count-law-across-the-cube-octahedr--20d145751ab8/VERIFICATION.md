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

# Reproducibility and verification

Run `python verify_sections.py` with Python 3. This self-contained standard-library checker builds exact rational vertices from signed permutations, reconstructs their active facets and edges, counts sign-changing endpoint pairs on central planes, and compares counts with both analytic normal-chamber formulas. It tests six distinct rational parameters in both regimes and samples 65,000 independent Gaussian normals at each of six nonexceptional parameters; Gaussian rotational invariance makes their plane directions Haar-uniform. It separately exercises cuboctahedral central section edge counting, probability normalization, endpoint identities, and sampled strict mean trends.

Verified execution reported:

```
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 6/5
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 3/2
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 9/5
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 11/5
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 5/2
EXACT_RATIONAL_POLYTOPE_EDGE_AND_CHAMBER_TESTS_PASSED 14/5
CUBOCTAHEDRON_EIGHT_VERTEX_CHAMBER_TESTS_PASSED
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 1.2
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 1.5
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 1.8
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 2.2
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 2.5
INDEPENDENT_HAAR_MONTE_CARLO_PASSED 2.8
EXACT_ENDPOINTS_AND_MONOTONICITY_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

The computer checks are independent of the symbolic proof in the sense that section crossing counts are computed directly from exact active-facet polyhedral edge incidence. The Monte Carlo tests are finite experiments, not proofs of the full parameter theorem. The rigorous support, probability, and monotonicity claims are proved analytically in RESULT.md. No independent mathematical audit has been performed.
