# Quantitative stability for path-maximal graph-indexed random-walk ranges

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

For a connected bipartite simple graph \(G\), let \(\widehat h(G)\) be the expected range of a uniformly chosen integer height function with edge increments exactly \(\pm1\). For a connected simple graph \(G\), let \(h(G)\) be the analogous expected range for a uniformly chosen integer 1-Lipschitz height function with edge increments in \(\{-1,0,1\}\). Pinning one vertex at zero only fixes the additive constant and does not affect the range.

Yinfeng Zhu (2026) proved the extremal inequalities
\[
\widehat h(G)\le \widehat h(P_n),\qquad h(G)\le h(P_n),
\]
for graphs of order \(n\), with the first statement for bipartite \(G\). The following quantitative refinements hold.

### Theorem 1: standard model

If \(G\) is a connected bipartite simple graph on \(n\) vertices and \(G\not\cong P_n\), then
\[
\boxed{\widehat h(P_n)-\widehat h(G)\ge \frac{1}{60\sqrt n}.}
\]
In particular the path is the unique maximizer.

The order \(n^{-1/2}\) is best possible. Let \(T_n\) be the tree obtained from a path \(x_0,\ldots,x_{n-3}\) by attaching two new leaves to \(x_{n-3}\). If \(M_L\) denotes the maximum of a length-\(L\) simple symmetric random walk, then
\[
\boxed{
\widehat h(P_n)-\widehat h(T_n)
 =\frac12\Pr(M_{n-3}=1)
 \sim \frac{1}{\sqrt{2\pi n}}.
}
\]
More explicitly, with \(L=n-3\),
\[
\Pr(M_L=1)=
\begin{cases}
2^{-L}\binom{L}{(L+1)/2},&L\text{ odd},\\[3pt]
2^{-L}\binom{L}{(L+2)/2},&L\text{ even}.
\end{cases}
\]

### Theorem 2: lazy model

If \(G\) is a connected simple graph on \(n\) vertices and \(G\not\cong P_n\), then
\[
\boxed{h(P_n)-h(G)\ge \frac{1}{2000\,n^{3/2}}.}
\]
For nonpath trees the stronger estimate
\[
\boxed{h(P_n)-h(T)\ge \frac{2}{405\sqrt n}}
\]
holds. Thus the path is also the unique maximizer in the lazy model.

The universal lazy constant is not claimed sharp; the point is a dimension-explicit separation valid for every connected nonpath graph.

## Proof of Theorem 1

Write \(b_m=\widehat h(P_{m+1})\). Zhu introduces, for \(d\ge2\),
\[
J_d=\frac4\pi\int_0^1\frac{s^d}{(1+s)^{3/2}\sqrt{1-s}}\,ds
\]
and a parity error \(\varepsilon_{d,p}\). Proposition 3.3 of that paper says that if \(q\) is the zero-edge rank of an auxiliary graph, \(X=d-q\), and
\[
\Delta=\mathbb E q-(1-p)d,
\]
then
\[
\mathbb E b_X-\mathbb E b_{Y_{d,p}}
\le \varepsilon_{d,p}-\Delta J_d-\mathbb E a_X,
\tag{1}
\]
where \(Y_{d,p}\sim\operatorname{Bin}(d,p)\) and \(a_X\ge0\). For the standard model \(p=1/2\), and Zhu proves
\[
\varepsilon_{d,1/2}<\frac{J_d}{2d}.
\tag{2}
\]
We retain more of the rank surplus than is needed for the qualitative extremal theorem.

An elementary lower bound useful below is
\[
\boxed{J_d\ge \frac{1}{\pi\sqrt2\sqrt{d+1}}.}
\tag{3}
\]
Indeed, restrict the integral to \([d/(d+1),1]\). There \(s^d\ge1/4\) and \((1+s)^{3/2}\le2\sqrt2\), while
\[
\int_{d/(d+1)}^1(1-s)^{-1/2}\,ds=\frac2{\sqrt{d+1}}.
\]

### A branching vertex

If a connected graph is not a path and has a vertex of degree at least three, three neighbours of that vertex form a triangle in the auxiliary graph on the opposite bipartition class. Zhu's odd-cycle rank estimate, specialized to a triangle, gives
\[
\Delta\ge\frac14.
\]
Let that auxiliary class have size \(d+1\), so \(d\ge2\). From (1)-(2), for \(d\ge3\) its loss relative to the binomial path comparator is strictly larger than
\[
J_d\left(\frac14-\frac1{2d}\right)\ge\frac{J_d}{12}.
\]
At \(d=2\), Zhu's exact values give
\[
\frac{J_2}{4}-\varepsilon_{2,1/2}=\frac18.
\]
The induction in Zhu's proof adds the two auxiliary-class contributions and then balances their sizes. Hence a loss in either class passes unchanged to the final comparison with \(P_n\). By (3),
\[
\widehat h(P_n)-\widehat h(G)
\ge \frac{1}{12\pi\sqrt2\sqrt n}
>\frac{1}{60\sqrt n}.
\tag{4}
\]

