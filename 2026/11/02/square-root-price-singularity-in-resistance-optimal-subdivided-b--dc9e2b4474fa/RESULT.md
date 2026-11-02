# Square-root price singularity in resistance-optimal subdivided bicliques

## Finding

For integers \(p,q\ge2\), subdivide every edge of \(K_{p,q}\) once, giving a graph \(S(K_{p,q})\) with \(N=p+q+pq\) vertices. A spoke joining an inserted vertex to the \(p\)-vertex side costs \(P>0\) per unit conductance; a spoke joining it to the \(q\)-vertex side costs \(Q>0\). All \(2pq\) edge conductances are independently selectable and nonnegative subject to total price \(B>0\). Minimize the sum \(\mathcal K\) of effective resistances over unordered vertex pairs, with disconnected networks assigned objective \(+\infty\).

**Theorem.** The unrestricted minimizer is unique, assigns a common strictly positive conductance \(x\) to every \(p\)-side spoke and a common strictly positive conductance \(y\) to every \(q\)-side spoke, and spends the full budget \(pq(Px+Qy)=B\). Define
\[
\begin{aligned}
 a_{p,q}&=\frac{p-1}{q}+\frac{(q-1)(p+1)}p+\frac{p+1}{N},\\
 b_{p,q}&=\frac{(p-1)(q+1)}q+\frac{q-1}{p}+\frac{q+1}{N},\\
 c_{p,q}&=(p-1)(q-1).
\end{aligned}
\]
Then the exact resistance objective for every positive orbit-constant pair is
\[
\boxed{\ \mathcal K(x,y)=N\left(\frac{a_{p,q}}x+\frac{b_{p,q}}y+\frac{c_{p,q}}{x+y}\right).\ }
\]
The unique optimal ratio \(t=y/x\) is the positive root of
\[
\boxed{\ Q a_{p,q}-\frac{P b_{p,q}}{t^2}+\frac{c_{p,q}(Q-P)}{(1+t)^2}=0,\ }
\]
and \(x=B/[pq(P+Qt)]\), \(y=tx\).

For the balanced family \(p=q=m\ge2\), with prices \(P,Q\) fixed, the expensive side receives asymptotically negligible but strictly positive conductance:
\[
\begin{cases}
\displaystyle\lim_{m\to\infty}\sqrt m\,\frac{y}{x}=\sqrt{\frac P{Q-P}},&Q>P,\\[6pt]
\displaystyle\lim_{m\to\infty}\sqrt m\,\frac{x}{y}=\sqrt{\frac Q{P-Q}},&P>Q,\\[6pt]
\displaystyle y/x=1\text{ for every }m,&P=Q.
\end{cases}
\]
There is a nontrivial transition at the *inverse-size price scale*. If \(P>0\) is fixed and \(Q_m=P(1+\delta/m)\) for fixed real \(\delta\) and sufficiently large \(m\), then
\[
\boxed{\ \frac{y_m}{x_m}\longrightarrow t_\delta>0,\qquad
\delta=\frac{(1-t_\delta)(1+t_\delta)^3}{t_\delta^2}.\ }
\]
For every \(\delta\in\mathbb R\) the displayed equation has exactly one positive solution.

## Assumptions and scope

Graphs are finite, simple, undirected and weighted by nonnegative edge conductances. Each original edge \(ij\) of \(K_{p,q}\) has a private inserted vertex \(z_{ij}\), adjacent only to its two original endpoints. The two pricing classes refer to *which side the original endpoint belongs to*, not to incident edge multiplicity. The budget constraint is an equality at the optimum because increasing every conductance uniformly strictly reduces effective resistance. A disconnected allocation has infinite total pairwise resistance. Both finite-size formulas hold for all integers \(p,q\ge2\), and all real prices and budgets \(P,Q,B>0\). The two asymptotic regimes are for balanced graphs with \(m\to\infty\); the critical window uses fixed \(\delta\), not \(\delta\) varying with \(m\).

## Proof

**Global symmetry and uniqueness.** Let \(L(w)\) be the weighted Laplacian on \(N\) vertices, and let \(J\) be the all-ones matrix. On connected networks, \(\operatorname{tr}(L^+)=\operatorname{tr}[(L+J/N)^{-1}]-1\). The trace-inverse is strictly convex in positive-definite matrices: along any nonzero symmetric direction \(H\), its second derivative is \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). This is positive because \(A^{-1/2}HA^{-1/2}\ne0\). On a simple graph the mapping from individual edge conductances to \(L\) is injective by its off-diagonal entries, so the connected objective is strictly convex in all edge conductances. On the compact budget simplex the objective diverges when the graph becomes disconnected, hence it has a unique minimizer. Permutations within either original vertex class induce graph automorphisms that preserve prices, so uniqueness forces all \(p\)-side spoke weights to be \(x\) and all \(q\)-side spoke weights to be \(y\). Connectedness forces both strictly positive. Homogeneity forces full expenditure.

