# A unique neutrality reversal in finite nonlinear public-goods games

## Finding

For a finite, well-mixed population playing a public-goods game with a multiplication factor affine in the number of contributors, the fixation probability of a single cooperator can exceed neutral drift at weak selection yet fall below it at strong selection. This phenomenon has a **complete finite-population classification**: it occurs if and only if the weak-selection condition \(r_1+2r_n>3K\) holds while one endpoint multiplier lies below \(K=n(N-1)/(N-n)\). When reversal occurs, the advantageous interval is unique, the positive neutrality crossing is unique, and the fixation probability has exactly one positive local maximum. For fixed interaction-group size, the crossing strength is asymptotically proportional to inverse population size, with an explicit integral equation for its constant.

## Assumptions and scope

Let \(N\) and \(n\) be integers satisfying \(N>n\geq3\), and let \(c,r_1,r_n\) be strictly positive real constants. An interaction group has \(n\) participants drawn uniformly without replacement from a well-mixed population of \(N\). If \(k\geq1\) of them contribute, each participant receives benefit \(ckr(k)/n\), and a contributor additionally pays cost \(c\), where

\[
r(k)=r_1+\frac{k-1}{n-1}(r_n-r_1),\qquad k=1,\ldots,n.
\]

Zero contributions produce zero public-good benefit. A population state \(X\in\{0,\ldots,N\}\) counts cooperators. Expected payoffs \(u_C(X)\) and \(u_D(X)\) are computed conditionally on the focal player's type and the \(n-1\) other sampled participants. Updates follow either Fermi pairwise imitation of intensity \(w\geq0\) or a Moran birth-death rule with exponential fitness \(\exp(wu)\). Mutations are absent, and \(\rho_C(w)\) is the probability that a single cooperator reaches fixation against \(N-1\) defectors. Both update rules have identical forward/backward transition **ratios**, although their waiting times may differ.

Define \(K=n(N-1)/(N-n)\), and for integers \(j\in\{0,\ldots,N-1\}\) define

\[
P_0=0,\qquad
P_j=cj\left[\frac{r_1}{K}-1+\frac{(j-1)(r_n-r_1)}{K(N-2)}\right]\quad(j\geq1).
\]

**Exact finite-population theorem.** For every \(w\geq0\),

\[
\rho_C(w)=\left(\sum_{j=0}^{N-1}e^{-wP_j}\right)^{-1}.
\]

The following cases are exhaustive.

1. If \(r_1+2r_n<3K\), then \(\rho_C(w)<1/N\) for every \(w>0\).
2. If \(r_1+2r_n=3K\), the same strict inequality holds for every \(w>0\) unless \(r_1=r_n=K\), in which case \(\rho_C(w)=1/N\) for all \(w\geq0\).
3. If \(r_1+2r_n>3K\) and \(\min(r_1,r_n)\geq K\), then \(\rho_C(w)>1/N\) for all \(w>0\).
4. If \(r_1+2r_n>3K\) and \(\min(r_1,r_n)<K\), there exist unique \(0<w_{\mathrm{peak}}<w_c<\infty\) such that \(\rho_C\) strictly increases on \((0,w_{\mathrm{peak}})\), strictly decreases for \(w>w_{\mathrm{peak}}\), exceeds \(1/N\) exactly for \(0<w<w_c\), and falls below \(1/N\) exactly for \(w>w_c\).

The fourth case consists of two disjoint biological regimes: synergy \(r_1<K<r_n\), and discounting \(r_n<K<r_1\), each also satisfying \(r_1+2r_n>3K\). In the synergistic regime the cooperator is *favored relative to a single defector* at every \(w>0\), even beyond \(w_c\), because \(\rho_C/\rho_D=\exp\{wc(N-1)(r_n/K-1)\}>1\). Being favored is different from being advantageous over neutral drift.

**Population-size theorem.** Fix an integer \(n\geq3\), real \(c>0\), and positive multipliers \(r_1,r_n\) satisfying either \(r_1<n<r_n\) or \(r_n<n<r_1\), together with \(r_1+2r_n>3n\). For every sufficiently large integer \(N\), the fourth case occurs. Its unique positive neutrality crossing satisfies

\[
\lim_{N\to\infty}Nw_c(N)=\tau_*,
\]

where \(\tau_*\in(0,\infty)\) is the unique positive solution to

