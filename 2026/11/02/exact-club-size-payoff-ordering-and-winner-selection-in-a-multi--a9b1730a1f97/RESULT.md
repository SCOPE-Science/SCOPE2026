# Exact club-size payoff ordering and winner selection in a multi-club restaurant game

## Finding

Fix any finite number \(K\geq 1\) of independently coordinated dining clubs in the untaxed, no-freeloading Kolkata Paise restaurant game. The **finite-population payoff order** is exactly the club-size order: for any two occupied clubs \(i,j\), the member of club \(i\) has greater eating probability than the member of club \(j\) if and only if \(g_i>g_j\). If unaffiliated diners are present, a member of club \(i\) has greater eating probability than an unaffiliated diner if and only if \(g_i>1\); a singleton club ties the unaffiliated diner.

For the fixed-\(K\) infinite-population limit under the ordinary payoff-based replicator equation, the complete state-space outcome is determined by the **initial largest occupied clubs**. If at least one club has positive initial fraction, every unaffiliated fraction and every initially smaller club fraction tends to zero exponentially. If exactly \(r\) clubs tie for the largest strictly positive initial fraction, precisely these \(r\) survive, each tending to \(1/r\). If no club is initially occupied, the entirely unaffiliated state is stationary. These are all possibilities.

The equilibrium set comprises exactly \(2^K\) points: the entirely unaffiliated state and, for every nonempty subset of clubs, its equal-share state with no unaffiliated diners. Each pure-club equilibrium is a hyperbolic sink; an equal-share equilibrium of \(r\geq2\) clubs is a hyperbolic saddle with exactly \(r-1\) unstable directions; the fully unaffiliated equilibrium is nonhyperbolic and loses every positive club-seed trajectory.

## Assumptions and scope

For the finite game take \(N\geq2\) diners and exactly \(N\) interchangeable restaurants. There are \(K\) labeled clubs with integer sizes \(g_i\geq0\) and \(n=N-\sum_i g_i\geq0\) unaffiliated diners. Each club independently chooses a uniformly random injection from its members into the restaurants, so distinct members of the same club never collide. Distinct clubs coordinate neither with each other nor with unaffiliated diners. Each unaffiliated diner independently chooses a uniformly random restaurant. At each occupied restaurant one diner is served, chosen uniformly. Payoff means the probability of receiving the meal; there are no taxes, redistribution, freeloading, restaurant preferences, or costs of club affiliation. A club payoff is considered only if that club has a member; an unaffiliated payoff only if \(n\geq1\).

For the mean-field statement, hold \(K\) fixed while \(N\to\infty\), with club proportions \(b_i=g_i/N\) and unaffiliated proportion \(f=n/N=1-\sum_i b_i\) converging in the closed simplex. Here \(b_i\geq0\), \(f\geq0\); payoffs extend smoothly to unoccupied types as invasion payoffs. The deterministic **ordinary replicator** dynamics are defined by

\[
\dot b_i=b_i(p_i-\bar p),\qquad \dot f=f(p_0-\bar p),\qquad \bar p=f p_0+\sum_{j=1}^K b_jp_j.
\]

They are distinct from threshold-tolerance switching, finite stochastic resampling, or endogenous creation of an extinct club.

## Proof

**1. Exact finite occupancy.** Set \(c_N(t)=1-(1-t)/N\) and \(L_{j,N}(t)=1-g_j(1-t)/N\). A tagged member of club \(i\) sees \(\operatorname{Bin}(n,1/N)\) unaffiliated arrivals at the chosen restaurant and, independently for every other club \(j\), one arrival with probability \(g_j/N\). A tagged unaffiliated diner instead sees \(\operatorname{Bin}(n-1,1/N)\) other unaffiliated arrivals and one Bernoulli arrival from every club. The identity \(1/(m+1)=\int_0^1 t^m\,dt\), together with independent club assignment, gives their exact probabilities

\[
 p_{i,N}=\int_0^1c_N(t)^n\prod_{\ell\ne i}L_{\ell,N}(t)\,dt,
 \qquad p_{0,N}=\int_0^1c_N(t)^{n-1}\prod_{\ell=1}^K L_{\ell,N}(t)\,dt\quad(n\geq1).
\]

