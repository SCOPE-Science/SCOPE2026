# Joint endpoint degrees decrease with distance in a uniform labeled tree

## Finding

Let \(T\) be uniform on the labeled trees on \([n]\), with \(n\ge3\), and fix distinct labels \(u,v\). For \(1\le k\le n-1\), let \(D^{(k)}\) have the law of \((\deg_T(u),\deg_T(v))\) conditional on \(d_T(u,v)=k\). There is a coupling of all these laws on one probability space such that
\[
D^{(1)}\ge D^{(2)}\ge\cdots\ge D^{(n-1)}=(1,1)
\quad\text{coordinatewise almost surely}.
\]
Thus for every coordinatewise nondecreasing function \(g\), the conditional mean of \(g(\deg_T(u),\deg_T(v))\) is nonincreasing in distance. For example, this applies to the probability that both endpoints meet prescribed degree thresholds, or that either endpoint does. The mean of each endpoint degree separately is strictly decreasing. The main claim is the joint order: ordering both marginals alone does not establish it.

## Assumptions and scope

This is the uniform **labeled** tree measure, with fixed distinct labeled endpoints; it is not a statement about uniformly chosen unlabeled trees or arbitrary spanning-tree models. The coupling is of the pairs of endpoint degrees, not of full trees or of path-vertex vectors of changing length. The strict mean comparison is not a claim of strict inequality for every increasing test function.

## Proof

First fix the ordered interior labels on the \(u\)-to-\(v\) path and put \(q=k+1\), \(m=n-q\). Suppose \(q<n\). Contract the specified path to a vertex \(*\). Each resulting tree on \(m+1\) vertices can be lifted by choosing, independently for each edge incident to \(*\), which marked vertex receives the edge. Every such choice gives a tree containing the specified path, and these choices recover all completions bijectively. Assign weight \(z_i\) to an attachment to marked vertex \(i\), numbering the endpoints 1 and 2. With \(Z=\sum_{i=1}^q z_i\), the weighted count of lifts of a contracted tree is \(Z^{\deg(*)}\). The classical Cayley degree-generating polynomial \((\prod_i x_i)(\sum_i x_i)^{N-2}\) for \(N=m+1\), evaluated at \(x_*=Z\) and all other \(x_i=1\), gives \(Z(m+Z)^{m-1}\). Normalizing at \(Z=q\) gives the conditional attachment generating function
\[
\frac{Z}{q}\left(\frac{m+Z}{n}\right)^{m-1}.
\]
This calculation depends only on \(q\), not the interior labels. Each tree has a unique path between the marked endpoints, so averaging over the disjoint label choices preserves the formula. Both endpoint degrees are one plus their attachment counts. If \(q=n\), conditioning forces a spanning path with endpoints \(u,v\) and no outside attachments.

The two-variable specialization \(z_1=s,z_2=t,z_i=1\) for \(i\ge3\) factors into the generating function for \(n-q-1\) independent trials (each contributes to endpoint 1 or 2 with probability \(1/n\) apiece and contributes to neither otherwise), times that for one independent choice \(J_q\) uniform on \(\{1,\ldots,q\}\). That choice contributes one to an endpoint only if \(J_q=1\) or \(2\).

Use prefixes of one common sequence of independent trials for all \(q\le n-1\). Independently, draw a uniformly random ordering of \(\{1,\ldots,n-1\}\) and let \(J_q\) be the first member of \(\{1,\ldots,q\}\) in that ordering. This is uniform on the prescribed set. Once an endpoint ceases to be first it cannot become first again as the set grows, so both endpoint contributions from the uniform choice are nonincreasing pathwise. Each trial contributes a nonnegative pair, and the prefix shortens as \(q\) increases. The two attachment counts therefore decrease simultaneously, with the final pair at \(q=n\) set to zero. Adding one to each count proves the stated coupling.

For \(q<n\), each endpoint attachment count has mean \((n-q-1)/n+1/q\). For \(q=n\) it is zero. These means decrease strictly at every step, as asserted.

## Verification

The unchanged `geodesic_degree_checker.py` from the source package compares the underlying path attachment distributions with exact Prüfer-word enumeration through \(n=8\); it is a finite check of the distribution used in the coupling, not a proof of the stochastic order. The all-size order follows from the common-prefix and nested-ordering construction above.

## Relationship to prior work

The attachment generating function is classical weighted Cayley enumeration applied to the contracted path. The same derivation applies when the fixed marked path is replaced by any fixed connected marked subtree. The generating function and its moments are used here as background, not claimed as novel. The earlier one-endpoint Cayley result gives the binomial-plus-Bernoulli marginal and its decreasing stochastic order. The simultaneous coupling controls increasing two-endpoint events, which cannot in general be compared from one-endpoint regressions alone. The earlier conditional leaf-count result studies a different statistic; the bivariate degree formula for complete bipartite spanning trees concerns a different tree law and does not assert the joint ordering here. No absolute publication-priority claim is made.

## References

1. O. Bernardi and A. H. Morales, *Counting trees using symmetries*, equation (1), Cayley's degree-enumeration formula.
2. J. Pitman, *Coalescent Random Forests*, Berkeley Statistics Technical Report 457 (1996), §2.2, Lemma 3, https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf.
3. *Exact negative regression between endpoint degree and distance in a uniform Cayley tree*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae.
4. *Conditional joint leaf law along a marked path in a uniform Cayley tree*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-conditional-joint-leaf-law-along-a-marked-path-in-a-uniform-cayl--4740ad229d71.
5. *Two-endpoint degree dependence along paths in bipartite uniform spanning trees*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-two-endpoint-degree-dependence-along-conditioned-paths-in-bipart--67820a932340.
