# The sharp five-halves onset of nonmonotone norms in a self-adjoint block pencil

## Finding

For real parameters \(\alpha>0\), \(b>0\), and \(t\geq0\), consider the real self-adjoint matrix
\[
M_{\alpha,b}(t)=\begin{pmatrix}-b&t\\t&bt^\alpha\end{pmatrix},\qquad
F_{\alpha,b}(t)=\|M_{\alpha,b}(t)\|_{\ell_2^2\to\ell_2^2}.
\]
The complete monotonicity diagram is as follows.

* If \(0<\alpha\leq4\), the function \(F_{\alpha,b}\) is strictly increasing on \([0,\infty)\) for every \(b>0\).
* If \(\alpha>4\), put \(b_c(\alpha)=2/\sqrt{\alpha(\alpha-4)}\). The same strict increase holds for \(b\leq b_c(\alpha)\). For \(b>b_c(\alpha)\), there is exactly one \(t_*\in(0,1)\) such that \(F_{\alpha,b}\) increases strictly on \([0,t_*]\), decreases strictly on \([t_*,1]\), and increases strictly on \([1,\infty)\). The location \(t_*\) is uniquely determined by
\[
\alpha b^2t_*^{\alpha-2}\big[(\alpha-2)t_*^\alpha-2\big]=4.
\]

Define the maximum **backward norm overshoot** at the unit interface by
\[
\Delta(\alpha)=\sup_{b>0}\max_{0\leq t\leq1}
\big(F_{\alpha,b}(t)-F_{\alpha,b}(1)\big)_+,
\qquad (u)_+=\max\{u,0\}.
\]
Then \(\Delta(\alpha)=0\) for \(0<\alpha\leq4\), whereas \(\Delta(\alpha)>0\) and its supremum is attained when \(\alpha>4\). The exact critical asymptotic is
\[
\boxed{\displaystyle\lim_{\varepsilon\downarrow0}
\frac{\Delta(4+\varepsilon)}{\varepsilon^{5/2}}
=\frac1{100\sqrt5}.}
\]
If \((b_\varepsilon,t_\varepsilon)\) is any maximizing pair for \(\Delta(4+\varepsilon)\), its parameters obey the sharp scaling laws
\[
\boxed{\quad\sqrt\varepsilon\,b_\varepsilon\longrightarrow\sqrt5,
\qquad\frac{1-t_\varepsilon}{\varepsilon}\longrightarrow\frac1{10}.\quad}
\]

## Assumptions and scope

All matrices are \(2\times2\) operators on a real or complex Euclidean two-space; the norm is the usual spectral/operator norm, not the entrywise maximum norm. Both \(\alpha\) and \(b\) range over all positive real values. At \(t=0\), define \(t^\alpha=0\). The term 'overshoot' compares parameter values \(0\leq t\leq1\) with the common reference \(t=1\); it is not a supremum over \(t>1\), where the norm is unbounded. The statements about the maximizing pair apply to every selection of global maximizers; no uniqueness at fixed positive \(\varepsilon\) is asserted.

## Proof

**1. Exact norm and stationary equation.** With \(m=t^\alpha\), the two eigenvalues of \(M_{\alpha,b}(t)\) are
\[
\lambda_\pm(t)=\frac{b(m-1)\pm\sqrt{b^2(1+m)^2+4t^2}}2.
\]
Thus, on \([0,1]\),
\[
F_{\alpha,b}(t)=\frac{b(1-m)+\sqrt{b^2(1+m)^2+4t^2}}2=b+u(t),
\]
where \(u(t)>0\) for \(t>0\) is the unique positive solution of
\[
u\big(b(1+t^\alpha)+u\big)=t^2.
\]
Implicit differentiation shows
\[
\operatorname{sgn} F'_{\alpha,b}(t)
=\operatorname{sgn}\left(2+2\frac{u(t)}b-(\alpha-2)t^\alpha\right)
\qquad(0<t<1).
\]
For \(t\geq1\), the positive eigenvalue has the larger absolute value, and its explicit expression is strictly increasing in \(t\). Therefore all possible decreases lie in \((0,1)\).

