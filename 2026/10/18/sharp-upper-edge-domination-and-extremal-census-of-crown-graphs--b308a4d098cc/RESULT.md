# Sharp upper edge domination and extremal census of crown graphs

## Finding
Let \(n\ge5\) be an integer. The *crown graph* \(G_n\) is the graph with vertex classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\) and exactly the edges \(a_i b_j\) for distinct indices \(i,j\). An edge set \(F\) *dominates edges* if every graph edge belongs to \(F\) or shares a vertex with some edge of \(F\). A dominating edge set is *inclusion-minimal* if removal of any chosen edge destroys domination.

Define \(\gamma'(G_n)\) to be the smallest cardinality of an edge-dominating set and \(\Gamma'(G_n)\) the largest cardinality of an inclusion-minimal one. Then
\[
\gamma'(G_n)=n-1,\qquad \Gamma'(G_n)=2n-4.
\]
The number of minimum edge-dominating sets is \(nD_{n-1}\), where \(D_r\) is the number of derangements of an \(r\)-element labelled set:
\[
D_r=r!\sum_{j=0}^{r}\frac{(-1)^j}{j!}.
\]
All minimum sets are obtained by choosing \(k\in\{1,\ldots,n\}\), excluding the two vertices \(a_k,b_k\), and taking a perfect matching \(a_i b_{\pi(i)}\) on the remaining vertices with \(\pi(i)\ne i\) for each \(i\ne k\).

There are exactly \(n(n-1)\) maximum inclusion-minimal edge-dominating sets. Every maximum set is uniquely indexed by distinct \(k,\ell\in\{1,\ldots,n\}\) and equals
\[
F_{k,\ell}=\{a_\ell b_j:j\notin\{k,\ell\}\}\ \cup\ \{a_jb_\ell:j\notin\{k,\ell\}\}.
\]
This is the disjoint union of two stars, one centered at \(a_\ell\) and one at \(b_\ell\). The gap \(\Gamma'(G_n)-\gamma'(G_n)=n-3\) therefore grows without bound on the connected \((n-1)\)-regular bipartite crown graphs.

## Assumptions and scope
All graphs are finite, simple, and undirected. The theorem concerns *ordinary*, not *perfect*, edge domination: an unselected edge may meet more than one chosen edge. The graph classes are labelled by their indexed bipartitions, and the counts distinguish different edge subsets. The two extremal characterizations hold for every integer \(n\ge5\); smaller orders are outside the theorem's maximum-set classification.

## Proof
For an arbitrary edge set \(F\subseteq E(G_n)\), let \(U\subseteq\{1,\ldots,n\}\) be the indices of vertices \(a_i\) incident with no edge of \(F\); similarly let \(V\) index the unoccupied vertices \(b_j\). An edge is undominated precisely when both its endpoints are unoccupied. Thus \(F\) is edge dominating if and only if there is no pair \(i\in U\), \(j\in V\) with \(i\ne j\). This is equivalent to one of three support patterns: \(U=\varnothing\), or \(V=\varnothing\), or \(U=V=\{k\}\) for some \(k\).

First suppose \(U=V=\varnothing\) and \(F\) is inclusion-minimal. If a chosen edge \(a_i b_j\) had a second chosen edge at either endpoint, removing it would leave at least one bipartition side fully incident: if the \(a_i\) endpoint remains covered, then \(U\) remains empty, while if the \(b_j\) endpoint remains covered, then \(V\) remains empty. Either alternative preserves domination. Therefore both endpoints of every chosen edge have selected-edge degree one. Consequently \(F\) is a perfect matching of all \(2n\) vertices and has size \(n\). Conversely any such perfect matching is inclusion-minimal: removing one edge makes its endpoints both uncovered and the removed edge undominated.

If exactly one of \(U,V\) is empty, say \(U=\varnothing\) and \(V\ne\varnothing\), every vertex on side \(A\) meets \(F\). If some edge of \(F\) meets a vertex \(a_i\) of selected-edge degree at least two, deleting that edge leaves \(U\) empty and still dominates all edges, contradicting minimality. Hence every \(a_i\) has selected-edge degree one, and necessarily \(|F|=n\). The reverse orientation is symmetric. These necessary size bounds do not assert every assignment of one edge per covered vertex is minimal.

