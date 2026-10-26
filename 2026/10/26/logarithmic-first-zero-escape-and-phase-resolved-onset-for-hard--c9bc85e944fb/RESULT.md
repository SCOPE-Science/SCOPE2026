# Logarithmic first-zero escape and phase-resolved onset for hard-truncated Gaussians

## Finding
For \(L>0\), let
\[
F_L(\xi)=\int_{-L}^{L}e^{-x^2}e^{-i\xi x}\,dx
=2\int_0^L e^{-x^2}\cos(\xi x)\,dx,
\]
and let \(\xi_1(L)\) be its smallest positive real zero. The normalized symmetric truncated-normal characteristic function has the same zeros.

**First-zero law.** The first zero exists for every \(L>0\), and
\[
\boxed{\xi_1(L)=2L+\frac{\log L+O(1)}L}\qquad(L\to\infty).
\]
In particular, the first zero lies beyond \(2L\) by a positive logarithmic boundary-layer distance for sufficiently large \(L\).

**Phase-resolved onset.** With \(\theta_L=2L^2+\log L\) interpreted modulo \(2\pi\), uniformly for \(y\) in every fixed compact real interval,
\[
\boxed{L e^{L^2}F_L\left(2L+\frac{\log L+y}{L}\right)
=\sqrt\pi e^{-y}-\frac1{\sqrt2}\cos(\theta_L+y+\pi/4)
+O_K\!\left(\frac{(1+\log L)^2}{L^2}\right).}
\]
The same estimate holds after one derivative with respect to \(y\).

For \(\theta\in\mathbb R/(2\pi\mathbb Z)\), set
\[
B_\theta(y)=\sqrt\pi e^{-y}-2^{-1/2}\cos(\theta+y+\pi/4),
\qquad y_*(\theta)=\min\{y\in\mathbb R:B_\theta(y)=0\}.
\]
The minimum exists. Define the unique exceptional phase
\[
\theta_*=-\log(2\sqrt\pi)\pmod{2\pi}.
\]
If \(L_j\to\infty\), \(\theta_{L_j}\to\theta\not\equiv\theta_*\), then
\[
\boxed{L_j(\xi_1(L_j)-2L_j)-\log L_j\longrightarrow y_*(\theta).}
\]
Every zero of \(B_\theta\) is simple when \(\theta\ne\theta_*\). At the exceptional phase there is a double tangency at \(y_c=\log(2\sqrt\pi)\), which is its first zero; no assertion about the actual first-zero limit along exceptional-phase sequences is made.

**Fixed-cutoff density.** For each \(L>0\), the large positive real zeros of \(F_L\) are simple, one near each sufficiently large \(n\pi/L\), and their counting function \(N_L(R)\), defined as the number of positive real zeros in \((0,R]\) counted with analytic multiplicity, obeys
\[
N_L(R)=\frac{L}{\pi}R+O_L(1)\qquad(R\to\infty).
\]

## Assumptions and scope
The transform convention is \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-i\xi x}\,dx\). Cutoff \(L\) is a positive real parameter; no integer or lattice restriction is imposed. The first-zero and boundary-layer conclusions are large-\(L\) statements. The fixed-cutoff count holds for each \(L>0\). The phase subsequence statement excludes only the explicitly stated exceptional phase, not a positive-measure set of phases.

## Proof
**1. Exact tail representation and a uniform endpoint estimate.** Completing the square gives
\[
F_L(\xi)=\sqrt\pi e^{-\xi^2/4}-2\operatorname{Re}\int_L^\infty e^{-x^2+i\xi x}\,dx
=\sqrt\pi e^{-\xi^2/4}\operatorname{Re}\operatorname{erf}(L+i\xi/2).
\]
Substitute \(x=L+v/L\) in the half-line tail. For all real \(\xi\),
\[
\int_L^\infty e^{-x^2+i\xi x}\,dx
=\frac{e^{-L^2+iL\xi}}L\left[\frac1{2-i\xi/L}+E_L(\xi)\right],
\]
where
\[
E_L(\xi)=\int_0^\infty e^{-(2-i\xi/L)v}(e^{-v^2/L^2}-1)\,dv.
\]
Since \(|1-e^{-u}|\le u\) for \(u\ge0\),
\[
|E_L(\xi)|\le L^{-2}\int_0^\infty v^2e^{-2v}\,dv=\frac1{4L^2}.
\]
This bound is uniform in the entire real frequency line. Differentiating the integral under the sign, \(|\partial_\xi E_L(\xi)|\le L^{-3}\int_0^\infty v^3e^{-2v}\,dv\), which also controls the rescaled derivative used below.

**2. Emergence scale of the first zero.** Write \(\xi=2L+(\log L+y)/L\). Completing the square exactly,
\[
\frac{\xi^2}4=L^2+\log L+y+\frac{(\log L+y)^2}{4L^2}.
\]
In the tail approximation, \(\xi/L=2+(\log L+y)/L^2\). Consequently, using
\(2/(2-2i)=2^{-1/2}e^{i\pi/4}\), the claimed compact-uniform expansion for \(B_{\theta_L}\) follows. Differentiating the explicit two terms and the dominated integral gives the stated \(C^1\) version.

For a global lower bound, \(|\int_L^\infty e^{-x^2+i\xi x}\,dx|\le e^{-L^2}/(2L)\); hence
\[
F_L(\xi)\ge\sqrt\pi e^{-\xi^2/4}-\frac{e^{-L^2}}L.
\]
This is strictly positive simultaneously for \(0\le\xi\le 2L+(\log L-2)/L\), once \(L\) is sufficiently large. For the upper bound, take \(y\in[4,4+2\pi]\) so that \(\cos(\theta_L+y+\pi/4)=1\). At \(\xi=2L+(\log L+y)/L\), the scaled expansion gives
\(L e^{L^2}F_L(\xi)=\sqrt\pi e^{-y}-2^{-1/2}+o(1)<0\).
Because \(F_L(0)>0\), at least one first positive zero exists in the resulting bounded rescaled interval. This proves the logarithmic law.

