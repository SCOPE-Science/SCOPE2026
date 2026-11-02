# Eight three-round theories of Cartesian products of finite cycles

## Finding

Let \(d\ge 1\), let \(n_1,\ldots,n_d\ge 3\) be integers, and let
\[
T(n_1,\ldots,n_d)=C_{n_1}\square\cdots\square C_{n_d}
\]
be the undirected Cartesian graph product of the simple cycles, with vertices the tuples of residues, two tuples adjacent exactly when they differ in one coordinate by a cyclic step of one. In the first-order language of equality and this **single unlabelled adjacency relation**, there are precisely **eight** equivalence classes under agreement on all sentences of quantifier rank at most three:

| Class | Exact condition on the list of factors | Smallest representative |
| --- | --- | --- |
| I | \(d=1,n_1=3\) | \(C_3\) |
| II | \(d=1,n_1=4\) | \(C_4\) |
| III | \(d=1,n_1=5\) | \(C_5\) |
| IV | \(d=1,n_1=6\) | \(C_6\) |
| V | \(d=1,n_1\ge7\), **or** \(d\ge2\) and every \(n_i\ge4\) | \(C_7\) |
| VI | \(d=2\) and \(n_1=n_2=3\) | \(C_3\square C_3\) |
| VII | \(d\ge3\) and every \(n_i=3\) | \(C_3\square C_3\square C_3\) |
| VIII | \(d\ge2\), at least one \(n_i=3\), and at least one \(n_j\ge4\) | \(C_3\square C_4\) |

Any two listed products agree through rank three **if and only if** they are in the same row. Every such graph has an equivalent product on at most \(27\) vertices, and \(27\) is optimal among representatives in this family because the smallest graph in class VII has \(3^3=27\) vertices. In particular the seven-cycle is rank-three equivalent to Cartesian tori of arbitrarily large dimension and degree whenever all factor lengths are at least four.

## Assumptions and scope

The graphs are finite, simple, loopless and undirected; each factor is an ordinary simple cycle of length at least three. The dimension \(d\) and the cycle lengths vary independently without an upper bound. No factor names, coordinate maps, constants, counting quantifiers, graph distance relations or distinguished vertices are part of the signature. The notation \(G\equiv_3 H\) means agreement on every first-order sentence of quantifier rank at most three, equivalently that the second player wins the three-round Ehrenfeucht–Fraïssé game.

## Proof

**Step 1: exact pair spectra for vertex-transitive graphs.** For distinct vertices \(u,v\) define \(e(u,v)\in\{0,1\}\) to be their adjacency indicator and
\[
S(u,v)=\{(e(u,w),e(v,w)):w\ne u,v\}\subseteq\{00,01,10,11\}.
\]
Write \(\Sigma(G)=\{(e(u,v),S(u,v)):u\ne v\}\). For any two finite nonempty vertex-transitive simple graphs with at least two vertices,
\[
G\equiv_3 H\quad\Longleftrightarrow\quad\Sigma(G)=\Sigma(H).
\]
For sufficiency, match the first selected vertices arbitrarily; transitivity makes the rooted possibilities independent of their locations. If the second selected vertex repeats the first, repeat in the other graph and match the third using the presence of an edge or a nonedge, both encoded by \(\Sigma\). Otherwise match the second selection by a pair with identical \((e,S)\); the third is then matched by exactly the appropriate one of the four pattern witnesses, or by repeating either selected vertex. All equality and adjacency relations are preserved. Conversely, if a pair type is available only on one side, the first two rounds can select it there; every possible response with the required adjacency in the other graph has some third-vertex pattern missing on one side. The third round reveals the difference. The same conclusion follows by writing a depth-three sentence specifying existence of a pair with precisely its four allowed third-vertex patterns. Thus the spectra are an exact invariant, not merely a necessary test.

**Step 2: all products with at least two factors.** Each product is vertex-transitive under coordinate translations, is regular of degree \(2d\), and has \(N=\prod_i n_i\) vertices. Distinct vertices have at most two common neighbors: a common neighbor of an adjacent pair comes only from a triangular factor \(C_3\); common neighbors of a nonadjacent pair amount to two-step paths, of which at most two exist in a Cartesian product of simple cycles. Consequently, after fixing any distinct \(u,v\), there are always vertices of patterns \(01\) and \(10\): each vertex has at least \(2d-2-1\ge1\) private neighbors (the subtraction by one is needed only when \(u,v\) are adjacent).

Pattern \(00\) also always occurs. At most \(2+4d\) vertices are forbidden by the union \(\{u,v\}\cup N(u)\cup N(v)\). For \(d\ge3\), \(N\ge3^d>2+4d\); for \(d=2\), \(N\ge12>10\) except for \(C_3\square C_3\). In that exceptional graph, transitivity and coordinate symmetries reduce distinct pairs to \(((0,0),(1,0))\) and \(((0,0),(1,1))\); respectively \((2,1)\) and \((2,2)\) witness \(00\). Therefore for \(d\ge2\), every pair's set \(S\) is either \(\{00,01,10\}\) or \(\{00,01,10,11\}\).

