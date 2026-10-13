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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier constructs the fixed point through length \(3^{11}\) and checks the digit/coordinate recurrence. It evaluates the exact recursive difference sets \(D_q\) for every \(0\le q\le20000\), compares them with the claimed exceptional-family classification, and independently samples the true differences in the fixed-point prefix for \(q\le1000\).

It also checks the substitution-language translation identity through eight levels. Finally, sliding-window Parikh counts are computed directly for every factor length through \(250\) and for selected larger lengths surrounding the exceptional powers.

These computations are stress tests of the symbolic proof. The theorem for all lengths follows from the exact recurrence and boundary analysis, not from finite extrapolation.

Independent audit has not been performed.
