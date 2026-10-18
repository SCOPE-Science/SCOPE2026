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

The included `verify.py` directly constructs all derivation matrices on \(NF_{2p}(\mathbb F_q)\) from generator images. An independent finite-field Gaussian elimination calculates rank; the program separately evaluates the obstruction recurrence. The minimal \(\mathbb F_2\) test additionally checks each derivation identity on all pairs of basis elements.

Run: `python verify.py`.

Observed output:
```
EXHAUSTIVE 2 4 {0: 1, 1: 1, 2: 6, 3: 8}
EXHAUSTIVE 4 4 {0: 1, 1: 3, 2: 60, 3: 192}
EXHAUSTIVE 3 6 {0: 1, 1: 2, 2: 6, 3: 18, 4: 216, 5: 486}
SAMPLED 5 10 3000
VERIFY_OK
```

The exhaustive enumerations test all \(16\), \(256\) and \(729\) generator images respectively; the sample uses a fixed seed. The arbitrary-prime result and smoothness are established in `RESULT.md`, not inferred from finite computations. Independent audit has not been performed.
