# Minimum total double Roman functions of connected chain graphs
## Finding
Let \(G=(X,Y,E)\) be a connected chain graph with
\[
|X|\ge3,\qquad |Y|\ge3.
\]
Put
\[
U_X=\{x\in X:N(x)=Y\},\qquad
U_Y=\{y\in Y:N(y)=X\}.
\]
Then
\[
\gamma_{tdR}(G)=6.
\]

Moreover, every minimum total double Roman dominating function has exactly two positive vertices. One vertex \(x\in U_X\) and one vertex \(y\in U_Y\) receive label \(3\), and every other vertex receives label \(0\). Thus the number of minimum functions is
\[
|U_X|\,|U_Y|.
\]

For the half graph \(H_n\), \(n\ge3\), both universal classes are singletons. Hence \(H_n\) has a unique minimum total double Roman dominating function.

## Assumptions and scope
A total double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\), and the subgraph induced by the positive-labeled vertices has no isolated vertices.

A chain graph is a bipartite graph whose neighborhoods in each bipartition class are linearly ordered by inclusion. Connectivity implies that each side has at least one vertex universal to the opposite side, so \(U_X\) and \(U_Y\) are nonempty.

## Proof
Choose
\[
x\in U_X,\qquad y\in U_Y.
\]
Assign label \(3\) to \(x\) and \(y\), and label every other vertex \(0\). The two positive vertices are adjacent, so the positive support has no isolated vertex. Every zero in \(X\) is adjacent to \(y\), and every zero in \(Y\) is adjacent to \(x\). Hence this is a total double Roman dominating function of weight \(6\), proving
\[
\gamma_{tdR}(G)\le6.
\]

We prove that weight below \(6\) is impossible and classify equality. Let \(f\) be a total double Roman dominating function. Since its positive support has no isolated vertices and \(G\) is bipartite, each bipartition class contains a positive vertex.

Suppose both \(X\) and \(Y\) contain zero-labeled vertices. A zero in \(X\) forces the labels on \(Y\) to contain either one \(3\) or two \(2\)'s, so the total weight contributed by \(Y\) is at least \(3\). Symmetrically, the weight contributed by \(X\) is at least \(3\). Thus
\[
\omega(f)\ge6.
\]
If equality holds, each side contributes exactly \(3\). The only way to defend a zero with total side-weight exactly \(3\) is a single label \(3\). Hence each side contains exactly one positive vertex, both labeled \(3\). Totality makes these two vertices adjacent. Since every other vertex is zero, the label-\(3\) vertex in \(X\) must be adjacent to every vertex of \(Y\), and the label-\(3\) vertex in \(Y\) must be adjacent to every vertex of \(X\). Therefore they lie in \(U_X\) and \(U_Y\).

Now suppose exactly one side contains zeros, say \(X\), while every vertex of \(Y\) is positive. Since \(|Y|\ge3\), the weight on \(Y\) is at least \(3\). The positive support condition forces at least one positive vertex in \(X\).

If the weight on \(X\) is \(1\), then every label-
\(1\) vertex in \(Y\) would require a neighbor of label at least \(2\) in \(X\); therefore all vertices of \(Y\) would have label at least \(2\), giving total weight more than \(6\).

If the weight on \(X\) is \(2\), then either \(X\) contains one label \(2\) or two labels \(1\). In the first case, defending a zero of \(X\) forces the weight on \(Y\) to be at least \(5\): with at least three positive vertices, the cheapest defending pattern is one label \(3\) and two labels \(1\). In the second case, no label-
\(1\) vertex of \(Y\) can be supported from \(X\), so the weight on \(Y\) is at least \(6\). Either way the total exceeds \(6\).

If the weight on \(X\) is at least \(3\), then a zero in \(X\) forces \(Y\) to contain either a label \(3\) or two labels \(2\). Because all three or more vertices of \(Y\) are positive, its weight is at least \(4\), and the total again exceeds \(6\).

The case in which only \(Y\) contains zeros is symmetric.

Finally, if neither side contains a zero, then all vertices are positive. Since \(|X|+|Y|\ge6\), weight at most \(6\) would force every vertex to have label \(1\). But a label-
\(1\) vertex must have a neighbor labeled \(2\) or \(3\), a contradiction.

Thus every total double Roman dominating function has weight at least \(6\), and equality is possible exactly for the universal opposite-side label-
\(3\) pairs described above.

## Verification
The included checker enumerates every connected canonical chain graph with both bipartition sizes in \(\{3,4\}\). For each graph it exhausts every labeling in \(\{0,1,2,3\}^{V(G)}\), tests the total double Roman definition directly from adjacency, computes the minimum weight, and compares every minimum function with the universal-pair classification.

## Relationship to prior work
The 2019 total-double-Roman literature establishes the definition, NP-hardness on bipartite graphs, and general relations with domination, total domination, double Roman domination, and total Roman domination. A primary full-text treatment proves the general upper bound
\[
\gamma_{tdR}(G)\le3\gamma_t(G),
\]
and lists Mathematics Subject Classification \(05C69\). Its searchable full text contains no chain-graph or half-graph theorem.

Connected chain graphs have total domination number \(2\), because the two universal opposite-side vertices form a total dominating set. The general inequality therefore gives the upper bound \(6\), but it does not prove equality or classify all minimum functions. The present theorem supplies exactly that missing equality structure: when both sides have at least three vertices, every optimum is forced to be one universal pair labeled \(3\).

Targeted searches under chain graph, half graph, Ferrers graph, and universal-vertex formulations did not locate an equivalent total-double-Roman classification.

## Limitations
The theorem assumes both bipartition classes have at least three vertices. Chain graphs with a side of size one or two have additional low-weight phenomena and are not covered here.

The exhaustive checker covers all connected canonical chain types with side sizes three and four; this is corroborative only. The arbitrary-size theorem follows from the proof.

A differently phrased or non-indexed chain-graph theorem may exist despite the targeted searches.

## References
1. G. Hao, L. Volkmann, D. A. Mojdeh, “Total double Roman domination in graphs,” Communications in Combinatorics and Optimization 5 (2020), 27–39, DOI 10.22049/CCO.2019.26484.1118; published online 16 July 2019.
2. Z. Shao, J. Amjadi, S. M. Sheikholeslami, M. Valinavaz, “On the Total Double Roman Domination,” IEEE Access 7 (2019), 52035–52041, DOI 10.1109/ACCESS.2019.2911659.
