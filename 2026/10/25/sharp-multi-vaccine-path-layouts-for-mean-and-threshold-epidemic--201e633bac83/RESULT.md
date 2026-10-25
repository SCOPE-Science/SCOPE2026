# Sharp multi-vaccine path layouts for mean and threshold epidemic risk

## Finding

Fix integers \(k\ge 2\), \(n\ge k+3\), and \(3\le t\le n-k\), and a transmission parameter \(0<p<1\). On a path of \(n\) individuals vaccinate exactly \(k\) individuals perfectly, choose one initial infected individual uniformly among the \(N=n-k\) unvaccinated individuals, and retain each edge between unvaccinated neighbors independently with probability \(p\). The final epidemic size \(X\) is the size of the retained-edge connected component of the seed.

Write \(b=k+1\), and let \(L_0,\ldots,L_k\) be the numbers of unvaccinated vertices in successive gaps (including endpoint gaps, which may be empty). Then \(\sum_iL_i=N\) and every nonnegative integral length profile occurs for some vaccine placement.

**Exact threshold-optimal layouts.** If \(N\le b(t-1)\), the minimum of \(\Pr(X\ge t)\) is zero, and precisely those placements with every \(L_i\le t-1\) attain it. If \(N>b(t-1)\), the minimum is positive and its entire minimizing set consists of permutations of
\[
\big(N-(b-1)(t-1),\,t-1,\ldots,t-1\big).
\]
The minimum threshold-exceedance probability is
\[
\frac{p^{t-1}}N\left[\big(t-(t-1)p\big)\big(N-(b-1)(t-1)\big)-t(t-1)(1-p)\right].
\]
Every characterization is strict off the stated minimizing set, for every \(0<p<1\).

**Mean-optimal layouts and sharp incompatibility.** The placements minimizing \(\mathbb E[X]\) are exactly the profiles in which all gap lengths differ by at most one: every length equals \(\lfloor N/b\rfloor\) or \(\lceil N/b\rceil\). These mean minimizers are independent of \(p\). At least one placement minimizes both objectives exactly when \(N\le b(t-1)+1\); for \(N\ge b(t-1)+2\) their minimizing sets are disjoint. Thus the two optimization criteria diverge at a sharp, budget-dependent population threshold.

## Assumptions and scope

The graph is a labeled finite path with \(n\) vertices. Vaccine efficacy is perfect; vaccinated vertices neither seed nor transmit infection. Exactly \(k\) vertices are vaccinated before a single uniformly selected susceptible seed. Conditional on the seed, edge transmissions are independent Bernoulli variables with common parameter \(p\). The outcome coincides with the bond-percolation cluster of that seed. The result concerns fixed \(n,k,t,p\), not stochastic changes in the vaccine set. Thresholds satisfy \(t\ge3\) and vaccine budgets satisfy \(k\ge2\). These bounds deliberately focus on multi-vaccine higher-threshold risk, not previously analyzed one-vaccine first-transmission problems.

## Proof

**1. Gap decomposition and a tail identity.** Vaccinated vertices disconnect the path into \(b\) paths, with \(L_i\ge0\) and sum \(N\). Each unvaccinated seed is equally likely, so \(N\Pr(X\ge t)=\sum_iG_t(L_i)\), where \(G_t(L)\) is the sum over the \(L\) possible seeds of the probability that its open-edge component has at least \(t\) vertices. Evidently \(G_t(L)=0\) for \(L<t\). For \(L\ge t\), maximal runs of \(\ell\) vertices connected by open edges yield the exact finite sum
\[
G_t(L)=L p^{L-1}+2(1-p)\sum_{\ell=t}^{L-1}\ell p^{\ell-1} +(1-p)^2\sum_{\ell=t}^{L-2}(L-\ell-1)\ell p^{\ell-1}.
\]
The terms respectively enumerate the all-open path, runs touching exactly one endpoint, and runs touching neither endpoint. Empty sums are zero. Finite geometric-series evaluation gives
\[
G_t(L)=p^{t-1}\left[\big(t-(t-1)p\big)L-t(t-1)(1-p)\right]\quad(L\ge t).
\]
For clarity, set \(a=p^{t-1}(t-(t-1)p)>0\) and \(c=t(t-1)(1-p)p^{t-1}>0\). Then \(G_t(L)=aL-c\) for \(L\ge t\), and
\[
c-a(t-1)=-(t-1)p^t<0.\]

**2. Full threshold-risk minimizer classification.** If \(N\le b(t-1)\), a profile with all gaps at most \(t-1\) exists. Its risk is zero. Conversely, any gap of length at least \(t\) contributes \(G_t(L)>0\), so these and only these are minima.

Suppose \(N>b(t-1)\). Every feasible profile has an active gap of length at least \(t\). If two lengths \(u,v\ge t\) are active, replace them with \(u+v-(t-1)\) and \(t-1\). Their sum is unchanged, the first remains active, and the tail sum changes by \(c-a(t-1)=-(t-1)p^t<0\). Therefore a minimizer has exactly one active gap. If any other gap has length below \(t-1\), move one vertex from the active gap to it. Since \(N>b(t-1)\), the active gap remains at least \(t\), while the target gap remains below \(t\). The tail sum decreases by \(a>0\), a contradiction. Thus every inactive gap has length exactly \(t-1\), proving the stated unique multiset. Substitution yields the minimum probability. The argument is finite, terminating, and all improving moves are strict.

