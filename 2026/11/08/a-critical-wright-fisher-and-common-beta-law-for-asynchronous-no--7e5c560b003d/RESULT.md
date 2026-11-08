# A critical Wright–Fisher and common-Beta law for asynchronous noisy voting on complete bipartite graphs

## Finding

Let \(a_n,b_n\to\infty\) with no restriction on their ratio, and put \(s_n=a_n^{-1}+b_n^{-1}\). On \(K_{a_n,b_n}\) run continuous-time fair-refresh noisy voting: each vertex has an independent rate-one clock; on ringing, with probability \(\varepsilon_n\in(0,1)\) it chooses a fresh fair bit and otherwise copies a uniform neighbor. Write \(X_n(t),Y_n(t)\) for the fractions of opinion-one vertices in the two parts, and \(Z_n=(X_n+Y_n)/2\).

**Dynamic assertion.** If \(\varepsilon_n/s_n\to\lambda\in[0,\infty)\) and \(Z_n(0)\to z\in[0,1]\) in probability, then in \(D([0,T],[0,1])\), for every finite \(T\),
\[
 (Z_n(t/s_n))_{0\le t\le T}\ \Longrightarrow\ (Z(t))_{0\le t\le T},
\]
where \(Z(0)=z\) is the unique Wright–Fisher-type diffusion with generator
\[
 \mathcal G_\lambda f(z)=\lambda(1/2-z)f'(z)+\tfrac14z(1-z)f''(z).
\]
At every fixed rescaled time \(t>0\), \(X_n(t/s_n)-Y_n(t/s_n)\to0\) in probability, including from initially unbalanced opinions.

**Stationary assertion.** Give the finite chain its unique invariant distribution, and write \((X_n^*,Y_n^*)\) for its part densities. If \(\varepsilon_n/s_n\to\lambda\in(0,\infty)\), then
\[
 (X_n^*,Y_n^*)\Longrightarrow (B_\lambda,B_\lambda),\qquad B_\lambda\sim\operatorname{Beta}(2\lambda,2\lambda).
\]
If the ratio tends to zero, the limit is \((B_0,B_0)\), with \(B_0\) a fair \(\{0,1\}\)-Bernoulli random variable; if it tends to infinity, the limit is the constant \((1/2,1/2)\).

There is also an exact finite-size formula. Let \(c=1-\varepsilon\), \(s=1/a+1/b\), and \(W\) be the stationary covariance of distinct vertex spins coded as \(\pm1\) when the vertices belong to opposite parts. Then
\[
 W=\frac{cs}{2(1-c^2)+c^2s},\qquad
 \operatorname{Var}\left(\frac{X^*+Y^*}{2}\right)=\frac{s+[2+2c-cs]W}{16}.
\]
The stationary spin covariance of any two distinct vertices in the same part equals \(cW\). These identities hold for all integers \(a,b\ge1\), with same-part pair claims only when that part has at least two vertices.

## Assumptions and scope

Graphs are finite, simple, unweighted complete bipartite graphs. Clock processes and update coins are independent, and all opinions take values in \(\{0,1\}\). For a given finite graph, the refresh probability is strictly positive, ensuring a unique stationary distribution. No bounded-ratio assumption on \(a_n/b_n\) is made: the smaller part need only diverge. In the dynamics theorem, \(\varepsilon_n/s_n\) has a **finite** limit; no process-limit claim on that time scale is made when this ratio diverges. The stationary assertion covers all three limiting regimes.

## Proof

**1. Exact generator.** For a state with part fractions \(x=i/a\) and \(y=j/b\), the count \(i\) increases at rate \((a-i)[\varepsilon/2+cy]\) and decreases at rate \(i[\varepsilon/2+c(1-y)]\); the rates for \(j\) are obtained by interchanging the two parts. Hence, with \(z=(x+y)/2\), \(d=x-y\),
\[
 Lz=\varepsilon(1/2-z),\qquad Ld=-(1+c)d.
\]
Writing \(H(x,y)=\varepsilon/2+c(x+y-2xy)\), the predictable quadratic-variation densities are
\[
 \Gamma(z)=\tfrac{s}{4}H(x,y),\qquad \Gamma(d)=sH(x,y),
 \quad H(x,y)=\varepsilon/2+2cz(1-z)+\tfrac c2d^2.
\]
For all states \(0\le H\le1\). Dynkin's formula for \(d^2\) therefore gives, for every deterministic initial state,
\[
 \mathbb E[d(t)^2]\le e^{-2(1+c)t}d(0)^2+\frac{s}{2(1+c)}.
\]
The same estimate holds for random initial states after averaging and implies convergence of the time integral of \(d^2(t/s)\) to zero in \(L^1([0,T])\), as well as pointwise synchronization at each positive rescaled time. In stationarity it implies \(\mathbb E[d^2]\le s/[2(1+c)]\).

