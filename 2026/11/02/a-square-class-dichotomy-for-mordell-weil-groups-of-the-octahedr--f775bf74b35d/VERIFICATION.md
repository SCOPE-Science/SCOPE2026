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

Exact verification: run `python verify.py` in a directory containing this document and the standalone script. The script uses SymPy and was run successfully with output `VERIFY_OK` and `UNIFORM_PARAMETER_VERIFY_OK`. It checks the symbolic curve identity, exact discriminant, duplication and tripling, relevant finite-fiber coordinates, minimal infinity coefficients and valuation inequalities, the local-contribution arithmetic, and a symbolic arbitrary-parameter identity. Its calculations do not independently establish geometric rank, primitivity or Galois invariance: those conclusions require the proof's standard global intersection-theoretic theorems. No independent audit has been performed.
