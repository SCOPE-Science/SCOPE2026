# Sharp optimal and orthogonal cycle projections on two-length path bundles

## Finding
For integers \(r\ge2\) and \(2\le a\le b\), let \(G(a,b;r)\) be the finite simple two-terminal graph consisting of one internally disjoint path of length \(a\) and \(r\) further internally disjoint paths, each of length \(b\), all connecting the same terminals. Give every edge unit \(\ell_1\) weight, orient all paths from the first terminal to the second, and write \(Z=\ker D\subset\ell_1(E(G);\mathbb R)\) for the real cycle-flow space, with \(D\) the oriented incidence map. The relative projection constant, minimizing **over every linear projection** onto \(Z\), is
\[
\lambda(Z,\ell_1(E))=
\begin{cases}
\dfrac{(a+b)^2}{a^2+b^2+2ab/r}, & (r-2)b\le ra,\\[4pt]
1+\dfrac{a}{b}, & (r-2)b\ge ra.
\end{cases}
\]
At equality of the branch conditions the two formulas agree. For \(r=2\) the first branch always applies. The canonical Euclidean-orthogonal cycle projection \(C\) has a different exact endpoint norm:
\[
\|C\|_{1\to1}=\|C\|_{\infty\to\infty}=\frac{r(a+b)}{b+ra}.
\]
The optimal projection changes form sharply when \(r\ge3\) and \(b/a\) crosses \(r/(r-2)\): on the large-ratio side, a minimal projection subtracts the complete path-mean imbalance exclusively along the distinguished shortest path. In the concrete simple, unweighted planar series-parallel family \(G_r=G(2,2r;r)\), for every integer \(r\ge3\),
\[
\lambda(Z(G_r),\ell_1(E(G_r)))=1+\frac1r,
\qquad \|C_{G_r}\|_{1\to1}=\frac{r+1}{2},
\qquad \frac{\|C_{G_r}\|_{1\to1}}{\lambda(Z(G_r),\ell_1(E(G_r)))}=\frac r2.
\]
Thus the canonical orthogonal projector becomes arbitrarily less efficient than the best \(\ell_1\)-projection, even within simple two-terminal series-parallel graphs.

## Assumptions and scope
All parameters above are integers. The paths have disjoint internal vertices; there are no parallel edges because \(a,b\ge2\). The edge norm is the unweighted real \(\ell_1\)-norm. The minimization is over all real linear idempotents with range \(Z\), without requiring orthogonality or graph-automorphism invariance. The compared canonical projector is orthogonal in the **standard unweighted Euclidean edge inner product**. No analogous assertion about a minimum in the edge \(\ell_\infty\) norm is made.

## Proof
Write \(L_0=a\), \(L_j=b\) for \(1\le j\le r\). A vector \(z\) is in \(Z\) exactly when it is constant with value \(t_i\) along each path \(i\), and \(\sum_{i=0}^{r}t_i=0\): conservation at each internal degree-two vertex makes the flow path-constant, and conservation at a terminal gives the sole relation.

Any permutation of edge coordinates within each path fixes every vector of \(Z\) and is an isometry of the ambient \(\ell_1\). The permutation group of the \(r\) equally long paths also preserves \(Z\) and is isometric. Averaging any projection onto \(Z\) over this finite group cannot increase its norm and produces a commuting projection. It annihilates the zero-mean coordinates on each path; consequently it factors through the vector \(s\) of path coordinate means. A linear projection of \(\mathbb R^{r+1}\) onto the hyperplane \(\sum_i t_i=0\) is precisely \(s\mapsto s-w\sum_i s_i\), where \(\sum_iw_i=1\). Permutation symmetry of the long paths forces \(w_0=u\) and \(w_j=(1-u)/r\) for \(1\le j\le r\), for some real \(u\). Conversely every such choice defines a projection on the whole edge space, so this reduction is exact over all projections.

For a coordinate unit vector supported on path \(i\), the output is constant on path \(j\) with value \((\mathbf1_{i=j}-w_j)/L_i\). Hence the absolute column sum for a short-path edge and a long-path edge, respectively, is
\[
 A(u)=(1+b/a)|1-u|,\qquad
 B(u)=\frac ab|u|+\left|1-\frac{1-u}{r}\right|+\frac{r-1}{r}|1-u|.
\]
The norm is \(\max\{A(u),B(u)\}\). Put \(R=b/a\ge1\). If \(u<0\), then \(A(u)>1+R\ge2\), while \(u=1\) yields norm \(1+R^{-1}\le2\). If \(u>1\), then \(B(u)=u(1+R^{-1})>B(1)\). Thus a minimizer occurs within \([0,1]\). There,
\[
 A(u)=(1+R)(1-u),\qquad B(u)=2-\frac2r+u\left(\frac1R-\frac{r-2}{r}\right).
\]
If \(\gamma=R^{-1}-(r-2)/r>0\), the first function strictly decreases and the second increases, so their unique crossing minimizes the maximum. The crossing is \(u_*=(R-1+2/r)/(R+R^{-1}+2/r)\), and substitution yields \((1+R)^2/(R^2+1+2R/r)\). If \(\gamma<0\), both functions decrease, so \(u_*=1\) is minimal, giving \(1+R^{-1}\). If \(\gamma=0\), the second is constant and the two values coincide at their crossing; the same formula holds with nonunique symmetric minimizers. These cases give the two asserted branches.

