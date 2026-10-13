# Perfect Italian domination after matching deletion in complete bipartite graphs
## Finding
Let \(2\le m\le n\) and \(0\le t\le m\). Write \(G_{m,n,t}=K_{m,n}-M_t\), where the deleted edges are \(a_i b_i\) for \(1\le i\le t\). A perfect Italian dominating function is a map \(f:V(G_{m,n,t})\to\{0,1,2\}\) such that every vertex with label zero has neighbor-label sum exactly two. Its weight is the sum of all labels, and \(\gamma_I^p\) is the minimum weight.

The exact value is
\[
\gamma_I^p(G_{m,n,t})=
\begin{cases}
2,&m=2,\ t=0,\\
3,&m=2,\ t=1,\\
3,&(m,n,t)=(2,3,2)\text{ or }(3,3,3),\\
4,&\text{otherwise}.
\end{cases}
\]

The minimum functions can also be counted exactly. Put
\[
C(m,n,t)=\sum_{a,b\in\{1,2\}}\ \sum_{s=0}^{\min\{a,b,t\}}
\binom ts\binom{m-t}{a-s}\binom{n-t}{b-s},
\]
where a binomial coefficient is zero when its lower index lies outside its natural range. In every weight-four case except \((m,n,t)=(2,2,2)\), the number of minimum functions is
\[
C(m,n,t)+2\mathbf 1_{(m,n,t)=(3,3,2)}+\mathbf 1_{(m,n,t)=(3,4,3)}.
\]
For \((2,2,2)\) the number is nine. In the lower-weight cases, the numbers of minimum functions are: two for \((2,2,0)\), two for \((2,2,1)\), one for \((2,n,0)\) when \(n>2\), one for \((2,n,1)\) when \(n>2\), one for \((2,3,2)\), and two for \((3,3,3)\).

## Assumptions and scope
All graphs are finite and simple. The matching \(M_t\) has pairwise disjoint endpoints and lies between the two shores of \(K_{m,n}\). Relabeling lets its edges be written as \(a_i b_i\) for \(1\le i\le t\). The theorem concerns the exact perfect Italian domination number and the complete set of minimum functions only; it does not enumerate functions of larger weight.

For a labeling, write \(x_i=f(a_i)\), \(y_j=f(b_j)\), and let \(X=\sum_i x_i\) and \(Y=\sum_j y_j\). A zero vertex \(a_i\) sees weight \(Y-y_i\) when \(i\le t\) and weight \(Y\) otherwise. Symmetrically, a zero vertex \(b_j\) sees weight \(X-x_j\) when \(j\le t\) and weight \(X\) otherwise.

## Proof
Suppose first that a perfect Italian dominating function has weight at most three. If both shores contain a zero vertex, a zero on the first shore forces \(Y\ge2\), while a zero on the second forces \(X\ge2\); hence the total weight is at least four, a contradiction. Therefore one shore is entirely positive.

If the first shore is entirely positive, then \(m\le3\). For \(m=2\), weight two is possible precisely when \(t=0\): assigning label one to both vertices of the two-vertex shore works, and deleting even one incident edge destroys this weight-two pattern. At weight three, the same two vertices must still both carry label one in the nontrivial infinite case; the unique extra unit must lie on every deleted mate that would otherwise see only one unit. This is possible exactly for \(t=1\), giving the family \(m=2,t=1\). If instead the second shore is entirely positive, its size is at most three. The only new possibility with \(m=2\) is \((m,n,t)=(2,3,2)\), where all three vertices on the second shore have label one. With three vertices on each shore, the only weight-three possibility is \((3,3,3)\), where all vertices of either one shore receive label one. These constructions show that the listed weight-two and weight-three cases are feasible, and the preceding exhaustion shows that no other case has weight below four.

Every remaining parameter choice has a weight-four function. If \(t=0\), put label two on one vertex in each shore. If \(t\ge1\), put label two on the two endpoints of one deleted edge. Every zero vertex then sees exactly two units, because the only missing adjacency at the chosen index joins two positive vertices. This proves the formula for \(\gamma_I^p\).

It remains to classify and count minimum functions. Consider first a weight-four case in which both shores contain a zero. Then \(X\ge2\) and \(Y\ge2\), so \(X=Y=2\). Each shore therefore has positive-support size either one, consisting of a single label two, or two, consisting of two labels one. For every deleted pair index \(i\le t\), if \(x_i=0\), then the zero vertex \(a_i\) requires \(Y-y_i=2\), hence \(y_i=0\). The symmetric argument gives the converse. Thus the two positive supports agree on the deleted matched indices.

