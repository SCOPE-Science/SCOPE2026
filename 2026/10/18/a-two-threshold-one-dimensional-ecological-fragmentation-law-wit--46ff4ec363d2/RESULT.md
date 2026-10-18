# A two-threshold one-dimensional ecological fragmentation law with exact Gaussian fluctuations

## Finding

For the discrete competitive ecological map defined below, a one-dimensional ring has an exactly solvable strong-competition sector. With initially independent, equally likely local biomasses one and two, the eventual occupied-site count \(S_n\) on \(C_n\), \(n\ge5\), obeys

\[
\begin{array}{c|c|c}
\text{coupling}&\mathbb E S_n&\operatorname{Var}(S_n)\\
\hline
1<\alpha\le2&3n/8&7n/64\\
\alpha>2&n/8&7n/64.
\end{array}
\]

In both rows, \((S_n-\mathbb E S_n)/\sqrt{7n/64}\) converges in distribution to a standard Gaussian as \(n\to\infty\). The common finite-size variance is not a claim that the two count distributions coincide.

There is also a **temporal transition not visible in occupancy**. For \(1<\alpha<2\), initial runs of exactly two high-biomass sites generate persistent synchronous period-two oscillators; their probability of occurrence tends exponentially to one as the ring grows. The normalized total biomass tends in probability to \(3/4\) on even updates and \(5/8\) on odd updates. At \(\alpha=2\) every trajectory instead becomes stationary, with normalized final biomass tending to \(5/8\), while the occupied-site fraction stays \(3/8\). For \(\alpha>2\), it is stationary with occupied fraction \(1/8\) and biomass fraction \(1/4\). These laws are for the stated discrete ecological map, not a prediction for arbitrary continuous Lotka–Volterra dynamics.

## Assumptions and scope

Let \(n\ge5\), with vertices \(i\in\mathbb Z/n\mathbb Z\) of the cycle \(C_n\). Biomass \(N_i(t)\in\{0,1,2\}\) is updated synchronously by the discrete gLV rule

\[
N_i(t+1)=N_i(t)+\operatorname{sgn}\!\left(N_i(t)\left[2-N_i(t)-\frac{\alpha}{2}\left(N_{i-1}(t)+N_{i+1}(t)\right)\right]\right),
\]

with \(\operatorname{sgn}(0)=0\), \(\alpha>1\), and independent \(N_i(0)\) taking one and two with probability \(1/2\) each. Extinction is absorbing. Write \(X_i=\mathbf1_{\{N_i(0)=2\}}\). This explicitly restricts both the graph family and the initial law; other distributions and inhomogeneous couplings are not covered by the stated numerical constants.

Define the eventual occupancy indicators

\[
Y_i=X_i(1-X_{i-1}X_{i+1}),\qquad
Z_i=X_i(1-X_{i-1})(1-X_{i+1}),
\]

and the count of initial maximal runs of exactly two high-biomass sites,

\[
Q_n=\sum_{i=0}^{n-1}(1-X_{i-1})X_iX_{i+1}(1-X_{i+2}).
\]

All indices are cyclic. Then \(S_n=\sum_iY_i\) for \(1<\alpha\le2\), while \(S_n=\sum_iZ_i\) for \(\alpha>2\).

## Proof

**Reduction in one update.** Because both neighbors initially have biomass at least one, every site initially at one has strictly negative growth sign for \(\alpha>1\) and becomes zero. Every site initially at two decreases by one because the positive neighbor load makes its growth sign negative. Thus \(N_i(1)=X_i\), as an exact identity, not just a statement about occupancy.

**Second update and eventual period.** For a site with \(X_i=1\), put \(h_i=X_{i-1}+X_{i+1}\in\{0,1,2\}\). The new growth sign is that of \(1-\alpha h_i/2\). In \(1<\alpha<2\), the site becomes two if \(h_i\le1\) and zero if \(h_i=2\); at \(\alpha=2\), the values are two, one, zero for \(h_i=0,1,2\); for \(\alpha>2\), the values are two, zero, zero. The claimed \(Y_i\) and \(Z_i\) therefore give the exact final supports.

For \(1<\alpha<2\), the surviving sites form exactly the boundary vertices of each maximal run of ones in \((X_i)\), counting a singleton only once. The only adjacent survivors come from runs of length exactly two; they alternate synchronously between biomass two (at even times \(t\ge2\)) and biomass one (at odd times \(t\ge3\)). All other survivors are isolated with biomass two. At \(\alpha=2\), the adjacent pairs remain at biomass one; endpoints of longer runs attain biomass two by the third update. At \(\alpha>2\), only originally isolated high-biomass sites survive, each at biomass two. Consequently \(N(t+2)=N(t)\) for all \(t\ge2\) in the open intermediate regime and \(N(t+1)=N(t)\) for \(t\ge3\) at equality and \(t\ge2\) above equality. This also covers the fully occupied initial binary ring: no boundary survives.

The exact biomass identities for \(t\ge2\) in the open intermediate regime are

\[
\sum_iN_i(t)=\begin{cases}2S_n,&t\text{ even},\\2S_n-2Q_n,&t\text{ odd}.\end{cases}
\]

At equality and for \(t\ge3\), this biomass is \(2S_n-2Q_n\); above equality it is \(2S_n\). For each \(i\), \(\mathbb E Q_n=n/16\), because its summand fixes the four initial binary values to \((0,1,1,0)\). Taking expectations or applying finite-dependence laws of large numbers gives the limiting normalized biomass values in the Finding.

