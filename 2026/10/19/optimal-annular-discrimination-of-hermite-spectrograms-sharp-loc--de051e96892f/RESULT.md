# Optimal annular discrimination of Hermite spectrograms: sharp local stability and Gaussian crossover

## Finding

Fix any integers \(0\le n<m\) and any prescribed planar area \(A>0\). Among all Lebesgue-measurable phase-space regions \(\Omega\subset\mathbb R^2\) of area \(A\), the contrast between the Gaussian-window short-time Fourier energies of the normalized Hermite functions \(h_m\) and \(h_n\) has a **unique maximizer up to null sets**: a centered annulus. Its inner and outer squared radii are the unique pair \(a,a+A\) satisfying
\[
 a>\left(\frac{m!}{n!}\right)^{1/(m-n)},\qquad
 e^{-a}\left(\frac{a^m}{m!}-\frac{a^n}{n!}\right)
 = e^{-(a+A)}\left(\frac{(a+A)^m}{m!}-\frac{(a+A)^n}{n!}\right).
\]
The annulus is \(\Omega_* =\{(x,\xi): a<\pi(x^2+\xi^2)<a+A\}\). Write \(g(t)=e^{-t}(t^m/m!-t^n/n!)\), \(b=a+A\), \(p=g'(a)>0\), \(q=-g'(b)>0\). For \(\Delta=\sup_{|\Omega|=A}\int_\Omega(|V_\varphi h_m|^2-|V_\varphi h_n|^2)\,dx\,d\xi\), the exact infinitesimal stability constant is
\[
 \lim_{\varepsilon\downarrow0}\;\inf_{\substack{|\Omega|=A\\|\Omega\triangle\Omega_*|=\varepsilon}}
 \frac{\Delta-\int_\Omega(|V_\varphi h_m|^2-|V_\varphi h_n|^2)\,dx\,d\xi}{\varepsilon^2}
 =\frac{pq}{4(p+q)}.
\]
This coefficient is sharp against **all measurable, possibly nonradial** competitors. For consecutive degrees \(m=n+1\), the positive radial contrast density has its unique maximum exactly at \(t=n+1+\sqrt{n+1}\).

A two-scale high-degree limit follows. Let \(N=n+1\to\infty\), \(A_n=s\sqrt N\) with fixed \(s>0\), and \(m_n>n\). If \((m_n-n)/\sqrt N\to c>0\), then
\[
 \frac{a_n-N}{\sqrt N}\to\alpha_{c,s},\quad
 \Delta_{n,m_n}(s\sqrt N)\to
 \int_{\alpha_{c,s}}^{\alpha_{c,s}+s}
       [\varphi_0(u-c)-\varphi_0(u)]\,du,
\]
where \(\varphi_0(u)=e^{-u^2/2}/\sqrt{2\pi}\) and \(\alpha_{c,s}>c/2\) uniquely solves
\(\varphi_0(\alpha_{c,s}-c)-\varphi_0(\alpha_{c,s})
=\varphi_0(\alpha_{c,s}+s-c)-\varphi_0(\alpha_{c,s}+s)\).
If instead \(k=m_n-n\ge1\) is **fixed**, then \((a_n-N)/\sqrt N\to\beta_s>0\), the unique solution of
\(\beta_s\varphi_0(\beta_s)=(\beta_s+s)\varphi_0(\beta_s+s)\), and
\[
 \lim_{n\to\infty}\frac{\sqrt{n+1}}{k}\Delta_{n,n+k}(s\sqrt{n+1})
 =\varphi_0(\beta_s)-\varphi_0(\beta_s+s).
\]
Thus gaps of order \(\sqrt n\) admit a nonzero limiting contrast, whereas fixed gaps have the sharp \(n^{-1/2}\) resolution scale.

## Assumptions and scope

