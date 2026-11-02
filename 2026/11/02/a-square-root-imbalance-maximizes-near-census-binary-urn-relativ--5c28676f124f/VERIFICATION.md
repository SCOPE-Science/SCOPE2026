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

The analytical theorem is proved in `RESULT.md`, by exact reduction to a two-point hypergeometric law, a uniform interior Stirling expansion, an endpoint-exclusion estimate, and a quartic optimization after square-root rescaling. Its asymptotics are **not** conclusions of finite testing.

`checker.py` is self-contained Python 3 code using only the standard library. Run from the extracted file directory:

```bash
python3 checker.py
```

The executed checks established 357 rational/probability and high-precision KL identities for every binary composition with population sizes 3 through 16, including color interchange. Nine larger-population optimizations, for sizes 50, 51, 100, 101, 200, 400, 401, 800, and 801, illustrated the asserted asymptotic location and positive gain. A separate symbolic Taylor calculation verified the quartic coefficient \(-8/3\) in the leading smooth profile and the quadratic coefficient \(4/3\) in its first Stirling correction. The exact \(n=4\) witness reduces to \(\frac14\log(256/243)>0\).

The tests do not certify uniqueness of finite-population maximizers, literature priority, or correctness under models other than the one stated. Independent mathematical validation has not been performed.
