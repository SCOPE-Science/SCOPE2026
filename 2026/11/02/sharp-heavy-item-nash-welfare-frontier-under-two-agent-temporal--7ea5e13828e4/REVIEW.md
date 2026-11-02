# Self-review

## Correctness — PASS

The exact theorem is stated with two agents, identical positive additive valuations, at least two goods, the heavy-item fraction \(\delta\ge 1/2\), and offline integral two-way partition benchmarking. The key premises have independent simple proofs: any offline partition containing a good of value \(h\ge V/2\) has product at most \(h(V-h)\); EF1 imposes \(x\ge(V-h)/2\) on the smaller final bundle when the larger contains that item; monotonicity of \(x(V-x)\) for \(x\le V/2\) yields the claimed fraction. The boundary where the heavy good is in the smaller bundle is handled as equality of the two loads. For \(h<V/2\), a separate elementary EF1/AM–GM argument proves the uniform claim. Three positive goods \((q,q,h)\) force the relevant temporal allocation, and exact products prove attained equality. The finite verifier (21,840 sequences and 1,040,454 EF1 final partitions) supports but is not invoked in place of the infinite proof.

## Originality — PASS with residual priority risk

Primary full texts and theorem/proof passages were inspected, including Yang et al. (2026) §§2–4 and appendix, Elkind et al. (2024/2025) existence and p-mean sections, Barman et al. (2018) Lemma 1 and proof, and Feng–Hu–Li (2026) §§2 and 5. The closest general guarantees use a population-uniform ratio \(e^{-1/e}\) and a smaller-item hypothesis \(\delta\le1/2\). The latter covers the endpoint and must not be counted as novel; the open heavy-item region \(\delta>1/2\) and its exact temporal minimax frontier are not explicitly established in the inspected texts. Previously derived formulas for a single exceptional good and equal-valued residual goods can realize sharp examples but do not imply the universal lower bound for arbitrary positive good values. The 2026 results on least-loaded updates and the older temporal EF1 feasibility theorem are not re-claimed. An unindexed equivalent proof or a specialized consequence hidden elsewhere in broader results remains possible.

## Mathematical value — PASS

The result closes a natural parameter-dependent welfare question raised by work that combines exact EF1, irrevocable arrivals, and Nash-welfare optimization: it determines the **entire dominant-good sharp frontier**, not merely a special numerical case. The three-good lower bound persists even with knowledge of the future and under randomization, while a known elementary online rule meets the bound. This distinguishes the cost of *temporal* fairness from final-time EF1 without relying on an arbitrary finite census. The full arbitrary-valued upper bound is essential: limiting attention to one-heavy-plus-unit-good inputs would supply examples but not certify minimax optimality.

## Closest sources and limitations

- Yang et al., arXiv:2609.03846 (first public 2026-09-03): online feasibility, population-uniform and small-item NSW results, five-item temporal counterexample; no heavy-item sharp frontier stated.
- Barman, Krishnamurthy and Vaish, arXiv:1707.04731 (2018), Lemma 1: known coarse universal EF1/NSW factor.
- Elkind et al., arXiv:2410.14593 (2024/2025): temporal EF1 existence and hardness under more general valuation models.
- Feng, Hu and Li, ICALP 2026, DOI 10.4230/LIPIcs.ICALP.2026.90: alternative proof of coarse EF1 gap, not a two-agent heavy-item curve.

Only identical positive additive utilities of two agents and one-by-one irrevocable arrivals are proved. The claim is not a classification of all extremizers, and the small-item bound outside the sharp heavy regime is not asserted new or sharp. Independent confirmation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