**Exact moments and the variance coincidence.** Each \(Y_i\) and \(Z_i\) depends on just three independent initial bits. At \(p=1/2\), direct enumeration gives

\[
\begin{array}{c|c|c|c|c}
\text{indicator}&\mathbb E U_i&\operatorname{Var}(U_i)&\operatorname{Cov}(U_i,U_{i+1})&\operatorname{Cov}(U_i,U_{i+2})\\
\hline
Y_i&3/8&15/64&-5/64&1/64\\
Z_i&1/8&7/64&-1/64&1/64.
\end{array}
\]

For example, simultaneous adjacent \(Y\)-survival requires the length-four binary word \((0,1,1,0)\), of probability \(1/16\), whereas simultaneous adjacent \(Z\)-survival is impossible. Two-site-separated joint survival has probabilities \(5/32\) and \(1/32\), respectively. At cyclic separation greater than two the indicators are independent; for \(n\ge5\) these are all covariance classes, and both classes lead to

\[
\operatorname{Var}\!\left(\sum_iU_i\right)
=n\{\operatorname{Var}(U_0)+2\operatorname{Cov}(U_0,U_1)+2\operatorname{Cov}(U_0,U_2)\}=7n/64.
\]

The two sequences are bounded, stationary and two-dependent when realized on the infinite Bernoulli line. Their positive asymptotic variance \(7/64\) allows the classical finite-dependent central limit theorem. The difference between the linear-window count and its cyclic version involves at most four boundary indicators, so it is bounded independently of \(n\) and disappears after normalization by \(\sqrt n\). This proves both Gaussian limits.

**Abundance of macroscopic oscillators.** In \(1<\alpha<2\), a nontrivial period-two orbit occurs if and only if \(Q_n>0\). Partition the first \(4\lfloor n/4\rfloor\) initial binary sites into disjoint blocks of four. A block equal to \((0,1,1,0)\) guarantees a maximal two-site run. Their independence yields

\[
\mathbb P(Q_n=0)\le (15/16)^{\lfloor n/4\rfloor}.
\]

Moreover \(\mathbb E Q_n=n/16\) and \(\operatorname{Var}(Q_n)=O(n)\) by finite dependence; hence \(2Q_n/n\to1/8\) in probability, proving persistent macroscopic even–odd biomass contrast.

## Verification

The standalone file `verify.py` implements the published update rule independently of the closed-form occupancy statements, using exact integer comparisons. It enumerates every initial configuration on \(C_n\), \(5\le n\le11\), for rational test couplings \(\alpha=3/2,2,5/2\), and checks all trajectories through the fifth update, final support, period, total biomass identities, complete means, second moments, and counts of length-two oscillators. A separate enumeration of the 3-, 4-, and 5-bit local windows verifies every covariance and normalized-variance identity. Run `python verify.py` from a directory containing that standalone program; no external packages are required.

The enumeration covers the specified finite test rings, not all ring lengths. The proof is symbolic and applies to every \(n\ge5\) as stated.

## Relationship to prior work

Sergo, Koller, Erba and Zdeborová (2026) introduced the synchronous discrete gLV map and studied percolation and dominant ecological attractors mainly on random regular graphs of degree at least three. Their Eq. (2)–(3) is exactly the rule specialized here; Appendix C gives generic coupling breakpoints and a general bound of period two on attractors. Those facts are credited, not claimed as new. The present contribution is the explicit one-dimensional strong-competition support and oscillation classification, two distinct exact occupancy laws, their identical finite-size variances, and quantitative Gaussian and oscillator-prevalence limits. A general period-two bound does not identify which random initial states oscillate or how their biomass varies macroscopically.

Classical finite-dependent central limit theory supplies the probabilistic limit once the dynamical reduction and nontrivial local covariance computations have been established. Earlier stochastic predator–prey cellular automata and continuous spatial Lotka–Volterra rings use different update mechanisms, so their reported phase or oscillation phenomena do not imply these precise count identities.

## Limitations

The proof concerns a one-dimensional connected degree-two cycle, equal fixed pairwise coupling, capacity exactly two, and independent equiprobable initial biomasses one or two. It makes no statement for weaker coupling \(\alpha\le1\), longer-range edges, random regular graphs of higher degree, or continuous-time population models. Exact finite-size variances do not imply equal finite-size distributions. The Gaussian statement is an asymptotic distributional result; no rate of convergence is claimed. The source paper's more general result that periods cannot exceed two is prior work. The bibliographic comparison does not establish absolute priority against unindexed analyses of this same one-dimensional specialization.

## References

1. D. Sergo, C. Koller, V. Erba and L. Zdeborová, *Percolation and clustering in ecological communities: A dynamical theory*, arXiv:2606.09494v1 (first posted 8 June 2026), https://arxiv.org/abs/2606.09494. Especially Section II and Appendix C.
2. W. Hoeffding and H. Robbins, *The central limit theorem for dependent random variables*, Duke Mathematical Journal 15 (1948), 773–780, https://doi.org/10.1215/S0012-7094-48-01568-3.
3. T. Tomé and K. C. de Carvalho, *Stable oscillations of a predator–prey probabilistic cellular automaton: a mean-field approach*, Journal of Physics A 40 (2007), 12901–12915, https://doi.org/10.1088/1751-8113/40/43/005 (different stochastic ecological rule).
4. J. C. Sprott, J. C. Wildenberg and Y. Azizi, *A simple spatiotemporal chaotic Lotka–Volterra model*, Chaos, Solitons & Fractals 26 (2005), 1035–1043 (continuous-time ring model).