The normalized Gaussian window is \(\varphi(x)=2^{1/4}e^{-\pi x^2}\); the short-time Fourier transform is
\(V_\varphi f(x,\xi)=\int_\mathbb R f(t)\overline{\varphi(t-x)}e^{-2\pi i\xi t}\,dt\).
Normalize Hermite functions so that their Bargmann transforms are the unit Fock monomials \((\pi^j/j!)^{1/2}z^j\). Hence, with \(t=\pi(x^2+\xi^2)\),
\[
 |V_\varphi h_j(x,\xi)|^2=e^{-t}t^j/j!,\qquad j\ge0.
\]
Every measurable \(\Omega\) with finite area \(A\) is admissible; no connectedness, boundedness, regularity, or radiality is assumed. Physical phase-space area is \(dx\,d\xi\). The variable \(t=\pi|z|^2\) has full-angular area measure \(dt\): a radial shell \(a<t<b\) has area \(b-a\). The stability limit is at fixed \(n,m,A\); its error constants are not claimed uniform in high-degree parameters.

We optimize **a difference of two fixed diagonal Rayleigh quotients** of the Gaussian localization operator, not its largest eigenvalue over all signals. The limit \(c>0\) and \(s>0\) are held fixed; the fixed-degree-gap limit is stated separately.

## Proof

**1. Radial contrast and one sign change.** By the Bargmann–STFT identity above,
\[
 \mathcal D_{n,m}(\Omega):=\int_\Omega(|V_\varphi h_m|^2-|V_\varphi h_n|^2)
   =\int_\Omega g(\pi|z|^2)\,dA(z),
 \qquad g(t)=\frac{e^{-t}t^n}{m!}(t^{m-n}-Q),\quad Q=m!/n!.
\]
Write \(k=m-n\) and \(t_0=Q^{1/k}\). Then \(g(t)<0\) for \(0<t<t_0\) and \(g(t)>0\) for \(t>t_0\). On \(t>t_0\),
\[
 (\log g)''(t)=-\frac n{t^2}
 -\frac{k t^{k-2}[t^k+(k-1)Q]}{(t^k-Q)^2}<0.
\]
(The first summand vanishes when \(n=0\), but the second is strictly negative.) Moreover, \(g(t_0)=0\) and \(g(t)\to0\) as \(t\to\infty\). Thus \(g\) has exactly one positive maximizer \(t_*\), with strictly increasing branch \((t_0,t_*)\) and strictly decreasing branch \((t_*,\infty)\).

