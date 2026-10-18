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

# Reproduction and verified scope

Execute `python verify.py` with Python 3 and SymPy installed. The script checks the Schur-complement polynomial identities symbolically, enumerates all nonempty bipartitions for \(3\le n\le8\), checks the component and degree counts and tests how each singular support lies in the component arrangement. It exhaustively inspects every nonzero symmetric zero-diagonal matrix over \(\mathbb F_3\) with \(n=3,4,5\), checking the complete-bipartite component decomposition for each rank-two input. A successful run ends in `VERIFY_OK`.

The all-parameter proof is the explicit localized quotient and the direct Segre-degree calculation in RESULT.md. Finite tests are independent consistency evidence, not a proof outside the tested ranges; in particular they do not establish infinite-parameter uniqueness or characteristic-two results. No independent audit has been performed.
