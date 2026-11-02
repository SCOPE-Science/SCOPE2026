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

# Verification of the exact correspondence census

`checker.py` computes equation (1) by integer arithmetic and, independently, explicitly enumerates every binary matrix representing a relation between two two-level orders. It tests both confluence implications by quantification over comparable source pairs and actual target witnesses.

For positive \(a,c,b,d\in\{1,2,3\}\), restricting to \(a+c\le4\) and \(b+d\le4\), the direct checker compares 36 complete finite universes with formula (1). It also checks 625 order-reversal identities for parameters in \(\{1,\ldots,5\}\), and selected asymmetric anchor values. Execute `python3 checker.py`; successful execution prints `ALL_CHECKS_OK`.

This finite computational verification does not establish any assertion for unbounded parameter values. The general quantified result is proved through the complete structural partition in RESULT.md. The checked property is two-sided order confluence, not a stronger category-theoretic bisimulation or a full modal model preservation theorem. Independent audit has not been performed.
