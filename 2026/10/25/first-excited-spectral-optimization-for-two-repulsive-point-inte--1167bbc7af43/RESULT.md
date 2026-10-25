# First-excited spectral optimization for two repulsive point interactions on a circle

## Finding

Let \(\mathbb T_L=\mathbb R/L\mathbb Z\), with \(L>0\), and consider the periodic Schrödinger operator
\[
H_{\alpha,d}=-\frac{d^2}{dx^2}+\alpha(\delta_0+\delta_d),\qquad \alpha>0,\quad 0<d<L.
\]
The lower branch emerging from the free double eigenvalue \(k_1^2=(2\pi/L)^2\) has expansion, for each fixed \(d\),
\[
\lambda_{\mathrm{low}}(\alpha,d)=k_1^2+\frac{2\alpha}{L}\left(1-\left|\cos\frac{2\pi d}{L}\right|\right)+O_d(\alpha^2),\qquad \alpha\downarrow0.
\]
Its first-order coefficient is maximized exactly at \(d=L/4\) and \(d=3L/4\). In the strong-coupling limit \(\alpha\to\infty\), the first excited eigenvalue converges, for each fixed \(d\), to the second eigenvalue of the union of Dirichlet interval spectra on lengths \(d\) and \(L-d\). The maximum of that limiting eigenvalue is \(9\pi^2/L^2\), attained exactly at \(d=L/3\) and \(d=2L/3\).

Thus the two asymptotic spectral-design problems select different spacings: quarter spacing for the weak-coupling linear response, and one-third spacing in the Dirichlet-decoupling limit. This is a statement about the two asymptotic objectives, not a claim about the exact maximizing separation at finite \(\alpha\).

## Assumptions and scope

The circle has circumference \(L\); the two point interactions have equal repulsive strength \(\alpha\). The quadratic form is
\[
q_{\alpha,d}[u]=\int_0^L |u'(x)|^2\,dx+\alpha\bigl(|u(0)|^2+|u(d)|^2\bigr)
\]
on periodic \(H^1(0,L)\). Eigenvalues are ordered with multiplicity. The weak-coupling expansion is pointwise for each fixed \(d\), and its remainder is written \(O_d(\alpha^2)\); no uniform remainder in \(d\) is claimed. The strong-coupling statement is also pointwise in fixed \(d\in(0,L)\). No assertion is made about the exact optimizer for finite positive coupling.

## Proof

**Weak coupling.**

At \(\alpha=0\), the eigenvalue \(k_1^2\), where \(k_1=2\pi/L\), has normalized eigenspace basis \(\phi_\pm(x)=L^{-1/2}e^{\pm i k_1x}\). The restriction of the point-interaction form perturbation to this eigenspace is represented by
\[
\frac1L\begin{pmatrix}
2 & 1+e^{-2ik_1d}\\
1+e^{2ik_1d} & 2
\end{pmatrix}.
\]
Its eigenvalues are \(\frac1L(2\pm|1+e^{2ik_1d}|)=\frac2L(1\pm|\cos(k_1d)|)\). First-order degenerate perturbation theory therefore gives the two branches
\[
 k_1^2+\frac{2\alpha}{L}\left(1\pm\left|\cos\frac{2\pi d}{L}\right|\right)+O_d(\alpha^2).
\]
The lower branch has the coefficient stated above. Since \(0\le |\cos(2\pi d/L)|\le1\), its coefficient is largest precisely when \(\cos(2\pi d/L)=0\), namely at \(d=L/4\) or \(3L/4\) modulo \(L\).

As a useful boundary check, when \(d=L/2\), the function \(u(x)=\sin(2\pi x/L)\) vanishes at both interaction points. It therefore satisfies the derivative-jump conditions for every \(\alpha>0\), and \(k_1^2\) remains an exact eigenvalue. This is consistent with the zero first-order shift of the lower branch at equal spacing.

**Strong coupling.**

As \(\alpha\to\infty\), bounded form energy forces \(u(0)=u(d)=0\). The monotone form limit is the direct sum of Dirichlet Laplacians on intervals of lengths \(d\) and \(L-d\); on the compact circle, the ordered eigenvalues converge to the ordered union of these interval spectra.

By the symmetry \(d\leftrightarrow L-d\), it suffices to take \(0<d\le L/2\), so \(L-d\) is the longer interval. The lowest limiting eigenvalue is \((\pi/(L-d))^2\), and the second is
\[
\lambda_1^{\infty}(d)=\min\left\{\left(\frac{2\pi}{L-d}\right)^2,\left(\frac{\pi}{d}\right)^2\right\}.
\]
The first term increases with \(d\) and the second decreases. Their intersection satisfies \(2/(L-d)=1/d\), hence \(d=L/3\), where both terms equal \(9\pi^2/L^2\). This is the unique maximizer on \((0,L/2]\); symmetry gives the other maximizer \(2L/3\).

## Verification

The weak-coupling matrix is explicitly Hermitian; its two eigenvalues follow from the modulus of the off-diagonal entry. The optimization uses only the range of the cosine. The strong-coupling spectrum is the union of the elementary Dirichlet spectra \((n\pi/d)^2\) and \((m\pi/(L-d))^2\), and the maximum follows by intersecting one increasing and one decreasing function. No numerical search or finite enumeration is used. The limits and the absence of a finite-coupling optimizer claim are part of the statement.

## Relationship to prior work

Exner's 2019 paper on finite families of point interactions on a circle or sphere studies optimization of the principal (ground-state) eigenvalue. The present statement concerns the lower branch of the first nonzero free double eigenvalue and its strong-coupling Dirichlet limit; the ground-state objective does not by itself imply either spacing result. A separate registry search found a related ground-state maximization claim but no direct match for this excited-state asymptotic comparison. The full text of the closest primary paper was not retrieved, so related calculations in its body cannot be ruled out conclusively.

## Limitations

The weak-coupling remainder is pointwise in the separation; uniformity in \(d\) and convergence of finite-coupling maximizers are not established. The strong-coupling optimization is for the limiting Dirichlet-decoupled spectrum, not for every finite \(\alpha\). The claim is specific to two equal repulsive point interactions on a circle and does not classify larger interaction families or other boundary conditions.

## References

1. P. Exner, “An optimization problem for finite point interaction families,” arXiv:1906.01229 (first publicly posted 2019-06-04). The accessible abstract describes ground-state optimization on a circle or sphere.
