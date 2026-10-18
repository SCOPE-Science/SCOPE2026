# A sharp kurtosis clock ordering for harmonic diffusion with distributed resetting

## Finding

The theorem compares two physically distinct resetting clocks at the same mean reset interval. Between resets a one-dimensional particle follows the harmonic Ornstein–Uhlenbeck evolution; at a reset its position is independently redrawn from a centered distribution. Define the stationary fourth cumulant by \(K_4=\mathbb E[X^4]-3(\mathbb E[X^2])^2\). For a deterministic clock of period \(T>0\) and a Poisson clock of rate \(1/T\), write \(K_4^{\mathrm{det}}\) and \(K_4^{\mathrm{Poi}}\) for the respective stationary fourth cumulants, and write \(L_2^{\mathrm{det}}\) and \(L_2^{\mathrm{Poi}}\) for the stationary fourth-power attenuation of the position retained from the last reset.

**Sharp protocol ordering.** For every \(k,T>0\), every \(D\ge0\), and every centered resetting distribution of positive finite variance \(v\) and finite fourth moment,
\[
\frac{K_4^{\mathrm{Poi}}}{L_2^{\mathrm{Poi}}}
\ge\frac{K_4^{\mathrm{det}}}{L_2^{\mathrm{det}}},
\]
with equality exactly when \(v=D/k\). The inequality is strict otherwise. This compares the signs of the *actual* (unnormalized) cumulants, because both attenuation factors are positive, but is not an assertion that the unnormalized cumulants themselves are ordered.

**Exact sign-transition classification.** Put \(q=D/k\), let \(\kappa_R=\mathbb E[R^4]-3v^2\) be the reset law's fourth cumulant, and let \(\tau=kT\). Define
\[
F_{\mathrm{det}}(\tau)=1-\frac{\tanh\tau}{\tau},\qquad
F_{\mathrm{Poi}}(\tau)=\frac{4\tau^2}{(1+2\tau)^2}.
\]
Then each normalized cumulant is exactly
\[
\frac{K_4^{\mathrm{clock}}}{L_2^{\mathrm{clock}}}
=\kappa_R+3(v-q)^2F_{\mathrm{clock}}(\tau).
\]
Both functions \(F\) increase strictly from zero to one, with \(F_{\mathrm{Poi}}(\tau)>F_{\mathrm{det}}(\tau)\) for every \(\tau>0\). If \(\kappa_R<0\) and \(3(v-q)^2>-\kappa_R\), the fourth cumulant of *each* protocol crosses once and only once from negative to positive as \(T\) increases. The Poisson crossing occurs strictly earlier. If \(\kappa_R<0\) and \(3(v-q)^2\le-\kappa_R\), both cumulants stay strictly negative at every finite \(T\). If \(\kappa_R\ge0\), neither protocol exhibits a negative fourth cumulant; equality at finite \(T\) occurs only when \(\kappa_R=0\) and \(v=q\).

For the natural symmetric binary reset law \(\mathbb P(R=a)=\mathbb P(R=-a)=1/2\), with \(a>0\) and \(\alpha=D/(ka^2)\), a sign transition exists precisely in the two disjoint diffusivity regions
\[
0\le\alpha<1-\sqrt{2/3}\quad\text{or}\quad \alpha>1+\sqrt{2/3}.
\]
For \(D=0\), the Poisson and deterministic critical dimensionless periods are, respectively,
\[
\tau_{\mathrm{Poi}}=\frac{\sqrt{2/3}}{2(1-\sqrt{2/3})}
=2.22474487139158\ldots,
\qquad
\tau_{\mathrm{det}}=2.98470458535788\ldots,
\]
where \(\tau_{\mathrm{det}}\) is the unique positive solution of \(\tanh\tau=\tau/3\). At the matched mean period \(\tau=5/2\), the *unnormalized* binary-reset cumulants have opposite signs:
\[
K_4^{\mathrm{Poi}}=a^4/132>0,\qquad K_4^{\mathrm{det}}<0.
\]
This explicit discrepancy cannot be detected from the reset distribution or mean reset interval alone.

## Assumptions and scope

