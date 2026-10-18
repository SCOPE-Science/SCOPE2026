# Three sharp stationary occupation-tail regimes under heavy-tailed renewal resets

## Finding

Consider a linear birth–death–immigration process restarted from zero at independent renewal times. A Lomax resetting clock creates three sharply different stationary occupation-tail laws as the per-particle birth rate passes through the per-particle death rate. In all three regimes a proper stationary occupation distribution exists, even when it has no finite positive moment.

Put \(k=u/\lambda\), where \(u>0\) is the immigration intensity, \(\lambda>0\) is the individual birth rate, and \(\mu>0\) is the individual death rate. For fixed \(b,\alpha>0\), reset durations have survival function
\[
\Pr(T>t)=(1+t/b)^{-(1+\alpha)},\qquad t\ge0.
\]
Let \(N\) denote the stationary occupation at an arbitrary observation time, and put \(q=\lambda/\mu\) in the subcritical case. As integers \(n\to\infty\), the following equivalences hold, with all constants explicit.

**Subcritical: \(0<\lambda<\mu\).**
\[
\boxed{\Pr(N=n)\sim \frac{\big(b(\mu-\lambda)\big)^\alpha(1-q)^k}{\Gamma(k)}\;\frac{n^{k-1}q^n}{(\log n)^\alpha}.}
\]
Every positive power moment of \(N\) is finite.

**Critical: \(\lambda=\mu\).**
\[
\boxed{\Pr(N\ge n)\sim (b\lambda)^\alpha\frac{\Gamma(k+\alpha)}{\Gamma(k)}\,n^{-\alpha}.}
\]
For every real \(p>0\), \(\mathbb E[N^p]<\infty\) if and only if \(p<\alpha\).

**Supercritical: \(\lambda>\mu\).**
\[
\boxed{\Pr(N\ge n)\sim \big(b(\lambda-\mu)\big)^\alpha(\log n)^{-\alpha}.}
\]
Every positive power moment of \(N\) is infinite. In particular, finite-mean resetting intervals suffice for a proper stationary probability law but do not ensure finite stationary occupation moments.

## Assumptions and scope

Let \((Z_t)_{t\ge0}\) be a nonexplosive continuous-time chain on \(\mathbb N_0\), initialized at \(Z_0=0\), with transitions
\[
 n\longrightarrow n+1\quad\text{at rate }u+\lambda n,
 \qquad n\longrightarrow n-1\quad\text{at rate }\mu n.
\]
All four parameters \(u,\lambda,\mu,b\) and the renewal-tail parameter \(\alpha\) are strictly positive. The reset intervals are independent identically distributed random variables of survival \((1+t/b)^{-(1+\alpha)}\), independent of every demographic noise source. Each reset sets the occupation to zero; subsequent evolution is independent of earlier cycles. Rates are constant between resets. No coupling to other sites or self-consistent density feedback is asserted.

The mean renewal interval is \(\mathbb ET=b/\alpha<\infty\). The stationary renewal age \(A\) has density and tail
\[
 f_A(t)=\frac\alpha b(1+t/b)^{-1-\alpha},\qquad
 \Pr(A>t)=(1+t/b)^{-\alpha}.
\]
The stationary occupation \(N\) is the random variable \(Z_A\) with the age sampled independently of a fresh zero-started chain. The formulas above apply for all specified positive parameters and integer \(n\) tending to infinity; no simultaneous limit in parameters is claimed.

## Proof