**3. Mean-risk objective and its minimizers.** On an unvaccinated interval of length \(L\), the sum of expected outbreak sizes over all seed locations is the sum of connectivity probabilities over ordered pairs of vertices:
\[
H(L)=\sum_{u=1}^L\sum_{v=1}^L p^{|u-v|}=L+2\sum_{d=1}^{L-1}(L-d)p^d,\qquad H(0)=0.
\]
Consequently \(N\mathbb E[X]=\sum_iH(L_i)\). Its consecutive first differences obey \(H(L+1)-H(L)=1+2\sum_{d=1}^L p^d\), and hence its second differences equal \(2p^{L+1}>0\) for every \(L\ge0\). When \(u\ge v+2\), transferring one vertex from the longer interval to the shorter decreases \(H(u)+H(v)\) strictly. Iterating gives precisely the balanced profiles, while reversing any transfer shows no unbalanced profile is minimizing.

**4. Compatibility boundary.** If \(N\le b(t-1)\), each balanced profile has all gap lengths at most \(t-1\) and hence optimizes both objectives. If \(N=b(t-1)+1\), the risk-optimal multiset \((t,t-1,\ldots,t-1)\) is balanced, so compatibility remains. If \(N\ge b(t-1)+2\), the risk-optimal multiset has one length at least \(t+1\) and \(b-1\) lengths \(t-1\), and so is not balanced. Since the complete minimizing sets are as proved above, the two sets are disjoint. This proves the exact threshold.

## Verification

An independent exact-rational finite verifier, `verify.py`, enumerates edge states for path lengths up to seven and compares both gap formulas with direct weighted seed counts. It also enumerates all nonnegative gap compositions for \(k\in\{2,3,4\}\), \(3\le N\le9\), \(3\le t\le N\), and \(p\in\{1/3,2/3\}\), comparing exhaustive optimum profiles against both classifications. The reproducible certificate `verification_certificate.json` records 168 direct edge-enumeration cases and 31,584 optimized profile evaluations in 168 parameter configurations.

For \(k=2\), \(N=10\), \(t=3\), and \(p=1/2\), the balanced profile \((4,3,3)\) gives \(\mathbb E[X]=77/40\) and \(\Pr(X\ge3)=11/40\); the threshold-optimal profile \((6,2,2)\) gives \(\mathbb E[X]=321/160\) and \(\Pr(X\ge3)=9/40\). The exact inequalities exhibit a nontrivial strict tradeoff. The finite checks do not replace the symbolic proof.

## Relationship to prior work

Altarelli et al. (arXiv:1309.2805, first posted September 11, 2013) study network immunization using approximate message-passing objectives. Their Section II describes the bond-percolation representation and Section III its optimization setting, but the inspected paper does not give the exact, all-budget, all-threshold path classification here. Aspnes, Chang, and Yampolskiy (technical report July 2004) study virus inoculation and the sum-of-squares partition objective with deterministic reachability after immunization; the present result instead treats incomplete independent transmission and the exact probability of exceeding an arbitrary outbreak size. Yuan et al. (arXiv:1407.3215) motivate outbreak-size risk thresholds for stochastic vaccination, but study two noninteracting populations rather than path layouts. These comparisons establish different explicit objectives and domains, not universal priority; an unrecognized equivalent path-percolation result remains possible.

## Limitations

No statement is made for multiple simultaneous infection seeds, correlated edge transmissions, heterogeneous susceptibility, imperfect vaccines, non-path graphs, weighted vaccination costs, or actual epidemic outcomes. At \(p=0\) or \(p=1\), strict uniqueness statements may fail; the theorem requires \(0<p<1\). Threshold-specific layouts cannot be claimed to minimize all upper tails simultaneously. The count of all minimizing vaccine **sets** depends on permutations of repeated and zero gap lengths, and is not separately asserted. General publication novelty remains subject to independent literature verification; no independent mathematical audit has been performed.

## References

1. F. Altarelli, A. Braunstein, L. Dall'Asta, J. R. Wakeling, R. Zecchina, *Containing epidemic outbreaks by message-passing techniques*, arXiv:1309.2805v1 (September 11, 2013), https://arxiv.org/pdf/1309.2805 .
2. J. Aspnes, K. Chang, A. Yampolskiy, *Inoculation strategies for victims of viruses and the sum-of-squares partition problem*, Yale technical report YALEU/DCS/TR-1295 (July 2004), https://www.cs.yale.edu/publications/techreports/tr1295.pdf .
3. Yuan et al., *Optimal vaccination in a stochastic epidemic model of two non-interacting populations*, arXiv:1407.3215 (July 10, 2014), https://arxiv.org/abs/1407.3215 .
