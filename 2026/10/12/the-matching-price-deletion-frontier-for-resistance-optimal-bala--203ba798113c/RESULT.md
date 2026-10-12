# The matching-price deletion frontier for resistance-optimal balanced bicliques

## Finding
For each integer \(n\ge 3\), consider a balanced complete bipartite graph \(K_{n,n}\) with a distinguished perfect matching. A matching edge has unit-conductance price \(t>0\), every other edge has price one, and the total budget is one. Among **all individual nonnegative edge-conductance allocations** whose positive-weight support connects all vertices, the Kirchhoff index has a unique global minimizer.

Define
\[
T_n=\frac{n^2(4n^2-11n+8)}{(n-2)(4n^3-11n^2+10n-4)}.
\]
The distinguished matching is **completely deleted at the unique optimum if and only if** \(t\ge T_n\). In that regime the optimal conductances are zero on each matching edge and \(1/[n(n-1)]\) on every other edge; the minimum Kirchhoff index is
\[
K_n^*(t)=\frac{n(4n^3-11n^2+10n-4)}{n-2}.
\]
For \(0<t<T_n\), both edge classes are used. Their unique optimal conductances are
\[
a_n^*=\frac{x_n}{n(t x_n+n-1)},\qquad
b_n^*=\frac{1}{n(t x_n+n-1)},
\]
where \(x_n>0\) is the **unique positive solution** of
\[
\frac{(n-1)t}{n}
+\frac{n-1}{2}\frac{t(n-2)/2-(n-1)}{(x+(n-2)/2)^2}
+\frac{n-1}{2}\frac{t-1}{(x+n-1)^2}=0.
\]
The exact minimum in this regime is \(K_n^*(t)=2n^2(t x_n+n-1)H_n(x_n)\), with
\[
H_n(x)=\frac{n-1}{n}+\frac{n-1}{2x+n-2}+\frac{1}{2(x+n-1)}.
\]
Thus the formula is an explicit algebraic scalar characterization, rather than a claim of elementary radicals for its root.

The thresholds are strictly decreasing in \(n\), exceed one, and satisfy
\[
T_n=1+\frac2n+\frac{7}{2n^2}+O(n^{-3}).
\]
For each fixed \(t>1\), the matching is therefore deleted for all sufficiently large \(n\). At \(t=1\), all edges instead receive exactly \(1/n^2\) and \(K_n^*(1)=n^2(4n-3)\). For fixed \(0<t<1\),
\[
\frac{a_n^*}{n b_n^*}\longrightarrow
\frac12\left(\sqrt{\frac{2-t}{t}}-1\right),\qquad
\frac{K_n^*(t)}{n^3}\longrightarrow 2+2\sqrt{t(2-t)}.
\]
For fixed \(t\ge 1\), the latter normalized limit is \(4\). More sharply, if the price itself approaches one via \(t_n=1+s/n\) for any fixed \(s\in\mathbb R\) and sufficiently large \(n\) so \(t_n>0\), then
\[
\frac{a_n^*}{b_n^*}\longrightarrow \left(1-\frac{s}{2}\right)_+.
\]
The finite-network deletion boundary is therefore resolved even inside its order-\(1/n\) critical window.

## Assumptions and scope
The graph is undirected. Its two vertex classes have size \(n\); the distinguished matching connects corresponding indices. An edge conductance is nonnegative and contributes its price times its conductance to the budget. At the optimum the budget constraint is an equality. A disconnected positive-weight graph is assigned infinite Kirchhoff index. The Kirchhoff index \(K(L)=\sum_{u<v}R_{uv}\) is the sum of effective resistances of all unordered vertex pairs; for a connected graph with \(N=2n\) vertices, \(K(L)=N\sum_{j=2}^N\lambda_j(L)^{-1}\). The claims apply to every positive real price \(t\) and every integer \(n\ge3\), including exact equality at \(t=T_n\). The case \(n=2\) is excluded because removing its perfect matching disconnects the graph.

