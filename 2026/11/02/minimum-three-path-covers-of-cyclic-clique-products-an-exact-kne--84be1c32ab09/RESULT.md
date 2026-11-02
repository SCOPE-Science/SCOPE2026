# Minimum three-path covers of cyclic clique products: an exact Kneser-spectrum enumerator

## Finding

For integers \(m\ge3\) and \(n\ge6\), let \(G_{m,n}=C_m\square K_n\) be the Cartesian product of the **labelled** cycle on positions \(0,1,\ldots,m-1\) and the complete graph on labels \([n]=\{1,\ldots,n\}\). A *three-path vertex cover* is a set of vertices meeting every (not necessarily induced) path on three distinct vertices. Every minimum cover has \(m(n-2)\) vertices. More precisely, the complement of each minimum cover contains **exactly two vertices in every clique fiber**, and, writing those two labels as \(A_i\in\binom{[n]}2\), adjacent fibers satisfy \(A_i\cap A_{i+1}=\varnothing\), with indices modulo \(m\). Every such cyclic sequence gives a minimum cover, exactly once.

Thus the exact number of distinct minimum three-path vertex covers on the labelled graph is
\[
\boxed{\mathcal N_{m,n}=\binom{n-2}{2}^{m}+(n-1)(3-n)^m+\frac{n(n-3)}2.}
\]
The cycle positions and clique labels remain fixed; the count is **not** taken modulo automorphisms. In particular, \(\mathcal N_{3,6}=90\), \(\mathcal N_{4,6}=1710\), \(\mathcal N_{3,7}=630\), and \(\mathcal N_{4,7}=11550\).

The exact multiplicity formula, not merely the optimal cover cardinality, is the main assertion.

## Assumptions and scope

All graphs are finite, simple and undirected; \(C_3\) is a triangle. The product has vertex set \(\{(i,j): i\in\mathbb Z/m\mathbb Z,\ j\in[n]\}\). Two vertices are adjacent when they lie in the same clique fiber with different labels, or have the same label in consecutive cycle fibers. A *dissociation set* is a vertex set whose induced graph has maximum degree at most one. The complement of a three-path vertex cover is exactly a dissociation set: a graph contains a three-vertex path if and only if one of its vertices has at least two distinct neighbors.

The lower bound \(n\ge6\) ensures that the three color classes of a proper three-coloring of any cycle can be assigned pairwise disjoint two-element label sets. It cannot be removed uniformly: for instance, with \(n=5,m=3\), the maximum dissociation size is five rather than six, as independently exhaustively checked. No formula for smaller clique sizes is claimed.

## Proof

**1. Fiber capacity and existence.** Any dissociation set \(S\subseteq V(G_{m,n})\) contains at most two vertices in any fiber \(\{i\}\times[n]\), since three vertices of a clique contain a vertex of induced degree two. Consequently \(|S|\le2m\). A proper three-coloring of \(C_m\) exists for every \(m\ge3\); choose the disjoint pairs \(\{1,2\}\), \(\{3,4\}\), \(\{5,6\}\) for its three colors. Taking these two vertices in each corresponding fiber induces exactly one edge per fiber and no inter-fiber edge. Hence \(S\) is dissociation, \(|S|=2m\), and the optimum cover cardinality is \(mn-2m=m(n-2)\).

**2. Exhaustive classification at equality.** Every maximum dissociation set must saturate each of the \(m\) clique-fiber capacities, so it specifies a unique pair \(A_i\) at every cycle position. The two selected vertices in one fiber are adjacent, already using their entire permitted induced degree one. A selected inter-fiber edge therefore violates the degree restriction. Such an edge joins equal labels in adjacent fibers, and is absent exactly when \(A_i\cap A_{i+1}=\varnothing\) for all \(i\). Conversely, when all these intersections are empty the induced subgraph is precisely the disjoint union of \(m\) single edges, so every admissible sequence is a maximum dissociation set. Taking complements proves the advertised one-to-one correspondence with minimum three-path covers.

This argument has a general form: for any finite graph \(H\) and \(n\ge\max\{4,2\chi(H)\}\), maximum dissociation sets in \(H\square K_n\) have cardinality \(2|V(H)|\) and are in bijection with graph homomorphisms \(H\to\operatorname{KG}(n,2)\). Indeed, a proper \(\chi(H)\)-coloring provides pairwise disjoint label pairs for color classes, and the preceding fiber-equality argument applies verbatim. The cyclic case below admits an explicit closed count.

**3. Translation to Kneser closed walks.** Let \(\operatorname{KG}(n,2)\) have the two-element subsets of \([n]\) as its vertices, two of them being adjacent if disjoint. Denote its adjacency matrix by \(A\). The classified cyclic pair sequences are precisely graph homomorphisms \(C_m\to\operatorname{KG}(n,2)\), equivalently closed walks of length \(m\) with a labelled starting vertex. Therefore \(\mathcal N_{m,n}=\operatorname{tr}(A^m)\).

