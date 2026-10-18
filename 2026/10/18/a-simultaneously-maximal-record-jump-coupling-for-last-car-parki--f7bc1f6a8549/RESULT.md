# A simultaneously maximal record-jump coupling for last-car parking deficits

## Finding

For each integer \(n\ge1\), choose a classical parking function uniformly from the \((n+1)^{n-1}\) successful preference lists of \(n\) labeled cars and \(n\) consecutively numbered spaces. Let \(J_n\) be the parking space occupied by the final car, and \(D_n=n+1-J_n\) its distance from the right boundary, including its own space. These definitions specify separate probability distributions, not a joint experiment across sample sizes.

**Theorem (simultaneous maximal record-jump coupling).** There is an increasing integer-valued Markov process \((X_n)_{n\ge1}\), with \(X_n\overset{\mathrm d}=D_n\) and \(X_1=1\), whose only transitions from a state \(m\le n\) at stage \(n\) are **stay at \(m\)** and **jump to the newly exposed state \(n+1\)**. It converges almost surely to a finite standard Borel random variable \(B\), with \(\Pr(B=m)=b_m=e^{-m}m^{m-1}/m!\). Moreover, this *single* coupling attains the total-variation lower bound at every stage simultaneously:

\[
\Pr(X_n\ne B)=d_{\mathrm{TV}}(D_n,B)=\Pr(B>n)
=\sum_{m=n+1}^{\infty}\frac{e^{-m}m^{m-1}}{m!}.
\]

The same value is the Kolmogorov distance \(\sup_{t\in\mathbb R}|\Pr(D_n\le t)-\Pr(B\le t)|\). In fact \(D_n\preceq_{\mathrm{st}}D_{n+1}\preceq_{\mathrm{st}}B\), and the positive mass at **each** old state strictly decreases with \(n\).

The sharp second-order error is
\[
 d_{\mathrm{TV}}(D_n,B)
 =\sqrt{\frac2\pi}\,n^{-1/2}
 -\frac5{9\sqrt{2\pi}}\,n^{-3/2}+O(n^{-5/2}).
\]

Under the constructed process, the number of jumps is finite almost surely but has **infinite expectation**: the expected number through stage \(N\) is \(e^{-1}\log N+O(1)\). This is a property of the specified coupling, not of a canonical joint parking construction.

## Assumptions and scope

The parking rule is one-way: car \(i\) tries its preferred location and, if occupied, advances to the first unoccupied location to the right. The uniform law is on *successful* full preference lists, with order of car arrivals fixed. Integers satisfy \(n\ge1\) and \(1\le m\le n\). Write \(p_n(m)=\Pr(D_n=m)\); set \(p_n(m)=0\) outside its support. By Pinsky's Corollary 5, the exact marginal distribution is
\[
 p_n(m)=\frac1n\binom{n}{n+1-m}
 \frac{(n+1-m)^{n+1-m}m^{m-2}}{(n+1)^{n-1}},
\]
where at \(m=1\), \(m^{m-2}=1\) by the evident value \(1^{-1}=1\). All statements concern probability distributions; no coupling of actual preference lists of different lengths is claimed.

## Proof

**1. Strict loss of mass at every old state.** For \(1\le m\le n\), direct cancellation of the preceding probability formula gives
\[
 \frac{p_{n+1}(m)}{p_n(m)}
 =\frac n{n+2}\left(\frac{n+1}{n+2}\right)^{n-1}
 \left(1+\frac1{n+1-m}\right)^{n+1-m}.
\]
The map \(x\mapsto(1+1/x)^x\) is strictly increasing for \(x>0\); consequently the ratio is largest at \(m=1\). Now
\[
 p_n(1)=\left(\frac n{n+1}\right)^{n-1}
\]
is strictly decreasing in \(n\). Indeed, for real \(x\ge1\), the logarithmic derivative of its smooth extension is
\[
 -\log(1+1/x)+\frac{x-1}{x(x+1)}<0,
\]
because \(\log(1+1/x)>1/(x+1)\). Thus \(0<p_{n+1}(m)<p_n(m)\) on every old state.

**2. Transition kernel.** Start with \(X_1=1\). Conditional on \(X_n=m\), let
\[
 \Pr(X_{n+1}=m\mid X_n=m)=\frac{p_{n+1}(m)}{p_n(m)},
 \qquad
 \Pr(X_{n+1}=n+1\mid X_n=m)=1-\frac{p_{n+1}(m)}{p_n(m)}.
\]
These are valid probabilities by step 1. Inductively the mass at each old state is \(p_{n+1}(m)\), and mass conservation places the remaining amount \(p_{n+1}(n+1)\) at the new state. This proves all marginals and the asserted record-jump transition restriction. The kernel is uniquely forced among Markov kernels with only these two possible destinations.

