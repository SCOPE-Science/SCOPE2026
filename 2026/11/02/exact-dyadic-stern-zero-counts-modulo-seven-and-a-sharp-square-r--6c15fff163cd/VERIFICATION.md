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

# Reproducibility

Execute `python3 verify.py` using Python 3 standard-library modules only. Expected terminal line:

```text
VERIFY_OK projective_polynomial_identities=8 rational_coprimality=1 direct_indices=262144 state_levels=300 minimal_order=6
```

The program exactly checks every state-polynomial identity and rational polynomial coprimality; an independent Stern integer recurrence tests all indices below \(2^{18}\), and a projective transfer recurrence tests 300 levels. The proof in RESULT.md uses these explicit certificates and formal power-series uniqueness to cover every level. The infinite spectral sharpness argument is algebraic, not computationally enumerated. The historical-priority comparison is provisional; no independent audit has been performed.
