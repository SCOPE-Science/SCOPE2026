# Eight habitats are sharp for dispersal-dependent optimal corridor reinforcement on trees

## Finding

**Theorem (sharp tree threshold and eight-habitat classification).** Let \(T\) be any finite unweighted tree of \(n\geq 2\) equal-quality habitat patches. Each existing corridor independently supports passage with probability \(p\in(0,1)\). One corridor can be made perfectly reliable, at the same cost regardless of the edge selected. Select the edge maximizing the expected size of the connected open-edge component of a uniformly sampled initial patch. Equivalently, maximize the standard pairwise probability-of-connectivity index, or its equivalent-connected-area transform, after one corridor upgrade.

For every tree with \(2\le n\le 7\), there is an edge optimal simultaneously for **every** \(p\in(0,1)\). Of the 23 unlabelled trees with \(n=8\), exactly two have no such uniformly optimal edge. Each has exactly one interior change in the set of optimal edges:

1. On the tree with edge set \(\{01,05,12,23,24,56,67\}\), upgrade edge \(12\) for \(0<p<(\sqrt 5-1)/2\) and edge \(01\) for \((\sqrt 5-1)/2<p<1\). Both are optimal at equality. All other edges are strictly suboptimal for \(0<p<1\).
2. On the tree with edge set \(\{01,05,12,23,24,56,57\}\), upgrade either \(12\) or \(05\) for \(0<p<1/2\), and edge \(01\) for \(1/2<p<1\). All three are optimal at \(p=1/2\). Every other edge is strictly suboptimal for \(0<p<1\).

Here two-digit strings in the edge-set notation denote the endpoints of an undirected edge, with vertices \(0,1,\ldots,7\); they are **edge labels**, not decimal numbers. Thus eight patches are the smallest tree landscape on which relative dispersal ability can alter the best single-corridor reinforcement.

## Assumptions and scope

The graph is a finite simple undirected tree, not a general graph with cycles. All vertices have unit habitat quality, and edge reliabilities are equal except for one upgraded edge. Passages along distinct edges are independent. The source patch is uniform among the \(n\) patches, and the restoration budget permits precisely one existing edge to change from probability \(p\) to \(1\), with equal costs. The result evaluates pairwise connection probabilities and expected connected-component size, not realized occupancy or long-term population persistence.

Define \(d_T(a,b)\) as graph distance, with \(d_T(a,a)=0\). Before upgrading, expected reachability from a uniformly chosen source is
\[
R_T(p)=\frac1n\sum_{a,b\in V(T)}p^{d_T(a,b)}.
\]
If edge \(e=uv\) is upgraded, let \(R_{T,e}(p)\) denote the resulting expectation. The same comparisons optimize the probability-of-connectivity numerator \(\sum_{a,b}\Pi_{ab}\), since on a tree \(\Pi_{ab}\) equals the product of its unique-path edge reliabilities. Equal patch qualities make the normalizing denominator independent of the candidate edge; taking the equivalent-connected-area square root also preserves the ranking.

## Proof

**Step 1: Exact edge improvement polynomial.** Removing \(e=uv\) leaves components \(A\ni u\) and \(B\ni v\). Let \(d_A\) and \(d_B\) be their respective tree distances and define
\[
F_e(p)=\sum_{a\in A}\sum_{b\in B}p^{d_A(a,u)+d_B(v,b)}.
\]
A pair of patches separated by \(e\) has original connection probability \(p^{d_A(a,u)+1+d_B(v,b)}\); improving \(e\) changes this to \(p^{d_A(a,u)+d_B(v,b)}\). No other pair changes. Counting both orientations gives the **exact identity**
\[
R_{T,e}(p)-R_T(p)=\frac{2(1-p)}{n}F_e(p).
\]
Since \(2(1-p)/n>0\), the optimal edge maximizes \(F_e(p)\). Its coefficient of \(p^j\) is the nonnegative integer number of unordered vertex pairs separated by \(e\) whose connecting path has length \(j+1\). In particular, \(F_e(0)=1\) and \(F_e(1)=|A||B|\).

**Step 2: Finite exhaustive classification with an exact dominance certificate.** The companion `verify_corridors.py` enumerates every labelled tree on \(2\le n\le8\) using the Prüfer-sequence bijection, canonicalizes each unlabelled tree by its center-rooted sorted subtree strings, and constructs \(F_e\) by exact breadth-first distances on the two sides of each edge. The numbers of distinct trees are respectively \(1,1,2,3,6,11,23\), covering all classes. If the coefficient vector of one edge polynomial is componentwise at least another's, the former is never worse on \(0<p<1\). Retaining only coefficientwise maximal **distinct** vectors is therefore logically sufficient: a discarded edge is strictly dominated by one that remains, or equals it identically.

