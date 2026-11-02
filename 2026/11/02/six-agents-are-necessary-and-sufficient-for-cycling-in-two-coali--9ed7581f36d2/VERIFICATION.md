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

# Reproduction

Run `python3 check.py` using the included standalone Python checker. It performs a complete search of all labeled symmetric enemy relations through five players, exact profitable edge comparisons, directed-cycle detection, and exact-fraction verification of eight moves in the six-agent real-line witness. The checker reports `LOWER_OK graphs=1098 states=15834 profitable_edges=28108`, `WITNESS_OK`, and `VERIFY_OK`.

The infinite family statement is resolved by the six-agent witness and exhaustive finite lower bound: every smaller cutoff instance is a symmetric enemy graph in the enumerated domain. No external datasets, floating-point tolerances, or third-party proof systems are required. The code execution is a self-review reproducibility check, not independent audit.