If the support sizes are \(a,b\in\{1,2\}\) and their common matched support has size \(s\), choose those matched indices in \(\binom ts\) ways, the remaining first-shore support in \(\binom{m-t}{a-s}\) ways, and the remaining second-shore support in \(\binom{n-t}{b-s}\) ways. Summing gives \(C(m,n,t)\).

A weight-four minimum can fail to have a zero on both shores only in very small boundary cases. If the three-vertex shore is entirely positive, its labels must all be one and the opposite shore has total label one. Every zero on that opposite shore must then be matched, so there can be at most one unmatched vertex there and it must be the unique positive one. In the minimum-weight-four regime this contributes one extra function for \((3,3,2)\) and one for \((3,4,3)\). The symmetric orientation contributes a second extra function for \((3,3,2)\). The apparent case \((3,3,3)\) is not included because its minimum weight is already three. No larger shore can be entirely positive at weight four. Finally, \(G_{2,2,2}\) is the disjoint union of two edges. A minimum weight-two perfect Italian function on a single edge has exactly three label patterns, namely \((2,0)\), \((1,1)\), and \((0,2)\); independent choices on the two components give nine minimum functions.

The lower-weight minimum counts follow from the same exhaustion: the two balanced orientations occur only for \((2,2,0)\) and \((2,2,1)\); the families with a larger second shore have a unique orientation; \((2,3,2)\) has the unique all-one labeling on its three-vertex shore; and \((3,3,3)\) has the two all-one shore labelings.

## Verification
The standalone program `verify.py` constructs \(G_{m,n,t}\) implicitly from the shore sums and deleted matched indices, exhausts every labeling by \(\{0,1,2\}\), tests the exact perfect-Italian condition, and compares both the minimum weight and the number of minimizers with the theorem. It exhaustively checks all parameter triples with \(2\le m\le n\le5\) and \(m+n\le9\), comprising 178,848 labelings across 34 parameter triples. It also evaluates the closed formulas on 10,295 parameter triples with \(2\le m\le30\) and \(m\le n\le40\). Finite computation is a stress test; the universal statement is established by the proof above.

## Relationship to prior work
Lauri and Mitillos characterize graphs of perfect Italian domination number two and three and determine the complete-bipartite baseline: \(\gamma_I^p(K_{2,n})=2\), while \(\gamma_I^p(K_{m,n})=4\) for \(m,n\ge3\). Their result corresponds to the undeleted case \(t=0\) and does not classify matching-deleted bicliques or count their minimum functions.

Pazhaniappan, Sathi, and Malayil study perfect Italian domination on structured bipartite graph classes and establish algorithms and hardness boundaries for convex, tree-convex, and related classes. Their article motivates exact structural analysis on ordered bipartite graphs, but its inspected text contains no theorem for complete bipartite graphs with a matching deleted, crown graphs, or minimum-function enumeration. Ben Othman's 2024 exact-value paper treats circulants, generalized Petersen graphs, strong grids, and Jahangir graphs rather than this family.

The theorem is therefore a matching-deletion refinement of the known complete-bipartite baseline. The originality-bearing part is not merely the scalar value four in the generic region: it is the complete low-weight phase diagram together with the support-synchronization rule and closed count of all minimum perfect Italian functions.

## Limitations
The result is restricted to deleting a matching from a complete bipartite graph. Deleting an arbitrary edge set can create interacting deficits that are not represented by the one-index support synchronization used here. The literature search found no covering statement under perfect Italian domination, PIDF, two-fair domination, or matching-deleted biclique terminology, but a poorly indexed equivalent result remains a residual originality risk. No independent audit has been performed.

## References
1. R. Pazhaniappan, M. M. Sathi, and M. V. Malayil, “Perfect Italian Domination on Structured Bipartite Graphs: Algorithms, Parameterization, and Hardness,” *Mathematics* 14 (2026), 3380. DOI: 10.3390/math14183380.
2. J. Lauri and C. Mitillos, “Perfect Italian domination on planar and regular graphs,” *Discrete Applied Mathematics* 285 (2020), 676–687. Preprint: arXiv:1905.06293. DOI: 10.1016/j.dam.2020.05.024.
3. K. Ben Othman, “On the Perfect Italian Domination Numbers of Some Graph Classes,” *Galoitica: Journal of Mathematical Structures and Applications* 11 (2024), 35–46. DOI: 10.54216/GJMSA.0110104.
