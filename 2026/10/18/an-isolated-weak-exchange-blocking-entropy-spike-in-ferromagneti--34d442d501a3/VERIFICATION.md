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

Execute `python verification.py` with Python 3 and SymPy 1.12 or newer. The script is standalone and contains the complete 32-state construction, 16-state reversal reduction, ten exact characteristic-polynomial identities, SCC decomposition, exact real-root isolation, independent energy-difference checks, and full energy recomputation of every configuration at lengths 6 through 12 for all five coupling regimes. It also checks the finite-volume half-coupling correction at lengths 6 through 25. The packaged code was executed successfully with final output `ALL CHECKS PASS`.

The checker evaluates only finitely many configurations. The proof of all-size counting and the thermodynamic limits is instead the analytic matrix-trace identity and the Perron-Frobenius argument reproduced in RESULT.md. No independent audit or external certification has occurred.
