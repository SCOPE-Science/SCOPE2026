# A phase-resolved reliability law for two-season seed-bank rescue

## Finding

A finite cohort of seeds can be divided in advance between two establishment seasons, which may share arbitrarily correlated good/bad environmental conditions. Whenever each season has positive probability of being the **only** favorable season, the asymptotically optimal first-season allocation fraction is determined solely by the two within-good-season per-seed failure probabilities, regardless of the probability or correlation of environmental states. The excess chance of no establishment above unavoidable simultaneous bad seasons decays at a sharp exponential rate. Its leading constant does **not** generally converge: it follows an explicit lattice-phase law, and for irrational allocation fractions its accumulation points form a complete interval. If a singly favorable environmental state disappears, the optimal fraction moves to an endpoint.

## Assumptions and scope

Let \(N\ge1\) be an integer. A fixed decision \(k\in\{0,\ldots,N\}\) assigns \(k\) initially viable seeds to first-season establishment and \(N-k\) seeds to second-season establishment. This is a precommitted, nonadaptive allocation; successful early recruitment terminates the question but does not alter the prescribed trials. No new seeds enter the cohort, and storage survival can be incorporated into the effective conditional success rate of the second-season attempts.

Let \((G_1,G_2)\in\{0,1\}^2\) indicate season suitability, and write \(q_{ij}=\Pr(G_1=i,G_2=j)\). Their joint law is unrestricted except for \(q_{ij}\ge0\) and \(\sum_{ij}q_{ij}=1\). Conditional on \((G_1,G_2)\), seed-level establishment events are mutually independent, with per-seed success probability \(1-a\) for first-season seeds if \(G_1=1\), and \(1-b\) for second-season seeds if \(G_2=1\). A bad season permits no establishment. Assume \(0<a,b<1\). The objective is to maximize the probability of **at least one** establishment over both seasons; it is neither a long-run growth-rate objective nor a stochastic-population persistence criterion.

The exact no-establishment probability is
\[
F_N(k)=q_{00}+q_{10}a^k+q_{01}b^{N-k}+q_{11}a^k b^{N-k}.
\]
The convention \(a^0=b^0=1\) applies when a season receives no seeds. Put \(E_N=\min_{0\le k\le N}F_N(k)-q_{00}\).

**Two exclusive-good-season states present.** Assume \(q_{10}>0\) and \(q_{01}>0\). Set
\[
A=-\log a,\qquad B=-\log b,\qquad
\theta=\frac{B}{A+B},\qquad \lambda=\frac{AB}{A+B},
\]
and
\[
C=q_{10}e^{A/2}+q_{01}e^{B/2}+q_{11}e^{|A-B|/2}.
\]
For every \(N\ge1\),
\[
\min(q_{10},q_{01})e^{-\lambda N}\le E_N\le Ce^{-\lambda N}.
\]
Every minimizing integer \(k_N\) satisfies the *finite-budget* bounds
\[
\theta N-\frac{\log(C/q_{10})}{A}\le k_N\le
\theta N+\frac{\log(C/q_{01})}{B}.
\]
Consequently \(k_N/N\to\theta\) and \(\lim_{N\to\infty}N^{-1}\log E_N=-\lambda\). For any \(N\), the function \(F_N\) is strictly convex on its real extension to \([0,N]\); hence the minimizing integer choices are at most two adjacent integers, obtainable from the floor and ceiling of the clipped continuous minimizer.

**Exact phase correction.** Let
\[
G(t)=q_{10}e^{-At}+q_{01}e^{Bt},\quad
h(x)=\min_{m\in\mathbb Z}G(m-x),
\]
with
\[
t_0=\frac{\log(Aq_{10}/(Bq_{01}))}{A+B},\qquad
 t_c=\frac{\log(q_{10}(1-a)/(q_{01}(b^{-1}-1)))}{A+B}.
\]
Then \(t_c<t_0<t_c+1\), \(h\) is continuous, nonconstant and 1-periodic, and its image is exactly \([G(t_0),G(t_c)]\). For all sufficiently large \(N\), more specifically all \(N\) satisfying
\[
N\min(\theta,1-\theta)\ge |t_0|+2,
\]
one has the quantitative phase estimate
\[
0\le E_N-e^{-\lambda N}h(\theta N)
\le q_{11}e^{|B-A|(|t_0|+1)}e^{-2\lambda N}.
\]
If \(\theta\) is irrational, the accumulation set of the normalized errors \(e^{\lambda N}E_N\) is **the entire closed interval** \([G(t_0),G(t_c)]\). If \(\theta\) is rational, the normalized errors approach a finite, periodic set of phase constants instead.

