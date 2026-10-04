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

The primary theorem and definitions were checked against the open-access arXiv and published versions.

For the counterexample, set \(\mathcal H=\mathbb R^2\), \(I=\{1\}\), \(V_1=W_1=\mathcal H\), and \(v_1=w_1=1\). The two possible outer weavings are identical and satisfy
\[
\|P_{\mathcal H}x\|^2=\|x\|^2.
\]
Thus the fusion pair is woven with exact bounds \(1,1\).

The local frames \((e_1,e_2)\) and \((e_2,e_1)\) are orthonormal bases, so their lower and upper frame bounds are all \(1\). Ordinary atomwise weaving allows the atomic selection that yields \((e_1,e_1)\). For \(x=e_2\),
\[
|\langle e_2,e_1\rangle|^2+|\langle e_2,e_1\rangle|^2=0,
\]
so this weaving is not a frame. This directly disproves the forward implication of the stated equivalence.

For the reverse implication, an arbitrary outer subset \(\sigma\subseteq I\) determines the block-constant atomic subset containing all \((i,j)\) with \(i\in\sigma\). If the flattened local systems are atomwise woven with bounds \(L,U\), this particular atomic weaving has those bounds. Uniform local bounds \(a>0\) and \(b<\infty\) imply \(aE_\sigma\le Q_\sigma\le bE_\sigma\), hence the corresponding fusion weaving has bounds \(L/b\) and \(U/a\).

The earlier arXiv:1802.03352 Lemma 2.2 was checked separately: it selects complete local blocks according to partitions of the outer fusion index. It therefore supports the blockwise replacement but does not cover atomwise weaving.

Limit: no claim is made about stronger hypotheses that might force arbitrary atomwise local weaving from fusion weaving.
