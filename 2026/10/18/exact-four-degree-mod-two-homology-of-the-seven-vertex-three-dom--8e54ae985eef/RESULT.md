# Exact four-degree mod-two homology of the seven-vertex three-domination complex

## Finding
For the simplicial complex \(D_{7,3}\) of graphs on the labeled vertex set \(\{0,1,\ldots,6\}\) with domination number at least three, its reduced homology satisfies
\[
\widetilde H_j(D_{7,3};\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{106},&j=6,\\
\mathbb F_2^{623},&j=7,\\
\mathbb F_2,&j=8,\\
\mathbb F_2^{35},&j=9,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus this natural seven-vertex graph-property complex has nonzero reduced mod-two homology in four consecutive degrees. The claim concerns homology over \(\mathbb F_2\), not an integral or homotopy classification.

## Assumptions and scope
Let \(V=\{0,1,\ldots,6\}\). A graph \(G=(V,E)\) has domination number \(\gamma(G)\), the smallest cardinality of a subset \(S\subseteq V\) such that every vertex outside \(S\) is adjacent to at least one vertex of \(S\). The complex \(D_{7,3}\) has the \(\binom72=21\) possible unordered edges as vertices; its simplices are precisely the nonempty edge sets \(E\) for which \(\gamma(V,E)\geq3\), with the empty face included by convention. This property is downward closed. All homology here is reduced simplicial homology with \(\mathbb F_2\) coefficients. The combinatorial claim is exhaustive for the fixed set of seven graph vertices, not a statement about other orders.

## Proof
Represent each simple graph by a \(21\)-bit edge mask. A pair \(\{a,b\}\subset V\) dominates a graph exactly when every \(c\in V\setminus\{a,b\}\) is adjacent to \(a\) or \(b\). A singleton dominator extends to a dominating pair because \(|V|=7\), hence \(\gamma(G)\geq3\) if and only if no pair dominates. Consequently an exhaustive enumeration of all \(2^{21}\) masks using the \(21\) pair tests and five remaining vertices per pair enumerates precisely all faces. The number of faces by edge-set cardinality \(k=0,\ldots,12\) is
\[
(1,21,210,1330,5985,19782,47187,76590,76860,43330,13566,2310,105).
\]
There are exactly \(287277\) faces including the empty face; the maximum simplex dimension is \(11\). The reduced Euler characteristic obtained by alternating this face vector is \(-551\).

The accompanying complete verifier constructs an explicit simplicial Morse matching as follows. Excluding the empty face, examine each of the 21 edge coordinates in a fixed order. At each coordinate, match every still-unmatched pair of faces of the form \(F,F\cup\{e\}\), when both exist. This is a definite finite matching, specified exactly by the source program. Reverse every matched cover arrow in the Hasse diagram and orient each remaining cover arrow from upper face to lower face. The program constructs all \(2{,}113{,}692\) cover relations among \(287{,}276\) nonempty faces; its topological sort visits all of those faces, proving that this matching is acyclic. It leaves one critical vertex and respectively \(162,941,269,41\) critical faces in dimensions \(6,7,8,9\), with no other critical faces.

The algebraic Morse boundary is computed directly over \(\mathbb F_2\). For each degree, let \(P\) send a critical face to its standard critical generator and a matched upper face to zero. If a noncritical face \(u\) is paired with a face \(v\) one dimension above, the simplicial boundary relation gives
\[
P(u)=\sum_{\substack{w\subset v,\,|w|=|u|\\w\ne u}}P(w)
\quad\text{over }\mathbb F_2.
\]
Acyclicity makes this recurrence well founded. Applying \(P\) to the simplicial boundary of every critical generator produces the exact reduced Morse differential. Its four consecutive ranks from dimension \(6\) through dimension \(9\), mapping down by one dimension, are \(0,56,262,6\). Since the critical chain-group dimensions in these degrees are \(162,941,269,41\), the resulting Betti numbers are respectively \(162-56=106\), \(941-56-262=623\), \(269-262-6=1\), and \(41-6=35\). The single critical vertex yields no reduced degree-zero homology. There are no critical cells in other dimensions and thus no homology there.

As an independent choice of discrete gradient, the verifier repeats all operations with the 21 edge coordinates in reverse order. It yields one critical vertex, and critical dimensions \(6,7,8,9\) with counts \(161,760,85,37\). The second complete Hasse acyclicity check succeeds. Its corresponding boundary ranks are \(0,55,82,2\), giving exactly the same four reduced Betti numbers. Both exact Morse computations are finite, not probabilistic or sampled.

## Verification
Compile the included standalone file using `g++ -std=c++17 -O2 verify_d73.cpp -o verify_d73`. Run `./verify_d73` and `./verify_d73 --reverse`. Each invocation enumerates all graph masks, checks every nonempty face and every covering relation, performs a complete topological sort of the modified Hasse graph, constructs the exact \(\mathbb F_2\) Morse differential, and independently checks its expected Betti numbers. Both paths must end with `VERIFY_OK`. Their face-vector alternating sum agrees with \(-551=106-623+1-35\). No external data files or unpublished numerical tables are required.

## Relationship to prior work
González and Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number* (arXiv:1901.07130, publicly available from January 22, 2019), define this family and prove a uniform wedge-of-two-spheres theorem for \(D_{n,n-2}\) (Theorem 1.1), and a separate classification of \(D_{5,2}\) (Proposition 1.3). Their Section 1 and Problem 1.4 discuss the unresolved greater complexity of the remaining domination filtration and note an Euler-characteristic computation for \(D_{6,3}\). Those results do not determine \(\widetilde H_*(D_{7,3};\mathbb F_2)\), whose parameter has \(3<7-2\). Other publicly available calculations of \(D_{6,3}\) determine a different six-vertex complex; their Betti numbers cannot imply this seven-vertex calculation. The present contribution is the exact four-degree mod-two classification, not a claim that previous work did not initiate this program.

## Limitations
This is one finite complex with exactly seven labeled graph vertices; there is no induction or claim for larger sizes, no calculation of persistence maps, no identification of integral torsion, and no homotopy equivalence asserted. Agreement of two Morse computations, face counts, and Euler characteristics does not supply independent external certification. Published-coverage searches cannot rule out all unindexed equivalent results.

## References
1. Jesús González and Teresa I. Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number*, arXiv:1901.07130, first version January 22, 2019; see Theorem 1.1, Proposition 1.3, Problem 1.4, and Section 2. https://arxiv.org/abs/1901.07130
2. Previously published computation, *A mixed-dimensional sphere wedge for \(D_{6,3}\)*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-mixed-dimensional-sphere-wedge-for-d-6-3--55d89ec4bab2 (six-vertex case; distinct parameters).
3. Previously published computation, *Mixed-dimensional mod-two homology of \(D_{6,3}\)*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mixed-dimensional-mod-2-homology-of-d-6-3--9a3a7140d738 (six-vertex case; distinct parameters).
