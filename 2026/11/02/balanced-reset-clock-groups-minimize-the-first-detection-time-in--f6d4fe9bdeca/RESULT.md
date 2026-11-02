# Balanced reset-clock groups minimize the first detection time in Brownian search

## Finding

Consider a team of \(N\) independent identically prepared searchers, with \(K\) independent and statistically identical renewal clocks, where \(1\le K\le N\). Each clock synchronously returns all searchers in its assigned group to the same starting configuration. Search terminates when the first searcher reaches a common target. For any positive integer group sizes \(\mathbf n=(n_1,\ldots,n_K)\) with \(\sum_j n_j=N\), its first-detection survival is
\[
\Pr(T_{\mathbf n}>t)=\prod_{j=1}^K M_{n_j}(t),\qquad M_m(t)=\mathbb E[Q_t^m],
\]
where \(Q_t\) is one searcher's no-hit probability conditional on a single clock history up to \(t\).

**Fixed-controller classification.** For every \(t\ge0\) and every identical independent clock law, this survival probability is minimized over all \(K\)-group partitions by the *balanced* sizes: with \(N=Ka+b\), \(0\le b<K\), there are \(K-b\) groups of size \(a\) and \(b\) groups of size \(a+1\). It is maximized by \((N-K+1,1,\ldots,1)\). Splitting any existing group across two independent identical clocks weakly accelerates detection in usual stochastic order. For Brownian searchers on the half-line, positive starting distance, positive diffusivity, and a positive finite Poisson resetting rate, every nontrivial balancing or splitting improvement is **strict at every \(t>0\)**; the balanced group-size multiset is the unique fixed-\(K\) optimum, up to group relabeling.

The smallest nontrivial exact comparison occurs for \(N=4\), \(K=2\):
\[
\Pr(T_{(3,1)}>t)-\Pr(T_{(2,2)}>t)=M_3(t)M_1(t)-M_2(t)^2
=\frac12\mathbb E\left[Q_t^{(1)}Q_t^{(2)}\big(Q_t^{(1)}-Q_t^{(2)}\big)^2\right]>0,
\]
for independent clock-history copies \(Q_t^{(1)},Q_t^{(2)}\) in the stated Brownian–Poisson regime. Thus the result orders the **entire first-detection distributions**, not only their means.

## Assumptions and scope

A single searcher, started from a fixed initial configuration, has a target first-passage survival \(S_0(u)\in[0,1]\), \(S_0(0)=1\). Each resetting event starts a fresh independent copy of its no-reset trajectory; searchers are independent conditional on their reset clocks. Each group uses a renewal process starting with age zero, with i.i.d. strictly positive interarrival durations and almost surely finitely many events in compact time intervals. Different groups have independent, identically distributed clocks, and groups form a partition of the \(N\) labeled searchers. The comparison fixes the common interarrival law and \(N,K\); it changes only group membership, not resetting rates or search physics.

For one clock history with renewal times \(0=\tau_0<\tau_1<\cdots<\tau_m<t=\tau_{m+1}\), define
\[
Q_t=\prod_{i=0}^m S_0(\tau_{i+1}-\tau_i).
\]
Always \(0\le Q_t\le1\). Brownian specialization: a walker starts at \(x_0>0\) on \((0,\infty)\), has diffusion coefficient \(D>0\), is absorbed at zero and reset to \(x_0\) at clock rate \(r>0\), with
\[
S_0(0)=1,\qquad S_0(u)=\operatorname{erf}\!\left(\frac{x_0}{\sqrt{4Du}}\right)\quad (u>0).
\]

## Proof

**1. Conditional survival.** For each fixed clock realization, a single searcher avoids the target throughout \([0,t]\) precisely when all reset-to-reset excursions avoid it. Independence of excursions gives conditional survival \(Q_t\). For a group of \(m\) searchers on the same clock, their conditional joint no-hit probability is \(Q_t^m\). Integrating over that clock gives \(M_m(t)\); independence of the clocks assigned to distinct groups yields the product formula. This also establishes the formula for arbitrary (non-Poisson) renewal laws satisfying the scope hypotheses.

