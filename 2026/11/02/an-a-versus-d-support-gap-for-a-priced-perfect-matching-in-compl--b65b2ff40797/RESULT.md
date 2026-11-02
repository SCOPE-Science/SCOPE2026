# An A-versus-D support gap for a priced perfect matching in complete bipartite networks

## Finding

Let \(m\ge3\) be an integer. In \(K_{m,m}\), mark the perfect matching \(M=\{u_iv_i:1\le i\le m\}\). Assign arbitrary individual nonnegative conductances to the \(m^2\) edges. A matched edge costs \(P>0\) per conductance unit; every other edge costs \(Q>0\); the expenditure bound is \(B>0\). A disconnected allocation has infinite total effective resistance and zero spanning-tree determinant. Define \(r=P/Q\), and

\[
 r_A(m)=\frac{m^2(4m^2-11m+8)}{(m-2)(4m^3-11m^2+10m-4)},\qquad
 r_D(m)=\frac{m(2m-3)}{(m-2)(2m-1)}.
\]

**Theorem.** Both (A) minimizing the sum of all unordered-pair effective resistances and (D) maximizing the weighted spanning-tree determinant have unique global optimizers among all individual conductance allocations. Each assigns a common weight \(x\) to matched edges and a common weight \(y>0\) to unmatched edges. The A-optimizer satisfies \(x=0\) precisely for \(r\ge r_A(m)\); the D-optimizer satisfies \(x=0\) precisely for \(r\ge r_D(m)\). For every \(m\ge3\),

\[
0<r_D(m)<r_A(m),\quad
r_A(m)-r_D(m)=\frac{2m(m-1)(4m^2-9m+6)}{(m-2)(2m-1)(4m^3-11m^2+10m-4)}>0.
\]

Consequently, throughout the nonempty price interval \(r_D(m)\le r<r_A(m)\), the D-optimal design deletes the entire perfect matching while the A-optimal design retains it. At \(m=4\), the two thresholds are \(10/7\) and \(56/29\), respectively.

For the A-optimal allocation with \(r<r_A(m)\), let \(u_A>0\) be the unique solution to

\[
0=rH_m(u)+(ru+m-1)H_m'(u),\quad
H_m(u)=\frac1{2(u+m-1)}+\frac{m-1}{m}+\frac{m-1}{2u+m-2}.
\]

Then \(y_A=B/[mQ(ru_A+m-1)]\) and \(x_A=u_A y_A\). For \(r\ge r_A(m)\), take \(u_A=0\), \(x_A=0\), and \(y_A=B/[m(m-1)Q]\). These are exact (univariate rational-root) prescriptions; the equation after clearing its strictly positive denominator is quartic. Its uniqueness is in the positive real domain, not a claim about complex roots.

In the critical price scaling \(r=1+\gamma/m\) with any fixed \(\gamma\ge0\), let \(u_D=x_D/y_D\) be the analogous ratio at the D-optimum. Then

\[
\lim_{m\to\infty}u_A=\max\{0,1-\gamma/2\},\qquad
\lim_{m\to\infty}u_D=\max\{0,1-\gamma\}.
\]

In particular \(r_A=1+2/m+O(m^{-2})\), whereas \(r_D=1+1/m+O(m^{-2})\): the two criteria disagree across an asymptotically order-\(1/m\) price window.

## Assumptions and scope

The weighted Laplacian is \(L=\sum_{\{i,j\}\in E} w_{ij}(e_i-e_j)(e_i-e_j)^T\), with \(w_{ij}\ge0\). For a connected weighted graph on \(n=2m\) vertices, the A-objective is \(\mathcal K=n\operatorname{tr}(L^\dagger)=\sum_{i<j}(e_i-e_j)^TL^\dagger(e_i-e_j)\), and the D-objective is \(\tau=\prod_{k=2}^{n}\lambda_k(L)/n\). The feasible domain consists of nonnegative conductances satisfying \(P\sum_{e\in M}w_e+Q\sum_{e\notin M}w_e\le B\), with connected support for finite A-objective or positive D-objective. No edgewise symmetry restriction is imposed. At \(m=2\), removing all matched edges disconnects the network and the assertion is not made.