**3. Finite terminal state and simultaneous optimality.** Pinsky's exact marginal law has \(p_n(m)\to b_m\) for each fixed \(m\ge1\). Since \(X_n\) is nondecreasing, \(B=\lim_nX_n\) exists in \(\mathbb N\cup\{\infty\}\); for every finite \(k\),
\[
 \Pr(B\le k)=\lim_{n\to\infty}\Pr(X_n\le k)
 =\sum_{m=1}^k b_m.
\]
The Borel masses sum to one, so \(B<\infty\) almost surely, and integer monotonicity implies eventual stabilization. A trajectory that ends at \(m\) must reach \(m\) no later than stage \(m\), since a transition can enter a new state only when that state is first exposed; hence for \(n\ge m\), \(B=m\) forces \(X_n=m\). Therefore
\[
 \{X_n=B\}=\{B\le n\},\qquad
 \Pr(X_n\ne B)=\Pr(B>n).
\]
Every law supported on \(\{1,\ldots,n\}\) is at total-variation distance at least \(\Pr(B>n)\) from the Borel law, by testing the complement of that set. The displayed coupling meets this bound; thus it is simultaneously maximal at all \(n\).

**4. Pointwise and stochastic refinements.** For the Borel probability \(b_m\), cancellation yields, for \(1\le m\le n\),
\[
 \frac{p_n(m)}{b_m}
 =\frac{e^m(n-1)!(n+1-m)^{n+1-m}}
 {(n+1-m)!(n+1)^{n-1}}.
\]
The consecutive ratio across \(m\) is
\[
 \frac{p_n(m+1)/b_{m+1}}{p_n(m)/b_m}
 =e\left(1-\frac1{n+1-m}\right)^{n-m}>1
 \quad(1\le m<n),
\]
since \(\log(1+1/t)<1/t\). At \(m=1\), \(p_n(1)/b_1=e[n/(n+1)]^{n-1}>1\). Therefore \(p_n(m)>b_m\) at every \(m\le n\), and the cumulative-distribution difference is positive at each proper threshold and maximized at \(n\). The likelihood-ratio ordering additionally gives \((B\mid B\le n)\preceq_{\mathrm{st}}D_n\preceq_{\mathrm{st}}B\). The construction in step 2 gives \(D_n\preceq_{\mathrm{st}}D_{n+1}\) directly.

**5. Sharp error and jump count.** Stirling's expansion implies
\[
 b_m=\frac1{\sqrt{2\pi}}m^{-3/2}
 \left(1-\frac1{12m}+O(m^{-2})\right).
\]
Euler--Maclaurin summation over \(m>n\) gives
\[
 \sum_{m>n}m^{-3/2}=2n^{-1/2}-\tfrac12n^{-3/2}+O(n^{-5/2}),
 \qquad
 \sum_{m>n}m^{-5/2}=\tfrac23n^{-3/2}+O(n^{-5/2}),
\]
which proves the displayed two-term error formula. For \(k\ge2\), the jump at stage \(k\) occurs precisely when \(X_k=k\), with probability
\[
 p_k(k)=\frac{k^{k-2}}{(k+1)^{k-1}}
 =\frac1{ek}\bigl(1+O(k^{-1})\bigr).
\]
The expected jump count through \(N\) is the sum from \(k=2\) to \(N\), hence \(e^{-1}\log N+O(1)\); its infinite total mean coexists with a.s. finitely many jumps because the terminal state is finite.

## Verification

Run `python verify.py` with Python 3 and the standard library. The checker independently enumerates all successful preference lists through \(n=7\) and compares their final-car deficits with the closed finite law. Exact `fractions.Fraction` computations check normalization, every cross-size mass inequality, conservation of the record-jump transition, and successive likelihood ratios for \(n\le100\). Floating-point calculations separately sanity-check the Borel comparisons and limiting total-variation constant. All 735 programmed assertions passed. The unrestricted inequalities, existence and convergence of the process, and asymptotics are analytical arguments above, not consequences of finite enumeration.

## Relationship to prior work

Pinsky (2024), Corollaries 5--6, supplies the exact one-size final-car position law and its Borel weak limit; these formulas and limits are expressly used rather than claimed as new. Diaconis and Hicks (2016), Theorem 1 and Corollary 3, supplies a distinct parking-preference statistic with an equivalent finite distribution under reindexing, and a Borel limit. The contribution here is the **across-all-sizes** strict pointwise mass-loss law, a specified unique stay-or-new-maximum Markov coupling, its simultaneous optimality for total variation, and the finite-almost-sure/infinite-mean jump-count phenomenon. These are genuine consequences of the earlier exact law, so an implicit prior deduction remains a priority risk. They are not claimed to strengthen the earlier formulas for arbitrary complete parking-permutation distributions or the fixed-size joint last-car statistics.

## Limitations

The coupling links distributions, not actual nested uniform random preference lists, and does not preserve the joint positions of several final cars. The infinite expected number of jumps refers only to this explicitly constructed process. The novelty assessment reflects inspected published work, not a proof of historical priority. Total variation at stage \(n\) is controlled by the Borel tail; it does not supply uniform approximation of unbounded test functions (the critical Borel distribution has infinite mean).

## References

1. R. G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529 (first posted 2024-04-17), especially Corollaries 5 and 6. https://arxiv.org/abs/2404.11529
2. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821 (first posted 2016-11-29), especially Theorem 1 and Corollary 3. https://arxiv.org/abs/1611.09821
3. A. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, arXiv:2108.08661 (2021), contrasting preference-coordinate asymptotics. https://arxiv.org/abs/2108.08661
