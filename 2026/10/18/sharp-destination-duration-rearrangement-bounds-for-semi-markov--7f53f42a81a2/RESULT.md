# Sharp destination–duration rearrangement bounds for semi-Markov passage-time variance

## Finding

Fix a finite absorbing semi-Markov network. Keep both its embedded transition probabilities and the unconditional holding-time distribution at every nonabsorbing state fixed, while allowing the holding time and the next destination to be dependent. The mean time to absorption cannot change, but its variance has a **sharp, explicitly computable interval**. Both endpoints are attained *simultaneously for every initial state*: to maximize variance, assign the largest holding times to destinations having the largest remaining mean passage times; to minimize variance, reverse that assignment. The choice needs no nonlinear optimization over paths or conditional waiting-time laws.

Precisely, let the nonabsorbing states be \(1,\ldots,d\), with an absorbing state \(\partial\). Write \(p_{ij}\) for the embedded transition probability from \(i\) to \(j\in\{1,\ldots,d,\partial\}\), and let \(P=(p_{ij})_{1\le i,j\le d}\). Assume \(\rho(P)<1\), with \(\rho\) the spectral radius. At every visit to nonabsorbing state \(i\), draw a fresh pair \((H_i,J_i)\); its destination marginal is \(\Pr(J_i=j)=p_{ij}\), while its holding-time marginal \(F_i\) is fixed and has \(\Pr(H_i>0)=1\) and \(\mathbb E[H_i^2]<\infty\). The joint laws may otherwise vary arbitrarily from one admissible model to another, and fresh draws are conditionally independent of the past on entry to a state.

Define \(\mu_i=\mathbb E[H_i]\), \(\nu_i=\mathbb E[H_i^2]\), \(N=(I-P)^{-1}\), \(m=N\mu\), and \(m_\partial=0\). For each \(i\), list all positive-probability destinations as \(j_{i1},\ldots,j_{ik_i}\) in nondecreasing order of their \(m\)-values, breaking ties arbitrarily, and set \(c_{i0}=0\), \(c_{ir}=\sum_{s=1}^{r}p_{i,j_{is}}\). For the left quantile \(Q_i(u)=\inf\{t:F_i(t)\ge u\}\), put

\[
 a_i^+=\sum_{r=1}^{k_i}m_{j_{ir}}\int_{c_{i,r-1}}^{c_{ir}}Q_i(u)\,du,
 \qquad
 a_i^-=\sum_{r=1}^{k_i}m_{j_{ir}}\int_{1-c_{ir}}^{1-c_{i,r-1}}Q_i(u)\,du.
\]

With \(a^\pm=(a_1^\pm,\ldots,a_d^\pm)^\top\), **for every admissible collection of destination–duration joint laws and every initial nonabsorbing state \(i\)**,

\[
 \boxed{\ [N(\nu+2a^-)]_i-m_i^2\ \le\ \operatorname{Var}_i(T_\partial)\ \le\ [N(\nu+2a^+)]_i-m_i^2.\ }
\]

A *single* simultaneous minimizer is realized at each state by \(H_i=Q_i(U_i)\) and choosing destination \(j_{ir}\) when \(U_i\in(1-c_{ir},1-c_{i,r-1})\); a single simultaneous maximizer uses \(U_i\in(c_{i,r-1},c_{ir})\). Each \(U_i\) is a fresh uniform variate at each visit. At any fixed initial state, **every intermediate variance value is attainable** by mixing the two extremal joint kernels. When a state \(k\) reachable from \(i\) before absorption has a nonconstant holding time and at least two positive-probability destinations with different remaining means, the bounds for \(i\) are strict.

## Assumptions and scope

The network has finitely many nonabsorbing states and one absorbing state, and the embedded chain reaches the absorbing state almost surely from every nonabsorbing state. The condition \(\rho(P)<1\) is exactly the required finite-state transience condition. Holding times are strictly positive almost surely and have finite second moments; atoms, lattice laws, and dependencies between holding time and selected destination are permitted. The result concerns passage starting *at state entry*, not a stationary-age or residual-life observation. An absorbing target set can be contracted to \(\partial\). The theorem does not require reversibility, irreducibility among transient states, or moment-generating functions.

## Proof