Let \(k>0\), \(D\ge0\), and let independent positive inter-reset intervals \(W_n\) have finite positive mean \(T=\mathbb E[W_n]\). At each reset choose an independent position \(R_n\) from a common law with \(\mathbb E[R]=0\), \(0<v=\mathbb E[R^2]<\infty\), and \(\mathbb E[R^4]<\infty\). Assume the renewal clock, reset draws, and Brownian increments are mutually independent. Between resets,
\[
dX_t=-kX_t\,dt+\sqrt{2D}\,dB_t.
\]
Interpret the stationary one-time law through the equilibrium renewal-age construction. For deterministic interarrivals, this requires a uniformly randomized phase in \([0,T)\) when sampling the stationary population: the distribution observed at a *fixed* phase of a synchronized deterministic resetting experiment can be different. For Poisson resets, stationary age is exponential of mean \(T\). These conditions exclude time-dependent reset distributions, correlated reset draws, state-dependent resetting clocks, and multiplicative diffusion.

For a general renewal clock, let \(A\) be its equilibrium backward-recurrence age, with probability law
\[
\mathbb P(A\in dt)=\frac{\mathbb P(W>t)}{T}\,dt,\quad t\ge0,
\]
and put \(Z=e^{-2kA}\) and \(L_j=\mathbb E[Z^j]\), for \(j=1,2\). Here \(L_2>0\). The general cumulant identity also covers renewal protocols other than the two compared clocks, but no universal ordering across *all* renewal waiting-time distributions is asserted.

## Proof

**Stationary construction.** The equilibrium renewal-age construction is valid for every positive interarrival law with finite mean. At a stationary observation epoch, the most recent reset draw \(R\), the elapsed age \(A\), and subsequent Brownian increments are independent. Solving the harmonic stochastic differential equation conditionally on the age gives the distributional representation
\[
X=\sqrt Z\,R+\sqrt{q(1-Z)}\,G,
\qquad q=D/k,
\]
where \(G\) is an independent standard Gaussian. The formula remains valid when \(D=0\), with the Gaussian term absent. The stationary clock/position construction is shift invariant in distribution; for deterministic resets the uniform random phase is essential to this assertion.

**Fourth cumulant.** Write \(m_4=\mathbb E[R^4]\). Conditioning on \(Z\), expanding the fourth moment, and using \(\mathbb E[G^2]=1\) and \(\mathbb E[G^4]=3\), we obtain
\[
\mathbb E[X^2]=q+(v-q)L_1,
\]
\[
\mathbb E[X^4]
=m_4L_2+6vq(L_1-L_2)+3q^2(1-2L_1+L_2).
\]
Subtracting three times the square of the second moment yields the exact renewal identity
\[
K_4=\kappa_R L_2+3(v-q)^2(L_2-L_1^2),
\qquad \kappa_R=m_4-3v^2.
\]
Thus \(K_4/L_2=\kappa_R+3(v-q)^2 F\), with \(F=1-L_1^2/L_2\). Strict positivity of \(L_2\) shows the claimed equivalence of signs. This formula is valid whether or not the centered reset law is symmetric.

**The two clocks.** Under deterministic reset periods, the equilibrium age is uniform on \([0,T]\), so
\[
L_j^{\mathrm{det}}=\frac{1-e^{-2jkT}}{2jkT}.
\]
Under Poisson reset times of mean \(T\), the equilibrium age is exponential of mean \(T\), so
\[
L_j^{\mathrm{Poi}}=\frac1{1+2jkT}.
\]
Substitution directly gives the two displayed \(F\)-functions.

**Strict clock ordering.** For \(\tau>0\), \(\sinh\tau>\tau\), and the strictly increasing function \(s\mapsto s/\sqrt{1+s^2}\) shows
\[
\tanh\tau>\frac{\tau}{\sqrt{1+\tau^2}}.
\]
Moreover, the *exact algebraic identity*
\[
(1+2\tau)^4-(1+\tau^2)(1+4\tau)^2
=\tau^2(24\tau+7)>0
\]
implies
\[
\frac1{\sqrt{1+\tau^2}}>
\frac{1+4\tau}{(1+2\tau)^2}.
\]
Combining the inequalities gives
\[
\frac{\tanh\tau}{\tau}>
\frac{1+4\tau}{(1+2\tau)^2},
\]
which is exactly \(F_{\mathrm{det}}(\tau)<F_{\mathrm{Poi}}(\tau)\). Multiplication by \(3(v-q)^2\) proves strict normalized-cumulant ordering unless \(v=q\), in which case the normalized values both equal \(\kappa_R\).

