# A singular connectivity window for stochastic social-conformity lifetimes

## Finding
For the finite-group, fitness-weighted imitation and forgetting process defined below, initially seeded by one adopter, the expected lifetime \(L_{n,m}(s,\mu)\) has three exact strong-conformity regimes. With \(n\ge2\) groups of \(m\ge1\) agents, forgetting weight \(\gamma>0\), intrinsic appeal \(a>0\), social conformity \(s\to\infty\), and intergroup coupling \(\mu\in[0,1]\),
\[
\lim_{s\to\infty}\frac{L_{n,m}(s,\mu)}s=
\begin{cases}
\dfrac1\gamma,&\mu=0,\\[3pt]
\dfrac{1+(n-1)\mu}{n\gamma},&\mu>0\text{ fixed}.
\end{cases}
\]
The limits fail to commute at zero coupling when \(n>1\). At the distinguished coupling scale \(\mu=c/s\), for every fixed \(c\ge0\), the limit exists and is *independent of group size and intrinsic appeal*:
\[
\lim_{s\to\infty}\frac{L_{n,m}(s,c/s)}s
=U_n(c,\gamma)
=\sum_{i=1}^{n}\frac{1}{i\left(\gamma+\frac cn(n-i)\right)}
\prod_{j=1}^{i-1}
\frac{\frac cn(n-j)}{\gamma+\frac cn(n-j)}.
\]
Empty products equal one. In particular, \(U_n(0,\gamma)=1/\gamma\) and \(\lim_{c\to\infty}U_n(c,\gamma)=1/(n\gamma)\). For two groups the entire crossover is
\[
U_2(c,\gamma)=\frac{4\gamma+c}{2\gamma(2\gamma+c)}.
\]
**Consequently**, for every fixed \(n\ge2,m\ge1,a>0,\gamma>0\), sufficiently strong finite conformity makes the exact expected lifetime attain a global minimum at some *strictly interior* coupling \(0<\mu<1\). This existence conclusion does not assert a unique optimizer or a finite-parameter closed form.

## Assumptions and scope
There are \(N=nm\) agents in \(n\) labeled groups of \(m\) agents. The state is \(\mathbf k=(k_1,\ldots,k_n)\in\{0,\ldots,m\}^n\), where \(k_i\) adopters in group \(i\) carry the meme. Define \(x_i=k_i/m\), \(\omega_{ii}=1\), \(\omega_{ij}=\mu\) for \(i\ne j\), \(\eta=1+(n-1)\mu\), and
\[
F_{A,i}=a+sx_i,\qquad F_{B,i}=1+s(1-x_i).
\]
In one discrete updating step, only one count changes by one. The source's common normalization and the nonzero transition probabilities are defined *exactly* by
\[
 Z(\mathbf k)=\frac\eta n\sum_{j=1}^n
 \left[\frac{k_j}{N}F_{A,j}+\frac{m-k_j}{N}F_{B,j}\right]
 +\gamma\frac{\sum_j k_j}{N},
\]
\[
 p_{i,+}(\mathbf k)=\frac{m-k_i}{NZ(\mathbf k)}
 \sum_{j=1}^n\omega_{ij}\frac{k_j}{N}F_{A,j},\quad
 p_{i,-}(\mathbf k)=\frac{k_i}{NZ(\mathbf k)}
 \left[\gamma+\sum_{j=1}^n\omega_{ij}\frac{m-k_j}{N}F_{B,j}\right].
\]
All remaining probability is a self-loop. State \(\mathbf0\) is absorbing; at any finite \(s\) every nonzero state eventually reaches \(\mathbf0\), since \(\gamma>0\). The initial state is \((1,0,\ldots,0)\), and the same lifetime results hold for any other single-agent seed by group symmetry. Lifetime means expected number of **global discrete updating steps**, not steps per agent or conditioned persistence. Statements at \(\mu=c/s\) apply for sufficiently large \(s\) so \(c/s\le1\). In the motivating interpretation \(0<a<1\) describes an intrinsically unappealing meme, but the mathematical result holds for every \(a>0\).

## Proof
**1. The forgetting-free fast process.** Set the small parameter \(\varepsilon=1/s\). For fixed \(\mu\), transition probabilities are rational in \(\varepsilon\) and have a finite limit. For any \(\mu>0\), this limit is invariant under exchanging adopters with nonadopters: its leading fitnesses are proportional to \(x_i\) and \(1-x_i\), respectively, and the forgetting contribution vanishes. Because every pair of groups communicates and imitation may copy either type when both occur, all configurations other than the global all-adopter and all-nonadopter states are transient for the finite limiting chain. Their mean absorption times are finite.

