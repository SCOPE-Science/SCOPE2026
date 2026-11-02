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

# Verification

Execute `python3 verify_frobenius_reciprocal.py` with the standard Python 3 library. The verifier selects explicit irreducible-polynomial models without third-party packages, evaluates the map directly, computes actual target indegrees, and compares every zero-, one-, two-, and high-fiber count for tested coefficients. It checks all nonzero inputs for each tested instance; it does not claim exhaustive verification over all finite fields or all nonzero coefficients.

Expected output:

```
VERIFY_OK fields=14 coefficient_cases=173 direct_nonzero_inputs=70549 types=['base', 'outside_nonsquare', 'outside_square'] all_fibers=PASS
```

The infinite-family proof is algebraic, based on the norm polynomial \(R^2+(\operatorname{Tr}(a)-N(y))R+N(a)\) and complete root-count character/trace calculations. No external or independent mathematical audit has been conducted.
