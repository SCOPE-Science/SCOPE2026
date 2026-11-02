# Logarithmic heterogeneity and the critical expiring-coupon process

## Finding

For independent draws from an alphabet of size \(n\), let \(\theta_{n,i}\in[-B,B]\) be deterministic, satisfy \(\sum_{i=1}^n\theta_{n,i}=0\), and suppose \(n^{-1}\sum_i e^{-\theta_{n,i}}\to\kappa\in[1,e^B]\). Draw type \(i\) with probability \(p_{n,i}=(1+\theta_{n,i}/\log n)/n\). Retain a type only if it has appeared among the last \(M_n=\lfloor n\log n+cn\rfloor\) draws, with fixed \(c\in\mathbb R\). Write \(Z_n(k)\) for the number of currently absent types, using all draws since time one when \(k<M_n\). As \(n\to\infty\),
\[
\bigl(Z_n(\lfloor n\log n+ns\rfloor)\bigr)_{s\in\mathbb R}
\;\Longrightarrow\; (Z_c(s))_{s\in\mathbb R}
\]
locally in the Skorokhod \(J_1\) topology, where \(Z_c\) has an explicit immigration–death construction: let \(\Xi\) be a Poisson point process on \(\mathbb R\) with intensity \(\kappa e^{-x}\,dx\), let independently \(\mathcal B\) be a Poisson point process on \([c,\infty)\times(0,\infty)\) with intensity \(\lambda\,db\,e^{-\ell}d\ell\), and put \(\lambda=\kappa e^{-c}\). Then
\[
Z_c(s)=\#\{x\in\Xi:x>s\}+\sum_{(b,\ell)\in\mathcal B}\mathbf1\{b\le s<b+\ell\}.
\]
In particular, for \(s<c\) the process is a pure-death coupon count with Poisson mean \(\kappa e^{-s}\). On \([c,\infty)\) it is a stationary immigration–death chain with immigration rate \(\lambda\), per-particle death rate one, and Poisson stationary mean \(\lambda\).

Let \(T_n=\inf\{k\ge1:Z_n(k)=0\}\) and \(H_c=\inf\{s\in\mathbb R:Z_c(s)=0\}\). Then
\[
\frac{T_n-n\log n}{n}\Longrightarrow H_c.
\]
The limit is *not* an exponential law. For \(s\le c\),
\[
\Pr(H_c\le s)=\exp(-\kappa e^{-s}).
\]
For \(s>c\), if \(Q\) is the immigration–death chain started from independent \(Q(0)\sim\operatorname{Pois}(\lambda)\), and \(\tau_0\) is its first hitting time of zero, then
\[
\Pr(H_c\le c+t)=\Pr(\tau_0\le t),\quad t\ge0.
\]
For every \(q>0\) the latter distribution has the exact Laplace transform
\[
\mathbb E e^{-q\tau_0}=
\frac{e^{-\lambda}\displaystyle\int_0^1 y^{q-1}dy}
{\displaystyle\int_0^1 y^{q-1}e^{-\lambda(1-y)}dy}
=\frac{e^{-\lambda}}{q\displaystyle\int_0^1 y^{q-1}e^{-\lambda(1-y)}dy}.
\]
The limiting centered completion time has finite mean, exactly
\[
\boxed{\mathbb E H_c=c-E_1(\lambda)+\operatorname{Ei}(\lambda)-\gamma-\log\lambda,\qquad\lambda=\kappa e^{-c}},
\]
where \(E_1(x)=\int_x^\infty e^{-u}\,du/u\), \(\operatorname{Ei}(x)=\gamma+\log x+\int_0^x(e^u-1)du/u\), and \(\gamma\) is Euler's constant. This is the expectation of the **limit law**; no convergence of finite-\(n\) means is asserted. By Jensen, \(\kappa\ge1\). In particular the two-level profile with half \(\theta_{n,i}=a\) and half \(\theta_{n,i}=-a\) yields \(\kappa=\cosh a>1\) for \(a\ne0\), producing a strict delay in the critical first-completion CDF at every finite rescaled time. The limiting law depends on the heterogeneous profile solely through \(\kappa\).

## Assumptions and scope

