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

This is an analytic verification record. It covers the exact weights, both extreme fundamental functions, the localized operator norm, and the asymptotic normalization. No external or independent audit has been performed.

1. For \(d_n=16^{-n}\), the disjoint intervals satisfy \(|I_n|=|J_n|=d_n\). The source excess weight has integral \(\sum_{n\ge1}(1/n^2-d_n)\), and the target excess has integral \(\sum_{n\ge1}(4^{-n}-d_n)\). Both are finite. Since all weights are at least one, the Banach function axioms include the usual local integration bounds.
2. The interval-swapping involution preserves Lebesgue measure, so \(v_0\) and \(v_1\) have the same distribution. The source is fixed; hence the four individual minimal/maximal extrema of the pair agree between target choices. On \(16^{-N}\le a<16^{-(N-1)}\), direct integration bounds the target maximum by \((16/3)4^{-N}\), while \(\varphi_X^{\max}(a)\ge1/\sqrt{N+1}\).
3. For each finite-measure \(E\), weighted Cauchy–Schwarz gives the supremal \(L^2(w)\)-unit-ball value \((\int_E v_i^2/w)^{1/2}\); it is attained when this integral is finite and positive by a function proportional to \((v_i/w)\mathbf1_E\). Finite unions give the required diverging lower bounds if it is infinite.
4. Aligned: \(v_0^2/w=n^2\) on \(I_n\) and one elsewhere. For \(16^{-N}\le a<16^{-(N-1)}\), \((N-1)^2a\le \mathcal A_0(a)^2\le ((N-1)^2+3N)a\). This proves the displayed exact limit with normalization \(\log(1/a)\).
5. Separated: \(v_1^2/w=16^n\) on each \(J_n\), and \(\int_{J_n}v_1^2/w=1\). For every \(a>0\), choose a sufficiently deep tail whose total measure is below \(a\); then finite unions of arbitrarily many disjoint tail intervals give unrestricted local norm growth.

The finite series identities used above are \(\sum_{k\ge0}(k+1)16^{-k}=256/225\) and \(\sum_{k\ge0}k(k+1)16^{-k}=512/3375\). These follow by differentiating the geometric series; they are not experimental input.

Limits: this verification does not establish any broader class of weights, global weighted embedding, or independent novelty certification. Comparison with older unindexed examples remains a bibliographic risk.
