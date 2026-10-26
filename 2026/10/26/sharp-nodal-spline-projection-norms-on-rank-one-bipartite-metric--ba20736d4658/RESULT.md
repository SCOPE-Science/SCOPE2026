# Sharp nodal spline projection norms on rank-one bipartite metric graphs

## Finding
Let \(a,b\geq2\). Form a complete bipartite metric graph \(K_{a,b}\), assigning positive lengths \(\ell_{ij}=u_i v_j\) to its edges. The \(L^2\)-orthogonal projector \(P\) onto the continuous functions affine in arclength along every edge has the **exact sharp endpoint norms**
\[
\|P\|_{L^1\to L^1}=\|P\|_{L^\infty\to L^\infty}
=\frac73-\frac{4\vartheta}{3(1+\vartheta)},\qquad
\vartheta=\min\left\{\min_i\frac{u_i}{\sum_hu_h},\ \min_j\frac{v_j}{\sum_hv_h}\right\}.
\]
The maximal absolute amplification occurs precisely at the graph vertices whose normalized factors equal \(\vartheta\). For each maximizing vertex, the sign of its projection kernel is a bounded measurable input attaining the displayed \(L^\infty\) norm.

For each fixed pair \((a,b)\), write \(r=\max\{a,b\}\). Then
\[
\min_{u_i,v_j>0}\|P\|=\frac73-\frac4{3(r+1)},\qquad
\sup_{u_i,v_j>0}\|P\|=\frac73.
\]
The minimum is attained exactly when every normalized factor on *both* sides is at least \(1/r\); the supremum is not attained. Thus, when \(a=b\), the minimum has unique balanced normalized lengths on both sides. When \(a>b\), all \(u_i/\sum_hu_h=1/a\), while each \(v_j/\sum_hv_h\ge1/a\); the analogous statement holds with the sides exchanged. Over the entire family with \(a,b\ge2\), the least possible norm is \(17/9\), attained for \(a=b=2\) with uniform normalized factors.

The sharp maximal negative excursion of \(Pf\), among measurable \(0\leq f\leq1\) and all graph points, equals
\[
\sup_{0\leq f\leq1}\|(-Pf)_+\|_\infty
=\frac23-\frac{2\vartheta}{3(1+\vartheta)}.
\]

## Assumptions and scope
The graph contains exactly the \(ab\) edges joining vertices \(U_i\) to \(V_j\), with positive edgewise arclength measure and lengths \(u_i v_j\). Distinct edges meet only at their common original vertices. There are no extra interior finite-element nodes. The domain of \(P\) is \(L^2\) on the disjoint edge interiors with identified vertex endpoints; its range consists of continuous, edgewise affine nodal splines. The same finite-rank integral formula extends \(P\) boundedly to \(L^1\) and \(L^\infty\). All stated norms are induced by the unnormalized arclength measure; multiplying all edge measures by one constant does not change \(P\).

The rank-one factorization of lengths is essential; no assertion is made for an arbitrary matrix of positive edge lengths. The conditions \(a,b\ge2\) ensure the graph is genuinely cyclic and not a single interval or star.

## Proof
Let \(\varphi_z\) be the standard vertex-hat functions, equal to one at \(z\), zero at all other graph vertices, and affine on each edge. Put \(U=\sum_i u_i\) and \(V=\sum_j v_j\). Exact integration of the products of two hats yields the symmetric Gram matrix \(M\):
\[
M_{U_iU_h}=\delta_{ih}\frac{u_iV}{3},\quad
M_{V_jV_k}=\delta_{jk}\frac{v_jU}{3},\quad
M_{U_iV_j}=\frac{u_iv_j}{6}.
\]
It is positive definite: if the associated nodal function has zero \(L^2\) norm, it vanishes on every edge and hence at every vertex.

Its inverse has the explicit entries
\[
(M^{-1})_{U_iU_h}=\frac{3\delta_{ih}}{u_iV}+\frac1{UV},\quad
(M^{-1})_{V_jV_k}=\frac{3\delta_{jk}}{v_jU}+\frac1{UV},\quad
(M^{-1})_{U_iV_j}=-\frac2{UV}.
\]
To verify this identity without assuming it, multiply the proposed blocks by the three blocks of \(M\). For the \(UU\) block, the diagonal-block product contributes \(\delta_{ih}\), a remaining \(u_i/(3U)\), and the opposite-block product contributes \(-u_i/(3U)\); they cancel. For the \(UV\) block, the diagonal term contributes \(-2u_i/(3U)\), while the opposite block contributes \(u_i/(6U)+u_i/(2U)\), again zero. The two other blocks follow by symmetry. Hence this is the inverse.

