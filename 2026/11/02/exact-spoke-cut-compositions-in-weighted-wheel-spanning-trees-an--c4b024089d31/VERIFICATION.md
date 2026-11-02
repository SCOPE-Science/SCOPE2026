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

# Reproducible verification

Run `python3 check_wheel_spokes.py` from the directory containing the research files. It uses only Python 3's standard library and terminates after enumerating all possible \(n\)-edge wheel subsets for \(3\le n\le8\).

Observed output: `PASS 5458 exact assertions/comparison checks, with analytic finite- and limit-law proofs in RESULT.md`.

The checks independently compare the marked-composition bijection and component-size multiplicities with brute-force enumeration of spanning trees, and compare the enumerated coefficient sum with an integer Bareiss determinant. Fixed-order coefficient convergence and floating-point evaluation of the Poisson-even normalizer are additional diagnostics.

**Limits:** These finite computations cannot establish the assertions for arbitrary wheel order, nor rule out existing results in literature. The general proof uses a global bijection, exact stars-and-bars counts and a dominated-convergence argument; an independent mathematical audit has not been performed.
