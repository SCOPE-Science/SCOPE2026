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

Run `python3 verify.py` in a directory containing this file and `verify.py`. It uses only the Python standard library. The checker generates all three-generator denumerant values by dynamic programming, then compares the exact first-difference slopes across consecutive blocks of length equal to the least common multiple of the generators. It also checks the exact modulo-inverse descent pattern on specified examples and the zero/positive step boundary for unit-generator cases. `VERIFY_OK` indicates completion of those finite checks.

The mathematical proof of the all-parameter theorem relies on finite partial fractions at roots of unity, a discrete Fourier sawtooth identity, and the Chinese remainder theorem. The executable check does not independently certify those infinite arguments, exhaust all primitive triples, or establish historical originality. Independent audit has not been performed.
