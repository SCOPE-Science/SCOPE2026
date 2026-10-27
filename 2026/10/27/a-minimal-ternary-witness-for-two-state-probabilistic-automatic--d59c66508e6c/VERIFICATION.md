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

The standalone verifier `verify_pfa.py` was run with Python's exact `Fraction` arithmetic. It checked every transition-matrix row sum and entry bounds, enumerated all 27 words in \(\{a,b,c\}^3\), and confirmed the unique maximizer, the largest competitor, and the exact gap. Output: `VERIFY_OK`.

The one-state lower bound is proved directly in `RESULT.md`: a one-state row-stochastic transition matrix is \([1]\), so the acceptance probability is independent of the input. No sampling, floating-point arithmetic, or extrapolation is used for the claim. Independent validation has not been performed.
