# Complete general-position and maximal-set polynomials of triangular graphs

## Finding
For each integer \(n\ge2\), write \(T_n=J(n,2)=L(K_n)\). Its vertices are the two-element subsets of \([n]\), adjacent when they intersect. A set of vertices is *in general position* if no three distinct selected vertices occur on any shortest path. Define \(\psi_n(z)=\sum_{S\text{ in general position}}z^{|S|}\) and \(\phi_n(z)=\sum_{S\text{ inclusion-maximal in general position}}z^{|S|}\). We establish the following complete labelled exponential generating functions (formal at \(n=0,1\)):

\[
\boxed{\sum_{n\ge0}\psi_n(z)\frac{t^n}{n!}=\exp\!\left(te^{zt}-\frac{zt^2}{2}+\frac{z^3t^3}{6}\right).}
\]
\[
\boxed{\sum_{n\ge0}\phi_n(z)\frac{t^n}{n!}=\exp\!\left(t(e^{zt}-1)-\frac{zt^2}{2}+\frac{(z^3-3z^2)t^3}{6}\right)+t\exp\!\left(\frac{z^3t^3}{6}\right).}
\]
They simultaneously enumerate **all** general-position sets and **all inclusion-maximal** general-position sets by cardinality, not merely their largest and smallest possible sizes.

In particular, put \(U_n=[z^{\operatorname{gp}(T_n)}]\psi_n(z)\). If \(n\equiv0\pmod3\), then
\[
U_n=\frac{n!}{6^{n/3}(n/3)!}.
\]
Otherwise,
\[
U_n=n!\sum_{\substack{1\le k\le n\\k\equiv n\pmod3}}\frac{a_k}{k!\,6^{(n-k)/3}((n-k)/3)!},\qquad a_1=a_2=1,\quad a_k=k\ (k\ge3).
\]
The general-position number is \(n\) when \(3\mid n\), and \(n-1\) otherwise. Put \(L_n=[z^{\operatorname{gp}^-(T_n)}]\phi_n(z)\). If \(n\) is even,
\[
L_n=\frac{n!}{2^{n/2}(n/2)!};
\]
if \(n\) is odd, then
\[
L_n=\binom n3\frac{(n-3)!}{2^{(n-3)/2}((n-3)/2)!}
+\mathbf1_{n\ge5}\,5\binom n5\frac{(n-5)!}{2^{(n-5)/2}((n-5)/2)!}.
\]
The lower general-position number is \(n/2\) for even \(n\) and \((n+3)/2\) for odd \(n\).

## Assumptions and scope
All graphs are finite, undirected and simple. Set cardinalities count the edges of a selected subgraph of \(K_n\); the vertices of \(T_n\) are those edges. Every set is labelled by the original ground set \([n]\). We count each *vertex set* once, without choosing an ordering, star center when a single edge is present, or an auxiliary decomposition. The generating-function variable \(t\) marks original vertices and \(z\) marks selected edges. The formal cases \(n=0,1\) count the unique empty graph configuration; all graph statements concern \(n\ge2\).

## Proof
**1. Geodesics and selected-edge components.** In \(T_n\), two disjoint edges of \(K_n\) have distance two, with every common neighbor an edge meeting both. Thus a three-vertex geodesic consists exactly of a selected length-two *induced path* in the graph on chosen vertices. Therefore a chosen family \(S\subseteq E(K_n)\) is in general position if and only if its induced line graph is \(P_3\)-free, equivalently a disjoint union of cliques. A family of distinct pairwise-intersecting edges of a simple graph is either a star (all share a common endpoint) or the three edges of a triangle: for any two intersecting edges \(ab,ac\), an edge meeting both but not containing \(a\) must be \(bc\), and then no additional distinct edge meets all three. Since different clique components in the selected line graph have no adjacent edges, their original supports are disjoint. Consequently every selected-edge family decomposes uniquely into disjoint supports carrying either a single edge, a two-or-more-edge star, or one full triangle; unused original vertices are singleton supports.

**2. Exact all-set enumeration.** A support of size one has weight \(1\); size two has weight \(z\) (one unique edge); size three has weight \(3z^2+z^3\) (three two-edge stars or the unique triangle); and size \(k\ge4\) has weight \(kz^{k-1}\) (choose one center). In the labelled-component exponential formula the exponent is therefore
\[
t+\frac{zt^2}{2}+\frac{(3z^2+z^3)t^3}{6}+\sum_{k\ge4}\frac{kz^{k-1}t^k}{k!}
=te^{zt}-\frac{zt^2}{2}+\frac{z^3t^3}{6}.
\]
The correction for size two removes the duplicate center choices, and the size-three correction adds the missing triangle. This proves the first boxed identity.

**3. Exact inclusion-maximality.** If at least two original vertices are unused, adding the edge between two unused vertices creates a new isolated selected-edge component. If a component is a two-edge star, adding the missing leaf-to-leaf edge completes a triangle. If exactly one vertex \(u\) is unused and there is any selected component other than a full triangle, that component is a star; attaching \(u\) to its center retains a star, and for a single-edge component either endpoint can serve as center. Therefore a maximal configuration either has no unused vertices and no two-edge-star component, or has exactly one unused vertex and every other component a complete triangle.

