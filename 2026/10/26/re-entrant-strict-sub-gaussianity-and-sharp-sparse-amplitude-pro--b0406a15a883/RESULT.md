# Re-entrant strict sub-Gaussianity and sharp sparse-amplitude proxy growth

## Finding
For any fixed real \(a\ge4\), let \(X_{a,p}\) be the symmetric four-atom law with mass \((1-p)/2\) at each of \(-1,1\) and mass \(p/2\) at each of \(-a,a\), for \(0\le p\le1\). Its variance and optimal Gaussian proxy variance are
\[
v_{a,p}=1+p(a^2-1),\qquad
s_a^2(p)=\sup_{t\ne0}\frac{2}{t^2}\log\left((1-p)\cosh t+p\cosh(at)\right).
\]

**Theorem.** For every \(a\ge4\), the parameter set \(\{p\in(0,1):s_a^2(p)=v_{a,p}\}\) contains an open interval adjacent to zero and another adjacent to one, but omits \(p_a=1/(2a^4)\). At this excluded parameter,
\[
\mathbb E[X_{a,p_a}^4]-3v_{a,p_a}^2<-\frac32,
\]
so negative fourth cumulant does not prevent a positive gap between optimal proxy and true variance. Moreover, as \(a\to\infty\),
\[
v_{a,p_a}\longrightarrow1,\qquad
\mathbb E[X_{a,p_a}^4]-3v_{a,p_a}^2\longrightarrow-\frac32,
\qquad s_a^2(p_a)\sim\frac{a^2}{8\log a}\longrightarrow\infty.
\]
Thus the strictly sub-Gaussian locus in mixing weight is disconnected, while the natural sparse-amplitude family has bounded fourth moment and unbounded Gaussian variance proxy. No assertion is made that there are exactly two components.

## Assumptions and scope
The distribution is centered and symmetric. All assertions concerning the disconnected locus hold for **every real** \(a\ge4\); endpoint neighborhoods depend on \(a\) and need not have uniform widths. The proxy parameter is the *smallest* \(s^2\) satisfying \(\mathbb E e^{tX_{a,p}}\le e^{s^2t^2/2}\) for all real \(t\). Equality of optimal proxy with the true variance is called strict sub-Gaussianity. The asymptotic takes \(a\to\infty\) with \(p=p_a\), not with fixed \(p\).

## Proof
**1. Moments and the excluded parameter.** Symmetry gives mean zero. Direct atom summation yields
\[
\mathbb E X_{a,p}^2=1+p(a^2-1),\qquad
\mathbb E X_{a,p}^4=1+p(a^4-1).
\]
At \(p=p_a=1/(2a^4)\), the second moment exceeds one and the fourth moment equals \(3/2-1/(2a^4)<3/2\). Hence the fourth cumulant is strictly less than \(-3/2\), and tends to that value as \(a\to\infty\), while the variance tends to one.

