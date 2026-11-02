# A sharp Fourier-mode stability transition for harmonic perimeter contraction

## Finding

Fix \(0<r<1\). For every real \(2\pi\)-periodic \(C^3\) function \(h\), write
\[
h_k=\frac{1}{2\pi}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta.
\]
For sufficiently small real \(\varepsilon\) put \(F_\varepsilon(e^{i\theta})=e^{i(\theta+\varepsilon h(\theta))}\), let \(u_\varepsilon\) denote its harmonic Poisson extension to the disk, and set \(\Gamma_{\varepsilon,r}=\{u_\varepsilon(re^{i\phi}):0\le\phi\le2\pi\}\). The map \(F_\varepsilon\) is an orientation-preserving circle diffeomorphism. Its interior trace \(\Gamma_{\varepsilon,r}\) is a strictly convex Jordan curve for sufficiently small \(|\varepsilon|\).

Define the real, even Fourier multipliers
\[
d_0(r)=1,\qquad d_1(r)=r,\qquad
d_k(r)=\frac{r^{k-2}}{2}\big((k+1)r^2-(k-1)\big)\quad (k\ge2),
\qquad d_{-k}(r)=d_k(r).
\]
Then the planar harmonic perimeter deficit has the precise second variation
\[
2\pi r-\operatorname{Per}\big(\operatorname{co}\Gamma_{\varepsilon,r}\big)
=\pi r\varepsilon^2\sum_{k\in\mathbb Z\setminus\{0\}}
\big(1-d_{|k|}(r)^2\big)|h_k|^2
+O_{r,h}(|\varepsilon|^3).
\tag{1}
\]
The complete Hessian is strictly positive modulo constant \(h\), the infinitesimal rotation. Its **sharp** lower spectral gap, with the normalized \(L^2(d\theta/(2\pi))\) distance from constants, is
\[
G(r)=1-\max\left\{r^2,\left(\frac{3r^2-1}{2}\right)^2\right\}>0.
\tag{2}
\]
Specifically,
\[
\sum_{k\ne0}(1-d_{|k|}(r)^2)|h_k|^2
\ge G(r)\sum_{k\ne0}|h_k|^2.
\tag{3}
\]
The optimal directions switch at exactly \(r=1/3\): equality in (3), for nonconstant real \(h\), holds precisely when its nonconstant part is a first-harmonic trigonometric function for \(1/3<r<1\), a second-harmonic one for \(0<r<1/3\), or any combination of first and second harmonics at \(r=1/3\). At each radius these directions attain the quadratic coefficient sharply in (1).

## Assumptions and scope

The source disk is \(\mathbb D\subset\mathbb C\); complex-valued harmonicity means harmonicity of the real and imaginary parts. The boundary perturbation \(h\) is real and \(C^3\). The smallness threshold for \(|\varepsilon|\), and the remainder in (1), depend on the fixed pair \((r,h)\); no uniform remainder over all high-frequency perturbations is asserted. The circumference of the convex hull is the usual planar perimeter; for these small perturbations the convex hull is the bounded region enclosed by \(\Gamma_{\varepsilon,r}\). All Fourier coefficients use normalized Haar measure \(d\theta/(2\pi)\).

## Proof

