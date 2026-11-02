# Universal linear variance for temporal repetitions in the noisy voter model

## Finding

For every connected finite or countably infinite locally finite graph \(G=(V,E)\) with at least two vertices, every observation vertex \(u\), noise parameter \(0<\varepsilon\le1\), and integers \(d,L\ge1\), define

\[
R_L^{(d)}=\sum_{t=1}^{L}\mathbf1\{X_t(u)=X_{t+d}(u)\}.
\]

Under the synchronous fair-noise noisy voter dynamics defined below,

\[
\boxed{\operatorname{Var}(R_L^{(d)})\ge\frac{\varepsilon^2}{4}L.}
\]

For \(\varepsilon=1\), equality holds for every \(L,d\). For fixed \(0<\varepsilon<1\), the variance dichotomy in Lemma 2.3 and conditional central limit theorem in Theorem 2.7 of Benjamini, Helman Tov and Zhukovskii [1] give the further conclusions

\[
\boxed{\lim_{L\to\infty}\frac{\operatorname{Var}(R_L^{(d)})}{L}=v_{G,u,d,\varepsilon}\in[\varepsilon^2/4,\infty),}
\]

\[
\boxed{\frac{R_L^{(d)}-\mathbb ER_L^{(d)}}{\sqrt L}\Longrightarrow N(0,v_{G,u,d,\varepsilon}).}
\]

The constant \(v_{G,u,d,\varepsilon}\) is finite by the covariance-decay estimate in [1]. For \(\varepsilon=1\), these asymptotic conclusions hold with \(v_{G,u,d,1}=1/4\). Thus the logarithmic-variance alternative for the **unthinned** repetition statistic raised explicitly in [1, Section 2.2] cannot occur under the stated dynamics.

## Assumptions and scope

At time zero, \((X_0(v))_{v\in V}\) are independent fair \(\{0,1\}\)-valued bits. At each integer time \(t\ge1\), every vertex \(v\) independently either (i) refreshes to a new fair bit with probability \(\varepsilon\) or (ii) with probability \(1-\varepsilon\), copies the previous-time opinion of a uniformly sampled neighbor of \(v\). Choices and refresh bits at all distinct vertex-time positions are mutually independent and independent of the initial bits. The updates are simultaneous. Local finiteness and positive degree ensure that the copy distribution is well-defined. Observations are at one fixed vertex \(u\), across all times \(t\in\{1,\dots,L+d\}\). No stationarity assumption is made.

The finite-time variance bound also holds on a countable locally finite graph without requiring positive recurrence, reversibility, transitivity, finite diameter, or a finite-graph limit. The random variables in the bound are the *unmodified, consecutive-time* lag comparisons.

## Proof

**1. Conditional ancestor representation.** Set \(\sigma_t(v)=2X_t(v)-1\). For every possible initial position \((v,0)\) and refresh position \((v,s)\), let \(Y_{v,s}\) be an independent Rademacher sign. The source at \((v,0)\) is used initially, and the source at \((v,s)\) is used precisely if a refresh occurs there. Let \(\mathcal A\) denote the collection of all refresh flags and neighbor-copy arrows, but no source signs. Tracing arrows backward from each \((u,t)\) terminates after at most \(t\) steps at a unique initial position or refresh position. Write its source label as \(A_t\), measurable with respect to \(\mathcal A\). Consequently \(\sigma_t(u)=Y_{A_t}\), with source signs independent of \(\mathcal A\). This is a finite backward tracing argument even on an infinite locally finite graph.

**2. Exact conditional variance.** The equality indicator is

\[
\mathbf1\{X_t(u)=X_{t+d}(u)\}=\frac{1+Y_{A_t}Y_{A_{t+d}}}{2}.
\]

For each unordered pair of *distinct* source labels \(\{a,b\}\), let \(m_{ab}(\mathcal A)\) count how many indices \(t\in\{1,\ldots,L\}\) have \(\{A_t,A_{t+d}\}=\{a,b\}\). Terms with \(A_t=A_{t+d}\) are deterministic when conditioned on \(\mathcal A\). For distinct unordered pairs, the characters \(Y_aY_b\) are centered and orthogonal in \(L^2\) of the independent source signs, even if the pairs share one endpoint. Thus

\[
\operatorname{Var}(R_L^{(d)}\mid\mathcal A)
=\frac14\sum_{\{a,b\}:\,a\ne b}m_{ab}(\mathcal A)^2.
\tag{1}
\]

There are finitely many contributing pairs for fixed \(L,d\), so the identity requires no infinite-series interchanges.

**3. The forced distinct-pair witnesses.** For each \(t=1,\ldots,L\), let \(E_t\) be the event that \(u\) independently refreshes at both times \(t\) and \(t+d\). On \(E_t\), the ancestor pair is exactly

\[
\{A_t,A_{t+d}\}=\{(u,t),(u,t+d)\},
\]