Subtracting two club integrals, and then a club integral from an unaffiliated integral, gives

\[
 p_{i,N}-p_{j,N}=\frac{g_i-g_j}{N}\int_0^1(1-t)c_N(t)^n\prod_{\ell\notin\{i,j\}}L_{\ell,N}(t)\,dt,
\]
\[
 p_{i,N}-p_{0,N}=\frac{g_i-1}{N}\int_0^1(1-t)c_N(t)^{n-1}\prod_{\ell\ne i}L_{\ell,N}(t)\,dt.
\]

The displayed integrals are strictly positive, including at boundary sizes \(g_\ell=0\) or \(g_\ell=N\), because their integrands are positive for \(0<t<1\). The claimed finite rankings, equality cases, and all quantifiers follow.

**2. Limit and positive gap kernels.** Put \(L_j(t)=1-b_j(1-t)\). Since \(c_N(t)^n\to e^{f(t-1)}\) uniformly for fixed \(f\) (and likewise for \(n-1\)), the limiting probabilities are

\[
 p_i=\int_0^1 e^{f(t-1)}\prod_{\ell\ne i}L_\ell(t)\,dt,
 \qquad p_0=\int_0^1 e^{f(t-1)}\prod_{\ell=1}^K L_\ell(t)\,dt.
\]

Define \(H_i\) and \(H_{ij}\) by inserting \((1-t)\) into the corresponding integrands and omitting, respectively, club \(i\), or clubs \(i,j\), from the product. Direct subtraction yields the **exact identities**

\[
 p_i-p_0=b_iH_i,\qquad p_i-p_j=(b_i-b_j)H_{ij}.
\]

Each kernel is continuous and strictly positive throughout the closed simplex. In fact, \(e^{f(t-1)}\geq e^{-1}\), while \(L_\ell(t)\geq t\) for \(0\leq t\leq1\); every kernel has at most \(K-1\) such factors. Therefore a uniform bound is

\[
 H_i,H_{ij}\geq\delta_K:=\frac{e^{-1}}{K(K+1)}>0.
\]

For \(K=1\), the pairwise kernel \(H_{ij}\) is not needed.

**3. Exhaustive global convergence.** Let \(B(t)=\sum_i b_i(t)=1-f(t)\), with \(B_0=B(0)>0\). Since \(p_i-p_0=b_iH_i\),

\[
 \dot B=f\sum_i b_i(p_i-p_0)=f\sum_i b_i^2H_i\geq0.
\]

For two initially occupied clubs,

\[
 \frac{d}{dt}\log\frac{b_i}{b_j}=(b_i-b_j)H_{ij},
\]

so equality is preserved by uniqueness, and any strict initial size ordering remains strict and grows in logarithmic ratio. Choose one of the largest initially positive clubs, indexed by \(m\). It remains maximal, so \(b_m(t)\geq B_0/K\). Whenever \(f(0)>0\),

\[
 \frac{d}{dt}\log\frac{b_m}{f}=b_mH_m\geq \delta_KB_0/K.
\]

Thus \(f(t)\leq [f(0)/b_m(0)]e^{-\delta_KB_0t/K}\); when \(f(0)=0\), \(f\) remains zero. If an occupied club \(j\) starts strictly smaller than \(m\), let \(R_j=b_j(0)/b_m(0)<1\). Its ratio to \(m\) never exceeds \(R_j\), hence \(b_m-b_j\geq B_0(1-R_j)/K\) and

\[
 b_j(t)\leq R_j\exp\!\left[-\delta_KB_0(1-R_j)t/K\right].
\]

Club fractions initially zero remain zero. Clubs initially tied for the positive maximum remain identical at all times. Conservation of total fraction now gives exactly the stated limit: each of the \(r\) tied largest clubs approaches \(1/r\) and all other groups approach zero. The bounds establish exponential convergence of all losing types. When \(B_0=0\), the fully unaffiliated vertex is stationary.