The second possibility occurs exactly when \(u,v\) have a common neighbor. If \(u,v\) are adjacent, this is equivalent to the changed coordinate having length three. For nonadjacent \(u,v\), it is equivalent to graph distance two. Nonadjacent pairs of distance two always exist, by changing two coordinates by one. Nonadjacent pairs with no common neighbor exist exactly when the diameter is at least three, because any pair at distance at least three has no common neighbor; the product diameter is \(\sum_i\lfloor n_i/2\rfloor\). Among products with \(d\ge2\), diameter two occurs only for \(C_3\square C_3\). Thus the entire spectrum is determined by (a) whether there are length-three factors, (b) whether there are factors of length at least four, and (c) whether the diameter exceeds two. This yields exactly the four types VI, VII, VIII and V in the table.

**Step 3: one factor and strict separation.** For \(d=1\), direct examination of the possible cyclic distances gives the following complete spectra. To make the table compact write \(A=\{00,01,10\}\), \(B=\{00,01,10,11\}\), \(D=\{01,10\}\), and \(F=\{01,10,11\}\). Each table entry \((e,S)\) is a distinct pair type; the second component is a *set* of third-vertex patterns.

| Graph | Full pair spectrum \(\Sigma\) |
| --- | --- |
| \(C_3\) | \(\{(1,\{11\})\}\) |
| \(C_4\) | \(\{(1,D),(0,\{11\})\}\) |
| \(C_5\) | \(\{(1,A),(0,F)\}\) |
| \(C_6\) | \(\{(1,A),(0,D),(0,B)\}\) |
| \(C_n,n\ge7\) | \(\{(1,A),(0,A),(0,B)\}\) |
| \(C_3\square C_3\) | \(\{(1,B),(0,B)\}\) |
| \(C_3^{\square d},d\ge3\) | \(\{(1,B),(0,A),(0,B)\}\) |
| mixed products | \(\{(1,A),(1,B),(0,A),(0,B)\}\) |

For the cycle tail \(n\ge7\), every pair has a \(00\) witness because the two selected vertices and their four possible neighbors occupy at most six vertices. Adjacent vertices have no common neighbor, nonadjacent distance-two pairs have a common neighbor, and nonadjacent pairs at distance at least three have none. The finite exceptions \(n=3,4,5,6\) follow by inspecting their complete lists of cyclic distances. The eight displayed spectra are pairwise different, so the exact-spectrum lemma proves both equivalence within each class and inequivalence across classes. Their smallest representative sizes are \(3,4,5,6,7,9,27,12\), so the sharp maximum is \(27\). This finishes the proof.

## Verification

Two standalone Python 3 programs accompany this result. `torus_types.py` enumerates all two-point witness spectra for 76 Cartesian cycle products, including dimensions one through five, and compares each to the theorem's eight explicit predicted spectra. `direct_rank3.py` independently computes complete logical types by recursively forming atomic triple types, one-quantifier ordered-pair types, two-quantifier pointed types, and finally the rank-three sentence type; it tests 21 named graphs, including products in all eight classes. Both scripts include repeated choices and exact equality/adjacency checks; captured outputs are provided. These finite computations corroborate, but are not the basis for, the unbounded-dimension proof above.

To reproduce with Python 3 from the folder containing the scripts, run `python3 torus_types.py` and `python3 direct_rank3.py`. No third-party Python packages are needed.

## Relationship to prior work

Brown and Hoshino (2007, Theorem 4.9) classify the Ehrenfeucht–Fraïssé game on **single cycles** and in particular establish the length-seven stabilization at three rounds. That theorem settles the single-factor restriction but does not give equivalences between cycles and cycle products, across dimensions, or between mixed and unmixed multidimensional tori. Verbitsky (arXiv:math/0401361v1, Sections 1–2) studies first-order graph definability and quantifier rank through Ehrenfeucht games, with general bounds in classes admitting separators, rather than this exact fixed-rank classification. Exact pair-pattern invariants are standard game-theoretic devices; the additional claim here is the all-dimension identification of the eight spectra and the sharp cross-dimensional collapse. Previous results for Hamming graphs and two-factor toroidal grids concern different signatures/ranks or restricted product families; these partial cases do not by themselves give the complete eight-class rank-three statement.

## Limitations

Nothing is asserted for quantifier rank four or higher, counting logic, labelled factors, weighted cycle products, arbitrary Cartesian products, or products involving a factor of length one or two. The exact historical-priority assessment remains qualified: related graph-product and finite-model-theory results may contain an equivalent formulation not located in the accessible material.

## References

1. Jason Brown and Richard Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, published 30 April 2007. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf . See especially Theorem 4.9 and Conclusions.
2. Oleg Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1, first publicly posted 26 January 2004. https://arxiv.org/abs/math/0401361 .
