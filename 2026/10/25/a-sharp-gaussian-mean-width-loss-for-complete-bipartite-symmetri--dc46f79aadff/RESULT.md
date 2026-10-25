# A sharp Gaussian mean-width loss for complete-bipartite symmetric edge polytopes

## Finding

For every integer pair \(p,q\ge 2\), set \(n=p+q\) and \(d=n-1\), and partition \(\{1,\ldots,n\}=A\sqcup B\) into parts of sizes \(p,q\). Define the symmetric edge polytopes, with their **standard, unrescaled Euclidean root embeddings** in the sum-zero hyperplane \(H\), by
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in A,\ j\in B\},\qquad
P_n=\operatorname{conv}\{\pm(e_i-e_j):1\le i<j\le n\}.
\]
Let \(U\) be uniform on the Euclidean unit sphere of \(H\), and set \(W_{p,q}=w_{P_{p,q}}(U)\), \(W_n=w_{P_n}(U)\), where \(w_K(u)=h_K(u)+h_K(-u)\). Put
\[
b_n=\sqrt{2\log n}-\frac{\log\log n+\log(4\pi)}{2\sqrt{2\log n}},\qquad a_n=\frac1{\sqrt{2\log n}}.
\]

**Theorem (sharp mean-width loss and limiting angular law).** For all \(p,q\ge2\), the inequality \(W_{p,q}\le W_n\) holds pointwise and the exact strict-event probability is
\[
\mathbb P\{W_n>W_{p,q}\}=\frac{p(p-1)+q(q-1)}{n(n-1)}.
\]
Suppose, as \(n\to\infty\), that \(p/n\to\alpha\in(0,1)\), and write \(\beta=1-\alpha\). For four independent standard Gumbel variables \(G_1,G_2,G_3,G_4\) (each with CDF \(e^{-e^{-x}}\)), define
\[
\begin{aligned}
D_\alpha={}&\max\{\log\alpha+G_1,\log\beta+G_2\}
+\max\{\log\alpha+G_3,\log\beta+G_4\}\\
&-\log(\alpha\beta)-\max\{G_1+G_4,G_2+G_3\}.
\end{aligned}
\]
Then \(D_\alpha\ge0\) almost surely, with an atom at zero of mass \(2\alpha\beta\), and
\[
\boxed{\quad\frac{\sqrt d}{2a_n}(W_n-W_{p,q})\ \Longrightarrow\ D_\alpha.\quad}
\]
Moreover, **the means converge at the same sharp scale**:
\[
\boxed{\quad\lim_{n\to\infty}\frac{\sqrt d}{2a_n}\bigl(\mathbb EW_n-\mathbb EW_{p,q}\bigr)=-\log\bigl(\alpha(1-\alpha)\bigr)-1.\quad}
\]
The constant is strictly positive for every \(0<\alpha<1\), is minimized at the balanced ratio \(\alpha=1/2\) with value \(\log4-1\), and varies nontrivially with imbalance. Nevertheless, both families have the identical first-order mean-width asymptotic \(\mathbb EW_n\sim\mathbb EW_{p,q}\sim4\sqrt{2\log n}/\sqrt n\), as well as the same Euclidean circumradius \(\sqrt2\).

## Assumptions and scope

The limits concern a deterministic sequence of integers \(p,q\ge2\) with \(p+q=n\to\infty\) and strictly positive limiting part proportions. The root polytopes have intrinsic dimension \(d=n-1\); all directional widths and radii use the Euclidean metric induced from \(\mathbb R^n\), not lattice-normalized widths or volumes. The limiting random variable is defined by four *independent* standard Gumbels. The exact finite-size strict-event formula requires only that the Gaussian coordinate distribution be atomless and exchangeable; the asymptotic distribution and mean result are proved here for uniform spherical direction (equivalently, isotropic Gaussian direction after radial normalization).

## Proof

**1. Exact support functions.** Let \(g=(g_1,\ldots,g_n)\) be a vector with distinct entries and set \(A_+=\max_{i\in A}g_i\), \(A_-=-\min_{i\in A}g_i\), with analogous definitions for \(B_+,B_-\). Direct maximization over the root vertices gives
\[
h_{P_n}(g)=\max\{A_+,B_+\}+\max\{A_-,B_-\},
\qquad
h_{P_{p,q}}(g)=\max\{A_++B_-,B_++A_-\}.
\]
Because both polytopes are centrally symmetric, their widths are twice these support values. In particular \(h_{P_{p,q}}(g)\le h_{P_n}(g)\). Equality holds precisely when the index of the global maximum and that of the global minimum belong to **different** parts. This is clear because a root attaining the full range is an admissible cross-part root exactly then; with distinct entries its maximizing ordered pair is unique.