**4. Complete equilibrium and local types.** At an equilibrium with some club present, coexistence with \(f>0\) is impossible: an active club has strictly greater payoff than the unaffiliated type. With \(f=0\), all active club payoffs must agree, forcing equal positive fractions through \(p_i-p_j=(b_i-b_j)H_{ij}\). Thus every nonempty subset \(S\) of \(r=|S|\) clubs gives exactly one equilibrium, \(b_i=1/r\) for \(i\in S\), \(b_i=0\) otherwise, and \(f=0\). Together with the fully unaffiliated vertex this gives \(2^K\) equilibria.

At one of these equal-share states set \(A_r(t)=(r-1+t)/r\). Permutation symmetry and the exact payoff differences give \(r-1\) contrast eigenvalues

\[
 \lambda_+(r)=\frac1r\int_0^1(1-t)A_r(t)^{r-2}\,dt>0\quad(r\geq2),
\]

while all \(K-r+1\) absent-type invasion directions (unaffiliated type included) have eigenvalue

\[
 \lambda_-(r)=-\frac1r\int_0^1(1-t)A_r(t)^{r-1}\,dt<0.
\]

For \(r=1\), only the negative invasion eigenvalue occurs and equals \(-1/2\). Hence pure-club vertices are hyperbolic sinks, and every \(r\geq2\) equal-share equilibrium is a hyperbolic saddle of unstable dimension \(r-1\). The entirely unaffiliated point has zero linearization but is unstable to any positive occupied-club seed by the global convergence theorem.

## Verification

The independent standard-library program `verify.py` tests the exact rational finite-population payoff differences for all nonnegative compositions through ten diners with at most four club labels (16,314 comparisons). It separately exhausts restaurant assignments for cases through four diners (55 exact equalities). Four mean-field trajectories verify unique-winner and initial-tie outcomes. Eight local-spectrum perturbations test the positive contrast and negative invasion eigenvalues. All checks passed. The finite checks and trajectory integration support, but do not replace, the exact proofs above. Run with `python verify.py`.

## Relationship to prior work

Harlalka, Belmonte, and Griffin (arXiv:2302.14142, first publicly posted 2023-02-27) introduce the club game, prove the one-club evolutionary advantage, and simulate **two** clubs, explicitly identifying theory for multiple clubs as future work. Harlalka and Griffin (arXiv:2502.15377, first posted 2025-02-21) derive finite and limiting payoff formulas for **two** clubs and analyze a different threshold-tolerance switching model, including a no-unaffiliated two-club winner outcome. The latter article explicitly identifies extensions beyond two clubs and the relationship to standard replicator dynamics as future work. Its accompanying Mathematica notebooks reportedly contain a multi-club replicator analysis; those notebooks were not accessible for direct comparison and constitute a significant remaining originality risk. The present theorem supplies an all-finite-\(K\) exact payoff order, a complete all-\(K\) replicator basin classification including free diners and exact ties, exponential bounds, and local saddle indices. It does not claim novelty for the one-club advantage or for the two-club qualitative monoculture effect.

## Limitations

The selection theorem concerns deterministic infinite-population ordinary replicator flow for any **fixed finite** number of independent clubs; it is not a theorem about finite-population stochastic absorption, tolerance switching, tax policies, cheating, correlated club restaurant choice, or a number of clubs increasing with population size. The finite-size result concerns **payoff ranking**, not a finite stochastic selection rule. Zero-sized clubs cannot spontaneously appear under replicator dynamics. An external independent audit has not been performed. Potential equivalent results in inaccessible supplementary notebooks or other literature remain a bibliographic risk.

## References

1. A. Harlalka, A. Belmonte, and C. Griffin, *Stability of Dining Clubs in the Kolkata Paise Problem with and without Cheating*, arXiv:2302.14142v1 (2023-02-27), https://arxiv.org/abs/2302.14142.
2. A. Harlalka and C. Griffin, *Multi-Group Dynamics with Tolerant Switching in the Kolkata Paise Restaurant Problem with Dining Clubs*, arXiv:2502.15377 (first posted 2025-02-21); *Journal of Physics: Complexity* 6, 025002 (2025), https://arxiv.org/abs/2502.15377.