### Even cycles

It remains to consider a connected graph of maximum degree at most two that is not a path. In the bipartite setting this is \(C_{2m}\).

For \(m\ge3\), each auxiliary graph is \(C_m\), every auxiliary edge has weight \(2\), and \(d=m-1\). Its increment law is that of iid variables
\[
\Pr(X_i=0)=\frac12,\qquad \Pr(X_i=\pm1)=\frac14,
\]
conditioned on \(\sum_iX_i=0\). Let \(Z\) count zero increments. The zero-edge rank is \(q=Z\) except on the all-zero configuration, where \(q=m-1\). Since \(X_i=(\epsilon_i+\eta_i)/2\) for independent Rademacher variables,
\[
\Pr\!\left(\sum_iX_i=0\right)=4^{-m}\binom{2m}{m}.
\]
A one-coordinate conditioning gives
\[
\mathbb E\!\left[Z\mid\sum_iX_i=0\right]=\frac{m^2}{2m-1},
\qquad
\Pr(Z=m\mid\sum_iX_i=0)=\frac{2^m}{\binom{2m}{m}}.
\]
Therefore the exact rank surplus is
\[
\boxed{
\Delta_m=\frac{3m-1}{2(2m-1)}-\frac{2^m}{\binom{2m}{m}}.
}
\tag{5}
\]
It equals \(2/5\) at \(m=3\). For \(m\ge4\), the second term decreases and is at most \(8/35\), while the first term exceeds \(3/4\); hence \(\Delta_m>73/140>2/5\). Thus always \(\Delta_m\ge2/5\).

Using (1)-(2), each auxiliary class loses at least
\[
J_d\left(\frac25-\frac1{2d}\right)\ge\frac{3J_d}{20}.
\]
There are two equal classes, so the global gap is at least \(3J_d/10\). Since \(n=2m=2(d+1)\), (3) gives
\[
\widehat h(P_n)-\widehat h(C_n)
>\frac{3}{10\pi\sqrt n}
>\frac1{60\sqrt n}.
\]
For \(C_4\), each auxiliary graph is a single edge with zero weight \(4\): its nonzero indicator has parameter \(1/3\), rather than the path comparator's \(1/2\). The two classes therefore contribute a total loss \(2(1/2-1/3)=1/3\). This completes the proof.

## Sharpness of the standard order

For the fork \(T_n\), put \(L=n-3\). Couple \(P_n\) and \(T_n\) by using the same \(L\) spine increments and the same two final Rademacher variables \(\xi_1,\xi_2\). If the spine endpoint is \(S_L\), maximum \(M_L\), and minimum \(m_L\), a four-case check over \((\xi_1,\xi_2)\) gives the conditional expected difference
\[
\frac14\mathbf 1_{\{M_L-S_L=1\}}+
\frac14\mathbf 1_{\{S_L-m_L=1\}}.
\]
Time reversal and sign symmetry show that both indicators have expectation \(\Pr(M_L=1)\), proving the exact formula in Theorem 1.

The reflection identity
\[
\Pr(M_L\ge a)=\Pr(S_L\ge a)+\Pr(S_L\ge a+1)
\]
implies
\[
\Pr(M_L=1)=
\begin{cases}
\Pr(S_L=1),&L\text{ odd},\\
\Pr(S_L=2),&L\text{ even}.
\end{cases}
\]
Stirling's formula then yields \(\Pr(M_L=1)\sim\sqrt{2/(\pi L)}\), and hence the claimed \(1/\sqrt{2\pi n}\) gap. No uniform lower bound of larger order than \(n^{-1/2}\) is possible.

## Proof of Theorem 2

Let \(d=n-1\). Zhu's lazy comparison uses \(p=2/3\) in (1), proves for cyclic graphs
\[
\Delta_G\ge\frac{2}{7d},
\]
and obtains
\[
h(P_n)-\mathbb E b_{K-1}
\ge \frac{2J_d}{7d}-\varepsilon_{d,2/3}.
\tag{6}
\]
For \(d\ge4\), the explicit estimate in Lemma 5.4 gives
\[
\frac{d\varepsilon_{d,2/3}}{J_d}<\frac{37125}{131072}.
\]
Consequently, using (3),
\[
\frac{2J_d}{7d}-\varepsilon_{d,2/3}
>
\frac{2269}{917504}\frac{J_d}{d}
\ge
\frac{2269}{917504\pi\sqrt2}\frac1{d\sqrt{d+1}}
>
\frac1{2000n^{3/2}}.
\tag{7}
\]
For \(d=2,3\), the exact expressions in Zhu's proof are positive by margins much larger than the right side of (7). Since
\[
h(G)\le\mathbb E b_{K-1},
\]
this proves the stated bound for every cyclic graph.

