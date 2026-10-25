# Shape-dependent Gaussian-dilution transition and singular optimal sub-gamma scales for Gamma jumps

## Finding
For a centered compound-Poisson process with Gamma jumps plus independent Gaussian noise, there is an exact phase diagram for the smallest right sub-gamma scale at the *actual* variance. Write \(J\sim\operatorname{Gamma}(\alpha,\beta)\) with shape \(\alpha>0\), scale \(\beta>0\); let \(N\sim\operatorname{Poisson}(\lambda)\), \(\lambda>0\), and let \(Z\sim N(0,1)\) be independent. Set
\[
X=\sigma Z+\sum_{j=1}^{N}J_j-\lambda\alpha\beta,\qquad V=\sigma^2+\lambda\alpha(\alpha+1)\beta^2,\qquad \rho=\frac{\lambda\alpha(\alpha+1)\beta^2}{V}\in(0,1].
\]
Define \(c_*\) as the infimum of \(c\ge0\) for which \(\log\mathbb E e^{tX}\le Vt^2/[2(1-ct)]\) for all \(0\le t<1/c\). Then:

**(i) Gamma shapes up to one.** For \(0<\alpha\le1\) and every \(\rho>0\), \(c_*=\beta\).

**(ii) Shapes above one.** For \(\alpha>1\), put \(\rho_c=3(\alpha+3)/[4(\alpha+2)]\), strictly between \(3/4\) and \(1\). If \(\rho_c\le\rho\le1\), then
\[
c_*=\beta\rho\frac{\alpha+2}{3}.
\]
If \(0<\rho<\rho_c\), the least pole exceeds BOTH the MGF-boundary and third-cumulant poles:
\[
c_*>\beta\max\left\{1,\rho\frac{\alpha+2}{3}\right\};
\]
it is attained at an interior argument \(0<s_*<1\) of the exact one-dimensional variational problem in the proof.

**(iii) A singular small-jump-fraction law.** For every fixed \(\alpha>1\), set \(d_\alpha=[2/(\alpha^2(\alpha+1))]^{1/(\alpha-1)}\). As \(\rho\downarrow0\),
\[
\frac{c_*}{\beta}=1+\frac{\alpha-1}{\alpha}d_\alpha\rho^{1/(\alpha-1)}+o(\rho^{1/(\alpha-1)}),\qquad
1-s_*=d_\alpha\rho^{1/(\alpha-1)}+o(\rho^{1/(\alpha-1)})
\]
for **every** maximizing \(s_*\). Here the jump intensity is positive at every \(\rho>0\); the pure Gaussian model \(\rho=0\) instead has \(c_*=0\).

**(iv) Exact Erlang-two benchmark.** At \(\alpha=2\), the transition is \(\rho_c=15/16\), and
\[
\frac{c_*}{\beta}=\begin{cases}
\dfrac{3(1+\sqrt{1-\rho})}{2(1+2\sqrt{1-\rho})},&0<\rho<15/16,\\[3pt]
\dfrac{4\rho}{3},&15/16\le\rho\le1.
\end{cases}
\]
For the lower interval a maximizing argument is \(s_*=4/3-[3\sqrt{1-\rho}]^{-1}\).

## Assumptions and scope
All parameters are fixed when optimizing the Laplace argument. The jumps are strictly positive, independent Gamma random variables; the Gaussian variance may vanish but the Poisson intensity must not vanish. The scale is variance-exact, one-sided, and refers to the centered sum, not a variance proxy chosen freely. At \(\rho=1\), the formula reproduces the known pure compound-Poisson Gamma-jump scale. The limiting case \(\rho\to0\) means increasing Gaussian variance relative to jump variance, not replacing the law by a Gaussian before optimizing the Laplace variable.

## Proof
We include the reduction so the new conclusions do not rely on an undocumented numeric optimizer. Write \(s=\beta t\). The log moment-generating function is
\[
K_X(t)=\frac{\sigma^2t^2}{2}+\lambda\left[(1-\beta t)^{-\alpha}-1-\alpha\beta t\right],\quad 0\le t<1/\beta,
\]
and is infinite for \(t\ge1/\beta\). Define
\[
M_\alpha(s)=\frac{2\{(1-s)^{-\alpha}-1-\alpha s\}}{\alpha(\alpha+1)s^2}=\sum_{m=0}^{\infty}a_ms^m,
\quad a_m=\frac{2(\alpha+2)_m}{(m+2)!},\quad a_0=1.
\]
Here \((z)_m=z(z+1)\cdots(z+m-1)\), with \((z)_0=1\). Direct division by \(Vt^2/2\) gives \(M_X(s)=1+\rho(M_\alpha(s)-1)\). The exact optimal-pole reduction, obtained by algebraically solving \(M_X(s)\le1/(1-cs/\beta)\) and accounting for the infinite MGF domain, is
\[
\boxed{\ \frac{c_*}{\beta}=\sup_{0<s<1}\Phi_{\alpha,\rho}(s),\qquad
\Phi_{\alpha,\rho}(s)=\frac{\rho[M_\alpha(s)-1]}{s\{1+\rho[M_\alpha(s)-1]\}}.\ }
\]
Arguments \(s\ge1\) with infinite MGF contribute at most \(1/s\le1\), and \(\Phi(s)\to1\) as \(s\uparrow1\), so the displayed supremum is indeed global. At the origin, \(\Phi(0+)=\rho a_1\), where \(a_1=(\alpha+2)/3\). Its first-order expansion is
\[
\Phi(s)=\rho a_1+\rho(a_2-\rho a_1^2)s+O(s^2),\qquad a_2=\frac{(\alpha+2)(\alpha+3)}{12}.
\]
If \(0<\alpha\le1\), the coefficient ratios satisfy \(a_{m+1}/a_m=(\alpha+m+2)/(m+3)\le1\), hence \(a_m\le1\) and \(M_X(s)\le(1-s)^{-1}\). Thus \(c_*\le\beta\), with equality forced by the positive-jump MGF singularity.

