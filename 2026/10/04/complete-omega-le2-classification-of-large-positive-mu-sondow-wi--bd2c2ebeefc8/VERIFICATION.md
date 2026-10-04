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

The checker evaluates the defining divisibility condition
\[
p^{\nu_p(n)}\mid \frac np+\mu
\]
for every prime divisor of \(n\). It verifies the prime, prime-square, and distinct-semiprime families over a regression set of primes and then exhaustively compares the theorem with the definition for
\[
1\le\mu<300,
\qquad
2\le n\le1500,
\qquad
\Omega(n)\le2,
\qquad
n>\mu.
\]

It also checks that \(674\) is composite, that the prime-square discriminant for \(\mu=673\) is nonsquare, and that no factorization of
\[
674=(p-1)(q-1)
\]
produces distinct primes \(p<q\).

The finite sweep is only a regression check. The theorem itself follows from the exact integrality characterization and the exhaustive three-shape proof.

A successful replay prints `VERIFY_OK`.
