# Complete shrinking-polar-cap spectral hierarchy for bandlimited spherical harmonics

## Finding
Let \(L\geq0\) be a fixed integer, let \(\mathcal H_{\leq L}\) be the complex spherical harmonics of degrees \(0,\ldots,L\) on the unit sphere, and use probability surface measure. Let \(C_{L,\delta}\) be the positive concentration operator with quadratic form equal to the energy in the north-polar cap
\[
\mathcal C_\delta=\{\omega\in S^2:(1-\omega_3)/2\leq\delta\},\qquad 0<\delta<1.
\]
For \(0\leq m\leq L\), put \(d=L-m\). The angular orders \(m\) and \(-m\) have identical spectral blocks, each with \(d+1\) eigenvalues \(\lambda_{m,0}(\delta)>\cdots>\lambda_{m,d}(\delta)>0\) for sufficiently small \(\delta\). Define
\[
\mathscr K_n(\alpha,\beta)=
\frac{\Gamma(n+\alpha+\beta+2)\Gamma(n+\alpha+2)}
{(\alpha+1)\Gamma(\alpha+1)^2\Gamma(n+\beta+1)\Gamma(n+1)}
\quad(n,\alpha,\beta\in\mathbb N_0).
\]
Then for each fixed \(L,m,j\) with \(0\leq j\leq L-m\),
\[
\boxed{\displaystyle
\lambda_{m,j}(\delta)=
\frac{\mathscr K_{L-m-j}(m+2j,m)}
{(m+2j+1)\binom{m+2j}{j}^{2}}
\delta^{m+2j+1}(1+O_L(\delta)).}
\]
Every leading constant is explicit and positive. Across the full \((L+1)^2\)-dimensional space, the powers \(\delta^{k+1}\), \(0\leq k\leq2L\), have exponent multiplicities exactly
\[
\boxed{\min\{k+1,2L-k+1\}.}
\]
The largest and smallest eigenvalues are each eventually simple, both in angular order zero, and satisfy
\[
\lambda_{\max}(C_{L,\delta})=(L+1)^2\delta(1+O_L(\delta)),\qquad
\lambda_{\min}(C_{L,\delta})=
\binom{2L}{L}^{-2}\delta^{2L+1}(1+O_L(\delta)).
\]
Consequently the exact leading conditioning constant is
\[
\boxed{\displaystyle
\kappa(C_{L,\delta})=(L+1)^2\binom{2L}{L}^2\delta^{-2L}(1+O_L(\delta)).}
\]
The unit least-concentrated eigenfunction, with a suitable phase, converges in \(L^2(S^2)\) to the zonal polynomial
\[
\sqrt{2L+1}\left(\frac{1-\omega_3}{2}\right)^L.
\]
In terms of the angular cap radius \(\vartheta\), \(\delta=(1-\cos\vartheta)/2\sim\vartheta^2/4\); hence the condition number grows like \(\vartheta^{-4L}\) when \(L\geq1\) is fixed.

## Assumptions and scope
The degree bound \(L\) is fixed before \(\delta\downarrow0\), and the complete scalar complex spherical-harmonic space through degree \(L\) is used. There is no simultaneous large-bandwidth limit. Both the full norm and the cap norm use the same probability surface measure, so the concentration spectrum is unaffected by changing the overall common normalization. Multiplicity refers to complex dimension: the angular orders \(\pm m\) contribute two copies for \(m>0\). The error terms need not be uniform in an increasing \(L\).

## Proof
**1. Exact reduction.** Set \(t=(1-\cos\vartheta)/2\). At angular order \(\pm m\), associated Legendre functions through degree \(L\) span, up to a harmless nonzero angular and radial scalar,
\[
e^{\pm im\varphi}[t(1-t)]^{m/2}p(t),\qquad \deg p\leq d=L-m.
\]
Integration over azimuth makes distinct angular orders orthogonal on both the sphere and the cap. The concentration quotient on this block is exactly
\[
\frac{\int_0^\delta |p(t)|^2t^m(1-t)^m\,dt}
{\int_0^1 |p(t)|^2t^m(1-t)^m\,dt}.
\]
Thus the block is the restriction operator from the \((d+1)\)-dimensional polynomial Hilbert space \(V_{m,d}\), with global weight \(t^m(1-t)^m\), to the interval \([0,\delta]\).

**2. Critical exterior-power lemma.** Let \(c_i(p)\) denote the coefficient of \(t^i\) in \(p\), and let \(Q=(Q_{ih})_{0\leq i,h\leq d}\) be the global monomial Gram matrix,
\[
Q_{ih}=\mathrm B(m+i+h+1,m+1).
\]
Define \(H_k=[(m+i+h+1)^{-1}]_{0\leq i,h<k}\) and let \(G_k=[(Q^{-1})_{ih}]_{0\leq i,h<k}\); empty determinants equal one. On substituting \(t=\delta u\), the restriction map, unitarily transferred to \(L^2([0,1],u^mdu)\), is
\[
T_\delta p(u)=\delta^{(m+1)/2}(1-\delta u)^{m/2}
\sum_{i=0}^d\delta^iu^ic_i(p).
\]
The first nonzero term in its \(k\)-fold exterior power comes **uniquely** from the coefficient indices \(0,\ldots,k-1\). It is a rank-one exterior operator: its range vector is \(1\wedge u\wedge\cdots\wedge u^{k-1}\), and its domain functional is \(c_0\wedge\cdots\wedge c_{k-1}\). Their squared norms are respectively \(\det H_k\) and \(\det G_k\). The remaining terms are at least one power of \(\delta\) higher (the weight multiplier also differs from one by \(O(\delta)\)). Therefore the operator norm of the exterior power, which equals the product of the \(k\) largest singular values, gives
\[
\prod_{i=0}^{k-1}\lambda_{m,i}(\delta)
=\delta^{k(m+k)}\det H_k\det G_k\,(1+O_L(\delta)),
\qquad 1\leq k\leq d+1.
\]
Dividing neighboring products, including the empty product for \(k=0\), yields
\[
\lambda_{m,j}(\delta)
=\frac{\det H_{j+1}}{\det H_j}
\frac{\det G_{j+1}}{\det G_j}
\delta^{m+2j+1}(1+O_L(\delta)).
\]
This also proves the strict intra-block ordering for sufficiently small \(\delta\); no numerical inference or finite enumeration is needed.

