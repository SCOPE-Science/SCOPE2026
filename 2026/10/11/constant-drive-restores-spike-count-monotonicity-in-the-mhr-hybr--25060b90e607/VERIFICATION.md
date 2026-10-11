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

The reset rule and model equations were checked directly against arXiv:2609.32842v1. A reset is counted only when \(h=\theta-v\) changes sign; the post-reset state is \(v^+=0\), \(\theta^+=\theta^-+\Delta\). The source's Proposition 4.14 and Conjecture 4.16 were inspected directly in the primary PDF.

For constant input \(I(t)\equiv I_0\), put \(V=v_{\mathrm{rest}}+I_0\). On a reset-free leg beginning at \((u,q)\) with \(u<V\), direct substitution verifies
\[
\Theta_{u,q}(v)
=
\left(\frac{V-v}{V-u}\right)^{1/\tau}q
+
\frac{(V-v)^{1/\tau}}{\tau}
\int_u^v f(s)(V-s)^{-1-1/\tau}\,ds.
\]
Differentiating this expression recovers
\[
\frac{d\Theta}{dv}=\frac{f(v)-\Theta}{\tau(V-v)}.
\]
Thus two legs with the same starting voltage and thresholds \(q_1>q_0\) satisfy
\[
\Theta_{u,q_1}(v)-\Theta_{u,q_0}(v)
=
\left(\frac{V-v}{V-u}\right)^{1/\tau}(q_1-q_0)>0
\]
for every finite \(v<V\).

Because the lower leg remains on the subthreshold side until its first sign-changing zero, the higher leg cannot reset earlier in voltage. If both reset, the higher leg resets at strictly larger voltage. If the lower leg never resets, neither can the higher leg. At a reset voltage \(r\), the next state is exactly \((0,r+\Delta)\), so the reset-voltage order becomes the initial-threshold order for the next leg. Constant forcing removes absolute-time dependence, allowing induction over all subsequent resets.

The proof establishes only the constant-input, \(v_0<V\) case. No numerical experiment, truncated enumeration, or simulation is used to infer an infinite-time statement. The general periodically forced conjecture remains unproved here.
