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

Run `python3 verify.py` from the directory containing this document. The checker uses only the Python standard library and asserts exact agreements rather than relying on sampled logs.

It counts all legal prefix-duplication derivations up to nineteen inserted symbols for each of five distinct seeds beginning `010`, including paths that leave the target sector. It then verifies equality with the claimed sector, exactly one derivation for every target, the weight difference, and the full coefficient formula. A structurally separate reverse-suffix dynamic program checks the minimum path lengths and their multiplicities for all 63 same-parity Fibonacci pairs through index sixteen. The checker also verifies two explicit changes at duplication bound four.

Expected recorded output:

```
PASS general-sector targets: 1750
PASS Fibonacci suffix pairs: 63
PASS sharp-bound examples: 2
PASS independent forward and reverse dynamic checks
```

The mathematical proof, rather than these finite checks, justifies arbitrary seeds and unbounded Fibonacci indices. No human or independent external audit is represented.
