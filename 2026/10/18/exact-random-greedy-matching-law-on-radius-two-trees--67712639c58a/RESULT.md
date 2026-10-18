# Exact random-greedy matching law on radius-two trees

## Finding
Let \(T\) be a finite tree with at least one edge, rooted at a vertex \(c\) from which every vertex is at distance at most two. Let the distinct neighbors of \(c\) be \(u_1,\ldots,u_d\), where \(d\ge1\). For each \(i\), let \(a_i\ge0\) be the number of leaf neighbors of \(u_i\) other than \(c\). Write \(e_i=cu_i\) and \(f_{i,h}=u_iw_{i,h}\) for \(1\le h\le a_i\). In a uniformly random permutation of the edges, accept an edge if neither endpoint is already covered by an accepted edge. The result is a maximal matching \(\mathbf M\).

For each \(i\), define
\[
Q_i(y)=\frac{a_i+y^{a_i+1}}{a_i+1},\qquad
p_\varnothing=\prod_{i=1}^d\frac{a_i}{a_i+1},\qquad
p_i=\int_0^1 y^{a_i}\prod_{j\ne i}Q_j(y)\,dy.
\]
These numbers are nonnegative exact rationals summing to one. The complete labeled output law is:

1. If every \(a_i\ge1\), then for every choice \(1\le h_i\le a_i\), the maximal matching \(M_\varnothing=\{f_{i,h_i}:1\le i\le d\}\) occurs with probability \(p_\varnothing/\prod_i a_i\). There is no output without a central edge if any \(a_i=0\).
2. For each \(k\in\{1,\ldots,d\}\), every choice of one \(f_{j,h_j}\) from each branch \(j\ne k\) with \(a_j\ge1\) gives the maximal matching \(M_k=\{e_k\}\cup\{f_{j,h_j}:j\ne k,\ a_j\ge1\}\), with probability
\[
\Pr(\mathbf M=M_k)=\frac{p_k}{\prod_{j\ne k,\ a_j\ge1}a_j}.
\]
Empty products equal one. These are all possible maximal matchings, and each displayed outcome has positive probability (the no-central outcome is included only when it exists). Because the integrands are polynomials of explicitly bounded degree, the output law is evaluable using exact rational polynomial multiplication and integration, without enumerating edge permutations.

