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
The arbitrary-field proof is symbolic.

The packaged checker `artifacts/verify.py` exhaustively verifies
\[
q\in\{2,3,5\}
\]
and
\[
n\in\{2,3,4\}.
\]

For every tested pair it constructs the automorphism group from the defining bracket, computes all element orbits, and checks the closed representative and orbit-size formulas.

For \(n=2\), the expected orbit count is
\[
2q.
\]
For every tested \(n\ge3\), it is
\[
2q+2.
\]

The checker also verifies that the orbit sizes sum to
\[
q^n.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.