Conversely, in a configuration of the first type, adding an edge within an existing star support with at least three selected edges produces a new edge meeting some, but not all, star edges, and hence an induced \(P_3\); there is no unselected edge within a one-edge or full-triangle support. Any edge joining two occupied components also produces an induced \(P_3\): the new edge meets an edge in one component and is disjoint from every edge of the other component not incident to its endpoint; when both components are one-edge supports, the two existing selected edges together with the new edge are themselves an induced \(P_3\). In a configuration of the second type, the only possible added edges join the unique unused vertex to one of the complete triangles, producing an induced \(P_3\), because the new edge meets at least one and misses another edge of that triangle. Thus the characterization is necessary and sufficient.

In the first maximality mode, allowable occupied component weights are \(z\) at size two, \(z^3\) at size three, and \(kz^{k-1}\) for sizes \(k\ge4\). Their exponential sum is
\[
t(e^{zt}-1)-\frac{zt^2}{2}+\frac{(z^3-3z^2)t^3}{6}.
\]
In the second mode we choose one unused vertex and partition the others entirely into triangles, with generating function \(t\exp(z^3t^3/6)\). The modes are disjoint for \(n\ge2\), proving the second boxed identity. The constant term for \(n=0\) is contributed by the first mode only.

**4. Extremal coefficients.** Every selected component except a complete triangle consumes precisely one more original vertex than selected edges; every triangle consumes equally many. Hence at most \(n\) edges are selected, with equality precisely when \(3\mid n\) and every component is a triangle. Otherwise exactly one nontriangle support remains to reach \(n-1\) selected edges; its size is \(k\equiv n\pmod3\). The component has \(a_k\) shapes, proving the displayed formula for \(U_n\).

For lower extremality in the first maximality mode, every occupied support has size at least two. A one-edge support uses two vertices at density \(1/2\); a triangle uses three with three selected edges; and a full star on \(k\ge4\) vertices has \(k-1\) selected edges. For even \(n\), the minimum-size maximal family consists of perfect matchings. For odd \(n\), replacing exactly one pair-block by either a triangle-block on three vertices (one added selected edge beyond half the support) or a five-vertex star-block (two added selected edges beyond half the support) yields the least possible edge count \((n+3)/2\). Any different odd-size block costs at least as much, and two such blocks cost more. The exceptional one-unused-triangles maximality mode has \(n-1\) selected edges, and occurs only when \(n\equiv1\pmod3\); for odd such \(n\ge7\), this exceeds \((n+3)/2\). Therefore it never contributes to the lower coefficient. Multiplying the number of ways to choose a triangle or five-vertex-star support by the number of perfect matchings on the remaining labelled vertices gives exactly the formula displayed for \(L_n\).

## Verification
The two standalone programs `verify_triangle_gp.py` and `verify_triangle_gp.cpp` reconstruct the full coefficients by different implementations. The Python script computes the labelled-block assemblies and checks every selected vertex subset directly against shortest-path forbidden triples for \(2\le n\le6\), including inclusion-maximality. The C++17 program separately enumerates all subsets through \(n=7\), checks induced \(P_3\)-freeness and maximality, and compares polynomial coefficient arrays. Both confirm the following full size distributions:

- \(n=5\): \(\psi_5(z)=1+10z+45z^2+60z^3+15z^4\), and \(\phi_5(z)=15z^4\).
- \(n=6\): \(\psi_6(z)=1+15z+105z^2+275z^3+240z^4+66z^5+10z^6\), and \(\phi_6(z)=15z^3+60z^4+6z^5+10z^6\).
- \(n=7\): \(\phi_7(z)=210z^5+217z^6\).

The code checks the all-parameter extremal formulas symbolically through \(n=15\) via exact coefficient recurrence. These finite checks corroborate but do not replace the infinite-family component proof.

## Relationship to prior work
Anand et al. (arXiv:1812.08460, initial public date 2018-12-20) established the general-position characterization using cluster graphs. Ghorbani et al. (arXiv:1903.04286) determined the scalar general-position number of triangular graphs. Di Stefano et al. (arXiv:2306.09965) characterized lower general-position sets and determined the lower number. Iršič et al. (arXiv:2401.05696) introduced general-position polynomials, with a result for the Kneser graph \(K(n,2)\), the **complement** of \(J(n,2)\), not this graph. Their available full-text statements do not furnish the two explicit triangular-graph generating functions or the listed extremal multiplicities. This is an enumerative refinement of established structural and extremal results, not a new claim about their scalar values.

## Limitations
The formulas count labelled vertex subsets, not isomorphism types. There is no claim of new scalar values for the previously determined largest and smallest sizes. Finite programs do not certify all parameter values; the general results depend on the proof above. Although targeted source comparisons found no prior exact pair of generating functions, unindexed work or enumerations under alternative terminology may overlap. An independent review has not been performed.

## References
1. B. S. Anand et al., *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (first public 2018-12-20).
2. Ghorbani et al., *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286 (2019).
3. Di Stefano et al., *Lower General Position Sets in Graphs*, arXiv:2306.09965 (2023).
4. Iršič et al., *General Position Polynomials*, arXiv:2401.05696 (2024).