Now let \(T\) be a nonpath tree. Choose a vertex of degree at least three and three incident edges. In the uniform lazy model on a tree, edge increments are iid uniform on \(\{-1,0,1\}\). Contract all zero edges, producing a random tree \(Q\) on \(K\) vertices. Zhu's contraction identity and tree equality in the contraction-count comparison give
\[
h(P_n)-h(T)=\mathbb E\bigl[b_{K-1}-\widehat h(Q)\bigr].
\tag{8}
\]
With probability \((2/3)^3=8/27\), the three chosen edges are all nonzero; because the original graph is a tree, they remain three distinct branches after zero-edge contraction. Hence \(Q\) is then a nonpath tree. Theorem 1 gives
\[
b_{K-1}-\widehat h(Q)\ge\frac1{60\sqrt K}\ge\frac1{60\sqrt n}.
\]
On the complementary event the integrand in (8) is nonnegative by the standard path theorem. Averaging proves
\[
h(P_n)-h(T)\ge\frac8{27}\frac1{60\sqrt n}=\frac2{405\sqrt n}.
\]
Combining the tree and cyclic cases gives Theorem 2.

## Interpretation

The qualitative path extremal theorem has a genuine stability scale. In the standard model, every nonpath bipartite graph is separated from the path by order at least \(n^{-1/2}\), and a one-fork perturbation of the path realizes exactly that order. Thus the exponent \(1/2\) is sharp.

For the lazy model, the same standard-model stability survives on nonpath trees through zero-edge contraction. Cyclic graphs are controlled by the weaker rank-surplus estimate currently available in the lazy comparison, producing a universal \(n^{-3/2}\) bound. No claim is made that the lazy cyclic exponent is optimal.

## Originality and relation to prior work

The expected-range extremal inequalities themselves are not new. Wu--Xu--Zhu (2016) proved the expectation conjectures for trees; Bok--Nešetřil (2018) treated unicyclic graphs; Berger--Ji--Metz (2019) proved the stronger lazy range-distribution domination for trees and partial standard results; Zhu (2026) proved the expected-range theorem for all connected bipartite graphs and derived the lazy theorem for all connected graphs. The quantities \(J_d\), \(\varepsilon_{d,p}\), the auxiliary-graph construction, the rank-surplus inequalities, and the contraction identities used above are all taken from Zhu (2026).

The contribution claimed here, to the best of our knowledge, is the quantitative stability extraction: a universal \(1/(60\sqrt n)\) standard gap with a matching \(n^{-1/2}\) fork family, together with explicit lazy gaps \(1/(2000n^{3/2})\) for arbitrary nonpaths and \(2/(405\sqrt n)\) for nonpath trees. The exact cycle rank-surplus formula (5) and the fork gap identity are included as proof ingredients, not as claims that earlier special-class literature contained no equivalent formulas.

A targeted search did not locate a prior theorem giving these dimension-explicit stability bounds or the sharp standard stability exponent. The principal residual originality risk is the 2016 tree paper, whose full text could not be inspected in this review; its abstract states the tree extremal theorem and it uses KC-transformations, so it is the most plausible source for an unstated or differently formulated quantitative tree refinement. The 2018/2019 special-class papers are also relevant to equality and strictness but the accessible statements do not give the bounds above.

## Limitations

- The standard theorem is conditional on the auxiliary comparison and rank-surplus lemmas of Zhu (2026); those prior lemmas are not reproved here.
- The constant \(1/60\) is convenient, not optimized. The fork family establishes only the optimal order \(n^{-1/2}\).
- The lazy universal \(n^{-3/2}\) exponent is not shown sharp; cyclic graphs may admit a stronger universal separation.
- The finding concerns expected range, not stochastic domination of the full range distribution. The stronger standard distributional problem remains outside this result.
- The full text of Wu--Xu--Zhu (2016) was not successfully inspected; this leaves a material residual originality risk for tree-specific quantitative statements.

## Reproducibility

`artifacts/verify_stability.py` is a standalone standard-library script. It exhaustively verifies the fork identity for small orders, checks the exact cycle auxiliary rank-surplus formula by direct weighted enumeration, and checks the numerical constant inequalities used above. `artifacts/verification_output.txt` records its output. These checks support the algebra; they do not replace the analytic proof.

## References

1. Y. Zhu, *Paths maximize the expected range of graph-indexed random walks*, arXiv:2609.19728 (2026). https://arxiv.org/abs/2609.19728
2. Y. Wu, Z. Xu, Y. Zhu, *Average Range of Lipschitz Functions on Trees*, Moscow Journal of Combinatorics and Number Theory 6 (2016), 96--116. https://zhuyinfeng.org/Data/Preprints/MJCNT16.pdf
3. A. Berger, C. Ji, E. Metz, *On the Distribution of Range for Tree-Indexed Random Walks*, European Journal of Combinatorics 81 (2019), 256--264. https://arxiv.org/abs/1808.04261
4. J. Bok, J. Nešetřil, *Graph-indexed random walks on pseudotrees*, Electronic Notes in Discrete Mathematics 68 (2018), 263--268. https://doi.org/10.1016/j.endm.2018.06.045