\[
\int_0^1 \exp\left[-c\tau_*\left(t\left(\frac{r_1}{n}-1\right)+\frac{r_n-r_1}{n}t^2\right)\right]dt=1.
\]

More generally, for each fixed \(\tau\geq0\),

\[
\lim_{N\to\infty}N\rho_C(\tau/N)=
\left[\int_0^1\exp\left(-c\tau\left[t\left(\frac{r_1}{n}-1\right)+\frac{r_n-r_1}{n}t^2\right]\right)dt\right]^{-1}.
\]

## Proof

**Hypergeometric payoff identity.** Conditional on a cooperator focal individual, the number of other cooperators in the group has law \(H_C\sim\mathrm{Hypergeom}(N-1,X-1,n-1)\). For a defector focal individual the corresponding law is \(H_D\sim\mathrm{Hypergeom}(N-1,X,n-1)\). Thus

\[
u_C-u_D=\frac{c}{n}\left[\mathbb E[(H_C+1)r(H_C+1)]-\mathbb E[H_Dr(H_D)]\right]-c.
\]

The first factorial-moment difference is
\(\mathbb E(H_C+1)-\mathbb EH_D=(N-n)/(N-1)\). For the quadratic term, the hypergeometric first and second factorial moments give

\[
\mathbb E[H_C(H_C+1)]-\mathbb E[H_D(H_D-1)]
=\frac{2(n-1)(X-1)(N-n)}{(N-1)(N-2)}.
\]

Substitution of the affine multiplier produces the exact expression

\[
\Delta_X:=u_C(X)-u_D(X)
=c\left[\frac{r_1}{K}-1+\frac{2(X-1)(r_n-r_1)}{K(N-2)}\right],\qquad1\leq X<N.
\]

Both stipulated update rules satisfy \(T_X^-/T_X^+=\exp(-w\Delta_X)\), with \(T_X^+\) and \(T_X^-\) the nonzero up/down one-step transition probabilities. Solving the birth-death harmonic equation with absorbing boundaries gives
\(\rho_C^{-1}=1+\sum_{j=1}^{N-1}\prod_{X=1}^jT_X^-/T_X^+\).
Summing the arithmetic progression \(\Delta_X\) proves the displayed exact fixation formula.

**Classification.** Summing these cumulative payoffs yields

\[
\sum_{j=0}^{N-1}P_j
=\frac{cN(N-1)}2\left[\frac{r_1+2r_n}{3K}-1\right].
\]

