# The incircle is the unique maximal numerical range of a two-dimensional compression of a three-point normal operator

## Finding
Let \(N\) be a bounded normal operator on a complex Hilbert space \(H\) of dimension at least two. If the spectrum has at most three points, define its **elliptical width** by
\[
\delta_2(N)=\sup_{\dim S=2}\delta(W(N_S)),\qquad N_S=P_SN|_S,
\]
where \(W(B)=\{\langle u,Bu\rangle:\|u\|=1\}\) and \(\delta(K)\) is the diameter of a largest closed Euclidean disk contained in the compact convex set \(K\). In particular, the diameter of any disk of radius zero is zero.

**Theorem.** Suppose \(\sigma(N)=\{z_1,z_2,z_3\}\), and the spectral points are noncollinear. Put \(T=\operatorname{conv}\{z_1,z_2,z_3\}\), let \(A>0\) denote its Euclidean area, let \(P=|z_1-z_2|+|z_2-z_3|+|z_3-z_1|\), and write \(c\) and \(r=2A/P\) for the incenter and inradius. Then
\[
\boxed{\delta_2(N)=2r=\frac{4A}{P}.}
\]
There is a two-dimensional subspace \(S\subset H\) with \(W(N_S)=\{w:|w-c|\le r\}\). Moreover, **every** two-dimensional compression attaining \(\delta_2(N)\) has numerical range equal to this same disk; in particular, the maximizing numerical-range *set* is unique even when maximizing subspaces are not.

In the diagonal model \(N=\operatorname{diag}(z_1,z_2,z_3)\), set
\[
 p_i=\frac{(z_i-c)^2}{(z_i-z_j)(z_i-z_k)}\quad(\{i,j,k\}=\{1,2,3\}),
 \qquad n=(\sqrt{p_1},\sqrt{p_2},\sqrt{p_3}).
\]
These numbers are positive real, sum to one, and \(S=n^\perp\) gives the claimed incircle. For a normal operator with arbitrary nonzero multiplicities of the three spectral projections, choose one unit eigenvector from each projection and apply the same construction on their three-dimensional span.

If \(\sigma(N)\) is collinear (including a one- or two-point spectrum), then \(\delta_2(N)=0\).

For a finite-dimensional \(N\in\mathbb M_d(\mathbb C)\), define
\[
 \Phi(N)=\sup\left\{\left\|\begin{pmatrix}B&N\\N^*&C\end{pmatrix}\right\|-\|B+C\|:\begin{pmatrix}B&N\\N^*&C\end{pmatrix}\succeq0,\quad B,C\in\mathbb M_d(\mathbb C)\right\}.
\]
Sababheh's previously established identity \(\Phi(X)=\delta_2(X)\) immediately makes the new explicit computation an exact positive-block norm-defect formula \(\Phi(N)=4A/P\) in the noncollinear three-point case (and \(\Phi(N)=0\) in the collinear case).

## Assumptions and scope
The operator is bounded, complex-linear, and normal, with no more than three **distinct** spectral points. Multiplicities, Hilbert-space dimension, and the moduli of the spectral values are unrestricted. The first claim concerns two-dimensional compressions, not compressions of other ranks. The positive-block consequence is asserted only in finite dimension, the setting of the cited extremal theorem. Euclidean area and perimeter use the complex plane's ordinary Euclidean metric.

## Proof
**1. Upper bound.** By the spectral theorem, \(W(N)\subseteq T\) when \(N\) has three distinct spectral points (indeed \(W(N)=T\) for a finite-point normal spectrum). Each compression has \(W(N_S)\subseteq W(N)\subseteq T\). The largest disk inside the triangle has radius \(r=2A/P\), hence \(\delta_2(N)\le2r\). If the spectrum is collinear, every compressed numerical range lies in a line, so its inradius is zero.

