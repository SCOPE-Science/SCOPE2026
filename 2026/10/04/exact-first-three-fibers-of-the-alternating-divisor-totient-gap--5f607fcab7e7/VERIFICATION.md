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

The checker independently constructs prime factorizations and divisor lists for every integer
\[
1\le n\le200000.
\]
It computes
\[
\chi(n),\qquad \varphi(n),\qquad \Delta(n)=\chi(n)-\varphi(n),
\]
and verifies all four statements used in the finding:

\[
\Delta(n)\ge0;
\]

\[
\Delta(n)=0
\]
exactly for \(n=1\) and primes;

\[
\Delta(n)=1
\]
exactly for prime squares and \(8\);

and
\[
\Delta(n)=2
\]
exactly for \(27\) and twice an odd prime.

The checker also compares the first thirty computed gap values with the published initial terms of OEIS A382545.

This finite replay is a regression test, not an infinite proof. The proof for all positive integers is contained in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
