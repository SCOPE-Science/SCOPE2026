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

The universal statement is established by the symbolic proof in `RESULT.md`. The accompanying `verify_gorenstein_two_heavy.py` is a separate finite regression check.

It reconstructs the finite divisor-core candidates from \(k\mid r\), \(1\le g\le k+2\), and factorizations \(AB=gk+1\); compares them with direct Gorenstein divisibility; evaluates the two heavy cyclic-quotient ages; checks terminality; and verifies the complete non-terminal boundary and the formula \(\tau(2r)+1\) for every \(2\le r\le100\).

Executed output:

`VERIFY_OK r=2..100; finite divisor-core parameterization, canonicality, terminal criterion, boundary family and count all agree with direct Gorenstein divisibility and chart ages`

Limits: this computation is finite and therefore cannot certify the universal quantifiers by itself. The infinite result rests on the exact arithmetic bijection and Reid--Tai proof in `RESULT.md`.
