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
# Computational verification

Run the provided script with `python3 verify_jordan_33.py` using Python 3 and no external packages. It constructs all nine basis monomials \(x^iy^j\), forms multiplication matrices in \(\mathbb F_p\), computes modular ranks of successive powers, and reconstructs Jordan partitions. The independent table evaluator applies the coefficient conditions in the proof.

Recorded successful output:

```
SAMPLE_OK 5 1500
SAMPLE_OK 7 1500
SAMPLE_OK 11 1500
EXHAUSTIVE_M2_SLICE_OK 3125
VERIFY_OK_JORDAN_33_COMPLETE_SPECTRUM
```

The test explicitly checks the two-conic classification over \(\mathbb F_5\), \(\mathbb F_7\) and \(\mathbb F_{11}\); a slice of \(3125\) higher-degree elements over \(\mathbb F_5\) is exhausted, and \(1500\) deterministic pseudorandom elements of the complete radical are checked in each prime field. The extension-field assertions, exhaustive ten-type completeness, and infinite family of polynomial counts rest on the mathematical proof, not on finite sampling.
