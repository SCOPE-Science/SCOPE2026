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

The proof was checked directly from the exact-proximal specialization of the source NIPG update on \(F(x)=a x^2/2\). The identities checked are the gradient step, coincidence of \(A_1\) and \(A_2\), equivalence of the curvature test to \(a t_k>c_0\), the exact reset \(t_{k+1}=c_1/a\), and the objective ratio \((1-a t_k)^2\).

`artifacts/verify_nipg_spike.py` uses exact rational arithmetic to replay the boundary expansion, large transient spikes, reset, and sharp safety cap. The finite replay does not prove the quantified statement; the algebra in `RESULT.md` does.
