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

Run `python3 verify.py` with Python 3.10 or newer; the code imports only Python standard-library modules. It independently propagates an exact-rational joint \((X,M)\) distribution and the gap for the same parameter/time choices; it checks stationarity equations and optimal speeds on a large finite grid. All checks passed at packaging time. The analytical proof in RESULT.md establishes the infinite-time speed and global optimizer. Sampling finitely many parameters cannot establish universal quantifiers, and no independent scientific audit has been performed.
