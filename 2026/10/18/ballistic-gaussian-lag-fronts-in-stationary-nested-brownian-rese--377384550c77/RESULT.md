# Ballistic Gaussian lag fronts in stationary nested Brownian resetting

## Finding

For the stationary nested-copying Brownian chain specified below, write \(q=2D/r\). For each integer \(j\geq2\) and lag \(t\geq0\), the cross-covariances with the first site obey

\[
C_j^+(t):=\operatorname{Cov}(X_1(0),X_j(t))
=q\,2^{1-j}e^{-rt}\sum_{k=0}^{j-1}\frac{(2rt)^k}{k!},
\qquad
C_j^-(t):=\operatorname{Cov}(X_j(0),X_1(t))
=q\,2^{1-j}e^{-rt}.
\]

For each \(j\), the downstream correlation \(C_j^+\) has exactly one maximizer \(t_j>0\). Its location and height obey

\[
rt_j=j-2+O(j^{-1}),\qquad
C_j^+(t_j)\sim\frac{4D}{r\sqrt{2\pi j}}\quad(j\to\infty).
\]

More precisely, for every real \(s\), uniformly when \(s\) ranges over a fixed compact subset of \(\mathbb R\),

\[
\lim_{j\to\infty}\sqrt j\,
C_j^+\!\left(\frac{j+s\sqrt j}{r}\right)
=\frac{4D}{r\sqrt{2\pi}}\,e^{-s^2/2}.
\]

The simultaneously measured covariance is instead \(C_j^+(0)=q\,2^{1-j}\), exponentially small with distance. Thus **optimizing a nonnegative observation lag changes the distance attenuation from exponential to algebraic**, with a ballistic delay and a Gaussian diffusive-width temporal front. In addition, the exact positive-lag covariance integrals exhibit directionality:

\[
\int_0^\infty C_j^+(t)\,dt=\frac{4D}{r^2}(1-2^{-j}),
\qquad
\int_0^\infty C_j^-(t)\,dt=\frac{4D}{r^2}2^{-j},
\]

so their ratio is \(2^j-1\). These are stationary *unequal-time* correlations, not the equal-time spatial correlations previously determined for this chain.

## Assumptions and scope

Fix \(D>0\), \(r>0\), and an integer \(N\geq2\). There are \(N\) particles on \(\mathbb R\). Independently between jumps, \(X_i\) undergoes Brownian motion with variance rate \(2D\). Each site has an independent Poisson reset clock of rate \(r\). A reset of site \(1\) replaces \(X_1\) by zero; a reset of site \(i\geq2\) replaces \(X_i\) by the instantaneous position of site \(i-1\), while leaving all other positions unchanged. The driving Poisson clocks and Brownian noises are mutually independent; the stationary initial vector has its joint law induced by the past resets and Brownian increments, so its coordinates are generally correlated. The two-time expectations refer to this unique stationary regime. The formulas hold for \(2\leq j\leq N\) and \(t\geq0\). The \(j\to\infty\) statements use any sequence of finite chains with \(N\geq j\); the first \(j\) coordinates do not depend on the presence of later sites.

## Proof

**1. Stationarity and elementary moments.** Construct the process from two-sided independent Brownian noises and Poisson clocks. To reconstruct \(X_i\) at a fixed time, trace its path backward to the previous site-\(i\) reset, then backward from that instant to the previous site-\((i-1)\) reset, and so forth until the most recent site-\(1\) reset. This visits a finite number of almost surely finite exponential waiting intervals and anchors the position at zero; the intervening Brownian increments have finite second moments. This provides a stationary construction. The backward ancestor reaches its site-\(1\) anchor in finite time almost surely, so any two initial conditions couple on the first \(N\) sites after sufficient time; hence the stationary law is unique.

The generator \(L\) satisfies

\[
LX_1=-rX_1,\qquad LX_i=r(X_{i-1}-X_i)\ (i\geq2),
\qquad L(X_1^2)=2D-rX_1^2.
\]

