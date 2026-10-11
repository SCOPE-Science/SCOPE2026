# A concentration criterion and Baire dichotomy for product measures on the Hilbert-cube shift

## Finding
Let \(K=[0,1]\), \(X=K^{\mathbb Z}\), and let \(\sigma:X\to X\) be the bilateral shift. Fix any metric compatible with the product topology. For an arbitrary sequence of Borel probability measures \((\nu_j)_{j\in\mathbb Z}\) on \(K\), consider the possibly non-invariant product measure \(\mu=\bigotimes_{j\in\mathbb Z}\nu_j\). For \(0<r<1\) define the maximal marginal concentration
\[
q_j(r)=\max_{a\in K}\nu_j\bigl(K\cap[a-r,a+r]\bigr).
\]
Then \(\mu\) is expansive in the measure-theoretic sense if and only if
\[
\exists\,r\in(0,1):\qquad\sum_{j\in\mathbb Z}\bigl(1-q_j(r)\bigr)=+\infty.
\]
Moreover, in the compact metrizable parameter space \(\mathcal P=\prod_{j\in\mathbb Z}\operatorname{Prob}(K)\), with each factor carrying its weak topology, the expansive product measures contain a dense \(G_\delta\). Their non-expansive complement is meagre yet dense. Both the expansive and non-expansive classes are dense even when restricted to parameter families in which **every** marginal is nonatomic and has full support.

## Assumptions and scope
Measure-theoretic expansivity means that for some \(\delta>0\), every two-sided Bowen ball
\[
\Gamma_\delta(x)=\{y\in X:d(\sigma^n x,\sigma^n y)\le\delta\text{ for every }n\in\mathbb Z\}
\]
has \(\mu\)-measure zero, for every \(x\in X\). No invariance, identical distribution, mixing, or stationarity is assumed. We use the weak product topology on the independent-marginal parameter space, not the weak topology on all measures on \(X\). Density among families of full-support nonatomic marginals is understood relative to this parameter topology. The source motivating the questions of non-invariant expansive measures and their topology was first public on 2025-06-26, with primary classification 37B05.

## Proof
**1. Replace Bowen balls by uniform coordinate boxes.** For \(0<r<1\) and \(x\in X\), set
\[
C_r(x)=\{y\in X:|x_j-y_j|\le r\text{ for every }j\in\mathbb Z\}.
\]
By compatibility of the metric with the product topology and compactness of \(X\), for each \(\delta>0\) there is \(r>0\) sufficiently small that \(C_r(x)\subseteq\Gamma_\delta(x)\) for every \(x\). Indeed, control of finitely many coordinates makes two points uniformly \(\delta\)-close, and the same uniform bound on all coordinates remains true after every shift. Conversely, for every \(r>0\), uniform continuity of the zeroth-coordinate projection gives \(\delta>0\) for which \(\Gamma_\delta(x)\subseteq C_r(x)\): apply the projection estimate to all shifted pairs. Thus measure expansivity is equivalent to existence of some \(r>0\) with \(\mu(C_r(x))=0\) for every \(x\).

**2. Exact independent-coordinate criterion.** The sets in the product defining \(C_r(x)\) decrease over finite coordinate ranges, so continuity from above and independence give
\[
\mu(C_r(x))=\prod_{j\in\mathbb Z}\nu_j\bigl(K\cap[x_j-r,x_j+r]\bigr).
\]
The centered closed-interval mass is upper semicontinuous as a function of the center, so its maximum \(q_j(r)\) is attained. Choosing a maximizing center independently for each coordinate proves
\[
\sup_{x\in X}\mu(C_r(x))=\prod_{j\in\mathbb Z}q_j(r).
\]
The interval \(K\) can be covered by \(N_r<\infty\) closed intervals of radius \(r\), hence \(q_j(r)\ge1/N_r\) uniformly in \(j\). For numbers \(q\in[1/N_r,1]\), elementary logarithmic inequalities give
\[
1-q\le-\log q\le N_r(1-q).
\]
Consequently \(\prod_jq_j(r)=0\) exactly when \(\sum_j(1-q_j(r))=+\infty\), proving the characterization.

**3. A dense \(G_\delta\) of expansive product laws.** Fix \(r_0=1/4\) and let \(q(\nu)=\max_{a\in K}\nu(K\cap[a-r_0,a+r_0])\). The map \(q:\operatorname{Prob}(K)\to[0,1]\) is upper semicontinuous: for weakly convergent \(\nu_n\to\nu\), take a convergent subsequence of maximizing centers and apply the Portmanteau inequality to slightly enlarged closed intervals, then shrink them. Therefore \(1-q\) is lower semicontinuous. For any finite set \(F\subset\mathbb Z\), the function \(\sum_{j\in F}(1-q(\nu_j))\) is lower semicontinuous. It follows that
\[
\mathcal E_0=\left\{(\nu_j):\sum_{j\in\mathbb Z}(1-q(\nu_j))=+\infty\right\}
=\bigcap_{M=1}^\infty\ \bigcup_{F\subset\mathbb Z\,\mathrm{finite}}
\left\{(\nu_j):\sum_{j\in F}(1-q(\nu_j))>M\right\}
\]
is a \(G_\delta\). It is dense: any basic open condition fixes only finitely many marginal coordinates, and all other marginals can be replaced by Lebesgue measure, for which \(q=1/2\). The criterion implies \(\mathcal E_0\) consists of expansive laws. Since \(\mathcal P\) is compact metrizable, the non-expansive class is contained in the meagre complement of \(\mathcal E_0\).

