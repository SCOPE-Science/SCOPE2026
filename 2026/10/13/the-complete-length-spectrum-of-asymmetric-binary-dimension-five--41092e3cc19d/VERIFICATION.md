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

# Verification of the length spectrum

The complete small-set search in `verify_lower.cpp`, compiled with `g++ -std=c++17 -O3`, was executed with arguments `9 11` and gave:

```text
size=9 normalized_cases=14950 rigid=0
size=10 normalized_cases=65780 rigid=0
size=11 normalized_cases=230230 rigid=0
```

Elapsed-time suffixes are omitted; they are not mathematical certificates. The program covers all normalized rank-five sets for these three sizes. Its image search rejects only mappings whose currently determined images are linearly dependent, leave the target set, or violate the pair-sum incidence invariant. Such necessary-condition pruning is sound.

The separately implemented `verify_spectrum.py` was executed on the four nested witness sets. It considers every ordered five-tuple of possible basis images, rejects singular assignments, and checks the full image set without the above pruning. Every witness has stabilizer order one and the script reports `VERIFY_OK`.

The complement argument is a general finite-group identity, not a computational extrapolation. The result does not certify any cases outside binary dimension five or disclose unperformed independent validation.