The coupon symbols are independent, with fixed-for-each-row probabilities \(p_{n,i}\) as in the theorem. The triangular profiles are uniformly bounded, exactly mean-zero, and have convergent exponential mean \(\kappa\); \(c\) is any fixed real number and \(M_n\) is as specified. These probability vectors are positive for sufficiently large \(n\). For all sufficiently large \(n\), \(M_n\ge n\). The one-sided collector starts with every type absent at discrete time zero; at step \(k\), the active window comprises indices \(\max\{1,k-M_n+1\},\ldots,k\). The convergence holds on every fixed compact interval in rescaled time, as a càdlàg integer-valued process. The limiting Poisson point processes are independent. No uniform-in-\(c\) or finite-sample error bound is claimed. The uniform profile is \(\kappa=1\); the new content is the sharp logarithmic-imbalance parameter \(\kappa\) and its effect on the complete critical-window law.

## Proof

**1. Continuous-time embedding and identification of rare marks.** Run independent Poisson clocks \(\{P_i\}_{i=1}^n\) with rates \(r_{n,i}=np_{n,i}=1+\theta_{n,i}/\log n\), started empty at physical time zero. Their superposition has rate \(\sum_i r_{n,i}=n\); its arrival labels, in order, have exactly the required probabilities \(p_{n,i}\). Set \(L_n=\log n+c\). First, consider the continuous-time number of clocks having no arrival in \((\max\{0,t-L_n\},t]\) at times \(t=\log n+s\).

For each type \(i\), denote its first arrival time by \(F_i\), and its consecutive arrival times by \(0<F_i=T_{i,1}<T_{i,2}<\cdots\). An absence interval is either the initial interval, ending at \(F_i\), or a later long interarrival gap: if \(T_{i,j+1}-T_{i,j}>L_n\), that gap creates a missing episode during physical times
\[
(T_{i,j}+L_n,T_{i,j+1}),
\]
with rescaled birth time \(b=c+T_{i,j}\) and duration \(\ell=T_{i,j+1}-T_{i,j}-L_n\). Initial missing episodes end at rescaled times \(F_i-\log n\).

For every fixed lower cutoff \(-K\),
\[
\Pr(F_i-\log n>x)=e^{-r_{n,i}(\log n+x)}=n^{-1}e^{-\theta_{n,i}-x}(1+o(1)),\quad x\ge-K,
\]
uniformly on compact \(x\)-ranges. Summing over \(i\), the initial-death point process above \(-K\) converges to intensity \(\kappa e^{-x}dx\), with expected number \(\kappa e^K\).

For an arrival of clock \(i\) at time \(u\), the next interarrival gap is independent exponential of rate \(r_{n,i}\). The Campbell–Palm identity consequently gives, for bounded \(u\)-regions and \(\ell>0\),
\[
\mathbb E\sum_j\mathbf1\{T_{i,j}\in du,\ T_{i,j+1}-T_{i,j}>L_n,\ T_{i,j+1}-T_{i,j}-L_n\in d\ell\}
=r_{n,i}^2e^{-r_{n,i}L_n}du\,e^{-r_{n,i}\ell}d\ell.
\]
For a bounded start interval \([0,U]\), at most one such marked gap can begin for any fixed \(i\) once \(L_n>U\). The event of a first arrival later than \(\log n-K\) and such an early marked gap are mutually exclusive for large \(n\). Therefore the independent per-type rare-mark array, with event probabilities of order \(1/n\), converges by the elementary multinomial law of small numbers to *independent* Poisson point processes: the initial deaths with intensity \(\kappa e^{-x}dx\) and marked long-gap births with intensity
\[
\lim_{n\to\infty}\sum_{i=1}^n r_{n,i}^2e^{-r_{n,i}L_n}du\,e^{-r_{n,i}\ell}d\ell
=\kappa e^{-c}\,du\,e^{-\ell}d\ell.
\]
The change of variables \(b=c+u\) gives births only for \(b\ge c\), with the claimed rate and independent exponential lifetimes. On any compact rescaled interval only a finite Poisson number of death and birth endpoints is relevant. Almost surely they are distinct and avoid deterministic interval boundaries. The map from these marked points to the count of active missing episodes is then continuous in the local \(J_1\) topology, proving convergence for continuous-time fixed-length windows.

