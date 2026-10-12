# Exact lower-tail phase boundary and stochastic-order reversal for calibrated power-exponential sums

## Finding
Let \(n\ge2\), let \(\beta>0\), and let \(X_1,\ldots,X_n\) be independent with density
\[
f_\beta(x)=\frac{\beta}{\Gamma(1/\beta)}e^{-x^\beta}\mathbf 1_{\{x>0\}}.
\]
Write \(S_n=\sum_{i=1}^nX_i\), \(M_n=\max_{1\le i\le n}X_i\), \(C_n=(n!)^{1/n}\), and \(\Delta_{n,\beta}(x)=\Pr(S_n\le x)-\Pr(C_nM_n\le x)\). The factor \(C_n\) is the unique positive scale matching the two leading small-\(x\) CDF terms.

For every integer \(n\ge2\) there is a unique \(\kappa_n>0\) solving
\[
\prod_{k=2}^n(\kappa_n+k)=(n!)^{1+\kappa_n/n}.
\]
For each fixed \(\beta\ne\kappa_n\), the **exact sign of the first nonzero CDF discrepancy at the origin** is
\[
\operatorname{sgn}\Delta_{n,\beta}(x)=
\begin{cases}+1,&0<\beta<\kappa_n,\\-1,&\beta>\kappa_n,\end{cases}
\qquad\text{for all sufficiently small }x>0.
\]
Moreover, \(\kappa_2=2\), whereas \(\kappa_n>2\) for all \(n\ge3\).

For three summands, define
\[
\lambda_3=\frac{\log3}{\log(3/6^{1/3})}.
\]
Then \(2<\kappa_3<21/10<\lambda_3\), with \(\kappa_3\approx2.06292239719\) and \(\lambda_3\approx2.19126813093\). **Every** \(\beta\in(\kappa_3,\lambda_3)\) produces a genuine CDF crossing:
\[
\Delta_{3,\beta}(x)<0\text{ for sufficiently small }x>0,
\qquad
\Delta_{3,\beta}(x)>0\text{ for sufficiently large }x.
\]
Consequently neither \(S_3\le_{\mathrm{st}}6^{1/3}M_3\) nor the reverse usual stochastic order holds for any such \(\beta\). This asserts at least one crossing, not uniqueness or a complete classification outside the displayed interval.

## Assumptions and scope
The density is a one-parameter power-exponential/generalized-gamma subfamily with a positive density value at zero. The variables are independent and identically distributed. All results are exact for fixed finite \(n\) and fixed real \(\beta>0\), with inequalities at sufficiently small or large positive arguments; the two thresholds in the crossing statement pertain to \(n=3\). Any common scale of the variables cancels from the comparison after appropriately scaling the argument.

## Proof
**1. Matched leading term and exact next term.** Put \(c_\beta=\beta/\Gamma(1/\beta)\). The distribution function of one summand obeys
\[
F_\beta(y)=c_\beta y\left(1-\frac{y^\beta}{\beta+1}+O(y^{2\beta})\right)
\quad(y\downarrow0).
\]
Hence, using \(C_n^n=n!\),
\[
\Pr(C_nM_n\le x)=\frac{c_\beta^n x^n}{n!}
\left(1-\frac{n}{(\beta+1)C_n^\beta}x^\beta+O(x^{2\beta})\right).
\tag{1}
\]
On the simplex \(D_n=\{(u_1,\ldots,u_n):u_i\ge0,\sum_i u_i\le1\}\), the change of variables \(X_i=xu_i\) gives
\[
\Pr(S_n\le x)=c_\beta^n x^n\int_{D_n}
 e^{-x^\beta\sum_i u_i^\beta}\,du.
\]
The simplex has volume \(1/n!\), and the Dirichlet beta integral gives
\[
\int_{D_n}\sum_{i=1}^n u_i^\beta\,du
=\frac{n\Gamma(\beta+1)}{\Gamma(n+\beta+1)}.
\]
Taylor's theorem, uniformly on the compact simplex, therefore yields
\[
\Pr(S_n\le x)=\frac{c_\beta^n x^n}{n!}
\left(1-\frac{n n!\Gamma(\beta+1)}{\Gamma(n+\beta+1)}x^\beta+O(x^{2\beta})\right).
\tag{2}
\]
The common leading coefficient is precisely why \(C_n\) is the sole possible matching scale. Subtracting (1) from (2), the coefficient of \(x^{n+\beta}\) has the sign of \(R_n(\beta)-1\), where
\[
R_n(\beta)=\frac{\Gamma(n+\beta+1)}{\Gamma(\beta+2)n!C_n^\beta}
=\prod_{k=2}^n\left(1+\frac\beta k\right)C_n^{-\beta}.
\tag{3}
\]
No claim about the sign at \(\beta=\kappa_n\) is inferred from this canceled coefficient.