## Proof
**Global uniqueness and orbit reduction.** Put \(N=2n\), \(J=\mathbf1\mathbf1^\top\), and \(M=L+J/N\). On a connected weighted graph, \(M\) is positive definite and \(K(L)=N(\operatorname{tr}M^{-1}-1)\). For a nonzero symmetric perturbation \(H\), the second directional derivative of \(\operatorname{tr}M^{-1}\) equals \(2\operatorname{tr}(M^{-1}HM^{-1}HM^{-1})>0\). The positivity follows by putting \(B=M^{-1/2}HM^{-1/2}\): the trace becomes \(\operatorname{tr}(M^{-1/2}B^2M^{-1/2})>0\) when \(H\ne0\). Since the off-diagonal entries of a graph Laplacian recover all individual edge conductances, distinct feasible allocations give distinct Laplacians; strict convexity holds throughout the connected domain. Positive scaling of every conductance lowers \(K\), so the budget is exhausted. Compactness of the budget simplex and divergence at a disconnected limit give existence. Thus the global minimizer is unique.

Simultaneous permutations of matching pairs and interchange of the two bipartition classes preserve the graph, prices, budget, and objective. Uniqueness makes the optimizer invariant under these symmetries. All matching edges therefore share one conductance \(a\ge0\), and all other edges share another \(b>0\). This is a consequence of global optimality, not an assumption restricting the search.

**Exact spectrum and objective.** The weighted Laplacian has block form
\[
L=\begin{pmatrix}dI&-B\\-B&dI\end{pmatrix},\quad
B=(a-b)I+bJ_n,\quad d=a+(n-1)b.
\]
Its nonzero spectrum comprises \(2d\) once, \(nb\) with multiplicity \(n-1\), and \(2a+(n-2)b\) with multiplicity \(n-1\). Indeed, the constant symmetric vector has eigenvalue zero, the constant antisymmetric vector eigenvalue \(2d\), and the symmetric/antisymmetric zero-sum vectors give the remaining eigenvalues. It follows that
\[
K(a,b)=2n\left[\frac{n-1}{nb}+\frac{n-1}{2a+(n-2)b}+\frac1{2(a+(n-1)b)}\right].
\]
The budget \(nta+n(n-1)b=1\) and ratio \(x=a/b\ge0\) give \(b=1/[n(tx+n-1)]\), and hence \(K(x)=2n^2 F_{n,t}(x)\), where \(F_{n,t}(x)=(tx+n-1)H_n(x)\) and \(H_n\) is as above. The limiting possibility \(b=0\) disconnects the graph, and \(F_{n,t}(x)\to\infty\) as \(x\to\infty\) whenever \(t>0\).

