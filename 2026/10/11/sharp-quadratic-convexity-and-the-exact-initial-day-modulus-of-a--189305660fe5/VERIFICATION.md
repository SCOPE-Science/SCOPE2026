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

# Reproducibility and limits

The standalone `verify.py` requires Python 3's standard library only; run it with `python3 verify.py` from the directory holding the file. It checks the numerical equality witnesses against the analytic value for \(2\le n\le13\) and the parameters in its parameter list, tests 67,536 seeded numerical configurations, and proves 12 specified *finite* polynomial identities using exact rational arithmetic. Actual output:

```
Exact rational identities: 12
Deterministic numeric witness + random tests: 67536
PASS (finite checks only)
```

The proof of the universal lower bound uses a norming sign vector, the equality case of Cauchy–Schwarz, and a one-variable arithmetic–geometric-mean minimization. Its exact witness uses complementary sign supports and an explicit orthogonality identity. These arguments, not the finite computations, establish the sharp coefficient and exact initial modulus for every permitted dimension and parameter.

No exact value of the classical modulus beyond \(\varepsilon_*=2/\sqrt{1+c}\) is computed; a strict lower-envelope gap there follows analytically from the equality classification and compactness. The proof has not been independently audited.