**Support boundary.** If \(q_{10}=0<q_{01}\), every optimal first-season count \(k_N\) is bounded independently of \(N\), and \(k_N/N\to0\). If \(q_{01}=0<q_{10}\), every optimal second-season count \(N-k_N\) is bounded independently of \(N\), and \(k_N/N\to1\). When both exclusive-good-season probabilities are zero, the only reducible term is \(q_{11}a^k b^{N-k}\), minimized by allocating all seeds to the season with the smaller conditional failure probability (or by every allocation if \(a=b\)); if \(q_{11}=0\), every allocation ties.

For an explicit irrational-phase illustration, choose \(a=1/2\), \(b=1/3\), \(q_{10}=q_{01}=1/8\), \(q_{11}=1/4\), \(q_{00}=1/2\). Then \(\theta=\log3/\log6\) is irrational, because rationality would imply that positive integer powers of 2 and 3 coincide. Hence the leading normalized reducible-failure prefactor has an interval, not a single limit.

## Proof

**1. Exact failure law.** Conditional on \((G_1,G_2)=(0,0)\), establishment always fails. Conditional on \((1,0)\), all \(k\) active seeds must independently fail, with probability \(a^k\). Conditional on \((0,1)\), the corresponding probability is \(b^{N-k}\). Conditional on \((1,1)\), both groups must fail, with probability \(a^kb^{N-k}\). Weighting by the four environmental state probabilities yields the stated \(F_N(k)\) without assuming independence between the two environments.

**2. Strict convexity and finite-budget bounds.** The real extension of \(F_N-q_{00}\) is a nonnegative sum of exponentials. Its second derivative is
\[
q_{10}A^2e^{-Ak}+q_{01}B^2e^{-B(N-k)}
+q_{11}(B-A)^2e^{-Ak-B(N-k)},
\]
which is strictly positive when \(q_{10},q_{01}>0\). The continuous minimizer is unique, and convexity restricts the integer minimizers to the adjacent floor and ceiling, clipped to the feasible interval.

For a lower bound, either \(k\le\theta N\), when \(q_{10}a^k\ge q_{10}e^{-\lambda N}\), or \(k\ge\theta N\), when \(q_{01}b^{N-k}\ge q_{01}e^{-\lambda N}\). In both cases all other terms are nonnegative. For the upper bound choose an integer \(k_0\in[0,N]\) within half a unit of \(\theta N\). Then the first two terms are at most \(q_{10}e^{A/2}e^{-\lambda N}\) and \(q_{01}e^{B/2}e^{-\lambda N}\); the joint-good term is at most \(q_{11}e^{|A-B|/2}e^{-2\lambda N}\), which is bounded by the same coefficient times \(e^{-\lambda N}\). Thus the stated upper and lower bounds hold. Each of the two positive single-good terms evaluated at a true minimizer is bounded above by \(Ce^{-\lambda N}\); taking logarithms gives the explicit window for \(k_N\). The exponential limit follows by squeezing.

**3. Integer phase law.** Write \(k=\theta N+t\). Direct substitution gives the exact decomposition
\[
F_N(k)-q_{00}=e^{-\lambda N}G(t)
+q_{11}e^{-2\lambda N}e^{(B-A)t}.
\]
The function \(G\) is strictly convex, diverges at both infinities, and has its unique real minimum at \(t_0\). Minimizing \(G\) over the integer translate \(\mathbb Z-\theta N\) gives \(h(\theta N)\). Every lattice minimizer lies between the neighboring lattice points around \(t_0\), so its distance to zero is at most \(|t_0|+1\). For \(N\min(\theta,1-\theta)\ge |t_0|+2\), the corresponding first-season count is feasible. Evaluating the exact decomposition at that lattice minimizer and using positivity of the correction proves both sides of the displayed phase estimate.

The sign of \(G(t+1)-G(t)\) changes exactly at \(t_c\), because
\[
G(t+1)-G(t)=
-q_{10}(1-e^{-A})e^{-At}
+q_{01}(e^B-1)e^{Bt}.
\]
For an optimal lattice point its coordinate \(t\) therefore belongs to \([t_c,t_c+1]\), and the endpoint values of \(G\) agree. The inequalities \(t_c<t_0<t_c+1\) follow, respectively, from \(1-e^{-A}<A\), \(e^B-1>B\), and from \(e^A-1>A\), \(1-e^{-B}<B\). As the lattice phase varies, the optimal coordinate sweeps both sides of \(t_0\) inside that interval, and \(G\) attains precisely its minimum \(G(t_0)\) and maximum \(G(t_c)\); continuity fills the interval. Integer relabeling proves \(h(x+1)=h(x)\), and coercivity of \(G\) proves continuity of the minimum over the translated lattice. For irrational \(\theta\), the set of fractional parts \(\{\theta N\}\), \(N\ge1\), is dense in the circle, so every value in the continuous range of \(h\) is a subsequential limit. The phase error tends uniformly to zero after multiplication by \(e^{\lambda N}\). For rational \(\theta\), the phase orbit is finite.

