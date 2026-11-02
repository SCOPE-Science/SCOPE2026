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

# Reproducibility and mathematical limits

The included `verify.py` uses only Python standard-library exact rational arithmetic plus deterministic random tests. Execute `python verify.py` from the directory containing the script. The recorded output is included as `checks.txt`:

```
PASS exact grounded inverses: 4082
PASS exhaustive global optimizers: 65
PASS exact endpoint-leader cutoff: 55
PASS sampled optimality exchanges: 5466943
PASS marginal telescoping identities: 67816
PASS fixed-k asymptotic profiles: 5
PASS all tests
```

The script builds a grounded path Laplacian directly for each leader set, performs independent rational Gaussian elimination, and compares the squared inverse trace with the closed gap-polynomial result. It exhaustively checks all leader choices through path order 11, reproduces the optimality rule and the endpoint threshold, and samples larger marginal exchanges and continuum profiles. Regression tests also include the simpler single-leader case without extending the theorem's claimed domain.

These finite calculations are **supporting checks**, not a replacement for the analytic identity of the grounded Green kernels or the all-integer exchange argument. The asymptotic statement rests on the uniform polynomial expansion and unique strictly convex continuum minimizer, not on sampling. Verification does not establish novelty or independent certification. The theory assumes uniform unweighted paths, perfect grounding and proportional-Laplacian damping with independent acceleration noise. All comparisons and logs pertain to the accompanying files.
