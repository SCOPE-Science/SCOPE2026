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

The standalone `verify.py` checks the exact integration identity, mean-square factor, comparison polynomial, rational witness, and Sturm root count using SymPy rational arithmetic. Run `python verify.py` after installing the dependency in `requirements.txt`. The proof, rather than finite tests, establishes stability for every iteration and all positive step parameters. An independent audit has not been performed.
