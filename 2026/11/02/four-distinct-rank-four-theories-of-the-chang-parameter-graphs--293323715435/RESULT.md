# Four distinct rank-four theories of the Chang parameter graphs

## Finding

In the first-order language with equality and undirected adjacency, the four strongly regular graphs with parameters \((28,12,6,4)\) are **pairwise equivalent at quantifier rank three and pairwise inequivalent at quantifier rank four**. These four graphs are the triangular graph \(T(8)\) and the three Chang graphs obtained from it by Seidel switching along a disjoint triangle and pentagon, a perfect matching, or an eight-cycle in \(K_8\).

More specifically, three first-order sentences of quantifier rank four, denoted \(\mathsf C\) (induced claw), \(\mathsf T\) (a triangle with a missing prescribed fourth-vertex adjacency pattern), and \(\mathsf E\) (an edge plus an isolated vertex with another missing pattern), take these respective truth vectors:

| Graph | \(\mathsf C\) | \(\mathsf T\) | \(\mathsf E\) |
| --- | --- | --- | --- |
| \(T(8)\) | false | false | false |
| Chang, switch on \(C_3\sqcup C_5\) | true | true | false |
| Chang, switch on a matching | true | false | true |
| Chang, switch on \(C_8\) | true | false | false |

A second, logically instructive fact holds: **each of the three Chang graphs realizes all eleven unlabelled induced four-vertex graphs**. Consequently, no sentence of the restricted form \(\exists x_1\exists x_2\exists x_3\exists x_4\,\theta\), with \(\theta\) quantifier-free, separates two Chang graphs. The rank-four separating sentences \(\mathsf T\) and \(\mathsf E\) use three existentially selected vertices and a universal condition on the fourth. This restricted-prefix observation does not assert indistinguishability under every existential formula with branching quantification.

## Assumptions and scope

All graphs are finite, nonempty, simple, and undirected, and only the adjacency predicate and equality are allowed. The first-order quantifier rank of a formula is the largest number of nested quantifiers on any branch. Write \(G\equiv_r H\) for agreement on every sentence of quantifier rank at most \(r\).

Label the vertices of \(K_8\) by \(0,1,\ldots,7\), and identify the twenty-eight vertices of \(T(8)\) with the unordered pairs \(ij\) where \(0\le i<j\le7\). Before switching, two different pairs are adjacent exactly when they share one endpoint. Seidel switching on a set \(S\) toggles precisely those adjacencies with one endpoint in \(S\) and the other outside \(S\). We use the three sets

\[
\begin{aligned}
S_{3+5}&=\{01,02,12,34,45,56,67,37\},\\
S_M&=\{04,15,26,37\},\\
S_8&=\{01,12,23,34,45,56,67,07\}.
\end{aligned}
\]

The classical Chang classification, as presented in the cited monograph, says these three switched graphs together with \(T(8)\) exhaust the isomorphism classes of strongly regular graphs with these parameters.

## Proof

**Three-round equivalence.** Each of the four explicit adjacency matrices has twenty-eight vertices, degree twelve, six common neighbors for any adjacent pair, and four common neighbors for any nonadjacent pair. For two distinct adjacent marked vertices, the numbers of remaining vertices adjacent to both, the first only, the second only, or neither are respectively \((6,5,5,10)\). For a distinct nonadjacent pair the corresponding numbers are \((4,8,8,6)\). All eight counts are positive. A Duplicator can therefore match the first selected vertex arbitrarily, the second while respecting equality and adjacency, and the third in exactly the required two-marked adjacency class. Hence every pair of the four graphs is equivalent at rank three.

**Explicit rank-four formulas.** Abbreviate by \(\operatorname{Distinct}(x,y,z)\) the conjunction of pairwise inequalities, and by \(x\sim y\) adjacency. Define these two quantifier-rank-one extension conditions with three free vertices:

\[
\begin{aligned}
P_{\bar x yz}(x,y,z)&:=\exists w\,[w\notin\{x,y,z\}\land w\not\sim x\land w\sim y\land w\sim z],\\
P_{xy\bar z}(x,y,z)&:=\exists w\,[w\notin\{x,y,z\}\land w\sim x\land w\sim y\land w\not\sim z].
\end{aligned}
\]

The notation \(w\notin\{x,y,z\}\) abbreviates three inequalities. Let \(\mathsf C\) assert the existence of four distinct vertices inducing a claw \(K_{1,3}\). Let

\[
\mathsf T:=\exists x\exists y\exists z\,[\operatorname{Distinct}(x,y,z)\land x\sim y\land x\sim z\land y\sim z\land \neg P_{\bar x yz}(x,y,z)].
\]

