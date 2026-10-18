# Spatial Poisson limits for late dimer arrivals in Page–Rényi parking

## Finding

Place \(n\ge2\) initially empty sites in a line. For each edge \(i\in\{1,\ldots,n-1\}\), let \(\xi_i\) be an independent exponential random variable of mean one. Examine edges in increasing order of \(\xi_i\), accepting a dimer on sites \(i,i+1\) precisely when both sites are then vacant. Write \(A_i=1\) for acceptance, and \(A_i=0\) otherwise.

**Theorem (late-deposition field).** The point measure
\[
\Xi_n=\sum_{i=1}^{n-1}A_i\,\delta_{\left(i/n,\,\xi_i-\log n\right)}
\]
converges vaguely in distribution on \([0,1]\times\mathbb R\) to a Poisson point process with intensity
\[
\nu(du,dx)=e^{-2}\,du\,e^{-x}dx.
\]
In particular, the spatial locations of the final \(k\) successful dimers, for any fixed positive integer \(k\), converge jointly to \(k\) independent uniform locations on \([0,1]\), independent of their jointly centered arrival times.

Put
\[
W_n(x)=\sum_{i=1}^{n-1}A_i\mathbf1\{\xi_i>\log n+x\},
\qquad \mu(x)=e^{-2-x}.
\]
For every compact \(K\subset\mathbb R\) there are finite constants \(C_K,n_K\) such that, for every \(n\ge n_K\),
\[
\sup_{x\in K}d_{\mathrm{TV}}\bigl(\mathcal L(W_n(x)),\operatorname{Poisson}(\mu(x))\bigr)
\le C_K\frac{\log n}{n}.
\]
A finite-size identity underlying the bound is as follows. Define \(H_m(u)=\sum_{j=0}^{m-1}(-u)^j/j!\) for integer \(m\ge1\) and \(0\le u\le1\). For every \(i\in\{1,\ldots,n-1\}\) and \(t\ge0\),
\[
\Pr(A_i=1,\xi_i>t)=
\int_{1-e^{-t}}^1H_i(u)H_{n-i}(u)\,du.
\tag{1}
\]
The scalar law \(\Pr(\max_{i:A_i=1}\xi_i-\log n\le x)\to\exp[-e^{-2-x}]\) follows, but is **not** asserted as novel: a Gumbel jamming-time prediction with this centering constant for dimer adsorption was already stated by De Smedt, Godrèche and Luck (2002). The new assertion is the entire spatially marked late-arrival Poisson field together with a quantitative count approximation.

## Assumptions and scope

The sites form the open finite path \(\{1,\ldots,n\}\), and dimers occupy adjacent pairs, with no desorption, reattempt advantage or periodic boundary. The clocks \(\xi_i\) are independent exponential variables of rate one; their first arrival suffices because a rejected edge can never become available again. Both time and spatial coordinates use the normalization in the theorem. Point-process convergence means vague convergence on bounded spatial regions and time sets bounded on both sides. The approximation concerns the **integer count** \(W_n(x)\), not total variation between a discrete spatial process and a continuous spatial Poisson process.

## Proof

**1. Exact one-edge law.** Transform each clock by \(U_i=1-e^{-\xi_i}\); these variables are independent uniform variables on \([0,1]\) and preserve the order of attempts. In a path of \(m\) sites, let \(h_m(u)\) denote the probability that its rightmost site is still empty after all edges with \(U_i\le u\) have attempted. Obviously \(h_1(u)=1\). For \(m\ge2\), the only attempt that can occupy the last site is at edge \(m-1\). Conditional on that edge attempting at time \(v\), its other endpoint is vacant exactly when the endpoint of the independent smaller path of \(m-1\) sites is vacant at \(v\). Therefore
\[
h_m(u)=1-\int_0^u h_{m-1}(v)\,dv,
\qquad h_1(u)=1,
\]
so induction gives \(h_m(u)=H_m(u)\). Now condition on \(U_i=u\). Edge \(i\) succeeds precisely when the two sites adjacent to it are both vacant. The two remaining subpaths, of lengths \(i\) and \(n-i\), are independent, so its conditional success probability is \(H_i(u)H_{n-i}(u)\). Integrating over \(u>1-e^{-t}\) proves (1). This also gives an exact rational value for every unconditional finite-size acceptance probability by integrating the polynomial over \([0,1]\).

