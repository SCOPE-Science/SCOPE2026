# The quadratic cutoff is sharp for rotation-angle covariance on \(SO(3)\)

## Finding

Let \(\vartheta(Q)\in[0,\pi]\) be the principal rotation angle of \(Q\in SO(3)\). For every radius \(0<R\le\pi\) and every real exponent \(\alpha>0\), set
\[
K_{R,\alpha}(U,V)=\bigl(R-\vartheta(U^{-1}V)\bigr)_+^{\alpha},\qquad U,V\in SO(3).
\]
Here \(t_+=\max(t,0)\). This continuous central kernel is positive semidefinite on every finite configuration of rotations **if and only if** \(\alpha\ge2\). For \(\alpha\ge2\), it is strictly positive definite on every finite set of distinct rotations, including at the sharp endpoint \(\alpha=2\). For every \(0<\alpha<2\), infinitely many irreducible character coefficients are strictly negative. At any fixed radius with irrational \(R/(2\pi)\), precisely one-half of the high-spin indices have negative coefficients in natural-density sense.

The positive-definiteness direction at and above exponent two is consistent with previously published projective-space sufficient conditions, and is **not** presented as novel. The distinguishing assertion is the necessity at every fixed support radius, with explicit high-frequency sign oscillation.

## Assumptions and scope

The group is the real compact Lie group \(SO(3)\) equipped with normalized Haar measure. Its irreducible unitary representations are indexed by integers \(\ell\ge0\), have dimension \(2\ell+1\), and central characters
\[
\chi_\ell(\theta)=\frac{\sin((\ell+\tfrac12)\theta)}{\sin(\theta/2)}
=1+2\sum_{j=1}^\ell\cos(j\theta).
\]
For a conjugation-invariant function, integration against Haar measure reduces to
\[
\int_{SO(3)}f(\vartheta(Q))\,dQ
=\frac1\pi\int_0^\pi f(\theta)(1-\cos\theta)\,d\theta.
\]
A continuous central kernel is positive semidefinite on all finite sets exactly when all its scalar Peter–Weyl transform blocks are nonnegative. This statement concerns global positive definiteness on the entire group; it does not assert positive definiteness of arbitrary functions of intrinsic distances on other manifolds.

## Proof

**Step 1: exact character reduction.** Define
\[
J_n(R,\alpha)=\int_0^R(R-\theta)^\alpha\cos(n\theta)\,d\theta,\qquad n\in\mathbb N_0.
\]
The character identity
\[
(1-\cos\theta)\chi_\ell(\theta)
=\cos(\ell\theta)-\cos((\ell+1)\theta)
\]
gives the exact scalar character integral
\[
b_\ell(R,\alpha)
=\int_{SO(3)}(R-\vartheta(Q))_+^\alpha\chi_\ell(Q)\,dQ
=\frac{J_\ell(R,\alpha)-J_{\ell+1}(R,\alpha)}{\pi}.
\]
The Fourier transform matrix equals \(b_\ell I_{2\ell+1}/(2\ell+1)\). Thus the sign of \(b_\ell\) is decisive, with no dependence on an unspecified normalization.

**Step 2: strictly positive coefficients at the quadratic endpoint.** Direct integration by parts gives
\[
J_0(R,2)=R^3/3,\qquad
J_n(R,2)=\frac{2R}{n^2}-\frac{2\sin(nR)}{n^3}
=2R^3h(nR),\quad n\ge1,
\]
where \(h(x)=(x-\sin x)/x^3\). For \(x>0\),
\[
-h'(x)=\frac{2x+x\cos x-3\sin x}{x^4}>0.
\]
Indeed, on \((0,\pi)\), the derivative of the numerator equals
\(2\sin(x/2)[2\sin(x/2)-x\cos(x/2)]>0\), using \(\tan y>y\) for \(0<y<\pi/2\); the numerator vanishes at zero. For \(x\ge\pi\), it is at least \(x-3>0\). Hence \(h\) is strictly decreasing, and \(J_\ell(R,2)>J_{\ell+1}(R,2)\) for all \(\ell\ge1\). At \(\ell=0\), strict positivity follows directly from
\[
J_0(R,2)-J_1(R,2)
=\int_0^R(R-\theta)^2(1-\cos\theta)\,d\theta>0.
\]
Therefore \(b_\ell(R,2)>0\) for every \(\ell\ge0\) and every \(R\in(0,\pi]\).

**Step 3: all higher powers.** For each \(\alpha>2\), the beta-integral identity
\[
(R-\theta)_+^\alpha
=\frac{\alpha(\alpha-1)(\alpha-2)}2
 \int_0^R(s-\theta)_+^2(R-s)^{\alpha-3}\,ds
\]
expresses the power as a strictly positive mixture of the quadratic kernels at smaller radii. Every \(b_\ell(s,2)\) in the integrand is positive for \(s>0\). Consequently \(b_\ell(R,\alpha)>0\) for all indices and all exponents \(\alpha\ge2\).

To deduce strict finite-set positive definiteness, take a nonzero finitely supported signed (or complex) measure \(\mu=\sum_jc_j\delta_{U_j}\) on pairwise distinct group elements. Its energy is a positive sum of the squared Hilbert–Schmidt norms of its irreducible Fourier matrices, each multiplied by a strictly positive transform block. If this energy were zero, every Fourier matrix of \(\mu\) would vanish. Completeness of matrix coefficients in continuous functions on the compact group would force \(\mu=0\), a contradiction.

