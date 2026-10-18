# A square-root singleton–doubleton covariance transition in finite Dirichlet populations

## Finding
Fix \(0<\gamma<1\). For each integer \(m\ge3\), draw \(P=(P_1,\ldots,P_m)\sim\operatorname{Dirichlet}(\gamma/m,\ldots,\gamma/m)\), then draw \(n\) conditionally independent labels from \(P\). Write \(A_1\) and \(A_2\) for the numbers of species observed exactly once and twice, respectively. There is an integer \(m_0(\gamma)\) such that for every \(m\ge m_0(\gamma)\), the smooth positive factor governing \(\operatorname{Cov}(A_1,A_2)\) has a unique real zero \(r_m>3\), and for every integer \(n\ge3\)
\[
\operatorname{sgn}\operatorname{Cov}(A_1,A_2)=\operatorname{sgn}(r_m-n).
\]
At an integer equality \(n=r_m\), the covariance is zero. The crossing has the two-term asymptotic
\[
\boxed{r_m=\sqrt{2(1-\gamma)m}+\frac{3+2\gamma}{2}+O_\gamma(m^{-1/2}).}
\]
More generally, for any fixed \(\gamma>0\) and integer sequence \(n_m/\sqrt m\to c\in(0,\infty)\), the covariance-sign ratio \(Q_{m,n_m}\) defined below satisfies
\[
\boxed{\lim_{m\to\infty}m\log Q_{m,n_m}=\frac{2(1-\gamma)}{c^2}-1.}
\]
Thus at every positive square-root sample scale, \(\gamma\ge1\) gives eventual strictly negative covariance, while \(0<\gamma<1\) has the sharp transition at \(c=\sqrt{2(1-\gamma)}\). No assertion of a universal finite-\(m\) one-crossing theorem is made.

## Assumptions and scope
The population has exactly \(m\) exchangeable possible species, with positive Dirichlet concentration \(\gamma/m\) per species and fixed total mass \(\gamma\). The sample size \(n\) counts draws with replacement conditional on the random probability vector; unconditionally this is the Dirichlet-multinomial (Pólya) law. The global one-crossing conclusion requires fixed \(\gamma\in(0,1)\) and sufficiently large integer \(m\). The scaling limit holds for every fixed \(\gamma>0\), and the displayed limits are not asserted uniformly as \(\gamma\) tends to zero or one. The zero \(r_m\) refers to the real-analytic gamma-function interpolation of the exact covariance-sign ratio, not a noninteger random sample size.

For \(x>0\) and integer \(j\ge0\), \((x)_j=\prod_{q=0}^{j-1}(x+q)\); in the interpolation, \((x)_t=\Gamma(x+t)/\Gamma(x)\) for admissible real \(t\). Empty products equal one.

## Proof
**Exact moments.** Put \(\alpha=\gamma/m\) and \(Z=(m\alpha)_n\). Exchangeability and Dirichlet integration give the probabilities that a specified label appears once, twice, and that two distinct specified labels appear once and twice, respectively:
\[
\begin{aligned}
p_1&=\frac{n\alpha((m-1)\alpha)_{n-1}}Z,\\
p_2&=\frac{\binom n2\alpha(\alpha+1)((m-1)\alpha)_{n-2}}Z,\\
p_{12}&=\frac{n(n-1)(n-2)\alpha^2(\alpha+1)((m-2)\alpha)_{n-3}}{2Z}.
\end{aligned}
\]
Therefore \(\operatorname{Cov}(A_1,A_2)=m(m-1)p_{12}-m^2p_1p_2=m^2p_1p_2(Q_{m,n}-1)\), with \(m^2p_1p_2>0\), where
\[
Q_{m,n}=\frac{m-1}{m}\frac{n-2}{n}\,
\frac{(\gamma)_n(\gamma-2\gamma/m)_{n-3}}
{(\gamma-\gamma/m)_{n-1}(\gamma-\gamma/m)_{n-2}}.
\tag{1}
\]
This follows from the joint Dirichlet-multinomial moments; it does not assume independently distributed species occupancies.

**Comparison with the infinite-species Ewens limit.** Write \(\beta=\gamma/m\), \(A=2(1-\gamma)\), and
\[
Q_{\infty,n}=\frac{n-2}{n}\frac{\gamma+n-1}{\gamma+n-3}
=1+\frac{A}{n(n+\gamma-3)}.
\]
There is an exact factorization
\[
\log Q_{m,n}=\log(1-m^{-1})+\log Q_{\infty,n}+h_n(\beta),\tag{2}
\]
where
\[
\begin{aligned}
h_n(\beta)={}&\log\frac{(\gamma)_{n-3}(\gamma-2\beta)_{n-3}}{(\gamma-\beta)_{n-3}^2}\\
&+2\log\frac{\gamma+n-3}{\gamma-\beta+n-3}
+\log\frac{\gamma+n-2}{\gamma-\beta+n-2}.
\end{aligned}\tag{3}
\]
For integer \(n\ge3\), concavity of \(x\mapsto\log(x)_{n-3}\) makes the first logarithm nonpositive. Its second derivative is a negative sum of reciprocal squares, bounded uniformly in \(n\) for \(x\ge\gamma/3\). Centered Taylor expansion therefore bounds it below by \(-C_\gamma\beta^2\). The remaining two logarithms are nonnegative and bounded above by \(C_\gamma\beta/n\). Hence, uniformly in all integers \(n\ge3\) as \(m\to\infty\),
\[
-C_\gamma m^{-2}\le h_n(\gamma/m)\le C_\gamma(mn)^{-1}.\tag{4}
\]
The gamma-function continuation satisfies these bounds for every real \(n\ge3\) as well; they follow using the decreasing trigamma function and the same logarithmic estimates.

