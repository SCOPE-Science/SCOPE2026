# Minimum total vertex-edge dominating sets of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph for \(n\ge3\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad
B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]

Then
\[
\gamma_{ve}^{t}(\operatorname{Cr}_n)=3.
\]

More strongly, the minimum total vertex-edge dominating sets are exactly
\[
\{a_i,a_j,b_k\}
\]
and
\[
\{a_k,b_i,b_j\},
\]
where \(i,j,k\) are pairwise distinct. Therefore the exact number of minimum sets is
\[
2\binom n2(n-2)=n(n-1)(n-2).
\]

## Assumptions and scope
A vertex \(v\) vertex-edge dominates an edge \(xy\) when at least one endpoint of \(xy\) lies in the closed neighborhood
\[
N[v].
\]
A set \(D\subseteq V(G)\) is vertex-edge dominating when every edge is vertex-edge dominated by some vertex of \(D\). It is total vertex-edge dominating when, in addition, the induced graph
\[
G[D]
\]
has no isolated vertices.

Equivalently, \(D\) is vertex-edge dominating exactly when
\[
N[D]=\bigcup_{v\in D}N[v]
\]
is a vertex cover of \(G\). This equivalence is used throughout the proof.

The theorem concerns the connected crown graphs \(n\ge3\).

## Proof
First we rule out sets of size \(2\).

A two-vertex set contained in one bipartition class induces no edge, so it fails the total condition. A cross-part pair
\[
\{a_i,b_i\}
\]
also induces no edge because \(a_i b_i\) is one of the deleted matching edges.

It remains to consider an adjacent cross-part pair
\[
D=\{a_i,b_j\},
\qquad i\ne j.
\]
The only vertices outside its closed neighborhood are
\[
a_j\quad\text{and}\quad b_i.
\]
Since \(i\ne j\), the edge
\[
a_jb_i
\]
belongs to the crown graph. Hence \(N[D]\) is not a vertex cover, so \(D\) is not vertex-edge dominating. Thus
\[
\gamma_{ve}^{t}(\operatorname{Cr}_n)\ge3.
\tag{1}
\]

Now choose pairwise distinct indices \(i,j,k\) and let
\[
D=\{a_i,a_j,b_k\}.
\]
Because \(k\ne i,j\), the vertex \(b_k\) is adjacent to both \(a_i\) and \(a_j\), so \(G[D]\) has no isolated vertices.

The two closed neighborhoods
\[
N[a_i]\cup N[a_j]
\]
contain every vertex of \(B\), since \(a_i\) and \(a_j\) miss different matched partners. The closed neighborhood \(N[b_k]\) contains every vertex of \(A\) except possibly \(a_k\). Therefore
\[
V(\operatorname{Cr}_n)\setminus N[D]\subseteq\{a_k\},
\]
which is independent. Hence \(N[D]\) is a vertex cover, and \(D\) is a total vertex-edge dominating set. By symmetry, every set
\[
\{a_k,b_i,b_j\}
\]
with pairwise distinct indices is also feasible. Together with (1), this proves
\[
\gamma_{ve}^{t}(\operatorname{Cr}_n)=3.
\]

For the classification, let \(D\) be any minimum set. Since \(G[D]\) has no isolated vertices, \(D\) must meet both bipartition classes. Because \(|D|=3\), it has type two vertices on one side and one on the other. Suppose
\[
D=\{a_i,a_j,b_k\},
\qquad i\ne j.
\]
Both \(a_i\) and \(a_j\) must have a neighbor inside \(D\). Their only possible selected neighbor is \(b_k\), so
\[
k\ne i,j.
\]
Thus \(i,j,k\) are pairwise distinct. The symmetric argument handles the other orientation.

There are
\[
\binom n2(n-2)
\]
sets of each orientation, so the total number is
\[
2\binom n2(n-2)=n(n-1)(n-2).
\]

## Verification
The included checker constructs each crown graph directly for
\[
3\le n\le8.
\]
It exhausts every vertex subset, tests the total condition inside the selected set, and tests vertex-edge domination through the equivalent requirement that every edge have an endpoint in \(N[D]\).

For each tested order it computes the minimum cardinality and compares the complete minimum-set family with the pairwise-distinct-index classification.

## Relationship to prior work
Total vertex-edge domination was introduced in 2017. The foundational work defines the parameter, proves NP-completeness on bipartite graphs, and develops bounds and equality results for trees.

Later work under the same parameter gives sharper tree bounds and structural tree results. A 2021 algorithmic paper proves that the minimum total vertex-edge domination problem is linear-time solvable on chain graphs and threshold graphs while remaining hard on several other graph classes. Crown graphs are not chain graphs for \(n\ge3\): any two deleted-matching indices induce a \(2K_2\).

A 2025 paper gives exact values for several graph operations and a characterization of graphs whose total vertex-edge domination number is \(2\). The searched literature did not supply the crown value or its complete minimum-set family.

The crown theorem is naturally compared with the complete bipartite graph. In
\[
K_{n,n},
\]
any selected edge is a two-vertex total vertex-edge dominating set. Deleting a perfect matching therefore raises the optimum from \(2\) to \(3\), and the missing edges force the three distinct matching indices that classify every optimum.

## Limitations
The theorem treats balanced crown graphs only. It does not classify total vertex-edge domination after deleting arbitrary matchings from \(K_{p,q}\).

The finite exhaustive check through \(n=8\) is corroborative only. The arbitrary-order theorem follows from the closed-neighborhood vertex-cover proof.

The 2021 algorithmic paper was accessible through its abstract, publication metadata, and stated chain-graph result, but its full article text was not accessible through the available route. A differently phrased or non-indexed crown treatment may therefore remain possible.

## References
1. R. Boutrig, M. Chellali, “Total vertex-edge domination,” International Journal of Computer Mathematics 95(9) (2018), 1820–1828, DOI 10.1080/00207160.2017.1343469; accepted author version posted online 16 June 2017.
2. B. Şahin, A. Şahin, “On total vertex-edge domination,” TWMS Journal of Applied and Engineering Mathematics 9(1), Special Issue (2019), 128–133.
3. N. Singhwal, P. V. S. Reddy, “Total vertex-edge domination in graphs: Complexity and algorithms,” Discrete Mathematics, Algorithms and Applications 14(7) (2022), 2250031, DOI 10.1142/S1793830922500318; published online 15 November 2021.
4. I. Majaba, R. F. Rulete, “Total Vertex-Edge Domination Number of Some Graphs,” Communications in Mathematics and Applications 16(4) (2025), 1067–1075, DOI 10.26713/cma.v16i4.3332.
