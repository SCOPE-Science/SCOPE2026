# Bessel concavity and the uniform continuum profile of optimally smooth discrete averages

## Finding

Let \(u_n:\{-n,\ldots,n\}\to\mathbb R\) be the unique normalized real convolution kernel minimizing the \(\ell^2(\mathbb Z)\)-operator norm of the second-difference smoother, as constructed in Richardson [1]. Put \(N=n+1\), \(m=\pi/2\), and define the even function \(K:\mathbb R\to\mathbb R\) by \(K(s)=0\) for \(|s|\ge1\) and, for \(0\le s<1\),
\[
 h(r)=\begin{cases}\displaystyle\frac{mJ_1(m\sqrt{1-r^2})}{\sqrt{1-r^2}},&0\le r<1,\\[4pt]m^2/2,&r=1,\end{cases}
 \qquad K(s)=\frac\pi2\int_s^1\left(\int_0^v h(r)\,dr\right)dv.
\]
Here \(J_1\) is the ordinary Bessel function of the first kind. Then the entire discrete coefficient profile converges uniformly:
\[
 \boxed{\lim_{n\to\infty}\max_{|k|\le n}\left|(n+1)u_n(k)-K\!\left(\frac{k}{n+1}\right)\right|=0.}
\]
The limiting profile is a compactly supported probability density, is strictly positive on \((-1,1)\), strictly decreases on \((0,1)\), and is strictly concave on \((-1,1)\). Its Fourier transform (with the convention \(\widehat K(t)=\int_{\mathbb R}K(s)e^{-its}\,ds\)) is
\[
 \boxed{\widehat K(t)=\begin{cases}-\pi\cos\!\sqrt{t^2+\pi^2/4}/t^2,&t\ne0,\\1,&t=0.\end{cases}}
\]
In particular \(K(0)=0.741417775971\ldots\), and \(K'(1^-)=-\pi/2\). Thus the limit is not the Epanechnikov parabola \(3(1-s^2)/4\), although the two profiles are close. For each fixed \(\delta\in(0,1)\), the coefficients \(u_n(k)\) are positive for all sufficiently large \(n\) whenever \(|k|\le(1-\delta)(n+1)\). No assertion is made here about positivity at every finite-radius endpoint coefficient.

## Assumptions and scope

All integers \(n\ge1\) are considered, and \(u_n\) is the real, even, normalized, support-radius-\(n\) optimizer of the unconstrained (not Fourier-positive constrained) second-difference problem. The discrete second difference may be taken as \(\Delta f(j)=f(j+2)-2f(j+1)+f(j)\); its Fourier multiplier modulus is independent of the translation convention. The source's exact finite-radius optimizer formula is used as an established theorem [1]; the continuum limit, Bessel representation, uniformity and shape statements are derived below.

## Proof

**1. Exact polynomial and scaling.** Write \(\theta_N=\pi/(2N)\), \(c_N=\cos\theta_N\), \(a_N=(1+c_N)/2\), and \(A_N=2\sin\theta_N/[N(1+c_N)]\). If \(T_N\) is the first-kind Chebyshev polynomial, Richardson's formula [1, equations (3)--(4)] identifies the Fourier symbol of \(u_n\) as
\[
 S_n(x)=\frac{A_NT_N(a_N(x+1)-1)}{x-1},\qquad
 S_n(\cos\xi)=\sum_{k=-n}^nu_n(k)e^{ik\xi}.
\]
The apparent singularity at \(x=1\) is removable because \(T_N(c_N)=0\), while \(A_Na_NT_N'(c_N)=1\), so \(S_n(1)=1\). For fixed real \(t\), the argument of \(T_N\) at \(x=\cos(t/N)\) is
\[
 a_N(1+\cos(t/N))-1
 =1-\frac{t^2+m^2}{2N^2}+o(N^{-2}).
\]
As \(T_N(\cos\xi)=\cos(N\xi)\), \(N^2A_N\to\pi/2\) and \(N^2(\cos(t/N)-1)\to-t^2/2\), it follows that
\[
 S_n(\cos(t/N))\to F(t):=-\frac{\pi\cos\sqrt{t^2+m^2}}{t^2}
\]
for \(t\ne0\); at zero \(S_n(1)=1=F(0)\), since \(m=\pi/2\).

**2. An integrable uniform majorant.** Let \(H_N(t)=S_n(\cos(t/N))\) on \([-\pi N,\pi N]\) and zero elsewhere. For \(x\in[-1,1]\), both \(x\) and \(a_N(x+1)-1\) lie in \([-1,1]\), and \(T_N(c_N)=0\). The Chebyshev bounds \(|T_N|\le1\), \(\max_{[-1,1]}|T_N'|\le N^2\), combined with \(A_N=O(N^{-2})\), show \(|S_n(x)|\le A_Na_NN^2=O(1)\). On \(1\le|t|\le\pi N\), the direct numerator bound and \(1-\cos(t/N)\ge2t^2/(\pi^2N^2)\) show \(|H_N(t)|\le C/t^2\). Therefore \(|H_N(t)|\le C/(1+t^2)\) uniformly, and dominated convergence yields \(\|H_N-F\|_{L^1(\mathbb R)}\to0\).

**3. Compactly supported inverse transform.** For arbitrary real \(t\) and \(a>0\) the elementary Fourier--Bessel identity is
\[
 \frac12\int_{-a}^a e^{-its}J_0(m\sqrt{a^2-s^2})\,ds
 =\frac{\sin(a\sqrt{t^2+m^2})}{\sqrt{t^2+m^2}}.
\]
For completeness, expand \(J_0\) and \(\cos(ts)\) in absolutely convergent power series and integrate \(s^{2k}(a^2-s^2)^j\) by the beta integral. The coefficient of \(a^{2r+1}\) is \((-1)^r(t^2+m^2)^r/(2r+1)!\), giving the right side. Differentiating this identity with respect to \(a\) at \(a=1\), in the distributional sense, gives the inverse Fourier representation
\[
 \cos\sqrt{t^2+m^2}
 =\mathcal F\!\left(\frac{\delta_{-1}+\delta_1}{2}-\frac12h(s)\mathbf1_{(-1,1)}(s)\right)(t).
\]
At \(t=0\), \(\cos m=0\) implies \(\int_0^1h(s)\,ds=1\). From the definition of \(K\), \(K(1)=0\), \(K'(1^-)=-\pi/2\), \(K'(0)=0\), and \(K''(s)=-\pi h(s)/2\) for \(|s|<1\). The exterior derivative is zero, so the full distributional second derivative is
\[
 K''=\frac\pi2(\delta_{-1}+\delta_1)-\frac\pi2h(s)\mathbf1_{(-1,1)}(s).
\]
Consequently \(-t^2\widehat K(t)=\pi\cos\sqrt{t^2+m^2}\). For \(t\ne0\) this gives \(\widehat K(t)=F(t)\), and continuity at \(t=0\) gives \(\widehat K(0)=\lim_{t\to0}F(t)=1\). In particular \(\int_{-1}^1K(s)\,ds=1\).

**4. Uniform coefficient convergence.** Fourier inversion for the finite trigonometric polynomial gives
\[
 N u_n(k)=\frac1{2\pi}\int_{-\pi N}^{\pi N}S_n(\cos(t/N))e^{-i(k/N)t}\,dt.
\]
Inversion for \(K\), and the \(L^1\)-convergence above, yield for every integer \(|k|\le n\)
\[
 \left|Nu_n(k)-K(k/N)\right|\le\frac1{2\pi}\|H_N-F\|_{L^1(\mathbb R)}\to0,
\]
with a bound independent of \(k\), proving the asserted uniform limit.

**5. Shape and bulk positivity.** For \(z\in(0,\pi/2]\), the alternating series for \(J_1(z)\) has decreasing term magnitudes and its first two terms sum to \((z/2)(1-z^2/8)>0\). Hence \(h(s)>0\) for \(0\le s\le1\). It follows directly that \(K(s)>0\) for \(0\le s<1\), \(K'(s)=-(\pi/2)\int_0^s h(r)\,dr<0\) for \(0<s<1\), and \(K''(s)=-(\pi/2)h(s)<0\) for \(|s|<1\). Evenness extends the result to negative \(s\). Uniform convergence and the positive minimum of \(K\) on \([-1+\delta,1-\delta]\) give the stated eventual positivity of every corresponding discrete coefficient. Evaluating the defining integral gives the displayed central height numerically; this decimal is supplementary, not needed for the proof.

## Verification

The accompanying `research26_checker.py` reconstructs the finite-radius coefficients by a cosine transform of the exact Chebyshev polynomial, verifies normalization, compares sampled profiles at radii from \(8\) through \(256\), checks the continuum integral Fourier transform at ten frequencies, and numerically checks mass and monotonicity. It completed 535 numerical assertions. The analytic argument, not any finite numerical test, establishes the uniform-in-radius limit and strict concavity for all \(s\in(-1,1)\). Reproduction requires Python 3, NumPy and SciPy: `python research26_checker.py`.

## Relationship to prior work

Richardson [1] proves uniqueness and the complete finite-radius Chebyshev expression for the minimizing smoothing kernel, its optimal Fourier norm, and a comparison with the parabolic Epanechnikov sampler. Those facts are assumed and explicitly credited here. Neither the Fourier--Bessel limit, the uniform all-index coefficient asymptotic, nor strict concavity of the resulting compact support density is stated as a theorem in the inspected source. Kravitz and Steinerberger [2] analyze first differences, the *Fourier-nonnegative-constrained* second-difference case, and a continuous triangle kernel. That is a different admissible class; their triangle density is not this signed-multiplier optimum. The new conclusions here are the spatial continuum classification and its global all-index convergence, not re-proofs of the known finite-dimensional extremal formula.

## Limitations

This theorem concerns the unique real unconstrained second-difference minimizer in one dimension. It does not determine a convergence rate, prove positivity of every finite-radius endpoint coefficient, or address other difference orders or multidimensional smoothers. The leading finite-radius optimizer is taken from [1], and historical priority for the new continuum representation is not established exhaustively. No independent validation has occurred.

## References

[1] Sean Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713 (first made public 2023-10-15), https://arxiv.org/html/2310.09713v1, especially Theorem 1 and equations (3)--(4), Sections 2.1--2.2 and 3.4.

[2] Noah Kravitz and Stefan Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, arXiv:2007.13700 (first made public 2020-07-27), https://arxiv.org/abs/2007.13700, especially Sections 1.2 and 1.4.