**2. Unique area-constrained annulus.** For \(A>0\), let
\(F_A(a)=\log g(a)-\log g(a+A)\) on \(a>t_0\). Strict concavity gives \(F_A'(a)>0\); also \(F_A(a)\to-\infty\) as \(a\downarrow t_0\), and \(F_A(a)\to A>0\) as \(a\to\infty\). Thus there is exactly one \(a\) with \(g(a)=g(a+A)=:\lambda>0\), necessarily \(a<t_*<a+A\). Strict unimodality implies
\(\{t:g(t)>\lambda\}=(a,a+A)\).
The planar superlevel set of \(z\mapsto g(\pi|z|^2)\) is precisely the stated annulus and has area \(A\). For any other set \(\Omega\) with \(|\Omega|=A\),
\[
 \mathcal D_{n,m}(\Omega_*)-\mathcal D_{n,m}(\Omega)
 =\int_{\Omega_*\setminus\Omega}(g-\lambda)\,dA
  +\int_{\Omega\setminus\Omega_*}(\lambda-g)\,dA\ge0.
\]
Both integrands are strictly positive away from the two zero-area boundary circles, so equality holds only for \(\Omega=\Omega_*\) almost everywhere. For the exact maximum, setting \(Q_j(t)=\Gamma(j+1,t)/j!\) (the upper regularized incomplete Gamma function),
\[
 \Delta_{n,m}(A)
 =Q_m(a)-Q_m(a+A)-Q_n(a)+Q_n(a+A).
\]
For \(k=1\), \(g(t)=e^{-t}t^n(t-(n+1))/(n+1)!\), and direct differentiation shows \(g'(t)=0\) on its positive branch exactly at \(t=n+1+\sqrt{n+1}\).

**3. Sharp symmetric-difference stability.** Define \(p=g'(a)>0\), \(q=-g'(b)>0\), \(b=a+A\), \(S=p^{-1}+q^{-1}\). If \(|\Omega\triangle\Omega_*|=\varepsilon\) and \(|\Omega|=|\Omega_*|\), the removed and added areas both equal \(r=\varepsilon/2\). In the radial area variable \(t\), the distribution functions of \(g-\lambda\) **inside** the annulus and \(\lambda-g\) **outside** it obey, as \(y\downarrow0\),
\[
 |\{z\in\Omega_*:0<g(\pi|z|^2)-\lambda<y\}|
 =Sy+O(y^2),\qquad
 |\{z\notin\Omega_*:0<\lambda-g(\pi|z|^2)<y\}|
 =Sy+O(y^2).
\]
Indeed, each boundary circle contributes a collar of radial area \(y/p+O(y^2)\) or \(y/q+O(y^2)\). The only zero-level points are those two circles, and away from them the contrast is separated from \(\lambda\). For any measurable removed mass \(r\), the minimum integral of its nonnegative cost function is the integral of the lowest \(r\) quantiles. Inverting \(Sy+O(y^2)\) shows that the sharp cost for removal is \(r^2/(2S)+O(r^3)\); the sharp cost for addition is the same. Consequently,
\[
 \inf_{\substack{|\Omega|=A\\|\Omega\triangle\Omega_*|=\varepsilon}}
 (\Delta_{n,m}(A)-\mathcal D_{n,m}(\Omega))
 =\frac{\varepsilon^2}{4S}+O(\varepsilon^3).
\]
The infimum and coefficient are attained to this order by exchanging **full-angular radial collars** of total area \(r\) around both sides of each boundary, with mass proportions \(p^{-1}:q^{-1}\). This proves sharpness even within radial competitors, hence over the full measurable class. Notice \(1/(4S)=pq/[4(p+q)]>0\).

**4. Gaussian gap crossover.** Put \(N=n+1\), \(p_j(t)=e^{-t}t^j/j!\). Stirling's formula, with uniform remainder on compact subsets of \(u\in\mathbb R\), gives
\[
 \sqrt N\,p_n(N+\sqrt N\,u)\longrightarrow\varphi_0(u).
\]
If \(k_n=m_n-n\) satisfies \(k_n/\sqrt N\to c>0\), the gamma shape \(m_n+1=N+k_n\) has mean shifted by \(c\sqrt N+o(\sqrt N)\), whence
\[
 \sqrt N\,g_{n,m_n}(N+\sqrt N\,u)
 \longrightarrow h_c(u):=\varphi_0(u-c)-\varphi_0(u)
\]
locally uniformly. On \(u>c/2\),
\(h_c(u)=\varphi_0(u-c)[1-e^{-c(u-c/2)}]\) is positive and strictly log-concave: differentiating its logarithm twice yields
\( -1-c^2 e^{c(u-c/2)}/(e^{c(u-c/2)}-1)^2<0\).
It therefore has one maximum and one unique equal-height interval \((\alpha_{c,s},\alpha_{c,s}+s)\) of length \(s\) above its positive threshold. Evaluating the prelimit equal-height equation at any two fixed values bracketing the limiting root, and using its strict monotonicity, proves \((a_n-N)/\sqrt N\to\alpha_{c,s}\). Integrating the local density limit over the moving interval proves the first claimed contrast limit.

If \(k=m_n-n\ge1\) is fixed, the exact ratio
\(p_{n+k}(t)/p_n(t)=t^k/[(n+1)\cdots(n+k)]\) gives the finer locally uniform expansion
\[
 \frac N{k}\,g_{n,n+k}(N+\sqrt N\,u)
 \longrightarrow u\varphi_0(u).
\]
The latter is positive and strictly log-concave on \(u>0\), since \((\log(u\varphi_0(u)))''=-u^{-2}-1\). Again the unique equal-height-root argument proves convergence of the endpoints to \(\beta_s\), and integration after rescaling gives
\(\sqrt N\Delta_{n,n+k}(s\sqrt N)/k\to\int_{\beta_s}^{\beta_s+s}u\varphi_0(u)\,du
=\varphi_0(\beta_s)-\varphi_0(\beta_s+s)\). This finishes all quantified statements.

## Verification

The included standalone `VERIFY.py` computes the exact annulus thresholds from the factorial ratio and equal-height condition, compares the Gamma-tail maximum with direct quadrature, tests strictly lower values on translated radial windows, checks the sharp local stability coefficient through explicit collar exchanges, and tests both high-degree scalings. It covers six degree pairs at four areas each and several asymptotic test families. Execute with `python VERIFY.py` using Python 3, NumPy and SciPy. The printed numerical checks are finite tests only; the arbitrary-parameter conclusions above follow from the analytic derivation.

## Relationship to prior work

Daubechies's diagonalization for radial Gaussian time-frequency localization already supplies \(\int_S e^{-t}t^j/j!\,dt\) for an individual Hermite eigenvalue. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I* (2020), reproduces this formula in Theorem 2.1 and in §3.1 studies **prescribed** unit-area rings and their eigenvalue ordering. These facts provide the foundational radial densities, not the optimization of the **difference** of two fixed levels over all measurable masks, its sharp symmetric-difference coefficient, or either double-scaling law.

Nicola–Tilli (arXiv:2106.03423) establishes the disk as the optimizer when **both the signal and mask** vary, by maximizing the first localization eigenvalue. Ramos (arXiv:2607.21590v1, July 23, 2026) develops inverse localization, Hermite rigidity and local/global first-eigenvalue maximization with Gaussian optimizers. Its bathtub argument involves the first eigenfunction, not the signed two-Hermite contrast treated here. Gómez–Guerra–Ramos–Tilli (arXiv:2307.09304) provides quantitative stability for the first-eigenvalue Faber–Krahn inequality, a different functional, optimizer family and comparison metric. The individual Poisson/Gamma formulas, rearrangement principle and Gaussian central limit tools are classical and are not claimed as discoveries; the precise composite all-pair contrast solution, sharp local coefficient and linked scaling transition constitute the present statement.

## Limitations

The objective measures the **difference of two specified diagonal Hermite responses**, not optimal binary quantum hypothesis testing, not minimum-error adaptive discrimination, not a full localization-operator eigengap, and not recovery of arbitrary signals. The optimizing annulus is centered at the fixed STFT origin. The local stability coefficient is an infinitesimal assertion for fixed degrees and area, not a uniform finite-distance estimate. The Gaussian crossover assumes either \(k/\sqrt N\to c>0\) or a fixed positive integer \(k\); intermediate regimes and explicit rates are not proved. The mathematical priority claim is provisional: an unindexed equivalent measure-optimization or two-state discrimination theorem cannot be excluded by finite literature searches, and independent scientific review has not been performed.

## References

1. J. P. G. Ramos, *Eigenfunctions, Free Boundaries, and Time-Frequency Localization*, arXiv:2607.21590v1 (first public July 23, 2026), https://arxiv.org/html/2607.21590v1.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, Journal of Fourier Analysis and Applications 26 (2020), article 47, https://doi.org/10.1007/s00041-020-09751-9, especially Theorem 2.1 and §3.1.
3. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, Inventiones Mathematicae (2022), https://doi.org/10.1007/s00222-022-01119-8; arXiv:2106.03423.
4. F. Gómez, D. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber-Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304 (2023), https://arxiv.org/abs/2307.09304.
5. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612, cited through [2] and [3].