**Uniqueness and boundary cases.** For \(\tau>0\),
\[
\frac{d}{d\tau}\left(1-\frac{\tanh\tau}{\tau}\right)
=\frac{\tanh\tau-\tau\operatorname{sech}^2\tau}{\tau^2}>0.
\]
Indeed the numerator vanishes at zero and its derivative is \(2\tau\operatorname{sech}^2\tau\tanh\tau>0\). Also \(F_{\mathrm{Poi}}'(\tau)=8\tau/(1+2\tau)^3>0\). Both functions tend to \(0\) as \(\tau\downarrow0\) and to \(1\) as \(\tau\uparrow\infty\), attaining neither endpoint at finite positive \(\tau\). Hence a negative \(\kappa_R\) can cross zero if and only if \(0<\eta=-\kappa_R/[3(v-q)^2]<1\), with \(v\ne q\). The Poisson root is \(\sqrt\eta/[2(1-\sqrt\eta)]\); the deterministic root is the unique solution \(\tanh\tau=(1-\eta)\tau\). The strict clock ordering implies \(\tau_{\mathrm{Poi}}<\tau_{\mathrm{det}}\). If \(\eta\ge1\) or \(v=q\), both cumulants remain strictly negative for finite \(T\). The nonnegative \(\kappa_R\) cases follow directly from the cumulant identity and strict positivity of \(F\).

For binary resets \(v=a^2\) and \(\kappa_R=-2a^4\), so \(\eta=2/[3(1-\alpha)^2]\) if \(\alpha\ne1\). This yields the two disjoint diffusivity windows exactly as stated. At \(D=0\), the period-\(5/2\) Poisson factor is \(F_{\mathrm{Poi}}=25/36\), and \(L_2^{\mathrm{Poi}}=1/11\), so \(K_4^{\mathrm{Poi}}/a^4=(1/11)(-2+3\cdot25/36)=1/132\). For the deterministic clock, \(\tanh(5/2)>5/6\) because \(e^5>11\), so \(F_{\mathrm{det}}(5/2)<2/3\), forcing \(K_4^{\mathrm{det}}<0\). Finally, the strict deterministic root lies after \(5/2\) and before \(3\), and numerical high-precision solution gives the displayed approximation.

## Verification

A standalone file, `verify.py`, verifies the exact polynomial identity, the elementary chain of inequalities, the protocol crossover calculations, and the moment formula by **independently integrating the conditional second and fourth moments** for deterministic and Poisson ages. Four finite reset laws are used, including a centered but asymmetric three-atom law. Each is tested over multiple values of \(q\) and \(\tau\). Root values and the sign changes are checked separately. It prints the count of passed assertions; current execution produced `PASS: 428 independent arithmetic, quadrature, root and order assertions`. These numerical checks are finite corroboration; the all-parameter theorem follows from the proof above.

## Relationship to prior work

Eule and Metzger (2015/2016) establish the general renewal-reset stationary-distribution framework, including deterministic-clock limiting cases. This is the basis for the equilibrium-age representation, not a claim of a new renewal theory. Olsen (first public October 7, 2023) establishes exact stationary moments for **Poissonian** resetting to arbitrary position distributions in harmonic confinement. Its Poissonian moment formulas are prior work and can imply the Poissonian cumulant formula used here. Guéneau, Majumdar, and Schehr (June 2023) treat periodic and Poisson resetting of the **driving noise** of a harmonically confined active particle, rather than independently resetting the observed particle position to a distributed law.

The contribution evaluated here is the strict *matched-mean protocol ordering* of the fourth cumulant after its natural survival normalization, the complete unique-or-absent deterministic-clock sign-transition criterion for centered distributed position resets, and the explicit exact opposite-sign example at a common mean period. These are not assertions that either general renewal representations or Poissonian moment recurrences are new. The cited general frameworks make the formulas derivable in principle; an unidentified published reduction to exactly this order/threshold remains a priority risk.

## Limitations

The comparison is for identical centered reset distributions, identical harmonic and diffusion parameters, and equal **mean inter-reset time**, with stationary equilibrium-phase sampling. It does not claim a pointwise ordering of unnormalized fourth cumulants, of excess kurtosis, or of general non-Gaussian distance measures. A vanishing fourth cumulant is not a proof that the stationary distribution is Gaussian. The Poisson roots are algebraic consequences of known Poisson moment formulas, not separately claimed as original. State-dependent, correlated, and nonrenewal clocks require different analysis; a distribution-independent optimum among *all* renewal protocols has not been proved.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public 2023-10-07); Physical Review E **108**, 044120 (2023). https://arxiv.org/abs/2310.04840
2. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876 (2015); New Journal of Physics **18**, 033006 (2016). https://arxiv.org/abs/1510.07876
3. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (first public 2023-06-15); Journal of Physics A (2023). https://arxiv.org/abs/2306.09453