**1. Poisson expansion and convexity.** Write \(\mathcal P_r\) for circular Poisson convolution, with Fourier action \(\mathcal P_r(e^{in\theta})=r^{|n|}e^{in\phi}\). Since \(h\in C^3\) and \(r<1\) is fixed, Taylor's theorem and smoothing by the Poisson operator give an expansion in the \(C^2\) norm of \(\phi\):
\[
\gamma_{\varepsilon,r}(\phi):=u_\varepsilon(re^{i\phi})
=re^{i\phi}+\varepsilon U(\phi)+\varepsilon^2V(\phi)+O_{r,h}(|\varepsilon|^3),
\]
where
\[
U=i\mathcal P_r(e^{i\theta}h),\qquad
V=-\tfrac12\mathcal P_r(e^{i\theta}h^2).
\tag{4}
\]
For \(\varepsilon=0\) the curve is a radius-\(r\) circle with positive regular speed and curvature. The strict-convexity inequality \(\operatorname{Im}(\overline\gamma'\gamma'')>0\) and nonzero speed persist by \(C^2\) continuity. Moreover the turning number and topological degree remain one. Hence the perturbed curve is a strictly convex embedded Jordan curve, and the convex-hull perimeter equals its arclength \(\int_0^{2\pi}|\gamma'_{\varepsilon,r}(\phi)|\,d\phi\).

**2. Expanding the arclength.** Set \(A(\phi)=ire^{i\phi}\), so \(|A|=r\). The elementary expansion, valid uniformly because \(r>0\), is
\[
|A+\varepsilon U'+\varepsilon^2V'|
=r\left[1+\varepsilon\operatorname{Re}\frac{U'}A
+\varepsilon^2\left(\operatorname{Re}\frac{V'}A+
\frac12\left(\operatorname{Im}\frac{U'}A\right)^2\right)\right]
+O_{r,h}(|\varepsilon|^3).
\tag{5}
\]
The normalized means satisfy
\[
\frac{1}{2\pi}\int\operatorname{Re}\frac{U'}A\,d\phi=0,
\qquad
\frac{1}{2\pi}\int\operatorname{Re}\frac{V'}A\,d\phi
=-\frac12\frac1{2\pi}\int h(\theta)^2\,d\theta.
\tag{6}
\]
Indeed, from (4), the zeroth Fourier coefficient of \(U'/A\) is \(ih_0\), which is purely imaginary, and that of \(V'/A\) is \(-\tfrac12(h^2)_0\).

**3. Diagonalizing the remaining term.** Direct differentiation of (4) gives
\[
\frac{U'(\phi)}{A(\phi)}
=i\sum_{k\in\mathbb Z}(k+1)r^{|k+1|-1}h_k e^{ik\phi}.
\]
Because \(h\) is real, the Fourier coefficient at frequency \(k\) of \(\operatorname{Im}(U'/A)\) equals \(d_{|k|}(r)h_k\), where
\[
d_{|k|}(r)=\frac12\left((k+1)r^{|k+1|-1}+(1-k)r^{|1-k|-1}\right).
\tag{7}
\]
For \(k=0,1,2,\ldots\), this reduces exactly to the multipliers specified above. Parseval yields
\[
\frac1{2\pi}\int_0^{2\pi}\left(\operatorname{Im}\frac{U'}A\right)^2\,d\phi
=\sum_{k\in\mathbb Z}d_{|k|}(r)^2|h_k|^2.
\tag{8}
\]
Combining (5)–(8), and using \((h^2)_0=\sum_k|h_k|^2\), proves (1). The constant coefficient cancels since \(d_0=1\).

**4. Exact optimization over modes.** For every \(k\ge3\), we claim \(|d_k(r)|<r\). Set \(t=r^2\in(0,1)\) and divide by \(r\):
\[
\frac{|d_k(r)|}{r}
=\tfrac12t^{(k-3)/2}\big|(k+1)t-(k-1)\big|.
\tag{9}
\]
If the quantity inside the absolute value is nonnegative, it is at most \(2t\), so (9) is at most \(t^{(k-1)/2}<1\). Otherwise it is \((k-1)-(k+1)t\). For \(k=3\), (9) is \(1-2t<1\). For \(k>3\), elementary differentiation gives its maximum on the negative-sign interval at \(t=(k-3)/(k+1)\), with value
\[
\left(\frac{k-3}{k+1}\right)^{(k-3)/2}<1.
\]
Thus among nonconstant modes only \(k=1\) or \(k=2\) can maximize \(|d_k|\). Now \(d_1=r\), and \(d_2=(3r^2-1)/2\). Solving \(|d_2|=r\) on \((0,1)\) gives only \(r=1/3\) (the other nonnegative endpoint solution is \(r=1\)). For smaller radii \(|d_2|>r\); for larger radii \(|d_2|<r\). This proves the sharp formula (2), every equality case in (3), and strict positivity (since \(|d_1|<1\), \(|d_2|<1\), and \(|d_k|<r\) for \(k\ge3\)). A pure sine or cosine of the maximizing frequency attains the optimal quadratic Rayleigh quotient. \(\square\)

## Verification

The coefficient normalization was independently checked by direct Fourier quadrature: the boundary samples \(e^{i(\theta+\varepsilon\cos(k\theta))}\) were Fourier-transformed, Poisson-multiplied, differentiated, and numerically integrated to obtain the perimeter for various radii and frequencies. The observed normalized deficits agreed with \((1-d_k(r)^2)/2\), the value of the right-hand coefficient for \(h(\theta)=\cos(k\theta)\). A standalone checker accompanies this document, including exact rational tests of (7) and the gap-order inequalities, plus independent finite quadratures. These computations are supplementary; the infinite-dimensional result and sharp global mode comparison are proved above.

## Relationship to prior work

Zhong and Kalaj (2026, arXiv:2609.09316) proved the global sharp convex-hull mean-width contraction and its planar perimeter corollary, together with the exact equality rigidity for harmonic maps; those results are the motivation, not new claims here. Their planar corollary supplies the nonnegative deficit \(2\pi r-\operatorname{Per}\), but does not identify its full second variation or the change in its least-penalized perturbation. The present calculation supplies the diagonal Fourier Hessian and its exact radius-dependent spectral gap.

Koh and Kovalev (arXiv:0911.0623) treated the area contraction of harmonic disk automorphisms, rather than this perimeter deficit. Geleta (arXiv:2601.14717) studied the Lebesgue-area behavior of planar harmonic maps. Neither area statement determines the Fourier Hessian of the convex-hull perimeter. Some earlier, unindexed harmonic variation or geometric-shape literature may contain an equivalent calculation; this is an originality limitation, not a premise of the proof.

## Limitations

The result is local in \(\varepsilon\) at fixed \(r\), restricted to smooth orientation-preserving reparametrizations of the unit circle and the planar Poisson extension. It is not a nonlinear global \(L^2\)-stability inequality, and it does not supply uniform remainders for high-frequency \(h\) or characterize arbitrary nonsmooth boundary maps. The \(r=1/3\) transition is a local quadratic stability transition, not a change in the global equality theorem. Independent mathematical validation has not been performed.

## References

1. D. Zhong and D. Kalaj, *Sharp mean-width and Jacobian bounds for Euclidean and hyperbolic harmonic maps*, arXiv:2609.09316 (first public 2026-09-08), especially Theorem 1.4, Corollary 1.5, and Theorem 1.8. https://arxiv.org/abs/2609.09316
2. N.-T. Koh and L. Kovalev, *Area contraction for harmonic automorphisms of the disk*, arXiv:0911.0623. https://arxiv.org/abs/0911.0623
3. H. Geleta, *The Effect of Planar Harmonic Mappings on the Lebesgue Measure of Sets*, arXiv:2601.14717. https://arxiv.org/abs/2601.14717
