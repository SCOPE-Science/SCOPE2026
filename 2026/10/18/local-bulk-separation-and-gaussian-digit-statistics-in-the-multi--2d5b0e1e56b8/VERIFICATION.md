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

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The checker independently enumerates all legal binary prefixes for every length from 1 through 18 and confirms exact rational word counts, digit-count means, and variances against the dyadic-chain recurrence. It tests the squared-length concentration bound for lengths 1 through 1999, five finite golden-mean Perron first-symbol distributions, the closed form for the local-limit density, and series truncation errors using exact rational bounds.

Observed output:

```text
VERIFY_OK: 18 exact independent full-word enumerations; 1999 concentration bounds; 5 local Perron-cylinder tests
alpha in [0.3665416620667312, 0.3665416620667312]
sigma2 in [0.1489360344549201, 0.1489360344549201]
beta = 0.3207149131818564, gap = 0.0458267488848748
```

The printed intervals have equal displayed endpoints because of floating-point rounding; the code retains exact rational positive tail error bounds. The finite tests do not certify the infinite central limit, almost-sure frequency or total-variation assertions; those are proved analytically in `RESULT.md`.
