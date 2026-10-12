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

The theorem is algebraic. For digits \((a,c)\), the defining equation forces the unique candidate
\[
b=(a-1)!+\frac{c!-c}{a}.
\]
The checker enumerates all pairs
\[
1\le a\le60,
\qquad 0\le c\le60,
\]
and compares direct validity of this base with the stated four cases.

Independently, it enumerates every two-digit integer in bases
\[
2\le b\le100
\]
and tests the digit-factorial equation directly, comparing the complete observed set with predictions from the classification.

It also checks the exact fixed-trailing count for \(4\le c\le6\).

These are finite corroborations only. The unrestricted theorem follows from solving the factorion equation for the base and proving the digit-bound cases in `RESULT.md`.
