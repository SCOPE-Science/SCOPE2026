# A sharp Gaussian-noise transition for optimal sub-gamma scales

## Finding
Let \(N\sim\operatorname{Poisson}(\lambda)\), \(G\sim N(0,1)\) be independent, let \(b,\lambda>0\), and set \(X_s=b(N-\lambda)+\sqrt{s}\,G\) for \(s\ge0\). Write \(c_s\) for the smallest \(c\ge0\) such that
\[
\log\mathbb E e^{tX_s}\le\frac{(s+\lambda b^2)t^2}{2(1-ct)}\qquad(0\le t<1/c).
\]
For \(r=s/(\lambda b^2)\), the following exact classification holds:
\[
\boxed{c_s=\frac{b}{3(1+r)}\quad\Longleftrightarrow\quad 0\le r\le\frac13.}
\]
When \(r>1/3\), the optimal variational argument is unique and strictly positive; the optimal scale strictly exceeds the local third-cumulant bound \(b/[3(1+r)]\). It is characterized by a monotone scalar equation specified below. As \(r\to\infty\), its argument \(x_r\), in units of \(b t\), and its scale have the sharp asymptotics
\[
\boxed{x_r=\log r+3\log\log r-\log2+o(1),}\qquad
\boxed{\frac b{c_s}=\log r+3\log\log r+1-\log2+o(1).}
\]
More generally, let \(Y\) be any centered spectrally positive infinitely divisible law with finite nonzero variance \(V\), nonzero Lévy measure \(\nu\) with bounded positive support, and essential right endpoint \(b>0\): \(\nu((b-\varepsilon,b])>0\) for every \(0<\varepsilon<b\), while \(\nu((b,\infty))=0\). Allow an arbitrary Gaussian component in \(Y\). If \(c_s(Y)\) is the variance-exact right sub-gamma scale of \(Y+\sqrt{s}\,G\), then \(c_s(Y)\) is strictly decreasing in \(s\ge0\), and
\[
\boxed{\lim_{s\to\infty}c_s(Y)\log(s/V)=b.}
\]
The logarithm is taken only for \(s>V\). The limiting coefficient depends on the *largest available positive jump*, not its rate or the Gaussian variance already in \(Y\).

## Assumptions and scope
The Poisson law has fixed positive intensity \(\lambda\), fixed jump size \(b\), and the added Gaussian has variance \(s\), not standard deviation \(s\). All moment generating functions are evaluated on their maximal positive domains. At \(c=0\), the allowed \(t\)-range is all nonnegative real numbers. The complete classification includes \(s=0\), the exact boundary \(s=\lambda b^2/3\), and arbitrary \(s>\lambda b^2/3\). No uniqueness of a maximizer is asserted for the general bounded-jump law.

For the general statement, the Lévy–Khintchine exponent of \(Y\) is
\[
K_Y(t)=\frac{a t^2}{2}+\int_{(0,b]}(e^{tx}-1-tx)\,\nu(dx),\qquad
V=a+\int x^2\,\nu(dx)\in(0,\infty).
\]
Here \(a\ge0\) and \(\int x^2\nu(dx)>0\). No finite jump intensity, density, or atom at \(b\) is assumed.

## Proof
**1. Exact variational reduction.** For any such \(Y\), set \(A(t)=2K_Y(t)/t^2\) for \(t>0\), with \(A(0)=V\). After adding independent Gaussian variance \(s\), the cumulant generating function is \(K_Y(t)+st^2/2\). Elementary rearrangement of the inequality in the Finding, or the canonical remainder formula of Chen [1], gives the exact scale
\[
c_s(Y)=\sup_{t>0}\frac{A(t)-V}{t[s+A(t)]}.\tag{1}
\]
Indeed feasibility of \(c\) is equivalent to the displayed ratio being at most \(c\) whenever \(t<1/c\); for \(t\ge1/c\), the ratio is automatically at most \(1/t\le c\). This also proves attainment of the least feasible \(c\) and requires no unproved minimax step.

For \(Y=b(N-\lambda)\), put
\[
m(x)=\frac{2(e^x-1-x)}{x^2}=\sum_{n=0}^{\infty}\frac{2x^n}{(n+2)!},\quad m(0)=1,\quad r=\frac{s}{\lambda b^2}.
\]
Equation (1), after setting \(x=bt\), becomes
\[
\frac{c_s}{b}=\sup_{x>0}F_r(x),\qquad F_r(x)=\frac{m(x)-1}{x[r+m(x)]},\qquad F_r(0)=\frac{1}{3(1+r)}.\tag{2}
\]
The limiting value at zero follows from \(m(x)=1+x/3+O(x^2)\); at infinity \(0<F_r(x)<1/x\), so an optimizer exists in \([0,\infty)\).

