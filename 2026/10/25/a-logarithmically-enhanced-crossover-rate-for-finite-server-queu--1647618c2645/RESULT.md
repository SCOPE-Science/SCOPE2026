# A logarithmically enhanced crossover rate for finite-server queues supplied by a resetting searcher

## Finding

For a diffusive search-and-capture process supplying a finite-server queue, the resetting rate at which the queue's zero-reset critical starting position recovers its original stability boundary is **quadratic in the server count, multiplied by a squared logarithm**. More precisely, fix diffusion coefficient \(D>0\), interval length \(L>0\), and service rate per server \(\mu>0\). Let \(c\) be an integer server count, and write
\[
 a=\frac{c\mu L^2}{D},\qquad H=\log a,\qquad J=\log H.
\]
For every \(a>5/2\), put
\[
 x_c=L\left(1-\sqrt{1-\frac2a}\right).
\]
Every strictly positive solution \(r=r_e(c)\) of the exact mean-first-passage crossover equation
\[
 T_r(x_c)=T_0(x_c)=\frac1{c\mu}
\]
exists, and **all such positive solutions**, whether or not a uniqueness statement is imposed at finite \(c\), obey
\[
 \boxed{\frac{\sqrt{D r_e(c)}}{c\mu L}
 = H+2J+\frac{4J}{H}
 +O\left(\frac{J^2}{H^2}\right)}
 \qquad(c\longrightarrow\infty).
\]
Consequently,
\[
 \boxed{r_e(c)\sim \frac{(c\mu L)^2}{D}\left[\log\left(\frac{c\mu L^2}{D}\right)\right]^2.}
\]
The correction \(2\log\log a\) is unbounded and must be retained for an accurate asymptotic approximation of the normalized square-root rate.

## Assumptions and scope

The searcher is a one-dimensional Brownian motion with diffusion coefficient \(D\) on \([0,L]\), absorbed at \(0\) and reflected at \(L\). Independent Poisson resets at rate \(r\) return it instantaneously to its starting point \(x\); there is no capture/refractory delay. Captures feed a \(G/M/c\) queue with \(c\) statistically identical exponential servers of service rate \(\mu\). The search's renewal mean determines the interarrival mean; the queue stability boundary is \(c\mu T_r(x)=1\). All parameters \(D,L,\mu\) are fixed as integer \(c\to\infty\). The claim is about the positive reset-rate crossing at the **zero-reset critical position** \(x_c\), not about an arbitrary initial position or the maximum shrinkage rate.

The exact search mean (previously established) is
\[
 T_r(x)=\frac1r\left[\frac{\cosh(L\sqrt{r/D})}{\cosh((L-x)\sqrt{r/D})}-1\right],\qquad
 T_0(x)=\frac{x(2L-x)}{2D}.
\]
These formulas yield \(T_0(x_c)=1/(c\mu)\) whenever \(a>2\). The stronger assumption \(a>5/2\) makes the crossing nontrivial by ensuring resetting initially **reduces** this mean before sufficiently strong resetting increases it.

## Proof

Define
\[
 b=\sqrt{1-2/a},\quad \epsilon=1-b=\frac{2}{a(1+b)},\quad
 \theta=L\sqrt{r/D},\quad u=\epsilon\theta.
\]
The crossover equation is equivalent to
\[
 \frac{\cosh\theta}{\cosh(b\theta)}-1=\frac{\theta^2}{a}.
 \tag{1}
\]
The expansion at the origin is
\[
 \frac{\cosh\theta}{\cosh(b\theta)}-1-\frac{\theta^2}{a}
 =\frac{(1-b^2)(1-5b^2)}{24}\theta^4
 +O\big((1-b^2)\theta^6\big),\quad\theta\downarrow0.
 \tag{2}
\]
For \(a>5/2\), \(b^2>1/5\), so the leading coefficient is strictly negative. Conversely, for fixed \(a>5/2\), as \(\theta\to\infty\), the left ratio in (1) grows exponentially like \(e^{\epsilon\theta}\), outgrowing the polynomial right side. Continuity gives at least one finite, positive solution.

The hyperbolic addition law rewrites (1) **exactly** as
\[
 \cosh u-1+\tanh(b\theta)\sinh u
 =C_a u^2,\qquad C_a=\frac1{a\epsilon^2}
 =\frac{a(1+b)^2}{4}=a(1+O(a^{-1})).
 \tag{3}
\]
We show that \(u\to\infty\) along **every** sequence of positive roots as \(a\to\infty\). Suppose instead that a sequence has bounded \(u\). Dividing (3) by \(u>0\) and using \(0\le\tanh(b\theta)\le1\) bounds the left side by a constant depending only on the upper bound for \(u\). But \(C_au=\theta/(a\epsilon)\) and \(a\epsilon=2/(1+b)\to1\), so \(\theta\) would remain bounded. If a subsequence has \(\theta\to\theta_0>0\), division of (1) by \(\epsilon\), followed by \(a\to\infty\), gives \(\theta_0\tanh\theta_0=\theta_0^2\), impossible because \(\tanh t<t\) for \(t>0\). If instead \(\theta\to0\), the expansion (2), uniform for \(b\) sufficiently near one, is strictly negative for small positive \(\theta\), again contradicting a root. Thus \(u\to\infty\).

