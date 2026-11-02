# Twelve three-round theories of finite 2-regular graphs

## Finding

Let \(G\) and \(H\) be **nonempty finite simple undirected graphs in which every vertex has degree two**, in the signature consisting only of equality and a binary adjacency relation \(E\). Write \(G\equiv_3H\) when the graphs satisfy the same first-order sentences of quantifier rank at most three (equivalently, Duplicator wins the three-round Ehrenfeucht–Fraïssé game).

Every such graph is a disjoint union of cycles \(C_m\), \(m\ge3\). For a graph of at least seven vertices, define its cycle-presence vector
\[
\chi(G)=(\mathbf1_{C_3\text{ is a component}},\mathbf1_{C_4\text{ is a component}},\mathbf1_{C_m\text{ is a component for some }m\ge5}).
\]
Then **the complete classification** is
\[
G\equiv_3H\quad\Longleftrightarrow\quad
\begin{cases}
G\cong H,& |V(G)|,|V(H)|\le6,\\
\chi(G)=\chi(H),& |V(G)|,|V(H)|\ge7.
\end{cases}
\]
There are no equivalences between a graph of at most six vertices and one of at least seven. The five small singleton classes are \(C_3,C_4,C_5,C_6,C_3\sqcup C_3\); the seven further classes are indexed by the seven nonzero Boolean triples \(\chi\).

Every class has a representative of order at most \(12\), and this is sharp. The class \(\chi=(1,1,1)\) has the unique smallest representative \(C_3\sqcup C_4\sqcup C_5\) of order \(12\). In particular, \(C_7\equiv_3 C_5\sqcup C_5\) but \(C_5\not\equiv_3 C_7\).

## Assumptions and scope

Graphs are finite, nonempty, loopless, without multiple edges, and undirected; every vertex has degree exactly two. The only nonlogical relation is undirected adjacency \(E\), with **no** constants, orientation, vertex colors, component symbols, counting quantifiers, or order. The quantifier-rank convention is the maximum number of nested first-order quantifiers; conjunctive sibling quantifiers do not add their ranks. All statements are exact for every admissible graph order and cycle multiplicity, not only for connected graphs.

## Proof

**1. One remaining round after two named vertices.** Fix a graph \(G\) with \(N=|V(G)|\ge7\). For every ordered pair \((x,y)\), at most six vertices belong to \(\{x,y\}\cup N_G(x)\cup N_G(y)\); hence there exists a vertex \(z\) different from both and adjacent to neither. For an ordered pair, the complete atomic information obtainable by selecting one further vertex consists of whether the selected vertex equals \(x\) or \(y\), and (for a new vertex) its two adjacency bits to \(x,y\). Thus the one-round type of \((x,y)\) is determined exactly by the following six pair classes:

* \(Z\): \(x=y\); two choices for a distinct \(z\), namely adjacent or nonadjacent.
* \(T\): distinct adjacent vertices on a triangle \(C_3\); a third vertex adjacent to both is available and one-sided neighbors are unavailable.
* \(E_0\): distinct adjacent vertices not on a triangle; each of the two one-sided neighbor patterns is available and a common neighbor is unavailable.
* \(Q\): distinct nonadjacent vertices with two common neighbors; these are the opposite vertices of a \(C_4\). No one-sided neighbor is available.
* \(P\): distinct nonadjacent vertices with exactly one common neighbor; both one-sided neighbor patterns are available. Such pairs are distance two in a cycle of length at least five.
* \(F\): distinct nonadjacent vertices without a common neighbor; both one-sided neighbor patterns are available.

All six classes are mutually distinguishable by their atomic information and possible third-vertex adjacency patterns. In every case the \((0,0)\) pattern for a distinct third vertex is available by \(N\ge7\). There are no other pair classes: each vertex has exactly two neighbors; for nonadjacent pairs, the only possible common-neighbor counts are zero, one, or two. Two nonadjacent vertices with identical two-element neighborhoods lie opposite in a \(C_4\). For adjacent vertices, the two other neighbors coincide precisely in a triangle.

**2. Two remaining rounds after one selected vertex.** In the game recursion, a vertex's two-round type is exactly the set of one-round types of \((x,y)\) as \(y\) varies through \(V(G)\). The preceding classification gives:
\[
\begin{array}{c|c}
\text{component of }x&\{\text{one-round pair classes realizable from }x\}\\\hline
C_3&\{Z,T,F\}\\
C_4&\{Z,E_0,Q,F\}\\
C_m,\ m\ge5&\{Z,E_0,P,F\}
\end{array}
\]
For a vertex on \(C_3\), \(C_4\), or \(C_5\), the presence of an \(F\)-partner is guaranteed because \(N\ge7\) forces another component. For \(C_m\) with \(m\ge6\), a vertex at cyclic distance at least three supplies an \(F\)-partner even when the graph is connected. Every other listed pair class occurs directly within the specified cycle. The three displayed vertex types are distinct.

**3. Zero selected vertices and three remaining rounds.** By the standard exact Ehrenfeucht–Fraïssé/quantifier-rank recurrence, a graph's three-round type is the set of all two-round vertex types it realizes. By Step 2 this is precisely the nonempty set of component kinds \(C_3\), \(C_4\), and \(C_m\) with \(m\ge5\), or equivalently \(\chi(G)\). This proves equivalence when \(N\ge7\) and equality of vectors.