**Exact Laplacian trace.** Decompose the vertex space into the constant and standard representations of the two permutation groups. The subspace of inserted-vertex functions with all row and column sums zero has dimension \((p-1)(q-1)\) and Laplacian eigenvalue \(x+y\). Each of the \(p-1\) left-standard components is represented by a two-dimensional Laplacian block having eigenvalue sum \(qx+x+y\) and product \(qxy\). Each of the \(q-1\) right-standard blocks has eigenvalue sum \(py+x+y\) and product \(pxy\). The three-dimensional constant component has one zero eigenvalue, and its other two eigenvalues have sum \(qx+py+x+y\) and product \(Nxy\). The dimensions total \(N\). Using reciprocal-root sum = root sum/root product for each two-dimensional block yields
\[
\operatorname{tr}(L^+)=\frac{(p-1)(q-1)}{x+y}
+(p-1)\frac{qx+x+y}{qxy}
+(q-1)\frac{py+x+y}{pxy}
+\frac{qx+py+x+y}{Nxy}.
\]
Collecting the coefficients of \(1/x\) and \(1/y\) gives \(a_{p,q}\), \(b_{p,q}\) and \(c_{p,q}\) above. Kirchhoff's spectral identity \(\mathcal K=N\operatorname{tr}(L^+)\) proves the first boxed formula.

**Exact optimizer.** Substitute \(y=tx\) and \(x=B/[pq(P+Qt)]\) to obtain
\[
\mathcal K(t)=\frac{Npq}{B}(P+Qt)
\left(a_{p,q}+\frac{b_{p,q}}t+\frac{c_{p,q}}{1+t}\right).
\]
Differentiating gives the stated stationary equation. This function diverges both at \(t\downarrow0\) and \(t\uparrow\infty\), while strict convexity along the one-dimensional linear-budget segment implies a unique global minimizer and a unique stationary root.

**Square-root price law.** For \(p=q=m\), symmetry gives \(a_{m,m}=b_{m,m}=a_m\), where
\[
a_m=\frac{m^3+3m^2+m-3}{m(m+2)}=m+O(1),\qquad c_m=(m-1)^2=m^2+O(m).
\]
For \(Q>P\), the stationarity equation is
\[
\frac{P}{t_m^2}=Q+\frac{c_m}{a_m}\frac{Q-P}{(1+t_m)^2}.
\]
Since \(c_m/a_m\sim m\), its unique solution satisfies \(t_m\to0\). Multiplication by \(t_m^2\) then yields \(m t_m^2\to P/(Q-P)\). Interchanging the pricing classes gives the case \(P>Q\). If \(P=Q\), the exact equation reduces to \(t_m=1\).

**Critical window.** With \(Q_m/P=1+\delta/m\), divide the stationary equation by \(Pa_m\). Any root has a positive finite limit, since the equation is
\[
1+\frac\delta m-\frac1{t_m^2}+\frac{c_m}{a_m}\frac{\delta/m}{(1+t_m)^2}=0,
\]
with \(c_m/(ma_m)\to1\). The limiting equation is \(1-t^{-2}+\delta/(1+t)^2=0\), or the stated relation for \(\delta\). The function \(\phi(t)=(1-t)(1+t)^3/t^2\) has derivative
\[
\phi'(t)=-\frac{2(1+t)^2(t^2-t+1)}{t^3}<0,
\]
and maps \((0,\infty)\) continuously onto all of \(\mathbb R\). It therefore has a unique inverse. Strict monotonicity of the finite-size optimum and a compactness/bracketing argument prove \(t_m\to t_\delta\).

## Verification

The standalone \(\texttt{verify.py}\) replays 63 test groups, including full weighted-Laplacian spectra for six unequal/balanced bipartitions at three edge weight pairs, strict scalar objective minimizers for 30 price/size configurations, exact symbolic identities and derivative factorization, and 13 finite-size asymptotic comparisons. All passed in the delivered package. These finite tests independently corroborate calculations; the infinite parameter and limiting claims follow from the proof, not the tests.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006) prove general convexity and uniqueness for unpriced total-effective-resistance allocation and derive analytic solutions for other graph types (notably the barbell), providing the underlying optimization motivation, but not the edge-subdivided biclique trace, unequal spoke prices or its singular price law. Yang and Klein (arXiv version March 7, 2014) study unweighted Kirchhoff-index formulas for subdivisions and triangulations of general graphs; their results cover unit-conductance invariant calculations but not this priced conductance optimization or the critical window. The present proof develops an explicit weighted eigenspace reduction and exact two-orbit optimization.

## Limitations

This is a theorem for edge-subdivided complete bipartite graphs, not arbitrary subdivisions or directed networks. Only the balanced regime is analyzed asymptotically, and \(p,q\) are both at least two. Unrestricted uniqueness follows from convexity, while the scalar formulas require the derived symmetry reduction. Mathematical originality is assessed against the inspected primary sources and relevant searched records, not established by a proof of absence from all literature. An independent mathematical review has not been performed.

## References

- A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006, pp. 1185–1196. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
- Y. Yang and D. J. Klein, *Resistance distance-based graph invariants of subdivisions and triangulations of graphs*, arXiv:1403.1851, public preprint March 7, 2014. https://arxiv.org/abs/1403.1851