**2. Return to a fixed number of draws.** Let \(A_k\) be the physical time of the \(k\)-th arrival of the aggregated rate-\(n\) Poisson process. Doob's inequality for its compensated count (or equivalently maximal concentration for independent exponential interarrivals) gives, for each fixed \(B\),
\[
\max_{1\le k\le\lfloor n\log n+Bn\rfloor}|A_k-k/n|=o_{\mathbb P}(1).
\]
Indeed the squared maximal deviation is bounded by a constant multiple of \((\log n+B)/n\). Every missing interval in the coupon-index window has a start at index \(j+M_n\) and an end at the next arrival index for that same coupon, unless it is an initial missing interval. Its corresponding physical endpoint differs by \(o_{\mathbb P}(1)\), uniformly on bounded rescaled intervals, from \(T_{i,j}+L_n\) and the next physical arrival, respectively. Because the rates \(r_{n,i}\to1\) uniformly, residual gaps converge to unit exponentials, and a possible discrepancy in deciding if a gap is longer than the window can only arise for gaps within \(o(1)\) of length \(L_n\). For any deterministic \(\delta_n\downarrow0\) dominating the above clock error in probability, the expected number of such borderline gaps beginning at times in a fixed bounded interval is at most
\[
\sum_i U r_{n,i}\big(e^{-r_{n,i}(L_n-3\delta_n)}-e^{-r_{n,i}(L_n+3\delta_n)}\big)=O(\delta_n)=o(1).
\]
Together with the tight finite number of relevant marked gaps and endpoint noncollision, this proves the same local \(J_1\) limit for the fixed-\(M_n\) discrete sliding window. A slowly decreasing choice, for example \(\delta_n=n^{-1/4}\), suffices by the preceding maximal inequality.