A structural consequence of the law is the following nonuniformity bound. If \(d\ge2\) and all \(a_i\ge1\), then the greedy output is never uniform over maximal matchings. More precisely, writing \(\mathsf G\) for its law and \(\mathsf U\) for the uniform law, one has
\[
d_{\mathrm{TV}}(\mathsf G,\mathsf U)\ge
\frac1{1+\sum_{i=1}^d1/a_i}
-\prod_{i=1}^d\frac{a_i}{a_i+1}>0.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The input is a tree admitting a root at distance at most two from every vertex. Such trees have radius at most two; the chosen root and ordered branches are part of the representation, not an extra stochastic parameter. Every edge receives one independent atomless uniform arrival time, equivalently a uniformly random permutation. The matching is inclusion-maximal, not necessarily of maximum cardinality. The formulas give probabilities of individual **labeled** maximal matchings, not merely sizes or isomorphism classes. A branch with no outer leaf has \(a_i=0\) and is included without exceptional conventions beyond the empty-product rule.

Ordinary stars are a boundary case: their greedy outcome is a uniformly random single edge. The explicit formula specializes to double stars (the diameter-three case), but that part also follows from earlier general cograph laws and is not asserted as a new contribution. No theorem about arbitrary trees of greater radius, or the complete uniformity classification among all radius-two trees, is asserted.

## Proof
**1. List every possible maximal matching.** At most one edge \(e_i\) can be accepted, since all are incident with \(c\). If \(e_k\) is accepted, every other central edge is blocked by \(c\), as are all leaf edges of branch \(k\). In each other branch with \(a_j\ge1\), the earliest leaf edge is accepted (they all meet at \(u_j\)) and prevents every later leaf edge there; branches with \(a_j=0\) contribute nothing. Hence the output is precisely one of the sets \(M_k\) described above. If no central edge is accepted, each branch with \(a_j\ge1\) contributes its earliest leaf edge. This gives \(M_\varnothing\), and it is a maximal matching if and only if every branch has at least one leaf edge: a branch with \(a_j=0\) would leave the edge \(e_j\) available, contrary to maximality. Conversely, each displayed set is a maximal matching and can be produced by ordering its edges first, so no possible output was omitted.

**2. Characterize the accepted central edge.** Replace the uniformly random edge order with independent arrival times, all uniform on \([0,1]\). Call \(e_j\) *eligible* when its arrival precedes every leaf edge in its own branch. If no central edge is eligible, the greedy algorithm accepts no central edge. If at least one is eligible, the central edge with the earliest arrival among eligible central edges is accepted: at its arrival no earlier leaf edge from the same branch was accepted, and no earlier central edge was accepted, because an earlier accepted central edge would itself have been eligible. Once this central edge is accepted, all other central edges are blocked. Thus the accepted central edge is exactly the earliest eligible one, if any.

Each branch has \(a_j+1\) independent arrival times. Its central edge is eligible with probability \(1/(a_j+1)\), independently across branches. Accordingly, the probability of no eligible central edge is
\[
p_\varnothing=\prod_j\left(1-\frac1{a_j+1}\right)
=\prod_j\frac{a_j}{a_j+1}.
\]
This remains correct when a branch has no leaf edges: its central edge is always eligible, forcing \(p_\varnothing=0\).

**3. Evaluate the probability of each central winner.** Fix a branch \(k\). Condition on the central edge \(e_k\) arriving at time \(t\in[0,1]\), whose density is one. It is eligible exactly if its \(a_k\) leaf edges all arrive after \(t\), of probability \((1-t)^{a_k}\). For any other branch \(j\ne k\), the event that its eligible central edge arrives before \(t\) has probability
\[
\int_0^t(1-s)^{a_j}\,ds
=\frac{1-(1-t)^{a_j+1}}{a_j+1}.
\]
Hence the probability that this does **not** happen equals
\[
\frac{a_j+(1-t)^{a_j+1}}{a_j+1}=Q_j(1-t).
\]
The conditions lie in disjoint branches and are independent. Integrating over the arrival time of \(e_k\) and substituting \(y=1-t\) gives exactly
\[
\Pr(e_k\text{ is the accepted central edge})
=\int_0^1y^{a_k}\prod_{j\ne k}Q_j(y)\,dy=p_k.
\]
The events of no eligible central edge and of each possible earliest eligible central edge form a partition. This also proves \(p_\varnothing+\sum_kp_k=1\) without invoking computation.

**4. Restore labels of the pendant edges.** Conditional on which central edge (if any) is accepted, the selected leaf edge in every contributing branch is the minimum-arrival leaf edge of that branch. Permuting the leaf-edge labels within any one branch leaves the central-winner event unchanged. Such relabelings act transitively on the product of leaf-edge selections, so the conditional distribution over these label choices is uniform. The count of choices is \(\prod_i a_i\) for \(M_\varnothing\), and \(\prod_{j\ne k,\ a_j\ge1}a_j\) for \(M_k\). Division by these factors proves the exact probability of every output. Every \(p_k\) is positive because its integrand is positive for \(0<y<1\); if all \(a_i\ge1\), then \(p_\varnothing>0\). An explicit implementation multiplies the degree-at-most-\(a_j+1\) polynomials \(Q_j\) and integrates termwise; hence all arithmetic is exact and finite.

**5. The nonuniformity obstruction.** Suppose \(d\ge2\) and every \(a_i\ge1\). The no-central family has \(A=\prod_i a_i\) labeled members. For fixed \(k\), the \(k\)-central family has \(A/a_k\) members. There are therefore \(A(1+\sum_k1/a_k)\) maximal matchings, and the *uniform* probability of the no-central family is
\[
\mathsf U(\text{no central edge})=\frac1{1+\sum_k1/a_k}.
\]
The greedy probability is \(\prod_k(1+1/a_k)^{-1}\). Since the product of at least two terms \(1+1/a_k\) has strictly positive higher-degree cross terms,
\[
\prod_k(1+1/a_k)>1+\sum_k1/a_k,
\]
so the greedy probability is strictly smaller. Total-variation distance is the supremum of event-probability differences, yielding the stated quantitative bound.

## Verification
The standalone Python 3 verifier `artifacts/verify.py` uses only the standard library and exact fractions. It independently computes the greedy matching law by conditioning on the *first available edge* and recursing on the remaining nonincident edges. This recurrence does not use the integral formula. It checked every branch-length profile \((a_1,\ldots,a_d)\) with \(1\le d\le5\), \(0\le a_i\le3\), and at most ten edges: 452 profiles and 5,163 labeled maximal-matching outcomes. A second check enumerated all edge permutations in smaller profiles: 189,821 permutations. It also checked 21,840 strict no-central obstructions and 289 double stars with positive parameters at most seventeen, including the exact total-variation formula. All checks passed with output recorded in `artifacts/verify_output.txt`.

To reproduce from the package root run `python3 artifacts/verify.py`. The expected result is the single line in `artifacts/verify_output.txt`. The finite checks corroborate, but do not prove, the all-parameter statement: the proof is the arrival-time partition and exact integration above.

## Relationship to prior work
Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders* (arXiv:2610.02276v1, first public October 1, 2026), studies **vertex**-order random-greedy maximal independent sets **of trees** and proves that the terminal law is uniform only on a one-vertex or one-edge tree. The complete public manuscript was inspected, including its theorem statements, related-work section, proofs, and limitations. The present theorem instead concerns **edge**-order random-greedy maximal **matchings** of trees, equivalently vertex-order maximal-independent-set sampling on their **line graphs**. Such a line graph is generally not a tree. The exact labeled matching law and its uniform double-star exception are not consequences of the cited tree-MIS theorem; the latter is acknowledged as the natural motivating contrast rather than claimed as new.

Krivelevich, Mészáros, Michaeli, and Shikhelman, *Greedy maximal independent sets via local limits* (Random Structures & Algorithms 64 (2024), DOI:10.1002/rsa.21200), treat the general random-priority process, principally through sizes and local-limit observables rather than a closed law for every labeled maximal matching of radius-two trees. The same random-edge-order maximal matching process is explicitly defined in Mahabadi, Roghani, Tarnawski, and Vakilian, *Sublinear Metric Steiner Tree via Improved Bounds for Set Cover* (ITCS 2025, DOI:10.4230/LIPIcs.ITCS.2025.74), which studies size estimation and query complexity rather than the terminal matching distribution. Kryven, Versendaal, and de Vries (arXiv:2608.07239v1) study uniformity of general iterative maximal-independent-set constructions, including sufficient conditions, but the consulted account does not provide these branch-integral probabilities.

Other inspected mathematical results give exact random-greedy maximal-independent-set laws on **cographs**, threshold graphs and bipartite chain graphs, and separately bounds on the *unweighted average size* of maximal matchings in cyclic graphs. The cograph result **does** imply the diameter-three double-star specialization (its line graph is a cograph), so that boundary specialization is prior-covered and is not claimed as an original corollary. These graph classes do not contain arbitrary line graphs of radius-two trees: for instance, the five-vertex path has radius two but its line graph is an induced four-vertex path, which is not a cograph or a bipartite chain graph; an unweighted arithmetic average over maximal matchings is not the random-greedy law. A general first-edge recurrence can in principle compute probabilities for a fixed finite graph, but does not subsume the closed family-wide product-integral formula or the sharp double-star uniformity condition. The original-process representation, line-graph correspondence, first-edge recursion, and exchangeability of symmetric leaf labels are standard background, not novelty claims.

## Limitations
The result does not classify uniform random-greedy matching sampling on arbitrary finite trees, nor even every mixture of zero and positive branch sizes within the radius-two family; it does completely determine their probabilities and the stated substantial subcases. It provides no asymptotic extremality claim. The literature comparison included primary full text and targeted searches under the random-greedy maximal matching, line-graph, dimer parking, and random sequential adsorption terminology, but cannot rule out equivalent older or unindexed work. In particular, there may be an earlier expression of the same law in dimer random-sequential-adsorption language. Mathematical proof and reproducible exact checks support correctness; originality remains subject to scholarly verification and no independent audit has been performed.

## References
1. J. Fairfax-Ball, “Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders,” arXiv:2610.02276v1, first submitted October 1, 2026, https://arxiv.org/abs/2610.02276.
2. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” Random Structures & Algorithms 64 (2024), 986–1015, DOI:10.1002/rsa.21200.
3. S. Mahabadi, M. Roghani, J. Tarnawski, and A. Vakilian, “Sublinear Metric Steiner Tree via Improved Bounds for Set Cover,” ITCS 2025, DOI:10.4230/LIPIcs.ITCS.2025.74.
4. I. Kryven, R. Versendaal, and M. de Vries, “Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints,” arXiv:2608.07239v1, first submitted August 7, 2026.
5. P. Diaconis, S. Holmes, and S. Janson, “Threshold graph limits and random threshold graphs,” arXiv:0908.2448v1 (2009), background on threshold graph constructions.
6. A. Boyacı, T. Ekim, and M. Shalom, “The Maximum Cut Problem in Co-bipartite Chain Graphs,” arXiv:1504.03666 (2015), background on chain-graph structure.
