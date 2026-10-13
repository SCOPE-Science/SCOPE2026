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

The checker uses only integer arithmetic and Python rational arithmetic. It verifies:

\[
\sigma(31^4)=954305=5\cdot11\cdot17351,
\]
that \(17351\) is prime by trial division, and the exact abundancy identity
\[
I\!\left(2\cdot5^2\cdot31^4\cdot11^2\cdot17351^2\right)
=
\frac{120128746647}{56859400510}
>
\frac{21}{10}.
\]

It also checks, for every prime \(r\le10000\) with \(r\equiv1\pmod3\) and every even exponent \(2\le e\le30\), that
\[
3\mid\sigma(r^e)
\quad\Longleftrightarrow\quad
e\equiv2\pmod6.
\]

The finite congruence grid is regression evidence, not the infinite proof. The all-prime argument is the reduction of the geometric sum modulo \(3\) in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