whose entries are distinct because \(d\ge1\). Moreover these unordered pairs are different for different indices \(t\), because the smaller of their two time labels is \(t\). Each such pair contributes a squared multiplicity of at least one to (1). Therefore, for every realization of \(\mathcal A\),

\[
\operatorname{Var}(R_L^{(d)}\mid\mathcal A)
\ge\frac14\sum_{t=1}^{L}\mathbf1_{E_t}.
\]

Since each event \(E_t\) has probability \(\varepsilon^2\), whether or not different events overlap, total variance gives

\[
\operatorname{Var}(R_L^{(d)})
\ge\mathbb E[\operatorname{Var}(R_L^{(d)}\mid\mathcal A)]
\ge\frac14\sum_{t=1}^L\Pr(E_t)
=\frac{\varepsilon^2L}{4}.
\]

No sign cancellations can occur because the coefficient of each degree-two character is a **nonnegative** multiplicity. This is the crucial mechanism that prevents the sublinear variance scenario.

**4. Asymptotics.** The original model and statistic coincide with those in [1]. Equation (7) of [1] gives \(\operatorname{Var}(R_L^{(d)})=O(L)\), uniformly in \(L\) for fixed \(d,\varepsilon\). Lemma 2.3 of [1] says that its variance is either \(O(\log L)\) or is asymptotic to a strictly positive constant times \(L\). The proved lower bound rules out the first case and provides the quantitative coefficient floor. For \(S_T^{(d)}=R_{T-d}^{(d)}/(T-d)\), the same lower bound implies

\[
\operatorname{Var}(S_T^{(d)})\ge\frac{\varepsilon^2}{4(T-d)},
\]

hence \((\log T)/T^2=o(\operatorname{Var}(S_T^{(d)}))\), verifying exactly the hypothesis of Theorem 2.7(1) in [1]. Its centered, variance-standardized Gaussian limit together with the positive limiting variance coefficient yields the displayed \(\sqrt L\)-normalized CLT. When \(\varepsilon=1\), every observation \(X_t(u)\) is an independent fair bit; the lag-equality indicators form independent fair bits (their associated time edges form a forest), so the variance is exactly \(L/4\) and the standard Bernoulli CLT applies directly.

## Verification

The included `verify.py` is standard-library Python 3 code. Run `python3 verify.py` from the extracted file directory. It checks the conditional Walsh variance identity by exhaustive source assignments for 2,048 short ancestor sequences, exactly computes the finite joint dynamics using rational transition probabilities on two- and three-vertex graphs, checks the lower bound for multiple lags and lengths, and tests equality at complete refresh. In total it reports 2,084 passed exact checks.

The infinite-graph conclusion, the all-length inequality, and the asymptotic normal law do **not** follow from the finite checker. They follow from steps 1–4 and the cited theorems, respectively.

## Relationship to prior work

Benjamini, Helman Tov and Zhukovskii [1], first publicly available July 4, 2022, introduce this exact synchronous model, the lag-repetition statistic, and an upper bound on its variance. Their Lemma 2.3 proves an \(O(\log L)\)-versus-positive-linear dichotomy, and explicitly leaves open whether variance can be sublinear. Their Theorem 2.7 gives a normal limit for the **original** statistic subject to a lower-variance growth hypothesis, and also analyzes a thinned statistic with established positive variance. Neither the universal positive finite-time lower bound nor the resulting removal of the growth hypothesis for the original statistic is stated in the inspected source.

Pymar and Rivera [2] study a different, asynchronous noisy-voter density process over vertices (rather than one site's lag-repetition time series). Carro, Toral and San Miguel [3] study aggregate and network heterogeneity properties under an annealed approximation. Their accessible abstracts do not entail the displayed pathwise-ancestry variance floor. The historical literature on influences, spin systems, and orthogonal decompositions may contain a broader inequality; its application here is not claimed to be definitively historically first.

## Limitations

The bound uses unbiased independent refresh signs, strictly positive refresh probability, synchronous copying (no negations), and nonnegative indicator coefficients. It does not establish an optimal constant for \(0<\varepsilon<1\), an explicit formula for the limiting variance on general graphs, Berry–Esseen bounds, or results for biased refresh, asynchronous updates, or nonlinear majority dynamics. The normal limit for \(0<\varepsilon<1\) invokes previously proved results [1]; it is not an independent proof of the underlying mixing CLT. Source [2] and [3] were compared via abstracts/model descriptions rather than their complete bodies. Independent mathematical validation and definitive priority investigation remain outstanding.

## References

[1] I. Benjamini, H. Helman Tov, M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, Annals of Probability 51(5) (2023), 1963–1992, DOI: 10.1214/23-AOP1637. First public preprint July 4, 2022, arXiv:2207.01224. Open full text: https://arxiv.org/html/2207.01224v2 .

[2] R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478. https://arxiv.org/abs/2112.01478 .

[3] A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, Scientific Reports 6 (2016), 24775, DOI: 10.1038/srep24775. https://www.nature.com/articles/srep24775 .
