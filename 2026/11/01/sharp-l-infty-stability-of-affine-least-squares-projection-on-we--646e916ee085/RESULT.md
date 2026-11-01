# Sharp \(L^\infty\) stability of affine least-squares projection on weighted metric stars

## Finding
Let a metric star have \(d\ge1\) edges of positive lengths \(\ell_1,\ldots,\ell_d\), with a positive constant volume density \(\rho_i\) on edge \(i\). Set \(m_i=\rho_i\ell_i\), \(M=\sum_{i=1}^d m_i\), and \(q_*=\min_i m_i/M\). Let \(P\) be the real \(L^2\)-orthogonal projection onto functions that are continuous at the common vertex and affine separately on each edge. Its exact, attained maximum-norm operator constant is
\[
\boxed{\|P\|_{L^\infty\to L^\infty}=\frac{7+3q_*}{3(1+q_*)}=\frac73-\frac{4q_*}{3(1+q_*)}.}
\]
The exact norm-maximizing evaluation points are both endpoints if \(d=1\), and precisely the exterior vertices of minimum edge mass if \(d\ge2\). At each such exterior vertex there is an explicit extremizing bounded sign input. The dual \(L^1\)-operator norm equals the same constant.

With the total mass and the number of edges fixed, the unique minimizers among edge-mass vectors have equal edge masses, and the minimum is \((7d+3)/(3(d+1))\). Moreover \(\|P\|>2\) if and only if \(q_*<1/3\): degree at least four forces this threshold, degree three reaches equality only for equal masses, and degree two crosses it precisely under sufficient imbalance. For \(0\le f\le1\), the largest possible negative excursion of \(Pf\) is \(2/[3(1+q_*)]\). The sharp family-wide supremum \(7/3\) is approached as one edge's relative mass tends to zero, but no strictly positive finite mass vector attains it.

## Assumptions and scope
The star is the quotient of intervals \([0,\ell_i]\) by identifying their left endpoints. There is no mass concentrated at vertices. On edge \(i\) write \(s=u/\ell_i\in[0,1]\) and integrate using \(d\mu_i=m_i\,ds\). Each \(m_i\) is strictly positive. The spline space consists of all real continuous functions on this graph whose restrictions are affine in \(s\); no boundary or Kirchhoff derivative conditions are imposed. Orthogonal projection is defined in \(L^2(\mu)\) and extends by the finite-rank kernel to bounded operators on \(L^1(\mu)\) and \(L^\infty(\mu)\). Operator norms on \(L^\infty\) use essential suprema, whereas every projected function has a continuous representative.

## Proof
Let \(\phi_0\) be the central hat with restriction \(1-s\) to every edge, and let \(\phi_i\) equal \(s\) on edge \(i\) and zero on other edges. Their Gram matrix \(G\), with indices \(0,1,\ldots,d\), has entries
\[
G_{00}=M/3,\qquad G_{0i}=m_i/6,\qquad G_{ii}=m_i/3,\qquad G_{ij}=0\quad(i\ne j,\ i,j>0).
\]
The Schur complement of the leaf diagonal is \(M/4\), so direct block inversion gives
\[
(G^{-1})_{00}=4/M,\qquad (G^{-1})_{0i}=-2/M,\qquad
(G^{-1})_{ij}=3\delta_{ij}/m_i+1/M\quad(i,j>0).
\]
This verifies invertibility for every positive mass vector, without any conditioning assumption. At a point on edge \(i\) with relative coordinate \(t\), and on edge \(j\) with relative coordinate \(s\), the reproducing kernel of \(P\) is
\[
K((i,t),(j,s))=\frac{4-6t+(-6+9t)s}{M}+\frac{3ts}{m_i}\,\delta_{ij}.
\]
Hence the row norm is \(R_i(t)=\sum_{j=1}^{d}m_j\int_0^1|K((i,t),(j,s))|\,ds\). For each fixed \((j,s)\), the kernel is affine in \(t\), so \(R_i\) is convex and its maximum occurs at an endpoint. All edge descriptions agree at the center, where
\[
R_i(0)=\int_0^1|4-6s|\,ds=5/3.
\]
At an exterior vertex let \(q=m_i/M\). The kernel equals \((-2+3s)/M\) on every other edge and \([-2+3(1+q^{-1})s]/M\) on edge \(i\). Direct integration of these two affine absolute values gives
\[
\begin{aligned}
R_i(1)&=(1-q)\int_0^1|-2+3s|\,ds
+q\int_0^1|-2+3(1+q^{-1})s|\,ds\\
&=(1-q)\frac56+q\left(\frac32(1+q^{-1})-2+\frac4{3(1+q^{-1})}\right)
=\frac{7+3q}{3(1+q)}.
\end{aligned}
\]
Since this decreases strictly with \(q\), the largest leaf rows are exactly those having \(q=q_*\). If \(d\ge2\), then every \(q<1\), and every leaf row exceeds \(5/3\). By convexity, each strict interior point has row norm below its leaf endpoint, proving the asserted maximizing set. If \(d=1\), the two endpoint norms both equal \(5/3\); the kernel signs at \(t=0\) and \(t=1\) disagree on a positive-measure interval, making the convexity inequality strict at every interior point.

