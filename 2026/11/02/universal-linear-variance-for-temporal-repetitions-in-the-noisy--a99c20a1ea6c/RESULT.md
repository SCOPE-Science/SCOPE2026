# Degree- and lag-independent variance bound for temporal repetitions in the noisy voter model

## Finding

Let \(G=(V,E)\) be a connected finite or countably infinite locally finite graph with at least two vertices, let \(u\in V\), and take integers \(d,L\ge1\). Set
\[
R_L^{(d)}=\sum_{t=1}^{L}\mathbf1\{X_t(u)=X_{t+d}(u)\}.
\]
In the synchronous fair-noise voter model below, for every \(0<\varepsilon\le1\),
\[
\operatorname{Var}(R_L^{(d)})\ge \varepsilon^2 L/4.
\]
This strengthens the degree- and lag-dependent lower bound of [2]. Unlike that bound, this estimate is independent of the degree of \(u\) and the lag, and applies to all sample lengths, including \(L\le d\). At \(\varepsilon=1\) the bound is attained for every \(L,d\).

As an application, \(\operatorname{Var}(R_L^{(d)})/L\) converges to a finite constant \(v_{G,u,d,\varepsilon}\ge\varepsilon^2/4\), and \((R_L^{(d)}-\mathbb E R_L^{(d)})/\sqrt L\) converges in distribution to \(N(0,v_{G,u,d,\varepsilon})\). The qualitative linear variance and unthinned CLT conclusions for \(0<\varepsilon<1\) were already obtained in [2] using [1].

## Assumptions and scope

Initially the vertex opinions \(X_0(v)\) are independent fair bits. At each time \(t\ge1\), simultaneously at each vertex \(v\), either refresh to a fresh independent fair bit with probability \(\varepsilon\), or copy the previous-time opinion of a uniformly sampled neighbor with probability \(1-\varepsilon\). The refresh flags, sampled neighbors, and fair bits are independent across vertex-time points, and independent of the initial bits. Positive finite degree makes the uniform copy rule well-defined. No stationarity is assumed.

## Proof

Write \(\sigma_t(v)=2X_t(v)-1\). Let \(\mathcal A\) contain all refresh flags and copy choices, but none of the fair signs. By tracing the copy choices backwards from \((u,t)\), the observed sign is \(Y_{A_t}\) where \(A_t\) is its initial or refresh source, measurable with respect to \(\mathcal A\), and \(Y_a\) are mutually independent Rademacher signs independent of \(\mathcal A\). The tracing takes at most \(t\) steps, including on an infinite graph.

The repetition indicator at index \(t\) equals \((1+Y_{A_t}Y_{A_{t+d}})/2\). Equal-source terms are deterministic conditional on \(\mathcal A\). For distinct source labels \(a,b\) let \(m_{ab}\) count the indices with unordered pair \(\{a,b\}\). The characters \(Y_aY_b\) have conditional mean zero and are pairwise orthogonal across distinct unordered pairs, because some independent centered sign occurs exactly once in the product. Hence
\[
\operatorname{Var}(R_L^{(d)}\mid\mathcal A)
=\tfrac14\sum_{\{a,b\}:a\ne b} m_{ab}^2.
\]
Only finitely many terms contribute. If \(u\) refreshes at both \(t\) and \(t+d\), its pair of labels is exactly \(\{(u,t),(u,t+d)\}\). Each such event contributes at least one to the sum of squared multiplicities, and pairs from different such indices are distinct by their smaller time label. Each event has probability \(\varepsilon^2\) even though the events can overlap. Taking expectations and using total variance yields the claimed bound.

For \(0<\varepsilon<1\), equation (7) and Lemma 2.3 of [1] bound the variance by \(O(L)\) and show that it is either \(O(\log L)\) or \((v+o(1))L\) for some \(v>0\). The lower bound rules out the former and gives the floor on \(v\). The statistic \(S_T^{(d)}\) of [1] is \(R_{T-d}^{(d)}/(T-d)\); its variance is at least \(\varepsilon^2/[4(T-d)]\). Thus \((\log T)/T^2=o(\operatorname{Var}(S_T^{(d)}))\), as required by Theorem 2.7(1) of [1]. The variance-standardized normal limit there and the variance asymptotic give the claimed limit with normalization \(\sqrt L\).

At \(\varepsilon=1\) the observed signs are independent over time. The edges \(\{t,t+d\}\), \(1\le t\le L\), form disjoint paths in the residue classes modulo \(d\). The independent vertex signs yield independent fair edge products: given those products, the vertex signs are freely specified at precisely one root of each path and then uniquely determined on the rest. The repetitions are therefore independent fair indicators with variance \(1/4\), giving equality and the ordinary Bernoulli CLT.

## Relationship to prior work

Benjamini, Helman Tov and Zhukovskii [1, §2.2] asked whether the *unthinned* statistic could have sublinear variance. For \(0<\varepsilon<1\) and \(L\ge d+1\), [2] showed that its variance is at least \(\frac12\varepsilon^{\Delta+4}(1+\lfloor(L-d-1)/(2d+2)\rfloor)\), where \(\Delta\) is the finite degree at the observation site. Their proof allows arbitrary initial laws independent of the updates for that lower bound, and obtains the unthinned CLT from [1] for independent fair initial bits. The present contribution is the stronger quantitative bound on the stated fair-start model, not the first qualitative resolution of the sublinear-variance question or of the conditional CLT. Conditioning on all ancestries exposes nonnegative squared multiplicities and does not require isolating individual refresh bits from their descendants.

## Verification and limitations

The accompanying `verify.py` checks finite instances of the variance identity and bound with independent sign enumeration and exact finite-state rational dynamics. The universal inequality follows from the proof, not from these cases. No optimality is asserted for \(0<\varepsilon<1\); no results for biased or asynchronous updates are claimed. The asymptotic step uses the cited theorem rather than an independent CLT proof.

## References

1. I. Benjamini, H. Helman Tov and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, Ann. Probab. 51(5) (2023), 1963–1992, DOI [10.1214/23-AOP1637](https://doi.org/10.1214/23-AOP1637), [arXiv:2207.01224v2](https://arxiv.org/html/2207.01224v2).
2. *Uniform linear variance for single-vertex noisy-voter repetitions on locally finite graphs*, [Resultary 2026-10-25, record 3fff36789a8d](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-uniform-linear-variance-for-single-vertex-noisy-voter-repetition--3fff36789a8d/RESULT.md).
