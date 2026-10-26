# Ten rank-three theories of cyclically oriented complete tripartite digraphs

## Finding

For positive integers \(a,b,c\), let \(D(a,b,c)\) be the loopless directed graph with three nonempty, pairwise disjoint independent vertex sets \(A,B,C\) of sizes \(a,b,c\). Every vertex of \(A\) sends an arc to every vertex of \(B\), every vertex of \(B\) sends an arc to every vertex of \(C\), and every vertex of \(C\) sends an arc to every vertex of \(A\); there are no other arcs. This is an independent-set blow-up of the directed triangle. Work in the first-order language consisting of equality and the single directed-edge predicate \(E\), without constants or predicates identifying the parts.

For a positive integer \(t\) and cutoff \(h\), write \(t\wedge h=\min(t,h)\). Define the finite *oriented footprint*
\[
\mathcal F(a,b,c)=\left\{\bigl(a\wedge3,b\wedge2,c\wedge2\bigr),\ \bigl(b\wedge3,c\wedge2,a\wedge2\bigr),\ \bigl(c\wedge3,a\wedge2,b\wedge2\bigr)\right\},
\]
where braces denote an ordinary set rather than a multiset.

**Theorem.** For all positive integers \(a,b,c,a',b',c'\),
\[
D(a,b,c)\equiv_3 D(a',b',c')\quad\Longleftrightarrow\quad
\mathcal F(a,b,c)=\mathcal F(a',b',c').
\]
Here \(\equiv_3\) means agreement on all first-order sentences of quantifier rank at most three. The family has **exactly ten** such equivalence classes. Its smallest representatives, up to cyclic permutation of the ordered part-size triple, are listed below. Each footprint is written as a set of ordered triples.

| Smallest representative \((a,b,c)\) | Oriented footprint \(\mathcal F\) | Number of vertices |
| --- | --- | ---: |
| \((1,1,1)\) | \(\{(1,1,1)\}\) | 3 |
| \((1,1,2)\) | \(\{(1,1,2),(1,2,1),(2,1,1)\}\) | 4 |
| \((1,1,3)\) | \(\{(1,1,2),(1,2,1),(3,1,1)\}\) | 5 |
| \((1,2,2)\) | \(\{(1,2,2),(2,1,2),(2,2,1)\}\) | 5 |
| \((1,2,3)\) | \(\{(1,2,2),(2,2,1),(3,1,2)\}\) | 6 |
| \((1,3,2)\) | \(\{(1,2,2),(2,1,2),(3,2,1)\}\) | 6 |
| \((1,3,3)\) | \(\{(1,2,2),(3,1,2),(3,2,1)\}\) | 7 |
| \((2,2,2)\) | \(\{(2,2,2)\}\) | 6 |
| \((2,2,3)\) | \(\{(2,2,2),(3,2,2)\}\) | 7 |
| \((3,3,3)\) | \(\{(3,2,2)\}\) | 9 |

The sole additional identification beyond cyclic rotation and truncation of each size at three is
\[
D(2,2,3)\equiv_3 D(2,3,3).
\]
Every graph in this family has a rank-three-equivalent representative on at most nine vertices, and **nine is the least possible uniform bound within the family**.

## Assumptions and scope

All three parts must be nonempty; all sizes are arbitrary positive integers. The arcs are oriented cyclically rather than bidirectionally. Reversing the orientation is not an allowed named operation; exchanging the parts by a *cyclic rotation* gives an isomorphic digraph, while swapping two part names is generally not an isomorphism. The logic has unrestricted first-order quantification but quantifier rank at most three, and it does **not** include counting quantifiers, colors naming parts, a global linear order, or a symmetric adjacency predicate replacing \(E\).

The classification is internal to the directed-triangle blow-up family. It is not a classification of all digraphs of quantifier rank three, nor a claim that the listed representatives define themselves within the class of all digraphs at this rank.

## Proof

**1. Rooted two-round profile.** Fix a vertex \(x\in A\). Relative to \(x\), the universe splits into four disjoint regions: the singleton \(\{x\}\); the other \(a-1\) vertices of \(A\); the \(b\) out-neighbors of \(x\) in \(B\); and the \(c\) in-neighbors of \(x\) in \(C\). These regions are definable relative to \(x\) by equality, non-adjacency, \(E(x,y)\), and \(E(y,x)\), respectively. All arcs between these regions are fixed by the directed-triangle template; inside each non-singleton region there are no arcs.

In the pointed language with \(x\) named, two additional rounds detect whether the region of non-neighbors other than \(x\) has size \(0\), \(1\), or at least \(2\). Equivalently, they detect \(a\wedge3\). They likewise detect whether each of the two neighbor regions has size \(1\) or at least \(2\), equivalently \(b\wedge2\) and \(c\wedge2\), because those regions are nonempty. For example, the first distinction uses \(\exists y\,(y\ne x\land\neg E(x,y)\land\neg E(y,x))\); the second uses two distinct witnesses satisfying the same non-neighbor condition. Two distinct out-neighbors are detected by \(\exists y\exists z\,(y\ne z\land E(x,y)\land E(x,z))\), with the analogous formula for in-neighbors. All have quantifier rank at most two over the named point.

Conversely, suppose two pointed graphs have the same triple \((a\wedge3,b\wedge2,c\wedge2)\) relative to their respective distinguished vertices. In a two-round Ehrenfeucht–Fraïssé game, Duplicator sends each selected vertex to a vertex of the corresponding one of these four regions, reuses an earlier image when a vertex is repeated, and otherwise chooses an unused vertex in that region. The truncated cardinalities ensure that this is always possible for at most two further selections. All equalities and directed-edge relations are then preserved. Thus the **complete pointed rank-two theory** of \(x\in A\) is characterized by precisely \((a\wedge3,b\wedge2,c\wedge2)\). The same reasoning applies at vertices of \(B\) and \(C\) with cyclically permuted parameters.

**2. Removing the root.** Two unpointed structures are rank-three equivalent exactly when they realize the same *set* of pointed rank-two theories. Indeed, if the sets agree, Duplicator can answer the first move with a vertex of the same pointed rank-two type and win the next two rounds. Conversely, if a pointed type is realized in just one structure, Spoiler selects such a vertex first and then applies the winning two-round strategy against any response. By step 1, the set of pointed types realized by \(D(a,b,c)\) is exactly its oriented footprint \(\mathcal F(a,b,c)\). This proves the displayed equivalence for all positive part sizes, without a finite-size assumption.

**3. Enumerating footprints.** Each individual part size can be replaced by its minimum with three without altering its footprint. The resulting \(3^3=27\) labeled triples, modulo the three cyclic rotations, have eleven orbits (Burnside's count is \((27+3+3)/3=11\)). Direct substitution into the three-term footprint formula gives the ten *distinct* sets displayed in the table. The only two cyclic orbits with the same footprint are represented by \((2,2,3)\) and \((2,3,3)\), both producing \(\{(2,2,2),(3,2,2)\}\). The other nine entries are pairwise distinct, which is verifiable directly from the displayed sets. Thus the number of rank-three types is exactly ten.

**4. Sharp representative bound.** The table provides representatives of sizes at most nine. Conversely, a footprint equal to \(\{(3,2,2)\}\) occurs only if all three part sizes are at least three: every root must have at least three vertices in its own part, and no root may have a smaller first coordinate. Thus any representative of the class of \(D(3,3,3)\) has at least nine vertices. The bound is sharp.

## Verification

The standalone `verify_cyclic_tripartite.py` implements two mathematically independent finite tests. First, it forms exact recursively defined atomic/Hintikka characters over **every vertex** of the twenty-seven capped structures and computes their rank-one, rank-two and rank-three equivalence partitions. Second, it implements the direct two-structure Ehrenfeucht–Fraïssé game with Spoiler permitted to move in either graph on every round. The latter uses one unselected representative per clone class, which is exhaustive under permutations of as-yet-unselected vertices within each part. The programs agree on all \(378\) unordered pairs (including self-pairs) of capped structures at ranks two and three. The verifier separately checks the rooted-profile formula, all \(729\) ordered capped pairs, truncation boundaries, the sole merger, and the sharp nine-vertex representative. Reproduce by running `python3 verify_cyclic_tripartite.py`; the captured output is in `verify_output.txt`.

These finite computations serve as independent checks of the finite table and the game characterization. The theorem for **arbitrary** part sizes is established by steps 1 and 2 of the proof; no finite extrapolation is used.

## Relationship to prior work

Pikhurko, Veith and Verbitsky (2003), especially Section 8, develop first-order quantifier-rank methods for arbitrary binary relational structures, including directed graphs. Their bounds concern identification and distinguishability broadly; they do not state the present exact rank-three classification or the oriented footprint.

Rabinovich's generalized-sum composition theorem (2007, with an earlier dated manuscript) supplies a general framework for first-order properties of compound structures. Its applications include complete bipartite graphs and cycles, but the inspected material does not calculate the ten distinct rank-three types of cyclic directed-triangle blow-ups or identify the exceptional merger. The general composition principle is consistent with, but does not itself supply, the necessary-and-sufficient small-rank footprint proved above.

Results on first-order depth of *undirected* complete multipartite graphs concern a different relation signature. Passing from this directed graph to its underlying undirected graph discards the cyclic orientation, so those depth formulas do not imply the equivalence above. Literature searches using the aliases “cyclic complete tripartite orientation,” “directed triangle blow-up,” and “lexicographic/generalized sum” did not locate a direct covering statement. Absence from indexed searches is not proof of historical priority.

## Limitations

The classification holds only in the specified pure directed-edge language and exactly at quantifier rank three. Adding named parts, counting quantifiers, or considering arbitrary oriented complete multipartite graphs changes the question. Independence from prior work has not been externally certified; an equivalent theorem might exist in literature not indexed or accessible in the searches. The accompanying verification is finite, although the general proof is not. Independent mathematical audit has not been performed.

## References

1. O. Pikhurko, H. Veith, and O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041, initially public 2003-11-04. https://arxiv.org/abs/math/0311041
2. A. Rabinovich, *Composition Theorem for Generalized Sum*, *Fundamenta Informaticae* 79 (2007), 137–167. https://doi.org/10.3233/FUN-2007-791-207
