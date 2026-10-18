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

The proof is algebraic and valid for all integers \(n\ge3\) and finite fields; no general theorem is inferred solely from enumeration. The standalone checker `verify.py` independently implements finite-field multiplication and counts all vectors satisfying the original idempotency equations. It tests 38 small configurations, including prime fields of characteristics two, three, five, seven, eleven and several quadratic extensions, against the closed formulas. Replay command: `python3 verify.py`. Observed terminal line: `VERIFY_OK: 38 exact finite-field idempotent censuses`.

Reproducibility requires only Python 3 and the files in this package. No external mathematical validation has been performed. The claim concerns the unweighted loopless complete graph, not weighted or general expander algebras.
