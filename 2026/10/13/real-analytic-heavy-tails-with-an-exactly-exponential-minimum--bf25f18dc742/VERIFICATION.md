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

The final claim was checked symbolically from the defining hazards.

1. **Regularity and positivity.** The map \(t(x)=\log\log(x+e^e)\) is real-analytic for \(x\ge0\). Logistic composition gives \(0<h_i(x)<1\) and real-analytic \(h_i\). Hence \(R_i\) and \(f_i=h_i e^{-R_i}\) are real-analytic on \((0,\infty)\), with \(f_i>0\).
2. **Exact minimum.** The logistic identity gives \(h_1+h_2=1\), hence \(R_1+R_2=x\). Independence therefore gives survival \(e^{-x}\) for the minimum for every \(x\ge0\).
3. **Proper factors.** Each hazard is at least \(1/2\) on infinitely many intervals whose lengths in the \(x\)-coordinate diverge, so each cumulative hazard tends to infinity.
4. **Heavy tails.** On alternating intervals one hazard is at most \(e^{-t}\). At the right endpoints this yields a cumulative-hazard ratio tending to zero. For every \(\lambda>0\), the bound \(\mathbb E e^{\lambda X_i}\ge e^{\lambda x-R_i(x)}\) along that subsequence diverges.
5. **Scope limit.** No claim is made for arbitrary target laws or for long-tailed, regularly varying, or subexponential factors. No finite computation is used as proof.
