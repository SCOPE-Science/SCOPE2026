# Sharp affine least-squares amplification on parallelepipeds and a dimension-five positivity threshold

## Finding

For every integer \(d\ge1\), every nondegenerate real \(d\)-dimensional parallelepiped \(Q\), and the ordinary \(L^2(Q)\)-orthogonal projector \(P_d\) onto the space of affine real-valued functions on \(Q\), its **sharp** \(L^\infty(Q)\)-operator norm is the following rational number:

\[
\boxed{\displaystyle
\Lambda_d=\|P_d\|_{L^\infty\to L^\infty}
=-1+\frac{12}{(d+1)!}
\sum_{k=0}^{\left\lfloor(3d+1)/6\right\rfloor}
(-1)^k\binom dk
\left(\frac{3d+1}{6}-k\right)^{d+1}.}
\]

All vertices of \(Q\) attain the maximal absolute kernel mass, and for each vertex a bounded sign-valued input realizes this exact norm. Define the sharp positivity defect for data in the unit interval by
\[
C_d=\sup_{0\le f\le1\ \mathrm{a.e.}}\left(-\min_{x\in Q}(P_df)(x)\right).
\]
Then \(C_d=(\Lambda_d-1)/2\). The constants \(\Lambda_d\) are **strictly increasing** with dimension. In particular, \(\Lambda_4=75437/25920<3<46973/14580=\Lambda_5\), so dimension **five** is exactly the first dimension in which some \(0\le f\le1\) has its affine least-squares projection below \(-1\). This remains possible with \(0<f\le1\) almost everywhere.

The sharp two-term asymptotic law is
\[
\boxed{\displaystyle
\Lambda_d=\sqrt{\frac{6d}{\pi}}\left(1+\frac{13}{60d}+o(d^{-1})\right)
\qquad(d\to\infty).}
\]

The first values are \(\Lambda_1=5/3\), \(\Lambda_2=233/108\), \(\Lambda_3=415/162\), \(\Lambda_4=75437/25920\), and \(\Lambda_5=46973/14580\).

## Assumptions and scope

The domain \(Q\) is an affine image of \([-1,1]^d\) under an invertible real affine map, with uniform Lebesgue measure, not an arbitrary polytope. The projector is element-local and unconstrained, onto all polynomials of total degree at most one; the input can be any real essentially bounded measurable function. The \(L^2\) inner product is unweighted. No assertion covers tensor-product multilinear \(Q_1\) shape functions, a global continuous finite-element projector, nonuniform densities, or higher polynomial degrees.

Affine changes of variables preserve this operator norm, because the common Jacobian-volume factor cancels in every orthogonality equation. It therefore suffices to prove the statements for \(Q=[-1,1]^d\) with normalized uniform measure \(\mu\), without imposing orthogonality of the parallelepiped's edges.

## Proof

**1. Reproducing kernel and exact extremizing location.** On the normalized cube, the constant function and \(\sqrt3\,x_i\) for \(1\le i\le d\) form an orthonormal basis of the real affine functions. Thus
\[
(P_df)(x)=\int_Q K_d(x,y)f(y)\,d\mu(y),\qquad
K_d(x,y)=1+3\sum_{i=1}^d x_i y_i.
\]
At a fixed \(x\), the largest possible absolute output over \(\|f\|_\infty\le1\) is exactly \(\int|K_d(x,y)|\,d\mu(y)\), attained by the measurable sign of that kernel. The integral is a convex function of \(x\) on the cube, hence its maximum occurs at a vertex, and coordinate sign symmetries make all vertices equivalent. If \(Y_i\) are independent uniform \([-1,1]\) variables, this proves
\[
\Lambda_d=\mathbb E\left|1+3\sum_{i=1}^dY_i\right|.
\]
Also \(\int K_d(x,y)\,d\mu(y)=1\). Therefore the negative kernel mass at \(x\) is one-half its absolute mass minus one-half. The indicator of the negative-kernel region at a vertex attains \(C_d=(\Lambda_d-1)/2\). For strictly positive unit-bounded inputs take \(f_\varepsilon=\varepsilon+(1-\varepsilon)\mathbf1_{\{K_d(v,\cdot)<0\}}\); its projected value at \(v\) is \(\varepsilon-(1-\varepsilon)C_d\). In particular, when \(C_d>1\) it lies below \(-1\) for \(0<\varepsilon<(C_d-1)/(C_d+1)\).