**2. Unique phase boundary.** Let \(L_n(\beta)=\log R_n(\beta)\). Then
\[
L_n(0)=0,\quad L_n'(0)=\sum_{k=2}^n\frac1k-\frac{\log(n!)}n>0,
\quad L_n''(\beta)=-\sum_{k=2}^n\frac1{(k+\beta)^2}<0.
\]
For the strict derivative inequality, sum \(\log k<H_{k-1}\) over \(2\le k\le n\), where \(H_j=\sum_{i=1}^j1/i\), and use \(\sum_{k=2}^nH_{k-1}=n(H_n-1)\). Furthermore \(L_n(\beta)\to-\infty\) as \(\beta\to\infty\), since the logarithmic product grows only as \((n-1)\log\beta\) but \(\beta\log C_n\) grows linearly. Strict concavity gives exactly one positive root, positive values before that root, and negative values after it. When \(n=2\), substituting \(\beta=2\) into (3) gives the root. When \(\beta=2\),
\[
R_n(2)=\frac{(n+1)(n+2)}{6(n!)^{2/n}}.
\]
The arithmetic mean of the \(n\) positive values \(k(n+1-k)\), \(1\le k\le n\), is \((n+1)(n+2)/6\) and their geometric mean is \((n!)^{2/n}\). Strict AM–GM applies for \(n\ge3\); therefore \(R_n(2)>1\) and \(\kappa_n>2\).

**3. A provably nonempty three-variable crossing interval.** For \(n=3\), equation (3) reads
\[
R_3(\beta)=\frac{(\beta+2)(\beta+3)}{6^{1+\beta/3}}.
\]
At \(\beta=2\), the strict inequality \(R_3(2)>1\) is equivalent to \(20^3>6^5\). At \(\beta=21/10\), the inequality \(R_3(21/10)<1\) is equivalent to the exact integer comparison \(2091^{10}<6^{17}100^{10}\). Thus \(2<\kappa_3<21/10\). Also \(\lambda_3>21/10\) follows from \(6^{7/10}>3^{11/10}\), equivalent to \(2^7>3^4\). In particular, \(\kappa_3<\lambda_3\) without relying on decimal root approximations.

**4. The opposite far-tail sign.** For \(\beta>1\), \(X_i^\beta\) has a gamma law of shape \(1/\beta\) and unit rate. Convexity implies
\[
\sum_{i=1}^nX_i^\beta\ge n^{1-\beta}S_n^\beta.
\]
The gamma survival tail and this inclusion give
\[
\limsup_{x\to\infty}x^{-\beta}\log\Pr(S_n>x)\le -n^{1-\beta}.
\]
Conversely the event that **all** \(X_i>x/n\) entails \(S_n>x\), and the one-variable tail has \(\lim_{t\to\infty}t^{-\beta}\log\Pr(X_i>t)=-1\). Hence the reverse liminf bound holds, proving
\[
\lim_{x\to\infty}x^{-\beta}\log\Pr(S_n>x)=-n^{1-\beta}.
\tag{4}
\]
For the scaled maximum, the same one-variable tail calculation gives
\[
\lim_{x\to\infty}x^{-\beta}\log\Pr(C_nM_n>x)=-C_n^{-\beta}.
\tag{5}
\]
For \(n=3\) and \(\beta<\lambda_3\), the exponent inequality \(3^{1-\beta}>6^{-\beta/3}\) holds. Equations (4)–(5) imply \(\Pr(S_3>x)/\Pr(6^{1/3}M_3>x)\to0\); equivalently \(\Delta_{3,\beta}(x)>0\) for all sufficiently large \(x\). Combining this with the negative small-\(x\) sign from Steps 1–3 for \(\kappa_3<\beta<\lambda_3\) proves the crossing and stochastic-order incomparability.

## Verification
A standalone standard-library checker (`check.py`) verifies the exact integer inequalities used to locate the open crossing interval, the identity of the first coefficients at \(\beta=1,2,3\) in finite dimensions, and the numeric localization of the positive root using bisection. Its output is corroborative; the proof of the real-parameter and all-dimension statements is Steps 1–4, not numerical sampling or finite checking.

## Relationship to prior work
Okamura, *A remark on the comparison of the sum and the maximum of positive random variables* (arXiv:2604.10395, first posted 12 April 2026), disproves the distributional-identity conjecture attributed to Arnold and Villaseñor, identifies the leading origin-matching scale, and compares tail exponential rates in the generalized-gamma family. Those contributions, the two-variable half-normal identity, the elementary Dirichlet integral, and gamma-tail facts are used here as existing foundations, not as new discoveries. The present result adds the next-order **signed** origin discrepancy for all sample sizes, proves the unique power-exponential phase boundary, and combines it with the competing upper-tail scale to exhibit a nonempty open family of **two-way CDF reversals** for three summands.

## Limitations
This does not establish that the CDFs cross only once or classify usual stochastic order outside the interval \((\kappa_3,\lambda_3)\). No conclusion at the canceled local coefficient \(\beta=\kappa_n\) is asserted. The parameters \(\kappa_n\) are given as unique transcendental-equation roots, not elementary closed forms. The result concerns the power-exponential subfamily with density proportional to \(e^{-x^\beta}\), not arbitrary generalized-gamma shapes or dependent summands. An earlier equivalent treatment in unindexed literature cannot be ruled out. The full original Arnold–Villaseñor article was not accessible for complete comparison.

## References
- Kazuki Okamura, *A remark on the comparison of the sum and the maximum of positive random variables*, arXiv:2604.10395, v1 posted 12 April 2026; v3 posted 26 July 2026. https://arxiv.org/abs/2604.10395
- Barry C. Arnold and Jose A. Villaseñor, *On a Characteristic Property of the Half-Normal Distribution*, Sankhya A 88 (2026), 192–200, DOI:10.1007/s13171-026-00435-y. Source available in abstract form during comparison.
- E. W. Stacy, *A Generalization of the Gamma Distribution*, Annals of Mathematical Statistics 33 (1962), 1187–1192. Classical distribution background.