Writing \(q=2D/r\), stationarity gives \(\mathbb E X_1=0\), \(\mathbb E X_1^2=q\), and by the linear recursion \(\mathbb E X_i=0\) for every site. For \(i\geq2\), the independent Brownian noises have zero cross-quadratic variation, while the two resetting mechanisms that act on \(X_1X_i\) yield

\[
L(X_1X_i)=rX_1X_{i-1}-2rX_1X_i.
\]

Therefore, with \(K_i=\mathbb E[X_1X_i]\), one has \(K_1=q\), \(K_i=K_{i-1}/2\), and hence \(K_i=q\,2^{1-i}\). In particular the earlier equal-time covariance is recovered, not asserted as a new result.

**2. Unequal-time covariance.** The linear observables form an invariant space under the Markov semigroup. Iteration of the triangular system in the preceding display gives, conditional on all coordinates at time zero,

\[
\mathbb E[X_j(t)\mid X(0)]
=e^{-rt}\sum_{k=0}^{j-1}\frac{(rt)^k}{k!}X_{j-k}(0).
\]

Multiplying by \(X_1(0)\) and averaging, using \(K_{j-k}=q\,2^{1-(j-k)}\), proves the expression for \(C_j^+\). Independently, \(\mathbb E[X_1(t)\mid X(0)]=e^{-rt}X_1(0)\); multiplying by \(X_j(0)\) gives the reverse-lag expression. The gamma integral identity \(\int_0^\infty e^{-u}u^k/k!\,du=1\) applied termwise to these positive finite sums proves both integrated-covariance identities and the directional ratio.

**3. Unique lag maximum.** Write \(n=j-1\), \(u=rt\), and define

\[
F_n(u):=q^{-1}C_j^+(u/r)
=2^{-n}e^{-u}\sum_{k=0}^{n}\frac{(2u)^k}{k!}.
\]

