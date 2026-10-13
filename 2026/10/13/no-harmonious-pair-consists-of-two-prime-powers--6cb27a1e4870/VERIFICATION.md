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

The proof has two exact algebraic checkpoints.

First, with
\[
A=\sigma(p^a),\quad B=\sigma(q^b),\quad
U=A-p^a,\quad V=B-q^b,
\]
the equation
\[
\frac{p^a}{A}+\frac{q^b}{B}=1
\]
is equivalent to
\[
UV=p^a q^b.
\]

Second, after support forcing gives
\[
U=q^b,\qquad V=p^a,
\]
substitution yields
\[
(p-1)(q-1)p^{a-1}=p^{a-1}-1,
\]
whose left side is at least \(p^{a-1}\) and whose right side is smaller.

The packaged checker exhaustively tests all ordered prime pairs
\[
p,q\le97
\]
and exponents
\[
1\le a,b\le8
\]
using exact rational arithmetic. It finds no harmonious pair of two prime powers.

The finite scan is corroborative only; the theorem is proved for all primes and all positive exponents by the argument above.