Set \(F(p,t)=\log[(1-p)\cosh t+p\cosh(at)]-v_{a,p}t^2/2\). At \(p=p_a\) and \(t=a\), the positive high-amplitude atom implies
\[
\log[(1-p_a)\cosh a+p_a\cosh(a^2)]>a^2-\log(4a^4).
\]
Because \(v_{a,p_a}a^2/2=a^2/2+(a^2-1)/(4a^2)\le a^2/2+1/4\),
\[
F(p_a,a)>g(a):=\frac{a^2}{2}-\frac14-\log(4a^4).
\]
For \(a\ge4\), \(g'(a)=a-4/a>0\) and \(g(4)=31/4-10\log2>0\). The latter follows, for instance, from \(\log2<3/4\), since \(e^{3/4}>1+3/4+(3/4)^2/2>2\). Thus \(F(p_a,a)>0\), meaning \(s_a^2(p_a)>v_{a,p_a}\), indeed with an explicit positive witness \(s_a^2(p_a)-v_{a,p_a}>2g(a)/a^2\).

**2. Endpoint intervals.** Fix \(a\ge4\). At \(p=0\), \(F(0,t)=\log\cosh t-t^2/2<0\) for every nonzero \(t\) because \(\tanh u<u\) for \(u>0\). Likewise \(F(1,t)=\log\cosh(at)-a^2t^2/2<0\). At these endpoints, the fourth derivative of \(F\) with respect to \(t\) at zero is respectively \(-2\) and \(-2a^4\). Since \(F\) is even and its value and first three derivatives at zero vanish for every \(p\), continuity of its fourth derivative provides \(\delta>0\) and endpoint weight neighborhoods on which \(F(p,t)<0\) for \(0<|t|<\delta\) (Taylor's theorem with integral remainder). On the compact region \(\delta\le|t|\le 2a+1\), strict endpoint inequalities and joint continuity give possibly smaller endpoint neighborhoods where \(F<0\). Finally, for \(|t|>2a\),
\[
(1-p)\cosh t+p\cosh(at)\le e^{a|t|}<e^{t^2/2}\le e^{v_{a,p}t^2/2},
\]
uniformly in \(p\in[0,1]\). Thus all nonzero \(t\) satisfy \(F(p,t)<0\) for weights sufficiently near zero or one; continuity gives that an open neighborhood of \(p_a\) fails at \(t=a\). The strict sub-Gaussian parameter set has nonempty parts on either side of a missing interior point, hence is disconnected.

**3. Sharp sparse-amplitude asymptotic.** Set \(p=p_a\) and \(L=\log(1/p)=\log(2a^4)\). Evaluating the proxy at \(t=2L/a\) and using the high-amplitude positive atom gives
\[
s_a^2(p_a)\ge\frac{a^2}{2L}\left(1-\frac{\log2}{L}\right).
\]
For a matching upper bound take \(a\) large enough that \(L/(2a)\le1\). When \(0\le t\le L/(2a)\), let \(M(t)=(1-p)\cosh t+p\cosh(at)\). The second derivative obeys
\[
M''(t)\le\cosh1+p a^2e^{L/2}=\cosh1+1/\sqrt2<3.
\]
Since \(M(0)=1\) and \(M'(0)=0\), twice integrating yields \(M(t)\le1+3t^2/2\), so \(2\log M(t)/t^2\le3\). For \(t\ge L/(2a)\), use \(\cosh t\le e^{t^2/2}\) and \(\cosh(at)\le e^{at}\). Then
\[
M(t)\le e^{t^2/2}+e^{at-L}\le2e^{\max\{t^2/2,at-L\}},
\]
which implies
\[
\frac{2\log M(t)}{t^2}\le
\max\left\{1,\frac{2a}{t}-\frac{2L}{t^2}\right\}
+\frac{8a^2\log2}{L^2}
\le\max\left\{1,\frac{a^2}{2L}\right\}+\frac{8a^2\log2}{L^2}.
\]
The second inequality maximizes the quadratic \(2au-2Lu^2\) over \(u=1/t>0\). As the law is symmetric, negative \(t\) contributes identically. Together with the small-\(t\) bound,
\[
\frac{a^2}{2L}\left(1-\frac{\log2}{L}\right)
\le s_a^2(p_a)
\le\max\left\{3,\frac{a^2}{2L}\right\}+\frac{8a^2\log2}{L^2}.
\]
Since \(L\sim4\log a\) and \(a^2/L\to\infty\), dividing by \(a^2/(2L)\) proves the asserted sharp asymptotic.

## Verification
Every inequality above is analytic and applies to the stated infinite range, without extrapolating from experiments. The accompanying `verify.py` computes exact rational second/fourth moments for integer amplitudes, tests the explicit moment-generating-function witness, and records the proxy asymptotic at its analytic evaluation point. The numerical results are consistency checks only, not the proof of either the endpoint intervals or the asymptotic.

## Relationship to prior work
Arbel–Marchal–Nguyen (2019), Sections 2–3, define the optimal proxy via the cumulant-generating function, prove a negative fourth cumulant is necessary for strict sub-Gaussianity, and construct a symmetric three-mass counterexample with *positive* fourth cumulant. The present four-atom two-radius family instead has a strictly negative fourth cumulant at the **failure** parameter, and exhibits disjoint strict regimes and a sharp divergent proxy under bounded fourth moments. Atouani–Marchal–Arbel (2025) thoroughly treat three-mass distributions, including a different single-scale threshold, not the four-atom reentrant structure or sparse-radius asymptotic. Their general methods do not supply the claimed parameter-specific theorem without the new argument above.

## Limitations
The exact number and endpoints of connected components are not determined. The asymptotic is restricted to \(p_a=1/(2a^4)\). The result does not establish novelty against all unindexed literature; it carries residual priority risk. No externally independent audit or validation has been performed.

## References
1. J. Arbel, O. Marchal, H. D. Nguyen, *On strict sub-Gaussianity, optimal proxy variance and symmetry for bounded random variables*, arXiv:1901.09188v1, first available 2019-01-26, https://arxiv.org/abs/1901.09188.
2. S. Atouani, O. Marchal, J. Arbel, *Optimal sub-Gaussian variance proxy for 3-mass distributions*, arXiv:2510.06132v1, first available 2025-10-07, https://arxiv.org/abs/2510.06132.
