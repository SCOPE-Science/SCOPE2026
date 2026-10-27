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

# Reproducibility and limits

Run `python3 check_weighted_wheel.py` in a Python installation with SymPy. The checker reconstructs the reduced incidence matrix and the full projection using exact rational arithmetic, checks symmetry, idempotence, every row sum for the selected input weights, sign-vector attainment, and exact polynomial and derivative identities. It reports `ALL EXACT CHECKS PASSED: 486 assertions`.

The tested range is \(3\le n\le12\) and \(\sqrt t\in\{1/4,1/2,1,2\}\). Finiteness of that test set is not an exhaustive proof over other dimensions or all real weights; general claims are established analytically in `RESULT.md`. The positive polynomial identity and finite rational witness are part of the proof and also checked exactly. Independent review is not performed.
