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

# Verification and limits

The accompanying `verify.py` is a standalone Python 3 standard-library program. Execute `python3 verify.py`. It enumerates each sign configuration for \(n=4,6,8\), checks the degree-\(n\) moment identity with exact fractions for sampled real coefficient vectors and five rational full-product correlations, verifies each claimed sharp bound, and tests equality coefficient vectors. The recorded output was:

```text
NEAR_INDEPENDENT_ENDPOINT_EXACT_OK 210
EVEN_CYCLE_CONSTANTS {4: '4', 6: '124/9', 8: '71'}
```

The exact calculation uses rational arithmetic with no external packages, stochastic error, or numerical tolerances. The finite test vectors are not an exhaustive test of the continuum of real coefficient vectors, all correlation parameters, or all even dimensions. General correctness is established in the independent analytic Fourier expansion, coefficient-averaging and AM–GM proof. The completeness and originality comparisons are same-model analysis; no independent mathematical audit has been performed.
