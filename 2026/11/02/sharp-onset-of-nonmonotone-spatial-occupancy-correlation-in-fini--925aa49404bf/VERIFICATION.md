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

# Reproducibility checks

Run `python verify.py` with Python 3.10 or later and SymPy installed. The checker reconstructs the stationary count-chain formulas and derivative numerators symbolically, and independently computes exact rational birth–death stationary weights for two through six patches. It checks 1,200 rational identities across 240 parameter cases, in addition to the symbolic equalities and exact illustrative fractions.

The mathematical proof of uniqueness for all positive immigration-to-extinction ratios is the Descartes-sign argument in `RESULT.md`; the finite tests are supporting regression checks and are not an exhaustive proof. The complete technical contents of several related finite-network correlation papers were unavailable for independent historical-priority resolution. No independent external audit was performed.