Now \(b\theta=b u/\epsilon\to\infty\) extremely rapidly. Writing \(\delta=1-\tanh(b\theta)\), one has \(0\le\delta\le2e^{-2b\theta}\), and (3) becomes
\[
 e^u-1-\delta\sinh u=C_a u^2.
 \tag{4}
\]
Since \(u\to\infty\), the exponentially small \(\delta\) is negligible, and (4) implies
\[
 e^u=C_a u^2(1+o(1)).
\]
More quantitatively, the same equation and \(C_a\asymp a\) give \(e^{-u}=O((au^2)^{-1})\) and the negligible correction \(\delta=O(e^{-2bu/\epsilon})\). Taking logarithms yields
\[
 u-2\log u=\log a+O(a^{-1}).
 \tag{5}
\]
Here \(u\to\infty\) is on the large branch of the inverse; the function \(s\mapsto s-2\log s\) is strictly increasing for \(s>2\). First, (5) forces \(u=H+O(J)\). Substituting the ansatz \(u=H+2J+\eta\) and expanding the logarithm gives
\[
 \eta=\frac{4J}{H}+O\left(\frac{J^2}{H^2}\right).
\]
Finally,
\[
 \frac{\sqrt{D r}}{c\mu L}=\frac{\theta}{a}=\frac{u}{a\epsilon},
 \qquad a\epsilon=\frac2{1+b}=1+O(a^{-1}).
\]
Thus replacing \(u\) by the normalized square-root rate perturbs the expansion only by \(O(H/a)\), which is absorbed in the displayed error. This establishes the stated asymptotic for every positive crossover root and its squared-rate consequence. It does **not** require or prove finite-\(c\) uniqueness.

## Verification

Run `python verify.py` with Python 3 and the `mpmath` package. The standalone program uses 90-digit precision, brackets and bisects the positive root, checks two independent hyperbolic evaluations of the mean first-passage equation, confirms the root changes sign, and tests dimensionless invariance under independent changes of physical units. It passed 13 root cases from one through ten billion servers and eight matched-parameter rescalings. Numerical convergence of the logarithmic expansion is slow as predicted; this finite suite corroborates the exact analysis but is **not** an all-dimensional proof.

## Relationship to prior work

Giral-Barajas and Bressloff (2026) derived the search mean \(T_r\), zero-reset critical site \(x_c\), finite-server queue-stability condition, and an implicit definition of the equalizing reset rate, and supplied numerical growth fits. None of those underlying identities are claimed as new. Their study motivates the need for an asymptotic scaling at large server counts; the present statement identifies the precise squared-logarithmic enhancement, plus the iterated-logarithm corrections, which is not stated in the examined source. Giral-Barajas and Bressloff (2025) studied the underlying search-fed \(G/M/c\) queue without resetting. General high-reset first-passage asymptotics are also established in other work, but extracting this particular moving-boundary crossover requires solving the coupled limit \(x_c\downarrow0\), \(r\uparrow\infty\), and \(c\uparrow\infty\).

## Limitations

This result assumes a finite reflecting interval, reset location equal to the starting position, instantaneous resets and capture, Poisson reset clocks, fixed positive \(D,L,\mu\), and integer server count tending to infinity. It does not prove uniqueness of the positive crossover at each finite count, describe other interval geometries or nonzero refractory times, or determine a finite-server error constant uniform over all parameters. The asymptotic coefficient and corrections are mathematical statements about a previously derived exact mean, not independently measured queue data. A broader published theorem on coupled resetting/queue limits may imply this result without naming these parameters; independent priority assessment is outstanding.

## References

1. J. Giral-Barajas and P. C. Bressloff, *Resetting-induced instability in queues fed by a search process in an interval*, arXiv:2602.05009 (first public posting 2026-02-04); *Physical Review E* **113**, 064101 (2026), DOI: 10.1103/pzz6-3hzf.
2. J. Giral-Barajas and P. C. Bressloff, *Stochastic 1D search-and-capture as a G/M/c queueing model*, arXiv:2503.21883 (2025), *Journal of Physics A: Mathematical and Theoretical* **58**, 355001 (2025).
3. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, *Physical Review E* **108**, 024114 (2023), DOI: 10.1103/PhysRevE.108.024114.
