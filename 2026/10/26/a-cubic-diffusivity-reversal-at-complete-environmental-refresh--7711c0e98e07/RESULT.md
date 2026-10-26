# A cubic diffusivity reversal at complete environmental refresh

## Finding
Consider the one-dimensional nearest-neighbor walk in an independent, identically distributed (iid) site environment, with the *entire* environment resampled independently after each step with probability \(p\in(0,1]\). Put \(B=2\omega_0-1\), where \(\omega_0\in[0,1]\) is a site's right-step probability, and write \(d=\mathbb EB\) and \(w=\operatorname{Var}(B)\). Write \(V(p)\) for the annealed central-limit variance per unit time and \(u(p)\) for the limiting speed.

**Theorem.** Uniformly over all laws of \(\omega_0\) on \([0,1]\), as \(\delta=1-p\downarrow0\),
\[
 u(1-\delta)=d-\tfrac12dw\,\delta^2+O(\delta^4),\qquad
 V(1-\delta)=1-d^2+3d^2w\,\delta^2-\tfrac12w^2\,\delta^3+O(\delta^4).
\]
For every nonconstant site law, \(p=1\) is a strict one-sided local **minimum** of \(V\) if \(d\ne0\), but a strict one-sided local **maximum** if \(d=0\). In the centered case the first two derivatives at \(p=1\) vanish while \(V'''(1^-)=3w^2>0\).

In a family of site laws depending on \(\delta\), if \(d_\delta/\sqrt\delta\to c\) and \(w_\delta\to w_0>0\), the sharp drift-disorder crossover is
\[
 \lim_{\delta\downarrow0}\frac{V_{\delta}(1-\delta)-V_{\delta}(1)}{\delta^3}
 =3c^2w_0-\tfrac12w_0^2.
\]
The limit is negative for \(|c|<\sqrt{w_0/6}\), positive for \(|c|>\sqrt{w_0/6}\), and the displayed order does not decide the boundary case.

For the canonical maximally disordered centered law \(\Pr(\omega_0=0)=\Pr(\omega_0=1)=1/2\), the diffusivity has the exact **global** formula, for every \(0<p\le1\),
\[
 \boxed{V(p)=\frac{p(3-p)^2}{(2-p)(1+p)^2}},\qquad
 \boxed{1-V(p)=\frac{2(1-p)^3}{(2-p)(1+p)^2}}.
\]
In particular \(V(p)<1\) for all \(0<p<1\) and \(V(p)\) is strictly increasing in \(p\). This exact example realizes the universal negative cubic coefficient \(-1/2\).

## Assumptions and scope
For each integer site \(x\) and refresh block \(k\), take \(\omega_x^{(k)}\) iid with common law on \([0,1]\), independently of refresh decisions. Starting at the origin, the walker at site \(x\) steps right with probability \(\omega_x^{(k)}\), otherwise left, until the next global refresh. After each step the environment is independently replaced with probability \(p\). The sequence of block lengths is iid geometric with \(\Pr(G=n)=p(1-p)^{n-1}\), \(n\ge1\). The annealed invariance principle at \(p>0\) follows from independent regeneration blocks with finite second moments. The stated \(V\) is the variance of its limiting normal distribution after subtracting \(nu(p)\), divided by \(n\). The endpoint \(p=0\) is not part of the theorem. Non-elliptic site laws are admissible for \(p>0\).

Let \(Z_n\) be the walk in one static iid environment, started at zero, and set \(m_n=\mathbb EZ_n\), \(s_n=\mathbb EZ_n^2\). Expectations include both walk randomness and the random environment. All claims concern the *annealed* variance, not quenched variances.

## Proof
**1. Regenerative generating functions.** The pairs \((G,Z_G)\) over successive refresh blocks are iid, each with \(G\) independent of its fresh environment. The renewal-reward law of large numbers and central limit theorem give, for \(\delta=1-p\),
\[
 u(p)=p\mathbb E Z_G=p^2\sum_{n\ge1}m_n\delta^{n-1},
 \quad V(p)=p\mathbb E[(Z_G-u(p)G)^2]
 =p^2\sum_{n\ge1}\mathbb E[(Z_n-nu(p))^2]\delta^{n-1}.
\]
The centering has zero mean per block. Since \(|Z_n|\le n\) and \(|u(p)|\le1\), these series and the required Taylor remainders converge uniformly for \(0\le\delta\le1/2\), uniformly over every site law.

**2. Four-step moment identities.** For any fixed step sequence \(\varepsilon_0,\ldots,\varepsilon_{n-1}\in\{-1,1\}\), set \(x_0=0\) and \(x_{j+1}=x_j+\varepsilon_j\). With \(B_x=2\omega_x-1\), independence by site gives the exact path probability
\[
 \mathbb P(\varepsilon_0,\ldots,\varepsilon_{n-1})
 =\prod_{x\in\mathbb Z}\mathbb E\!\left[\prod_{j:x_j=x}\frac{1+\varepsilon_j B_x}{2}\right].
\]
Enumerating the at most sixteen paths for \(n\le4\), and using \(\mathbb EB=d\), \(\mathbb EB^2=d^2+w\), yields
\[
\begin{array}{c|cc}
 n&m_n&s_n\\\hline
 1&d&1\\
 2&2d&2+2d^2\\
 3&3d-\frac12dw&3+6d^2\\
 4&4d-dw&4+12d^2-2d^2w-\frac12w^2.
\end{array}
\]
No higher site moments enter: no site is departed more than twice on a path of at most four steps. The bundled symbolic verifier independently enumerates these paths and verifies every table entry.

**3. Uniform cubic expansion.** Substitute the first column into the speed generating function. The first four terms give \(u(1-\delta)=d-\frac12dw\delta^2+O(\delta^4)\); the coefficient of \(\delta^3\) cancels exactly. In the variance series, replacing \(u(p)\) by \(d\) changes coefficients through degree three by zero: for \(n=1,2\) the relevant centered means \(m_n-nd\) vanish and the correction is quadratic in \(u-d\); for \(n\ge3\) the factor \(\delta^{n-1}\) makes its contribution order at least four.

Indeed put \(a_n=\mathbb E[(Z_n-nd)^2]\). The table yields
\[
 a_1=1-d^2,\quad a_2=2(1-d^2),\quad
 a_3=3(1-d^2)+3d^2w,\quad
 a_4=4(1-d^2)+6d^2w-\tfrac12w^2.
\]
Multiplying \((1-\delta)^2\sum_{n=1}^4 a_n\delta^{n-1}\) and collecting powers through degree three gives exactly the claimed variance expansion. For \(n\ge5\) the tail is bounded by \(4\sum_{n\ge5}n^2\delta^{n-1}=O(\delta^4)\) uniformly. The speed remainder follows from \(|m_n|\le n\). Consequently all remainder bounds are uniform in the site law.

When \(w>0\), for a fixed nonzero \(d\) the positive quadratic term determines the one-sided sign; for \(d=0\) the negative cubic term determines it. Uniformity permits substituting a \(\delta\)-dependent law to obtain the crossover limit. Differentiating the convergent generating series at \(p=1\) gives \(V'''(1^-)=3w^2\) in the centered case.