**4. Support boundary.** If \(q_{10}=0<q_{01}\), factor the reducible failure probability as
\[
F_N(k)-q_{00}=b^N b^{-k}(q_{01}+q_{11}a^k).
\]
The factor in parentheses is at least \(q_{01}>0\), and hence the function \(b^{-k}(q_{01}+q_{11}a^k)\) tends to infinity as the nonnegative integer \(k\) increases. Its global minimum occurs among a fixed finite set of integers, independent of \(N\). All minimizing feasible \(k_N\) are therefore eventually in that fixed set; for smaller \(N\) they are trivially bounded by the same fixed maximum. The case \(q_{01}=0<q_{10}\) follows by exchanging the seasons. If both vanish, direct comparison of the single joint-good product proves the last assertion.

## Verification

Run `python3 verify_seed_bank.py` with Python's standard library. The checker evaluates the exact failure expression against direct enumeration of all binary seed outcomes for small cohorts, checks discrete strict convexity, all integer optimal allocations and the finite-budget bounds for 2,592 parameter/budget profiles, and tests the two support boundaries. An additional analytical asymptotic calculation in the proof establishes the phase law for all cohort sizes; finite enumeration alone is not offered as an infinite proof.

## Relationship to prior work

Dormancy as temporal risk spreading is established in ecological life-history theory. Snyder (2006) studies interactions between dormancy, seed dispersal and space-time environmental correlations using evolutionary optimality; the full accessible paper does not optimize the one-off probability of any successful recruit in a finite preassigned cohort. Valleriani (2006) examines evolutionarily stable germination under correlated yields, a different objective; the full paper was not available for decisive chapter/appendix comparison. ten Brink, Gremer and Kokko (2020) examine long-term geometric-mean fitness and within-season phenology; their accessible full analysis is not an exact two-season finite-cohort rescue allocation theorem. Reliability allocation with common-cause failures is a natural general mathematical neighbor: Bai, Yun and Chung (1991) optimize redundant unit counts and mean cost rates, not the two-channel preassigned seed cohort. The novelty claim is restricted to the combined finite-budget allocation bounds, sharp and phase-resolved asymptotic law, and support-dependent discontinuity for the specified ecological rescue objective. No claim is made to introduce dormancy, geometric-mean bet hedging or common-cause reliability optimization.

## Limitations

The seed cohort size is fixed, allocation is chosen before environmental outcomes, all seed-level trials are conditionally independent, and environment states are binary and shared within each season. The result does not optimize evolutionary growth, recruitment numbers beyond the first success, conditional monitoring/adaptive reallocation, regeneration of the seed bank, or population persistence. Positive masses for both exclusive-good-year states are essential to the interior allocation law; the boundary cases are qualitatively different. The phase law assumes all model probabilities remain fixed as \(N\) grows. Uninspected or unindexed prior literature may contain more general statements that imply parts of these formulas. A self-review is not an independent audit.

## References

1. R. E. Snyder, “Multiple risk reduction mechanisms: can dormancy substitute for dispersal?”, *Ecology Letters* 9 (2006), 1106–1114, DOI: 10.1111/j.1461-0248.2006.00962.x. Author-hosted complete PDF: https://case.edu/biology/snyder/pubs/el2006.pdf. First online 2006-08-29.
2. A. Valleriani, “Evolutionarily stable germination strategies with time-correlated yield”, *Theoretical Population Biology* 70 (2006), 255–261, DOI: 10.1016/j.tpb.2006.07.008.
3. H. ten Brink, J. R. Gremer and H. Kokko, “Optimal germination timing in unpredictable environments: the importance of dormancy for both among- and within-season variation”, *Ecology Letters* 23 (2020), 620–630, DOI: 10.1111/ele.13461. Open-access full text: https://onlinelibrary.wiley.com/doi/full/10.1111/ele.13461.
4. D. S. Bai, W. Y. Yun and S. W. Chung, “Redundancy optimization of k-out-of-n systems with common-cause failures”, *IEEE Transactions on Reliability* 40 (1991), 56–59, DOI: 10.1109/24.75334.
