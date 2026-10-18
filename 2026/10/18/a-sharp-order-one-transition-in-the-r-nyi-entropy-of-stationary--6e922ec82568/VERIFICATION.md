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

# Verification of the stated theorem

`verify.py` (Python standard library only) independently forms stationary transition matrices using exact rational arithmetic and compares \(P^t\) and \(Q_t\) against the projection formula for state counts two through five and horizons zero through six. It then checks selected entropy sequences for orders on both sides of one, numerically solves the asserted single-maximizer equation, tests the large-lag coefficients, and compares the near-Shannon asymptotic location and height with decreasing distances from order one.

Reproduction: execute `python3 verify.py` from the extracted package directory. The reported result was `PASS 654 finite tests; analytic hypotheses and infinite statements require proof`. The example with \(\pi=(0.9,0.1)\), \(r=0.7\) had its largest sampled effective support at lag five, approximately \(2.605443373946\), exceeding its independence limit \(2.56\).

Finite tests do not establish a theorem for all state vectors, Rényi orders or lags. The sign arguments, uniqueness proof, endpoint divergence, exact entropy derivative, and implicit-function calculation in `RESULT.md` are the mathematical evidence for those quantifiers. The scope does not include general non-refresh kernels or a claim of independent verification.
