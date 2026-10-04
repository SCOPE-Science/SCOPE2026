# All-order sharp three-point smoothest averages

## Finding
Let \(k\ge 1\) be an integer and set \(r=k/2\) and
\[
c_r=\frac{r^r}{(r+1)^{r+1}}.
\]
For a symmetric normalized kernel \(u\) supported on \(\{-1,0,1\}\), define
\[
\mathcal C_k(u)=\sup_{0\ne f\in\ell^2(\mathbb Z)}
\frac{\|\nabla^k(u*f)\|_2}{\|f\|_2}.
\]
There is a unique number \(b_r>1\) satisfying
\[
(b_r-1)b_r^r=c_r.
\]
Then the unique unrestricted minimizer is
\[
u_k(-1)=u_k(1)=\frac{b_r}4,
\qquad
u_k(0)=1-\frac{b_r}2,
\]
and the exact sharp constant is
\[
\min_u \mathcal C_k(u)=2^k(b_r-1).
\]
If the additional constraint \(\widehat u\ge0\) is imposed, then for every \(k\ge1\) the unique minimizer is instead the same triangle kernel
\[
u^+(-1)=u^+(1)=\frac14,
\qquad
u^+(0)=\frac12,
\]
with exact sharp constant
\[
\min_{\widehat u\ge0}\mathcal C_k(u)
=2^k\frac{r^r}{(r+1)^{r+1}}.
\]
Thus the smallest nontrivial support radius admits a complete all-order solution in both variants. As \(k\to\infty\),
\[
\min_u\mathcal C_k(u)
\sim \frac{2^{k+1}W(e^{-1})}k,
\qquad
\min_{\widehat u\ge0}\mathcal C_k(u)
\sim \frac{2^{k+1}}{ek},
\]
so their ratio tends to \(eW(e^{-1})\approx0.7569451065\).

## Assumptions and scope
The kernel is real, symmetric, normalized by \(\sum_j u(j)=1\), and supported exactly within \(\{-1,0,1\}\); zero endpoint weights are allowed. The difference operator is the forward discrete difference \(\nabla f(j)=f(j+1)-f(j)\). The first minimization has no sign or Fourier-positivity restriction. The second requires \(\widehat u(\xi)\ge0\) for every frequency. No claim is made here for support radius \(n\ge2\).

## Proof
Write \(u(-1)=u(1)=a\) and \(u(0)=1-2a\), and set \(b=4a\). With \(t=\sin^2(\xi/2)\in[0,1]\),
\[
\widehat u(\xi)=1-bt,
\qquad
|\widehat{\nabla^k}(\xi)|=2^k t^{k/2}.
\]
Plancherel's theorem and the standard multiplier norm identity therefore give
\[
\mathcal C_k(u)=2^k\max_{0\le t\le1}t^r|1-bt|.
\]
It remains to solve this one-parameter minimax problem exactly.

If \(b\le1\), then \(1-bt\ge0\) on \([0,1]\), and for each fixed \(t>0\) the expression \(t^r(1-bt)\) strictly decreases as \(b\) increases. Hence the best point in this whole half-line is \(b=1\). At \(b=1\), differentiation gives the unique interior maximizer \(t=r/(r+1)\), with value
\[
c_r=\frac{r^r}{(r+1)^{r+1}}.
\]
This proves the Fourier-nonnegative result as well, because \(\widehat u=1-bt\ge0\) for all \(t\in[0,1]\) is equivalent to \(b\le1\). Uniqueness follows from the strict pointwise monotonicity before \(b=1\).

Now suppose \(b>1\). On \([0,1/b]\), the positive branch \(t^r(1-bt)\) has its unique maximum at
\[
t_0=\frac r{(r+1)b},
\]
with value
\[
A(b)=c_r b^{-r}.
\]
On \([1/b,1]\), the negative branch \(t^r(bt-1)\) is strictly increasing, so its maximum is
\[
B(b)=b-1.
\]
Therefore
\[
\max_{0\le t\le1}t^r|1-bt|=\max\{c_r b^{-r},b-1\}.
\]
The first term is strictly decreasing and the second strictly increasing. Their unique crossing \(b=b_r>1\) is consequently the unique global minimizer on \(b>1\), and it satisfies
\[
(b_r-1)b_r^r=c_r.
\]
Since \(b_r-1=c_r b_r^{-r}<c_r<1\), one has \(1<b_r<2\), so even the unrestricted optimal spatial weights are positive, although their Fourier transform changes sign near \(\xi=\pi\). Comparing \(b_r-1<c_r\) shows that this unrestricted minimizer strictly improves on the Fourier-nonnegative one.

For the asymptotics, let \(m_r=b_r-1\) and \(y_r=rm_r\). The defining equation becomes
\[
y_r\left(1+\frac{y_r}r\right)^r=rc_r.
\]
Also
\[
rc_r=\left(\frac r{r+1}\right)^{r+1}\longrightarrow e^{-1}.
\]
Since \(y_r\) stays bounded and positive, every limit point solves \(ye^y=e^{-1}\); strict monotonicity gives
\[
y_r\longrightarrow W(e^{-1}).
\]
Substituting \(r=k/2\) yields the two stated constant asymptotics and their ratio.

## Verification
The supplementary script `verify_three_point_all_orders.py` independently checks the equal-ripple equation, the branch maxima, the Fourier-nonnegative endpoint, low-order consistency with the known \(k=1\) and \(k=2\) constants, and the Lambert-\(W\) asymptotic numerically for representative orders. Its recorded output is `verification_output.txt` and begins with `VERIFY_OK`. These finite computations are consistency checks only; the theorem is proved analytically above.

## Relationship to prior work
Kravitz and Steinerberger solved the unrestricted first-difference problem for every support radius and the Fourier-nonnegative second-difference problem, with the triangle kernel in the latter setting. Richardson solved the unrestricted second-difference problem for every support radius. Gaitán, Garzón, and Madrid subsequently solved the unrestricted third-difference problem and the Fourier-nonnegative fourth- and sixth-difference problems, and explicitly tabulated several remaining derivative orders as open. The present statement does not replace those general-radius results: it fixes the natural first nontrivial radius \(n=1\) and obtains an exact classification for every derivative order at once. In particular, it gives exact finite-radius instances in rows that remain open at general radius, while recovering the known low-order cases when specialized to \(k=1,2,3\).

## Limitations
The proof exploits that a symmetric normalized radius-one kernel has only one free scalar parameter. For larger support, the corresponding weighted minimax problem is genuinely multivariate and the argument does not extend directly. The literature comparison used the recent source's full-text open-problem table, the earlier low-order source abstracts/results, targeted web searches, and targeted published-finding corpus searches; an equivalent radius-one all-order formula under different notation in uncatalogued approximation literature cannot be ruled out absolutely.

## References
1. José Gaitán, Carlos Garzón, José Madrid, *The smoothest average and some extremal problems for polynomials*, arXiv:2604.25074v1, 2026.
2. Sean Richardson, *A Sharp Fourier Inequality and the Epanechnikov Kernel*, arXiv:2310.09713v1, 2023.
3. Noah Kravitz, Stefan Steinerberger, *The smoothest average: Dirichlet, Fejér and Chebyshev*, arXiv:2007.13700v1, 2020; published 2021.
