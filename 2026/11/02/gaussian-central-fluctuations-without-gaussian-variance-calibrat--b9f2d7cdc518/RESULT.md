# Gaussian central fluctuations without Gaussian variance calibration for a thermal-wall tracer

## Finding
Consider a unit-mass free particle shuttling between thermal walls separated by \(L>0\). Independently on departure from wall \(i\in\{H,C\}\), its outgoing speed is sampled with density \(f_i(v)=\beta_i v\exp(-\beta_i v^2/2)\), \(v>0\), for fixed \(\beta_H,\beta_C>0\). Start at a new departure from wall \(H\); count energy transferred in **completed two-leg cycles** only. For cycle \(k\), set
\[
W_k=L/V_{H,k}+L/V_{C,k},\qquad R_k=(V_{H,k}^2-V_{C,k}^2)/2.
\]
The pairs \((W_k,R_k)\) are independent and identically distributed, but their coordinates within a pair need not be independent. Let \(T_n=\sum_{k=1}^nW_k\), \(N(t)=\max\{n\geq0:T_n\leq t\}\), and \(Q(t)=\sum_{k=1}^{N(t)}R_k\). Write
\[
\mu=L\sqrt{\pi/2}(\sqrt{\beta_H}+\sqrt{\beta_C}),\quad
\nu=\beta_H^{-1}-\beta_C^{-1},\quad
c=L^2(\beta_H+\beta_C)/2,\quad j=\nu/\mu.
\]

**Distribution/second-moment mismatch away from equilibrium.** If \(\beta_H\ne\beta_C\), then
\[
\frac{Q(t)-jt}{\sqrt{t\log t}}\ \xrightarrow{\ d\ }\ 
\mathcal N\!\left(0,\frac{c\nu^2}{\mu^3}\right),\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}Q(t)}{t\log t}
=\frac{2c\nu^2}{\mu^3}.
\]
Thus the weak Gaussian limit has exactly **half** the asymptotic coefficient of the untruncated finite-time variance, reflecting lack of uniform integrability of the squared normalized heat current.

**Equilibrium boundary.** If \(\beta_H=\beta_C=\beta\), then
\[
\frac{Q(t)}{\sqrt t}\ \xrightarrow{\ d\ }\ 
\mathcal N\!\left(0,\frac{2}{\beta^2\mu}\right),\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}Q(t)}t
=\frac{2}{\beta^2\mu}.
\]
The two scalings are different; the equilibrium variance statement is included to delimit the regime rather than claimed as a new variance result.

## Assumptions and scope
The observation begins at a completed-wall-emission renewal, with no initialization from a stationary residual-life law. Each velocity sample is independent of all previous samples; both inverse temperatures and \(L\) are strictly positive. A cycle consists of one outward flight from each wall and has the precise joint duration/reward above. \(Q(t)\) excludes a pending, not-yet-complete cycle. If individual-wall transfers are instead counted at each collision, the difference is a single boundary energy term; the asymptotic statements can be transferred when its squared expectation is bounded, but that extension is not needed here. The limits hold for real \(t\to\infty\); logarithms refer to a fixed time unit and changing that unit does not affect the coefficients.

## Proof
**1. Exact moments and waiting-time tail.** For each thermal speed, \(E=V^2/2\) has an exponential distribution with rate \(\beta\). Consequently \(\mathbb E R=\nu\), \(\operatorname{Var}R=\beta_H^{-2}+\beta_C^{-2}\), and \(\mathbb E(1/V)=\sqrt{\pi\beta/2}\), giving \(\mathbb E W=\mu\). A one-leg flight \(\tau=L/V\) satisfies exactly
\[
\mathbb P(\tau>x)=1-\exp(-\beta L^2/(2x^2))
=\frac{\beta L^2}{2x^2}+O(x^{-4}).
\]
The sum of two independent regularly varying positive random variables of index two is subexponential; alternatively split its convolution at \(x-x^{2/3}\) to obtain
\[
\mathbb P(W>x)=\frac c{x^2}(1+o(1)).
\]
The truncated centered cycle-time second moment therefore obeys
\[
H(b):=\mathbb E[(W-\mu)^2\mathbf1_{\{|W-\mu|\le b\}}]
\sim2c\log b.
\]
Also \(\mathbb E[W R^2]<\infty\): the only potentially singular cases are small outgoing speed, for which the other speed has exponential energy tails and the \(1/V\) factor remains integrable under a Rayleigh density.

