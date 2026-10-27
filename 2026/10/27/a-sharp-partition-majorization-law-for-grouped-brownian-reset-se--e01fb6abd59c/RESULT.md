# A sharp partition-majorization law for grouped Brownian reset search

## Finding

Consider \(n\ge2\) independent one-dimensional Brownian searchers with diffusivity \(D>0\), each starting at \(x_0>0\), and a common absorbing target at the origin. Partition the searchers into \(k\) nonempty groups of sizes \(\lambda=(\lambda_1,\ldots,\lambda_k)\), where \(1\le k\le n\) and \(\sum_i\lambda_i=n\). Each group possesses an independent rate-\(r\) Poisson clock, with \(r>0\); at each event all members of that group instantaneously return to \(x_0\). A search succeeds when **any** searcher first reaches the target. Write \(T_\lambda\) for this completion time and \(S_\lambda(t)=\Pr(T_\lambda>t)\).

For every \(t>0\), let \(\mathcal R_t\) be a single group's Poisson reset schedule, let \(\Delta_0,\ldots,\Delta_{J_t}\) be the gaps it cuts out of \([0,t]\), and set
\[
q(s)=\begin{cases}\operatorname{erf}\!\left(x_0/\sqrt{4Ds}\right),&s>0,\\1,&s=0,\end{cases}\qquad
Z_t=\prod_{j=0}^{J_t}q(\Delta_j),\qquad
m_a(t)=\mathbb E[Z_t^a]\ (a\ge0).
\]
Then the exact survival law is
\[
\boxed{S_\lambda(t)=\prod_{i=1}^k m_{\lambda_i}(t).}
\]
For fixed \(n,k\), if the group-size vector \(\lambda\) **majorizes** \(\nu\) (their entries are rearranged decreasingly and \(\sum_{i\le j}\lambda_i\ge\sum_{i\le j}\nu_i\) for every \(j<k\)), then
\[
\boxed{S_\lambda(t)\ge S_\nu(t)\quad\text{for every }t\ge0.}
\]
At every \(t>0\), the inequality is strict unless the vectors have the same multiset of group sizes. If \(n=ak+b\) with integers \(a\ge1\), \(0\le b<k\), the **unique up to group relabeling** optimal and worst allocations at a fixed number of reset clocks are respectively
\[
\begin{aligned}
\lambda_{\mathrm{bal}}&=(\underbrace{a+1,\ldots,a+1}_{b},\underbrace{a,\ldots,a}_{k-b}),\\
\lambda_{\mathrm{uneven}}&=(n-k+1,\underbrace{1,\ldots,1}_{k-1}),\\
\boxed{m_{a+1}(t)^b m_a(t)^{k-b}}
&\ \le S_\lambda(t)\le\ 
\boxed{m_{n-k+1}(t)m_1(t)^{k-1}}.
\end{aligned}
\]
Here optimal means **maximizing** the chance of detection by each fixed deadline, equivalently minimizing target survival. The displayed bounds are sharp and strict for all nonextremal size multisets at \(t>0\).

Moreover, **merging any two reset groups** strictly increases \(S_\lambda(t)\) for every \(t>0\). Thus balanced assignment is best for a fixed number of independent clocks, while giving every searcher its own clock is best overall. These are stochastic orders of the entire first-detection-time laws, not just comparisons of their means. The means are finite at every \(r>0\) and satisfy the same strict comparisons.

## Assumptions and scope

Brownian increments are independent across searchers and restart independently after every reset. Group clocks are independent and identically distributed, with the same positive Poisson rate, and a reset restores a searcher to the same initial distance \(x_0\) with no refractory period. A comparison changes **only** which walkers share clocks, not any individual's marginal reset rate. All stated strict orders compare different size multisets at fixed \(n,k\), or a genuine merger, and assume \(t>0\), \(r>0\).

The proof's moment-order mechanism also works for any common law of independent group reset schedules and any identically distributed, completely renewed individual search process: its inequalities are weak generally and strict whenever the schedule-conditional single-searcher survival probability is nondegenerate. The Brownian-Poisson assumptions guarantee nondegeneracy and finite mean search times. At \(r=0\) all groupings coincide.

## Proof

**1. Conditional survival and exact factorization.** Conditional on a clock realization with gaps \(\Delta_j\), a single searcher must independently survive each Brownian excursion between successive resets. The reflection principle gives \(q(s)=\Pr(\inf_{0\le u\le s}(x_0+\sqrt{2D}W_u)>0)\) in the displayed error-function form. Independent renewal of Brownian excursions makes its conditional survival probability \(Z_t=\prod_j q(\Delta_j)\). Conditional independence of the \(\lambda_i\) members sharing one schedule gives \(Z_t^{\lambda_i}\). Different groups have independent clocks and Brownian motions, proving \(S_\lambda(t)=\prod_i m_{\lambda_i}(t)\) without approximations.

**2. The common-survival variable is nonconstant.** For fixed \(t>0\), the no-reset event has probability \(e^{-rt}>0\) and gives \(Z_t=q(t)\). The exactly-one-reset event also has positive probability, and its time \(u\) has a continuous density on \((0,t)\); it gives \(Z_t=q(u)q(t-u)\). Since \(q'(0+)=0\) and \(q'(t)<0\),
\[
q(u)q(t-u)-q(t)=-u q'(t)+o(u)>0
\quad(u\downarrow0).
\]
Hence \(Z_t\) is genuinely random, with \(0<Z_t\le1\).