For \(u\in[0,1]\), Taylor's alternating-series remainder gives
\[
|H_m(u)-e^{-u}|\le\frac1{m!}.
\]
Both functions lie in \([0,1]\), hence
\[
\left|H_i(u)H_{n-i}(u)-e^{-2u}\right|
\le\frac1{i!}+\frac1{(n-i)!}.
\tag{2}
\]
Write \(q(t)=\int_{1-e^{-t}}^1e^{-2u}\,du=\tfrac12e^{-2}(e^{2e^{-t}}-1)\). Summing (1) and (2), for any \(t\ge0\), yields the explicit boundary-uniform estimate
\[
\left|\mathbb E\sum_i A_i\mathbf1\{\xi_i>t\}-(n-1)q(t)\right|
\le 2(e-1)e^{-t}.
\tag{3}
\]
At \(t=\log n+x\), uniformly for \(x\) in compact sets, (3) and Taylor expansion imply
\[
\mathbb E W_n(x)=e^{-2-x}+O_K(n^{-1}).
\tag{4}
\]
Replacing the lower integration endpoint in (1) by an interval of transformed clock values similarly gives the expected counts in every bounded spacetime rectangle. The limiting intensity is \(e^{-2}du\,e^{-x}dx\).

**2. Quantitative stabilization.** The acceptance indicator of edge \(i\) is determined recursively by its earlier, lower-clock adjacent edges. A chain of causal predecessors leaving the window of edges \(\{j:|j-i|\le L\}\) must be a strictly decreasing sequence of at least \(L+2\) clocks along the path, moving monotonically either left or right. Each of the two possible sequences has probability \(1/(L+2)!\). Thus, if \(A_i^{[L]}\) is the indicator obtained by running the greedy procedure only on that window, coupled with the same clocks, then
\[
\Pr(A_i\ne A_i^{[L]})\le\frac2{(L+2)!}.
\tag{5}
\]
The definition also applies at the finite-path boundaries, where there are fewer possible chains. For \(L=\lceil\log n\rceil\), the probability that **any** indicator differs is at most \(2(n-1)/(L+2)!\), smaller than \(\log n/n\) for sufficiently large \(n\).

**3. Quantitative Poisson count.** Let \(B_i=A_i^{[L]}\mathbf1\{\xi_i>\log n+x\}\). Variables \(B_i,B_j\) are independent when \(|i-j|>2L\), and for distinct indices \(i,j\),
\[
\Pr(B_i=1)\le e^{-t},\qquad
\Pr(B_i=B_j=1)\le e^{-2t},\qquad t=\log n+x,
\]
because both events require their respective independent clocks to exceed \(t\). With dependency neighborhoods of at most \(4L+1\) indices, the standard dependency-graph Chen–Stein bound gives
\[
d_{\mathrm{TV}}\!\left(\mathcal L\Big(\sum_iB_i\Big),
\operatorname{Poisson}\Big(\sum_i\mathbb EB_i\Big)\right)
\le 2(n-1)(8L+1)e^{-2t}.
\tag{6}
\]
Combine (4), (5), (6), the coupling inequality for total variation, and \(d_{\mathrm{TV}}(\operatorname{Poisson}(a),\operatorname{Poisson}(b))\le|a-b|\). For \(x\in K\), the right side is bounded by \(C_K\log n/n\), proving the displayed uniform bound.

