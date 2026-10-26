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

The standalone `verify_model_domain.py` uses exact rational arithmetic. It verifies a representative point of the disputed branch and a point in the strict-concavity domain. The universal conclusion follows from the displayed eigenvalue decomposition and the equal-consumption ray proof in `RESULT.md`, not from finite sampling.

Verified algebraic identities:
- \(B=(1-\gamma)I+\gamma\mathbf1\mathbf1^\top\).
- The eigenvalue along \(\mathbf1\) is \(1+(n-1)\gamma\).
- \(2+(n-1)\gamma<0\Rightarrow1+(n-1)\gamma<-1\).
- Along \(q=t\mathbf1\), the coefficient of \(t^2\) in the consumer objective is \(-\frac n2(1+(n-1)\gamma)>0\) on that branch.

Limits: the check does not certify the source’s unrelated equilibrium or stability formulas, and no independent audit or independent validation has been performed.
