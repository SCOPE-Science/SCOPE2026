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

The checker computes the Lucas recurrences directly modulo each tested modulus. It determines the least period from return of the initial ordered pair and searches one full \(V\)-period for the entry point.

It tests every nonzero even parameter
\[
|p|\le40
\]
and every even modulus
\[
4\le m\le160.
\]
Whenever \(e_V(m)\) exists, it checks
\[
\pi_U(m)=\pi_V(m).
\]

It separately checks
\[
\nu_2(V_n)=1
\]
for even \(n\), and
\[
\nu_2(V_n)=\nu_2(|p|)
\]
for odd \(n\), throughout
\[
|p|\le80,\qquad 0\le n\le100.
\]
For each tested entry-point case with \(2^t\mid m\) and \(t\ge2\), it also verifies the necessary condition
\[
2^t\mid p.
\]

These finite computations are regression evidence only. The theorem for all nonzero even \(p\) and every even \(m>2\) satisfying the entry-point hypothesis is proved in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
