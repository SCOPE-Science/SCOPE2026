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
The checker reconstructs the Schröder-polynomial coefficient rows independently from the recurrence
\[
r_n(q)=qr_{n-1}(q)+\sum_{j=0}^{n-1}r_j(q)r_{n-1-j}(q)
\]
and compares them with
\[
a_{n,k}=\binom{2n-k}{k}C_{n-k}
\]
for
\[
1\le n\le120.
\]

It checks the exact adjacent-ratio identity for every coefficient in that range, verifies the unique-mode/two-mode classification, and checks through
\[
n\le10000
\]
that two-term plateaus occur exactly when
\[
n(n+1)/2
\]
is a square, equivalently when
\[
(2n+1)^2-8s^2=1.
\]

It also verifies the source's first four nontrivial Schröder polynomials and the first Pell plateau dimensions
\[
1,8,49,288,1681,9800.
\]

These finite tests are regression evidence. The all-parameter proof is the diagonal-deletion bijection and adjacent-ratio analysis in `RESULT.md`.