For \(u>0\), direct differentiation shows that \(F_n'(u)\) has the sign of \(H_n(u)-1\), where

\[
H_n(u)=\sum_{m=1}^{n}\frac{(n)_m}{(2u)^m},
\qquad (n)_m=n(n-1)\cdots(n-m+1).
\]

Every summand is strictly decreasing in \(u\), and \(H_n(u)\) decreases continuously from infinity to zero. Consequently it crosses one exactly once; \(F_n\) increases strictly before this crossing and decreases strictly after it. This proves existence and uniqueness of \(u_n=rt_j\), characterized by \(H_n(u_n)=1\).

**4. Centering of the maximum.** For each fixed \(M>0\), uniformly over \(|c|\leq M\), expanding each falling factorial and its denominator in the exponentially summable series yields

\[
H_n(n+c)=1-\frac{2+2c}{n}+O_M(n^{-2}).
\]

Indeed, for \(m\le n^{1/3}\), the expansion \((n)_m/(n+c)^m=1-[m(m-1)/2+mc]/n+O_M((1+m)^4/n^2)\) follows by Taylor expansion of its product logarithm. The complementary terms \(m>n^{1/3}\) contribute exponentially little, since \((n)_m\le n^m\) and \(n/(2(n+c))\le0.51\) for sufficiently large \(n\). Summing the controlled remainder over the first range against the geometric weights and using the sums \(\sum_{m\geq1}m2^{-m}=2\) and \(\sum_{m\geq1}m(m-1)2^{-m}=4\) give the coefficient. First comparing \(c=-2\) and \(c=0\) traps the unique root in this bounded range; in that range \(H_n'(n+c)=-2/n+O(n^{-2})\). Evaluating at \(c=-1\) and applying the mean-value theorem implies

\[
u_n=n-1+O(n^{-1})=j-2+O(j^{-1}).\]

**5. Gaussian lag profile.** For \(u=n+s\sqrt n+O(1)\), with \(s\) in a compact set, rewrite the covariance as

\[
F_n(u)=\left(e^{-u}\frac{u^n}{n!}\right)
\left[\sum_{m=0}^{n}\frac{(n)_m}{(2u)^m}\right].
\]

The bracket tends uniformly to \(\sum_{m=0}^\infty2^{-m}=2\) by a geometric dominating series. Stirling's formula with the Taylor expansion of \(n\log(u/n)-(u-n)\) yields, uniformly in the same window,

\[
\sqrt n\,e^{-u}\frac{u^n}{n!}\longrightarrow
\frac{e^{-s^2/2}}{\sqrt{2\pi}}.
\]

Multiplying the factors and restoring \(q=2D/r\), and replacing \(n=j-1\) by \(j\), gives the claimed Gaussian profile. The unique maximum has \(u=u_n=n-1+O(n^{-1})\), so its scaled height tends to the Gaussian center value. This completes the proof of all assertions.

## Verification

The standalone program `check.py` requires only the Python standard library and may be run as `python check.py`. It evaluates exact rational integrated-kernel sums, independently tests the conditional-mean differential relations by centered differences, checks the strict peak inequalities and known small-index peaks, and probes the Gaussian/peak asymptotics. It prints `PASS: 1546 deterministic assertions`. These tests provide finite reproducible consistency checks, not proof of the infinite-parameter limits; the latter are established in the analytical argument above.

## Relationship to prior work

Alston, Britton and Bertrand (2025, arXiv:2502.03225v1; Phys. Rev. Lett. 135, 167101) introduce the nested Brownian copying process, calculate its stationary marginals and **equal-time** two-point spatial correlations, and explicitly distinguish static analysis from future dynamical questions. This result uses their model and its equal-time first-to-downstream covariance, but identifies the **unequal-time, directional** covariance kernel, its unique optimal delay, algebraic optimal attenuation, sharp Gaussian delay profile, and integrated directional asymmetry. The equal-time covariance is not claimed new.

Britton, Le Jeune, Alston, Bressloff and Bertrand (2026, arXiv:2609.25252v1) analyze the **one-time relaxation toward stationarity** via accumulation times and a linearly propagating relaxation wavefront. Linear propagation in a reset-copying hierarchy is consequently not, by itself, a novelty claim here: the different observable is the *stationary two-time covariance*, and the distinctive outputs are its Gaussian large-distance profile and the exponential-versus-algebraic contrast. A complete text of that follow-up was not accessible for a decisive appendix-level comparison, creating residual originality risk. More general semigroup-response formulas may imply the finite kernel algebraically; the asymptotic extremal statement is the intended substantive contribution rather than the semigroup method alone.

## Limitations

The results concern the stationary finite-site model with a deterministic zero reset at the source, uniform Poisson rates, independent Brownian noises, positive diffusion constant, and the covariance between the first site and one downstream site. They do not classify heterogeneous reset rates, random nonzero anchors, arbitrary upstream pairs, nonlinear signals or nonstationary one-time relaxation. The asymptotic limit concerns sites increasingly far down finite directed chains, with the earlier sites unaffected by later ones. The inaccessible complete 2026 follow-up and the possibility of implicit coverage by a broader linear-response theorem remain specific scientific limitations.

## References

1. H. Alston, C. Britton and T. Bertrand, *Nested Stochastic Resetting: Nonequilibrium Steady-states and Exact Correlations*, arXiv:2502.03225v1, first posted 5 February 2025; *Physical Review Letters* **135**, 167101 (2025), DOI:10.1103/ccjj-6ksn. https://arxiv.org/html/2502.03225v1
2. C. Britton, B. Le Jeune, H. Alston, P. C. Bressloff and T. Bertrand, *Approach to Steady-State in Nested Resetting Processes*, arXiv:2609.25252v1 (2026), https://arxiv.org/abs/2609.25252
