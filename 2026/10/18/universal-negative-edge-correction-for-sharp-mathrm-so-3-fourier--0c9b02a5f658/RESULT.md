# Universal negative edge correction for sharp \(\mathrm{SO}(3)\) Fourier cutoffs

## Finding
Let \(P_L\) be the canonical Peter–Weyl projection on \(G=\mathrm{SO}(3)\) retaining every irreducible representation of integral angular momentum \(0\le\ell\le L\), with normalized Haar measure. Its exact endpoint convolution norm \(\Lambda_L=\|P_L\|_{L^1\to L^1}=\|P_L\|_{L^\infty\to L^\infty}=\|P_L\|_{C(G)\to C(G)}\) has the **two-term asymptotic**
\[
\Lambda_L=\frac4\pi(L+1)+C_{\mathrm{rot}}+o(1),\qquad L\to\infty,
\]
where the universal constant is the convergent improper integral
\[
C_{\mathrm{rot}}=\frac2\pi\int_0^\infty\left(\left|\cos u-\frac{\sin u}{u}\right|-|\cos u|\right)\,du<0.
\]
The integral is understood as an ordinary improper integral of the displayed difference, not as the difference of two divergent integrals. A rapidly converging interval/root series given below evaluates it approximately as \(-0.10304\). This is an additive correction to the leading sharp amplification factor, not an operator-norm estimate with an unspecified remainder.

## Assumptions and scope
For a rotation with half-angle \(\theta\in[0,\pi]\) on the double cover \(\mathrm{SU}(2)\to\mathrm{SO}(3)\), the integer-spin character is \(\chi_\ell(\theta)=\sin((2\ell+1)\theta)/\sin\theta\), extended continuously at the endpoints. Normalized Haar integration of such class functions is \((2/\pi)\int_0^\pi f(\theta)\sin^2\theta\,d\theta\). The central convolution kernel of \(P_L\) is \(K_L=\sum_{\ell=0}^L(2\ell+1)\chi_\ell\). No centrality restriction is placed on input functions. The conclusion is for the unfiltered **contiguous integer-spin** cutoff, not for arbitrary spectral masks, Cesàro means, or the full half-integer spectrum on \(\mathrm{SU}(2)\).

## Proof
**1. Exact norm reduction.** Convolution by \(K_L\) has endpoint norms equal to \(\|K_L\|_{L^1(G)}\), by the convolution bound and approximation of the kernel sign at the identity (for \(C(G)\) and \(L^\infty\)), or of an identity mass (for \(L^1\)). Put \(m=L+1\). Differentiate the elementary identity
\[
\sum_{\ell=0}^{m-1}\cos((2\ell+1)\theta)=\frac{\sin(2m\theta)}{2\sin\theta}
\]
to obtain
\[
K_L(\theta)\sin^2\theta=-m\cos(2m\theta)+\tfrac12\cot\theta\sin(2m\theta).
\]
The absolute value is invariant under \(\theta\mapsto\pi-\theta\). Hence exactly
\[
\Lambda_L=\frac4\pi\int_0^{\pi/2}\left|m\cos(2m\theta)-\tfrac12\cot\theta\sin(2m\theta)\right|\,d\theta.
\]
Also \(\int_0^\pi|\cos(2m\theta)|\,d\theta=2\) for every integer \(m\ge1\). With \(u=2m\theta\), subtracting the resulting \(4m/\pi\) gives the **exact finite-band deficit**
\[
\Lambda_L-\frac{4m}{\pi}=\frac2\pi\int_0^{m\pi}\left(\left|\cos u-b_m(u)\sin u\right|-|\cos u|\right)\,du,
\quad b_m(u)=\frac1{2m}\cot\!\left(\frac{u}{2m}\right).
\]
The integrand extends continuously to \(u=0\) by its limiting value.

**2. Uniform oscillatory tails.** For \(0<u<m\pi\), \(b_m\) is nonnegative and decreasing, and \(0\le b_m(u)\le 1/u\). Let \(h(u)=\sin u\,\mathrm{sgn}(\cos u)\), a periodic mean-zero function with a bounded primitive \(-|\cos u|\). For every \(R\ge10\) and every nonnegative decreasing \(b\le1/u\), integration by parts gives
\[
\left|\int_R^T b(u)h(u)\,du\right|\le \frac{C}{R}.
\]
The difference between \(|\cos u-b(u)\sin u|-|\cos u|\) and \(-b(u)h(u)\) is bounded by \(2b(u)|\sin u|\,\mathbf1_{\{|\cos u|\le b(u)|\sin u|\}}\). On each period beyond \(R\), the exceptional set has length \(O(1/u)\), so the integrated error is \(O(1/R)\), uniformly in \(m\) and \(T\le m\pi\). The same statements hold for \(b(u)=1/u\). For fixed \(u>0\), \(b_m(u)\to1/u\); on bounded intervals dominated convergence applies (the product \(b_m(u)\sin u\) is bounded near zero). Uniform tail control therefore proves the asserted improper-integral limit and the two-term asymptotic without exchanging divergent absolute integrals.

