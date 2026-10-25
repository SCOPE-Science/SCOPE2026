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

# Reproduction and limits

Run `python3 check_skeleton.py` from the same directory. It uses the Python standard library and checks 4,563 exact-rational and asymptotic-consistency assertions. In particular, the Gram matrix of \(1,t_1,\ldots,t_{n-1}\) is inverted independently of the proposed closed kernel formula, and the beta negative-part integral is evaluated by polynomial expansion independently of the compact survival-function proof. The test includes every pair \(3\le n\le11\), \(1\le s\le n\), both endpoint cases, rational benchmark values and large-dimension consistency checks.

The theorem's unbounded ranges of \(n\) and \(s\) are established analytically in `RESULT.md`; finite tests alone would be insufficient. The comparison with previous mathematics is a best-knowledge bibliographic assessment, not an exhaustive priority certificate. No independent validation has been performed.