Suppose \(\alpha>1\). The ratios \(a_{m+1}/a_m\) are decreasing. Thus for \(m\ge1\), \(a_m\le a_1(a_2/a_1)^{m-1}\). If \(\rho\ge a_2/a_1^2=\rho_c\), then \(\rho a_m\le(\rho a_1)^m\) for all \(m\ge1\). Term-by-term, \(M_X(s)\le[1-\rho a_1s]^{-1}\) on the required range \(0\le s<1/(\rho a_1)\). Therefore \(c_*\le\beta\rho a_1\), with the reverse inequality supplied by the limit \(s\downarrow0\).

If \(0<\rho<\rho_c\), the displayed origin expansion is strictly increasing, so \(c_*>\beta\rho a_1\). On the other boundary write \(\epsilon=1-s\), and set \(C_\alpha=2/[\alpha(\alpha+1)]\). Since \(M_\alpha(1-\epsilon)-1\sim C_\alpha\epsilon^{-\alpha}\),
\[
\Phi(1-\epsilon)=\frac1{(1-\epsilon)[1+\{\rho(M_\alpha(1-\epsilon)-1)\}^{-1}]}.
\]
For fixed \(\rho>0\) and \(\alpha>1\), this is \(1+\epsilon+o(\epsilon)>1\). Both endpoint values are therefore strictly smaller than the supremum, which continuity attains in \(0<s<1\).

For small \(\rho\) and fixed \(\alpha>1\), any maximizing argument must approach \(s=1\): on \(s\le1-\epsilon_0\) the variational profile is \(O(\rho)\), whereas its endpoint limit is one. Moreover, positivity of \(\Phi(1-\epsilon)-1\) entails \(\rho[M_\alpha(1-\epsilon)-1]> (1-\epsilon)/\epsilon\), which with the Gamma asymptotic forces \(\epsilon=O(\rho^{1/(\alpha-1)})\). Put \(\delta=\rho^{1/(\alpha-1)}\), \(\epsilon=\delta d\), with \(d\) in a compact nonnegative interval. Uniformly there,
\[
\Phi(1-\delta d)=1+\delta\left(d-\frac{d^\alpha}{C_\alpha}\right)+o(\delta).
\]
The profile \(d-d^\alpha/C_\alpha\) has the unique positive maximizer \(d_\alpha=(C_\alpha/\alpha)^{1/(\alpha-1)}\) and maximum \((\alpha-1)d_\alpha/\alpha\). Compact localization and uniform convergence prove both asymptotic formulas and the statement for every maximizer. At \(\rho=0\), \(K_X\) is exactly quadratic, giving \(c_*=0\).

For \(\alpha=2\), direct simplification gives \(M_2(s)=(3-2s)/[3(1-s)^2]\) and
\[
\Phi_{2,\rho}(s)=\frac{\rho(4-3s)}{3(1-s)^2+\rho s(4-3s)}.
\]
Its derivative has the sign of \((1-\rho)(4-3s)^2-1\) (with a positive denominator and fixed positive factor), hence an interior maximizer exists precisely for \(\rho<15/16\), at the displayed \(s_*\). Substitution gives the claimed closed form; otherwise the maximum is its origin value \(4\rho/3\).

## Verification
A separately runnable exact-arithmetic checker in `checks/verify.py` tests the Erlang-two derivative identity and closed-form optimizer at rational parameter values, the coefficient-ratio and critical-fraction identities for integer Gamma shapes, and direct evaluations of the original cumulant against the normalized transform. The recorded execution result is in `checks/verify_output.txt`. Numerical finite checks are not used as proof of the infinite-dimensional or limiting assertions; the proofs above are analytic.

## Relationship to prior work
Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws* (2026), develops the canonical transform and exact one-variable pole characterization, and determines the scale for pure compound-Poisson Gamma jumps. That framework and the pure-jump case are **prior**, not new. The results here concern **positive Gaussian variance in the Gamma-jump family**, give its shape-dependent transition and exact Erlang-two branch, and quantify the previously unresolved nonanalytic \(\rho\downarrow0\) boundary correction. Chen and Wang's directional extension (2026) concerns two-sided Lévy laws and signed jumps; its variational machinery can apply to the current one-sided setting but the located results do not state this parameter classification. Prior bounded-jump Gaussian-dilution classifications do not imply the unbounded Gamma boundary scale law, particularly its shape-dependent exponent. General Poisson proxy optimization uses a different concentration envelope. See references.

## Limitations
This is a scalar, spectrally positive, Gamma-jump law; no general claim is made for mixtures of Gamma shapes, negative jumps, other Lévy densities, or sharpness of the resulting Chernoff tail approximation. The positive-root stationary point for general \(\alpha>1\) is shown to exist, not necessarily unique (except for \(\alpha=2\)); all small-\(\rho\) maximizing points nevertheless have the stated asymptotic. Historical priority beyond inspected and searchable sources remains uncertain; independent review has not occurred.

## References
1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, publicly posted 2026-09-02; full HTML https://arxiv.org/html/2610.00032v1.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, publicly posted 2026-09-02; https://arxiv.org/abs/2609.02590.
3. L. Leskelä and A. Välimaa, *Sub-Poisson distributions: Concentration inequalities, optimal variance proxies, and closure properties*, arXiv:2508.12103v1; https://arxiv.org/html/2508.12103v1.