**2. Transfer inequality and all extrema.** Let \(Q,Q'\) be independent copies of \(Q_t\). For integers \(a\ge b+2\ge3\), direct symmetrization gives the exact identity
\[
M_aM_b-M_{a-1}M_{b+1}
=\frac12\mathbb E\!\left[(QQ')^b
 (Q^{a-b-1}-{Q'}^{a-b-1})(Q-Q')\right]\ge0.
\]
The integrand is nonnegative for \(Q,Q'\ge0\). Moving one searcher from a larger group of size \(a\) to a smaller group of size \(b\), whenever their sizes differ by at least two, therefore weakly decreases the overall target survival at every time. Repeating this move terminates at precisely the balanced sizes \((a,\ldots,a,a+1,\ldots,a+1)\). In reverse, transferring members from smaller groups to a largest group, until the other groups are singletons, weakly increases survival. This proves both global extrema (Schur convexity in the integer group-size vector) for every renewal law. Strictness holds whenever the distribution of \(Q_t\) assigns positive probability to two distinct positive values, since the integrand is then positive on a positive-probability event.

**3. Extra controllers.** Splitting a group of size \(a+b\), with positive \(a,b\), replaces the factor \(M_{a+b}\) by \(M_aM_b\). For an independent pair \(Q,Q'\),
\[
M_{a+b}-M_aM_b=\frac12\mathbb E[(Q^a-{Q'}^a)(Q^b-{Q'}^b)]\ge0.
\]
All other factors stay nonnegative. Hence splitting never increases target survival, and decreases it strictly if \(Q_t\) is nondegenerate on strictly positive values. A chain of splits also compares different controller budgets.

**4. Strictness for Brownian Poisson resetting.** Fix any \(t>0\). With probability \(e^{-rt}>0\), no reset occurs and \(Q_t=S_0(t)>0\). With positive probability there is exactly one reset with its epoch \(u\) in an arbitrarily short nonempty interval near zero; then \(Q_t=S_0(u)S_0(t-u)>0\). Since \(S_0(u)=1-o(u)\) as \(u\downarrow0\) and \(S_0'(t)<0\) for \(t>0\),
\[
S_0(u)S_0(t-u)=S_0(t)-uS_0'(t)+o(u)>S_0(t)
\]
for all sufficiently small \(u>0\). Thus \(Q_t\) is nonconstant with two strictly positive separated ranges at every \(t>0\); all nontrivial inequalities above are strict. In particular, any nonbalanced group-size vector can be improved by a finite chain of strict transfers, proving unique balanced optimality up to relabeling. The exact four-searcher gap follows by expanding the transfer identity with \(a=3,b=1\).

**5. Distributional and mean consequences.** The comparison is pointwise in \(t\), so it is usual stochastic order, and expectation of any nondecreasing measurable cost of detection time is correspondingly ordered whenever defined. For positive-rate Poisson resetting the mean detection time is finite, since the team's first hit is no later than that of any selected individual searcher, whose mean Brownian resetting detection time is \((e^{x_0\sqrt{r/D}}-1)/r<\infty\). This completes the proof.

## Verification

The supplied self-contained `verify.py` uses exact rational arithmetic to test 42 positive two-point-law transfer identities and a convergent trapezoidal discretization of the exact Brownian–Poisson renewal equation to test a further 28 strict moment and grouping comparisons at four positive observation times (70 assertions total). It can be run with `python3 verify.py` using only Python's standard library.

For Brownian resetting, every clock moment \(M_m\), \(m\in\mathbb N\), obeys the exact Volterra equation
\[
M_m(t)=e^{-rt}S_0(t)^m+r\int_0^t e^{-ru}S_0(u)^mM_m(t-u)\,du.
\]
The numerical reproduction uses \(D=x_0=1\), \(r=1.3\), and mesh width \(0.005\), reporting the independent, balanced, imbalanced and fully shared survival probabilities for \(N=4\) at \(t=0.25,0.5,1,2\). The analytical proof, not the finite checks, establishes strict all-time inequalities.

## Relationship to prior work

Biroli, Majumdar and Schehr (2023, arXiv:2303.18012) develop the Brownian target-search mean first-passage problem under two **extreme** protocols: all clocks independent, or one shared reset clock (their Sections III–IV, including renewal equations (4) and (20)). The present theorem resolves a distinct fixed-controller-budget question that interpolates those extremes via arbitrary finite group partitions, proves *distribution-wide* optimizer and pessimal partitions, and allows general renewal clocks. The source's renewal formulas are background, not claimed as new.

De Mauro, Biroli, Majumdar and Schehr (2025, arXiv:2509.06658) analyze collective simultaneous non-Poissonian resetting for stationary spatial statistics. Their concluding discussion explicitly distinguishes possible partial-particle resetting and first-passage extensions from their solved stationary questions. Their reset mechanism does not imply a fixed independent-clock grouping or its partition extremizers. The present strict inequality depends on common-clock survival moments, not merely on stationary spatial correlations.

## Limitations

The theorem assumes identical searchers and statistically identical independent reset clocks, synchronized only **within** permanently assigned disjoint groups, with full excursion renewal. It does not compare unequal rate budgets, adaptive regrouping, partial-position resetting, interactions or feedback-based resets. General weak extrema can tie in degenerate cases; strict uniqueness is proved for the stated Brownian–Poisson model, not for every renewal process. Finite numerical checks do not certify the infinite-horizon theorem, which follows analytically. The result is a mathematical statement about ideal processes, not an implementation cost or physical engineering model.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (first posted 2023-03-31), Phys. Rev. E 107, 064141 (2023). https://arxiv.org/pdf/2303.18012
2. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025). https://arxiv.org/pdf/2509.06658
