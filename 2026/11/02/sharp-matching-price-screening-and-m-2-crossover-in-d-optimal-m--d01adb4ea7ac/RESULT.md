# Sharp matching-price screening and \(m^{-2}\) crossover in D-optimal Möbius ladders

## Finding

For each integer \(m\ge4\), form the graph on \(\mathbb Z/(2m)\) from the cycle edges \(\{i,i+1\}\) and the \(m\) antipodal matching edges \(\{i,i+m\}\), with indices taken modulo \(2m\). Assign every cycle edge a price of one and every matching edge a price \(q>0\) per unit conductance. Under the budget \(B>0\), choose *each individual nonnegative edge conductance independently* to maximize the weighted spanning-tree enumerator
\[
\mathcal T(w)=\sum_{T\text{ a spanning tree}}\prod_{e\in T}w_e,
\qquad \sum_{e\text{ cycle}}w_e+q\sum_{e\text{ matching}}w_e\le B.
\]
The maximum and its conductance vector are unique. All cycle edges receive a common positive conductance \(a_*\), and all matching edges receive a common conductance \(b_*\ge0\). Define the sharp price threshold
\[
q_c(m)=\frac{m^2}{2m-1}.
\]
If \(q\ge q_c(m)\), then \(b_*=0\) and \(a_*=B/(2m)\). If \(0<q<q_c(m)\), then \(b_*>0\), and the ratio \(t_*=b_*/a_*\) is the **unique** positive solution of
\[
\frac{m\tanh\!\left(\frac m2\operatorname{arcosh}(1+t)\right)}{\sqrt{t(t+2)}}
=\frac{(2m-1)q}{2+qt}.
\]
In both cases,
\[
a_* = \frac{B}{m(2+qt_*)},\qquad b_*=t_*a_*,\qquad
\mathcal T_*=m a_*^{\,2m-1}[T_m(1+t_*)+1],
\]
where \(T_m\) is the usual Chebyshev polynomial of the first kind and \(t_*=0\) in the deletion regime.

There are two distinct large-network limits. If \(q>0\) is fixed, then
\[
\lim_{m\to\infty}t_*(m,q)
=\frac{2}{3q}\left(1-2q+\sqrt{(2q-1)^2+3}\right)>0.
\]
If instead \(q_m/m\to\alpha\in(0,1/2)\), then
\[
\lim_{m\to\infty}m^2t_*(m,q_m)=\frac{s_\alpha^2}{2},
\qquad \frac{\tanh(s_\alpha/2)}{s_\alpha}=\alpha,
\]
where \(s_\alpha>0\) is unique. If \(q_m/m\to\alpha\ge1/2\), then \(m^2t_*(m,q_m)\to0\); for \(\alpha>1/2\), all matching conductances vanish for sufficiently large \(m\).

## Assumptions and scope

The graph has \(2m\ge8\) labeled vertices, a simple cycle of \(2m\) edges, and a disjoint set of \(m\) antipodal edges. The first two small cases, \(m=2\) and \(m=3\), reduce to a distinguished-matching allocation on \(K_4\) and \(K_{3,3}\), respectively, and are intentionally excluded from the new theorem. Every edge weight is independently chosen from \([0,\infty)\); connectivity is required, as otherwise \(\mathcal T=0\). Prices are equal *within* the two indicated edge classes but need not be equal across them. No hypothesis that the optimizer is symmetric is imposed. The threshold and optimizer are valid for every real \(B,q>0\), including equality at the threshold.

## Proof