**3. Limiting Markov structure.** For \(s<c\), no new missing episodes have been born and \(Z_c(s)=\#\{x\in\Xi:x>s\}\sim\operatorname{Pois}(\kappa e^{-s})\). Its first zero time has CDF \(e^{-\kappa e^{-s}}\). At \(s=c\), \(Z_c(c)\sim\operatorname{Pois}(\lambda)\). Conditional on the remaining initial-death times being greater than \(c\), their excesses above \(c\) are independent unit exponentials, since the intensity of \(\Xi\) above \(c\) is proportional to \(e^{-(s-c)}ds\). The independent marks born after \(c\) arrive at rate \(\lambda\) and live for unit-exponential durations. Hence after \(c\) the count is exactly the stationary immigration–death process with transitions \(k\mapsto k+1\) at rate \(\lambda\) and \(k\mapsto k-1\) at rate \(k\). In particular \(\Pr(Z_c(s)=0)=e^{-\lambda}\) for every \(s\ge c\), while the stationary rate of entrances to zero is \(\lambda e^{-\lambda}\).

**4. Passage to first completion.** Almost surely every finite compact interval contains only finitely many limit jumps; they are of unit size, with no simultaneous jumps. For integer-valued càdlàg paths with these properties, hitting zero is continuous under local \(J_1\) convergence at paths whose first zero is attained by an isolated transition from one to zero and is not at a prescribed endpoint. The limiting chain has this property almost surely. The probability of completion before rescaled time \(-K<c\) is bounded by the no-expiration coupon-collector completion probability there; it tends to \(\exp(-\kappa e^K)\), which vanishes as \(K\to\infty\). The immigration–death chain is irreducible positive recurrent and hence hits zero almost surely. Compact-window convergence followed by \(K\to\infty\) proves \((T_n-n\log n)/n\Rightarrow H_c\).

**5. Exact first-hitting transform and mean.** Let \(Q\) be the immigration–death chain with \(Q(0)=k\), let \(\tau_0\) be its first hitting time of zero, and put \(U_{k0}(q)=\int_0^\infty e^{-qt}\Pr_k(Q(t)=0)dt\). Each initial individual survives to time \(t\) with probability \(e^{-t}\), and the surviving immigrants are independent Poisson with mean \(\lambda(1-e^{-t})\). Thus
\[
\Pr_k(Q(t)=0)=(1-e^{-t})^k\exp\{-\lambda(1-e^{-t})\}.
\]
The strong Markov property at \(\tau_0\) gives
\[
\mathbb E_k e^{-q\tau_0}=U_{k0}(q)/U_{00}(q).
\]
Substitute \(y=e^{-t}\). Averaging over the Poisson \(\lambda\) initial distribution yields
\[
\mathbb E e^{-q\tau_0}
=\frac{\displaystyle\int_0^1y^{q-1}e^{-\lambda}\,dy}
{\displaystyle\int_0^1 y^{q-1}e^{-\lambda(1-y)}dy},
\]
as asserted. Equivalently, conditioning on \(Q(0)=k\) and taking the derivative at \(q=0\) gives
\[
\mathbb E_k\tau_0
=\int_0^1\frac{e^{\lambda y}(1-(1-y)^k)}y\,dy.
\]
Averaging over \(k\sim\operatorname{Pois}(\lambda)\), including \(k=0\), gives
\[
\mathbb E[(H_c-c)_+]=\int_0^1\frac{e^{\lambda y}-1}{y}\,dy=\operatorname{Ei}(\lambda)-\gamma-\log\lambda.
\]
Before \(c\), the shifted-Gumbel first-appearance limit \(G\), with \(\Pr(G\le s)=e^{-\kappa e^{-s}}\), determines whether completion precedes expiry. Consequently
\[
\mathbb E\min(G,c)=c-\int_{-\infty}^c e^{-e^{-s}}ds=c-E_1(\lambda).
\]
Adding the post-\(c\) correction proves the mean formula.

## Verification

The accompanying standalone Python checker enumerates uniform finite stationary-window entry events for alphabet sizes \(2,3,4\); checks immigration–death mean-hitting equations and equivalent Laplace expressions to high precision; and simulates discrete sliding-window completion at \(n=350\), both for uniform probabilities and for a two-level logarithmically imbalanced profile, against birth–death matrix-exponential CDF values. All \(60\) programmed assertions passed. The numerical work supports the formulas but does not replace the infinite-limit proof. Execute \(\texttt{python check.py}\) in an environment with NumPy, SciPy and mpmath.

## Relationship to prior work

Long (arXiv:2604.26298v1, 29 April 2026) proves the exact stationary entry flux, subcritical exponential hitting laws, and the critical-window *one-time* occupancy mass and entry-rate asymptotics (Section 8.3). It explicitly distinguishes the critical regime from the rare-target regime but does not give the full critical-window missing-count process or the first-completion distribution after expiration. The homogeneous stationary functional limit and its hitting transform have also been established previously; neither is claimed as new here. The novel component is the stability boundary for nonuniform probabilities at relative scale \(1/\log n\), and the effective parameter \(\kappa\) governing both first completion and its entire limiting path. The uniform case recovers the critical stationary entrance rate \(e^{-c}e^{-e^{-c}}\), while general logarithmic profiles yield \(\lambda e^{-\lambda}\).

Attrill and Garoni (arXiv:2605.14206v1, 14 May 2026) obtain an \(M/M/\infty\)-queue limit for a **different**, clumsy-update coupon collector. Their Theorem 4.10 has the completion limit of an independent Gumbel variable *plus* a queue hitting time. Here the coupon probabilities vary at the logarithmic scale, deterministic expiration switches immigration on at the fixed location \(c\), and the effective intensity \(\kappa e^{-c}\) is altered by the entire heterogeneity profile. The first-completion law comes from this stitched process, rather than an independent sum. The known classical Gumbel law and Poisson-limit principles are used as tools, not claimed as discoveries. No claim of exhaustive historical priority is made.

## Limitations

Only fixed real \(c\), bounded near-uniform triangular probability profiles, deterministic expiration lengths, weak convergence of the first completion time and the limiting law's exact mean are proved. The stated result does not imply convergence of \(\mathbb ET_n\), uniformity in \(c\), finite-\(n\) convergence rates, or limits for probability profiles beyond the stated near-uniform regime. Earlier general point-process or scan-statistic theorems may provide alternative or broader derivations; publication priority requires independent literature review. No independent mathematical audit has been performed.

## References

1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1 (first public 2026-04-29), https://arxiv.org/pdf/2604.26298.
2. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1 (first public 2026-05-14), https://arxiv.org/pdf/2605.14206.
3. Classical Erdős–Rényi coupon-collector Gumbel limit; standard Poisson point-process thinning and the strong Markov property for immigration–death chains, as used in the proof above.
