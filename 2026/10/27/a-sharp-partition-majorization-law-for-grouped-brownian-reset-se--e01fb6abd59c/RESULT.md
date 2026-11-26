# A sharp partition-majorization law for grouped Brownian reset search

## Finding

Consider \(n\ge2\) one-dimensional Brownian searchers with independent Brownian driving noises and diffusivity \(D>0\), each starting at \(x_0>0\), and a common absorbing target at the origin. Partition the searchers into \(k\) nonempty groups of sizes \(\lambda=(\lambda_1,\ldots,\lambda_k)\), where \(1\le k\le n\) and \(\sum_i\lambda_i=n\). Each group has an independent rate-\(r\) Poisson clock, with \(r>0\); at each event all members of that group instantly return to \(x_0\). A search succeeds when **any** searcher first reaches the target. Write \(T_\lambda\) for this completion time and \(S_\lambda(t)=\Pr(T_\lambda>t)\).

For \(t>0\), let \(\Delta_0,\ldots,\Delta_{J_t}\) be the gaps cut out of \([0,t]\) by a single group's Poisson reset schedule. Set
\[
q(s)=\begin{cases}\operatorname{erf}\!\left(x_0/\sqrt{4Ds}\right),&s>0,\\1,&s=0,\end{cases}
\qquad Z_t=\prod_{j=0}^{J_t}q(\Delta_j),\qquad m_a(t)=\mathbb E[Z_t^a]\quad(a\ge0).
\]
Then the exact survival law is
\[
\boxed{S_\lambda(t)=\prod_{i=1}^k m_{\lambda_i}(t).}
\]
For fixed \(n,k\), if \(\lambda\) **majorizes** \(\nu\) (entries sorted in decreasing order and \(\sum_{i\le j}\lambda_i\ge\sum_{i\le j}\nu_i\) for every \(j<k\)), then
\[
\boxed{S_\lambda(t)\ge S_\nu(t)\quad\text{for every }t\ge0.}
\]
At every \(t>0\) the inequality is strict unless the vectors have the same multiset of group sizes. Writing \(n=ak+b\) with integers \(a\ge1\), \(0\le b<k\), the optimal and worst allocations at fixed \(k\) are respectively the balanced vector with \(b\) parts of size \(a+1\) and \(k-b\) of size \(a\), and \((n-k+1,1,\ldots,1)\). Each is unique up to group relabelling. Explicitly,
\[
m_{a+1}(t)^b m_a(t)^{k-b}\ \le S_\lambda(t)\le\ m_{n-k+1}(t)m_1(t)^{k-1}.
\]
Here optimal means maximizing the chance of detection by each fixed deadline. At \(t>0\) each bound is strict away from its attaining size multiset.

Merging any two groups strictly increases \(S_\lambda(t)\) for every \(t>0\). Thus independent clocks for every searcher are best overall, and a single shared clock is worst. These are stochastic orders of the whole first-detection laws. The means are finite at \(r>0\) and satisfy the same strict comparisons.

## Assumptions and scope

Clocks are independent of the Brownian driving noises. Brownian excursions restart independently after every reset; a reset restores the same distance \(x_0\) with no refractory period. Comparisons change only which searchers share clocks, not the individual reset rate. At \(r=0\) all groupings have the same law.

The factorization and weak moment orders also apply to identically distributed, completely renewed searchers with independent individual randomness and independent, identically distributed group schedules independent of that randomness. Use their schedule-conditional single-searcher survival probability as \(Z_t\). For that broader observation, a sufficient condition for the strict orders at a deadline is that \(Z_t>0\) almost surely and \(Z_t\) is nonconstant. Nondegeneracy alone is not enough for strict fixed-\(k\) majorization orders when \(Z_t\) may vanish: if \(Z_t\) takes only values \(0,z\) for some \(z>0\), each partition with the same \(n,k\) gives \(\Pr(Z_t=z)^k z^n\). The Brownian–Poisson model satisfies the positive, nonconstant condition at each \(t>0\); finiteness of the means is asserted for that model.

## Proof

**Conditional survival.** By the reflection principle, the no-reset survival probability over an interval of length \(s\) is \(q(s)\). Condition on one group's reset history. The excursions must all survive, giving \(Z_t=\prod_j q(\Delta_j)\) for one searcher. Conditional independence gives \(Z_t^{\lambda_i}\) for a group of size \(\lambda_i\). Averaging and using independence of groups yields \(S_\lambda(t)=\prod_i m_{\lambda_i}(t)\).

**Positivity and nondegeneracy.** The Poisson schedule has almost surely finitely many gaps and \(q(s)>0\) for each finite \(s\), so \(Z_t>0\). The no-reset event has probability \(e^{-rt}>0\) and gives \(Z_t=q(t)\). The exactly-one-reset event has positive probability and its reset time \(u\) has a density positive on \((0,t)\). The survival then is \(q(u)q(t-u)\). Since \(q'(0+)=0\) and \(q'(t)<0\),
\[
q(u)q(t-u)-q(t)=-u q'(t)+o(u)>0\qquad(u\downarrow0).
\]
Thus \(Z_t\) is nonconstant at every \(t>0\).