**2. Exact angular probability.** If the entries of \(g\) are independent standard normals, every ordered pair of distinct indices is equally likely to be the indices of the maximum and minimum. The probability that they lie in the same part is therefore \([p(p-1)+q(q-1)]/[n(n-1)]\). Let \(g_H\) denote the orthogonal projection onto \(H\). Every root has coordinate sum zero, so the support functions are unchanged by replacing \(g\) by \(g_H\). The Gaussian direction \(g_H/\|g_H\|_2\) is uniform on the unit sphere of \(H\), preserving strict inequalities. This proves the finite-dimensional assertion.

**3. Joint Gaussian extremes.** For independent standard Gaussian coordinates, classical Poisson convergence of upper and lower extremes yields joint convergence of the four group extremes after centering by \(b_n\) and scaling by \(a_n\). In the order \(A_+, B_+, A_-, B_-\), the limit is
\[
\bigl(\log\alpha+G_1,\ \log\beta+G_2,\ \log\alpha+G_3,\ \log\beta+G_4\bigr).
\]
For completeness, for a group of \(m\) indices with \(m/n\to c>0\), the upper-max CDF at \(b_n+a_nx\) is \(\Phi(b_n+a_nx)^m\to\exp(-c e^{-x})\), because \(n\overline\Phi(b_n+a_nx)\to e^{-x}\). For its maximum and negative minimum the joint CDF is
\[
\bigl(1-\overline\Phi(b_n+a_nx)-\overline\Phi(b_n+a_ny)\bigr)^m
\longrightarrow\exp(-c e^{-x}-c e^{-y}),
\]
so upper and lower limits are independent. The two disjoint groups are independent already at finite \(n\).

Subtract the two support-function identities from step 1. Their common leading \(2b_n\) cancels; the continuous-mapping theorem gives convergence, after division by \(a_n\), to the displayed \(D_\alpha\). Let \(R=\|g_H\|_2\), so \(R^2\) has chi-square law with \(d\) degrees of freedom and \(R/\sqrt d\to1\) in probability. The identity \(g_H=RU\) and homogeneity of widths imply
\[
\frac{\sqrt d}{2a_n}\bigl(W_n-W_{p,q}\bigr)
=\frac{\sqrt d}{R}\cdot\frac{h_{P_n}(g)-h_{P_{p,q}}(g)}{a_n}.
\]
Slutsky's theorem proves the asserted distributional limit. Since \(D_\alpha=0\) exactly if the two global extremizers occur in opposite parts, the zero atom has mass \(2\alpha\beta\).

**4. Convergence of expectations.** Standard Gaussian Mills bounds applied to the two classwise maxima and minima show bounded fixed moments of their centered, \(a_n\)-scaled extrema when \(p/n,q/n\) remain bounded away from zero. One explicit sufficient argument uses, for \(x\ge0\), the upper-tail union bound \(\Pr((M_m-b_n)/a_n>x)\le m\overline\Phi(b_n+a_nx)\), bounded for large \(n\) by a constant times \(e^{-x/2}\), and the lower-tail bound \(\Pr((M_m-b_n)/a_n<-x)\le\exp[-m\overline\Phi(b_n-a_nx)]\). For \(0\le x\le b_n/(2a_n)\), Gaussian tail ratios give \(m\overline\Phi(b_n-a_nx)\ge c_1 e^{c_2x}\) with constants independent of large \(n\), yielding an integrable doubly-exponential bound. For \(b_n/(2a_n)\le x\le b_n/a_n\), the probability is at most \(\exp(-c_3n^{1/2})\); for \(x>b_n/a_n\), writing \(t=b_n-a_nx<0\), one has \(\Phi(t)^m\le2^{-(m-1)}\Phi(t)\), whose weighted tail integrals are exponentially small. Thus the centered extremes have uniformly bounded fixed moments, and the same estimates apply to negated minima. Thus the normalized Gaussian support gap, bounded by sums of four centered extrema, is uniformly integrable and its expectation converges to \(\mathbb ED_\alpha\).

For the spherical means no further uniform-integrability claim about reciprocal radial fluctuations is needed: independence of \(R\) and \(U\) implies the **exact identity** \(\mathbb E[h_{P_n}(g)-h_{P_{p,q}}(g)]=\mathbb ER\,\mathbb E[h_{P_n}(U)-h_{P_{p,q}}(U)]\), while \(\mathbb ER/\sqrt d\to1\). Therefore the scaled expected width gap tends to \(\mathbb ED_\alpha\).

