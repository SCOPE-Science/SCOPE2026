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
# Verification of the jet-penalty kernel zero staircase

The theoretical certificate is the complete analytic proof in RESULT.md: orthogonal monomial norm computation, unit-circle phase equation, strict inward crossing derivative, and the critical-strength estimate for simple zeros. These identities cover every integer \(m\ge1\) and every finite \(\tau\ge0\), including equality at entry thresholds.

Finite corroboration independently enumerated polynomial roots for \(1\le m\le14\) over noncritical physical parameter samples \(q\in(0,m+1)\) and matched the formula exactly. The embedded `check.py` supplies a standard Python/Numpy independent implementation of these sample comparisons. This numerical exercise does not establish an all-orders or infinitely quantified result; the written analytic argument supplies that proof.

The checked data do not imply uniqueness relative to inaccessible or unindexed prior literature. Independent audit: not performed.
