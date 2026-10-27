# A corner-maximum principle for endpoint Hodge norms under arbitrary graph subdivisions

## Finding

Let \(G=(V,E)\) be a finite connected simple graph with at least one edge, and let \(\mathbf r=(r_e)_{e\in E}\) be a vector of positive integers. Replace each edge \(e\) with a path of \(r_e\) unit edges whose internal vertices are new and disjoint from all other replacement paths. Denote the resulting graph by \(G_{\mathbf r}\). Let \(C_{\mathbf r}\) be the Euclidean orthogonal projection onto the real cycle-flow space of \(G_{\mathbf r}\), and let \(Q_{\mathbf r}=I-C_{\mathbf r}\) be the cut-space projection. Both are evaluated as operators on ordinary, unweighted edge-coordinate \(\ell_1\).

**Corner-maximum theorem.** For any finite integer bounds \(1\le a_e\le b_e\), every integer choice \(a_e\le r_e\le b_e\), and either \(P=C\) or \(P=Q\),
\[
\boxed{\ \|P_{\mathbf r}\|_{1\to1}\le
\max_{\boldsymbol\varepsilon\in\{0,1\}^{E}}
\|P_{\mathbf s(\boldsymbol\varepsilon)}\|_{1\to1},\qquad
s_e(\boldsymbol\varepsilon)=
\begin{cases}a_e,&\varepsilon_e=0,\\ b_e,&\varepsilon_e=1.\end{cases}\ }
\]
Thus a worst-case endpoint norm over an entire multidimensional box of edge-subdivision budgets is realized at a corner: **no intermediate series length can be uniquely worst**. The same conclusion holds for the induced \(\ell_\infty\) norms. More precisely, both norm functions admit continuous extensions to \([1,\infty)^E\) that are quasiconvex in each coordinate separately. Here quasiconvex means the value at any intermediate point is at most the maximum of the values at the two endpoints; joint quasiconvexity is *not* asserted.

The theorem cannot be strengthened to monotonicity. Take the **diamond graph**, with two triangles sharing one edge \(e\), and replace only \(e\) by a length-\(k\) path. Then, for every integer \(k\ge1\),
\[
\boxed{\ \|C_k\|_{1\to1}=\max\left\{\frac{k+2}{k+1},\frac{3k+2}{2(k+1)}\right\}.\ }
\]
The norm decreases from \(3/2\) at \(k=1\) to \(4/3\) at \(k=2\), then strictly increases towards \(3/2\). The unique minimum over integral and real lengths \(k\ge1\) occurs at \(k=2\). This sharp dip explains why the corner theorem is an endpoint *maximum* principle rather than an individual-edge monotonicity law.

## Assumptions and scope

The graph is finite, connected, simple, and loopless; every replacement path has new degree-two interior vertices. All spaces, orthogonal projections, and induced \(\ell_1\) and \(\ell_\infty\) operator norms are real. Orient the original edges arbitrarily and the replacement paths consistently. Results are independent of orientations because changing orientations conjugates the projections by signed coordinate permutations. These are norms of the **canonical Euclidean orthogonal** projections, not minima over all projections. The continuous extensions are formal analytic interpolations of the exact integer-length formulas; graphs of fractional path length are **not** asserted to exist.

## Proof

**1. Exact weighted reduction.** Fix a cycle-basis matrix \(B\) of \(G\), whose full-rank columns span \(\ker\partial_G\). In the zero-cycle case set the matrices below to zero. Let \(R=\operatorname{diag}(r_e)\), and put
\[
H(\mathbf r)=B(B^{\mathsf T}RB)^{-1}B^{\mathsf T}.
\]
The replication map \(U\) repeats each old edge coordinate \(r_e\) times. Conservation at a new degree-two vertex makes every cycle flow constant along its replacement path, so \(\ker\partial_{G_{\mathbf r}}=U\ker\partial_G\) and \(U^{\mathsf T}U=R\). Hence the *ordinary* orthogonal cycle projector is exactly \(C_{\mathbf r}=UH(\mathbf r)U^{\mathsf T}\); the complementary projector is \(Q_{\mathbf r}=I-C_{\mathbf r}\). In particular the column indexed by any subedge of \(f\) has cycle-column sum
\[
A_f(\mathbf r)=\sum_{g\in E}r_g|H_{gf}(\mathbf r)|.
\]
Since the diagonal of a genuine orthogonal projector is between zero and one, the cut-column sum is
\[
B_f(\mathbf r)=1+A_f(\mathbf r)-2H_{ff}(\mathbf r).
\]
Thus the norm functions at integral \(\mathbf r\) are precisely \(M_C(\mathbf r)=\max_f A_f(\mathbf r)\) and \(M_Q(\mathbf r)=\max_f B_f(\mathbf r)\). Use these formulas as continuous extensions for real \(r_e\ge1\). Positivity follows from the corresponding weighted orthogonal projection: \(0\le r_fH_{ff}\le1\), hence \(0\le H_{ff}\le1\), and the displayed absolute column sums are nonnegative.

