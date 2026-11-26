---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite-state verification

Run `python3 verify_ensemble.py` for the joint real-start basin weights. The program uses exact integers for rounding decisions, enumerates every permitted state in both maps, checks the cycle types and uses exact midpoint-cell weights. It checks the normalized table, both sets of arithmetic cycle means and the rational ensemble expectations. Its output is `[[11335435, 0, 21950155], [2730, 22528, 0], [2602, 0, 240982]]`.

The original companion `python3 verify.py` independently implements the baseline census, digests, marginal means and encoding-count comparisons. Its optional `--native` mode cross-checks the transitions against NumPy binary16 evaluations. Neither finite-state verifier treats other floating-point expressions or rounding conventions, or real initial laws other than the stated uniformly sampled then rounded ensemble.
