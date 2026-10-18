# Sharp two-mode stability for rotational symmetries of planar projections

## Finding
For a continuous, real-valued function \(f\) on the unit sphere \(S^2\), define its order-\(j\) oriented great-circle Fourier measurement by
\[
\mathcal T_j f(R)=\frac1{2\pi}\int_0^{2\pi}f\bigl(R(\cos t,\sin t,0)\bigr)e^{-ijt}\,dt,
\qquad R\in SO(3),\quad j\in\{2,3\}.
\]
Give \(SO(3)\) probability Haar measure and give \(S^2\) its usual surface-area measure of total mass \(4\pi\). Let \(\Pi_\ell\) be the orthogonal projection onto spherical harmonics of degree \(\ell\), with \(L^2(S^2)\) norm taken in this surface-area measure. Then the following two-sided estimate holds with **both constants optimal**:
\[
\boxed{\frac1{2\pi^2}\sum_{\ell\ge2}\frac{\|\Pi_\ell f\|_2^2}{\ell+1/2}
\ \le\ \int_{SO(3)}\bigl(|\mathcal T_2f(R)|^2+|\mathcal T_3f(R)|^2\bigr)\,dR
\ \le\ \frac{35}{128\pi}\sum_{\ell\ge2}\frac{\|\Pi_\ell f\|_2^2}{\ell+1/2}.}
\]
The upper equality holds precisely when the spherical-harmonic components of degree at least two lie entirely in degree three. The lower bound is strict unless all components of degree at least two vanish, but its constant is approached by single harmonics of arbitrarily large degree. In particular, the measurements determine \(f\) modulo constant and linear functions, and the loss of one-half Sobolev derivative is optimal.

These sharp constants remain optimal **within the support functions of smooth, strictly convex bodies in \(\mathbb R^3\)**. Thus approximate vanishing of the second and third Fourier coefficients of all planar projections quantitatively controls the support function's distance, modulo ball radius and translation, in the explicitly specified negative half-order Sobolev norm.

## Assumptions and scope
The continuous-function statement applies, by density, to arbitrary real or complex \(L^2(S^2)\) functions, defining circle traces for almost every orientation. Set
\[
\|f\|_{*, -1/2}^2=\sum_{\ell\ge2}(\ell+1/2)^{-1}\|\Pi_\ell f\|_2^2.
\]
This is a norm on the quotient by constants and linear functions, equivalent to the usual \(H^{-1/2}(S^2)\) quotient norm; the *specific shifted Laplacian normalization* is necessary for the displayed sharp constants. There are no smoothness, central-symmetry or curvature assumptions in the analytic inequality. In the convex-geometric application, \(f=h_K\) is a support function, and every great-circle restriction equals the support function of the corresponding orthogonal planar projection. Translation adds only first Fourier harmonics; balls add only the zeroth harmonic.

## Proof
**Step 1: Exact singular spectrum.** Choose the standard orthonormal complex spherical harmonics \(Y_{\ell m}\), normalized for surface-area measure. On the reference equator the Fourier coefficient of order \(j\ge0\) of \(Y_{\ell m}\) vanishes unless \(m=j\), in which case it equals
\[
A_{\ell j}=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-j)!}{(\ell+j)!}}\,P_\ell^j(0).
\]
Schur orthogonality of the matrix coefficients of the irreducible degree-\(\ell\) rotation representation yields, including vanishing cross terms for distinct degrees,
\[
\int_{SO(3)}|\mathcal T_j f(R)|^2\,dR
=\sum_{\ell\ge j}\lambda_{\ell j}\|\Pi_\ell f\|_2^2,
\qquad \lambda_{\ell j}=\frac{|A_{\ell j}|^2}{2\ell+1}.
\]
For opposite parity the coefficient is zero. For \(\ell-j\) even, the associated Legendre identity
\[
P_\ell^j(0)=(-1)^{(\ell+j)/2}\frac{(\ell+j-1)!!}{(\ell-j)!!}
\]
gives, on setting \(c_k=4^{-k}\binom{2k}{k}\),
\[
\lambda_{\ell j}=\frac1{4\pi}
 c_{(\ell-j)/2}\,c_{(\ell+j)/2}.
\]
For every even \(\ell\ge2\), exactly \(j=2\) contributes to the sum of the two measurements; for every odd \(\ell\ge3\), exactly \(j=3\) contributes. Degrees zero and one are in the joint kernel. These identities first hold for spherical polynomials. Fubini's theorem and density extend them to all \(L^2\) inputs.

