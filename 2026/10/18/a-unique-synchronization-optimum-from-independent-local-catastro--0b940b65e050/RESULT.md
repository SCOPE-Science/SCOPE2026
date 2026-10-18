# A unique synchronization optimum from independent local catastrophes on two hopping sites

## Finding

Consider a two-site population or unbounded-occupancy particle network subject to independent local clearings. At stationarity, both sites are strictly overdispersed and their populations have **strictly positive** cross covariance, despite independent immigration and independent clearing clocks. For the precise generator below, put
\[
 k=d+r,\qquad \Delta=r^2+3(d+h)r+2d^2+4dh.
\]
For any \(a,d,h,r>0\), the unique invariant law obeys
\[
 \begin{aligned}
 m&:=\mathbb E[N_1]=\mathbb E[N_2]=\frac{a}{k},\\
 V&:=\operatorname{Var}(N_1)=\operatorname{Var}(N_2)
 =m+\frac{a^2r(k+h)}{k^2\Delta},\\
 C&:=\operatorname{Cov}(N_1,N_2)=\frac{a^2hr}{k^2\Delta}>0.
 \end{aligned}
\]
The induced fluctuations have the exact injection-independent identity
\[
 \frac{C}{V-m}=\frac{h}{d+r+h}\quad\text{with}\quad 0<\frac{C}{V-m}<1.
\]
For fixed \(a,d,h>0\), the covariance \(C\) has exactly one maximizing clearing rate \(r_*\). It lies strictly between zero and the per-particle death rate \(d\) and is the unique positive root of
\[
 P(r)=2d^3+4d^2h-(2d^2+4dh)r-(7d+6h)r^2-3r^3=0.
\]
Additionally, \(C\) grows strictly with hopping rate \(h\), and
\[
 \lim_{h\to\infty}C=\frac{a^2r}{(d+r)^2(3r+4d)},\qquad
 \lim_{r\to\infty}r^3C=a^2h.
\]
The stationary cross-lag covariance is also explicit for every \(t\ge0\):
\[
 \operatorname{Cov}(N_1(t),N_2(0))
 =e^{-(d+r+h)t}\bigl[C\cosh(ht)+V\sinh(ht)\bigr].
\]
These constitute one joint fluctuation-and-optimization classification for this physical process.

## Assumptions and scope

The continuous-time process \((N_1,N_2)\) has state space \(\mathbb Z_{\ge0}^2\). Four parameters are strictly positive: \(a\) (immigration per site), \(d\) (death per particle), \(h\) (hopping per particle in either direction), and \(r\) (local clearing per site). For \(i\in\{1,2\}\), independent Poisson arrivals increase \(N_i\) by one at rate \(a\); each existing particle dies at rate \(d\); each particle hops to the other site at rate \(h\); and an independent rate-\(r\) clearing clock sets \(N_i\) to zero without changing the other site. A clock ring at an already empty site leaves the state unchanged. There is no exclusion, reproduction, density-dependence or simultaneous global reset.

The generator for a function \(f(n_1,n_2)\), with the usual unit vectors \(e_i\), is
\[
\begin{aligned}
 \mathcal Lf(n)={}&a\sum_i[f(n+e_i)-f(n)]
 +d\sum_i n_i[f(n-e_i)-f(n)]\\
 &+h\sum_{i\ne j}n_i[f(n-e_i+e_j)-f(n)]
 +r\sum_i[f(n-n_ie_i)-f(n)].
\end{aligned}
\]
Terms with \(n_i=0\) in death or hopping are zero. Every identity concerns the unique stationary law, except the time-lag statement, for which the process is initialized in that law. Limits are taken at fixed remaining positive parameters. At \(r=0\), the stationary law instead factors into two independent Poisson distributions with mean \(a/d\), and \(C=0\).

## Proof

**Existence, uniqueness and moments.** Immigration makes this nonexplosive countable-state continuous-time chain irreducible. With \(S=N_1+N_2\), the generator satisfies
\[
 \mathcal L S=2a-(d+r)S.
\]
The hopping events preserve \(S\). Moreover,
\[
 \mathcal L S^2
 =4aS+2a-2dS^2+dS
 +r\sum_i[(S-N_i)^2-S^2]
 \le -(2d+r)S^2+(4a+d)S+2a.
\]
Here \(\sum_i N_i^2\le S^2\). The Foster--Lyapunov drift bounds give positive recurrence, uniqueness and finite stationary second moments, justifying the ensuing stationary generator identities. Alternatively, second-moment finiteness follows by stationary truncations of the latter drift inequality.

**Closed stationary balances.** Symmetry of the generator and uniqueness imply \(\mathbb E[N_i]=m\), \(\mathbb E[N_i(N_i-1)]=U\) and \(\mathbb E[N_1N_2]=W\). Apply the generator to \(N_1\), \(N_1(N_1-1)\), and \(N_1N_2\). The respective stationary equations are
\[
 \begin{aligned}
 &(d+r)m=a,\\
 &(2d+2h+r)U-2hW=2am,\\
 &-2hU+2(d+h+r)W=2am.
 \end{aligned}
\]
For clarity, the factor \(r\) appears only once in the factorial equation because resetting the other site leaves \(N_1(N_1-1)\) unchanged, while the mixed product is annihilated by either reset, giving \(2r\). Solving the nonsingular system gives
\[
 U=\frac{2a^2(d+r+2h)}{(d+r)\Delta},\qquad
 W=\frac{a^2(2d+r+4h)}{(d+r)\Delta}.
\]
Since \(V=U+m-m^2\) and \(C=W-m^2\), direct common-denominator reduction yields the formulas in the Finding and their exact ratio. Every denominator factor is strictly positive. The covariance and variance excess are strictly positive precisely in the asserted positive-parameter domain.