**3. Strict log-convexity.** By strict Cauchy-Schwarz for nonconstant positive \(Z_t\),
\[
m_j(t)^2<m_{j-1}(t)m_{j+1}(t)\qquad(j\ge1).
\]
Therefore the ratios \(m_{j+1}(t)/m_j(t)\) strictly increase with \(j\). If two group sizes satisfy \(A\ge B+2\), balancing one searcher from the larger to the smaller yields
\[
m_A(t)m_B(t)>m_{A-1}(t)m_{B+1}(t).
\]
Iterating integer balancing transfers establishes the majorization order and the sharp balanced and maximally uneven extremizers. Strictness follows at each nontrivial transfer.

**4. Merging independent clocks is harmful.** Let \(Z_t'\) be an independent copy of \(Z_t\). For positive integers \(A,B\),
\[
\begin{aligned}
m_{A+B}(t)-m_A(t)m_B(t)
&=\operatorname{Cov}(Z_t^A,Z_t^B)\\
&=\frac12\mathbb E\left[(Z_t^A-Z_t'^A)(Z_t^B-Z_t'^B)\right]>0.
\end{aligned}
\]
The integrand is nonnegative because both powers are strictly increasing functions of the same positive variable; it is positive with positive probability by Step 2. Multiplication by the other groups' positive moment factors proves strict survival increase under any genuine merger. Iteration gives the overall independent-versus-synchronized extremum.

**5. First-passage stochastic orders and finite means.** The inequalities hold pointwise for \(S_\lambda(t)=\Pr(T_\lambda>t)\), so they give the asserted usual stochastic orders. For finite expectation, fix \(s>0\). Whatever a surviving searcher's current location, the event of at least one reset in the first \(s\) of the next \(2s\) time units, no reset in the last \(s\), and a Brownian hit from \(x_0\) in that last \(s\), has conditional probability at least
\[
p_s=(1-e^{-rs})e^{-rs}(1-q(s))>0.
\]
Earlier hits only aid completion. Independence of future clocks and Brownian increments makes the conditional chance of continuing without detection through each such block at most \(1-p_s\). Consequently \(\Pr(T_\lambda>2js)\le(1-p_s)^j\) for every integer \(j\ge0\), and all means are finite. Integrating strict inequalities over positive \(t\) gives strict mean comparisons.

## Verification

The proof is exact and does not use finite numerical experiments to establish an infinite-dimensional stochastic assertion. The standalone script `check.py` checks the majorization and merger identities by exact rational arithmetic in an independent two-point conditional-survival environment, for every integer partition with up to twelve searchers. It also evaluates a Brownian schedule's distinct no-reset and one-reset survival values. Running `python3 check.py` reproduces `check_output.txt`, reporting 1,533 passed assertions. These finite checks are diagnostic only; Steps 1–5 establish the theorem for all permitted parameters, group sizes, and times.

For seven searchers controlled by three identical-rate clocks, the theorem implies that groups of sizes \((3,2,2)\) give strictly earlier first detection in stochastic order than \((4,2,1)\), which in turn outperform \((5,1,1)\), at every positive rate and every positive time. No optimization over the reset rate is needed for this ordering.

## Relationship to prior work

Biroli, Majumdar and Schehr (arXiv:2303.18012, first publicly posted 2023-03-31) calculate mean first-passage times and optimal resetting thresholds for two endpoint protocols: independently resetting walkers and fully synchronized resetting. Their protocol-specific survival formulas are acknowledged as prior results. Their article does not formulate or classify intermediate group allocations with a fixed number of independent reset clocks or establish the time-by-time majorization extremizers here. The comparison of those two endpoints alone can also follow from elementary Jensen's inequality; it is **not** asserted as a newly discovered endpoint phenomenon.

Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563) analyze position, spacing and extremes of the synchronously resetting Brownian gas without the present target-first-hit allocation problem. Lee and collaborators (arXiv:2412.02524) consider dynamically chosen group reset locations and a distinct avoidance problem. Suarez-Jimenez, Riascos and Boyer (arXiv:2604.20770) consider first *encounter*, when walkers occupy a target node simultaneously, not the present first hit by **any** walker. The distinction is essential: synchronous resets can help encounter tasks and cannot be compared to the present first-detection order without changing the event.

The mathematical step uses classical log-convexity and positive covariance of powers of one random variable. Its claimed contribution is the full deadline-uniform reset-controller allocation classification and strict stochastic ordering for this multi-searcher setting, not invention of those inequalities.

## Limitations

The classification requires statistically identical searchers, independent group clocks with identical marginal laws, and complete resetting of the individual dynamics. It does not order arbitrary incomparable size vectors, different per-group reset rates, interacting particles, position-dependent common reset rules, first-encounter targets, or the optimal-rate values themselves. Strict comparison at each **fixed** positive reset rate need not remain strict after separately minimizing mean first-passage times over rates that include zero. An undiscovered prior application of classical moment-majorization inequalities to grouped resetting remains a scholarly priority risk; no independent priority audit has been performed.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (first posted 2023-03-31); *Phys. Rev. E* **107**, 064141 (2023).
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first posted 2022-11-01).
3. J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General Resetting Theory for Group Avoidance*, arXiv:2412.02524 (first posted 2024-12-03); *Phys. Rev. Research* **8**, 013227 (2026).
4. C. D. Suarez-Jimenez, A. P. Riascos and D. Boyer, *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770 (first posted 2026-04-22).
5. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first posted 2025-09-08).
