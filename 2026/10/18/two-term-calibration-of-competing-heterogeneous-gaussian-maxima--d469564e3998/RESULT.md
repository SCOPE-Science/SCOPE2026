# Two-term calibration of competing heterogeneous Gaussian maxima

## Finding

For fixed \(r>1\), \(C>0\), and real \(d,e\), let \(L=\log n\), \(h=(r-1)/2\), and, for all sufficiently large integers \(n\),
\[
m_n=\left\lfloor Cn^rL^{-h}\left(1+\frac{d\log L+e}{L}\right)\right\rfloor.
\]
Take two independent samples, \(m_n\) independent \(N(0,1)\) observations and \(n\) independent \(N(0,r)\) observations. Let \(P_n\) be the probability that the first sample has the larger maximum. Put
\[
A=\frac{C}{\sqrt r}(4\pi)^h,\quad
F=\int_0^\infty (1-e^{-Ay^r})e^{-y}\,dy,
\]
\[
H=\int_0^\infty Ay^r e^{-y-Ay^r}\,dy,\qquad
J=\int_0^\infty Ay^r\log y\,e^{-y-Ay^r}\,dy.
\]
Then \(H>0\), and the **second-order winning-probability expansion** is
\[
\boxed{
P_n=F+\frac{(d-h/2)H\log L+
\left(e-\tfrac h2\log(4\pi)+\tfrac12(r-r^{-1})\right)H-hJ}{L}
+O_{r,C,d,e}\!\left(\frac{(\log L)^2}{L^2}\right).}
\]
In particular, the uncorrected critical sample-size rule \(d=e=0\) has the systematic signed bias
\[
P_n-F\sim-\frac{r-1}{4}H\frac{\log\log n}{\log n}<0.
\]
There is a **unique calibration pair** in the displayed two-parameter family for which the full order-\(1/\log n\) correction vanishes:
\[
\boxed{d_* =\frac{r-1}{4},\qquad
 e_* =\frac{hJ}{H}+\frac h2\log(4\pi)-\frac12(r-r^{-1}).}
\]
For that pair, \(P_n=F+O_{r,C}((\log\log n)^2/(\log n)^2)\). Uniqueness means uniqueness among fixed real choices of \(d,e\) in this expansion, not uniqueness among arbitrary sequences of sample sizes.

## Assumptions and scope

All observations within and across the two groups are independent. The first group has variance \(1\), and the second has variance \(r>1\); both have zero mean. The constants \(r,C,d,e\) remain fixed as the integer \(n\) tends to infinity. The floor is literal; it affects the expansion only by a super-polynomially small term in \(1/\log n\), since \(m_n\) grows as a positive power of \(n\). The constants in the remainder may depend on these fixed parameters. The equivalence with the first-order Gumbel integral of Zhang–Miao–Mao follows from \(A=e^{r\kappa}\), the substitution \(z=Ay^r\), and integration by parts. The same limiting probability \(F\) is the first-order critical-scale winner probability in Zhang–Miao–Mao (2026); the new claim is the finite-size expansion and the unique two-term calibration.

## Proof

**1. An exact probability representation.** Write \(\bar\Phi(t)=1-\Phi(t)\), where \(\Phi\) is the standard normal distribution function. If \(T_n\) is the maximum of the \(n\) standard normal observations in the high-variance group *before* multiplying by \(\sqrt r\), the probability integral transform gives the exact density
\[
Y_n=n\bar\Phi(T_n),\qquad f_{Y_n}(y)=\left(1-\frac yn\right)^{n-1}\mathbf 1_{(0,n)}(y).
\]
Conditioning on \(Y_n=y\) and defining \(t_n(y)=\bar\Phi^{-1}(y/n)\), one has the exact identity
\[
P_n=\int_0^n\Big[1-\big(1-\bar\Phi(\sqrt r\,t_n(y))\big)^{m_n}\Big]
\left(1-\frac yn\right)^{n-1}\,dy.
\tag{1}
\]
There is no distributional approximation in (1).

**2. Uniform tail and quantile expansions.** Let \(B_n=[L^{-3},L^3]\). The total contribution from \(Y_n\notin B_n\) is at most
\[
\Pr(Y_n<L^{-3})+\Pr(Y_n>L^3)
\le L^{-3}+e^{-L^3},
\]
for sufficiently large \(n\), using its exact distribution. Throughout \(B_n\), the positive quantile satisfies the uniform relation
\[
t_n(y)^2=2L-2\log y-\log L-\log(4\pi)
+O\left(\frac{\log L}{L}\right),\tag{2}
\]
obtained by solving the two-term Gaussian Mills expansion
\[
\bar\Phi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}\,t}
\left(1-\frac1{t^2}+O(t^{-4})\right).
\]
The error in (2) is uniform since \(|\log y|\le3\log L\); in particular \(t_n(y)^2\asymp L\). The ratio of two Gaussian tails, again uniformly on \(B_n\), is
\[
\frac{\bar\Phi(\sqrt r\,t)}{\bar\Phi(t)^r}
=\frac{(\sqrt{2\pi}\,t)^{r-1}}{\sqrt r}
\left(1+\frac{r-r^{-1}}{t^2}+O(t^{-4})\right).\tag{3}
\]
Equation (3) follows by dividing the two Mills expansions: the Gaussian exponentials cancel *exactly*, and the first relative correction is \(r-r^{-1}\).

