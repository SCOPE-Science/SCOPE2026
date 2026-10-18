# General-position polynomial of once-subdivided complete graphs

## Finding
For each integer \(n\ge3\), subdivide every edge of the complete graph \(K_n\) exactly once, obtaining \(G_n=S(K_n)\). Its complete ordinary general-position polynomial is \(\psi_n(z)=\sum_{X\subseteq V(G_n)\ \mathrm{GP}}z^{|X|}\), including the empty set. The family has the exact exponential generating function
\[
\sum_{n\ge0}\psi_n(z)\frac{x^n}{n!}
=\exp\!\left(zx+xe^{zx}-\frac{zx^2}{2}+\frac{z^3x^3}{6}\right)+z^2x^2e^x.
\]
The maximum cardinality and the number of labeled maximum general-position sets are respectively
\[
\operatorname{gp}(G_n)=n,\qquad
M_n=\sum_{t=0}^{\lfloor n/3\rfloor}\frac{n!}{(n-3t)!\,6^t\,t!}.
\]
In particular, the complete coefficients for \(n=3,4,5,6\) are respectively \((1,6,15,2)\), \((1,10,45,30,5)\), \((1,15,105,175,100,11)\), and \((1,21,210,655,900,357,31)\).

## Assumptions and scope
All graphs are finite, simple and undirected. The original vertices of \(G_n\) are \([n]=\{1,\ldots,n\}\); for every \(\{i,j\}\subseteq[n]\), a new vertex \(e_{ij}\) is adjacent exactly to \(i\) and \(j\). A vertex set is in *geodesic general position* (GP) if no three distinct selected vertices lie on one shortest path. Equivalently, none of the three is between the other two, where betweenness means equality in the triangle inequality for graph distance.

Every candidate set has a unique form \(X=U\cup\{e_{ij}:\{i,j\}\in F\}\), with \(U\subseteq[n]\) and \(F\subseteq\binom{[n]}2\). **Complete characterization:** this set is GP precisely in one of two disjoint situations:

(i) no edge of \(F\) has an endpoint in \(U\), and \(F\), regarded as a graph on \([n]\), contains no simple path with three edges (the path need not be induced); or

(ii) \(U=\{u\}\) and \(F=\{\{u,v\}\}\) for some \(v\ne u\).

## Proof
**Distances.** Between distinct original vertices the distance is \(2\). The distance from an original \(u\) to a subdivision vertex \(e_{ij}\) is \(1\) when \(u\in\{i,j\}\), otherwise \(3\). Distinct subdivision vertices have distance \(2\) if their underlying edges share an endpoint, otherwise distance \(4\). The latter statements follow because all walks in the subdivided clique alternate between original and subdivision vertices, and the indicated short walks exist.

**Three selected originals.** None lies on a shortest path between the other two, since their pairwise distances are all \(2\). **Two originals and one subdivision vertex.** Such a triple is forbidden exactly when the underlying edge meets the two selected originals: if both are its endpoints, the subdivision vertex is between them; if only one is its endpoint, that original lies on a three-edge shortest path from the other original to the subdivision vertex. If the underlying edge meets neither, all applicable triangle inequalities are strict.

**One original and two subdivision vertices.** If both underlying edges meet the original, the original is between the two subdivision vertices. If exactly one meets it, either the incident subdivision vertex lies between the original and the other subdivision vertex (if their edges share their other endpoint), or the original lies between the two subdivision vertices (if the underlying edges are disjoint). If neither edge meets the original, all applicable triangle inequalities are strict. Hence an incident selected edge is compatible with just one selected original and no other selected vertices; this proves case (ii) is the sole exception to case (i).

**Three subdivision vertices.** The middle subdivision vertex lies on a geodesic between the other two exactly when the corresponding first and third edges of \(K_n\) are disjoint and both meet the middle edge. These three edges are exactly a simple path on four distinct original vertices. Thus GP triples of this type are equivalent to the absence of a (possibly noninduced) three-edge path in \(F\). Together the three types prove the stated necessary-and-sufficient characterization.

**Connected-component lemma.** A connected simple graph having no ordinary three-edge path is either an isolated vertex, a star, or a triangle. Indeed a cycle of length at least four or a tree containing a three-edge path is forbidden. A triangle cannot have any attached edge without creating a three-edge path. A connected, triangle-free graph with no three-edge path is acyclic (any cycle has length at least four), and its tree diameter is at most two, so it is a star. The converse is immediate.