**Step 2: Exact infinite-degree optimization.** For fixed \(j=2\) or \(3\) and admissible \(\ell\), put \(s_{\ell j}=(\ell+1/2)\lambda_{\ell j}\). The central-binomial recurrence \(c_{k+1}/c_k=(2k+1)/(2k+2)\) implies
\[
\frac{s_{\ell+2,j}}{s_{\ell j}}
=\frac{(2\ell+5)(\ell-j+1)(\ell+j+1)}
{(2\ell+1)(\ell-j+2)(\ell+j+2)}<1.
\]
Indeed the denominator minus numerator, after cross multiplication, is exactly \(4j^2-1>0\). Stirling's formula gives \(c_k\sim(\pi k)^{-1/2}\), hence
\[
\lim_{\ell\to\infty,\ \ell\equiv j\ (\mathrm{mod}\ 2)}s_{\ell j}=\frac1{2\pi^2}.
\]
The two possible maxima occur at \(\ell=2,j=2\) and \(\ell=3,j=3\):
\[
s_{2,2}=\frac{15}{64\pi},\qquad
s_{3,3}=\frac{35}{128\pi}>s_{2,2}.
\]
Applying these optimal bounds termwise in the exact spectral identity proves the claim and its equality conditions. Single degree-three harmonics attain the upper constant. Single harmonics with degrees tending to infinity approach the lower constant but never attain it nontrivially.

**Step 3: Geometric sharpness and derivative loss.** If \(Y\) is any real spherical harmonic and \(r>0\), then \(h(u)=r+\varepsilon Y(u)\) has positive-definite spherical support Hessian \(\nabla_S^2h+h\,\mathrm{Id}\) for sufficiently small nonzero \(\varepsilon\), so it is the support function of a smooth strictly convex body. Its two measurement energies and quotient Sobolev norm both scale as \(\varepsilon^2\); their ratio is the corresponding spectral ratio. Therefore the extremizing and asymptotically extremizing examples can be chosen as genuine smooth strictly convex bodies. Since the high-degree energy multiplier is asymptotic to a positive multiple of \(\ell^{-1}\), no uniform lower estimate in the stronger \(H^{-s}\) quotient norm can hold for \(s<1/2\), even for smooth strictly convex support functions; rescaled high-degree harmonic perturbations disprove it.

## Verification
The standalone script `check_frame.py` uses only the Python standard library. It tests exactly, with rational arithmetic, the two lowest-degree multipliers and the strict monotonic ratio in 998 admissible degree steps; it also integrates the explicit zonal \(Y_{20}\) and \(Y_{30}\) moment formulas and checks the large-degree asymptotics by log-gamma evaluation. The 2006 reported checks passed. The infinite-degree theorem follows from the analytic identities and Stirling asymptotics above, **not** from the finite loop.

For an independent normalization cross-check, \(Y_{20}(u)=\sqrt{5/(16\pi)}(3u_3^2-1)\) has measurement energy \(3/(32\pi)\), whereas \(Y_{30}(u)=\sqrt{7/(16\pi)}(5u_3^3-3u_3)\) has energy \(5/(64\pi)\). Both can be obtained directly from \(\mathbb E[(1-C^2)^2]=8/15\) and \(\mathbb E[(1-C^2)^3]=16/35\) for \(C\) uniform on \([-1,1]\).

## Relationship to prior work
Myroshnychenko, Ryabogin and Saroglou (arXiv:2609.27192, first public 2026-09-23), Theorem 1.4, prove the qualitative statement that simultaneous vanishing of great-circle Fourier modes two and three forces a continuous function to be constant plus linear. Their Lemmas 4.11–4.12 provide qualitative equatorial-harmonic nonvanishing. The result above strengthens that particular rigidity assertion to an exact, quantitatively sharp stability inequality with identified extremizers and optimal Sobolev loss; the qualitative theorem by itself contains no uniform spectral constant.

The classical spherical Radon literature supplies associated-Legendre and representation-theoretic tools. In particular, McEwen and Price (arXiv:1510.01595) give spherical/spin Funk multipliers; Rubin (arXiv:2211.10348) develops harmonic multipliers for shifted Funk–Radon operators; and Hielscher and Quellmalz (2015) obtain singular values for vertical-slice averages. Those operators and statements are distinct from the *coupled second-plus-third Fourier measurement on all oriented great circles* and do not state this sharp two-sided quotient estimate. No claim is made that the underlying special-function identities or rotation orthogonality are new.

## Limitations
The measurement error controls a negative half-order Sobolev quotient norm, not Hausdorff distance or a positive-order curvature norm without additional uniform regularity. The constants refer to normalized Haar measure, surface-area \(L^2\), and the shifted spectral weight \((\ell+1/2)^{-1}\); changing these conventions changes the constants. The result concerns \(S^2\) and bodies in \(\mathbb R^3\); it does not assert the same constants in higher dimensions, nor does it give stable reconstruction from finitely many sampled planes. Literature priority has not been independently certified; more general harmonic-analytic frameworks might admit an equivalent formulation.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192 (2026), https://arxiv.org/abs/2609.27192.
2. J. D. McEwen, M. A. Price, *Scale-discretised ridgelet transform on the sphere*, arXiv:1510.01595, https://arxiv.org/abs/1510.01595.
3. B. Rubin, *On the Injectivity of the Shifted Funk-Radon Transform and Related Harmonic Analysis*, arXiv:2211.10348, https://arxiv.org/abs/2211.10348.
4. R. Hielscher, M. Quellmalz, *Reconstructing a Function on the Sphere from Its Means Along Vertical Slices* (2015), https://www-user.tu-chemnitz.de/~qmi/paper/circav.pdf.
