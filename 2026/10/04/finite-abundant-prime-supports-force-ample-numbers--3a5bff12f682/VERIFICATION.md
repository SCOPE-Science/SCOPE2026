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

The checker evaluates Fink's defining recurrence directly on exponent vectors for the displayed odd ample example
\[
3^9 5^5 7^2 11 13.
\]
It verifies
\[
a(n)=436791402496>430996190625=n.
\]

It also checks exactly that the same support
\[
Q=\{3,5,7,11,13\}
\]
satisfies
\[
\prod_{q\in Q}\frac{q}{q-1}
=
\frac{1001}{384}>2.
\]

Finally it numerically locates the unique \(\alpha_Q>1\) satisfying \(Z_Q(\alpha_Q)=2\) and confirms, at a nearby point \(s>\alpha_Q\), the characteristic inequality
\[
\frac{Z_Q(s)}{2-Z_Q(s)}>Z_Q(s-1),
\]
which is incompatible with \(a(n)\le n\) for every \(Q\)-smooth integer.

The numerical root check is only a regression illustration. The proof for arbitrary finite \(Q\), and the all-\(k\) corollary, are analytic and do not depend on finite computation.

A successful replay prints `VERIFY_OK`.
