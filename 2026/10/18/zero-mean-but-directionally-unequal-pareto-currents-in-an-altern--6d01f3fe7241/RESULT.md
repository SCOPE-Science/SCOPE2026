# Zero-mean but directionally unequal Pareto currents in an alternating-reset exclusion process

## Finding

Consider the one-dimensional symmetric simple exclusion process (SSEP) on \(\mathbb Z\), with every nearest-neighbor bond exchanged at rate one. Independently of the exclusion motion, complete configuration resets alternate between the two complementary step preparations: the \(+\) preparation occupies exactly the sites \(x\leq0\), and the \(-\) preparation occupies exactly the sites \(x\geq1\). The successive residence times of preparation \(s\in\{+,-\}\) are independent Pareto variables with exponent \(\alpha_s\in(3/2,2)\) and cutoff \(b_s>0\). Let \(Y\) be the rightward net particle current through \((0,1)\) **since the most recent reset**, sampled in the stationary alternating-renewal regime. This is a within-cycle current, not the sum of transport and instantaneous global-reset relocations.

Put
\[
\mu_s=\frac{\alpha_s b_s}{\alpha_s-1},\qquad
m(t)=t e^{-2t}\bigl(I_0(2t)+I_1(2t)\bigr),
\]
where \(I_0,I_1\) are modified Bessel functions, and define
\[
F_\alpha(b)=\int_0^b m(t)\,dt+b^\alpha\int_b^\infty t^{-\alpha}m(t)\,dt.
\]
Then the stationary mean and the two directional tails satisfy
\[
\mathbb E Y=\frac{F_{\alpha_+}(b_+)-F_{\alpha_-}(b_-)}{\mu_++\mu_-},
\]
\[
\mathbb P(Y>y)\sim K_+y^{-2(\alpha_+-1)},\qquad
\mathbb P(Y<-y)\sim K_-y^{-2(\alpha_--1)}\quad(y\to\infty),
\]
with the **exact coefficients**
\[
K_s=\frac{b_s^{\alpha_s}\pi^{1-\alpha_s}}{(\mu_++\mu_-)(\alpha_s-1)}>0.
\]
For every prescribed \(\alpha_+,\alpha_-\in(3/2,2)\) and \(b_+>0\), there exists **exactly one** \(b_->0\) for which \(\mathbb E Y=0\). If the two exponents differ, this zero-mean stationary current nonetheless has **different positive- and negative-tail powers**. Moreover, \(\mathbb E|Y|<\infty\) but \(\mathbb E[Y^2]=\infty\).

For example, \(\alpha_+=1.7\), \(\alpha_-=1.9\), \(b_+=1\) give the mean-canceling value \(b_-\approx1.4793465365\); at this value the positive- and negative-tail powers are \(1.4\) and \(1.8\), respectively. The decimal calibration is diagnostic, not a certified interval.

## Assumptions and scope

For configurations \(\eta\in\{0,1\}^{\mathbb Z}\), the reset-free generator on cylinder functions is
\[
(\mathcal L f)(\eta)=\sum_{x\in\mathbb Z}\bigl[f(\eta^{x,x+1})-f(\eta)\bigr],
\]
where \(\eta^{x,x+1}\) interchanges the two occupancies. Each reset starts a fresh independent copy of this dynamics from the deterministic preparation corresponding to the alternating reset sign. The duration \(T_s\) satisfies
\[
\mathbb P(T_s>t)=\Psi_s(t)=\begin{cases}1,&0\le t<b_s,\\(b_s/t)^{\alpha_s},&t\ge b_s.\end{cases}
\]
The durations for successive cycles are independent, and the sign switches at *every* reset. Since both \(\mu_s<\infty\), the alternating-renewal process has a time-stationary version. The stationary age \(A\) and current preparation sign \(S\) obey
\[
\mathbb P(S=s,A\in dt)=\frac{\Psi_s(t)}{\mu_++\mu_-}\,dt.
\]
With \(+\) preparation, the current accumulated since reset is \(J_0(t)=\sum_{x\ge1}\eta_x(t)\), which is finite almost surely for every finite \(t\). With \(-\) preparation it has the distribution of \(-J_0(t)\) by particle-hole and spatial symmetry. The theorem concerns the stationary-time law of this real-valued, integer-supported observable on the infinite lattice. It makes no thermodynamic-limit statement for fixed finite rings, where circulation makes a single-bond integrated current a different observable.

## Proof

