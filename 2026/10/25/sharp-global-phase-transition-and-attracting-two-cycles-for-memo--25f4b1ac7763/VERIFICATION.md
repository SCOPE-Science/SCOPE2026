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

# Reproduction and limits

The included `verify_exact.py` uses SymPy to check two nontrivial rational-derivative identities exactly, then carries out supplementary numerical orbit and stability checks across several positive parameter choices. Execute with `python verify_exact.py` in an environment with SymPy.

The infinite-time phase assertions, uniqueness and asymptotic equivalences are proved in `RESULT.md`, not certified by numerical sampling. Symbolic polynomial identities plus positive-term decompositions give the parameter-uniform signs. The implementation is a reproducibility aid, not an independent scientific audit.