**Fixed number of clocks.** Cauchy–Schwarz applied to \(Z_t^{(j-1)/2}\) and \(Z_t^{(j+1)/2}\) gives \(m_j(t)^2\le m_{j-1}(t)m_{j+1}(t)\) for integers \(j\ge1\), with strict inequality for positive nonconstant \(Z_t\). Here \(m_0(t)=1\) even for a broader model in which \(Z_t\) can be zero. When \(m_1(t)>0\), the ratios \(m_{j+1}(t)/m_j(t)\) are nondecreasing (strictly increasing under the strictness condition). For group sizes \(A\ge B+2\), the step to \((A-1,B+1)\) therefore does not increase the two-moment product, and strictly decreases it in the Brownian case. Integer majorization is generated, up to permutations, by these unit balancing transfers. This gives the claimed order and the two extremal size multisets. If \(Z_t=0\) almost surely in the broader setting, all positive-size group survival probabilities vanish and the weak order holds trivially.

**Merging clocks.** For positive integers \(A,B\) and an independent copy \(Z_t'\),
\[
 m_{A+B}(t)-m_A(t)m_B(t)
 =\tfrac12\mathbb E\big[(Z_t^A-(Z_t')^A)(Z_t^B-(Z_t')^B)\big].
\]
The two powers are strictly increasing on \([0,1]\), so the integrand is nonnegative and it is positive with positive probability whenever \(Z_t\) is nonconstant. In that case every other group's moment is positive too. This proves the strict increase on a genuine merger in the Brownian setting. Repeated mergers give the extremizers over all choices of \(k\).

**Finite means.** Fix \(s>0\) and a designated searcher. In any new block of length \(2s\), the event of at least one clock reset in the first \(s\) and none in the second \(s\) has probability \((1-e^{-rs})e^{-rs}\), independent of the past. Conditional on such a schedule, if the search has not already succeeded by the last reset, the designated searcher starts at \(x_0\) at that reset and has a reset-free interval of length at least \(s\) before the block ends. The probability of success by the end of the block is at least \(1-q(s)\) in that case; an earlier hit already counts as success. Thus each block, conditional on survival up to its start, has success probability at least
\[
p_s=(1-e^{-rs})e^{-rs}(1-q(s))>0.
\]
Consequently \(\Pr(T_\lambda>2js)\le(1-p_s)^j\) for integers \(j\ge0\). The means are finite, and integrating the strict pointwise survival inequalities over \(t>0\) gives the strict mean comparisons.

## Verification

The proof is analytic. The supporting `check.py` and `check_output.txt` record 1,533 finite diagnostic cases and checks, including moment-order comparisons for integer partitions of up to twelve searchers in a two-point conditional-survival model, and an example of distinct Brownian no-reset and one-reset survival values. These checks do not establish the claims for arbitrary parameters or check the broader strictness condition when survival can vanish.

For seven searchers controlled by three identical-rate clocks, groups of sizes \((3,2,2)\) give strictly earlier first detection in stochastic order than \((4,2,1)\), which in turn outperform \((5,1,1)\), at each positive rate. No optimization over rates is required.

## Relationship to prior work

Biroli, Majumdar and Schehr [1] give survival formulas and mean first-passage optimization for two endpoint protocols: independent resetting and fully synchronized resetting. The two-endpoint survival order also follows from Jensen's inequality and is not claimed new here. The two-searcher equal-distance result *Opposite sign survival correlations from a common reset clock* (Resultary `04868fbce99a`) gives the strict merger comparison for two singleton Brownian groups. The statement here concerns arbitrary group sizes and fixed-clock-count allocations, not just those endpoint or two-searcher cases.

Biroli, Larralde, Majumdar and Schehr [2] study the position, spacing and extreme statistics of the synchronously resetting Brownian gas. Lee and collaborators [3] consider dynamically chosen reset locations and avoidance. Suarez-Jimenez, Riascos and Boyer [4] consider first encounter when walkers occupy a target node together, not first hit by any searcher. De Mauro and collaborators [5] study conditional independence for a stationary Brownian gas with simultaneous resetting. Gonçalves, Madrid and Ramos [6] derive majorization comparisons for products of sample block averages, rather than products of group-conditional survival moments. Nothing here claims novelty for classical log-convexity or covariance inequalities; their application classifies arbitrary comparable allocations in this resetting model. The literature comparison is bounded and not a determination of historical priority.

## Limitations

The theorem does not order incomparable size vectors, unequal group rates, heterogeneous or interacting searchers, first-encounter targets, or state-dependent common resetting. Strict comparisons at one fixed positive rate need not remain strict after separately optimizing over rates that include zero.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012; Phys. Rev. E **107**, 064141 (2023).
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563.
3. J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General Resetting Theory for Group Avoidance*, arXiv:2412.02524; Phys. Rev. Research **8**, 013227 (2026).
4. C. D. Suarez-Jimenez, A. P. Riascos and D. Boyer, *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770.
5. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658.
6. Gonçalves, Madrid and Ramos, *Convex Order, Log-Convexity and Moments of Averages of Random Variables*, arXiv:2608.00813.
