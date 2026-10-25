# Sharp quadratic spherical-lune concentration and its dimension-dependent optimizer transition

## Finding
Fix an integer \(n\ge3\) and unit vectors \(u,v\in\mathbb R^n\) with angle \(0<\theta<\pi\). Let \(W=\{x\in S^{n-1}:x\cdot u\ge0,\ x\cdot v\ge0\}\), and put \(L=\pi-\theta\), \(m=n-2\), and \(q=\sqrt{m/n}\). Let \(\mathcal H_2\) be the **complex** space of restrictions to the sphere of homogeneous harmonic quadratic polynomials. Write
\[
\mathcal C_{n,L}=\sup_{0\ne f\in\mathcal H_2}
\frac{\int_W|f|^2\,d\sigma}{\int_{S^{n-1}}|f|^2\,d\sigma},
\]
where \(\sigma\) is probability surface measure.

The sharp answer, attained for all \(n,L\), is
\[
\boxed{\mathcal C_{n,L}=\max\{\Lambda_+(n,L),\Lambda_\mathrm{mix}(L)\}},
\]
where
\[
\Lambda_+(n,L)=\frac{L+\frac12\sin L\cos L+\sin L\sqrt{\frac14\cos^2L+\frac{n-2}{n}}}{2\pi},
\qquad
\Lambda_\mathrm{mix}(L)=\frac{L+\sin L}{2\pi}.
\]
The optimizer changes precisely at \(L_c=\arccos(2/n)\): \(\Lambda_+>\Lambda_\mathrm{mix}\) for \(0<L<L_c\), equality holds only at \(L=L_c\), and \(\Lambda_+<\Lambda_\mathrm{mix}\) for \(L_c<L<\pi\). In particular the top eigenvalue has complex multiplicity \(1\), then \(n-1\) at the transition, then \(n-2\).

Here is the **entire concentration spectrum**, as a multiset. Besides \(\Lambda_+\), it contains
\[
\Lambda_- =\frac{L+\frac12\sin L\cos L-\sin L\sqrt{\frac14\cos^2L+\frac{n-2}{n}}}{2\pi},
\qquad \Lambda_s=\frac{L-\sin L\cos L}{2\pi},
\]
with multiplicity one each, the numbers \(\frac{L+\sin L}{2\pi}\) and \(\frac{L-\sin L}{2\pi}\) with multiplicity \(n-2\) each, and \(\frac{L}{2\pi}\) with multiplicity \(\frac12(n-2)(n-1)-1\). Multiplicities add when numerical levels coincide; the last multiplicity is zero at \(n=3\).

## Assumptions and scope
Use the orthonormal bisector frame \(e_1=(u+v)/\|u+v\|\), \(e_2=(u-v)/\|u-v\|\), extended by arbitrary orthonormal vectors in the \(n-2\) orthogonal directions. Write \(x=(x_1,x_2,z)\), \(z\in\mathbb R^m\), \(t=x_1^2+x_2^2\). In this frame the lune condition is \(-L/2\le\phi\le L/2\) for \((x_1,x_2)=\sqrt t(\cos\phi,\sin\phi)\). Boundary conventions do not change integrals.

For explicit equality cases define the spherical harmonics
\[
S(x)=t-\frac2n,\qquad C(x)=x_1^2-x_2^2,\qquad
w(n,L)=\frac{\cos L}{2}+\sqrt{\frac{\cos^2 L}{4}+\frac{n-2}{n}}.
\]
When \(L<L_c\), all nonzero equality functions are exactly complex multiples of \(S+w(n,L)C\). When \(L>L_c\), all nonzero equality functions are exactly \(x_1(b\cdot z)\) for arbitrary nonzero \(b\in\mathbb C^m\). When \(L=L_c\), equality holds exactly for the nonzero functions in the complex span of \(S+C=2(x_1^2-1/n)\) and the \(m\) functions \(x_1z_j\). In particular the transition creates an \((n-1)\)-dimensional top eigenspace.

