# A universal two-time arrow for Poisson-kicked harmonic Brownian motion

## Finding

For a stationary harmonic Brownian particle subjected to any nontrivial compound-Poisson kick distribution, the full two-time position law is **never invariant under exchange of the observation times**, at any positive separation. This holds even when the kicks have no ordinary moments. When a fourth absolute kick moment exists, the lowest guaranteed polynomial witness is an explicit, strictly negative fourth-order correlation contrast. Its optimal observation lag and a two-lag identification law are exact:

\[
\begin{aligned}
\Delta_4(t)&:=\mathbb E[Z_0 Z_t^3]-\mathbb E[Z_0^3 Z_t]\\
&=-\frac{\rho\,\mathbb E[Y^4]}{4\kappa}
 e^{-\kappa t}(1-e^{-2\kappa t})<0,\\
t_{\rm peak}&=\frac{\log 3}{2\kappa},\\
\frac{\Delta_4(2t)}{\Delta_4(t)}&=e^{-\kappa t}(1+e^{-2\kappa t}).
\end{aligned}
\]

Here \(Z_t=X_t-\mathbb E[X_t]\) and \(t>0\). The final ratio is strictly decreasing from two to zero as \(\kappa t\) increases, so any two exact nonzero contrasts at lags \(t\) and \(2t\) uniquely identify the harmonic relaxation rate without prior knowledge of thermal diffusivity, kick frequency, or jump amplitudes.

If \(\mathbb E|Y|^4<\infty\), the precise **minimum total polynomial degree** detecting this temporal exchange asymmetry is three if \(\mathbb E[Y^3]\ne0\), and four if \(\mathbb E[Y^3]=0\). In the former case
\[
\Delta_3(t):=\mathbb E[Z_0Z_t^2]-\mathbb E[Z_0^2Z_t]
=-\frac{\rho\mathbb E[Y^3]}{3\kappa}e^{-\kappa t}(1-e^{-\kappa t}).
\]
The cubic and quartic absolute contrasts attain their unique maxima at \(\log 2/\kappa\) and \(\log 3/(2\kappa)\), respectively. In either case the covariance itself is symmetric in time.

## Assumptions and scope

Let \(\kappa>0\), \(D\ge0\), \(\rho>0\); let \(W\) be standard two-sided Brownian motion and \(J\) an independent two-sided compound-Poisson process of intensity \(\rho\) with real i.i.d. jumps \(Y\). Assume \(\mathbb P(Y\ne0)>0\) and \(\mathbb E\log(1+|Y|)<\infty\). The unique stationary process is the stochastic convolution solving
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t+dJ_t.
\]
The first theorem (nonexchangeability of \((X_0,X_t)\)) requires only these hypotheses. The polynomial statements additionally require \(\mathbb E|Y|^4<\infty\). The jump law may be discrete, continuous, biased, symmetric, or heavy-tailed, and may have an atom at zero; no sign or centering assumption is imposed on \(Y\). All statements concern fixed positive \(t\) in the stationary regime, not transient initialization or trajectory-level entropy production.

## Proof

**1. Stationary construction.** The unique stationary solution can be represented by
\[
X_t=\sqrt{2D}\int_{-\infty}^t e^{-\kappa(t-s)}dW_s
+\sum_{s_i\le t}e^{-\kappa(t-s_i)}Y_i.
\]
The logarithmic moment makes the infinite shot series absolutely convergent almost surely: its Poisson-integral integrability criterion follows from
\(\int_0^\infty\mathbb E[1\wedge(e^{-\kappa s}|Y|)]ds<\infty\).
For \(a=e^{-\kappa t}\in(0,1)\), independent increments give
\[
(X_0,X_t)=(U,aU+V_t),
\qquad U\mathrel{\perp}V_t,
\]
where \(U\) has the stationary law and \(V_t\) contains Brownian and compound-Poisson innovations over \((0,t]\).

**2. Exact distributional arrow without moments.** The two-dimensional law is infinitely divisible. Its Lévy measure away from \((0,0)\) is
\[
\begin{split}
\Pi_t(B)={}&\rho\int_0^\infty\mathbb P\big[(e^{-\kappa s}Y,ae^{-\kappa s}Y)\in B\big]ds\\
&+\rho\int_0^t\mathbb P\big[(0,e^{-\kappa s}Y)\in B\big]ds
\end{split}
\]
for Borel sets \(B\) disjoint from a neighborhood of the origin. The first term is supported on the slanted line \(L_a=\{(u,au):u\ne0\}\), and places nonzero Lévy mass there because \(\mathbb P(Y\ne0)>0\). The second term is supported on the vertical axis. Exchanging coordinates maps these supports to the distinct line \(L_{1/a}=\{(u,u/a):u\ne0\}\) and the horizontal axis. Since \(0<a<1\), \(L_a\) is disjoint from the latter supports away from the origin. Consequently the swapped Lévy measures differ. Uniqueness of the Lévy–Khintchine triplet proves that \((X_0,X_t)\) and \((X_t,X_0)\) have different laws. The Gaussian thermal contribution does not alter the Lévy measure, and so cannot restore exchangeability. This proves the full assertion without finite variance or fourth moments. It does **not** assert that the two bivariate probability measures are mutually singular.