**3. Exact coefficient evaluation.** The first determinant quotient is the squared norm of the monic degree-\(j\) polynomial orthogonal for the weight \(u^m\) on \([0,1]\). Its shifted Jacobi polynomial gives
\[
\frac{\det H_{j+1}}{\det H_j}
=\frac{1}{(m+2j+1)\binom{m+2j}{j}^{2}}.
\]
Jacobi's complementary-principal-minor identity gives
\[
\det G_k=\frac{\det Q_{[k:d],[k:d]}}{\det Q}.
\]
The next determinant quotient is therefore the value at zero of the degree-\((d-j)\) reproducing kernel for weight \(t^{m+2j}(1-t)^m\). The shifted Jacobi endpoint kernel identity evaluates it as \(\mathscr K_{d-j}(m+2j,m)\). This identity follows either from Christoffel--Darboux at the endpoint or by summing the explicitly normalized squared endpoint values of the Jacobi basis. Substitution proves the claimed coefficient.

**4. Whole-spectrum consequences.** The exponent from the pair \((m,j)\) is \(k+1\), where \(k=m+2j\). The conditions \(0\leq m\leq L\), \(0\leq j\leq L-m\) give, after counting the two copies when \(m>0\), exactly \(\min\{k+1,2L-k+1\}\) eigenvalues with exponent \(k+1\). The smallest exponent occurs only at \((m,j)=(0,0)\); its coefficient is \(\mathscr K_L(0,0)=(L+1)^2\). The largest exponent occurs only at \((0,L)\); its coefficient is \(\binom{2L}{L}^{-2}\). This gives the extremal asymptotics and the condition number.

**5. Least-concentrated mode.** The least eigenvalue belongs to the zonal polynomial block for small \(\delta\). A unit polynomial with cap energy \(O(\delta^{2L+1})\) must have each coefficient below degree \(L\) tending to zero: otherwise the rescaled local polynomial has a nonzero lower-order term and its positive weighted polynomial norm forces a larger power of \(\delta\). The only possible normalized limit is therefore a phase multiple of \(t^L\), whose full \(L^2([0,1],dt)\) norm is \((2L+1)^{-1/2}\). Choosing phase proves the stated limit. Lower-degree coefficients of the actual eigenfunction may be nonzero at order \(\delta\) and must not be discarded when computing the sharp smallest-eigenvalue constant.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The exact-rational checker compares both formulas for every coefficient for \(0\leq L\leq8\), verifies determinant-product exponents, the triangular multiplicity law, and the two extremal constants. It completed 291 passing exact-arithmetic assertions. Independent high-precision direct generalized-eigenvalue calculations for \(1\leq L\leq4\) and every angular order were also compared against the leading constants at \(\delta=10^{-4}\); they agreed to the expected first-order relative accuracy. These finite checks corroborate the formulas, while the exterior-power argument proves the theorem for all fixed finite \(L\).

## Relationship to prior work
Simons, Dahlen and Wieczorek formulate the spherical Slepian operator, decompose the polar-cap problem by azimuthal order, and establish an asymptotic regime in which the cap shrinks while the bandwidth increases at fixed Shannon number [1]. Michel, Plattner and Seibert give general spin-weighted spherical-cap concentration operators and commuting tridiagonal operators [2]. Those results are foundational but do not, in their inspected sections, supply this **fixed-bandwidth** complete small-cap exponent/multiplicity hierarchy, the explicit Jacobi endpoint constants, or the sharp smallest-mode condition number. The present statements do not claim the standard spherical-harmonic decomposition, Jacobi identities or Slepian formulation as original.

## Limitations
The asymptotic is not uniform when the degree cutoff grows with shrinking cap size, and it does not address spin-weighted sectors beyond scalar spin zero. The quantitative constants are local small-cap limits rather than exact eigenvalues at finite cap radii. Priority cannot be ruled out by a database search; related thesis-level treatments and unindexed spectral asymptotics remain possible. No independent mathematical audit has been performed.

## References
[1] F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424 (first posted 2004-08-31), SIAM Review 48 (2006), 504–536. https://arxiv.org/abs/math/0408424

[2] V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first posted 2021-03-26). https://arxiv.org/abs/2103.14650

[3] K. Seibert, *Spin-Weighted Spherical Harmonics and Their Application for the Construction of Tensor Slepian Functions on the Spherical Cap*, doctoral thesis, University of Siegen, 2018. https://dspace.ub.uni-siegen.de/entities/publication/87b140bd-e63e-434f-ba43-f98843cba1fd
