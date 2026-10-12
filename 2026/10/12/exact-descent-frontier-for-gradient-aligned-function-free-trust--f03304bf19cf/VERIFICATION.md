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

# Verification evidence and limits

The exact algebraic proof is in RESULT.md. It derives the only two possible limiting endpoint coefficients from the original Cauchy direction and the smoothness inequality, proves both are attained by explicit scalar quadratics, and solves their intersection with the quarter-descent target for every \(L,M>0\). The connected two-agent embedding shows that the same bound is a true infimum for decentralized penalties.

The standalone `verify.py` was executed using Python 3's `fractions.Fraction` with output `VERIFY_OK`. It checks 400 rational pairs of the two curvature bounds, seven relative denominators each, both exact endpoint models, and two connected-agent witnesses. The program does not establish the quantified real-parameter result on its own, and it is not a certificate for any outer iteration-complexity theorem. Full source comparison focused on the Cauchy construction and descent lemmas; unindexed equivalent research remains possible.