**3. Phase-resolved first zeros and exceptional tangency.** For each phase, \(B_\theta(y)>0\) at all sufficiently negative \(y\). For arbitrarily large \(y\), it is negative at phases where the cosine equals one. Thus a smallest zero exists. If \(B_\theta(y)=B_\theta'(y)=0\), then
\[
\cos(\theta+y+\pi/4)=\sin(\theta+y+\pi/4)=\sqrt{2\pi}\,e^{-y}>0.
\]
These equations force \(y=y_c=\log(2\sqrt\pi)\) and \(\theta=\theta_*\) modulo \(2\pi\). Moreover \(B_{\theta_*}''(y_c)=1>0\). To see that this tangency is the first zero at the exceptional phase, write \(u=y_c-y>0\) and note
\[
2B_{\theta_*}(y)=e^u-\cos u-\sin u>0,
\]
using \(e^u>1+u\ge\cos u+\sin u\). Thus for all other phases every zero is simple. If \(\theta_{L_j}\to\theta\ne\theta_*\), compact \(C^1\) convergence to \(B_\theta\), positivity to the left of its first simple zero, and the opposite signs across that zero give convergence of the first rescaled zeros as asserted. No multiplicity or sign-change assertion is made at the exceptional tangency.

**4. Fixed-cutoff infinite zero strings.** Integration by parts yields
\[
\xi F_L(\xi)=2e^{-L^2}\sin(L\xi)
+4\int_0^L x e^{-x^2}\sin(\xi x)\,dx.
\]
For fixed \(L>0\), another integration by parts gives \(\xi F_L(\xi)=2e^{-L^2}\sin(L\xi)+O_L(\xi^{-1})\). Differentiating this identity and integrating by parts once more gives
\[
(\xi F_L(\xi))'=2L e^{-L^2}\cos(L\xi)+O_L(\xi^{-1}).
\]
Choose any fixed \(0<\delta<\pi/(2L)\). Outside the \(\delta\)-neighborhoods of \(n\pi/L\), the sine term excludes all sufficiently large zeros. On each such neighborhood the cosine derivative has fixed nonzero sign for sufficiently large \(n\), and the sine signs at the endpoints are opposite. Hence exactly one simple zero occurs near each sufficiently large \(n\pi/L\), proving the count and simplicity.

## Verification
The companion `check.py` evaluates the exact error-function expression at high precision, compares it with direct quadrature, finds the first zeros at four cutoffs, checks the compact-window phase approximation, and follows a sequence of cutoffs satisfying \(2L^2+\log L=2\pi n\) toward the predicted first-zero phase limit. The numerical tests reproduce all predicted trends; they are not used as proof of the asymptotic theorem. The proof uses only Gaussian integration, an explicit uniformly controlled Laplace-tail remainder, and elementary real-zero arguments.

## Relationship to prior work
The Gaussian transform and finite normal characteristic function are classical. Csordas (2013) studies Fourier-transform zero conditions for positive definite kernels and Laguerre inequalities, but the inspected full text does not analyze hard-cutoff Gaussian first-real-zero onset. Tallis (1961) gives truncated-normal moment-generating-function formulas; its accessible abstract supports that background, but the full text was not available in this inspection. Ross, Fiddy and Nieto-Vesperinas (1980) discuss zeros of finite Fourier transforms and illustrate a truncated Gaussian in an inverse-scattering setting; only partial text was accessible, so possible stronger treatment is a residual priority risk. Lonke (2021) proves positivity of \(\operatorname{Re}\operatorname{erf}(z)\) in a sector, which already implies the zero-free bound \(|\xi|\le2L\). Its displayed error-function estimate can also imply portions of a quantitative lower bound just beyond that sector. The distinctive assertion here is the **matching first-zero upper bound, exact logarithmic scale, explicit oscillatory boundary-layer profile, and phase-selected root limit**; these do not follow from sector positivity alone. The DLMF error-function zero tables concern zeros of the entire \(\operatorname{erf}\) function, not zeros of its real part on moving vertical lines.

## Limitations
The error constant in the first-zero law is not made optimal. The phase limit deliberately excludes sequences approaching the one exceptional double-tangency phase; their first-zero behavior may require finer-order analysis. Fixed-cutoff zero strings are only eventually classified. No claim is made about all complex zeros or the entire finite-cutoff real-zero spectrum. Earlier unindexed asymptotic work on finite Gaussian Fourier transforms could have equivalent coverage; novelty has not been independently certified.

## References
- G. Csordas, *Fourier transforms of positive definite kernels and the Riemann \(\xi\)-Function*, arXiv:1309.0055v1, first posted 2013-08-31, https://arxiv.org/abs/1309.0055 .
- Y. Lonke, *The real part of the complementary error function*, arXiv:2101.07369, first posted 2021-01-15, https://arxiv.org/abs/2101.07369 .
- G. M. Tallis, *The Moment Generating Function of the Truncated Multi-Normal Distribution*, J. R. Stat. Soc. Ser. B 23 (1961), 223–229, https://doi.org/10.1111/j.2517-6161.1961.tb00408.x .
- G. Ross, M. A. Fiddy and M. Nieto-Vesperinas, *The Inverse Scattering Problem in Structural Determinations*, chapter (1980), https://doi.org/10.1007/978-3-642-81472-3_2 .
- NIST Digital Library of Mathematical Functions, Section 7.13, *Zeros of error functions*, https://dlmf.nist.gov/7.13 .
