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
The verification target is the exact profile
\[
m_H(\epsilon)=
\begin{cases}
2-\epsilon/2,&0\le\epsilon\le4/3,\\
4-2\epsilon,&4/3\le\epsilon\le2,
\end{cases}
\]
and
\[
\rho_{X_H}^{a}(\epsilon)=1-\frac12m_H(\epsilon)^2
\]
for
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]

`verify.py` checks the finite algebra behind the analytic proof with exact rational arithmetic. It verifies the two displayed linear symmetries on the defining facet functionals, the same-edge, adjacent-edge, next-nearest-edge and opposite-edge formulas, feasibility and unit norm of the two explicit attaining families at rational test parameters spanning both regimes and their endpoints, and the exact branch crossing at \(\epsilon=4/3\).

The continuum exhaustion is proved in `RESULT.md` by the symmetry classification of all six unit-sphere edges; it is not inferred from numerical sampling.

Limit: no independent audit or independent validation has been performed.