**Strict global optimality and symmetry.** Kirchhoff's weighted matrix-tree theorem writes \(\mathcal T(w)=\det \widehat L(w)\), where \(\widehat L\) is any reduced weighted graph Laplacian. The feasible budget polytope is compact; a positive-weight connected graph is feasible, so an optimum has \(\mathcal T>0\), hence a positive-definite reduced Laplacian. The objective is homogeneous of degree \(2m-1\), so the budget is saturated. The map \(w\mapsto\widehat L(w)\) is injective: off-diagonal entries identify every edge not incident to the grounded vertex, and the remaining diagonal entries then identify its incident edges. For a nonzero perturbation \(H\),
\[
\frac{d^2}{du^2}\log\det(\widehat L+uH)\bigg|_{u=0}
=-\operatorname{tr}(\widehat L^{-1}H\widehat L^{-1}H)<0.
\]
Thus \(\log\mathcal T\) is strictly concave on the connected feasible region and its maximizer is unique. Vertex rotation permutes the cycle edges transitively and the matching edges transitively, preserving prices and the budget; uniqueness forces constant conductances \(a\) and \(b\) on those classes. The cycle conductance must be positive, since setting all cycle conductances to zero disconnects the graph.

**Exact tree product.** Fourier vectors indexed by \(k=0,\ldots,2m-1\) diagonalize the two-class Laplacian, with eigenvalues
\[
\lambda_k=2a\left(1-\cos\frac{\pi k}{m}\right)
+b\bigl(1-(-1)^k\bigr).
\]
The product of nonzero even-indexed eigenvalues equals \(m^2 a^{m-1}\), from \(\prod_{j=1}^{m-1}4\sin^2(\pi j/m)=m^2\). For \(t=b/a\), the odd-indexed product is
\[
(2a)^m\prod_{j=0}^{m-1}\left(1+t-\cos\frac{(2j+1)\pi}{m}\right)
=2a^m[T_m(1+t)+1],
\]
using the exact polynomial identity \(\prod_j(x-\cos((2j+1)\pi/m))=2^{1-m}(T_m(x)+1)\), including multiplicities. Dividing the full nonzero product by \(2m\) proves
\[
\mathcal T(a,b)=m a^{2m-1}[T_m(1+b/a)+1].
\]