Finally let

\[
\mathsf E:=\exists x\exists y\exists z\,[\operatorname{Distinct}(x,y,z)\land x\not\sim y\land x\not\sim z\land y\sim z\land\neg P_{xy\bar z}(x,y,z)].
\]

Every displayed sentence has quantifier rank exactly four. For \(\mathsf T\), the \(C_3\sqcup C_5\)-switched graph has witness \((x,y,z)=(01,02,12)\). For \(\mathsf E\), the matching-switched graph has witness \((04,01,14)\). Direct finite enumeration of every distinct ordered triple in all four specified matrices establishes the complete truth table above, including the absence assertions. The same check finds ordered-witness counts for \(\mathsf T\) of \((0,36,0,0)\), and for \(\mathsf E\) of \((0,0,48,0)\), in table order. Direct enumeration of induced claws gives positive counts for each Chang graph and zero for \(T(8)\). Thus every pair of graphs has a rank-four distinguishing sentence.

**All four-vertex graph shapes in each Chang graph.** For each unordered four-vertex subset, encode its six potential edges and minimize that code over all twenty-four vertex permutations. Enumeration of all \(\binom{28}{4}=20475\) subsets gives ten unlabelled induced-four-vertex patterns in \(T(8)\) and all eleven possible patterns in each Chang graph. Every pattern on fewer than four distinct vertices embeds into a four-vertex pattern. Therefore any restricted four-existential-prefix sentence with a quantifier-free matrix has the same truth value in the three Chang graphs. This completes the proof.

## Verification

Two independently written complete programs accompany this result: `verify.py` uses adjacency matrices and canonical induced graph forms, and `verify_independent.cpp` uses bitset adjacency, a separately coded four-vertex canonicalizer, and full ordered-triple enumeration. Both check every vertex degree and all \(\binom{28}{2}=378\) common-neighbor counts, every ordered distinct triple for the two missing-pattern conditions, all ordered distinct quadruples for claws, and every unordered four-set for graph-shape saturation. The programs agree on the witness counts and all four truth vectors. Recorded output files are `output_python.txt` and `output_cpp.txt`.

Reproduce using `python3 verify.py` and `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. The proof of three-round equivalence is analytic; the two finite checking programs establish the specified boundary facts exhaustively, not by sampling. The code's graph labelling and switching conventions are fully specified above.

## Relationship to prior work

Chang's 1959–1960 classification and its presentation by Brouwer and Van Maldeghem classify the four strongly regular graphs, including the switching construction. The latter source explicitly notes that \(T(8)\) is claw-free while each Chang graph contains a claw; this previously establishes one of the three easy fourth-rank distinctions, not the separation of the three Chang graphs from each other. Pikhurko and Verbitsky survey first-order graph depth and observe that strongly regular graphs with common parameters are a standard obstruction to low-dimensional Weisfeiler–Leman refinement. Neither inspected source gives the two triple-extension formulas or the exact pairwise rank-three/rank-four classification reported here.

The restricted-existential-prefix saturation result is a structural refinement: induced subgraph occurrence on four vertices alone cannot distinguish the three Chang graphs, although their four-round theories differ. This does not claim equality of induced-subgraph counts or equivalence in counting logic.

## Limitations

The claim concerns exactly the four graphs with the specified parameters; it does not characterize all strongly regular graphs of arbitrary size. It is a full finite exhaustion, not a theorem about infinite families. Historical priority is not completely settled: the original Chang articles could not be inspected in full, so they might contain unindexed equivalent triple-extension information. Independent mathematical audit and external replication have not occurred. No claim is made about the precise rank of definition of any of these graphs among *all* twenty-eight-vertex graphs, only their pairwise relative distinguishing rank.

## References

1. L.-C. Chang, *The Uniqueness and Non-Uniqueness of the Triangular Association Scheme*, Science Record (Peking), 3 (1959), 604–613; and *Association Schemes of Partially Balanced Designs with Parameters ...*, Science Record (Peking), 4 (1960), 12–18. Cited for the classical classification; original full text not inspected.
2. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, Section 10.11, pp. 257–258 (2021), accessible at https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf. Inspected the complete relevant two-page section and switching/clique tables.
3. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 2010-03-25, https://arxiv.org/abs/1003.4865. Inspected introductory formal definitions and Section 5.1.5 on strongly regular graphs.
4. E. W. Weisstein, *Chang Graphs*, MathWorld, https://mathworld.wolfram.com/ChangGraphs.html. Inspected the switching descriptions and references.