**1. Passage moments.** Starting at entry into state \(i\), the regenerative identity is \(T_i=H_i+T_{J_i}'\), where \(T_\partial'=0\) and, conditional on \(J_i=j\), the future \(T_j'\) is a fresh copy of the passage time from \(j\), independent of \(H_i\). Thus first moments satisfy \(m_i=\mu_i+\sum_{j\le d}p_{ij}m_j\), proving \(m=N\mu\) independently of the destination–duration dependence. Let \(h_i=\mathbb E[T_i^2]\). Expansion gives

\[
 h_i=\nu_i+2\sum_j\mathbb E[H_i\mathbf1_{\{J_i=j\}}]m_j
       +\sum_{j\le d}p_{ij}h_j.
\]

Define \(a_i=\mathbb E[H_im_{J_i}]\). Then \(h=N(\nu+2a)\) and \(\operatorname{Var}_i(T_i)=h_i-m_i^2\). The moments are finite: an absorbing finite-state embedded chain has a geometrically decaying number of pre-absorption visits, and its first and second moment equations with finite forcing have finite nonnegative solutions. Equivalently, apply monotone iteration to truncated passage sums and dominate by the finite vector \(N(\nu+2\|m\|_\infty\mu)\).

**2. Exact local extrema.** At state \(i\), the two marginals of \((H_i,m_{J_i})\) are fixed. The second has finitely many values \(m_{j_{ir}}\), with masses \(p_{i,j_{ir}}\). The classical two-marginal rearrangement inequality gives the exact lower and upper bounds \(a_i^-\le a_i\le a_i^+\). An elementary finite proof swaps crossed pairs: if \(x<x'\) and \(y<y'\), replacing pairings \((x,y'),(x',y)\) with \((x,y),(x',y')\) increases the sum of products by \((x'-x)(y'-y)>0\). Approximation by quantile step functions extends this to arbitrary integrable holding laws because the destination means are bounded. Monotone and reverse-monotone quantile assignments attain the two expressions above, even if \(F_i\) has atoms.

**3. Global extrema and attainable interval.** The Green matrix \(N=I+P+P^2+\cdots\) is entrywise nonnegative. Applying it to the local inequalities, and subtracting the common squared mean, yields the asserted variance envelope. The local quantile assignments can be made independently at all states, so they realize the lower or upper endpoint *for every starting state simultaneously*. For any \(\lambda\in[0,1]\), replacing every local joint kernel by the mixture \(\lambda Q_i^+ +(1-\lambda)Q_i^-\), with a fresh mixture selection at each visit, preserves both marginals and gives \(a=\lambda a^++(1-\lambda)a^-\); hence the variance at each initial state runs through its entire interval. If the local holding law and destination residual-mean law are both nonconstant, strict rearrangement gives \(a_k^+>a_k^-\). Whenever \(k\) is reachable from \(i\) before absorption, \(N_{ik}>0\); the \(i\)-th interval then has positive width.

**4. Exact three-state illustration.** Take \(1\to2\) or \(\partial\), each with probability \(1/2\), and \(2\to\partial\) surely. Let \(H_1\sim\operatorname{Unif}(0,2)\) and \(H_2=1\). All allowable couplings have \(\mathbb E_1T_\partial=3/2\). Sending the *lower* half of \(H_1\) to state \(2\) produces \(T_\partial\sim\operatorname{Unif}(1,2)\), with variance \(1/12\). Sending the *upper* half to state \(2\) gives a half-and-half mixture of \(\operatorname{Unif}(0,1)\) and \(\operatorname{Unif}(2,3)\), with variance \(13/12\). Independent destination choice yields variance \(7/12\). Thus dependence alone changes the variance by a factor of \(13\) while preserving every specified holding marginal, transition probability, and passage mean.

## Verification

The standalone `verify.py` uses exact rational arithmetic (standard Python only). It enumerates all \(6^3=216\) assignments of four equiprobable holding-time atoms to two destinations in a three-transient-state feedback network, recomputes passage means and variances from the renewal equations, and verifies that one sorted assignment and one reverse-sorted assignment attain the extrema for **all three starts simultaneously**. It also checks the three-state continuous example by exact moment integration. Its recorded run passed **1,954 exact rational assertions**. These finite tests are illustrative, not the proof of the universal theorem; the latter is Steps 1–3 above.

## Relationship to prior work

Voits (2026, arXiv:2610.13505v1), especially Definition 1 and Theorem 15, develops the semi-Markov kernel and complete hitting-time moment formulas; invariance of the mean under the associated pseudo-rates is prior work. Le, van der Burg, Heidergott, Lindner and Zocca (2026, arXiv:2603.26414v1), especially Theorem 2 and Appendix A, calculate variances and derivatives for random edge traversal costs. Butler and Bronson (2002), especially Section 2, derive semi-Markov first-passage transforms. None of these inspected statements fixes each *state's unconditional holding-time law* and the embedded transition matrix, then optimizes over the **dependence between holding duration and next destination** to obtain simultaneously attainable quantile envelopes across all starting states. The two-marginal rearrangement principle itself is classical (see Glasserman and Yao, 2004); its use is not claimed as new. The assessed contribution is the exact **network-wide optimization and strictness statement under fixed rowwise marginals**, not the known renewal equations or rearrangement inequality in isolation.

## Limitations

No uniqueness of the optimizing joint kernels is claimed (ties or atoms can produce nonunique assignments). The theorem concerns second moments only: the same ordering need not optimize higher moments or every tail probability. It does not cover infinite state spaces, infinite second holding moments, nonrenewal correlations between successive visits, or starting at a positive elapsed age. More general semi-Markov dependence/optimization theorems might subsume the result; independent priority examination remains necessary.

## References

1. J. B. Voits, *Graph-theoretic framework for semi-Markov networks: transient and stationary occupation probabilities, hitting times and weak ergodicity breaking*, arXiv:2610.13505v1 (first submitted 2026-10-09), https://arxiv.org/html/2610.13505v1.
2. T. Le, R. van der Burg, B. Heidergott, I. Lindner, A. Zocca, *Random Walks with Traversal Costs: Variance-Aware Performance Analysis and Network Optimization*, arXiv:2603.26414v1 (2026-03-27), https://arxiv.org/abs/2603.26414.
3. R. W. Butler and D. A. Bronson, *Bootstrapping Survival Times in Stochastic Systems by Using Saddlepoint Approximations*, Journal of the Royal Statistical Society B 64 (2002), 31–49, doi:10.1111/1467-9868.00323.
4. P. Glasserman and D. D. Yao, *Optimal couplings are totally positive and more*, Journal of Applied Probability 41 (2004), 321–332.
