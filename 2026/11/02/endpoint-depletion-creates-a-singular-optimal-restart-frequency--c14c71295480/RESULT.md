# Endpoint depletion creates a singular optimal restart frequency in circular Brownian search

## Finding

Let a Brownian particle with generator \(D\partial_{xx}\), \(D>0\), move on a circle of circumference \(L>0\), with perfect absorption at one point. Unwrap the circle as \((0,L)\) with absorbing endpoints. The initial position and every independently redrawn position after a complete rate-\(r\) Poisson reset have the same density
\[
 f_\alpha(x)=\frac{[x(L-x)]^\alpha}{L^{2\alpha+1}B(\alpha+1,\alpha+1)},\qquad 0<x<L,\quad \alpha>-1.
\]
Set \(k=L\sqrt{r/D}\) and \(F_\alpha(k)=2\,{}_1F_1(\alpha+1;2\alpha+2;-k)/(1+e^{-k})\). The mean time to absorption is exactly
\[
 T_\alpha(r)=\frac{L^2}{D}\frac{1-F_\alpha(k)}{k^2F_\alpha(k)},\qquad r>0.
\]
Writing \(A_\alpha=\Gamma(\alpha+1)/[2\Gamma(2\alpha+2)]\), its large-reset-frequency law is
\[
 T_\alpha(r)\sim\frac{L^2}{D}A_\alpha k^{\alpha-1}\qquad(k\to\infty).
\]
Hence the infimum over finite \(r\geq0\) is zero and unattained for \(-1<\alpha<1\); at \(\alpha=1\) the infimum is \(L^2/(12D)\), again unattained, and every finite reset rate gives strictly larger mean time. For \(\alpha>1\), the mean time diverges as \(r\to\infty\).

The finite-rate optimum has a singular boundary. Put \(\alpha_{\mathrm c}=(\sqrt{57}-3)/4\). For every \(1<\alpha<\alpha_{\mathrm c}\), at least one strictly positive finite global minimizing rate exists. As \(\varepsilon=\alpha-1\downarrow0\), **every** global minimizer \(r_*(\alpha)\) satisfies
\[
 \frac{L^2}{D}\,r_*(1+\varepsilon)\sim\frac4{\varepsilon^2}.
\]
The optimized mean has the finer expansion
\[
 \min_{r\geq0}T_{1+\varepsilon}(r)
 =\frac{L^2}{12D}\left[1+\varepsilon\log\frac1\varepsilon
 +\varepsilon\left(\log2+\gamma_{\mathrm E}-\frac53\right)+o(\varepsilon)\right],
\]
where \(\gamma_{\mathrm E}\) is Euler's constant. These statements neither claim uniqueness of minimizers nor classify the global optimum for \(\alpha\geq\alpha_{\mathrm c}\).

## Assumptions and scope

The circle is unwrapped at the target; reaching either interval endpoint ends the experiment. Initial and post-reset positions are independent, identically distributed draws from the displayed strictly positive interior beta density. Brownian excursions, reset locations, and the homogeneous Poisson clock are mutually independent. A reset does not incur an additional travel delay. The target is perfectly absorbing. The normalization \(k=L\sqrt{r/D}\) treats \(r\) in inverse physical time, while \(\alpha\) is a dimensionless endpoint-depletion exponent. The mean for \(r=0\) is understood by the continuous no-reset limit, not by substituting \(k=0\) into the displayed quotient.

## Proof

**1. Discounted single-excursion hitting probability.** For fixed \(x\in(0,L)\), let \(\tau_x\) be the first exit time of Brownian motion from \((0,L)\). Then \(u_r(x)=\mathbb E_x[e^{-r\tau_x}]\) uniquely solves \(Du_r''=ru_r\), \(u_r(0)=u_r(L)=1\). Solving gives
\[
 u_r(Ly)=\frac{e^{-ky}+e^{-k(1-y)}}{1+e^{-k}},\qquad 0\leq y\leq1.
\]
Averaging over the beta reset law and using its reflection symmetry yields
\[
 F_\alpha(k)=\frac2{B(\alpha+1,\alpha+1)(1+e^{-k})}
 \int_0^1y^\alpha(1-y)^\alpha e^{-ky}\,dy
 =\frac{2\,{}_1F_1(\alpha+1;2\alpha+2;-k)}{1+e^{-k}}.
\]
Each excursion succeeds before the next reset with probability \(F_\alpha(k)\). The mean duration of an excursion truncated by an independent rate-\(r\) exponential time is \((1-F_\alpha(k))/r\). The renewal equation therefore gives \(T=(1-F)/(rF)\), proving the exact mean formula.