Let \(\rho>0\) be the limiting probability that a configuration with one adopter reaches the all-adopter state before the all-nonadopter state. It is independent of the seed's group or individual. Exact type-exchange symmetry says that the probability that one **nonadopter** introduced into the all-adopter state instead reaches the all-nonadopter state is also \(\rho\). At all-adopter consensus, each global updating step causes a forgetting escape with probability
\[
p_{\mathrm{esc}}=\frac{\gamma}{\frac\eta n(a+s)+\gamma}.
\]
The forgotten individual is uniform. After escape, the expected fast excursion duration remains bounded as \(s\to\infty\), while the probability of final extinction before the next return to all-adopter consensus converges to \(\rho\). A geometric-renewal decomposition therefore gives mean residence \(\sim 1/(\rho p_{\mathrm{esc}})\) starting at all-adopter consensus. From a single adopter, the probability of first reaching that state converges to \(\rho\), and the initial fast episode has bounded expectation. Cancellation of the two fixation probabilities yields
\[
L_{n,m}(s,\mu)\sim\frac1{p_{\mathrm{esc}}}\sim\frac{s\eta}{n\gamma}
\qquad(\mu>0\text{ fixed}).
\]
This does **not** follow by setting \(\mu=0\) in the formula, because the limiting fast chain changes its number of closed classes at that boundary.

**2. Completely disconnected groups.** If \(\mu=0\), the only group ever containing adopters is the initially seeded group. At infinite conformity, the two probabilities for that group's count \(1\le k<m\) to increase or decrease have ratio
\[
\frac{p_{k,-}^{(0)}}{p_{k,+}^{(0)}}=\frac{m-k}{k}.
\]
The gambler's-ruin difference equations then give the exact probability \(\alpha_m=2^{-(m-1)}\) that one adopter reaches full local adoption before extinction; by type symmetry the probability of extinguishing one isolated nonadopter in a full-adopter group is the same \(\alpha_m\). In the state where only this group is full of adopters, \(Z\sim s/n\), while the chance to forget one adopter in a global update is \((\gamma/n)/Z\sim\gamma/s\). The same renewal cancellation as above gives \(L_{n,m}(s,0)\sim s/\gamma\). For \(m=1\), the local fixation probabilities equal one and the argument still applies.

**3. Boundary layer \(\mu=c/s\).** When \(s\to\infty\) with fixed \(c\), the leading fast chain has exactly \(2^n\) closed group-monomorphic states: each group consists entirely of adopters or entirely of nonadopters. From any mixed group, local imitation reaches one of those states in finite expected time; the probability that a single minority individual takes over a group is again \(\alpha_m=2^{-(m-1)}\). At any group-monomorphic state the normalization satisfies \(Z\sim s/n\). On time accelerated by \(s\), a single adopter group loses a member through forgetting at rate \(\gamma\). For every ordered pair of differently typed groups, imitation across the pair creates a single minority individual at rate \(c/n\) in either direction. Each such introduction changes the destination group's eventual monomorphic type with probability \(\alpha_m\).

More formally, order the finite transition matrix into the fast transient configurations and the group-monomorphic configurations. Its fast block has spectral radius strictly less than one. The Schur complement of \(I-P_s\), expanded in \(\varepsilon\), eliminates the fast block and gives on the slow states the generator \(\alpha_m G\), where \(G\) has birth and death rates for the number \(k\) of adopter groups
\[
b_k=\frac cn k(n-k),\qquad d_k=k\gamma+\frac cn k(n-k),\qquad 1\le k\le n,
\]
with \(b_n=0\), absorbing state \(k=0\), and \(d_n=n\gamma\). This Schur-complement argument also establishes convergence of expected absorption times: \(G\)'s transient submatrix is invertible because forgetting permits a positive-probability path to zero from every positive \(k\). The initial lone adopter reaches the slow state \(k=1\) with probability \(\alpha_m\) and otherwise becomes extinct after an asymptotically negligible fast period. Hence its rescaled lifetime is \(\alpha_m\) times the mean absorption time of \(\alpha_m G\) from \(k=1\); both appearances of \(\alpha_m\) cancel. The limit is therefore the mean lifetime of \(G\) from \(k=1\), independent of \(m\) and \(a\).

