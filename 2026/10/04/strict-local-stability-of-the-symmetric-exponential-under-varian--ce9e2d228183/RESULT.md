# Strict local stability of the symmetric exponential under variance normalization
## Finding
Let \(1<p<2\), let \(E,E'\) be independent standard exponential random variables, and define
\[
Z_s=s(E-1)-(1-s)(E'-1),\qquad 0\le s\le1.
\]
For
\[
R_p(s)=\frac{\|Z_s\|_p}{\|Z_s\|_2},
\]
the symmetric point \(s=1/2\) satisfies the exact logarithmic Hessian identity
\[
\left.\frac{d^2}{ds^2}\log R_p(s)\right|_{s=1/2}
=\frac{4(2-p)^2}{p}>0.
\]
Consequently the symmetric two-sided exponential is a strict local minimizer of the variance-normalized \(L_p\) ratio throughout the entire unresolved interval \(1<p<2\). In particular, the conjectured global change from the symmetric to the one-sided exponential near \(p\approx1.68\) cannot be produced by a loss of local stability of the symmetric candidate; if that global change occurs, it is a competition between separated minima rather than a local bifurcation at \(s=1/2\).

## Assumptions and scope
The statement concerns only Eitan's complete one-parameter reduction \(Z_s\) for centered log-concave random variables. It does not determine the global minimizer of \(R_p\), locate the conjectured transition exponent, or prove that only the two endpoint types compete globally.

Write \(s=1/2+t\), and put
\[
S=E+E',\qquad D=E-E'.
\]
Then
\[
Z_{1/2+t}=\frac D2+t(S-2).
\]
The change of variables from \((E,E')\) to \((S,D)\) has joint density \(e^{-S}/2\) on \(S>0\) and \(|D|<S\).

## Proof
Set
\[
M_p(t)=\mathbb E\left|\frac D2+t(S-2)\right|^p.
\]
For each fixed \(r>0\), define
\[
J_r(t)=\int_{-r}^{r}\left|\frac d2+t(r-2)\right|^p\,dd.
\]
Because \(1<p<2\), the weak second derivative of \(|x|^p\) is the locally integrable function \(p(p-1)|x|^{p-2}\). Hence \(J_r\) is twice continuously differentiable and
\[
J_r''(t)=p(p-1)(r-2)^2\int_{-r}^{r}\left|\frac d2+t(r-2)\right|^{p-2}\,dd.
\]
The singular kernel is integrable and, uniformly in its translation,
\[
\int_{-r}^{r}\left|\frac d2+a\right|^{p-2}\,dd
\le \frac{2^{3-p}}{p-1}r^{p-1}.
\]
Indeed, after the substitution \(x=d/2\), an interval of fixed length has maximal integral against the even decreasing kernel \(|x|^{p-2}\) when centered at the origin. The resulting majorant is integrable against \((r-2)^2e^{-r}\,dr\). Dominated convergence therefore permits two differentiations under the outer integral
\[
M_p(t)=\frac12\int_0^\infty e^{-r}J_r(t)\,dr.
\]
At \(t=0\), oddness in \(d\) gives \(M_p'(0)=0\), while
\[
\begin{aligned}
M_p''(0)
&=p\,2^{2-p}\int_0^\infty r^{p-1}(r-2)^2e^{-r}\,dr\\
&=2^{2-p}\Gamma(p+1)\bigl(p^2-3p+4\bigr).
\end{aligned}
\]
Also
\[
M_p(0)=2^{-p}\Gamma(p+1).
\]
Therefore
\[
\left.\frac{d^2}{dt^2}\log\|Z_{1/2+t}\|_p\right|_{t=0}
=\frac1p\frac{M_p''(0)}{M_p(0)}
=\frac{4(p^2-3p+4)}p.
\]
On the other hand, independence and unit variances give
\[
\|Z_{1/2+t}\|_2^2=\left(\frac12+t\right)^2+\left(\frac12-t\right)^2
=\frac12+2t^2,
\]
so
\[
\left.\frac{d^2}{dt^2}\log\|Z_{1/2+t}\|_2\right|_{t=0}=4.
\]
Subtracting yields
\[
\left.\frac{d^2}{dt^2}\log R_p(1/2+t)\right|_{t=0}
=\frac{4(p^2-4p+4)}p
=\frac{4(2-p)^2}{p}>0.
\]
Since \(R_p(s)=R_p(1-s)\), the first derivative at \(s=1/2\) vanishes. The positive second derivative proves strict local minimality.

## Verification
The proof is analytic for every real \(1<p<2\). The only singular differentiation is justified by the explicit translated-kernel bound above, so no finite experiment is used to infer the all-\(p\) statement. The companion script `verify_hessian.py` independently checks the polynomial and Gamma-recurrence algebra and compares the predicted Hessian with direct deterministic quadrature of the defining moment integral at representative exponents. Running it produces `VERIFY_OK`.

## Relationship to prior work
Eitan proved that sharp centered log-concave moment-ratio problems reduce to the family \(Z_s\); his paper also solves certain even-integer norm-ratio maximization problems, but it does not state this variance-normalized local Hessian for \(1<p<2\). Melbourne, Roysdon, Tang, and Tkocz explicitly leave the variance-constrained problem open and, from numerical evidence, conjecture a global switch from the symmetric to the one-sided exponential near \(p\approx1.68\). Their statement supplies the motivating global question; the calculation here resolves the local stability mechanism at the symmetric candidate over the whole open interval.

## Limitations
No global optimality is claimed. The calculation does not determine the transition exponent, exclude additional nonsymmetric local minima, or compare their objective values. The novelty assessment is based on targeted database searches and full-text inspection of the two most directly relevant sources; an unindexed note could in principle contain the same local calculation.

## References
1. J. Melbourne, M. Roysdon, C. Tang, T. Tkocz, *From simplex slicing to sharp reverse Hölder inequalities*, arXiv:2505.00944. Earliest public version: 2025-05-02. See Section 3.1 for the variance-constrained open problem.
2. Y. Eitan, *The centered convex body whose marginals have the heaviest tails*, arXiv:2110.14382. See Section 3 for the one-parameter two-sided exponential reduction.