It remains to analyze \(U=V=\{k\}\). Every vertex other than \(a_k,b_k\) has positive selected-edge degree. If a chosen edge \(a_i b_j\) has both ends of degree at least two, deleting it does not change either uncovered-index set, so domination persists. Hence minimality forces at least one endpoint of every chosen edge to have selected-edge degree one. Conversely, if every chosen edge has an endpoint of degree one, removing \(a_i b_j\) uncovers \(a_i\) or \(b_j\), where \(i,j\ne k\). In the first case the edge \(a_i b_k\) becomes undominated; in the second, the edge \(a_k b_j\) becomes undominated. Therefore minimality is **equivalent** to the chosen-edge graph on its \(2(n-1)\) active vertices being a star forest with no isolated vertices. Here a single edge is permitted as a one-edge star.

If such a star forest has \(c\) components, its number of edges equals \(2(n-1)-c\). Since both active bipartition sides contain \(n-1\ge4\) vertices, no single star spans all of them; hence \(c\ge2\), giving \(|F|\le2n-4\). Equality forces precisely two components. They must be one star centered at some \(a_i\) and one centered at some \(b_j\). If \(i\ne j\), then \(b_i\) is an active right vertex distinct from the right center and must be a leaf of the left-centered star, but the edge \(a_i b_i\) is absent from the crown graph. Thus \(i=j=\ell\), and the two components consist of exactly the edges of \(F_{k,\ell}\) displayed above, with \(k\ne\ell\). Each displayed set indeed has two nontrivial stars, dominates every edge, and is inclusion-minimal by the degree-one condition. Their distinct uncovered pair \(k\) and distinct star center \(\ell\) determine them uniquely. There are \(n(n-1)\) choices.

In the same \(U=V=\{k\}\) case, every active vertex has positive chosen degree, so \(|F|\ge n-1\). Equality implies a perfect matching on the active vertices. The absence of the diagonal edges \(a_i b_i\) forces its matching permutation to be fixed-point-free. Conversely, each such deranged matching dominates edges (the only omitted vertices are the forbidden pair \(a_k,b_k\)) and is minimal: deleting any chosen edge uncovers its endpoints and leaves that edge undominated. This gives exactly \(nD_{n-1}\) minimum sets.

The other two support cases always use at least \(n\) edges, as established above (or simply because one bipartition is fully occupied), and the full-support case also has at least \(n\) edges. Hence \(n-1\) is the minimum. For \(n\ge5\), \(2n-4>n\), so only the two-component star forests attain the maximum. This completes the classification and both counts. The gap is their difference, \(n-3\).

## Verification
The included independent verifier `verify.py` enumerates every edge subset for \(n=3,4,5\), tests edge domination directly from closed edge neighborhoods and then tests inclusion-minimality by single-edge deletion. It checks all minimum sets against the derangement construction for those sizes, and at \(n=5\) checks *every* maximum set against the two-star family. The exact exhaustive search covers \(2^6+2^{12}+2^{20}=1,052,736\) candidate subsets; for \(n=5\) it finds 45 minimum sets of size 4 and 20 maximum sets of size 6. The verifier additionally checks the domination and deletion-minimality of all \(F_{k,\ell}\) for dimensions \(5\) through \(25\). See `verify_output.txt` for the actual output. These finite checks corroborate, but do not replace, the proof for all \(n\ge5\).

## Relationship to prior work
Anderson and Kuenzel (2026) establish structural results for **nonbipartite** well-edge-dominated graphs and motivate comparing the minimum and largest inclusion-minimal edge-dominating sets. Their main classification does not cover the bipartite crown family or its extremal enumerations. Anderson, Kuenzel and Rall (2021) characterize other well-edge-dominated graph families, including complete bipartite graphs and Cartesian products; their stated results do not entail the two-star extremal census after deleting a perfect matching. Known general relationships between matching parameters and edge domination may imply weaker lower bounds, but do not supply the complete extremal-family classification here. Perfect edge domination, in which an unselected edge must touch **exactly one** selected edge, is a different invariant and its formulas are not being restated.

## Limitations
The maximum-set classification is restricted to \(n\ge5\); it does not assert a common description in smaller orders. The proof classifies the minimum and maximum configurations but not the number of inclusion-minimal configurations at each intermediate size. A targeted literature and mathematical-index comparison found no directly covering result, but cannot certify absolute publication priority. No independent external audit has been performed.

## References
1. Sarah E. Anderson and Kirsti Kuenzel, *Characterizing all nonbipartite well-edge-dominated graphs*, arXiv:2606.00802, first publicly submitted 2026-05-30, https://arxiv.org/abs/2606.00802 .
2. Sarah E. Anderson, Kirsti Kuenzel, and Douglas F. Rall, *On well-edge-dominated graphs*, arXiv:2110.07133, 2021, https://arxiv.org/abs/2110.07133 .
