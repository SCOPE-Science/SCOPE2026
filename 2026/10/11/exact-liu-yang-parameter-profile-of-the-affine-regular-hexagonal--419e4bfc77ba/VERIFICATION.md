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
The verification target is
\[
L'_Y(\lambda,X_H)=1+2m-3m^2,
\qquad
m=\min\{\lambda,1-\lambda\},
\]
for
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]

The analytic proof reduces the unit-sphere supremum to ordered vertex pairs by convexity on each product of two boundary edges. `verify.py` then checks the finite polyhedral step with exact rational arithmetic. It reconstructs all parameter breakpoints where absolute facet functionals can exchange dominance, derives the active quadratic on each open cell, proves that only the three branches in `RESULT.md` occur, verifies domination by the proposed branch on \(0\le m\le1/2\), and checks the uniform attaining pair, the peak \(4/3\), and the balanced value \(5/4\).

No sampling is used to establish the infinite statement. The verifier certifies only the finite facet decomposition after the analytic convexity reduction.

Limit: no independent audit or independent validation has been performed.