**2. Exact finite formula.** Write \(Y_i=2U_i-1\) with independent \(U_i\sim\mathrm{Unif}[0,1]\), let \(S_d=\sum_iU_i\), and set \(a=(3d+1)/6\). Symmetry of \(S_d\) around \(d/2\) implies
\[
\Lambda_d=6\mathbb E|S_d-a|=12\mathbb E(a-S_d)_+-1.
\]
The inclusion-exclusion formula for the volume of a clipped unit cube gives, for all real \(z\),
\[
\Pr(S_d\le z)=\frac{1}{d!}\sum_{k=0}^d(-1)^k\binom dk(z-k)_+^d.
\]
Integrating this cumulative distribution from \(0\) to \(a\) yields
\[
\mathbb E(a-S_d)_+=\frac{1}{(d+1)!}\sum_{k=0}^{\lfloor a\rfloor}(-1)^k\binom dk(a-k)^{d+1},
\]
which establishes the claimed exact norm and positivity-defect formulas.

**3. Strict growth and the dimension-five threshold.** Condition on \(Z_d=1+3\sum_{i=1}^dY_i\). Jensen's inequality yields \(\mathbb E(|Z_d+3Y_{d+1}|\mid Z_d)\ge|Z_d|\), with strict inequality whenever \(|Z_d|<3\), because the added uniform variable straddles zero. This event has positive probability for every \(d\ge1\), proving \(\Lambda_{d+1}>\Lambda_d\). Direct substitution in the exact rational formula gives \(\Lambda_4=75437/25920<3\) and \(\Lambda_5=46973/14580>3\). Since \(C_d=(\Lambda_d-1)/2\), the precise first dimension of a negative excursion below \(-1\) is five. The nonnegative-data minimum is attained by the stated indicator at a vertex.

**4. Two-term asymptotic with controlled remainder.** For every real \(z\), the Fourier absolute-value identity is
\[
|z|=\frac2\pi\int_0^\infty\frac{1-\cos(tz)}{t^2}\,dt.
\]
By independence and symmetry, \(\mathbb E\cos(3t\sum_iY_i)=\big(\sin(3t)/(3t)\big)^d\). After \(s=\sqrt{3d}\,t\),
\[
\Lambda_d=\frac{2\sqrt{3d}}\pi\int_0^\infty
\frac{1-\cos(s/\sqrt{3d})\,[\operatorname{sinc}(\sqrt{3/d}\,s)]^d}{s^2}\,ds.
\]
For fixed \(s\), Taylor expansion gives
\[
[\operatorname{sinc}(\sqrt{3/d}\,s)]^d
=e^{-s^2/2}\left(1-\frac{s^4}{20d}+O_s(d^{-2})\right),\qquad
\cos(s/\sqrt{3d})=1-\frac{s^2}{6d}+O_s(d^{-2}).
\]
These expansions can be integrated with a uniform remainder: split at \(s=d^{1/9}\) and at \(s=\delta\sqrt d\) for fixed sufficiently small \(\delta>0\). On the first range the Taylor remainder divided by \(s^2\), multiplied by \(d\), is bounded by \(d^{-1}e^{-cs^2}\) times a fixed polynomial in \(s\); on the intermediate range \(|\operatorname{sinc}(\sqrt{3/d}\,s)|^d\le e^{-cs^2}\); beyond the latter split its absolute value is bounded by \(\rho^d\) for some \(\rho<1\), giving an exponentially small integrated tail after division by \(s^2\). The Gaussian term has the same tail control. Hence the termwise expansion is valid to order \(o(d^{-1})\) after factoring \(\sqrt d\).