**4. Full spacetime process.** Consider finitely many pairwise disjoint rectangles in \([0,1]\times\mathbb R\), each with time coordinate bounded below. Form the count in each rectangle using the localized events in Step 2. For any fixed joint factorial-moment order \(k\), the number of ordered \(k\)-tuples of distinct edges with two positions at distance at most \(2L\) is \(O_k(Ln^{k-1})\). The probability of any such tuple of late arrivals is at most \(C_k n^{-k}\), because its \(k\) distinct exponential clocks must all exceed a fixed lower threshold of the form \(\log n+s\). Thus all close tuples contribute \(O_k(L/n)\). For separated tuples, the localized windows are disjoint, hence their marked indicators are independent; (1)–(4) give limiting factorial moments equal to those of independent Poisson variables of means prescribed by \(\nu\). The coupling error in (5) is \(o(1)\). These mixed factorial moments determine the limiting independent Poisson rectangle counts, and the bounded first moments give local tightness. This proves vague point-process convergence.

**5. Last successful arrivals.** For every fixed \(x\), the Poisson count in Step 3 yields the stated Gumbel marginal limit. The upper tail is tight since
\[
\Pr\left(\max_{i:A_i=1}\xi_i>\log n+B\right)
\le(n-1)e^{-\log n-B}\le e^{-B}.
\]
For each fixed \(k\), the expected limiting number of points above a sufficiently negative time threshold tends to infinity. These two facts justify taking the last \(k\) points of the limiting process. Since its intensity is a product of Lebesgue measure in space and a continuous measure in time, their spatial coordinates are independent uniforms, independent of the ordered times.

## Verification

The companion `check.py` is a standalone Python 3 program requiring only the standard library. Run `python3 check.py`. It independently enumerates early-arrival edge subsets and their orderings to verify the finite endpoint-vacancy polynomial, enumerates every ordering of the edge clocks for path sizes 2–9 to verify (1) at \(t=0\), and checks that every discrepancy caused by radius-one or radius-two truncation has the decreasing causal path asserted in Step 2. It uses exact rational arithmetic. Its finite checks are not substitutes for Steps 1–5, which prove the all-size statements.

## Relationship to prior work

De Smedt, Godrèche and Luck (2002), Section 5, explicitly state that their earlier Gumbel jamming-time law applies also to dimer deposition, with constant \(\alpha=p^2e^{-2p}\). For an initially vacant path (their \(p=1\)), this is \(e^{-2}\). Consequently, **the scalar Gumbel law, including its centering, is prior art**, not the novelty asserted here. Their discussion does not give a spatially marked Poisson limit or a total-variation error rate for late successful dimer counts.

Gerin (2015), Theorems 5 and 7 and Lemma 8, proves the infinite-volume occupancy-time law, gives a logarithmic-scale result for the number of trials and localizes rare late accepted sites. It provides key motivating tools, but not the finite edge-by-edge formula (1), the spatial Poisson extreme-process statement, or the quantitative \(O(\log n/n)\) Poisson-count bound. Penrose and Sudbury (2005) provide general exact forward equations and normal approximations for random deposition counts, rather than this rare late-arrival process. Purvis, Reeve, Wattis and Mao (2015) analyze near-jamming availability and coverage scaling, not a multitime marked Poisson limit. Standard Chen–Stein dependency-graph theory is used as an existing tool, not claimed as a new method.

## Limitations

The theorem is specific to nearest-neighbor dimers on a finite path with independent rate-one exponential first arrivals. It does not establish corresponding laws for longer cars, irregular graphs, edge-dependent clocks or continuous-location parking. Spatial convergence is weak/vague, not total variation against a continuous spatial process. The stated rate concerns one threshold count at a time and need not be sharp. A complete independent historical-priority assessment of all later adsorption literature remains outstanding. Independent external scientific validation has not been performed.

## References

- G. De Smedt, C. Godrèche and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465 (first public February 26, 2002), Sections 2.3, 3 and 5. See in particular Section 5's dimer Gumbel statement.
- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, *Annals of Applied Probability* 15 (2005), 853–889, arXiv:math/0503519.
- L. Gerin, *The Page–Rényi parking process*, *Electronic Journal of Combinatorics* 22 (2015), #P4.4, arXiv:1411.8002 (first public November 28, 2014).
- B. Purvis, L. Reeve, J. A. D. Wattis and Y. Mao, *Scaling behavior near jamming in random sequential adsorption*, *Physical Review E* 91 (2015), 022118.
- R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: The Chen–Stein method*, *Annals of Probability* 17 (1989), 9–25.