## Proof

**1. Global uniqueness and symmetry.** On \(\mathbf1^\perp\), the Laplacian of a connected graph is positive definite. The map \(L\mapsto\operatorname{tr}((L|_{\mathbf1^\perp})^{-1})\) is strictly convex along every nonconstant affine line of positive-definite matrices: for symmetric nonzero \(E\), its second directional derivative is \(2\operatorname{tr}(A^{-1}EA^{-1}EA^{-1})>0\). The map from individual edge conductances to the Laplacian is injective because each off-diagonal matrix entry is the negative of its unique corresponding edge weight. Hence the A-objective is strictly convex in the individual conductances wherever the network is connected. The D-objective \(\log\det(L|_{\mathbf1^\perp})\) is strictly concave by the same injectivity. The feasible budget set is compact, and the objective diverges (respectively tends to zero) on disconnected limits, so both unique optima exist. Scaling all conductances up improves either objective, so expenditure is exactly \(B\).

Simultaneously permuting the matched index pairs and interchanging the two bipartition classes preserves both objectives and prices. This symmetry group is transitive separately on the matched and unmatched edge sets. Uniqueness thus forces common matched weight \(x\) and common unmatched weight \(y\). Since \(m\ge3\), the crown graph \(K_{m,m}\setminus M\) is connected, so \(x=0\) is admissible, while \(y=0\) disconnects the graph; therefore \(y>0\) at either optimum.

**2. Exact spectrum.** In the two classes, put \(d=x+(m-1)y\). With the matched pairs in order, the Laplacian has block form

\[
L=\begin{pmatrix}dI_m&-xI_m-y(J_m-I_m)\\-xI_m-y(J_m-I_m)&dI_m\end{pmatrix}.
\]

The vectors constant on each class yield eigenvalues \(0\) and \(2d\). For every vector orthogonal to the all-ones vector in a class, its symmetric and antisymmetric lifts give eigenvalues \(my\) and \(2x+(m-2)y\), each with multiplicity \(m-1\). Thus

\[
\mathcal K(x,y)=2m\left[\frac1{2d}+\frac{m-1}{my}+\frac{m-1}{2x+(m-2)y}\right],
\]

and, by the matrix-tree identity,

\[
\tau(x,y)=\frac{2d}{2m}(my)^{m-1}[2x+(m-2)y]^{m-1}.
\]

**3. A-optimal threshold.** Put \(u=x/y\ge0\). Budget equality gives \(y=B/[mQ(ru+m-1)]\). Substituting in the A-objective gives the positive multiple

\[
\mathcal K(u)=\frac{2m^2Q}{B}(ru+m-1)H_m(u).
\]

