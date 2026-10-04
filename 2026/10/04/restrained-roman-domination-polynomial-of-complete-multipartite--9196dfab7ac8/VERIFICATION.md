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

The symbolic proof reduces the defining local conditions to part counts and applies finite inclusion-exclusion exactly. The accompanying `verify.py` is a regression check independent of that derivation: it builds each graph explicitly, enumerates every labeling, evaluates the literal neighborhood definition, compares the structural criterion, and then compares both the complete weight histogram and the minimum-weight formula.

The replay range is every nondecreasing complete-multipartite profile with at least two parts and total order at most \(9\). Finite enumeration does not prove the unrestricted theorem; it checks boundary cases and guards against algebraic or normalization mistakes. No external or independent validation has been performed.