**Sharp support transition.** The saturated budget gives \(a=B/[m(2+qt)]\) with \(t\ge0\). The logarithmic objective, up to a constant independent of \(t\), is
\[
F_m(t)=\log[T_m(1+t)+1]-(2m-1)\log(2+qt).
\]
Writing \(u=\operatorname{arcosh}(1+t)\), the Chebyshev identity \(T_m(1+t)=\cosh(mu)\) yields for \(t>0\)
\[
F_m'(t)=\frac{m\tanh(mu/2)}{\sinh u}-\frac{(2m-1)q}{2+qt},
\qquad
F_m'(0)=\frac{m^2-(2m-1)q}{2}.
\]
As \(t\to\infty\), the cycle conductance tends to zero and the graph tends to \(m\) disjoint edges; consequently \(\mathcal T\to0\). Strict concavity in the affine budget coordinate \(b\) and the strict monotonicity of \(b=Bt/[m(2+qt)]\) in \(t\) imply that the derivative changes sign at most once from positive to negative. Thus \(F_m'(0)\le0\) forces the unique boundary maximum \(t=0\); otherwise there is exactly one positive critical point, necessarily the unique optimum. This proves the threshold, the scalar equation, and uniqueness even among asymmetric allocations.

**Fixed-price limit.** Fix \(q>0\). The threshold tends to infinity, so the optimizer is eventually interior. The stationarity identity and \(\tanh(mu/2)\le1\), \(\sinh u\ge t\) imply \(t_*\le 2m/[(m-1)q]\le4/q\). The positive roots cannot tend to zero: if \(t_*\to0\), then \(u\to0\) and \(\tanh(mu/2)/\sinh u\to\infty\), whereas the stationarity equation divided by \(m\) has a bounded right-hand side. On any convergent subsequence with positive limit, \(\tanh(mu/2)\to1\), so the limit solves
\[
\frac1{\sqrt{t(t+2)}}=\frac{2q}{2+qt}
\quad\Longleftrightarrow\quad
3q^2t^2+(8q^2-4q)t-4=0.
\]
The quadratic has exactly one positive root, the stated expression. Boundedness and subsequence uniqueness establish convergence.

**Critical scaling.** Let \(q_m/m\to\alpha>0\), and evaluate the derivative at \(t=s^2/(2m^2)\), for fixed \(s>0\). Since \(m\operatorname{arcosh}(1+t)\to s\),
\[
\frac{F_m'(s^2/(2m^2))}{m^2}\longrightarrow
\frac{\tanh(s/2)}s-\alpha.
\]
The function \(s\mapsto\tanh(s/2)/s\) decreases strictly from \(1/2\) to \(0\). For \(0<\alpha<1/2\), choosing \(s\) on either side of its unique level-set root gives respectively positive and negative derivative signs. Since the derivative changes from positive to negative only once, these brackets squeeze \(m^2t_*\) to \(s_\alpha^2/2\). For \(\alpha\ge1/2\), the derivative at every fixed \(s>0\) is eventually negative, so \(m^2t_*\le s^2/2\) eventually; letting \(s\downarrow0\) gives the zero limit. If \(\alpha>1/2\), eventually \(q_m>q_c(m)\), hence \(t_*=0\) identically.

## Verification

Run `python3 verify.py` with Python's standard library. The executable performs exact integer matrix-tree determinant comparisons for small graph sizes, checks the scalar stationarity relation in the interior, compares the proposed optimizer with independently chosen asymmetric feasible conductances, and tests numerical convergence in both asymptotic regimes. In the recorded run, **815 assertions passed**. These finite checks are corroboration; the proof of the assertions over all integers \(m\ge4\) and all positive prices and budgets is analytic above.

## Relationship to prior work

Jakobson and Rivin (1999, 2000) established general variational conditions for weighted graph complexity and explicitly noted that the eight-vertex Möbius ladder is not equiarboreal. Their conditions explain why nonuniform edge classes can matter, but do not provide the all-size, arbitrary-price two-class optimum or the singular price-dependent scaling limit. The cases \(m=2\) and \(m=3\) fall under previously treated complete and complete-bipartite priced-design models, so our claim concerns \(m\ge4\). The unweighted tree-count sequence of Möbius ladders is known; the identity \(\mathcal T(1,1)=m[T_m(2)+1]\) is not claimed to be new. Tzeng and Wu (2000) compute spanning-tree generating functions on hypercubic lattices and Möbius-strip quadrangular nets, a different network family and not a conductance-budget design problem. Khosoussi and collaborators (2016) investigate maximizing weighted spanning trees through constrained edge selection and broad approximation methods; their principal edge-selection formulation does not supply this exact continuous-conductance price theorem. Related results on weighted finite open ladders concern determinantal edge kernels and do not, on the available summary, imply the Möbius-ladder price transition. Generic matrix-tree, Fourier, Chebyshev, concavity, and KKT ingredients are prior mathematical tools; the claimed contribution is their exact synthesis into this priced Möbius-ladder classification and its two scaling laws.

## Limitations

Prices are uniform within each of two rotational edge orbits; arbitrary individual price heterogeneity is not classified. This is a weighted tree-enumerator or D-optimal allocation result, not a theorem about unweighted spanning-tree count, finite-time failure probability, or mixing speed. The strict concavity proof ensures uniqueness within the model but does not establish that no other publication contains an equivalent formulation. 

## References

1. D. Jakobson and I. Rivin, *On Some Extremal Problems in Graph Theory*, first posted 1999-07-08, arXiv:math/9907050, https://arxiv.org/abs/math/9907050.
2. D. Jakobson and I. Rivin, *Extremal Metrics on Graphs I*, first posted 2000-01-28, arXiv:math/0001169, https://arxiv.org/abs/math/0001169.
3. W.-J. Tzeng and F. Y. Wu, *Spanning Trees on Hypercubic Lattices and Non-orientable Surfaces*, first posted 2000-01-27, arXiv:cond-mat/0001408, https://arxiv.org/abs/cond-mat/0001408.
4. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, first posted 2016-04-05, arXiv:1604.01116, https://arxiv.org/abs/1604.01116.
5. OEIS A020871, *Number of spanning trees in a Moebius ladder*, https://oeis.org/A020871 (known unweighted counts).
