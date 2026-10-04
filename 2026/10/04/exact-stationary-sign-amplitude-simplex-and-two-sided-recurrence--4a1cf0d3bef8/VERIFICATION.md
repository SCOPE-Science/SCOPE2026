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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies the coefficient identity
\[
(a+1-b)P+(a-1+b)N
=
a(P+N)+(1-b)(P-N),
\]
which converts the invariant first-coordinate balance into the sign-amplitude simplex.

For the classical parameters
\[
(a,b)=\left(\frac{17}{10},\frac12\right),
\]
it verifies exactly
\[
r_+=\frac5{11},
\qquad
r_-=-\frac56,
\]
and
\[
(a+1-b)P+(a-1+b)N=1
\iff
11P+6N=5.
\]

It also checks the branch characteristic-polynomial signs at the classical parameters:
\[
q_+(0)<0<q_+(1),
\qquad
q_+(-1)<0,
\]
and
\[
q_-(0)<0,
\qquad
q_-(1)<0<q_-(-1).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The general eigenvalue placement and bounded bi-infinite orbit classification are analytic arguments recorded in `RESULT.md`; they are not inferred from finite numerical sampling.