**A single optimal clearing rate.** Differentiation of the exact covariance yields
\[
 \frac{\partial C}{\partial r}
 =\frac{a^2hP(r)}{(d+r)^3\Delta^2}.
\]
On \(r\ge0\),
\[
 \begin{aligned}
 P(0)&=2d^2(d+2h)>0,\\
 P(d)&=-10d^3-6d^2h<0,\\
 P'(r)&=-(2d^2+4dh)-2(7d+6h)r-9r^2<0.
 \end{aligned}
\]
Thus \(P\) has precisely one zero \(r_*\in(0,d)\), and \(C\) increases then decreases strictly. As \(C\to0\) both as \(r\downarrow0\) and \(r\to\infty\), this zero gives the unique global maximum. The derivative with respect to hopping is
\[
 \frac{\partial C}{\partial h}
 =\frac{a^2r(2d+r)}{(d+r)\Delta^2}>0.
\]
Dividing the positive rational function by its highest powers of \(h\) and \(r\) yields the stated limits.

**Two-time identity.** The conditional mean vector obeys the closed affine equation \(\frac{d}{dt}\mathbb E[N(t)\mid N(0)]=A\mathbb E[N(t)\mid N(0)]+a(1,1)^\mathsf T\), with
\[
 A=-(d+r+h)I+h\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Stationarity and the tower property imply \(\operatorname{Cov}(N(t),N(0))=e^{At}\Sigma\), where \(\Sigma=\begin{pmatrix}V&C\\C&V\end{pmatrix}\). Exponentiating the involution in \(A\) establishes the displayed cross-lag formula.

## Verification

The standalone `verification.py` checks the stationary mean/factorial/mixed balances, both variance expressions, the ratio, all polynomial derivative identities and limiting forms by exact SymPy simplification. It independently solves truncated two-dimensional stationary generators for five parameter choices (including one zero-reset reference case), comparing numerical first and second moments against the exact infinite-state formulas, and checks the unique maximizing root at five other parameter choices. It reports 68 passed assertions. Truncation checks are corroborative only and are not an infinite-state proof. Run with a Python environment containing `sympy`, `numpy` and `scipy`:

```shell
python verification.py
```

For the concrete all-unit case \(a=d=h=r=1\), \(\Delta=13\), \(m=1/2\), \(V=29/52\), \(C=1/52\) and \(C/(V-m)=1/3\). These are exact rational values, not fitted data.

## Relationship to prior work

Grange (2023; arXiv:2311.12414, especially Sections 2--5 and Appendices A--C) introduced independent local clearing in a nonconserving zero-range process on an extensive, fully connected fitness network and derived generating-function equations and stationary mean occupations. The present theorem isolates a physically natural finite two-site analogue with independent immigration and no reproduction, carrying a simultaneous joint covariance calculation and a complete clearing-rate optimum classification not stated in that work. The result does not claim priority for local clearing, hopping or moment-generator methodology.

Kapodistria, Phung-Duc and Resing (2015/2016) derive factorial moments for immigration/death with binomial catastrophes in a single population and extend their framework to an external switching environment. Those calculations do not directly state joint covariances for two populations coupled by bidirectional migration and cleared independently. Mandjes, Starreveld and Bekker (2018) derive factorial-moment recursions for infinite-server queueing networks with faulty links rather than instantaneous whole-site occupation clearings. The claimed contribution is the exact signed cross fluctuation, its injection-independent ratio, and a unique interior optimum specific to independent local whole-site clearing. Broader queueing or branching-network theory may implicitly entail the result and warrants independent priority examination.

## Limitations

The theorem covers two sites, equal parameters, symmetric hopping, independent Poisson site clears and homogeneous linear immigration/death. It does not cover hard-core exclusion, more than two sites, joint resetting, unequal populations, density-dependent reproduction, heavy-tailed waiting times, or nonlinear hopping. The covariance identity is an exact theorem for this model, not an experimentally validated law. No universal covariance-sign claim is made for general multitype catastrophe networks. Priority against all older queueing and catastrophe literature is not independently certified.

## References

- Pascal Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, first arXiv submission 21 November 2023, https://arxiv.org/abs/2311.12414.
- Stella Kapodistria, Tuan Phung-Duc and Jacques Resing, *Linear birth/immigration-death process with binomial catastrophes*, Eurandom Report 2015006 (2015), https://www.eurandom.tue.nl/reports/2015/006-report.pdf; doi:10.1017/S0269964815000297.
- Michel Mandjes, Nicos J. Starreveld and René Bekker, *Queues on a Dynamically Evolving Graph*, Journal of Statistical Physics (2018), https://doi.org/10.1007/s10955-018-2036-7.
