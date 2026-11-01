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

# Reproduction and verification limits

Run `python3 verify_quadrilateral_vertex_index.py` from the same directory as the mathematical result. The script uses Python's `fractions.Fraction` and enumerates active sets of the sector linear-program constraints; it does not call the closed formula to construct any LP constraints. It reports 101 verified rational input quadrilaterals. The finite tests do not establish the theorem for arbitrary real parameters. The analytic sector inequalities and explicit witness coordinates are the universal certificate. The original finite-convexification literature is not reproduced or embedded. No independent audit has occurred.