For \(u>0\), stationary points therefore solve \(rH_m(u)+(ru+m-1)H_m'(u)=0\). At the boundary,

\[
H_m(0)=\frac1{2(m-1)}+\frac{m-1}{m}+\frac{m-1}{m-2},\qquad
H_m'(0)=-\frac1{2(m-1)^2}-\frac{2(m-1)}{(m-2)^2}.
\]

The one-sided derivative has the sign of \(r-r_A(m)\), where

\[
r_A(m)=-\frac{(m-1)H_m'(0)}{H_m(0)}
=\frac{m^2(4m^2-11m+8)}{(m-2)(4m^3-11m^2+10m-4)}.
\]

Strict convexity on the affine budget line implies that the one-sided derivative is nonnegative exactly when its left endpoint \(x=0\) is optimal. If it is negative, there is a unique interior optimum: as \(y\downarrow0\), the reciprocal \(my\) term diverges. The change of parameter \(u\mapsto x=Bu/[mQ(ru+m-1)]\) is strictly increasing, so uniqueness along the affine budget line gives uniqueness of the nonnegative stationary solution.

**4. D-optimal threshold.** The D-objective after substituting budget has log, up to constants,

\[
\log\tau(u)=\log(u+m-1)+(m-1)\log(2u+m-2)-(2m-1)\log(ru+m-1)+C.
\]

Its right derivative at zero is

\[
\frac1{m-1}+\frac{2(m-1)}{m-2}-\frac{(2m-1)r}{m-1}.
\]

Since \(\log\tau\) is strictly concave as a function of the linearly constrained pair \((x,y)\), the matching is deleted exactly when that derivative is nonpositive, i.e. at \(r\ge r_D(m)\). The denominator in \(r_A-r_D\) is positive: \(m-2>0\), \(2m-1>0\), and \(4m^3-11m^2+10m-4=m(m-2)(4m-3)+4(m-1)>0\). The numerator is positive because \(4m^2-9m+6>0\) (discriminant \(-15\)). This proves the strict gap.

**5. Critical-window scaling.** Let \(r=1+\gamma/m\) for fixed \(\gamma\ge0\). For every fixed \(u\ge0\), the derivatives satisfy

\[
\lim_{m\to\infty}m\frac{d}{du}[(ru+m-1)H_m(u)]=2\gamma+4u-4,
\]

\[
\lim_{m\to\infty}m\frac{d}{du}\log\tau(u)=2-2\gamma-2u.
\]

The convergence is uniform on compact intervals. For either optimization problem, strict convexity/concavity on the affine budget line and the derivative signs at two fixed points enclosing the limiting critical point show convergence of the unique nonnegative optimizer to the respective positive-part expression (at equality, use any fixed positive upper comparison point). Expansion of the rational thresholds yields the asserted \(1/m\) and \(2/m\) leading constants. No stronger error rate for the optimizer itself is claimed.

## Verification

The attached `verify_matching.py` reconstructs the symbolic threshold equations, threshold difference, and limiting derivative identities. It also checks 63 full weighted-Laplacian spectral decompositions against the formulas above, 63 budget/support configurations, 1,890 asymmetric feasible allocations, and 12 successful numerical optimizations over the individual edge variables. The script completed successfully with Python, NumPy, SciPy, and SymPy. These finite checks are safeguards, not substitutes for the all-parameter proof.

## Relationship to prior work

Ghosh, Boyd and Saberi established the convex total-effective-resistance conductance-allocation framework and solved several graph families analytically; their July 2006 conference paper studies trees/barbells rather than priced matching classes in \(K_{m,m}\). Yang's 2012 work treats extremal unweighted bipartite Kirchhoff indices, not independent conductance-price allocation. Klee and Stamps obtain the unweighted crown-graph Laplacian spectrum, which covers the \(x=0\) spectral endpoint but not its optimal-price frontier. Khosoussi and coauthors analyze spanning-tree-determinant design and edge selection, not an A-versus-D cutoff comparison on this family. The matched-edge prices and objective-dependent exact support gap are the asserted additional statements. Their derivation uses standard convexity and spectral tools; general spectral or optimization theory is not claimed as new.

## Limitations

This is a classification of a two-price balanced bipartite family; it is not a theorem for arbitrary priced graphs or unequal bipartitions. The root equation is an implicit but unique exact characterization, not a closed radical formula for each \(x_A\). Numerical tests are finite and do not independently certify the infinite-family proof. A specialized unlocated prior source could cover the threshold despite the comparisons described; no claim of exhaustive publication priority is made. No independent external audit is asserted.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf . Expanded: *SIAM Review* 50(1), 37–66 (2008), https://doi.org/10.1137/050645452 .
2. Y. Yang, *Bounds for the Kirchhoff Index of Bipartite Graphs*, *Journal of Applied Mathematics* (2012), Article 195242. https://doi.org/10.1155/2012/195242 .
3. S. Klee and M. T. Stamps, *Eigenvalues of Graph Laplacians via Rank-One Perturbations*, arXiv:2008.01669 (2020), Section 3.3 on crown-graph spectra. https://arxiv.org/abs/2008.01669 .
4. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116 (2016). https://arxiv.org/abs/1604.01116 .