**2. An explicit incenter compression.** Work first with \(D=\operatorname{diag}(z_1,z_2,z_3)\). The incenter \(c\) lies on each internal angle bisector. Thus the two vectors \(z_i-z_j\) and \(z_i-z_k\) have arguments symmetric about \(z_i-c\); their product has the same argument as \((z_i-c)^2\). Therefore \(p_i=(z_i-c)^2/[(z_i-z_j)(z_i-z_k)]\) is a *strictly positive real number*. The Lagrange interpolation identity
\[
\sum_{i=1}^3\frac{(z_i-c)^2}{(z_i-z_j)(z_i-z_k)}\prod_{\ell\ne i}(w-z_\ell)=(w-c)^2
\]
holds because both sides have degree at most two and agree at all three distinct values \(w=z_i\). Comparing coefficients of \(w^2\) gives \(p_1+p_2+p_3=1\).

Let \(n=(\sqrt{p_1},\sqrt{p_2},\sqrt{p_3})\) and \(S=n^\perp\). A determinant cofactor expansion relative to \(n\oplus S\) gives
\[
\det(wI_S-D_S)=\langle n,\operatorname{adj}(wI_3-D)n\rangle=\sum_i p_i\prod_{\ell\ne i}(w-z_\ell)=(w-c)^2.
\]
Thus \(D_S\) is a \(2\times2\) matrix with both eigenvalues equal to \(c\). By Schur triangularization it is unitarily similar to \(\begin{psmallmatrix}c&h\\0&c\end{psmallmatrix}\), whose numerical range is a **closed disk centered at \(c\)**, of radius \(|h|/2\); the disk may a priori be degenerate.

For each pair \(i\ne j\), the vector \(v_{ij}=\sqrt{p_j}\,e_i-\sqrt{p_i}\,e_j\) belongs to \(S\) and satisfies
\[
 \frac{\langle v_{ij},Dv_{ij}\rangle}{\|v_{ij}\|^2}=
 \frac{p_jz_i+p_i z_j}{p_i+p_j}\in[z_i,z_j].
\]
Consequently the centered disk \(W(D_S)\) meets **each of the three side lines** of \(T\), and is contained in \(T\). Since every side line is at distance exactly \(r\) from \(c\), containment gives radius at most \(r\), while meeting any side line gives radius at least \(r\). Therefore \(W(D_S)=\overline{B(c,r)}\). This proves attainability and \(\delta_2(D)=2r\).

For arbitrary multiplicity and infinite-dimensional \(H\), each of the three nonzero spectral projections contains a unit eigenvector. Their orthogonal span reduces \(N\) to \(D\), and the same plane \(S\) inside that span has the required compression. The upper bound from Step 1 still applies.

**3. Uniqueness of the maximizing numerical-range set.** If another two-dimensional compression \(C=N_E\) attains \(\delta(W(C))=2r\), its elliptical numerical range \(F=W(C)\) contains a disk of radius \(r\) lying in \(T\). The triangle's largest inscribed disk is unique: it is precisely \(D_r=\overline{B(c,r)}\). Thus \(D_r\subseteq F\subseteq T\). Since \(r>0\), \(F\) is a full-dimensional elliptical disk; write \(F=\{x\in\mathbb R^2:q(x)\le0\}\) for a nondegenerate real quadratic polynomial \(q\). The function \(\theta\mapsto-q(c+r(\cos\theta,\sin\theta))\) is a nonnegative trigonometric polynomial of degree at most two. At the three distinct tangency points where \(D_r\) meets the sides of \(T\), it vanishes: those points lie on the boundary of \(F\) because \(F\subseteq T\). Each of these three zeros has even multiplicity. A nonzero trigonometric polynomial of degree at most two has at most four zeros counted with multiplicity on a full period (multiply by \(e^{2i\theta}\) and apply the polynomial root bound). Hence this function vanishes identically. The entire circle \(\partial D_r\) lies in \(\partial F\), so the two filled ellipses coincide, \(F=D_r\).

For \(3\times3\) diagonal \(D\), a maximizing plane \(n^\perp\) must therefore have the repeated compressed eigenvalue \(c\). The same cofactor identity, evaluated at each \(z_i\), forces \(|n_i|^2=p_i\). Only arbitrary diagonal phases of the normal vector remain. This gives the promised explicit and, up to coordinate phases, unique optimizing plane in dimension three.