**4. Exact fair-arrow benchmark.** If every site has an independently chosen deterministic right/left arrow, each fair, reflection symmetry gives \(u(p)=0\). Conditional on the first arrow pointing right, let \(J\ge1\) be the first positive site whose arrow points left. Then \(\Pr(J=j)=2^{-j}\); the walk moves to site \(j\) by time \(j\) and subsequently alternates between \(j\) and \(j-1\). The opposite initial arrow has the reflected trajectory and identical squared displacement. Thus the second-moment generating function of the *static* walk equals
\[
\begin{aligned}
 F(z)&=\sum_{n\ge1}\mathbb EZ_n^2 z^{n-1}\\
 &=\sum_{j\ge1}2^{-j}\left[\sum_{n=1}^j n^2z^{n-1}+
 \frac{z^j((j-1)^2+j^2z)}{1-z^2}\right]\\
 &=\frac{(1+z/2)^2}{(1-z/2)^2(1-z^2)}.
\end{aligned}
\]
The geometric-block formula now gives \(V(p)=p^2F(1-p)\), which simplifies to the two boxed rational identities. The strict inequality follows from the positive exact expression for \(1-V(p)\). For monotonicity, differentiate with \(z=1-p\):
\[
 \frac{d}{dz}V(1-z)=\frac{6z^2(z+2)}{(z-2)^3(z+1)^2}<0\qquad(0<z<1).
\]
This completes the proof.

## Verification
The standalone `verify.py` enumerates all annealed paths of lengths one through four in a polynomial ring over the first two site-bias moments. It checks normalized path probabilities, each displayed moment identity, the complete cubic expansions, and the fair-arrow rational generating function and all-refresh variance. Run `python verify.py` with the dependency declared in `requirements.txt`. The checks passed on the packaged source. The general statements are proved analytically above; symbolic computation is supplementary.

## Relationship to prior work
Martin and Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1 (first public 2026-10-08), introduce the iid global refresh model and obtain its exact regenerative variance series (their Eq. (3.15)) and the second derivative \(V''(1)=24(\mathbb EZ_1)^2\operatorname{Var}(\omega_0)\). Their theorem asserts a local variance minimum for nonzero average step bias. This result **uses** that regenerative series, but evaluates the next universal coefficient, proves the opposite local behavior at zero bias, identifies a drift-disorder transition window, and solves the fair-arrow specialization globally. No new central limit theorem is claimed.

Avena and den Hollander, *Random walks in cooling random environments*, arXiv:1610.00641v1, and Avena–Chino–da Costa–den Hollander, *Random walk in cooling random environment: ergodic limits and concentration inequalities*, arXiv:1803.03295v1, treat deterministic cooling schedules, rather than the fixed-parameter geometric global-refresh law; they provide useful regeneration context, not the present coefficient or rational benchmark.

## Limitations
The cubic expansion is a high-refresh asymptotic, not a global monotonicity theorem for arbitrary site laws. On the crossover boundary \(|c|=\sqrt{w_0/6}\), higher-order terms determine the sign. The exact all-\(p\) formula concerns the fair deterministic-arrow law only; it does not imply global slowdown for every centered random environment. The independent validity of the regenerative central limit theorem follows from standard iid block arguments. The findings have not received independent scientific validation. Equivalence to an older unstated consequence of general renewal formulas remains possible.

## References
1. Raphael Martin and Jan Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1, 2026-10-08, https://arxiv.org/html/2610.11919.
2. Luca Avena and Frank den Hollander, *Random walks in cooling random environments*, arXiv:1610.00641v1, 2016-10-03, https://arxiv.org/abs/1610.00641.
3. Luca Avena, Yuki Chino, Conrado da Costa and Frank den Hollander, *Random walk in cooling random environment: ergodic limits and concentration inequalities*, arXiv:1803.03295v1, 2018-03-08, https://arxiv.org/abs/1803.03295.