**5. Evaluate the mean constant exactly.** The Gumbel max-stability identity yields
\[
\mathbb E\max\{\log\alpha+G_1,\log\beta+G_2\}
=\gamma_{\mathrm E}+\log(\alpha+\beta)=\gamma_{\mathrm E},
\]
with the same equality for \(G_3,G_4\). The two sums \(S_1=G_1+G_4\) and \(S_2=G_2+G_3\) are independent and identically distributed, each with mean \(2\gamma_{\mathrm E}\). Thus
\[
\mathbb E\max(S_1,S_2)=2\gamma_{\mathrm E}+\tfrac12\mathbb E|S_1-S_2|.
\]
A difference of independent standard Gumbels has the standard logistic law: if \(G=-\log E\) with \(E\sim\operatorname{Exp}(1)\), then \(G_1-G_2=\log(E_2/E_1)\) has CDF \(1/(1+e^{-x})\) by direct exponential integration. Consequently \(S_1-S_2\) is a sum of two independent standard logistic variables. Writing each logistic variable as \(\log(V/(1-V))\) for a uniform \(V\) on \((0,1)\), its positive-part expectation is
\[
\begin{aligned}
\tfrac12\mathbb E|S_1-S_2|&=
\int_{u+v>1}\log\frac{uv}{(1-u)(1-v)}\,du\,dv\\
&=2\int_0^1 u\log\frac{u}{1-u}\,du=1.
\end{aligned}
\]
Therefore \(\mathbb E\max(S_1,S_2)=2\gamma_{\mathrm E}+1\), and subtraction in the definition of \(D_\alpha\) yields \(\mathbb ED_\alpha=-\log(\alpha\beta)-1\).

**6. The coinciding first order and circumradius.** The Gaussian full-root support has expectation \(2b_n+O(a_n)\). The Gaussian bipartite support differs by only \(O(a_n)\) in mean, by step 4. Since \(\mathbb ER\sim\sqrt d\) and width is twice support, both mean widths equal \(4b_n/\sqrt d\,(1+o(1))\). Finally every defining vertex has norm \(\sqrt2\). Central symmetry means any ball of radius smaller than \(\sqrt2\) cannot contain both antipodes of such a vertex, while the radius-\(\sqrt2\) ball at zero contains all vertices; hence each circumradius equals \(\sqrt2\).

## Verification

Run `python verify.py` using Python 3 and NumPy. It independently checks 750 numerical support-gap identities by direct vertex enumeration, exhaustively checks the strict-event combinatorics for five small bipartitions, evaluates the logistic integral by midpoint quadrature, and tests the four-Gumbel limit's mean and zero atom at four positive part ratios. The actual reproduced output was `VERIFY_OK vertex_support=750 exhaustive_rank=5 gaussian_limit_cases=4 logistic_quadrature=100000`. None of these finite numerical checks by itself proves the asymptotic limit: the proof above is the analytic evidence.

## Relationship to prior work

Higashitani, Jochemko, and Michałek define the symmetric edge polytope and give complete-bipartite facet, triangulation, and Ehrhart results. D'Alì, Delucchi, and Michałek investigate its geometry, relations to other graph polytopes, and metric duality. Kabluchko, Litvak, and Zaporozhets connect Euclidean mean widths of regular polytopes to Gaussian maxima. Classical Gaussian extreme-value theory supplies the upper/lower Gumbel convergence. This finding is the **sharp second-order difference between two deterministic graph-root polytopes**, including the distribution with a nontrivial zero atom, the exact angular probability, and the evaluated imbalance-dependent mean coefficient. It is not a new proof of the underlying Gumbel theorem or a general theorem for all graphs.

## Limitations

The sharp distribution and mean constant have only been proved for two parts of positive limiting proportions; no uniform-in-imbalance limit or sparse-part crossover is claimed. An alternative expression in older Gaussian order-statistics or graph-polytope literature may encode part or all of this result, and no bibliographic search can establish absolute novelty. Independent validation has not been performed. Finite numerical simulations should not be substituted for the analytic Gaussian extreme-value and moment arguments.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 2018-07-20, https://arxiv.org/html/1807.07678v1.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, https://arxiv.org/html/1910.05193v1.
3. Z. Kabluchko, A. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, https://arxiv.org/abs/1511.08479.
4. T. Kálmán, L. Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127, https://arxiv.org/abs/2203.17127.