Write \(D(w)=\sum_{j=0}^{N-1}\exp(-wP_j)\). Then \(D(0)=N\), \(D'(0)=-\sum_jP_j\), and \(D''(w)=\sum_jP_j^2\exp(-wP_j)\). Apart from the identically neutral case, \(D''(w)>0\) for all real \(w\). For nonpositive \(\sum P_j\), Jensen's inequality implies \(D(w)\geq N\), with strict inequality at positive \(w\) unless every \(P_j=0\). If \(\sum P_j>0\) and all prefixes are nonnegative, \(D(w)<N\) for all positive \(w\). If instead some prefix is negative, \(D'(0)<0\), strict convexity holds, and \(D(w)\to\infty\) as \(w\to\infty\). Strict convexity gives exactly one positive stationary point of \(D\) and exactly one positive crossing of the level \(N\); since \(\rho_C=1/D\), these are respectively the maximum of fixation and the neutrality crossing.

To classify negative prefixes, observe that \(P_j/(cj)\) is affine in \(j\), taking the values \(r_1/K-1\) at \(j=1\) and \(r_n/K-1\) at \(j=N-1\). Therefore some \(P_j<0\) if and only if \(\min(r_1,r_n)<K\). Under the strict positive-mean condition the two multipliers cannot both be below \(K\). Finally \(P_{N-1}=c(N-1)(r_n/K-1)\), and the standard opposite-mutant fixation identity proves the claimed favored-versus-advantageous distinction.

**Population-size scaling.** With \(n,c,r_1,r_n\) fixed and \(N\to\infty\), \(K\to n\). Uniformly in \(j\in\{0,\ldots,N-1\}\),

\[
\frac{P_j}{N}-cG(j/N)\longrightarrow0,
\qquad G(t)=t\left(\frac{r_1}{n}-1\right)+\frac{r_n-r_1}{n}t^2.
\]

Consequently the Riemann sums \(D_N(\tau/N)/N\) converge, locally uniformly in \(\tau\in[0,\infty)\), to \(I(\tau)=\int_0^1e^{-c\tau G(t)}dt\). The strict parameter assumptions give \(\int_0^1G(t)dt=(r_1+2r_n-3n)/(6n)>0\) and \(G(t)<0\) on a nonempty open subinterval. Hence \(I(0)=1\), \(I'(0)<0\), \(I''(\tau)>0\), and \(I(\tau)\to\infty\); \(I\) has precisely one positive root of \(I(\tau)=1\). For all sufficiently large \(N\), the finite strict-reversal assumptions hold. Evaluate the locally uniform convergence on either side of the unique positive limiting root: the finite crossing is trapped between these two points, proving \(Nw_c(N)\to\tau_*\). The scaled fixation formula follows from reciprocation.

## Verification

The accompanying standalone `verify.py` uses Python 3 standard library only. It independently enumerates the focal hypergeometric payoff sums with exact rational arithmetic for finite population and group sizes and compares them to the analytical affine gap. It also checks the cumulative-payoff endpoint and sum identities, solves a one-step Fermi fixation recurrence, and brackets two strict neutrality crossings numerically. Execution passed 1777 assertions. The asymptotic numerical comparisons are illustrative Riemann-sum checks, not substitutes for the uniform-convergence proof.

For \(N=6\), \(n=3\), \(c=1\), \(r_1=4\), \(r_n=7\), the five nonzero cumulative payoffs are \((-1/5,-1/10,3/10,1,2)\), and \(w_c\approx5.592288595787\). Cooperation is favored over defection at every positive strength, yet becomes less likely to fix than a neutral mutant above this crossing. For \(r_1=9\), \(r_n=4\) instead, the cumulative payoffs are \((4/5,11/10,9/10,1/5,-1)\), and \(w_c\approx1.155476074721\). In both cases the weak-selection advantage and strong-selection disadvantage are strict.

Run with `python3 verify.py` in a Python 3 environment. The program has no external dependencies and does not load auxiliary data.

## Relationship to prior work

Hauert and McAvoy (2024) introduce and analyze this affine-multiplier public-goods model; their equations (26), (29)–(30) provide the generic fixation expression and finite-population payoff structure, and equations (31)–(34) prove **weak-selection** advantage conditions. In particular, the weak-selection condition used above is previously established and is *not* claimed as new. Their analytic discussion subsequently considers weak selection and numerical stationary distributions at different strengths. What is assessed here is the exact classification over **every positive strength**, uniqueness of the selection-induced neutrality reversal and the critical \(1/N\) strength scaling.

Hindersin, Wu, Traulsen and García (2019) discuss general evolutionary-game fixation computations and varying selection strengths without deriving these model-specific sharp reversals or their population-size limits. Wu, García, Hauert and Traulsen (2013) identify robustness of two-strategy **relative** fixation rankings under exponential or Fermi selection. Their ranking is not a comparison of a single strategy's fixation probability with neutral drift, which is why its invariance does not preclude the phenomenon proven here.

## Limitations

The result is exact for mutation-free, two-strategy, well-mixed finite populations with uniformly sampled groups, affine contributor-dependent public-good multiplication factors, and the specified exponential or Fermi update ratios. It does not assert corresponding universality for nonlinear payoff-to-fitness maps, finite mutation, population structure, other sampling protocols, or frequency-dependent selection intensity. The positive crossing of the *neutral* fixation benchmark must not be confused with a change of the *relative* fixation ordering of cooperation and defection. External independent validation and definitive historical priority review have not been performed.

## References

1. C. Hauert and A. McAvoy, **Frequency-dependent returns in nonlinear public goods games**, *Journal of the Royal Society Interface* **21** (2024), 20240334; arXiv:2404.13728, first posted 21 April 2024. https://arxiv.org/html/2404.13728v3 ; https://doi.org/10.1098/rsif.2024.0334
2. L. Hindersin, B. Wu, A. Traulsen and J. García, **Computation and Simulation of Evolutionary Game Dynamics in Finite Populations**, *Scientific Reports* **9** (2019), 6946. https://doi.org/10.1038/s41598-019-43102-z
3. B. Wu, J. García, C. Hauert and A. Traulsen, **Extrapolating Weak Selection in Evolutionary Games**, *PLOS Computational Biology* **9** (2013), e1003381. https://doi.org/10.1371/journal.pcbi.1003381