**2. Rank-one dependence on one length.** Hold all coordinates except \(r_e=t\ge1\) fixed at arbitrary real values at least one. Denote the matrix at \(t=1\) by \(H^0\), and set \(h=H^0_{ee}\), \(c_g=H^0_{ge}\), and \(d(t)=1+(t-1)h>0\). The Sherman–Morrison identity applied to the positive-definite cycle-basis Gram matrix gives
\[
H_{gf}(t)=H^0_{gf}-\frac{t-1}{d(t)}c_gc_f.
\]
For the distinguished edge, \(H_{ge}(t)=c_g/d(t)\). Therefore its two column sums are
\[
A_e(t)=\frac{\sum_{g\ne e}r_g|c_g|+th}{d(t)},\qquad
B_e(t)=\frac{d(t)+\sum_{g\ne e}r_g|c_g|+(t-2)h}{d(t)}.
\]
For any other edge \(f\ne e\), let \(D_{gf}(t)=d(t)H^0_{gf}-(t-1)c_gc_f\). Then
\[
A_f(t)=\frac{\sum_{g\ne e}r_g|D_{gf}(t)|+t|c_f|}{d(t)},
\]
\[
B_f(t)=\frac{d(t)+\sum_{g\ne e}r_g|D_{gf}(t)|+t|c_f|-2D_{ff}(t)}{d(t)}.
\]
Each numerator is convex in \(t\) because it is a sum of absolute values of affine functions and further affine terms; \(d(t)\) is strictly positive and affine. These statements also cover bridges and forests, where the relevant entries simply vanish.

**3. Fractional-convex maximum inequality.** If \(N(t)\) is convex and \(d(t)>0\) affine on an interval, then for \(s\le t\le u\), writing \(t=(1-\theta)s+\theta u\),
\[
\frac{N(t)}{d(t)}\le
\frac{(1-\theta)N(s)+\theta N(u)}{(1-\theta)d(s)+\theta d(u)}
\le\max\left\{\frac{N(s)}{d(s)},\frac{N(u)}{d(u)}\right\}.
\]
Apply this separately to every cycle and cut column and then maximize over \(f\): both \(M_C\) and \(M_Q\) are quasiconvex in \(t\), uniformly in all other lengths.

**4. Corner reduction.** For any \(\mathbf r\in\prod_e[a_e,b_e]\), apply the one-coordinate maximum inequality to its first coordinate to bound either norm by the maximum of its two endpoint-length values. Repeat successively in the other coordinates. After \(|E|\) applications every remaining length vector is a corner. The argument is valid at all real intermediates and hence at integer subdivision vectors. The projectors are symmetric, so induced \(\ell_\infty\) and \(\ell_1\) norms coincide.

**5. Sharp nonmonotonic witness.** Orient the diamond edges as the common edge \(uv\), followed by \(ua,va,ub,vb\), with the two triangle cycles \((1,-1,1,0,0)\) and \((1,0,0,-1,1)\). Their Gram matrix is \(\begin{psmallmatrix}3&1\\1&3\end{psmallmatrix}\), with inverse \(\frac18\begin{psmallmatrix}3&-1\\-1&3\end{psmallmatrix}\). When only the common edge is given length \(k\), the resulting Gram matrix is \(\begin{psmallmatrix}k+2&k\\k&k+2\end{psmallmatrix}\), whose inverse is
\[
\frac{1}{4(k+1)}\begin{pmatrix}k+2&-k\\-k&k+2\end{pmatrix}.
\]
The common-path columns have absolute sum \((k+2)/(k+1)\), while each of the four other-edge columns has absolute sum \((3k+2)/(2(k+1))\). The former decreases strictly, the latter increases strictly, and they coincide exactly at \(k=2\). This proves the displayed formula, both strict trends, and uniqueness of the minimum.

## Verification

The included standalone `verify.py` uses only the Python standard library and exact rational arithmetic. It builds independent fundamental-cycle bases and Gram projectors, and independently reconstructs the Euclidean projector of each explicitly subdivided graph from its grounded incidence Laplacian. It checks both operator norms in **28 direct expanded-graph cases**, tests **216 coordinatewise midpoint comparisons**, exhaustively checks the box-bound inequality over **2,052 finite subdivision vectors**, and verifies the diamond identity for **17 lengths**. Run `python verify.py`. These are finite checks only; Steps 1–5 prove the universal statement.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii established the real graph-cycle projection setting, orthogonal/invariant projection framework, and exact examples for tori and Hamming graphs. Earlier treatments of diamond and Laakso graphs motivate studying edge refinements. A known nonuniform subdivision identity already gives the pointwise Gram-matrix expression for canonical cycle and cut projection norms; that pointwise identity is **not claimed as new**. The result here is the separate **coordinatewise quasiconvex optimization law**, its multidimensional corner-maximum consequence, and the precise nonmonotonic witness. These conclusions require comparing different length vectors via a rank-one Gram update and fractional-convex inequalities; simply evaluating one of the pointwise formulas does not constitute the comparison.

Nowak and Stachowiak's 2026 discussion of edge subdivision addresses exactness and preservation of quadratic residuals under appropriately scaled series reductions, rather than maximum absolute column sums of ordinary unit-edge projectors across independent subdivision budgets. Search results do not constitute a proof of absolute bibliographic novelty; the broad pointwise identity creates an especially relevant residual overlap risk.

## Limitations

The corner bound is a **worst-case** statement; it does not claim coordinatewise monotonicity, convexity, or joint quasiconvexity. It uses finite connected simple graphs, unit edges after subdivision, and canonical orthogonal projectors. It does not optimize arbitrary nonorthogonal projection operators or assert the result for arbitrary weighted \(\ell_p\) norms. The existing pointwise nonuniform-subdivision formula is strong prior coverage; the only asserted new mathematical content is the global inequality/optimization principle and its sharp nonmonotone interpretation. No independent mathematical assessment or exhaustive literature search has been performed.

## References

1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first publicly submitted 2023-05-21, §§1.4–1.6 and 2. https://arxiv.org/html/2305.12582v1
2. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first publicly submitted 2018-07-10. https://arxiv.org/abs/1807.03814
3. P. Nowak and M. Stachowiak, *Cycle Closure: Exact Potentials, Weighted Defects, and Scale Compatibility*, 2026, §5.1, doi:10.5281/zenodo.21726647. https://doi.org/10.5281/zenodo.21726647