**2. Complete monotonicity diagram.** For \(\alpha\leq4\), the displayed derivative sign is strictly positive because \(t^\alpha<1\) for \(0<t<1\). Suppose \(\alpha>4\). It remains positive when
\(t\leq t_0=(2/(\alpha-2))^{1/\alpha}\). For \(t_0<t<1\), its sign changes precisely when
\[
 b^2=\frac4{\alpha t^{\alpha-2}((\alpha-2)t^\alpha-2)}=:B_\alpha(t)^2.
\]
Indeed, at derivative zero one has \(u/b=((\alpha-2)t^\alpha-2)/2\); substituting this identity into the defining quadratic for \(u\) gives the expression above, and each implication is reversible. The function \(B_\alpha(t)\) decreases strictly from infinity to \(2/\sqrt{\alpha(\alpha-4)}\) as \(t\) increases from \(t_0\) to \(1\). For fixed \(t\), the ratio \(u/b\) decreases strictly with \(b\); hence \(F'<0\) precisely when \(b>B_\alpha(t)\). This proves all claimed strict-monotonicity intervals, existence and uniqueness of \(t_*\), and the stationary equation.

**3. Localization of positive overshoot.** Set \(R=\sqrt{b^2+1}=F_{\alpha,b}(1)\). Since \(R>b\), substituting \(R\) into the quadratic equation for \(F=b+u\) shows, for \(0<t<1\),
\[
F_{\alpha,b}(t)>R
\quad\Longleftrightarrow\quad
\frac{t^2-t^\alpha}{1-t^2}>\frac Rb.
\]
For \(\alpha=4+\varepsilon\), \(\varepsilon>0\), the elementary secant-slope inequality
\[
\frac{1-x^p}{1-x}\leq p\qquad(0<x<1,\ p\geq1)
\]
with \(x=t^2\) and \(p=(\alpha-2)/2=1+\varepsilon/2\) gives
\[
1<\frac Rb< \frac{t^2-t^\alpha}{1-t^2}
\leq t^2(1+\varepsilon/2).
\]
Consequently every positive overshoot occurs only when
\[
 b>\frac2{\sqrt{\varepsilon(4+\varepsilon)}},
\qquad t> (1+\varepsilon/2)^{-1/2}.
\]
Writing \(b=\beta/\sqrt\varepsilon\) and \(t=1-s\varepsilon\), any positive overshoot therefore has \(\beta\geq2/\sqrt{4+\varepsilon}\) and \(0\leq s\leq1/4+O(\varepsilon)\). This localization is uniform over **all** candidates, not merely stationary points.

**4. Uniform expansion.** For \(b\) sufficiently large and \(t\) in a fixed neighborhood of \(1\), expanding the positive quadratic root gives
\[
F_{\alpha,b}(t)=b+
\frac{G_\alpha(t)}b-
\frac{H_\alpha(t)}{b^3}+
\mathcal R_{\alpha,b}(t),
\]
where
\[
G_\alpha(t)=\frac{t^2}{1+t^\alpha},\qquad
H_\alpha(t)=\frac{t^4}{(1+t^\alpha)^3},\qquad
|\partial_t\mathcal R_{\alpha,b}(t)|\leq Cb^{-5}
\]
for all \(\alpha\) sufficiently close to \(4\), uniformly in \(t\) near \(1\) and \(b\) above a fixed positive threshold. The remainder estimate follows by writing the root as
\(b(1+t^\alpha)\sqrt{1+4t^2/(b^2(1+t^\alpha)^2)}\) and differentiating the convergent Taylor remainder in its small argument.

Uniformly for bounded \(s\geq0\), direct Taylor expansion at \((\alpha,t)=(4,1)\) yields
\[
G_{4+\varepsilon}(1-s\varepsilon)-G_{4+\varepsilon}(1)
=\varepsilon^2\left(\frac s4-s^2\right)+O(\varepsilon^3),
\]
\[
H_{4+\varepsilon}(1-s\varepsilon)-H_{4+\varepsilon}(1)
=\frac{s\varepsilon}4+O(\varepsilon^2).
\]
Here \(G_\alpha(1)=1/2\), \(H_\alpha(1)=1/8\),
\(\partial_tG_{4+\varepsilon}(1)=-\varepsilon/4\),
\(\partial_t^2G_4(1)=-2\), and \(\partial_tH_4(1)=-1/4\).
Combining these identities, for every localized positive candidate,
\[
\frac{F_{4+\varepsilon,\beta/\sqrt\varepsilon}(1-s\varepsilon)
-F_{4+\varepsilon,\beta/\sqrt\varepsilon}(1)}{\varepsilon^{5/2}}
=L(\beta,s)+O(\varepsilon),
\]
where the error is **uniform** for \(\beta\geq2/\sqrt{4+\varepsilon}\), \(0\leq s\leq1/4+O(\varepsilon)\), and
\[
L(\beta,s)=\frac{s}{\beta}\left(\frac14-s\right)-\frac{s}{4\beta^3}
=\frac{s(\beta^2-1)}{4\beta^3}-\frac{s^2}{\beta}.
\]
The uniformity for unbounded \(\beta\) follows because all remainder terms are bounded by constants times \(\varepsilon/\beta\), \(\varepsilon/\beta^3\), and \(\varepsilon^2/\beta^5\), and \(\beta\) has a positive lower bound.

**5. Sharp optimization and maximizers.** For \(\beta\leq1\), \(L(\beta,s)\leq0\). For \(\beta>1\), the unique optimal \(s\) is
\[
s_\beta=\frac{\beta^2-1}{8\beta^2},
\qquad \max_{s\geq0}L(\beta,s)
=\frac{(\beta^2-1)^2}{64\beta^5}.
\]
The last expression has its unique positive maximum at \(\beta=\sqrt5\), where \(s_\beta=1/10\) and the value is \(1/(100\sqrt5)\). Because this optimizer satisfies all localization constraints strictly for small positive \(\varepsilon\), the explicit admissible trial
\(b=\sqrt{5/\varepsilon}\), \(t=1-\varepsilon/10\) supplies the matching lower limit. The uniform expansion supplies the upper limit. Any maximizing pair must approach the unique optimizer of \(L\): sequences with \(\beta\to\infty\), \(\beta\to1\), or \(s\to0\) have limiting value zero, strictly below the positive optimal coefficient. This proves both parameter limits.

To see that an actual maximum exists for each fixed \(\alpha>4\), note that the phase diagram supplies a positive candidate; the overshoot is zero for \(b\leq b_c(\alpha)\), while its supremum over \(0\leq t\leq1\) tends uniformly to zero as \(b\to\infty\), by the displayed quadratic-root expansion for fixed \(\alpha\). Continuity on the remaining compact parameter strip completes the existence proof.

## Verification

The accompanying `checker.py` is a stand-alone Python-standard-library script. It tests the exact fifth-power stationary polynomial identity, the quadratic-root equation, sampled monotonicity and overshoot regimes, uniqueness of sampled interior maxima, and convergence toward the universal critical coefficient. Run `python3 checker.py` in the directory containing that file. These are finite cross-checks; the proof for all real parameters and the asymptotic supremum are analytical and do not rely on sampling.

## Relationship to prior work

Wu, Ling, and Xu (2026) establish the universal exponent-four monotonicity criterion for a broader nonsymmetric matrix family, prove nonmonotonicity is possible above four, and analyze the single concrete matrix \(\bigl(\begin{smallmatrix}-2&t\\t&2t^5\end{smallmatrix}\bigr)\). Those results are prior work. The present claim determines the complete \((\alpha,b)\) phase diagram inside the canonical symmetric family and, more substantially, its globally optimized critical onset with exponent \(5/2\), exact coefficient, and optimizer scaling. Substituting \(\alpha=5\), \(b=2\) into the new stationary equation recovers the polynomial equation in their Example 2.1; that single instance does not give the two-parameter classification or uniform sharp asymptotic. The earlier generalized-quadratic-operator literature treats constant diagonal blocks and does not cover the moving nonlinear diagonal \(bt^\alpha\).

## Limitations

The critical expansion concerns the reference interval \(0\leq t\leq1\) and a real self-adjoint two-parameter family, not all complex parameters in the general matrix theorem. It proves only the leading \(5/2\)-power coefficient, not a complete series at the critical exponent. It does not assert a formula for arbitrary operator-valued \(A\), universal nonmonotonicity beyond the chosen family, or independence from every possible earlier calculus-based treatment. No independent mathematical review has been performed.

## References

1. K. Wu, J. Ling, Q. Xu, *Norm attainment of a class of block operator matrices*, arXiv:2605.25283 (first public version May 24, 2026), especially Theorem 2.1, Corollary 2.3, Example 2.1, and Theorem 3.6. https://arxiv.org/abs/2605.25283
2. K. Wu and Q. Xu, *The numerical ranges of the generalized quadratic operators*, arXiv:2511.04313 (November 6, 2025), especially Sections 1–2. https://arxiv.org/abs/2511.04313
3. C.-K. Li, Y.-T. Poon, M. Tominaga, *Spectra, norms and numerical ranges of generalized quadratic operators*, Linear and Multilinear Algebra 59 (2011), 1077–1104, DOI:10.1080/03081087.2010.483473. https://doi.org/10.1080/03081087.2010.483473
