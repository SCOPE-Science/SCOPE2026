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

Run `python verify.py` with Python 3 and no third-party packages. The checker exhaustively enumerates projective normal lines and conjugation orbits for odd prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and the parameter action for \(\mathbb F_2,\mathbb F_4,\mathbb F_8\). Expected output ends with `VERIFY_OK`; the actual run returned:

```text
odd q=3: generating_planes=9, orbit_sizes=[3, 6]
odd q=5: generating_planes=25, orbit_sizes=[10, 15]
odd q=7: generating_planes=49, orbit_sizes=[21, 28]
even q=2: generating_planes=4, trace_class_counts={0: 3, 1: 1}, orbit_sizes=[1, 3]
even q=4: generating_planes=16, trace_class_counts={0: 10, 1: 6}, orbit_sizes=[6, 10]
even q=8: generating_planes=64, trace_class_counts={0: 36, 1: 28}, orbit_sizes=[28, 36]
VERIFY_OK
```

These finite enumerations are sanity checks, not proof for arbitrary prime powers. The all-field proof is given in `RESULT.md`. No independent audit or independent validation has been performed.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
