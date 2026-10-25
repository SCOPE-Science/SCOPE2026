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

The analytic proof diagonalizes the commuting symmetric generators, derives the exact trigger equation, and bounds every summand before the earliest modal crossing. It verifies sharpness on a minimizing pure mode and classifies the case in which every mode has \(2a_i+\lambda\le0\).

The included `verify_gap.py` uses only the Python standard library to check representative cases and the factor-two comparison. These numerical checks are consistency checks, not a substitute for the proof; they do not validate noncommuting systems, uncertain parameters, disturbances, or external validation channels.

Reproduction output:

```text
PASS: pure mode attains d* = 0.28
PASS: mixed state gap = 0.32789569691683085 > d*
PASS: stable-only support has no finite trigger
PASS: exact gap >= twice generic bound (tau = 0.06000000000000001 )
PASS: empty trigger-capable set gives no finite gap
```
