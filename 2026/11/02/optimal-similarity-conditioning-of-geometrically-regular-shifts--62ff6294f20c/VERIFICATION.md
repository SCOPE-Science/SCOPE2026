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

# Verification of mathematical statements

The checker `verify_similarity.py`, runnable with `python verify_similarity.py`, uses the Python standard library and compares rational squares of all sampled weights. It performs **7,350** exact comparisons of initial and shifted product blocks for \(q\in\{1/2,2/3,4/5\}\), sampled parameter pairs in \((-1,1)^2\), lengths one through seven and offsets zero through thirteen. It also compares twelve truncated infinite-product logarithms against the two-term dilogarithmic asymptotic.

Expected output:

```
exact rational block comparisons: 7350
high-precision asymptotic diagnostics: 12
all diagnostics passed
```

These checks are supporting finite diagnostics. Infinite-dimensional optimality is established by exact inequalities for every integer \(k\) followed by \(k\to\infty\); the singular limit uses an integrable-derivative Euler–Maclaurin estimate. This is not an independently audited or formally certified proof.
