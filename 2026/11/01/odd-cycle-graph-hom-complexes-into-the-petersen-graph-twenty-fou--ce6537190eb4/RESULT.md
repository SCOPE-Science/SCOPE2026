# Odd-cycle graph-Hom complexes into the Petersen graph: twenty-four circles and rigid nine-cycles

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertices the two-element subsets of \([5]\), adjacent precisely when disjoint. Let \(C_m\) denote the simple cycle on \(m\) ordered vertices. Using the ordinary graph-Hom polyhedral CW complex, the complete homotopy types for the first three admissible odd source lengths are

\[
\operatorname{Hom}(C_5,P)\simeq\coprod^{120}\{\mathrm{pt}\},\qquad
\operatorname{Hom}(C_7,P)\simeq\coprod^{24}S^1,\qquad
\operatorname{Hom}(C_9,P)\simeq\Bigl(\coprod^{24}S^1\Bigr)\sqcup\Bigl(\coprod^{360}\{\mathrm{pt}\}\Bigr).
\]

For the natural action of \(\operatorname{Aut}(P)\cong\mathfrak S_5\), in each of the two circle-bearing cases the complete integral first-homology representation is

\[
H_1\bigl(\operatorname{Hom}(C_m,P);\mathbb Z\bigr)
\cong \operatorname{Ind}_{C_5}^{\mathfrak S_5}\mathbb Z,
\qquad m\in\{7,9\},
\]

where \(C_5\) on the right is an order-five cyclic subgroup of \(\mathfrak S_5\), acting trivially on \(\mathbb Z\). The 360 isolated maps for source length nine are precisely the based, oriented traversals of the twenty simple nine-cycles in \(P\). These are full homotopy and integral symmetry statements for this finite parameter range, not an assertion for all odd source lengths.

## Assumptions and scope

The graph \(P\) is simple and loopless. A cell of \(\operatorname{Hom}(C_m,P)\) is an \(m\)-tuple \((A_0,\ldots,A_{m-1})\) of nonempty subsets of \(V(P)\) such that each pair \((A_i,A_{i+1})\) is completely adjacent in \(P\), with subscripts modulo \(m\). Its closure is \(\prod_i\Delta(A_i)\), a product of simplices of dimension \(\sum_i(|A_i|-1)\). The zero-dimensional cells are graph homomorphisms, equivalently length-\(m\) closed walks with a marked start. Two zero-cells are joined by a one-cell exactly when they differ in one coordinate and both values are common neighbors of the images of its two source neighbors. All homology is singular homology with integral coefficients; \(\coprod\) denotes a disjoint union, not a wedge.

## Proof

**Graph structure and number of maps.** The Kneser presentation gives ten vertices and fifteen edges, each vertex having three neighbors. It has girth five and is square-free. Its adjacency spectrum consists of eigenvalues \(3\), \(1\), and \(-2\) with multiplicities one, five, and four. Thus the number of homomorphisms from \(C_m\) is the trace of its adjacency matrix to the \(m\)-th power,
\[
N_m=3^m+5+4(-2)^m,
\]
which equals \(120\), \(1680\), and \(17640\) for \(m=5,7,9\). A second, independent enumeration recursively constructs the same closed walks from the explicit disjointness relation.

**Exact component enumeration.** Index the ten vertices by two-subsets of \([5]\). For each length-\(m\) closed walk \(w\) and each coordinate \(i\), consider every replacement value in \(N_P(w_{i-1})\cap N_P(w_{i+1})\). Joining the old and replaced walks when different yields precisely the one-skeleton, since a one-dimensional Hom cell changes one factor from a singleton to two values. Exhaustive union-find on this finite graph yields the following complete component-size distributions:

| Source | Number of zero-cells | Connected components by zero-cell count |
| --- | ---: | --- |
| \(C_5\) | 120 | 120 components of size 1 |
| \(C_7\) | 1,680 | 24 components of size 70 |
| \(C_9\) | 17,640 | 24 components of size 720 and 360 components of size 1 |

The supplied checker constructs each replacement from the graph definition and checks these results. There is no assumption based on the expected homotopy type in the connectivity algorithm.

**Exact component Euler characteristics.** Two complete, independently formulated CW-cell enumerations agree. The first starts with each singleton-valued homomorphism and repeatedly inserts an allowed value into one coordinate until no further valid product cells exist. Every cell is reached: select one value in each coordinate of an arbitrary cell, then insert the remaining values one at a time; each intermediate product is a subcell of the target. The second uses the 50 distinct nonempty subsets of neighborhoods in the Petersen graph as transfer states, with transitions between two states exactly when every cross pair is an edge. There are 110 ordered valid transitions. Closed length-\(m\) state walks, weighted by the total sum of subset cardinalities minus one, enumerate all CW cells independently.