**1. Reset-free mean.** By the SSEP one-particle duality or the closed discrete heat equation for the density, for \(+\) step preparation the expected instantaneous rightward current across \((0,1)\) is the return probability of the rate-one nearest-neighbor continuous-time walk:
\[
m'(t)=e^{-2t}I_0(2t),\qquad m(0)=0.
\]
The Bessel recurrence \(I_0(z)-I_2(z)=2I_1(z)/z\) gives the stated integral identity
\[
m(t)=\int_0^t e^{-2u}I_0(2u)\,du
=t e^{-2t}\bigl(I_0(2t)+I_1(2t)\bigr).
\]
The standard positive-argument Bessel asymptotics imply \(m(t)\sim\sqrt{t/\pi}\). Also \(m(t)>0\) for \(t>0\), \(m(t)\le t\), and \(m(t)\le C\sqrt t\) for all \(t>0\) with some finite constant \(C\).

**2. A concentration estimate without an independent-particle approximation.** Let \(\rho_i(t)=\mathbb E\eta_i(t)\) and, for \(i<j\), set \(c_{ij}(t)=\operatorname{Cov}(\eta_i(t),\eta_j(t))\). For nonadjacent indices, the covariance evolves by the sum of the two discrete Laplacians. At adjacent sites \(j=i+1\), its evolution is
\[
\partial_t c_{i,i+1}
=c_{i-1,i+1}+c_{i,i+2}-2c_{i,i+1}
-\bigl(\rho_i-\rho_{i+1}\bigr)^2.
\]
The initial covariance is zero, and the two-particle exclusion semigroup preserves positivity. Thus the forced equation with nonpositive source gives \(c_{ij}(t)\le0\) for distinct \(i,j\). This also follows from known negative-dependence results for SSEP [5]. Since the right half-line initially contains no particles, and its expected occupation at finite times is \(m(t)<\infty\), approximation by finite sums yields
\[
\operatorname{Var}(J_0(t))\le\mathbb E J_0(t)=m(t),\qquad
\mathbb E[J_0(t)^2]\le m(t)^2+m(t).
\]
In particular, for each \(u>0\),
\[
\frac{J_0(y^2u)}{y}\;\xrightarrow[y\to\infty]{\mathbb P}\;\sqrt{u/\pi}.
\]
This is a genuine large-time law of large numbers: it follows because the mean divided by \(y\) has that limit and the variance divided by \(y^2\) tends to zero. No assumption of independent SSEP particles has been made.

**3. Alternating-renewal reward law.** In one full \(+,-\) regeneration pair, the expected amount of time spent in phase \(s\) with elapsed age between \(t\) and \(t+dt\) is \(\Psi_s(t)dt\). Divide by the mean pair length \(M=\mu_++\mu_-\). Conditional on \(S=s,A=t\), the law of the signed current is that of \(sJ_0(t)\). Consequently, for every Borel set \(B\subseteq\mathbb R\),
\[
\mathbb P(Y\in B)=\frac1M\sum_{s\in\{+,-\}}\int_0^\infty
\Psi_s(t)\,\mathbb P(sJ_0(t)\in B)\,dt,
\]
interpreting \(sJ_0\) in the obvious signed sense. Because \(m(t)=O(\sqrt t)\) and \(\alpha_s>3/2\), the mean is absolutely integrable, and the exact displayed mean formula follows.

**4. Exact one-sided tail constants.** The positive tail is
\[
\mathbb P(Y>y)=\frac1M\int_0^\infty \Psi_+(t)\,
\mathbb P(J_0(t)>y)\,dt.
\]
For any fixed \(\epsilon>0\), replace \(t\) by \(y^2u\) on \(t\ge\epsilon y^2\). The concentration estimate in Step 2 gives pointwise convergence of the conditional probability to \({\bf1}_{\{u>\pi\}}\), except at the immaterial boundary \(u=\pi\). Pareto domination allows dominated convergence, so the contribution of these ages, divided by \(y^{-2(\alpha_+-1)}\), tends to
\[
\frac{b_+^{\alpha_+}}M\int_{\epsilon}^\infty
u^{-\alpha_+}{\bf1}_{\{u>\pi\}}\,du.
\]
To control shorter ages uniformly, apply Markov's inequality to \(J_0(t)^2\) and the moment estimate in Step 2. Splitting the age integral at \(b_+\) and at one gives
\[
\int_0^{\epsilon y^2}\Psi_+(t)\mathbb P(J_0(t)>y)\,dt
\le C_1y^{-2}+C_2\epsilon^{2-\alpha_+}
y^{-2(\alpha_+-1)}
\]
for all sufficiently large \(y\), with finite constants depending on the fixed parameters. Here the range \(\alpha_+<2\) matters. Let \(y\to\infty\) then \(\epsilon\downarrow0\), obtaining
\[
\mathbb P(Y>y)\sim\frac{b_+^{\alpha_+}}{M(\alpha_+-1)}
(\pi y^2)^{1-\alpha_+}.
\]
The \(-\) preparation is the reflected law; the negative-tail coefficient follows identically. Since both tail exponents lie strictly between one and two, \(Y\) has a finite absolute first moment but an infinite second moment.

