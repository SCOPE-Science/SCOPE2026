# A sharp sign transition for orthogonal random widths of rectangular boxes

## Finding
For a rectangular box with positive side lengths \(a,b,c\), choose a Haar-uniform ordered orthonormal pair \((U,V)\) in \(\mathbb R^3\). Denote its directional width by \(W(u)\), and put
\[
S=a+b+c,\quad Q=a^2+b^2+c^2,\quad
A=\frac{2}{3\pi}-\frac14,\quad B=\frac{8}{3\pi^2}-\frac14.
\]
Then
\[
\boxed{\operatorname{Cov}(W(U),W(V))=BS^2+(A-B)Q.}
\tag{1}
\]
In particular, writing
\[
\tau=\frac{32-3\pi^2}{8(4-\pi)}=0.348201061933\ldots,
\qquad\frac13<\tau<1,
\]
the covariance is **positive, zero, or negative if and only if** \(Q/S^2\) is respectively below, equal to, or above \(\tau\). All three possibilities occur among strictly positive boxes.

For any fixed sum of side lengths \(S>0\), the covariance is uniquely maximized by the cube, with the strictly positive value
\[
\boxed{\max\operatorname{Cov}(W(U),W(V))=
\frac{S^2}{9}\left(\frac2\pi+\frac{16}{\pi^2}-\frac94\right)>0.}
\tag{2}
\]
Its sharp infimum over positive boxes of the same \(S\) is the negative number
\[
\boxed{\inf\operatorname{Cov}(W(U),W(V))=S^2\left(\frac{2}{3\pi}-\frac14\right),}
\tag{3}
\]
not attained because all three side lengths must remain positive. The infimum is approached by rod-like limits. Equations (1)–(3) determine the full covariance range by continuity.

## Assumptions and scope
The box is a nondegenerate Euclidean orthotope in three dimensions; its location and choice of coordinate signs are irrelevant. Width is the separation of two supporting planes perpendicular to the indicated unit vector. The ordered pair \((U,V)\) is sampled using Haar probability on the Stiefel manifold of orthonormal two-frames: \(U\) is uniform on the sphere, and conditional on \(U\), \(V\) is uniform on the unit circle in \(U^\perp\). Choosing two **independent** directions would give zero covariance, so that different coupling is excluded. No claim is made for arbitrary orientations of parallelepiped edge vectors, higher-dimensional boxes, or the full bivariate width distribution.

## Proof
**1. Projection identity and conditional Haar averaging.** For \(u=(u_1,u_2,u_3)\) on the unit sphere,
\[
W(u)=a|u_1|+b|u_2|+c|u_3|.
\tag{4}
\]
Every coordinate of uniform \(U\) is uniformly distributed on \([-1,1]\), so \(\mathbb E|U_i|=1/2\) and \(\mathbb EW(U)=S/2\). Conditional on \(U\), the \(j\)-th coordinate of uniformly circular \(V\in U^\perp\) has the form \(\sqrt{1-U_j^2}\cos\Theta\) for uniform \(\Theta\in[0,2\pi)\), up to a phase shift. Therefore
\[
\mathbb E(|V_j|\mid U)=\frac2\pi\sqrt{1-U_j^2}.
\tag{5}
\]
**2. The two distinct matrix coefficients.** By symmetry, the expectation \(\mathbb E|U_iV_j|\) depends only on whether the two indices coincide. For \(i=j\), using (5) and the uniform coordinate marginal,
\[
\mathbb E|U_iV_i|=\frac2\pi\int_0^1t\sqrt{1-t^2}\,dt
=\frac{2}{3\pi}.
\tag{6}
\]
For \(i\ne j\), condition on \(U_j=t\). The two remaining coordinates have a uniform angular distribution on the circle of radius \(\sqrt{1-t^2}\). Hence
\[
\mathbb E(|U_i|\mid U_j=t)=\frac2\pi\sqrt{1-t^2},
\]
and, by (5),
\[
\mathbb E|U_iV_j|
=\frac4{\pi^2}\cdot\frac12\int_{-1}^{1}(1-t^2)\,dt
=\frac{8}{3\pi^2}.
\tag{7}
\]
**3. Exact covariance and sign classification.** Expanding (4) at \(U\) and \(V\) and using (6)–(7) yields
\[
\mathbb E[W(U)W(V)]=\frac{2Q}{3\pi}
+\frac{8(S^2-Q)}{3\pi^2}.
\]
Subtracting the product of the means, \(S^2/4\), gives (1). The exact coefficient inequalities \(A<0<B\) follow from \(3<\pi<22/7\): indeed \(\pi>8/3\), while \(\pi^2<(22/7)^2<32/3\). Also
\[
A-B=\frac{2(\pi-4)}{3\pi^2}<0.
\]
Thus (1) is strictly decreasing as \(Q\) increases at fixed \(S\), and its unique zero occurs at \(Q/S^2=-B/(A-B)=\tau\). Cauchy–Schwarz gives \(Q\ge S^2/3\), with equality only for a cube, and positivity of all three lengths yields \(Q<S^2\); any ratio between these endpoints is achieved along \((a,b,c)\propto(1,t,t)\), \(0<t\le1\).

