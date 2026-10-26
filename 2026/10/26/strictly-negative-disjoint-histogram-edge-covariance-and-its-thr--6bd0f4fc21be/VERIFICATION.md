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

# Reproducibility and boundaries

Run `python3 verify_disjoint_covariance.py` in a standard Python 3 environment. The script requires only the standard library, computes the exact conditional folded-binomial means as rational numbers, and enumerates all two-block total allocations for six rational probability vectors at each \(N=1,\ldots,12\). It completed 72 strict-sign comparisons successfully. The independent analytical proof covers every integer \(N\ge1\), every positive four-cell probability profile, every allowed residual mass, and all fixed-profile asymptotic regimes; exhaustive testing over that infinite domain is impossible.

For additional non-certificate numerical orientation, the balanced-pair case at \((u,v)=(1/4,1/2)\) gives \(-0.05665803\), \(-0.05636616\), \(-0.05631791\) at \(N=128,512,1024\), approaching \(-\sqrt{1/8}/(2\pi)\). These values can be independently reproduced by summing \(g_{1/2}(k)g_{1/2}(\ell)\) against the multinomial two-total law; no numerical approximation is used in the proof.

Known limits: the claim is restricted to uncentered disjoint edges and fixed cell probabilities; no shrinking-imbalance crossover theorem or general-reference centered null variance is claimed. Independent audit has not been performed.