**3. A strictly negative and computable constant.** Put \(F(u)=\sin u-\operatorname{Si}(u)\), where \(\operatorname{Si}(u)=\int_0^u(\sin t)/t\,dt\), so \(F'(u)=\cos u-\sin u/u\). Split the improper integral into periods \([k\pi,(k+1)\pi]\). The first period contributes \(J_0=\operatorname{Si}(\pi)-2<0\): indeed the alternating Taylor bound \(\sin u/u\le1-u^2/6+u^4/120\) on \([0,\pi]\) yields \(\operatorname{Si}(\pi)\le\pi-\pi^3/18+\pi^5/600<2\).

For \(k\ge1\), write \(a=k\pi\). The function \(g_a(t)=\cos t-\sin t/(a+t)\) has exactly one zero \(t_0\in(\pi/4,\pi/2)\), since \(\tan t=a+t\) has precisely one solution in \((0,\pi/2)\). Let \(B=a+\pi/2\) and \(q=1/(a+t_0)\). Relative to the sign of \(\cos t\), its absolute integral defect is \(J_k=-T_a+E_a\), where
\[
T_a=\int_0^{\pi/2}\frac{(\pi-2t)\sin t}{(a+t)(a+\pi-t)}\,dt\ge\frac{\pi-2}{B^2}
\]
and
\[
0<E_a=2\int_{t_0}^{\pi/2}\left(\frac{\sin t}{a+t}-\cos t\right)dt
\le2(\sqrt{1+q^2}-1)<q^2.
\]
Writing \(\delta=\pi/2-t_0=\arctan q\), we have \(\delta<q<1/(a+\pi/4)\), hence
\[
q^2<\frac1{B^2}\left(1-\frac1{B(a+\pi/4)}\right)^{-2}
\le\frac1{B^2}\left(1-\frac8{15\pi^2}\right)^{-2}<\frac{\pi-2}{B^2}.
\]
The last strict numerical inequality is elementary, for instance from the rational bound \(\pi>157/50\). Thus **every** \(J_k\) is strictly negative. Taylor expansion in \(1/a\) gives \(T_a=(\pi-2)/a^2+O(a^{-3})\), \(E_a=a^{-2}+O(a^{-3})\), whence \(J_k=(3-\pi)/(k^2\pi^2)+O(k^{-3})\). In particular, the interval series converges absolutely and the limiting constant is strictly negative.

For numerical evaluation, let \(r_k\in(k\pi,k\pi+\pi/2)\) be the unique positive root of \(\tan r_k=r_k\). Then the exact series is
\[
C_{\mathrm{rot}}=\frac2\pi\left[\operatorname{Si}(\pi)-2+
\sum_{k=1}^{\infty}\left((-1)^k\{2F(r_k)-F(k\pi)-F((k+1)\pi)\}-2\right)\right].
\]
It converges at rate \(O(1/K)\) after \(K\) periods.

## Verification
The standalone `checker.py` independently computes the same finite-band norms by numerical quadrature of the absolute weighted-character kernel, checks the character-sum identity, and evaluates successive truncations of the root series. In those finite calculations, \(\Lambda_0=1\), the cases \(L=1,2,4,11\) match the closed form, and the root series approaches approximately \(-0.10304\). These numerical checks are corroboration only: the statements for all \(L\) and the existence/negativity of the limit are established by the preceding analysis.

## Relationship to prior work
Work on rotation-group Wigner Fourier transforms and sampling (McEwen et al., arXiv:1508.03101) motivates controlling the endpoint norm of the unfiltered cutoff; its sampling theorem does not furnish this two-term norm. Fan's study of Cesàro kernels on classical groups (1997) addresses summability and convergence thresholds with a different family of kernels, not the present contiguous Peter–Weyl projector's additive constant. The older character-norm and compact-group Fourier convergence literature studies related divergence phenomena but no identical two-term formula was established from available material. A published leading-order result for the full low-pass \(\mathrm{SU}(2)\) projector does not imply the present formula: the \(\mathrm{SO}(3)\) kernel retains only **even** highest weights in the double cover, and taking absolute values prevents recovering its norm from the norm of the full \(\mathrm{SU}(2)\) kernel.

## Limitations
The constant is expressed by a conditionally integrated *difference* (and an absolutely convergent series of period contributions), not by a claimed elementary closed form. The theorem concerns the full operator norm; it does not assert uniform convergence of individual Fourier series or a rate for the displayed \(o(1)\) remainder. The decimal is descriptive, not a rigorously interval-certified bound. The 1982 paper on compact-group character norms was not available in full text for statement-by-statement comparison; independent literature review remains appropriate.

## References
- J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris and Y. Wiaux, *A novel sampling theorem on the rotation group*, arXiv:1508.03101 (first public version 2015-08-13), https://arxiv.org/abs/1508.03101.
- D. Fan, *Cesàro kernels on classical groups*, J. Austral. Math. Soc. 63 (1997), 364–389, https://doi.org/10.1017/S1446788700000951.
- S. Giulini, P. M. Soardi and G. Travaglini, *Norms of characters and Fourier series on compact Lie groups*, J. Funct. Anal. 46 (1982), 88–101, https://doi.org/10.1016/0022-1236(82)90045-3.
- D. Fan, *Cesàro means of Fourier series on rotation groups*, Proc. Amer. Math. Soc. 123 (1995), 1105–1114, https://doi.org/10.2307/2160707.
