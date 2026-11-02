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

# Verification and reproducibility

Execute `python3 artifacts/verify.py` with standard-library Python 3. The script independently builds the Coxeter graph as Fano-plane nonline triples, verifies 28 vertices and 42 edges, computes breadth-first-search distances, confirms all shell sizes, checks all four nontrivial distance polynomials by exact integer matrix arithmetic, and checks the square-free adjacency annihilator and trace moments. It then brackets and numerically solves the critical scalar equation and checks representative real exponents.

Expected terminal output:

```
COXETER_EXACT_GRAPH_AND_DISTANCE_SPECTRUM_OK vertices=28 edges=42 shells=1,3,6,12,6
COXETER_SHARP_EXPONENT_NUMERIC_CHECK_OK alpha=0.570406337320575
```

The finite numerical probes do not prove monotonicity or the classification for every real exponent. That part follows from the derivative and concavity bounds in RESULT.md. The exact finite identities support the distance-algebra decomposition. No independent external validation has been performed.