**4. Density of non-expansive laws with good marginals.** Fix a nonempty basic open subset of \(\mathcal P\), constraining a finite set \(F\) of coordinates. Each constrained marginal can be chosen nonatomic, with full support, inside its prescribed weak neighborhood (smooth an arbitrary law and mix in a small positive Lebesgue component). For each \(j\notin F\), choose \(\varepsilon_j\in(0,1/2)\) with \(\sum_{j\notin F}\varepsilon_j<\infty\), and choose \(\rho_j>0\) with \(\rho_j\to0\) as \(|j|\to\infty\). Set
\[
\nu_j=(1-\varepsilon_j)\operatorname{Unif}[0,\rho_j]+\varepsilon_j\operatorname{Leb}[0,1].
\]
Every such marginal is nonatomic and has full support. Choose \(x_j=0\) for the unconstrained coordinates, and choose each constrained \(x_j\) inside the support of its marginal. For every fixed \(r>0\), all but finitely many \(j\notin F\) satisfy \(\rho_j<r\), hence \(\nu_j([0,r])\ge1-\varepsilon_j\). All exceptional factors are strictly positive, and \(\prod_{j\notin F}(1-\varepsilon_j)>0\) because the series converges. Consequently \(\mu(C_r(x))>0\) **for every** \(r>0\). By step 1 the law is not expansive. This proves density of non-expansive laws even with full-support nonatomic marginals. The earlier density construction can similarly approximate constrained marginals by such good ones while assigning Lebesgue measure in the tail, proving density of good expansive laws.

## Verification
All assertions above follow by compactness, continuity from above, Portmanteau, the countable-product formula, and elementary series/product inequalities. There is no finite computation or parameter cutoff on which the result depends. A direct boundary sanity check is obtained by comparing the all-Lebesgue product, for which each \(q_j(1/4)=1/2\), with the summably contaminated shrinking-interval products of step 4: both have full-support nonatomic marginals, but only the first is expansive. This verifies that support and atomlessness alone cannot decide measure expansivity. The proof does not infer genericity in the full space of all probability laws from genericity in the product-law parameter space.

## Relationship to prior work
Pedrosa–Rego–Trilles study expansive measures for regular flows, non-invariant measures, and the topological complexity of expansive-measure collections [1]. Their theorem for flow measures does not furnish a necessary and sufficient concentration criterion for arbitrary independent nonstationary marginals of a discrete Hilbert-cube shift. Morales gives foundational measure-expansivity terminology [2], but no equivalent nonstationary product classification was established from the inspected relevant source material. Lacerda's subsequent October 2026 preprint [3] proves expansivity for a product Lebesgue law on the Hilbert cube and obtains genericity in an ambient probability-measure space; the currently accessible abstract and opening theorem statements do not state the present exact two-sided concentration criterion or density of full-support nonatomic non-expansive product laws. The complete text of [3] could not be inspected, leaving a material residual originality risk. A related general descriptive-set-theoretic study of expansive measures [4] establishes an ambient \(G_{\delta\sigma}\) complexity result, but not the concentration iff or this product-parameter density distinction.

## Limitations
The result concerns independent coordinate-product laws and two-sided shift time; it does not characterize dependent measures, one-sided dynamical balls, flows with time reparametrization, or genericity in all \(\operatorname{Prob}(X)\). It does not claim that the entire expansive product-law subset is itself a \(G_\delta\); only that it contains a specified dense \(G_\delta\). Non-invariant measures are allowed, not required. The exact criterion may have equivalent formulations in earlier unindexed probability or symbolic-dynamics literature.

## References
[1] E. Pedrosa, E. Rego and A. Trilles, *On the Invariance of Expansive Measures for Flows*, arXiv:2506.21533v1 (first public 2025-06-26), https://arxiv.org/html/2506.21533v1.

[2] C. A. Morales, *Measure-expansive systems*, arXiv:2503.16757 (electronic posting 2025-03-21; older preprint noted in its metadata), https://arxiv.org/abs/2503.16757.

[3] G. Lacerda, *Typical expansive measures for infinite-dimensional maps*, arXiv:2610.09482v1 (first public 2026-10-07), https://arxiv.org/abs/2610.09482.

[4] K. Lee, C. A. Morales and B. Shin, *On the set of expansive measures*, Communications in Contemporary Mathematics **20** (2018), 1750086, DOI:10.1142/S0219199717500869.
