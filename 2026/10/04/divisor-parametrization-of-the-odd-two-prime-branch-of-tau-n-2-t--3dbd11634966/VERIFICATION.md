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
Run `python3 verify.py`.

For every
\[
0\le t\le20,
\]
the checker independently tests the primality of
\[
2\cdot3^t+1,
\]
brute-forces every nonnegative solution of
\[
ab+2a+2b+1=3bt
\]
inside bounds that are exhaustive in this finite range, and compares those solutions with the divisor parametrization
\[
b=d-2,\qquad
a=3t-2-\frac{3(2t-1)}d.
\]

For every admissible prime \(t\), it also checks the exact counts
\[
\tau(3(2t-1))-1
\]
for the full nonnegative system and
\[
\tau(3(2t-1))-2
\]
for the \(a,b\ge2\) branch.

Finally, it verifies the arithmetic-function equality from prime exponents:
\[
\tau(n^2)=(2a+1)(2b+1)
\]
and
\[
\tau(\varphi(n))=3(a+t)b.
\]

The finite replay is not used to prove the infinite theorem. The proof is the reversible product identity in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