**4. Block-norm consequence.** For finite matrices only, apply \(\Phi(X)=\delta_2(X)\), proved in Sababheh's Theorem 3.2, to the value from Steps 1–2. No claim is made here that the optimizing positive blocks attain their supremum at finite values of the lifting parameter.

## Verification
An exact symbolic diagnostic takes the right triangle with vertices \(0,3,4i\), center \(c=1+i\), radius \(r=1\), and weights \(p=(1/6,1/3,1/2)\). It confirms the polynomial identity
\[
 \frac16(w-3)(w-4i)+\frac13w(w-4i)+\frac12w(w-3)=(w-1-i)^2.
\]
The standalone `verify_incircle.py` checks this identity with exact rational arithmetic and verifies the compression eigenvalues, nilpotence, and disk radii in five additional explicit triangles using finite-precision linear algebra. It prints `INCIRCLE_COMPRESSION_EXACT_AND_FINITE_OK`. These computations supplement, and do not establish, the universal analytic theorem. Reproduction: `python verify_incircle.py` with Python 3, NumPy, SciPy and SymPy.

## Relationship to prior work
Sababheh, *An Extremal Formula for Elliptical Width and the Bourin–Lee Conjecture* (arXiv:2610.04377v1, publicly posted 2026-10-03), proves the general identity \(\Phi(X)=\delta_2(X)\) and works out a specially symmetric \(3\times3\) normal example to establish a radius bound. That identity and example are **not** claimed as new. The new exact statement computes \(\delta_2(N)\) from the **arbitrary** spectral triangle, supplies a constructive incircle compression, and classifies all maximal compression numerical-range sets.

Adam and Maroulas (2002) establish the general tangency of a normal compression to the sides of its spectral polygon; this is closely related and is expressly credited, but their tangency assertion alone does not compute the optimizing largest inscribed disk or its unique circular realization. Gau and Wu's studies of normal compressions (2004), and Adam's further inverse-configuration work (2011), are relevant context; implicit coverage by more general Poncelet/inellipse theory remains a literature risk. Bourin and Lee (2022) introduced the positive-block inequalities and the elliptical-width correction, but their results do not give this triangle-resolved equality.

## Limitations
This calculation is confined to operators with at most three spectral points. It does not determine the elliptical width of arbitrary normal operators with more spectral points, nor any fixed-block higher-eigenvalue defect. The closed-disk and numerical-range-set uniqueness proof assumes a nondegenerate spectral triangle; collinear spectra give only the zero-width assertion. The exact norm-defect identity in the block consequence is borrowed from the cited 2026 source and is used only in finite dimensions. The construction is self-contained, but priority is subject to fuller historical comparison, especially with the inaccessible 2004 predecessor on normal compressions and classical inverse inellipse theorems.

## References
1. M. Sababheh, *An Extremal Formula for Elliptical Width and the Bourin–Lee Conjecture*, arXiv:2610.04377v1 (2026), https://arxiv.org/abs/2610.04377.
2. M. Adam and J. Maroulas, *On compressions of normal matrices*, Linear Algebra Appl. **341** (2002), 403–418, doi:10.1016/S0024-3795(01)00505-5.
3. H.-L. Gau and P.-Y. Wu, *Numerical range of a normal compression*, Linear Multilinear Algebra **52** (2004), 195–201, doi:10.1080/0308108031000123659.
4. H.-L. Gau and P.-Y. Wu, *Numerical range of a normal compression II*, Linear Algebra Appl. **390** (2004), 121–136, doi:10.1016/j.laa.2004.04.013.
5. M. Adam, *On numerical ranges of the compressions of normal matrices*, Appl. Math. Comput. **217** (2011), 4699–4709, doi:10.1016/j.amc.2010.11.023.
6. J.-C. Bourin and E.-Y. Lee, *Eigenvalue inequalities for positive block matrices with the inradius of the numerical range*, Internat. J. Math. **33** (2022), 2250009, arXiv:2111.15180.
