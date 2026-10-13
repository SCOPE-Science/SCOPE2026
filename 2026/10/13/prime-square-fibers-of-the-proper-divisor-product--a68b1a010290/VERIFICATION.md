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

For each prime
\[
p\le5000,
\]
the checker forms
\[
M=p^2(p+1)=B(p^2)
\]
and enumerates every positive divisor \(n\mid M\). It computes
\[
s(n)=\sigma(n)-n
\]
from an independent prime factorization and records all divisors satisfying
\[
ns(n)=M.
\]

The expected fiber is
\[
\{6,9\}
\]
when \(p=3\), and
\[
\{p^2\}
\]
for every other tested prime.

This finite replay is regression evidence only. The all-prime classification is proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