**Step 4: sharp necessity and the sign distribution.** Fix \(0<\alpha<2\) and \(R\in(0,\pi]\). Standard one-sided Fourier endpoint expansion, obtained by partitioning near \(\theta=0\) and \(\theta=R\), gives
\[
J_n(R,\alpha)=
\frac{\alpha R^{\alpha-1}}{n^2}
+\frac{\Gamma(\alpha+1)}{n^{\alpha+1}}
\cos\!\left(nR-\frac{\pi(\alpha+1)}2\right)
+O_{R,\alpha}(n^{-3}).
\]
A direct derivation avoids any assumption about sampling or numerical stability. With \(\gamma(s,z)=\int_0^z t^{s-1}e^{-t}\,dt\) analytically continued along the principal branch, substitution \(u=R-\theta\) gives the **exact identity**
\[
J_n(R,\alpha)=\operatorname{Re}\!\left[
\frac{e^{inR}\gamma(\alpha+1,inR)}{(in)^{\alpha+1}}\right],\qquad n\ge1.
\]
Use \(\gamma(s,z)=\Gamma(s)-\Gamma(s,z)\) and the elementary large-argument integration-by-parts expansion
\[
\Gamma(s,z)=z^{s-1}e^{-z}\left(1+\frac{s-1}{z}+O_s(|z|^{-2})\right)
\]
on the ray \(z=inR\), for each fixed positive \(R\). The first upper-gamma term is purely imaginary after the prefactor is included, its next term contributes exactly \(\alpha R^{\alpha-1}/n^2\), and the remainder is \(O_{R,\alpha}(n^{-3})\). This proves the displayed expansion including its error bound. For the integer case \(\alpha=1\), the exact identity \(J_n=(1-\cos(nR))/n^2\) gives the same result directly.

Subtracting consecutive indices cancels the common leading \(n^{-2}\) term to order \(n^{-3}\). Since \(\alpha+1<3\), this yields
\[
\boxed{\;
 b_\ell(R,\alpha)=
\frac{2\Gamma(\alpha+1)\sin(R/2)}{\pi\ell^{\alpha+1}}
\sin\!\left((\ell+\tfrac12)R-\frac{\pi(\alpha+1)}2\right)
+o_{R,\alpha}(\ell^{-\alpha-1}).\;}
\]
The amplitude is nonzero for every allowed \(R\). If \(R/(2\pi)\) is irrational, the phase angles are equidistributed modulo \(2\pi\), so their sine is negative for a set of indices of natural density \(1/2\); the asymptotically negligible error does not affect the density because the zero set of sine has angular measure zero. If \(R/(2\pi)\) is rational and \(R<\pi\), the phases visit equally spaced points in a periodic orbit of at least three positions; one has strictly negative sine and recurs infinitely often. For \(R=\pi\), the sine equals \((-1)^{\ell+1}\sin(\pi\alpha/2)\), which alternates strictly in sign since \(0<\alpha<2\). In every case there are infinitely many \(\ell\) with \(b_\ell<0\). The Peter–Weyl characterization then rules out positive semidefiniteness. This proves necessity and completes the theorem.

## Verification

The self-contained accompanying `checker.py` evaluates the exact character integrals in two independent ways (complex incomplete gamma functions and direct quadrature), checks the closed quadratic formula, confirms strictly positive consecutive differences for sampled radii and degrees, and finds negative coefficients for subcritical exponents at multiple radii. In its recorded execution, all 374 finite diagnostic assertions passed. These calculations are checks of formulas and representative signs, **not** a finite certificate for the quantified infinite-frequency theorem; the proof above supplies the latter.

For direct reproduction, run `python checker.py` in a Python 3 environment with `mpmath` installed. The checker uses no external datasets or proprietary modules. The complete mathematical sign argument is self-contained in this document.

## Relationship to prior work

Beatson–zu Castell–Xu (2011, arXiv:1110.2437) develops spherical Pólya-type sufficient criteria. Xu (2017, arXiv:1701.00787) extends the setting to compact two-point homogeneous spaces and gives positivity of projective-space truncated powers above a dimension-dependent exponent. Lu (2024 online / 2025 journal) proves strict positive definiteness of truncated powers at the same sufficient threshold, including real projective spaces. Since \(SO(3)\) with its bi-invariant rotation-angle geometry corresponds to \(\mathbb{RP}^3\) up to a factor-two distance scaling, **these sources cover the sufficient half \(\alpha\ge2\) of the result**. The present claim does not take credit for that half. It establishes, through an explicit representation-theoretic coefficient asymptotic, the missing sharp *necessity for each individual radius* and infinitely many negative modes below the threshold. General classifications of strictly positive definite kernels on projective spaces supply spectral criteria but do not alone establish this exponent cutoff.

## Limitations

The theorem only concerns radial truncated powers of the principal rotation angle on the full compact group \(SO(3)\) and support radii \(0<R\le\pi\). It makes no claim of a new sufficient condition and does not classify all central positive-definite functions or kernels on other compact groups. An equivalent necessity argument under real-projective Jacobi or Euclidean radial notation could exist outside inspected sources; neither database searches nor bounded primary-text review proves universal novelty. All spectral calculations and the proof are presented for independent mathematical review; no independent audit has occurred.

## References

1. R. K. Beatson, W. zu Castell, and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (first posted 2011-10-11), https://arxiv.org/abs/1110.2437.
2. Y. Xu, *Positive definite functions on the unit sphere and integrals of Jacobi polynomials*, arXiv:1701.00787 (first posted 2017-01-03), https://arxiv.org/abs/1701.00787.
3. T. Lu, *Strictly positive definite functions on spheres*, Journal of Approximation Theory 306 (2025), article 106120 (online 2024-11-15), https://doi.org/10.1016/j.jat.2024.106120; author-posted full text https://www.math.wichita.edu/~lu/resume/power.pdf.
4. O. Barbosa and V. A. Menegatto, *Strictly positive definite kernels on two-point compact homogeneous spaces*, arXiv:1505.00591 (2015), https://arxiv.org/abs/1505.00591.