The cell vectors, from dimension zero upward, are
\[
\begin{aligned}
 m=5 &: (120),\\
 m=7 &: (1680,2520,840),\\
 m=9 &: (17640,45360,44280,19440,3240).
\end{aligned}
\]

For \(m=7\), each of the 24 components has cell vector \((70,105,35)\) and Euler characteristic \(70-105+35=0\). For \(m=9\), each of the 24 nontrivial components has cell vector \((720,1890,1845,810,135)\), again with Euler characteristic zero; each of the 360 remaining components is a single zero-cell. The checker classifies every CW cell by the connected component of any of its vertices and confirms these assertions, as well as an independent transfer-matrix count of the global cell vector.

**From Euler characteristic to homotopy.** By Matsushita's theorem for square-free codomains (Theorem 1.2 and Corollary 5.9 of the cited paper), each connected component of \(\operatorname{Hom}(G,H)\) is homotopy equivalent to a point or to \(S^1\) whenever \(G\) is nonbipartite and \(H\) is square-free. Each source cycle here is odd, and the Petersen graph is square-free. Thus a component of Euler characteristic zero is a circle and a singleton component is a point. This proves all three homotopy types. In particular there are no higher homology groups and no integral torsion.

**Automorphism representation.** The five four-element stars of two-subsets sharing a fixed element of \([5]\) are exactly the maximum independent sets of \(P\). Any graph automorphism permutes those stars and is determined by that permutation, proving \(\operatorname{Aut}(P)=\mathfrak S_5\). Exhaustive action of the 120 ground-set permutations on a representative nontrivial Hom component shows that the orbit comprises all 24 circle components and its stabilizer has order five. Since a subgroup of \(\mathfrak S_5\) of order five is cyclic, the stabilizer is \(C_5\). Its action on the integral first homology of one circle is a homomorphism \(C_5\to\{\pm1\}\), necessarily trivial. Translating an integral generator therefore yields the asserted induced integral \(\mathfrak S_5\)-module.

**The rigid nine-cycle maps.** A separate simple-cycle enumeration finds exactly twelve cycles of length five, no cycles of length seven, and twenty cycles of length nine in \(P\), counting each undirected cycle once. Exactly 360 isolated \(C_9\)-homomorphisms are found; each is injective on vertices, hence traverses a nine-cycle. There are exactly \(20\cdot 2\cdot9=360\) based, oriented traversals. This exhausts the isolated components.

## Verification

Run `python3 verify.py` with Python 3.9 or later; no nonstandard packages or network access are required. The checker enumerates all homomorphisms and CW cells, independently reproduces every global cell vector by a 50-state transfer calculation, checks component-wise Euler characteristics, and enumerates the full natural \(\mathfrak S_5\)-action. It also compares the closed-walk counts with the adjacency-spectrum formula, independently counts simple five-, seven-, and nine-cycles, and checks the isolated-map characterization. All asserted finite checks were executed on the embedded code. The external square-free graph-Hom theorem is a cited mathematical premise, not proved by a finite calculation.

## Relationship to prior work

Matsushita, *Hom complexes of graphs whose codomains are square-free* (first public arXiv version December 26, 2024; final journal version 2026), proves the general point-or-circle component restriction used above for nonbipartite source graphs and square-free targets. Its accessible full text was checked at the introductory statements and the main theorems in Section 5, and was text-searched for the Petersen graph without an identified instance of the complete three-length classification. The general restriction itself neither specifies the component counts nor determines the induced \(\mathfrak S_5\)-module here.

Fujii, Kimura and Nozaki independently proved a related square-free-codomain classification and an algorithm to classify components (arXiv:2412.19039). The publicly accessible abstract does not provide these exact finite counts; the complete preprint was unavailable for material comparison in the present check, so an unlocated equivalent worked example remains a genuine literature risk. The computation concerns ordinary graph-Hom polyhedral complexes, not graph coloring counts without reconfiguration or the two-point-source neighborhood complex. A search for exact pairs and equivalent Kneser-graph notation found no covering formula, but absence from search results is not a uniqueness proof.

## Limitations

The homotopy classifications are proved only for source lengths five, seven and nine, not for all odd cycles. The integral representation statement is about first homology, not an equivariant homotopy equivalence. The proof depends on the cited general theorem of Matsushita and on the exhaustive finite calculations whose complete implementation is supplied. The material of the independent companion preprint was not fully accessible; the originality judgment remains subject to that source and to unindexed literature. No independent external validation of this computation or manuscript has been performed.

## References

1. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (first version 2024-12-26); Journal of Combinatorial Theory Series B **178** (2026), 267–293. https://arxiv.org/abs/2412.19144 . Main theorem: Theorem 1.2 and Corollary 5.9.
2. S. Fujii, K. Kimura and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039 (2024). https://arxiv.org/abs/2412.19039 .
