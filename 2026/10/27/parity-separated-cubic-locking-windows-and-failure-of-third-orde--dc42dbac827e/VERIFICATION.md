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

# Mathematical verification and limits

The exact itinerary identities were derived by composing \(x\mapsto(1+h)x+h\) below \(1/2\), and \(x\mapsto(1-h)x+2h\) above \(1/2\). The crossing-step inequalities follow from expansions of \(m\log(1+h)\) and \(-m\log(1-h)\), whose nonzero first-order comparison gaps remain uniform for compact cubic offsets. The stated \(q^{-2}\) displacement coefficients follow by Taylor expansion of those exact product formulas.

`CHECK.py` was executed from this package prior to writing the record and produced the accompanying `CHECK_OUTPUT.txt`. It tests odd and even denominators and three parameters inside each certified window. Checks are numerical and finite; the infinite-range proof rests on the analytic uniform error bounds. Uncertified aspects include maximal plateau endpoints, analogous conclusions for general velocity profiles, and independent review.
