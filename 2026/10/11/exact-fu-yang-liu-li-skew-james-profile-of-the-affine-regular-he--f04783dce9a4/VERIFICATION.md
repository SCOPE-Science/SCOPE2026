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
The analytic proof reduces the full statement to four edge cases for \(0<t\le1\).

The exact target is
\[
L=\frac{t^2+t+1}{t+1}.
\]
After moving
\[
x=(1,a)
\]
to the fixed edge, the two nontrivial cases are:

\[
y=(c,1):
\quad
A=\max\{1+tc,a+t\},
\quad
B=1-ta+\max\{0,t-c\},
\]
and
\[
y=(-b,1-b):
\quad
A=-tb+\max\{1,a+t\},
\quad
B=\max\{t+b,1+t-ta\}.
\]

In the first case, \(A>L\) and \(B>L\) force simultaneously
\[
a>\frac1{1+t}
\quad\text{and}\quad
a<\frac1{1+t}.
\]
In the second case, the two possible branches of \(B>L\) force either
\[
a>1
\]
or
\[
a<\frac1{1+t},
\]
each contradicting the lower inequality from \(A>L\).

The explicit equality pair
\[
x=(1,0),
\qquad
y=\left(\frac{t}{1+t},1\right)
\]
has both transformed norms equal to \(L\).

`verify.py` uses exact `Fraction` arithmetic. It verifies the two generating isometries, the canonical edge formulas, all four edge-class inequalities on a large rational test family, both equality families, and the reciprocal formula on rational parameters. These finite checks are supplementary; the displayed inequalities prove the continuum result.

No independent audit or independent validation has been performed.
