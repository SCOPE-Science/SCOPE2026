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
# Reproducible checks

The proof is analytic and covers all primes \(p\ge5\). Execute `python verify.py` with Python 3 and no third-party packages. The script independently enumerates \(p^2\) character phases for every prime from 5 through 251 and checks the predicted root-grid minimum, exactly three minimizing positions, and actual parabolic sums for sampled three-site configurations in both cancellation orientations. The observed output was:

```
VERIFY_OK 1384774 numeric comparisons; all primes 5..251 and sampled parabolic triples
```

This is a deterministic floating-point numerical corroboration, not exhaustive exact arithmetic or a replacement for the infinite proof. The main proof establishes the root-grid minimum by strict trigonometric inequalities. No independent audit or external certification has been performed.