For the canonical orthogonal projection, Euclidean minimization of the squared edge distance on the path-constant subspace shows that the corresponding hyperplane coefficient vector has \(w_i=L_i^{-1}/\sum_jL_j^{-1}\). Thus \(w_0=b/(b+ra)\) and \(w_j=a/(b+ra)\) for long paths. Substitution in the two column norms gives
\[
 A_{\mathrm{orth}}=\frac{r(a+b)}{b+ra},\qquad
 B_{\mathrm{orth}}=1+\frac{(r-1)a}{b+ra}.
\]
The difference is \((r-1)(b-a)/(b+ra)\ge0\); hence \(A_{\mathrm{orth}}\) is the operator norm. The projector's real matrix is symmetric, giving the identical induced \(\ell_\infty\) norm. Finally set \(a=2\), \(b=2r\), \(r\ge3\). The second branch is applicable because \(r\ge r/(r-2)\), and direct exact substitution yields the three asserted identities, including the unbounded ratio. All statements hold for every permitted integer parameter, not merely for checked examples.

## Verification
The accompanying standalone exact-rational script `projection_bundle_checker.py` constructs the projectors from path-coordinate means, checks the graph-flow and idempotence conditions, reconstructs the canonical orthogonal projector independently using a cycle-basis Gram inverse, compares full edge-column sums with the formulas, and checks rational competing parameters on a finite grid. It passed 28 graph instances. These finite computations are reproducibility checks; the preceding finite-group symmetrization and one-variable minimax argument establish global optimality for all parameters.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023), §§1.4 and 2, study invariant and minimal cycle-space projections, including Hamming graphs and discrete tori; their finite-group averaging principle is used here and not claimed as new. Their 2018 paper studies recursively generated multibranching diamond and Laakso graphs, including the equal-arm base graph, but the inspected sections do not give this unequal-path two-branch optimum or the graph-family orthogonal/minimal ratio. The equal-length value \(2r/(r+1)\) is a familiar symmetric boundary and is not asserted as an independent new result.

The general study of minimal projections onto hyperplanes in sequence spaces predates this work (Blatter--Cheney, 1974, cited by Baronti--Franchetti, 1990), and Shekhtman--Skrzypek (2014) explicitly compare minimal and orthogonal hyperplane projections. The new graph-specific claim combines the path-incidence reduction, the sharp two-length boundary, and the exact unbounded ratio for the **unweighted Euclidean graph Hodge** projection. A full-text comparison with both older hyperplane articles remains an explicit originality risk; no claim is made to originate generic hyperplane minimax methods.

## Limitations
Only this particular two-length path-bundle family is classified. The explicit minimal projector need not be unique, particularly on the transition boundary. The phenomenon is an unbounded **ratio of two projection norms**, not a claim about intrinsic Banach--Mazur distortion or independent mathematical certification. The full primary texts of Blatter--Cheney (1974) and Shekhtman--Skrzypek (2014) could not be inspected, so equivalence to an earlier graph-specialized statement remains a residual bibliographic risk.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public May 21, 2023), §§1.1, 1.4, 2.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (first public July 10, 2018), §§1, 5--6.
3. J. Blatter and E. W. Cheney, *Minimal projections onto hyperplanes in sequence spaces*, Ann. Mat. Pura Appl. 101 (1974), 215--227, DOI:10.1007/BF02417105 (full text not inspected).
4. M. Baronti and C. Franchetti, *Minimal and polar projections onto hyperplanes in the spaces* \(\ell_p\) *and* \(\ell_\infty\), Riv. Mat. Univ. Parma 16 (1990), 331--342, pp. 331--332 and references.
5. B. Shekhtman and L. Skrzypek, *Minimal versus orthogonal projections onto hyperplanes in* \(\ell_1^n\) *and* \(\ell_\infty^n\) (2014), DOI:10.1007/978-3-319-06404-8_20 (full text not inspected).