**3. The corrected Poisson intensity.** The floor in \(m_n\) contributes \(O(n^{-r}L^h)\) relative error. Substitute \(\bar\Phi(t_n(y))=y/n\) into (3), then use (2) and the prescribed sample size. Writing \(u(y)=Ay^r\), the resulting intensity is uniformly on \(B_n\)
\[
\begin{aligned}
R_n(y)&=m_n\bar\Phi(\sqrt r\,t_n(y))\\
&=u(y)\left(1+\frac{(d-h/2)\log L+e-h\log y-
(h/2)\log(4\pi)+(r-r^{-1})/2}{L}
+O\left(\frac{(\log L)^2}{L^2}\right)\right).
\end{aligned}\tag{4}
\]
Here the \(-h\log L/2\) term arises from the next-order variation of \(t_n(y)^{r-1}\), and \((r-r^{-1})/2\) from the first Mills-ratio correction. Keeping both is essential.

**4. Expansion under the integral.** Uniformly for \(y\in B_n\), replacing \((1-\bar\Phi(\sqrt r\,t_n(y)))^{m_n}\) by \(e^{-R_n(y)}\) costs \(o(L^{-k})\) for every fixed \(k>0\), since \(m_n\bar\Phi(\sqrt r\,t_n(y))^2\) is exponentially small in \(L\) times a fixed power of \(L\). The exact \(Y_n\) density differs from \(e^{-y}\) on \(B_n\) by at most an exponentially small integrated error. Put \(\delta_n(y)=R_n(y)/u(y)-1\). Taylor's formula gives
\[
1-e^{-R_n(y)}=(1-e^{-u(y)})+u(y)e^{-u(y)}\delta_n(y)
+O\big(u(y)^2e^{-u(y)/2}\delta_n(y)^2\big).
\]
Since \(|\delta_n(y)|=O(\log L/L)\) uniformly and both \(u e^{-u}\) and \(u^2e^{-u/2}\) are bounded, the integrated error is \(O((\log L)^2/L^2)\). The two discarded tails from step 2 are smaller. Integrate the coefficient in (4) against \(e^{-y}\,dy\) and use the definitions of \(F,H,J\). This proves the boxed expansion.

**5. Sign and cancellation.** The integrand defining \(H\) is strictly positive on \((0,\infty)\). With \(d=e=0\), the coefficient of \(\log L/L\) is \(-hH/2=-(r-1)H/4\), strictly negative. To attain \(P_n-F=O((\log L)^2/L^2)\), first the coefficient of \(\log L/L\) must be zero, forcing \(d=h/2\); then the constant coefficient of \(1/L\) must vanish, forcing \(e=e_*\). These choices also suffice, proving the claimed uniqueness and the accelerated rate.

## Verification

The standalone script `verify_gaussian_calibration.py` evaluates the exact one-dimensional integral (1), using the finite-\(n\) density rather than replacing it by an exponential, and compares it with the analytic expansion and optimized calibration. It independently checks that the derivative of \(F\) with respect to \(\log C\) equals \(H\). Running `python verify_gaussian_calibration.py` with SciPy and NumPy produced `PASS: 36 analytic consistency and finite-n quadrature assertions.` Tested variance ratios were \(r=1.44,2,4\) at \(n=10^6,10^{12},10^{24},10^{48}\); the large integer sample sizes enter the exact binomial maximum distribution numerically and are not Monte Carlo simulations. These finite checks do not prove the asymptotic error bound, which follows from steps 1–5.

For \(r=2,C=1\), numerical quadrature gives \(F\approx0.594814360967\), \(H\approx0.143268670122\), and the cancelling pair \((d_*,e_*)\approx(0.25,-0.405709479722)\).

## Relationship to prior work

Zhang, Miao and Mao (arXiv:2605.21155, first public submission 2026-05-20), Theorem 1, prove the critical first-order sample-size law and its nondegenerate limiting probability; this paper is the starting point and owns \(F\). The full available paper, including its derivation, multigroup theorem, and numerical section, was inspected. The present claim strengthens the two-group critical law by determining a signed explicit \(\log\log n/\log n\) bias and the unique cancellation of both first correction terms, which are not stated in that theorem.

Gasull, Jolis and Utzet (arXiv:1308.5541) study refined normal extreme-value norming constants and rates; their univariate expansions motivate care with Mills terms but do not state the competing-group probability correction. Davydov and Rotar (arXiv:2305.05967 and arXiv:2503.02473) study the general winner problem and limiting point-process methods without an explicit next-order two-Gaussian sample-size calibration.

## Limitations

Only the independent, zero-mean, fixed-two-group Gaussian model with \(r>1\) is treated. No uniformity is asserted as \(r\downarrow1\), \(C\) varies, or \(d,e\) depend on \(n\). The asymptotic rate is for the winning probability, not a total-variation approximation of the maximum distributions. A general-purpose second-order extreme-value theorem might give an alternative derivation; priority beyond the inspected sources has not been independently certified. The verification script is a finite numerical cross-check, not a formal proof or independent audit.

## References

- Chunxu Zhang, Baiqi Miao and Tiantian Mao, *Asymptotic Probabilities of Attaining the Maximum in Heterogeneous Gaussian Samples* (2026), arXiv:2605.21155, https://arxiv.org/abs/2605.21155 (first public 2026-05-20).
- Armengol Gasull, Maria Jolis and Frederic Utzet, *On the norming constants for normal maxima* (arXiv:1308.5541), https://arxiv.org/abs/1308.5541.
- Yu. Davydov and V. Rotar, *The Distribution of Argmaximum or a Winner Problem* (arXiv:2305.05967), https://arxiv.org/abs/2305.05967.
- Yu. Davydov and V. Rotar, *Point Process Approach to the Winner Problem* (arXiv:2503.02473), https://arxiv.org/abs/2503.02473.
