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
The counterexample can be replayed symbolically. For every \(\sigma\subseteq\mathbb N\), the weave energy coefficient is \(\sum_{j\in\sigma}4^{-j}+\sum_{j\notin\sigma}4^{1-j}\), hence lies in \([1/3,4/3]\). A common Bessel reconstruction family has scalar coefficients in \(\ell^2\); Cauchy--Schwarz makes the reconstruction sums absolutely convergent. Toggling only index \(j\) forces \(t_j(2^{-j}-2^{1-j})=0\), hence every \(t_j=0\), contradicting reconstruction.

For the repair, the lower weaving inequality is \(C K K^*\le T_\sigma T_\sigma^*\). Douglas factorization yields \(K=T_\sigma U_\sigma\) with \(\|U_\sigma\|^2\le1/C\); coordinate projections give a partition-dependent reconstruction family with that uniform Bessel bound. Conversely, a uniform Bessel bound \(B\) gives \(\|K^*f\|\le\sqrt B\,\|T_\sigma^*f\|\), hence a uniform lower weaving bound \(1/B\).

The 2021 and 2024 theorem statements and relevant proof steps were inspected. Each source proof chooses the factorization operator only after fixing the weaving, so the constructed reconstruction family depends on the partition. No computation beyond exact geometric sums is required. The claim does not certify any independent review and does not assess unrelated downstream statements.