**2. Diffusion limit.** Set \(\widetilde Z_n(t)=Z_n(t/s_n)\). Its jump magnitudes are at most \(1/(2\min(a_n,b_n))\), and its drift is \((\varepsilon_n/s_n)(1/2-z)\). A second-order Taylor expansion of its generator acting on \(f\in C^3([0,1])\), with the quadratic variation above, yields
\[
 s_n^{-1}Lf(z)=\frac{\varepsilon_n}{s_n}(1/2-z)f'(z)+\frac18 H(x,y)f''(z)+r_n,
\]
where \(\sup|r_n|\le C_f\max(a_n^{-1},b_n^{-1})\). Since \(c_n\to1\), \(\varepsilon_n\to0\), and \(\int_0^T \mathbb E[d_n(u/s_n)^2]du\to0\), the integrated generator converges in probability to \(\int_0^T\mathcal G_\lambda f(Z(u))du\). Bounded drifts, bounded quadratic variations and vanishing jumps yield tightness by the semimartingale criterion; any subsequential limit solves the \(\mathcal G_\lambda\)-martingale problem, which is well posed on \([0,1]\) (including the absorbing-boundary case \(\lambda=0\)). Its solution is the claimed diffusion.

**3. Exact finite moments.** Code opinions as spins \(\sigma_v=2\xi_v-1\). Independent fair refresh gives mean-zero stationary spin at each vertex. By vertex symmetry let \(U_A,U_B\) be the spin products of two different vertices in each part and \(W\) the spin product across parts. Applying the generator to two-spin products at stationarity gives \(U_A=cW\), \(U_B=cW\), and
\[
 2W=c\left[\frac1a+\frac1b+(1-\frac1a)U_A+(1-\frac1b)U_B\right].
\]
Solving yields the displayed formula for \(W\), including the singleton-part cases by dropping non-existent same-part pairs. Counting diagonal and off-diagonal terms in the variance of \(Z\) gives the displayed variance identity.

**4. Invariant limits.** For \(\varepsilon_n/s_n\to\lambda<\infty\), compactness provides subsequential stationary limits of \(Z_n^*\). The diffusion limit applies to their random initial conditions (use tightness and condition on the initial density); the subsequential limit is invariant for \(\mathcal G_\lambda\). For \(\lambda>0\), this Jacobi diffusion has unique stationary \(\operatorname{Beta}(2\lambda,2\lambda)\) density, obtained by the zero-flux relation; hence all subsequences agree. The \(L^2\) synchronization bound promotes scalar convergence to the diagonal joint law. For \(\lambda=0\), the finite variance formula gives \(\operatorname{Var}(Z_n^*)\to1/4\), and symmetry fixes the mean at \(1/2\), forcing the fair two-atom limit. For \(\lambda=\infty\), the same formula gives \(\operatorname{Var}(Z_n^*)\to0\). This also establishes the stated extreme regimes without assuming convergence of the stationary diffusion at zero mutation.

## Verification

The accompanying standalone Python program `verify.py` builds the exact lumped continuous-time Markov generator on all \((a+1)(b+1)\) opinion-count states, solves for its stationary distribution with rational Gaussian elimination, and independently checks the drift and bracket identities, two-spin correlations, and the exact stationary variance for small part sizes and multiple rational refresh probabilities. It reports `VERIFY_OK 2664 exact assertions` when run with Python 3. These finite checks are not the justification for the infinite asymptotics; the proof above is.

## Relationship to prior work

Pymar and Rivera (first public version 2021) study noisy-voter density asymptotics on general graphs and prove ordered/disordered regimes, without the complete-bipartite stationary critical Beta law or the arbitrary-imbalance dynamic limit here. Chen, Choi and Cox (2013) prove broad Wright–Fisher limits for **unnoised** voter densities; the present statement treats a precise refresh perturbation, the critical invariant law, and two-group synchronization. Aljovin, Jara and Xiang (2024) derive noisy-voter Wright–Fisher limits on **complete** graphs and quantitative equilibration profiles, not the bipartite arbitrary-imbalance statement. Mori, Hisakado and Nakayama (2018) analyze multi-agent-per-site network voter diffusion, which has a different multi-community model and scaling. General reduction principles are acknowledged and no universal one-dimensional diffusion theory is claimed. In a separate **synchronous** bipartite update scheme, the two group densities may instead have independent Beta limits: the update convention materially changes the coupling.

## Limitations

The theorem does not give a quantitative process-convergence rate, total-variation convergence of the full configuration law, or a process limit when \(\varepsilon_n/s_n\to\infty\). It also does not cover a bounded-size part, where a different random-environment limit occurs. General diffusion-reduction results may provide alternative derivations; exhaustive historical novelty cannot be certified without an independent literature audit. Only self-review has been performed.

## References

1. R. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, first posted 2021-12-02, arXiv:2112.01478, https://arxiv.org/abs/2112.01478.
2. Y.-T. Chen, J. Choi and J. T. Cox, *On the convergence of densities of finite voter models to the Wright–Fisher diffusion*, 2013, arXiv:1311.5786, https://arxiv.org/abs/1311.5786.
3. E. Aljovin, M. Jara and Y. Xiang, *Thermalization and convergence to equilibrium of the noisy voter model*, 2024, arXiv:2409.05722, https://arxiv.org/abs/2409.05722.
4. S. Mori, M. Hisakado and K. Nakayama, *A voter model on networks and multivariate beta distribution*, 2018, arXiv:1810.05643, https://arxiv.org/abs/1810.05643.
5. R. A. Blythe, *Ordering in voter models on networks: Exact reduction to a single-coordinate diffusion*, 2010, arXiv:1006.1557, https://arxiv.org/abs/1006.1557.