**2. Exact uniqueness and the noise threshold.** Put \(U(x)=m(x)-1\) and \(D(x)=xm'(x)-U(x)\). As \(m(x)=\sum_{n\ge0}a_nx^n\) with \(a_n=2/(n+2)!\),
\[
D(x)=\sum_{n\ge2}(n-1)a_nx^n>0\quad(x>0),
\]
and direct differentiation yields
\[
\operatorname{sign}F'_r(x)=\operatorname{sign}\big((r+1)D(x)-U(x)^2\big).\tag{3}
\]
We prove that \(R(x)=U(x)^2/D(x)\) strictly increases from \(4/3\) to infinity. For every integer \(j\ge0\), the ratio between the coefficients of \(x^{j+2}\) in \(U^2\) and \(D\) is
\[
\rho_j=\frac{2\big[2^{j+6}-(j+6)^2-(j+6)-2\big]}{(j+1)(j+5)(j+6)}.\tag{4}
\]
This follows by summing the binomial coefficients with indices \(3,\dots,j+3\). A subtraction gives
\[
\rho_{j+1}-\rho_j=
\frac{2\big[2^{j+6}(j^2+3j-4)+j^3+22j^2+155j+326\big]}
{(j+1)(j+2)(j+5)(j+6)(j+7)}>0.\tag{5}
\]
For \(j=0\) the numerator's bracket equals \(70\), and for \(j\ge1\) both summands in the bracket are nonnegative, with the polynomial strictly positive. The positive-coefficient quotient lemma proves strict monotonicity of \(R\): if \(f_j/g_j\) increases strictly and \(g_j>0\), then the derivative of \((\sum f_jx^j)/(\sum g_jx^j)\) is a sum of positive terms \((k-j)(f_kg_j-f_jg_k)x^{j+k-1}\). Equation (4) gives \(R(0+)=\rho_0=4/3\). Also \(U(x)\sim2e^x/x^2\) and \(D(x)\sim(x-3)U(x)\), whence \(R(x)\to\infty\).

Consequently, if \(r\le1/3\), (3) is negative for all \(x>0\), and the unique maximizer of (2) on \([0,\infty)\) is the origin. If \(r>1/3\), there is exactly one positive solution of
\[
R(x_r)=r+1,\tag{6}
\]
with (3) positive before and negative after it. This is the unique global maximizer and strictly improves the origin value. Equation (2) proves the claimed if-and-only-if classification, including equality at \(r=1/3\).

**3. Sharp large-Gaussian expansion.** Put \(L=\log r\), and consider \(r\to\infty\). At \(x_0=L+4\log L\), one has \(m(x_0)/r\sim2L^2\), so \(F_r(x_0)\sim1/L\). Since \(m(x)=\mathbb E e^{xB}\) for \(B\sim\operatorname{Beta}(1,2)\),
\[
0<m(x)-1\le \frac{x}{3}e^x,\qquad F_r(x)\le\frac{e^x}{3r}.
\]
Thus no maximizer lies below \((1-\delta)L\) for fixed \(\delta>0\) and large \(r\). Also \(F_r(x)\le1/x\) excludes \(x\ge(1+\delta)L\). Hence \(x_r/L\to1\). The stationary equation from (3) is
\[
x_rm'(x_r)(r+1)=[m(x_r)-1][r+m(x_r)].\tag{7}
\]
As \(x_r\to\infty\), \(xm'(x)/m(x)=x-2+O(x^2e^{-x})\); dividing (7) by \(r m(x_r)\) now yields
\[
\frac{m(x_r)}r=x_r-3+o(1).\tag{8}
\]
Inserting \(m(x_r)=2e^{x_r}x_r^{-2}(1+o(1))\) into (8) gives \(x_r=L+3\log L-\log2+o(1)\). Finally, using (2) and (8),
\[
\frac b{c_s}=\frac{x_r(r+m(x_r))}{m(x_r)-1}=x_r+1+o(1),
\]
which proves the second boxed asymptotic.

**4. Universal bounded-positive-jump law.** For general \(Y\), the power series for \(A-V\), positivity of the Lévy measure, and \(\int x^n\nu(dx)\le b^{n-2}\int x^2\nu(dx)\) imply, for every \(t>0\),
\[
0<\frac{A(t)-V}{t}\le \frac{b}{3}\Big(\int x^2\nu(dx)\Big)e^{bt}.\tag{9}
\]
For \(L=\log(s/V)\to\infty\) and \(0<\delta<1\), (1) and (9) bound the objective by \(O(s^{-\delta})\) on \(t\le(1-\delta)L/b\), and by \(1/t\le b/[(1-\delta)L]\) on the complement. Thus \(\limsup Lc_s(Y)\le b/(1-\delta)\).

Choose \(0<\eta<b\) so that \((1+\delta)(b-\eta)>b\). The finite, strictly positive mass \(\nu((b-\eta,b])\) yields
\[
A(t)\ge\frac{2\nu((b-\eta,b])}{t^2}\big(e^{(b-\eta)t}-1-(b-\eta)t\big).
\]
At \(t=(1+\delta)L/b\), this implies \(A(t)/s\to\infty\). Hence (1) is asymptotic to \(1/t\) at that point, so \(\liminf Lc_s(Y)\ge b/(1+\delta)\). Letting \(\delta\downarrow0\) proves the limit. The positive function in (1) is pointwise strictly decreasing in \(s\), has a positive finite limit at \(t\downarrow0\), and tends to zero as \(t\to\infty\). Attainment on this compactified domain then proves **strict**, rather than merely weak, decrease of \(c_s(Y)\) with \(s\).

## Verification
The standalone `check.py` reproduces the rational coefficient ratios in (4) for the first 101 indices and tests their strict increase through index 100. It checks the endpoint-versus-interior transition and numerically locates stationary optimizers across a range of variance ratios. It also compares computed large-noise optimizers and inverse scales against the asymptotic center. This is a finite diagnostic, **not** a proof of coefficient positivity for all orders or of any limiting theorem. The general argument is in Parts 1–4 of the Proof.

To reproduce: run `python3 check.py` with Python 3.10 or later. No third-party Python libraries are used.

## Relationship to prior work
Chen [1, Sections 2, 3, 5] introduced the canonical remainder and the exact optimal variance-exact sub-gamma scale for spectrally positive infinitely divisible laws. In particular, it establishes a convolution upper bound and notes that Gaussian addition may reduce the optimal scale. Those established formulas are used rather than claimed as novel; [1] does not state the exact Gaussian-variance threshold, unique optimizer equation, or sharp Gaussian-variance decay here.

Chen and Wang [2, Sections 4, 6, 7] treat two-sided jumps and prove a different local-versus-interior phase transition for Skellam laws. Their rare *positive-jump* asymptotic also has a logarithmic scale and a \(3\log\log\) optimizer correction. That overlap in technique and exponent is material. Their canonical remainder contains the negative-jump component \(m(-x)\), whereas Gaussian addition supplies an atom at zero and yields \((r+m(x))/(r+1)\). Their quoted Skellam statements therefore do not give the exact Gaussian transition \(r=1/3\), the single positive optimizer theorem for this family, or the all-bounded-support limit. Chen and Wang [3] optimize a different parameter, namely the variance proxy at fixed underlying distribution, and its accessible abstract does not claim the present Gaussian-addition formulas; its full text could not be inspected.

## Limitations
The unique interior optimizer and two-term inverse-scale expansion are specific to fixed-size positive Poisson jumps with independently added Gaussian variance. The universal support-endpoint law assumes a nonzero positive Lévy measure with finite essential right endpoint; it does not cover unbounded jump supports, directional signed-jump mixtures, or multidimensional envelopes. The result addresses variance-exact sub-gamma envelopes, not exact tail probabilities or best Chernoff bounds. The original general variational framework and the related Skellam logarithmic phenomenon predate this calculation. The inaccessible full text of [3] creates a residual priority risk; mathematical novelty is not an independence certification.

## References
[1] Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, first-public-record date September 2, 2026. https://arxiv.org/html/2610.00032v1

[2] Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, September 2, 2026. https://arxiv.org/html/2609.02590v1

[3] Y. Chen and X. Wang, *Feasible Frontiers for Sub-Gamma Envelopes: the Variance--Pole Trade-off for Infinitely Divisible Laws*, arXiv:2609.23069v1, September 19, 2026. https://arxiv.org/abs/2609.23069