The verified classification produces only five tree shapes with more than one such maximal vector. Among the 11 seven-vertex trees, exactly one has two vectors, with difference (up to sign) \(p(1-p)\): one edge therefore wins throughout the open interval. The other ten have a unique maximal vector. Among the 23 eight-vertex trees, 19 have a unique maximal vector. The four remaining trees have exactly two distinct maximal polynomials each; their differences, up to sign, are precisely
\[
p(2-p),\qquad p(1-p^2),\qquad p(2p-1),\qquad p(p^2+p-1).
\]
The first two have constant strict sign on \((0,1)\); the last two change sign exactly once, at \(1/2\) and \((\sqrt5-1)/2\), respectively. This proves the universal lower bound and the complete eight-vertex classification. The source gives executable exact integer comparisons; its assertions verify these counts and these polynomial forms, not merely sampled parameter values. The underlying Prüfer bijection and canonical rooted-tree recursion establish completeness of the finite search.

**Step 3: Explicit eight-vertex witnesses.** In the first displayed tree, two candidate edge polynomials are
\[
\begin{aligned}
F_{01}(p)&=1+2p+4p^2+4p^3+3p^4+2p^5,\\
F_{12}(p)&=1+3p+3p^2+3p^3+3p^4+2p^5.
\end{aligned}
\]
Their difference is \(F_{01}-F_{12}=p(p^2+p-1)\). All other edge polynomials are coefficientwise dominated by one of these two, yielding the stated unique crossover.

In the second tree the only two distinct coefficientwise-maximal polynomials are
\[
\begin{aligned}
F_{01}(p)&=1+2p+5p^2+4p^3+4p^4,\\
F_{12}(p)=F_{05}(p)&=1+3p+3p^2+4p^3+4p^4.
\end{aligned}
\]
Here \(F_{01}-F_{12}=p(2p-1)\), yielding the stated half-probability crossover and ties. Other edges are strictly dominated for interior \(p\).

## Verification

Run `python3 verify_corridors.py` with Python 3 (standard library only). It independently enumerates all Prüfer-labelled trees, canonicalizes them, builds complete exact coefficient vectors, discards only coefficientwise-dominated choices, and checks the remaining exact differences against the four specified patterns. It also enumerates all subsets of open edges for the two explicit witness graphs at \(p=1/4\) and \(p=3/4\), independently checking ten exact rational instances of the upgrade identity. All tests passed on the packaged source. A numerical sample alone is not used as a proof of a continuum claim.

## Relationship to prior work

Saura and Rubio (2010) develop the ecological probability-of-connectivity framework and importance of individual links, including sensitivity to dispersal traits. On uniform-reliability trees their link-removal importance is proportional to \(pF_e(p)\), whereas single-link reinforcement to certainty is proportional to \((1-p)F_e(p)\); their **rankings coincide**. That equivalence is acknowledged, not claimed as new. Williams and Snyder (2005) optimize habitat corridor restoration to obtain landscape-spanning routes, using a different path-establishment objective. Hamonic et al. (2022, journal article published 2023) formulate the more general budget-constrained equivalent-connected-area optimization problem; its single equal-cost upgrade instance encompasses the present optimization objective for each fixed parameter value. Their contribution is a general solver and preprocessing, rather than a smallest-tree all-parameter classification. The present claim is specifically the complete sharp eight-vertex obstruction, the two exceptional shapes, and their exact crossing thresholds—not the established connectivity index, probability formula, or ability to numerically optimize a fixed network.

## Limitations

The classification is exhaustive only through eight-vertex **trees**. It makes no claim for arbitrary graphs, weighted habitats, unequal corridor probabilities, uncertain costs, interactions between multiple improvements, density-dependent dispersal, or real population dynamics. On more than eight vertices further switching patterns may occur. Prior-coverage risk remains that a specialized edge-Wiener/Hosoya-polynomial ranking theorem or a landscape-connectivity table implies this exact cutoff; absence from inspected sources is not an independence proof. The result has undergone self-review only, not independent auditing.

## References

1. S. Saura and L. Rubio, "A common currency for the different ways in which patches and links can contribute to habitat availability and connectivity in the landscape," *Ecography* 33 (2010), 523–537, DOI: 10.1111/j.1600-0587.2009.05760.x. First publicly posted by publisher 2010-07-28. Primary PDF: https://nsojournals.onlinelibrary.wiley.com/doi/pdf/10.1111/j.1600-0587.2009.05760.x
2. F. Hamonic, C. Albert, B. Couëtoux and Y. Vaxès, "Optimizing the ecological connectivity of landscapes," *Networks* 81 (2023), 278–293, DOI: 10.1002/net.22131. Full text first published 2022-11-18: https://onlinelibrary.wiley.com/doi/full/10.1002/net.22131
3. J. C. Williams and S. A. Snyder, "Restoring habitat corridors in fragmented landscapes using optimization and percolation models," *Environmental Modeling and Assessment* 10 (2005), 239–250, DOI: 10.1007/s10666-005-9003-9. Authorized full text: https://research.fs.usda.gov/download/treesearch/15032.pdf
4. Y. Youssef, Y. Khorramzadeh and S. Eubank, "Network reliability: The effect of local network structure on diffusive processes," *Physical Review E* 88 (2013), 052810, arXiv:1308.4577 (2013-08-21). Motivating background on reliability and spread, not the claimed classification.
