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
The verification target is the claim
\[
S_P(X_H)=\frac14
\]
for
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]

`verify.py` performs exact finite checks for the two non-calculus steps used by the proof:

1. It enumerates all signed facet functionals \(f,g\in\{\pm s,\pm t,\pm(s-t)\}\), computes their dual norms on all six vertices of the unit ball, and verifies
\[
\|f+g\|_*+\|f-g\|_*\le3.
\]
This is the finite certificate behind
\[
N(x+y)+N(x-y)\le3.
\]

2. It verifies exactly that \(x=(1,1)\) and \(y=(1,0)\) are unit vectors, that \(N(x+y)=2\), \(N(x-y)=1\), and that the P-angle cosine is \(1/4\).

The infinite upper bound is not inferred from sampling. It follows analytically from the facet inequality and the elementary two-case estimate on \(A=N(x+y)\), \(B=N(x-y)\) with \(A,B\le2\) and \(A+B\le3\).

Limit: no independent audit has been performed, and the literature search cannot establish absolute uniqueness.