**4. Complete derivation of the spectrum.** Let \(F\) be the \(n\times\binom n2\) unsigned vertex-to-edge incidence matrix of \(K_n\). Thus a column corresponding to a two-element set has ones at those two labels. The matrix \(F^{\mathsf T}F\) has entry two for equal pairs, one for intersecting distinct pairs, and zero for disjoint pairs. Writing \(J\) for the all-ones matrix on two-element subsets and \(I\) for the identity,
\[
 A=J+I-F^{\mathsf T}F.
\]
Further, \(FF^{\mathsf T}=(n-2)I_n+J_n\), since its diagonal entries are \(n-1\) and its off-diagonal entries are one. Hence \(F\) has rank \(n\), and the pair-vector space decomposes orthogonally into the constants (dimension one), the image under \(F^{\mathsf T}\) of the label-coordinate sum-zero space (dimension \(n-1\)), and \(\ker F\) (dimension \(\binom n2-n=n(n-3)/2\)). On these three spaces, respectively, \(A\) acts by
\[
 d=\binom n2+1-2(n-1)=\binom{n-2}{2},\qquad 3-n,\qquad1.
\]
On the sum-zero image, \(J\) vanishes and \(F^{\mathsf T}F\) has eigenvalue \(n-2\); on \(\ker F\), both \(J\) and \(F^{\mathsf T}F\) vanish. These statements also prove that the three spaces exhaust all eigenvalues and their multiplicities. Taking the trace of the \(m\)-th power yields
\[
\mathcal N_{m,n}=d^m+(n-1)(3-n)^m+\frac{n(n-3)}2,
\]
which is the claimed exact formula for every \(m\ge3,n\ge6\).

## Verification

The standalone standard-library program `verify.py` reconstructs the **original graph** \(C_m\square K_n\) and exhaustively tests every candidate dissociation subset with at most two vertices in each clique fiber; no larger subset could be dissociation by the proved fiber bound. The exhaustive test covers \((n,m)=(5,3),(5,4),(6,3),(6,4),(7,3),(7,4)\), including \(707281\) row assignments for \((7,4)\). For \(n\ge6\) the computed maximum is \(2m\) and the exact number of maximizers matches the formula. It separately enumerates all length-\(m\) Kneser closed walks for every \(6\le n\le10\) and \(3\le m\le12\), and independently compares the original-graph degree test with the disjoint-pair homomorphism criterion on six additional finite base graphs.

To replay, run `python3 verify.py` using only the embedded script and the Python standard library; successful completion prints `VERIFY_OK`. These finite checks corroborate the bijection and matrix identities. The proof above, rather than an extrapolation from those cases, establishes the infinite result.

## Relationship to prior work

The dissociation-set invariant and its enumeration are established topics; Yuan, Yang, Ge and Gong (2024, arXiv:2412.17095) study extremal **total** counts of dissociation sets in connected graphs, particularly trees and unicyclic graphs. Their inspected results do not determine the multiplicity of maximum dissociation sets in the present highly cyclic products. Tepeh (2026, arXiv:2606.22428) studies the distinct parameter of degree-limited domination on Cartesian products; its inspected product results do not enumerate minimum three-path covers.

The closest direct product paper found is Suo, Chen and Zhang (2022), *k-Path vertex cover in Cartesian product graphs*, which explicitly treats products of cycles and complete graphs and seeks exact values or bounds for **minimum cover cardinality**. That known target is not the asserted novelty: our result is an exact classification and closed multiplicity formula for **all** minimum covers. The available abstract and bibliographic record did not contain such an enumeration; the full article text could not be inspected, so possible unobserved prior coverage remains a residual priority risk. The classical Kneser-graph spectrum is also not claimed as new: the proof independently derives it and applies it to the extremal cover multiplicity.

Related work of Wang, Tu and Lang (2023), *Entropy, Graph Homomorphisms, and Dissociation Sets*, bounds total numbers in bipartite settings, and does not cover the present nonbipartite clique-cycle optimum-multiplicity problem. These are implication comparisons, not conclusions from title matches alone.

## Limitations

The theorem counts **minimum** three-path vertex covers only, not all covers of every size. It requires \(n\ge6,m\ge3\), and it counts sets on labelled vertices rather than symmetry classes. The formula depends on the strict three-vertex path-cover definition, equivalently induced maximum degree at most one in the complement; it is **not** a formula for one-limited dominating sets, where the degree constraint is imposed on a different vertex subset. Earlier work may contain an equivalent formula under alternative names, especially an inaccessible relevant 2022 product paper. No independent mathematical audit has been performed.

## References

1. B.-J. Yuan, N. Yang, H.-Y. Ge, S.-C. Gong, *The number of dissociation sets in connected graphs*, arXiv:2412.17095, first public version December 22, 2024. https://arxiv.org/abs/2412.17095
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, first public version June 21, 2026. https://arxiv.org/abs/2606.22428
3. M.-G. Suo, J.-R. Chen, J.-M. Zhang, *k-Path vertex cover in Cartesian product graphs*, Journal of Shandong University (Natural Science) 57 (2022), 103–110, doi:10.6040/j.issn.1671-9352.0.2021.784. https://lxbwk.njournal.sdu.edu.cn/EN/Y2022/V57/I12/103
4. Z. Wang, J. Tu, R. Lang, *Entropy, Graph Homomorphisms, and Dissociation Sets*, Entropy 25 (2023), 163, doi:10.3390/e25010163. https://pmc.ncbi.nlm.nih.gov/articles/PMC9858558/
