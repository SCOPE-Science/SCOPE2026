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

## Reproducible checks

Run `python3 verify.py` with Python 3. The script uses only the standard library and exact integer arithmetic. It reconstructs the 40-vertex intersection matrix from the published incidence rules and verifies the matrix identity and trace certificates.

Observed output:

- PASS: constructed the 40-divisor intersection matrix from the published incidence rules
- PASS: exact matrix identity G^3 - 16 G^2 - 336 G = 0
- PASS: trace(G) = -80 and trace(G^2) = 2080
- CONCLUSION: spectrum 28^1, (-12)^9, 0^30; rank 10; inertia (1, 9, 30)
- LIMIT: the spectrum proves full rank in Num(X), not index one of the generated sublattice

No independent audit or independent validation was performed.