**Enumeration.** Let \(A_n(z)\) count edge subsets \(F\) on a labeled \(n\)-element original ground set that contain no three-edge path, weighting each selected edge by \(z\), including isolated original labels. Each connected component is an isolated vertex, a star, or a triangle. For a component on \(k\) labels, its total weight is \(1\) if \(k=1\), \(z\) if \(k=2\), and \(kz^{k-1}\) if \(k\ge3\), with the additional triangle contribution \(z^3\) when \(k=3\). The labeled exponential formula therefore gives
\[
\sum_{n\ge0}A_n(z)\frac{x^n}{n!}
=\exp\!\left(xe^{zx}-\frac{zx^2}{2}+\frac{z^3x^3}{6}\right).
\]
Here the subtraction corrects the two orientations of a two-vertex star, and the cubic term adds triangle components. Case (i) permits independently choosing any number of original vertices \(U\), weighted by \(z\), while all edge-components occupy labels outside \(U\). Hence its EGF is the last displayed expression multiplied by \(e^{zx}\). Case (ii) contributes precisely \(n(n-1)z^2\) to \(\psi_n\), since it selects an ordered incident pair of original labels. Its EGF is \(z^2x^2e^x\). The two cases are disjoint, proving the full formula.

**Maximum sets.** In case (i), write \(W=[n]\setminus U\). Every component of \(([n],F)\) lying in \(W\) is a star (possibly isolated) or a triangle. A star on \(k\) vertices has \(k-1\) edges, whereas a triangle on three vertices has three edges, so \(|F|\le|W|\) with equality if and only if every vertex of \(W\) belongs to a triangle component. Thus \(|X|=|U|+|F|\le n\). Case (ii) contains only two vertices, so also cannot exceed \(n\) when \(n\ge3\). Taking \(U=[n]\) attains \(n\). Every maximum set is therefore formed by choosing \(t\) disjoint unordered triples of original labels, taking the three subdivision vertices indexed by edges within each triple, and taking all remaining original vertices. For given \(t\), the number of such triple partitions is \(n!/((n-3t)!6^t t!)\); summing over \(0\le t\le\lfloor n/3\rfloor\) proves \(M_n\).

## Verification
The standalone `gp_subdivision_verifier.cpp` independently constructs \(G_n\), computes all-pairs shortest paths by breadth-first search, evaluates forbidden geodesic triples without using the formula, and exhaustively compares them against the proposed structural classification for \(3\le n\le6\). It also tests the degree and leading coefficient. Exactly 2,131,008 vertex subsets were inspected across four graphs; no disagreements occurred. `gp_subdivision_series_check.py` uses an independent labeled-component recurrence to replay the generating-function coefficients through \(n=9\) and checks the maximum-set formula. The actual execution outputs are included. Finite exhaustive tests cannot replace the preceding proof for unbounded \(n\).

## Relationship to prior work
The general-position polynomial was introduced and studied by Iršič, Klavžar, Rus and Tuite in their 2024 paper, which computes it for other graph families and graph operations; its full accessible article does not provide this subdivision-family enumerator. Ghorbani and collaborators' Theorem 4.4 (2019) determines the general-position *number* of \(L(K_n)\), namely \(n\) when \(3\mid n\) and \(n-1\) otherwise. The induced edge-vertex subproblem of \(S(K_n)\) is related to that line-graph problem, but that scalar theorem does not count all vertex subsets of \(S(K_n)\), including original vertices and mixed configurations. Existing graph-metric homotopy results for \(S(K_n)\) concern different invariants. The novelty assessed here is the joint original/subdivision-vertex characterization, complete polynomial and the complete maximum-set count, not prior facts about \(L(K_n)\).

## Limitations
This theorem concerns uniform one-subdivision of every edge of a complete graph, not arbitrary subdivision lengths or general base graphs. Its claim of original contribution is subject to undetected or unindexed equivalent literature. The argument is self-contained but has not been independently validated.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1 (first posted 2024-01-11); *Results in Mathematics* 79 (2024), Article 110, DOI:10.1007/s00025-024-02133-3.
2. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. R. Mahid, G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286, Theorem 4.4 (2019).