The projector kernel is
\[
K(x,y)=\sum_{z,w}\varphi_z(x)(M^{-1})_{zw}\varphi_w(y).
\]
For a fixed vertex \(U_k\), parameterize the edge \(U_iV_j\) by \(t\in[0,1]\), starting at \(U_i\). Then
\[
K(U_k,(ij,t))=
\begin{cases}
\displaystyle \frac{(1+3/w)(1-t)-2t}{UV},& i=k,\\[3pt]
\displaystyle \frac{1-3t}{UV},&i\ne k,
\end{cases}
\qquad w=\frac{u_k}{U}.
\]
The integral over \([0,1]\) of the absolute value of a linear function with endpoint values \(A>0\) and \(-B<0\) is \((A^2+B^2)/(2(A+B))\). Multiplying the edgewise integral by its edge length and summing, the \(b\) edges incident to \(U_k\) contribute
\[
\frac{(3+w)^2+4w^2}{6(1+w)},
\]
and the remaining edges contribute \(5(1-w)/6\). Their sum simplifies to
\[
\int_G|K(U_k,y)|\,dy
=\frac73-\frac{4w}{3(1+w)}.
\]
Exactly the same calculation at a vertex \(V_j\) holds with \(w=v_j/V\).

Every \(Pf\) is affine along each edge, so its maximum absolute value is attained at some vertex. At each vertex the integral of \(|K|\) is the exact norm of that evaluation functional, attained by its kernel sign. Therefore the operator's \(L^\infty\) norm is the largest vertex integral. Since \(K(x,y)=K(y,x)\), its integral operator has the same induced \(L^1\) norm by duality. The function \(g(w)=7/3-4w/[3(1+w)]\) has strictly negative derivative \(-4/[3(1+w)^2]\), proving the exact norm and precisely identifying maximizing vertices. No interior edge point is an additional maximizing evaluation location: for endpoints \(U_i,V_j\) of an edge, the kernels \(K(U_i,\cdot)\) and \(K(V_j,\cdot)\) have strictly opposite signs on a positive-measure segment close to \(U_i\), since \(K(U_i,U_i)>0\) whereas \(K(V_j,U_i)=-2/(UV)<0\). Thus strict triangle inequality for the integral of the absolute interpolated kernel applies at every interior point.

The normalized positive factors on the \(a\)- and \(b\)-vertex sides each sum to one. Hence their smallest combined value \(\vartheta\) is at most \(1/r\), with equality exactly when *every* normalized factor is at least \(1/r\). This proves all minimizers and the minimum. A positive factor may approach zero, so \(\vartheta\downarrow0\), showing the supremum \(7/3\) is sharp and unattained. The smallest possible \(r\) is two, proving the global minimum \(17/9\).

Lastly \(P1=1\), hence \(\int_G K(x,y)\,dy=1\). At any vertex, the largest downward excursion for \(0\le f\le1\) is the negative integral of \(K\), namely \(\tfrac12(\int|K|-1)\), attained by the indicator of its negative set. Maximization over vertices gives the stated positivity defect. Inside an edge the function \(Pf\) is affine, so no larger negative excursion occurs there.

## Verification
The accompanying standalone `verify.py` independently constructs exact rational Gram matrices for positive integer edge-factor configurations, inverts them by Gauss–Jordan elimination over rational numbers, integrates the absolute kernels exactly edge by edge, and checks the formulas. It tests a collection of complete bipartite graphs with both color classes of sizes two through five and several nonuniform profiles. The finite tests are a cross-check; the universal assertions follow from the displayed inverse identity and exact integral calculation.

## Relationship to prior work
Grigorieff and Sloan's work investigates stability of continuous splines under nonuniform **interval** grids and discrete inner products; its publicly inspected publisher abstract and author-hosted explanatory abstract do not assert sharp metric-network endpoint norms. Arioli and Benzi's technical report on quantum-graph finite elements develops graph mass matrices and their conditioning (Section 5), including assembled mass-matrix formulas that supply context for our Gram-matrix construction, but its inspected text does not give the sharp bipartite projection norm or its full factor-balancing characterization. Neither result implies the formula here without a new inverse-kernel calculation and sharp absolute integration. In particular, a usual interval spline projector and an energy-gradient projection on a finite graph act on different function spaces and do not cover these operators. This is a limited comparison of inspected literature, not proof of exhaustive historical novelty.

## Limitations
The length matrix must factor as \(\ell_{ij}=u_iv_j\), and no interior edge nodes are included. The equality case for \(L^1\) concerns the operator norm, not necessarily attainment by an \(L^1\) input on this nonatomic measure space. The positive-input excursion and all extremizers mentioned are in \(L^\infty\). Related work under other graph-FEM or approximation-theoretic names might contain an equivalent formula; this possibility remains open pending independent bibliographic examination. The complete 1998 Grigorieff–Sloan paper was not materially inspected; only its publisher abstract and an explanatory abstract were available for the specific domain comparison.

## References
- R. D. Grigorieff and I. H. Sloan, “Stability of discrete orthogonal projections for continuous splines,” *Bulletin of the Australian Mathematical Society* 58 (1998), 307–332; public online version dated 17 April 2009, DOI: 10.1017/S0004972700032263.
- M. Arioli and M. Benzi, “A finite element method for quantum graphs,” Emory University Technical Report TR-2015-009 (October 2015); later *IMA Journal of Numerical Analysis* 38 (2018), 1119–1163, DOI: 10.1093/imanum/drx029. The accessible full text of the technical report was inspected at https://www.researchgate.net/publication/282778059_A_FINITE_ELEMENT_METHOD_FOR_QUANTUM_GRAPHS.