At the cube, direct substitution gives (2). To check its strict positivity without relying on decimals, note that the function \(f(x)=2/x+16/x^2-9/4\) decreases for \(x>0\), and \(f(22/7)=3/484>0\). Since \(\pi<22/7\), \(f(\pi)>0\), proving \(\tau>1/3\). At the rod limit, (1) tends to \(AS^2<0\), proving \(\tau<1\). Because \(A-B<0\), the cube uniquely maximizes (1) and the rod value is its sharp unattained infimum. Connectedness of the positive side-length simplex gives the entire interval of intermediate values. No probabilistic independence of the two widths was assumed.

## Verification
Running the standalone `verify_orthogonal_widths.py` with Python, NumPy, SciPy and SymPy verifies the symbolic covariance and threshold identities; numerically reconstructs the two pairwise Haar coefficients by independent spherical quadrature; checks five noncongruent three-dimensional boxes including the cube and elongated examples; and checks the sharp extrema and rod-limit sequences. The checker reports its pass status and diagnostic constants. Spherical quadrature is numerical corroboration with stated tolerances, **not** a proof for all real side lengths. The universal proof is equations (4)–(7) plus the elementary normalization inequalities above.

## Relationship to prior work
Finch, *Width Distributions for Convex Regular Polyhedra* (first public arXiv 2011), evaluates one-direction moments of the regular cube and tetrahedron, including the mean squared width. Kabluchko, Litvak and Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables* (2015 preprint), develop one-direction cube projection moments in all dimensions. Neither inspected primary text states this **mixed-width covariance in a common orthonormal frame**, which is not recoverable merely from a single-direction marginal law.

The publicly available works *Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes*, *Haar-random planar projection perimeter moments of all orthotopes*, and *All-dimensional area–perimeter covariance of random orthotope shadows* describe other couplings and observables: respectively width versus projected facet brightness at one shared normal, perimeter of an integrated two-plane shadow, and area–perimeter covariance of a projected planar body. Their displayed theorems and proofs do not assert (1) or its sharp shape sign threshold. In particular, an averaged perimeter-square moment does not determine the width-pair correlation at exactly a right angle without additional angle-resolved information. This is a statement-level comparison, not a proof of exhaustive historical priority.

## Limitations
The signs classify covariance, **not independence** of the two widths or ordering of their full joint distributions. The conclusion is specific to three-dimensional orthogonal boxes. The marginal-width formula and spherical-coordinate integrals are classical; the claimed contribution is their combined orthogonal-frame covariance and complete signed shape classification. Additional specialized stereological literature could contain an equivalent mixed-moment evaluation. The automated checker and literature search do not constitute independent validation or a claim of worldwide priority.

## References
1. Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public 2011-10-04. https://arxiv.org/abs/1110.0671 .
2. Zakhar Kabluchko, Alexander E. Litvak, Dmitry Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479 (2015). https://arxiv.org/abs/1511.08479 .
3. *Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes*, publicly available research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-aspect-ratio-phase-diagram-for-width-brightness-covariance--ef50d44d3e36 .
4. *Haar-random planar projection perimeter moments of all orthotopes*, publicly available research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-haar-random-planar-projection-perimeter-moments-of-all-orthotope--5f6a2c7bb90c .
5. *All-dimensional area–perimeter covariance of random orthotope shadows*, publicly available research result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-all-dimensional-area-perimeter-covariance-of-random-orthotope-sh--357f1ce92466 .