**5. Unique zero-mean calibration.** Write \(T_{\alpha,b}=bU_\alpha\), where \(\mathbb P(U_\alpha>u)=u^{-\alpha}\) for \(u\ge1\), and let \(H(t)=\int_0^t m(s)\,ds\). Fubini's theorem gives
\[
F_\alpha(b)=\mathbb E[H(bU_\alpha)].
\]
Since \(m(t)>0\), \(H\) is strictly increasing; hence \(F_\alpha(b)\) is continuous and strictly increasing in \(b>0\). The bound \(H(t)\le C't^{3/2}\) and \(\mathbb E[U_\alpha^{3/2}]<\infty\) for \(\alpha>3/2\) imply \(F_\alpha(b)\to0\) as \(b\downarrow0\). Since \(U_\alpha\ge1\) and \(H(b)\to\infty\), also \(F_\alpha(b)\to\infty\) as \(b\to\infty\). Therefore the equation \(F_{\alpha_-}(b_-)=F_{\alpha_+}(b_+)\) has precisely one positive solution. This proves all assertions.

## Verification

A standalone Python program, `verify.py`, evaluates the Bessel mean in two independent ways, checks the alternating-renewal normalization, solves the unique mean-balancing equation, tests the tail-coefficient algebra using an explicitly labeled deterministic-age proxy, and computes finite-state SSEP transition semigroups to test nonpositive pair covariances and the variance envelope. Run with `python verify.py` using NumPy and SciPy. The program is numerical evidence only. The exact infinite-lattice tail statements depend on the probabilistic proof in Steps 1–4, not on finite-state numerical experiments.

At \(\alpha_+=1.7\), \(\alpha_-=1.9\), \(b_+=1\), numerical quadrature gives \(b_-\approx1.4793465365292602\) and \(F_{\alpha_+}(b_+)\approx3.102804645579363\). The directional tail coefficients are approximately \(K_+\approx0.1154718275\) and \(K_-\approx0.1503261178\). The comparison is sensitive to the convention of rate **one per undirected bond**; changing the hopping rate rescales these numbers.

## Relationship to prior work

Basu–Kundu–Pal [1] established resetting-induced currents and renewal descriptions of SSEP with a single step reset under exponential reset times. Sadekar–Basu [2] analyzed two complementary step reset configurations under independent Poisson resetting, including zero-mean nonequilibrium states. Mishra–Basu [3] studied a **single step configuration** with heavy-tailed renewal reset times and calculated stationary distributions and current-moment regimes. Derrida–Gerschenfeld [4] established detailed current-fluctuation properties of SSEP with step initial data. Negative-dependence theory [5] supplies an alternative route to the variance inequality used here.

The present assertion is about deterministic alternation of **two different Pareto residence laws**, its exactly calibrated zero mean, and its exact direction-dependent stationary tail constants. Neither the Poisson two-configuration analysis [2] nor the single-configuration power-law resetting analysis [3] covers these jointly specified cycles. The shared renewal principle and the reset-free SSEP current are established ingredients; novelty is not claimed for those foundations. A hidden equivalence with a more general published semi-Markov resetting theorem remains a substantive originality risk.

## Limitations

The result describes the stationary signed **within-cycle** current and does not include global mass teleportation during a reset. Although the reset-free process has infinitely many particles, its one-sided current at finite time is finite almost surely; the global reset is defined on configurations by a deterministic map. On a fixed finite reflecting interval the net interface current is bounded, whereas on a ring individual-bond current includes circulation; neither is covered by this infinite-line argument. The infinite-lattice setting is essential. The regime \(3/2<\alpha_\pm<2\) is needed both for finite means and for the second-moment argument giving exact tail constants; no claims are made here at the marginal exponents or outside this interval. Numerical examples are not interval-certified.

## References

[1] U. Basu, A. Kundu, and A. Pal, *Symmetric Exclusion Process under Stochastic Resetting*, arXiv:1906.11801v1 (first public 2019-06-27), https://arxiv.org/abs/1906.11801.

[2] O. Sadekar and U. Basu, *Zero-current Nonequilibrium State in Symmetric Exclusion Process with Dichotomous Stochastic Resetting*, arXiv:2004.00951v1 (first public 2020-04-02), https://arxiv.org/html/2004.00951v1.

[3] S. Mishra and U. Basu, *Symmetric Exclusion Process under Stochastic Power-law Resetting*, arXiv:2211.14120v1 (first public 2022-11-25), https://arxiv.org/abs/2211.14120.

[4] B. Derrida and A. Gerschenfeld, *Current Fluctuations of the One Dimensional Symmetric Simple Exclusion Process with Step Initial Condition*, arXiv:0902.2364 (2009), https://arxiv.org/abs/0902.2364.

[5] J. Borcea, P. Brändén, and T. M. Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340 (2007), https://arxiv.org/abs/0707.2340.