At any maximizing exterior vertex \(i\), the real function
\[
f_j(s)=\begin{cases}
\operatorname{sgn}[-2+3(1+q_*^{-1})s],&j=i,\\
\operatorname{sgn}[-2+3s],&j\ne i,
\end{cases}
\]
with arbitrary values at the finitely many zeros has \(\|f\|_\infty=1\) and \((Pf)(i,1)=R_i(1)\). Thus the upper bound is attained. Symmetry of \(K\) with respect to \(\mu\) implies equality of the \(L^1\) and \(L^\infty\) norms.

Because \(P1=1\), each kernel row integrates to one. For data \(0\le f\le1\), the most negative output at a given point is the integral of the negative part of that row, of magnitude \((R_i(t)-1)/2\). Maximizing gives the claimed exact positivity defect. Finally \(q_*\le1/d\), with equality exactly for equal masses; differentiation of \((7+3q)/(3(1+q))\) gives \(-4/[3(1+q)^2]<0\). The mass-balancing optimum, strict threshold \(q_*<1/3\), and family-wide \(7/3\) envelope follow. The condition \(q_*\to0\) is possible only in a family of positive mass vectors, not at a permitted finite endpoint.

## Verification
The standalone file `verify_star.py` independently builds and rationally inverts nodal Gram matrices and integrates absolute affine kernel rows without using the closed-form inverse or closed-form leaf norm. Its recorded execution passed 27,416 exact-rational assertions on 382 positive-mass stars, including all Gram inverse identities, center and leaf values, strict interior comparisons, and global maxima. For equal edge masses, the predicted constants for degrees one through seven are \(5/3,17/9,2,31/15,19/9,15/7,13/6\). These finite checks independently test calculations; the preceding algebraic argument establishes the infinite family.

## Relationship to prior work
Classical linear-spline orthogonal projections on intervals have a mesh-independent upper bound of three; Kayumov discusses the sharp classical constant and its extension to differential-operator splines. Oswald proves that for general triangulated domains in Euclidean dimension at least two the analogous finite-element \(L^\infty\) norm is not uniformly bounded, while recalling the one-dimensional bound. Hangelbroek, Narcowich, Sun and Ward give general boundedness criteria for least-squares projections in spaces generated by positive-definite kernels on manifolds. These results do not state the exact arbitrary-edge-mass metric-star norm or its shortest-edge maximizing and balancing laws. The case of one or two edges is a low-complexity path specialization; the branching classification and mass-dependent formula encompass arbitrary finite star degree.

## Limitations
Only a single junction with no additional interior vertices is treated. The edge densities are positive and constant separately on each edge, though lengths and densities are arbitrary. Variable densities along individual edges, higher-degree splines, several junctions, boundary-constrained splines, and general graph topology are not classified. The input extremizers are measurable sign functions, not necessarily continuous. A historical treatment of very short interval partitions or of metric-star nodal projectors could contain a prior equivalent formula and is an unresolved publication-priority risk; this document does not assert independent external validation.

## References
- A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first posted 2004-08-30. https://arxiv.org/abs/math/0408418
- P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19. https://arxiv.org/abs/math/0611573
- T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424, first posted 2010-05-13. https://arxiv.org/abs/1005.2424
- C. de Boor, *A bound on the \(L^\infty\)-norm of \(L^2\)-approximation by splines in terms of a global mesh ratio*, Mathematics of Computation 30 (1976), 765–771, DOI:10.1090/S0025-5718-1976-0425432-1.
- I. Pesenson, *Polynomial splines and eigenvalue approximations on quantum graphs*, Journal of Approximation Theory 135 (2005), 203–220, DOI:10.1016/j.jat.2005.04.007.