**1. Conditional law and stationary representation.** Define
\[
 \Theta(t)=
 \begin{cases}
 \dfrac{\lambda\big(e^{(\lambda-\mu)t}-1\big)}{\lambda-\mu},&\lambda\ne\mu,\\[5pt]
 \lambda t,&\lambda=\mu.
 \end{cases}
\]
The zero-initialized transition probability generating function is
\[
 H(t,z)=\mathbb E[z^{Z_t}]=\big(1+\Theta(t)(1-z)\big)^{-k},\qquad0\le z\le1.
\]
Indeed \(H(0,z)=1\), and differentiation shows it solves the forward generating-function equation
\[
 \partial_tH=(z-1)\left(uH+(\lambda z-\mu)\partial_zH\right),
\]
because \(\Theta'=\lambda+(\lambda-\mu)\Theta\) and \(k=u/\lambda\). This identifies the transition law uniquely for the nonexplosive birth–death–immigration chain.

Equivalently, let \(G\sim\operatorname{Gamma}(k,1)\) be independent of \(A\). Then, conditional on \((G,A)\),
\[
 N\sim\operatorname{Poisson}\big(G\Theta(A)\big).
\]
The invariant regenerative mixture therefore has exact generating function
\[
 \mathbb E[z^N]=\frac\alpha b\int_0^\infty
 \frac{dt}{(1+t/b)^{1+\alpha}\big(1+\Theta(t)(1-z)\big)^k}.
\]
This is a probability generating function for every positive parameter tuple; the regeneration theorem with finite mean cycle length gives convergence to this stationary marginal.

**2. Subcritical local masses.** Suppose \(c=\mu-\lambda>0\) and \(q=\lambda/\mu\in(0,1)\). Given age \(t\), the occupation has negative-binomial mass
\[
 \Pr(Z_t=n)=\frac{\Gamma(n+k)}{\Gamma(k)n!}
 (1-q_t)^kq_t^n,\qquad
 q_t=\frac{q(1-e^{-ct})}{1-qe^{-ct}}.
\]
The reset-free equilibrium has the same expression with \(q_t\) replaced by \(q\). Dividing the stationary mass by this equilibrium mass yields
\[
 R_n=\mathbb E\left[
 (1-qe^{-cA})^{-k}
 \left(\frac{1-e^{-cA}}{1-qe^{-cA}}\right)^n\right].
\]
Put \(s_n=(\log n)/c\). For fixed \(\varepsilon\in(0,1)\), the integrand is exponentially small in \(n^\varepsilon\), uniformly on \(A\le(1-\varepsilon)s_n\). Uniformly on \(A\ge(1+\varepsilon)s_n\), it tends to one. On the intermediate age band it is bounded by \((1-q)^{-k}\), and that band's probability divided by \(\Pr(A>s_n)\) tends to \((1-\varepsilon)^{-\alpha}-(1+\varepsilon)^{-\alpha}\). Sandwiching and then letting \(\varepsilon\downarrow0\) gives
\[
 R_n\sim\Pr(A>s_n)\sim \big(bc/\log n\big)^\alpha.
\]
Finally \(\Gamma(n+k)/n!\sim n^{k-1}\), proving the stated exact mass prefactor. Since \(q<1\), all polynomial moments are finite.

**3. Critical tail.** When \(\lambda=\mu\), the mixed Poisson parameter is \(W=\lambda AG\). The Lomax age is regularly varying with index \(-\alpha\), while the independent Gamma variable has moments of every positive order. Breiman's product-tail lemma gives
\[
 \Pr(W>x)\sim (b\lambda)^\alpha\mathbb E[G^\alpha]x^{-\alpha}
 =(b\lambda)^\alpha\frac{\Gamma(k+\alpha)}{\Gamma(k)}x^{-\alpha}.
\]
For any fixed \(0<\eta<1\), conditional Poisson Chernoff bounds show
\[
 \Pr(W>(1+\eta)n)-e^{-C_\eta n}\le\Pr(N\ge n)
 \le \Pr(W>(1-\eta)n)+e^{-C_\eta n}
\]
for some \(C_\eta>0\) and all sufficiently large \(n\). Regular variation followed by \(\eta\downarrow0\) transfers the asymptotic to \(N\). The layer-cake formula proves the sharp moment cutoff, including divergence at \(p=\alpha\).

**4. Supercritical tail.** When \(g=\lambda-\mu>0\),
\[
 W=G\Theta(A)=\frac{\lambda G}{g}(e^{gA}-1).
\]
Fix \(\varepsilon\in(0,1)\). The event \(n^{-\varepsilon}\le G\le n^\varepsilon\) has complement of probability \(o((\log n)^{-\alpha})\), by the Gamma density near zero and its exponential upper tail. On this event, the inequalities \(W\ge n\) are squeezed between age exceedance events at \((1\pm\varepsilon)(\log n)/g+O(1)\). As \(\Pr(A>t)\sim(b/t)^\alpha\), sandwiching and sending \(\varepsilon\downarrow0\) gives
\[
 \Pr(W\ge n)\sim(bg)^\alpha(\log n)^{-\alpha}.
\]
Conditional Poisson concentration and slow variation of this tail transfer the equivalence from \(W\) to \(N\). Finally, a logarithmic tail has infinite positive moments by the layer-cake criterion.

## Verification

The accompanying `verify.py` can be run using Python and SciPy. It checks the exact probability-generating-function differential equation at multiple interior parameter points, independently integrates the subcritical negative-binomial mass ratio, computes the critical geometric conditional survival using a rescaled integration variable, and checks the supercritical geometric survival integral against the claimed logarithmic scale. The included finite checks are reproducibility tests, not proofs of any infinite asymptotic limit. The asymptotic arguments above use analytic sandwich bounds and classical regular-variation tools.

## Relationship to prior work

Grange's 2023 work on locally reset nonconserving zero-range processes (arXiv:2311.12414), especially its equations for the single-site occupation chain and Poisson local-reset term, motivates the demographic generator. It treats Poisson resetting in a coupled mean-field particle model and concentrates on stationary mean occupations and condensation, not an iid heavy-tailed renewal catastrophe clock or the three exact occupation-tail equivalents above. Grange's earlier global-reset paper (arXiv:1910.05991) supplies complementary Poisson-renewal background.

Masó-Puigdellosas, Campos, and Méndez (arXiv:2205.01613) derive age-mixture/renewal propagator identities in diffusive resetting; the age-mixture device is prior art, not claimed as new. The present calculation combines that device with a Gamma–Poisson demographic transition kernel and distinguishes local mass asymptotics below criticality from survival-tail asymptotics at and above criticality. Foss, Korshunov, and Palmowski (arXiv:2007.13507) obtain related logarithmic-type population tails under heavy-tailed random **offspring environments**, a different mechanism from iid complete renewal resets. The logarithmic form alone is therefore not claimed as unprecedented.

## Limitations

The theorem concerns one autonomous site with fixed immigration and strictly positive per-particle birth and death rates. It does **not** solve the interacting multi-site, self-consistent nonconserving zero-range process with renewal resetting, and it makes no claim about condensation across fitness levels. The reset clock has a specific Lomax tail; extensions to general regularly varying inter-reset laws need separate hypotheses and proofs. None of the asymptotic equivalences is uniform across \(\lambda=\mu\). The finite checker provides numerical corroboration but no certified analytic error bounds. The originality comparison is limited to the inspected sources and may be affected by broader renewal-catastrophe or branching-process results not identified here.

## References

1. Pascal Grange, *Local resetting in non-conserving zero-range processes with extensive rates* (first publicly posted 21 November 2023), arXiv:2311.12414, https://arxiv.org/abs/2311.12414.
2. Pascal Grange, *Non-conserving zero-range processes with extensive rates under resetting*, arXiv:1910.05991, https://arxiv.org/abs/1910.05991.
3. Axel Masó-Puigdellosas, Daniel Campos, and Vicenç Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613, https://arxiv.org/abs/2205.01613.
4. Sergey Foss, Dmitry Korshunov, and Zbigniew Palmowski, *Branching processes with immigration in atypical random environment*, arXiv:2007.13507, https://arxiv.org/abs/2007.13507.
5. L. Breiman, *On some limit theorems similar to the arc-sin law*, Theory of Probability and Its Applications **10** (1965), 323–331; classical product-tail lemma used with Gamma mixing.