**2. Marginal normal attraction of the cycle clock.** Put \(a_n=\sqrt{c n\log n}\). By the previous truncated second moment, \(nH(a_n)/a_n^2\to1\), while \(n\mathbb P(|W-\mu|>a_n)\to0\) and the truncated-tail centering error divided by \(a_n\) vanishes. The Lindeberg theorem applied to the truncated triangular array, followed by removal of rare discarded terms, proves
\[
\frac{T_n-n\mu}{\sqrt{c n\log n}}
\xrightarrow{\ d\ }\mathcal N(0,1).
\]
Using the exact inversion \(\{N(t)\geq n\}=\{T_n\leq t\}\), choose \(n=\lfloor t/\mu+x\sqrt{(c/\mu^3)t\log t}\rfloor\); the displayed limit yields
\[
\frac{N(t)-t/\mu}{\sqrt{t\log t}}
\xrightarrow{\ d\ }\mathcal N(0,c/\mu^3).
\]

**3. Reward error and the unequal-temperature Gaussian law.** Let \(M_n=\sum_{k=1}^n(R_k-\nu)\). Although rewards and holding times within a cycle are dependent, \(N(t)+1\) is a stopping time for the joint cycle-pair filtration. By stopped-martingale isometry and \(\mathbb E N(t)=O(t)\), \(\mathbb E M_{N(t)+1}^2=\operatorname{Var}(R)\mathbb E[N(t)+1]=O(t)\). The marked renewal theorem applied to \(g(a)=\mathbb E[(R-\nu)^2\mathbf1_{\{W>a\}}]\) (continuous, decreasing and integrable by \(\mathbb E[W(R-\nu)^2]<\infty\)) shows \(\sup_{t\geq0}\mathbb E[(R_{N(t)+1}-\nu)^2]<\infty\). It follows that \(\mathbb E M_{N(t)}^2=O(t)\). Thus
\[
Q(t)-jt=\nu\,[N(t)-t/\mu]+M_{N(t)}
\]
and the martingale term divided by \(\sqrt{t\log t}\) tends to zero in \(L^2\). Slutsky's theorem proves the first nonequilibrium limit.

**4. Full second moment and the factor two.** For this positive nonlattice \(W\) with a smooth inverse-Rayleigh-convolution density, the renewal expansion at the index-two borderline is
\[
\mathbb E N(t)=\frac t\mu+\frac c{\mu^2}\log t+O(1),\qquad
\operatorname{Var}N(t)=\frac{2c}{\mu^3}t\log t+o(t\log t).
\]
These identities follow by expanding the Laplace transform of \(W\),
\[
\phi(s)=1-\mu s+c s^2\log(1/s)+O(s^2),\quad s\downarrow0,
\]
and the exact renewal-moment transforms
\[
\mathcal L_t\{\mathbb E N(t)\}(s)=\frac{\phi(s)}{s(1-\phi(s))},\quad
\mathcal L_t\{\mathbb E N(t)^2\}(s)=\frac{\phi(s)(1+\phi(s))}{s(1-\phi(s))^2},
\]
using second-order renewal/Tauberian inversion. Explicit derivations for inverse-Rayleigh renewal counts and the corresponding physical heat-current variance also appear in Horii–Lefevere–Itami–Nemoto (2022), Sections II and III; their Equation (61) agrees with the coefficient here after conversion to the present cycle convention. Now \(Q=\nu N+M_N\), \(\operatorname{Var}M_N=O(t)\), and Cauchy–Schwarz gives \(|\operatorname{Cov}(N,M_N)|=O(t\sqrt{\log t})=o(t\log t)\). Hence \(\operatorname{Var}Q(t)\sim\nu^2\operatorname{Var}N(t)\), establishing the factor two relative to the weak-limit Gaussian. Convergence of second moments of the normalized variables would force equality of these coefficients, so uniform integrability of their squares is impossible.