For this birth–death chain, the first-step equations and backward differences give, for the expected extinction time from state one,
\[
U_n(c,\gamma)=\sum_{i=1}^{n}\frac1{d_i}\prod_{j=1}^{i-1}\frac{b_j}{d_j}.
\]
Substitution yields the asserted explicit product sum. The first term survives at \(c=0\), whereas for \(c\to\infty\) all terms with \(i<n\) vanish and the \(i=n\) term tends to \(1/(n\gamma)\). Directly setting \(n=2\) gives the displayed rational crossover.

**4. Strictly interior optimal coupling.** For each fixed \(s>0\), every transient-state inverse \((I-Q_s(\mu))^{-1}\) exists for \(0\le\mu\le1\), and its entries are continuous in \(\mu\). Therefore \(L_{n,m}(s,\mu)\) attains a global minimum. The preceding fixed-coupling limits give
\[
\lim_{s\to\infty}\frac{L_{n,m}(s,0)}s
=\lim_{s\to\infty}\frac{L_{n,m}(s,1)}s=\frac1\gamma,
\]
whereas at \(\mu=1/2\) the limit is \((n+1)/(2n\gamma)<1/\gamma\) for \(n\ge2\). Thus for all sufficiently large finite \(s\), both endpoint values strictly exceed the value at \(\mu=1/2\), forcing every global minimum to be interior. This proves existence only, not uniqueness.

## Verification
The included `verify.py` implements the complete finite count-state transition kernel above and solves the absorbing first-step linear equations by exact rational Gaussian elimination. It checks strong-conformity predictions for \((n,m)=(2,1),(2,2),(3,1)\), finite-pressure strict endpoint comparisons, the boundary-layer product formula at several \(c\) values, and the closed two-group formula: 29 assertions pass. These are finite corroborations; the claims for all group sizes and all parameters are established by the analytical finite-state arguments, not by enumeration. An exact-rational finite illustration at \(n=m=2\), \(a=1/3\), \(\gamma=1/5\), \(s=200\) gives approximately 1001.725 updating steps at \(\mu=0\), 741.383 at \(\mu=1/2\), and 985.942 at \(\mu=1\). The code returns exact fractions before decimal printing.

## Relationship to prior work
Braga and Wardil (2023) define the fitness and normalization-based meme process (their Eqs. 1–3), solve the *single-group* extinction problem by a birth–death recurrence (their Eqs. 4–13), and use a weak-connection approximation for multiple groups (their Sec. III.B). The present statement instead concerns the **exact finite multi-group chain**, proving strong-conformity asymptotics, the noncommuting connectivity limit, the universal \(\mu\sim c/s\) boundary layer, and an eventual interior optimum in the actual expected extinction time. It does not re-claim their model or single-group formula. Lessard (2025) develops general two-timescale Markov-chain projection methods for stochastic evolutionary games; the general projection principle is acknowledged and used here, whereas the meme-model-specific rates, lifetime cancellation, and interior-minimum implication are not the conclusions established there. Older fixation-time literature likewise supplies general methods rather than this model-specific phase diagram.

## Limitations
The result assumes equal-sized groups, homogeneous intrinsic appeal and forgetting, the stated all-to-all group-coupling weights, finite \(n,m\), and a single initial adopter. The asymptotics hold with \(n,m,a,\gamma\) fixed; they are not uniform over growing group size or vanishing forgetting. Fixed-positive-coupling limits are not interchangeable with the zero-coupling limit. The theorem does not identify a unique finite-\(s\) optimizing coupling. Other stochastic updating conventions or continuous-time clocks may change numerical constants. The available primary comparisons cannot exclude all equivalent formulations elsewhere; publication priority requires independent assessment.

## References
1. I. Braga and L. Wardil, “Stochastic evolution of bad memes,” *Physical Review E* **108**, 064103 (2023). DOI: 10.1103/PhysRevE.108.064103. Full author-provided text: https://www.researchgate.net/publication/376202208_Stochastic_evolution_of_bad_memes . First verified public date: 2023-12-04.
2. S. Lessard, “Two Timescales in Stochastic Evolutionary Games,” *Dynamic Games and Applications* (2025). DOI: 10.1007/s13235-025-00617-7. Author-hosted paper: https://dms.umontreal.ca/~lessards/LessardDGAA2025.pdf . Preprint: arXiv:2411.01032 (2024).
3. G. J. Baxter, R. A. Blythe, and A. J. McKane, “Fixation and Consensus Times on a Network: A Unified Approach,” *Physical Review Letters* **101**, 258701 (2008). DOI: 10.1103/PhysRevLett.101.258701.