The leading integral is \(\int_0^\infty(1-e^{-s^2/2})s^{-2}\,ds=\sqrt{\pi/2}\). The order-\(1/d\) integral is
\[
\int_0^\infty e^{-s^2/2}\left(\frac16+\frac{s^2}{20}\right)\,ds
=\frac{13}{60}\sqrt{\frac\pi2}.
\]
Combining them proves \(\Lambda_d=\sqrt{6d/\pi}\,(1+13/(60d)+o(d^{-1}))\).

## Verification

The standalone `verify.py` performs exact rational computations without third-party packages. It evaluates the binomial expression and independently reconstructs the Irwin--Hall density by repeated convolution of piecewise polynomials, integrates \(|6s-3d+1|\) against that density, and compares the two results exactly through dimension nine. It also checks strict growth over a finite test range, the exact five low-dimensional values, the exact dimension-five crossing, and numerical agreement with the asymptotic coefficient for larger dimensions. The universal convexity, inclusion-exclusion, and Fourier remainder arguments are the proof; finite checks are corroboration, not a replacement.

Execute `python verify.py` from a directory containing the file. The script reports the assertion count and exits nonzero on failure.

## Relationship to prior work

The sharp \(L^\infty\) behavior of least-squares projectors is a classical approximation-theory stability question. Foucart (2006) studies maximum norms of one-dimensional orthogonal spline projectors. Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first public 2010-05-13) give boundedness and near-best approximation for kernel-generated least-squares projectors on compact manifolds; their object is not the finite-dimensional local affine projector on a parallelepiped. Both support the mathematical motivation but do not yield the present sharp cube formula.

A separate published exact result for the affine local projector on a simplex gives \(\Lambda_d^{\mathrm{simplex}}=2(d+1)((d+1)/(d+2))^d-1\), which is of order \(d\). The present parallelepiped formula is not implied by that result: the affine-kernel evaluation involves a sum of independent uniforms rather than one Dirichlet barycentric coordinate. In particular, the cube grows only like \(\sqrt d\), and its first excursion below \(-1\) for data in \([0,1]\) occurs at dimension five rather than dimension three for a simplex. The difference between these two natural element shapes is part of the present motivation.

An earlier published result on a reverse-projection perturbation uses the centered absolute first moment of an Irwin--Hall sum. It does not concern this affine \(L^2\) projector, the nonzero threshold shift in the exact formula, or the sharp positivity classification. Defant, Galicer, Mansilla, Mastyło and Muro (2022, Chapter 8) study projection constants of polynomial subspaces on the **discrete Boolean cube** with normalized counting measure. Their degree-one random-variable kernels involve Bernoulli signs, whereas the local affine \(L^2\) projector here uses continuously uniform coordinates; in particular, their discrete formula does not determine the present exact continuous-cube constants or positivity cutoff. The formula uses standard inclusion-exclusion and Gaussian asymptotics; neither method is claimed to be new.

## Limitations

The problem is deliberately local, uniform-measure, degree one, and on parallelepipeds. The exact rational formula and dimension threshold do not determine stability of globally coupled finite-element projections, higher-order polynomial spaces, arbitrary convex polytopes, or weighted designs. The asymptotic expansion has a proved little-o error at the displayed order; no uniform explicit finite-dimensional error bound is asserted. An equivalent historical cube formula could exist in approximation-theory textbooks or projection-constant tables under terminology not recovered by the searches, so historical priority remains provisional. Independent review has not been carried out.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424v1, first public 2010-05-13; SIAM J. Math. Anal. 43 (2011), 662--684. https://arxiv.org/abs/1005.2424.
2. S. Foucart, *On the value of the max-norm of the orthogonal projector onto splines with multiple knots*, J. Approx. Theory 140 (2006), 154--177. DOI: 10.1016/j.jat.2005.12.004.
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical record, 2026-10-04. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34.
4. *The equally spaced reverse-projection perturbation changes sign exactly in dimension nine*, published mathematical record, 2026-10-04. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-equally-spaced-reverse-projection-perturbation-changes-sign--1b2f50a075e8.
5. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1 (2022), Chapter 8, pp. 101--105. https://arxiv.org/abs/2208.06467.