**3. Mixed cumulants and first polynomial obstruction.** Under \(\mathbb E|Y|^4<\infty\), denote the order-\(n\) stationary cumulant by \(c_n\). Direct Poisson integration gives for \(n=3,4\)
\[
c_n=\rho\mathbb E[Y^n]/(n\kappa),
\qquad
c_2=D/\kappa+\rho\mathbb E[Y^2]/(2\kappa).
\]
Centering removes \(c_1\) without modifying higher cumulants. For integers \(p,q\ge1\), \(p+q=n\le4\), the joint cumulant of \(p\) copies of \(Z_0\) and \(q\) copies of \(Z_t\) equals
\[
K_{p,q}(t)=a^q c_n,
\]
since only the common stationary term \(U\) can appear in a mixed cumulant; the innovation is independent. Thus \(K_{p,q}-K_{q,p}=(a^q-a^p)c_n\). At degree two there is only the symmetric covariance \(c_2a\). At degree three the potentially unequal mixed moments have difference \((a^2-a)c_3\). At degree four, the moment–cumulant identity gives \(\mathbb E[Z_0Z_t^3]-\mathbb E[Z_0^3Z_t]=(a^3-a)c_4\): every Gaussian pairing cancels between the two centered moments, since their variances and covariance are equal. As \(c_4=\rho\mathbb E[Y^4]/(4\kappa)>0\), the quartic contrast is strictly negative at every \(t>0\). This proves the minimum-degree classification (among joint polynomial moments of total degree at most four), and the stated formulas.

**4. Sharp lags and identification.** For the cubic contrast put \(a=e^{-\kappa t}\), so its magnitude is a positive multiple of \(a(1-a)\), which has its unique maximum at \(a=1/2\). For the quartic contrast the factor is \(a(1-a^2)\), whose derivative is \(1-3a^2\); its unique maximum on \((0,1)\) occurs at \(a=1/\sqrt3\). Dividing the quartic formulas at \(2t\) and \(t\) yields \(a(1+a^2)\), strictly increasing in \(a\in(0,1)\) with range \((0,2)\). As \(a=e^{-\kappa t}\) strictly decreases in \(\kappa\), this proves unique two-lag determination.

## Verification

`verify.py` uses exact rational arithmetic to build moments of the stationary random variable and its independent finite-interval innovation from cumulants. Across four nontrivial discrete jump laws, three relaxation rates, two Poisson rates, three thermal diffusivities (including zero), and four lag factors, it reconstructs all relevant centered two-time moments independently by the binomial formula and checks the cubic and quartic contrasts, covariance, variance splitting, positivity, and the two-lag identity. Execution passed **2,310 exact rational assertions**. The infinite-law claims follow from the analytic Lévy-measure and cumulant arguments, not from these finite tests. The derivative proof is elementary and does not require a numerical optimizer.

## Relationship to prior work

Di Bello, Majumdar, Marathe, Metzler, and Roldán (2023, arXiv:2309.13424, Section 5 and Fig. 5) introduce precisely this physical model and **numerically demonstrate** unequal forward and reverse \(X,X^3\) correlations for symmetric Gaussian kicks. Their exact stationary cumulants are prior ingredients; neither those cumulants nor the numerical plot is presented here as new. Their displayed numerical contrast motivates the present global signed formula, the sharp sampling lag, the two-lag identifiability statement, and the distributional no-moments theorem. The relation between symmetric covariance and full bivariate exchangeability is essential: zero probability current or symmetric autocovariance does not imply equal two-time *joint laws* for the present jump process.

Applebaum (2014, arXiv:1411.2752, Sections 2–4 and 6) provides established stochastic-convolution and infinitely-divisible-measure machinery, which the proof uses explicitly rather than claiming it as new. Ohga, Ito, and Kolchinsky (2023, arXiv:2303.13116) establish general thermodynamic bounds on cross-correlation asymmetry for finite-state stochastic systems; such inequalities neither give this exact shot-noise contrast nor classify the heavy-tailed bivariate law. Earlier linear-process time-reversibility theory provides qualitative non-Gaussian precedents; its relevance to this result is acknowledged. The innovation is the combination of a precise physical model, a universal moment-free bivariate obstruction, a sharp lowest-degree witness and universal lag-based recovery rule.

## Limitations

The result does not compute entropy production or any pathwise relative entropy. Fourth-order observations require a finite absolute fourth jump moment, and the two-lag inversion presumes exact stationary expectation values; statistical stability with finite/noisy data is not established. The qualitative irreversibility theorem, unlike the polynomial formulas, applies with only a finite logarithmic jump moment. A broad theorem about Lévy-driven linear-process reversibility or a previously unexamined shot-noise correlation paper might contain an implicit equivalent statement. No claim of independence from or replacement of standard stochastic-integration theory is made.

## References

1. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler, and É. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424 (first submitted September 23, 2023), https://arxiv.org/abs/2309.13424.
2. D. Applebaum, *Infinite Dimensional Ornstein-Uhlenbeck Processes Driven by Lévy Processes*, arXiv:1411.2752 (2014), https://arxiv.org/html/1411.2752v1.
3. N. Ohga, S. Ito, and A. Kolchinsky, *Thermodynamic Bound on the Asymmetry of Cross-Correlations*, arXiv:2303.13116 (2023), https://arxiv.org/html/2303.13116v4.
4. G. Bartosz and T. Kania, *Law equivalence of Ornstein–Uhlenbeck processes driven by a Lévy process*, arXiv:1803.02655 (2018); concerns equivalence of process laws rather than exchangeability of one bivariate stationary law.
5. I. Eliazar and J. Klafter, *Non-linear Shot Noise: Lévy, Noah & Joseph*, Physica A (2006), DOI:10.1016/j.physa.2005.06.056; relevant general shot-noise reference, not fully examined.