**4. Separation and small orders.** The rank-three sentence
\[
\exists x\,\exists y\,\forall z\,\bigl(z=x\lor z=y\lor E(z,x)\lor E(z,y)\bigr)
\]
asserts a dominating pair. Since two vertices of a 2-regular graph dominate at most six vertices, it is false at every order at least seven. At orders three through six the only graphs are \(C_3,C_4,C_5,C_6,C_3\sqcup C_3\); each has such a pair: any pair in \(C_3\), opposite vertices in \(C_4\), distance-two vertices in \(C_5\), opposite vertices in \(C_6\), or one vertex from each triangle, respectively.

These five graphs are pairwise distinguishable at rank at most three. The existence of a triangle separates the two triangle-containing cases from the three triangle-free cases; among the former, a nonadjacent pair exists only in \(C_3\sqcup C_3\). Among the latter, \(C_4\) is the unique graph with distinct nonadjacent twins \(x,y\), expressible by
\[
\exists x\,\exists y\,[x\ne y\land\neg E(x,y)\land\forall z\,(E(x,z)\leftrightarrow E(y,z))],
\]
whereas \(C_5\) is separated from \(C_6\) because every nonadjacent pair in \(C_5\) has a common neighbor, while \(C_6\) has an opposite pair with none.

For large graphs, each bit of \(\chi\) has a rank-three existential witness. The first is existence of a triangle. The second is existence of the nonadjacent-twin pair just displayed. The third is the sentence
\[
\exists x\,\exists y\,\bigl[x\ne y\land\neg E(x,y)\land
(\exists z\,[E(x,z)\land E(y,z)])\land
(\exists z\,[E(x,z)\land\neg E(y,z)])\bigr],
\]
which holds exactly when a cycle of length at least five occurs: it requests a nonadjacent pair with a common neighbor and a one-sided neighbor. Its rank is three because the two innermost existential quantifiers occur in separate conjuncts. Consequently the seven large classes are pairwise distinguishable, and Step 3 gives the converse.

**5. Optimal representatives.** The seven large vectors have smallest representatives:
\[
\begin{array}{c|c|r}
\chi &\text{representative}&\text{vertices}\\\hline
(0,0,1)&C_7&7\\
(1,1,0)&C_3\sqcup C_4&7\\
(0,1,0)&C_4\sqcup C_4&8\\
(1,0,1)&C_3\sqcup C_5&8\\
(0,1,1)&C_4\sqcup C_5&9\\
(1,0,0)&C_3\sqcup C_3\sqcup C_3&9\\
(1,1,1)&C_3\sqcup C_4\sqcup C_5&12
\end{array}
\]
Each minimum follows from the required cycle lengths and the constraint \(N\ge7\); these are attained by the displayed graphs. The last vector requires disjoint cycles with at least \(3+4+5=12\) vertices, proving global sharpness.

## Verification

`verify_2regular_types.py` independently constructs adjacency matrices for every partition of each order from three through 24 into cycle lengths at least three. It recursively computes rank-zero atomic triple types, rank-one pair extension sets, rank-two vertex extension sets, and rank-three sentence types, with repetitions allowed. It confirms that all 572 tested graphs fall into exactly the twelve classes above and that the classification criterion separates different types.

`verify_2regular_game.py` implements the two-sided adversarial Ehrenfeucht–Fraïssé minimax game without invoking the type-classification code. It checks pairwise non-equivalence for all twelve minimal representatives and ten additional claimed large-graph equivalences. Both scripts need only Python's standard library and can be run directly. The infinite proof uses Steps 1–5, not finite extrapolation.

## Relationship to prior work

Brown and Hoshino (2007), Theorem 4.9, classify \(k\)-round equivalence of **single** undirected cycles and give the three-round connected-family stabilization at length seven. The present result agrees on that connected subfamily but treats **all disjoint unions**, which the cited theorem does not classify. In particular, the newly classified comparison \(C_5\sqcup C_5\equiv_3 C_7\) does not follow by substituting equivalent connected components, because \(C_5\not\equiv_3C_7\).

Kopczyński and Tan (2013/2014) study the spectra of **two-variable logic with counting** through regular and biregular graph realizability; that does not provide rank-three equivalence classes in ordinary first-order adjacency logic. General Ehrenfeucht–Fraïssé methods supply the language for the proof, but no covering statement was found in the inspected literature or research-index comparison.

## Limitations

The theorem applies only to finite, nonempty, simple degree-two graphs and first-order adjacency at rank three. It makes no claim about higher rank, graphs of smaller or larger degree, orientation, marked vertices, or counting logic. Historical priority cannot be exhaustively certified from accessible sources; in particular an older Brown–Woodrow technical report was not available for full-text inspection. These limitations do not affect the self-contained classification proof.

## References

1. Jason Brown and Richard Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, especially Theorem 4.9 and the final discussion. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf (publisher date 2007-04-30).
2. Eryk Kopczyński and Tony Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829 (first submitted 2013-04-03; later journal version, SIAM J. Comput. 2015), Sections 1, 2, and 5. https://arxiv.org/html/1304.0829v4.
3. Heinz-Dieter Ebbinghaus and Jörg Flum, *Finite Model Theory*, Springer, 1995 (standard Ehrenfeucht–Fraïssé game recurrence; bibliographic reference, not represented as a source of the new classification).
