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

# Reproduction of finite checks

Use `python3 verify.py` with Python 3.11+ (standard library only). The program constructs independent faces by direct row-subset recursion and determines signed reduced Lefschetz numbers using inversion parity on oriented simplex vertices. This is independent of the fixed-orbit and transfer-matrix derivations. It checks every rotation for graph sizes \((3,2),(3,3),(3,4),(6,2),(6,3),(9,2)\). It separately computes cyclic row sums, transfer-matrix powers, and Fourier multiplicities, checking agreement with the all-parameter formulas over the ranges specified in RESULT.md.

An actual replay completed with the following terminal lines:

```
CHAIN_LEFSCHETZ_OK 3 2
CHAIN_LEFSCHETZ_OK 3 3
CHAIN_LEFSCHETZ_OK 3 4
CHAIN_LEFSCHETZ_OK 6 2
CHAIN_LEFSCHETZ_OK 6 3
CHAIN_LEFSCHETZ_OK 9 2
TRANSFER_AND_QUOTIENT_ENUMERATION_OK 9 5
CHARACTER_MULTIPLICITIES_AND_NECKLACES_OK 7 7
ALL_TESTS_PASSED
```

The finite tests do not establish the general formula: the exact uniform proof is the five-step argument in RESULT.md. The non-equivariant wedge result is a published theorem, not independently certified here. No independent external review was performed.
