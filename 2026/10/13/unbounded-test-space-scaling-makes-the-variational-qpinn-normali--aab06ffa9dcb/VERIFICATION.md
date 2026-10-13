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
# Verification

The verification is analytic. Let \(v\in\mathcal H_M\) and \(c\in\mathbb R\). Because the source defines \(\mathcal H_M\) as a span, \(cv\in\mathcal H_M\). Because the source's energy integral is linear in the test function,
\[
\mathcal E(\Theta,cv)=c\mathcal E(\Theta,v).
\]
Thus its squared second moment scales by \(c^2\), proving the A8 alternative exactly.

For Eq. (4.109), differentiating \(\mathcal E(\Theta,v)\) with respect to model parameters leaves linearity in \(v\) unchanged. Hence the first component of the difference between the nonlinear and parameter-linearized observables is a linear functional \(D_t\) on \(\mathcal H_M\). If \(D_t(v)\ne0\), then \(|D_t(cv)|=|c|\,|D_t(v)|\), so the supremum over the full span is infinite. No numerical sampling is needed or used.

The checked source boundaries are important: Assumption A10 normalizes only the selected basis functions, while Lemmas 4.1--4.2 explicitly invoke \(\|v\|_{1,B}\le1\). The theorem-level supremum is nevertheless written over all of \(\mathcal H_M\). The proof here establishes only that a bounded normalized test domain is necessary for a nontrivial uniform statement; it does not certify a repaired theorem.