**5. The equilibrium boundary.** When \(\nu=0\), Donsker's invariance principle for the finite-variance iid rewards \(R_k\), together with \(N(t)/t\to1/\mu\), yields via random time change
\[
\frac{M_{N(t)}}{\sqrt t}\xrightarrow{\ d\ }
\mathcal N(0,\operatorname{Var}R/\mu).
\]
The same stopped-martingale identity and bounded second moment of the last marked cycle give \(\mathbb E[M_{N(t)}^2]/t\to\operatorname{Var}R/\mu\), while \(\mathbb E M_{N(t)}=O(1)\). At equal temperatures \(\operatorname{Var}R=2/\beta^2\). This proves the equilibrium statements.

## Verification
Run `python checker.py` with NumPy and SciPy. Its seeded, independently generated Rayleigh/exponential samples check the exact mean cycle duration, signed mean cycle reward, and reward variance across three parameter settings. A separate numerical convolution integrates the exact two-leg duration tail and compares its asymptotic constant at two large thresholds. All 18 assertions passed in the recorded execution. The checker makes no claim of certifying a limit theorem by finite sampling; the proof above supplies the infinite-time arguments.

## Relationship to prior work
Lefevere, Mariani and Zambotti (2010), `arXiv:1007.2664`, establish the confined tracer model, equilibrium Green–Kubo analysis (Section 3.1), and a nonequilibrium current large-deviations principle (Section 3.3). Horii, Lefevere and Nemoto (2021), `arXiv:2106.03182`, examine finite-time heavy-tailed renewal moment-generating asymptotics, not the Gaussian weak law asserted here. Most importantly, Horii, Lefevere, Itami and Nemoto (2022), `arXiv:2203.08584`, Section III.C and Equation (61), already give the nonequilibrium **variance** coefficient. That coefficient, and the equilibrium variance result, are not asserted to be novel. The specific assessed contribution is the matched two-temperature weak Gaussian limit with its coefficient, its exact factor-two incompatibility with the previously known raw variance, and its sharp equilibrium change of normalization. The proof does not assume the weak limit follows merely from knowledge of the variance. General normal-domain-of-attraction and inverse-renewal principles form its acknowledged mathematical foundation.

## Limitations
This is a finite-time law at large \(t\), not an assertion of Gaussian tails at each fixed time. Its \(\sqrt{t\log t}\) limit is only weak, and its squared normalized variables fail uniform integrability. The model is a single unit-mass independent-Rayleigh thermal-wall tracer, with completed-cycle rewards from a fresh renewal start; interacting particles, non-Rayleigh boundary speeds, or nonrenewal boundary laws are not covered. The underlying variance coefficient and inverse-Rayleigh heavy-tail mechanism are established in previous work; historical priority of the specific distribution-level comparison has not been independently certified.

## References
- R. Lefevere, M. Mariani, L. Zambotti, *Large deviations of the current in stochastic collisional dynamics* (first public 2010-07-15), https://arxiv.org/abs/1007.2664.
- R. Lefevere, M. Mariani, L. Zambotti, *Large deviations for a random speed particle* (2011), https://arxiv.org/abs/1103.2815.
- H. Horii, R. Lefevere, T. Nemoto, *Large-time asymptotic of heavy tailed renewal processes* (2021), https://arxiv.org/abs/2106.03182.
- H. Horii, R. Lefevere, M. Itami, T. Nemoto, *Anomalous fluctuations of renewal-reward processes with heavy-tailed distributions*, Physical Review E **106**, 034130 (2022), https://arxiv.org/abs/2203.08584; https://doi.org/10.1103/PhysRevE.106.034130.
