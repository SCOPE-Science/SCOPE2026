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

The checker reconstructs the complementary divisor pairs
\[
P_i=\{2^i,15\cdot2^{a-i}\},
\qquad
Q_i=\{3\cdot2^i,5\cdot2^{a-i}\}
\]
for every tested exponent and verifies that each selected pair multiplies to
\[
15\cdot2^a.
\]
It then checks that the selected divisors are distinct, complement-closed, and sum exactly to
\[
30\cdot2^a.
\]

The replay covers \(a=2,\ldots,1002\), including all exceptional cases, and also checks the five closed-form fixed-plus-geometric identities appearing in `RESULT.md`.

A successful replay prints `VERIFY_OK`.

The finite replay is not the proof of the infinite statement. Exhaustiveness over all \(a\ge2\) follows from the five symbolic residue-class formulas modulo \(5\) plus the explicitly listed small values.