**Global sign separation for \(0<\gamma<1\).** Now \(A>0\), and \(n\mapsto Q_{\infty,n}\) is strictly decreasing from above one. Let \(c_\gamma=\sqrt A\). For each fixed \(0<\varepsilon<c_\gamma\), (2)–(4) yield, for all sufficiently large \(m\),
\[
Q_{m,n}>1\quad(3\le n\le(c_\gamma-\varepsilon)\sqrt m),
\qquad Q_{m,n}<1\quad(n\ge(c_\gamma+\varepsilon)\sqrt m).
\tag{5}
\]
Indeed \(\log(1-m^{-1})=-m^{-1}+O(m^{-2})\); the lower bound uses the monotone positive quantity \(\log Q_{\infty,n}\), whose smallest value on the first interval is asymptotically \(A/((c_\gamma-\varepsilon)^2m)\). The upper bound uses \(\log Q_{\infty,n}\le A/[n(n+\gamma-3)]\) and the upper bound in (4), both decreasing in \(n\) on the second interval.

On the intermediate window \((c_\gamma-\varepsilon)\sqrt m\le n\le(c_\gamma+\varepsilon)\sqrt m\), extend (1) to real \(n>3\) with gamma functions. Differentiation of (3) gives
\[
\partial_n h_n(\gamma/m)=O_\gamma((mn^2)^{-1}+m^{-2}n^{-2}),
\]
using a second symmetric difference of the digamma function for the first logarithm. On this window, \(\partial_n\log Q_{\infty,n}=-2A/n^3+O_\gamma(n^{-4})\), which strictly dominates the correction: \(\partial_n\log Q_{m,n}<0\) for large \(m\). By (5) and continuity there is exactly one zero \(r_m\) in this window, and there are no zeros outside it. This proves the sign classification for all integer \(n\ge3\), including a possible equality at an integer root.

**Two-term location.** Uniformly when \(n\asymp\sqrt m\), Taylor expansion of (3), whose quadratic remainder is uniformly \(O_\gamma(m^{-2})\), gives
\[
\log Q_{m,n}=-m^{-1}+\frac{A}{n^2}
+\frac{A(3-\gamma)}{n^3}+\frac{3\gamma}{mn}+O_\gamma(m^{-2}).\tag{6}
\]
For \(n=c_\gamma\sqrt m+d\), with bounded \(d\), the right side is
\[
\frac{3+2\gamma-2d}{c_\gamma m^{3/2}}+O_\gamma(m^{-2}).\tag{7}
\]
The derivative is \(-2/(c_\gamma m^{3/2})+O_\gamma(m^{-2})\); thus the unique real root obeys \(r_m=c_\gamma\sqrt m+(3+2\gamma)/2+O_\gamma(m^{-1/2})\).

For any fixed \(\gamma>0\) and \(n_m/\sqrt m\to c>0\), the first two terms in (2) and (4) instead give \(m\log Q_{m,n_m}\to-1+A/c^2\), proving the general scaling statement. The positive factor \(m^2p_1p_2\) ensures that each sign conclusion transfers unchanged to covariance.

## Verification
The standalone `check.py` enumerates all Dirichlet-multinomial count vectors with exact rational weights for \(m\in\{3,4,5\}\), \(n\in\{3,\ldots,8\}\), and \(\alpha\in\{1/4,1/2,1,2\}\), checking 72 exact covariance identities. High-precision gamma-function evaluations additionally check nine real crossover roots for total masses \(\gamma\in\{0.1,0.5,0.9\}\) and \(m\in\{100,1000,10000\}\), including opposite signs on either side of the predicted centered threshold. These are finite corroborations; the all-size classification follows from inequalities (2)–(7).

## Relationship to prior work
Huillet's finite-Dirichlet sampling formulas (2005), restated as the full joint species-frequency law in Huillet–Paroissin (2008, Theorem 2.1), give the distributional foundation of (1). The fixed-sample Kingman/Ewens limit in that work recovers \(Q_{\infty,n}\), but does not state the growing-sample singleton–doubleton sign boundary or the \(O(1)\)-accurate finite-species cutoff. The present conclusion is a qualitative two-parameter asymptotic statement extracted from, rather than a replacement for, those classical formulas. Holmes–Harris–Quince (2012) motivates Dirichlet-multinomial modeling of species counts without identifying this covariance threshold. For comparison, iid uniform occupancy corresponds to a distinct fixed-probability model and does not yield this transition by parameter substitution.

## Limitations
Only fixed total concentration is considered; \(\gamma\) may not drift with \(m\) in the stated error bounds. The theorem asserts an eventual one-crossing property for \(0<\gamma<1\), not for every finite number of species. At \(\gamma\ge1\), only the negative sign throughout positive square-root sample scales is asserted, not a global sign classification for all sample sizes. The exact joint frequency law was known; novelty is limited to the specified covariance sign transition and its sharp finite-support correction. Equivalent asymptotic statements may be implicit in earlier sampling literature; no independent scientific audit has been performed.

## References
1. T. Huillet, *Sampling Formulae Arising from Random Dirichlet Populations*, Communications in Statistics: Theory and Methods 34 (2005), 1019–1040, doi:10.1081/STA-200056809. Earliest verified publication date: 2005-06-14.
2. T. Huillet and C. Paroissin, *Sampling from Dirichlet partitions: estimating the number of species*, arXiv:0809.4181, first submitted 2008-09-24; later Environmetrics 20 (2009), 853–876. Theorem 2.1, Sections 2.1–2.4.
3. I. Holmes, K. Harris, and C. Quince, *Dirichlet Multinomial Mixtures: Generative Models for Microbial Metagenomics*, PLoS ONE 7 (2012), e30126, doi:10.1371/journal.pone.0030126.