The statements concern one exact harmonic degree only (no lower degrees), arbitrary complex coefficients, and the open angle range; no assertion is made about Dirichlet eigenvalues on the lune or higher-degree concentration.

## Proof
**1. Geometry and moment normalization.** For \(x\) uniform on the sphere, \(t\) has beta law \(\mathrm{Beta}(1,m/2)\), its angle \(\phi\) is independent and uniform on \([0,2\pi)\), and, conditional on \(t,\phi\), \(z=\sqrt{1-t}\,Z\), where \(Z\) is uniform on \(S^{m-1}\) (the symmetric two-point set when \(m=1\)). In particular
\[
\mathbb E t^2=\frac8{n(n+2)},\quad
\mathbb E[t(1-t)]=\frac{2m}{n(n+2)},\quad
\mathbb E(1-t)^2=\frac{m(m+2)}{n(n+2)}.
\]
The second and fourth moments of \(Z\) are \(\mathbb E Z_iZ_j=\delta_{ij}/m\) and
\[
\mathbb E Z_iZ_jZ_kZ_l=\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}}{m(m+2)}.
\]
These formulas are also valid at \(m=1\).

Every \(f\in\mathcal H_2\) has a unique representation \(f(x)=x^{\mathsf T}Ax\), for complex symmetric \(A\) with \(\operatorname{tr}A=0\). The full-sphere Hermitian norm is \(\|f\|_2^2=2\operatorname{tr}(AA^*)/[n(n+2)]\), so the localized quadratic form defines a Hermitian concentration operator on the traceless-symmetric matrices.

**2. Orthogonal invariant blocks.** Put \(U_0=S\), \(U_c=C\), \(U_s=2x_1x_2\), and write \(z=(z_1,\ldots,z_m)\). The following summands exhaust \(\mathcal H_2\):
\[
\operatorname{span}\{U_0,U_c\}\ \oplus\
\operatorname{span}\{U_s\}\ \oplus\
\operatorname{span}\{x_1z_j:1\le j\le m\}\ \oplus\
\operatorname{span}\{x_2z_j:1\le j\le m\}\ \oplus\
\{z^{\mathsf T}Bz:B=B^{\mathsf T},\operatorname{tr}B=0\}.
\]
They are orthogonal on the full sphere and invariant for concentration on \(W\): reflection in the \(e_2\) coordinate removes odd cross terms, while orthogonal invariance in \(z\) and the displayed spherical fourth-moment identity remove all other cross terms. The dimensions are \(2,1,m,m,\frac12m(m+1)-1\), totaling \(\dim\mathcal H_2=(n+2)(n-1)/2\).

Normalize \(U_0\) and \(U_c\) in full-sphere \(L^2\), whose squared norms are respectively \(4m/[n^2(n+2)]\) and \(4/[n(n+2)]\). Their \(2\times2\) localized Gram matrix is **exactly**
\[
K_0=\frac1{2\pi}\begin{pmatrix}
L&q\sin L\\ q\sin L&L+\sin L\cos L
\end{pmatrix}.
\]
This follows by integrating \(1\), \(\cos2\phi\), and \(\cos^2 2\phi\) over the aperture. Its two distinct eigenvalues are \(\Lambda_\pm\) as stated, since \(\sin L>0\).

Every other block is scalar: the \(U_s\) ratio is \((L-\sin L\cos L)/(2\pi)\), the \(x_1z_j\) ratio is \((L+\sin L)/(2\pi)\), the \(x_2z_j\) ratio is \((L-\sin L)/(2\pi)\), and a transverse traceless quadratic has ratio \(L/(2\pi)\). These follow from the integrals of \(\sin^2 2\phi\), \(\cos^2\phi\), \(\sin^2\phi\), and \(1\), respectively. This proves the full multiset and all its multiplicities.