**2. Endpoint-depletion trichotomy.** Watson's lemma applied to the preceding positive integral gives, for fixed \(\alpha>-1\),
\[
 F_\alpha(k)=\frac{2\Gamma(2\alpha+2)}{\Gamma(\alpha+1)}k^{-\alpha-1}
 \left[1-\frac{\alpha(\alpha+1)}k+O(k^{-2})\right].
\]
The exponentially small denominator correction does not change the expansion. Consequently
\[
 \frac{D}{L^2}T_\alpha(r)
 =A_\alpha k^{\alpha-1}\left[1+\frac{\alpha(\alpha+1)}k+O(k^{-2})\right]-k^{-2}.
\]
The leading term is positive and dominates \(k^{-2}\) because \(\alpha>-1\). This proves the three large-rate regimes and the zero infimum when \(\alpha<1\).

**3. Strict critical inequality.** At \(\alpha=1\), evaluate the beta integral exactly:
\[
 F_1(k)=\frac{12}{k^3}\left(k-2\tanh\frac k2\right).
\]
The inequality \(T_1(r)>L^2/(12D)\) is equivalent to \(\tanh(k/2)>6k/(k^2+12)\). Put \(z=k/2\) and \(h(z)=(3+z^2)\sinh z-3z\cosh z\). Then \(h(0)=0\), \(h'(z)=z(z\cosh z-\sinh z)>0\) for \(z>0\), since the derivative of the factor in parentheses is \(z\sinh z>0\). The inequality is strict for every finite positive rate. At zero reset rate, \(T_1(0)=L^2/(10D)>L^2/(12D)\). The large-rate limit equals \(L^2/(12D)\), proving the critical infimum and its nonattainment.

**4. Finite-rate existence above critical endpoint depletion.** Write \(p=\alpha+1\), \(Y=X(L-X)\), and let \(m_j=\mathbb E[\tau_X^j]\) for a no-reset excursion started from the beta law. Standard exit-time boundary equations give
\[
 \mathbb E_x\tau_x=\frac{x(L-x)}{2D},\qquad
 \mathbb E_x\tau_x^2=\frac{x(L-x)[L^2+x(L-x)]}{12D^2}.
\]
Beta moments satisfy \(\mathbb EY=L^2p/[2(2p+1)]\) and \(\mathbb EY^2=L^4p(p+1)/[4(2p+1)(2p+3)]\). Expanding the Laplace transform at \(r=0\) yields
\[
 T_\alpha(0)=\frac{L^2}{D}\frac{p}{4(2p+1)},\qquad
 \left.\frac{dT_\alpha}{dr}\right|_{0+}
 =\frac{L^4}{D^2}\frac{p(2p^2-p-7)}{96(2p+1)^2(2p+3)}.
\]
The derivative is negative precisely when \(-1<\alpha<\alpha_{\mathrm c}\). If \(1<\alpha<\alpha_{\mathrm c}\), a small positive reset rate strictly improves the no-reset mean, whereas the high-rate mean diverges by Step 2. Continuity supplies at least one global minimum at an interior positive rate. The sign test alone makes no claim about global optimality for larger exponents.

**5. Singular location of every optimum.** Let \(\alpha=1+\varepsilon\downarrow1\) within the existence interval and let \(k_\varepsilon=L\sqrt{r_*(\alpha)/D}\) be any global minimizer. Choosing the trial point \(k=\varepsilon^{-1}\) in Step 2 shows \(\limsup_{\varepsilon\downarrow0}(D/L^2)T_{1+\varepsilon}(r_*)\leq1/12\). If any sequence of minimizers stayed bounded, continuity in \((\alpha,k)\), including \(k=0\), and the strict inequality from Step 3 would contradict that bound. Thus **all** minimizers satisfy \(k_\varepsilon\to\infty\).

For \(\alpha\) in a fixed sufficiently small compact interval to the right of one, the integral expansion of Step 2 and its \(k\)-derivative are uniform (differentiate the dominated Watson expansion, or differentiate the defining Laplace integral and apply the same expansion). Stationarity at an interior minimizer gives
\[
 0=\varepsilon+\frac{\alpha(\alpha+1)(\alpha-2)}{k_\varepsilon}
 +O(k_\varepsilon^{-2})+O(k_\varepsilon^{-\alpha-1}).
\]
Multiplication by \(k_\varepsilon\), together with divergence of that quantity, proves \(\varepsilon k_\varepsilon\to2\); hence \(r_*L^2/D=k_\varepsilon^2\sim4/\varepsilon^2\). Finally \(A_{1+\varepsilon}=(1/12)[1+(\gamma_{\mathrm E}-8/3)\varepsilon+o(\varepsilon)]\) and \(k_\varepsilon\sim2/\varepsilon\). Substitution into the uniform expansion in Step 2 proves the stated expansion of the minimized mean. No numerical minimization is used in these deductions.

## Verification

The accompanying standalone `verify.py` makes an independent hypergeometric-versus-quadrature comparison, checks the closed critical-shape formula, compares the small-rate derivative against independent exit-time moments, tests large-frequency asymptotic ratios, and computes absorption times of independently discretized finite Markov chains with full resetting. It also performs finite numerical minimizations illustrating the singular optimization scale. Running it with the accompanying dependency file produces 103 passing finite assertions. These tests do not certify either a continuous-parameter assertion or the global asymptotic argument; those follow from the proof above.

## Relationship to prior work

Julián-Salgado, Castro-Villarreal, Dagdug, and Boyer (2026) formulate circular Brownian resetting to arbitrary spatial distributions and analyze rate-optimality transitions for two reset sites. Their accessible abstract establishes the setting, but full-text access was unavailable here, so its potential coverage of other reset densities remains a priority risk. Méndez, Flaquer-Galmés, and Campos (2024), Sections II and IV, provide the general distributional renewal formula and examine uniform and exponential reset laws when the target lies in their support. Their general mean formula already implies the exact mean displayed here after substituting the beta law; **that formula is not claimed as independently new**. Linn and Lawley (2023), Sections 2 and 3.2, establish general frequent-reset first-passage asymptotics and the uniform-initial-condition case, which cover the basic frequent-reset scaling framework. The contribution evaluated here is the Beta endpoint-depletion optimization: existence of a finite optimum immediately above linear vanishing, its singular \(4/(\alpha-1)^2\) rate, and the finer optimized-value expansion. A prior independent result for finitely supported circular reset distributions treats the favored **approach side** rather than the mean-time minimization for continuous beta laws; the two assertions are not equivalent.

## Limitations

No global classification is proved for \(\alpha\geq\alpha_{\mathrm c}\), no uniqueness is asserted in the finite-optimum regime, and the large-rate zero infima are mathematical limits without costs for arbitrarily frequent resets. The theorem does not include travel-time penalties, partially absorbing targets, non-Brownian motion, or non-beta spatial reset distributions in its optimized conclusions. The leading large-rate exponent is a specialization of established general renewal and short-time asymptotic principles. The full primary text of the motivating 2026 paper could not be inspected; originality is therefore best-knowledge rather than literature-wide priority certification.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug, and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1 (first submitted 2026-05-08), https://arxiv.org/abs/2605.08414.
2. V. Méndez, R. Flaquer-Galmés, and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1 (2024), https://arxiv.org/abs/2401.01125.
3. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409v1; Phys. Rev. E 108, 024114 (2023), https://arxiv.org/abs/2302.05409.
