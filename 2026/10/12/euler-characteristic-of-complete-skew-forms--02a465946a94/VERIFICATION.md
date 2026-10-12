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
The checker recursively enumerates ordered matchings for
\[
2\le n\le10
\]
and verifies that the number of distinct fixed-point labels is
\[
\frac{n!}{2^{\lfloor n/2\rfloor}}.
\]

It separately evaluates the recurrence
\[
F(0)=F(1)=1,
\qquad
F(n)=\binom n2F(n-2)
\]
through
\[
n=80
\]
and verifies the factorial closed form exactly.

The two finite checks validate the combinatorial implementation only. The infinite theorem follows from the symbolic fixed-point classification and Bialynicki--Birula decomposition in `RESULT.md`.