**3. The sharp top branch and the transition.** Since \(0<L<\pi\), we have \(\sin L>0\). The mixed branch \(\Lambda_\mathrm{mix}\) strictly exceeds \(\Lambda_s\), \((L-\sin L)/(2\pi)\), and \(L/(2\pi)\); \(\Lambda_+>\Lambda_-\) also holds. Hence the maximum is precisely the larger of \(\Lambda_+\) and \(\Lambda_\mathrm{mix}\). Their difference is
\[
\Lambda_+-\Lambda_\mathrm{mix}
=\frac{\sin L}{2\pi}\left(w(n,L)-1\right).
\]
The positive number \(w=w(n,L)\) is the positive root of \(w^2-(\cos L)w-(n-2)/n=0\). The value of this polynomial at \(w=1\) equals \(2/n-\cos L\). Because the polynomial has exactly one positive root, \(w>1\), \(w=1\), or \(w<1\) according as \(\cos L>2/n\), \(=2/n\), or \(<2/n\). This proves the sharp, unique transition \(L_c=\arccos(2/n)\).

**4. Equality.** In the orthonormal \((U_0,U_c)\) basis, the \(\Lambda_+\) eigenvector has component ratio \(w/q\); returning to the unnormalized basis yields \(U_0+w U_c\). The strict comparisons above rule out all other top eigenspaces except when the two top branches coincide. The \(x_1z_j\) block is scalar, so every complex linear combination is an eigenfunction with eigenvalue \(\Lambda_\mathrm{mix}\). At equality of the two branches their direct sum is the top eigenspace; \(w=1\), and \(U_0+U_c=2(x_1^2-1/n)\). This exhausts all cases for complex coefficients and completes the proof.

## Verification
The standalone `wedge_spectral_checker.py` builds an orthonormal basis of all complexified traceless-symmetric quadratics and **independently** forms the full concentration Gram matrix from beta and transverse-sphere fourth moments, followed by 64-node Gauss–Legendre quadrature in the angular variable. For dimensions \(n=3,4,5,8\) and eight aperture choices each, including the predicted crossing, it compares every sorted eigenvalue with the stated spectrum, verifies the trace and transition signs, and checks the Rayleigh quotients of both claimed equality branches. The included output records 192 successful assertions. This is a reproducible finite cross-check of the exact integral formulas; the proof above, not finite quadrature, supplies the all-dimension theorem.

## Relationship to prior work
Simons, Dahlen, and Wieczorek gave the general spherical Slepian concentration matrix and the polar-cap reduction. Michel, Plattner, and Seibert developed the general spin-weighted construction and commuting operators for caps. Seto, Wei, and Zhu studied a different Dirichlet-Laplacian eigenvalue problem on spherical lunes. Those works motivate the same geometry and Slepian framework, but neither the exact all-dimensional degree-two wedge spectrum nor the dimension-dependent optimizer-switch formula above is stated in the portions inspected. The general Slepian matrix framework is acknowledged as antecedent; the result here is its **explicit sharp evaluation and optimizer classification** for a non-axisymmetric domain, not a claim to invent concentration operators.

## Limitations
The analysis concerns homogeneous degree-two spherical harmonics only and open dihedral angles. The numerical verification uses finitely many dimensions and apertures; it is not a proof of any untested parameter case. Prior-art searches cannot exclude independently derived equivalent formulas in older or unindexed literature; the claim of originality is best-knowledge and has no independent audit. The theorem does not address optimal shapes among arbitrary regions, higher degrees, or the Dirichlet spectral gap on lunes.

## References
1. S. Seto, G. Wei, X. Zhu, *Fundamental gaps of spherical triangles*, arXiv:2009.00229, first posted 2020-09-01. Section 2 treats lunes for the Dirichlet Laplacian.
2. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted 2021-03-26. Sections 3 and 4 develop the Slepian matrix approach and cap operators.
3. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, first posted 2004-08-31, subsequently SIAM Review 48 (2006), 504–536. Sections 4–5 and Appendix A develop general regional matrices and cap localization.
