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

# Verification procedure

Run `python3 verify.py` from the extracted package. This requires only Python's standard library and tests the claim using a different arithmetic representation: Legendre's factorial valuation formula, with complete multiplier enumeration for a bounded range, an explicit-witness sweep for a larger range, direct integer binomial gcds for small \(n\), and special values.

The analytical proof is contained in `RESULT.md`. The finite tests verify computation consistency, not universal validity. The full theorem also uses the published Lemma 9 of arXiv:2606.22997v1 for the known zero-valuation branch. Independent mathematical review has not been performed.