**Price boundary.** Differentiating yields
\[
F'_{n,t}(x)=\frac{(n-1)t}{n}
+\frac{n-1}{2}\frac{t(n-2)/2-(n-1)}{(x+(n-2)/2)^2}
+\frac{n-1}{2}\frac{t-1}{(x+n-1)^2}.
\]
In particular \(F'_{n,t}(0)=tH_n(0)+(n-1)H_n'(0)\). Direct substitution gives
\[
H_n(0)=\frac{4n^3-11n^2+10n-4}{2n(n-2)(n-1)},\quad
H'_n(0)=-\frac{n(4n^2-11n+8)}{2(n-2)^2(n-1)^2}.
\]
Thus \(F'_{n,t}(0)\ge0\) exactly when \(t\ge T_n\). The feasible conductance \(a=x/[n(tx+n-1)]\) is strictly increasing in \(x\). Strict convexity along the budget line therefore makes the sign of the derivative at the left endpoint necessary and sufficient for a unique boundary minimum. If it is negative, there is exactly one interior minimum, the unique positive root displayed above. The boundary minimum and its objective follow by setting \(x=0\). Equality at \(t=T_n\) still gives the unique boundary allocation.

**Size dependence.** Algebraic simplification gives
\[
T_n-1=\frac{8(n-1)^3}{(n-2)(4n^3-11n^2+10n-4)}>0
\]
and
\[
\frac{dT_n}{dn}=-\frac{8n(n-1)^2(4n^3-16n^2+25n-16)}{(n-2)^2(4n^3-11n^2+10n-4)^2}<0\quad(n\ge3).
\]
The cubic in the numerator is positive at three and has positive derivative on that half-line. Expanding the rational function yields the asserted \(T_n\) asymptotic. When \(t=1\), every graph edge has the same price; edge transitivity and uniqueness force \(a=b=1/n^2\).

**Large-order and critical-window laws.** For fixed \(0<t<1\), set \(x=ny\). The normalized scalar objective satisfies, uniformly for \(y\) in compact subsets of \([0,\infty)\),
\[
\frac{F_{n,t}(ny)}{n}\longrightarrow
G_t(y)=\frac{2(1+ty)(1+y)}{1+2y}.
\]
For fixed \(t>0\), this limit grows without bound as \(y\to\infty\); the same lower bound \(F_{n,t}(x)\ge (n-1)(tx+n-1)/n\) keeps minimizing ratios \(x/n\) bounded. The derivative of \(G_t\) has the sign of \((t-1)+2ty+2ty^2\). For \(t<1\), its unique minimizer is \(y_t=(\sqrt{(2-t)/t}-1)/2\), proving the conductance ratio limit. Since \(G_t(y_t)=1+\sqrt{t(2-t)}\), the normalized Kirchhoff limit is \(2G_t(y_t)\). For fixed \(t>1\), we have \(T_n\to1<t\), so \(a_n^*=0\) eventually and the limit is four; for \(t=1\) the exact equal-allocation formula gives the same limit.

Finally fix \(s\in\mathbb R\) and set \(t_n=1+s/n\). The displayed exact derivative yields, uniformly for bounded nonnegative \(x\),
\[
F'_{n,t_n}(x)=\frac{2s+4x-4}{n}+O(n^{-2}).
\]
For \(s<2\), the derivative is negative at zero for large \(n\), and positive at a fixed sufficiently large \(x\); strict convexity along the budget line places the unique root in a bounded interval and forces \(x_n\to1-s/2\). For \(s>2\), \(t_n>T_n\) eventually and \(x_n=0\). At \(s=2\), the same bounded-interval derivative signs and \(T_n>1+2/n\) imply \(x_n\to0\). This proves the critical-window formula.

## Verification
Run `python3 checker.py` with Python 3.9 or later; the file uses only the standard library. It constructs exact rational weighted Laplacians, evaluates \(2n\operatorname{tr}L^\dagger\) via \(L+J/(2n)\), and compares independent rational matrix inverses to the stated spectrum and budget formulas. It tests endpoint optimality, nonsymmetric individual-edge allocations, and sample critical-window behavior. A successful run prints a `VERIFY_OK` line, followed by a reminder that finite tests do not prove the infinite-order claims. All conclusions above have analytical arguments independent of this checker.

As elementary calibration, for \(n=3\) the exact deletion threshold is \(T_3=99/35\). At \(t=3\), the optimizer removes the distinguished matching and assigns conductance \(1/6\) to the six remaining edges, producing Kirchhoff index \(105\). At \(t=1\), every one of the nine edges instead has conductance \(1/9\) and the minimum index is \(81\).

## Relationship to prior work
Ghosh, Boyd, and Saberi established general convex effective-resistance conductance optimization, including duality and explicit examples on barbell graphs. Their framework supplies the general objective but does not state the present particular-price decision rule or the matched-biclique critical window in the inspected proceedings material. Yang studied extremal Kirchhoff index over unweighted bipartite graph topologies, not optimization of priced conductances on a fixed matched biclique. Standard graph-invariant tables already give the Kirchhoff index of unweighted complete bipartite and crown graphs; these are the two fixed-weight endpoints of the spectral calculation, not the present optimization threshold. The result is a price-dependent resource-allocation classification rather than a newly named invariant or a claim to those earlier formulas.

## Limitations
The theorem assumes one matching price shared across matching edges, one shared price for all other edges, equal bipartition sizes, and an undirected continuous-conductance budget. It does not classify arbitrary nonuniform prices or integer/discrete edge-purchasing decisions. The scalar interior root is uniquely specified but not expressed in radicals. The asymptotic statements hold in the specified fixed-price or \(1/n\)-window regimes, not uniformly for arbitrary changing price sequences. Earlier equivalent specialized treatments may exist despite the targeted literature comparisons.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, pp. 1185–1196, https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf; expanded SIAM Review 50 (2008), 37–66, https://doi.org/10.1137/050645452.
2. Y. Yang, *Bounds for the Kirchhoff Index of Bipartite Graphs*, Journal of Applied Mathematics (2012), Article 195242, https://doi.org/10.1155/2012/195242.
3. E. W. Weisstein, *Kirchhoff Index*, MathWorld graph-family table, https://mathworld.wolfram.com/KirchhoffIndex.html (fixed-weight complete bipartite and crown formulas).
4. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339, first online September 5, 2006, https://doi.org/10.1002/qua.21068 (unweighted fixed-graph context).
