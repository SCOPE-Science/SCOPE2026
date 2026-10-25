# Seven rank-three theories of categorical products of complete graphs

## Finding

Let \(d\ge1\) and let \(q_1,\ldots,q_d\ge2\) be integers. The **categorical (direct or tensor) product of complete graphs**
\[
G(\mathbf q)=K_{q_1}\times\cdots\times K_{q_d}
\]
has as vertices the coordinate words \(a=(a_1,\ldots,a_d)\) with \(a_i\in[q_i]\). Its simple, irreflexive adjacency relation is
\[
a\sim b\quad\Longleftrightarrow\quad a_i\ne b_i\text{ for every }i.
\]
Use first-order sentences in the signature consisting of equality and this adjacency relation, without coordinate names, constants or counting quantifiers. Write \(G\equiv_r H\) for agreement on all sentences of quantifier rank at most \(r\).

**Theorem.** The entire family \(\{G(\mathbf q)\}\) has exactly **seven \(\equiv_3\) classes**, with the following exhaustive classification. Here *binary* means a factor \(K_2\); *nonbinary* means a factor \(K_q\) with \(q\ge3\).

| Class | Exact condition | Smallest family representative | Vertices |
| --- | --- | --- | ---: |
| C1 | \(d=1,q_1=2\) | \(K_2\) | 2 |
| C2 | \(d=1,q_1\ge3\) | \(K_3\) | 3 |
| C3 | \(d=2\), both factors binary | \(K_2\times K_2\) | 4 |
| C4 | \(d=2\), exactly one binary factor | \(K_2\times K_3\) | 6 |
| C5 | \(d\ge3\), all factors binary | \(K_2\times K_2\times K_2\) | 8 |
| C6 | \(d\ge2\), all factors nonbinary | \(K_3\times K_3\) | 9 |
| C7 | \(d\ge3\), both binary and nonbinary factors occur | \(K_2\times K_2\times K_3\) | 12 |

Two members of the family agree at rank three if and only if they lie in the same row. In contrast, the family has only **two rank-two classes**, distinguished by \(d=1\) versus \(d\ge2\). Every member is rank-three equivalent to one with at most **12 vertices**, and this bound is best possible when representatives are required to be members of this family.

## Assumptions and scope

All factors are loopless complete graphs of order at least two; the number of factors is any positive finite integer and factor orders may repeat. The language is the *pure, unlabelled graph language*. In particular, product coordinates and prime-factor decompositions are not named. The word "class" always means agreement of all first-order sentences at the stated quantifier rank, not graph isomorphism. The maximum-representative bound is an *internal family bound*, not a bound for all finite graphs sharing such a theory.

## Proof

**Step 1: the exact three-round invariant.** Every product is vertex-transitive (permutations of the coordinate alphabets act transitively). For two different vertices \(a,b\), record whether \(a\sim b\), and, for each of the four ordered adjacency patterns
\[
(0,0),\ (0,1),\ (1,0),\ (1,1),
\]
record whether there exists a *third* vertex \(c\notin\{a,b\}\) having the indicated adjacency to \(a\) and \(b\). Call the resulting finite record \(\tau(a,b)\).

For vertex-transitive simple graphs, having the same set of records \(\tau(a,b)\) is **equivalent** to \(\equiv_3\): the first move may be matched using transitivity; at the second move the responder matches the record; at the third, a corresponding existing adjacency pattern can be matched, while equality with the first or second vertex is handled directly. Conversely, if one record is absent on one side, the player distinguishing the structures chooses its first and second vertices in the graph possessing the record; the final choice exploits a pattern available on exactly one side. The same statement can also be verified directly as the recursion for the three-round Ehrenfeucht–Fraïssé game.

**Step 2: compute every possible third-vertex pattern.** Fix different \(a,b\), and put
\[
D=\{i:a_i\ne b_i\},\qquad S=\{i:a_i=b_i\}.
\]
Then \(D\ne\varnothing\), and \(a\sim b\) exactly when \(S=\varnothing\).

A common neighbor \(c\) of \(a,b\) must avoid both coordinate values in each coordinate in \(D\), and must avoid the one common value in coordinates in \(S\). Therefore the \((1,1)\) cell is nonempty exactly when **all factors indexed by \(D\) are nonbinary**. Such a vertex cannot equal either chosen vertex.

For the \((1,0)\) and \((0,1)\) cells, distinguish two cases. If \(S\ne\varnothing\), choose some \(j\in D\), set \(c_j=b_j\) (respectively \(a_j\)), and choose every other coordinate different from the value of \(a\) (respectively \(b\)). This gives a third vertex adjacent to exactly one of \(a,b\), because the two selected vertices are not adjacent. Thus both single-adjacency cells are always present for a nonadjacent pair. If \(S=\varnothing\), a witness adjacent to \(a\) but not \(b\) needs one coordinate \(i\) taking \(b_i\) and a *different* coordinate \(j\) taking a value outside \(\{a_j,b_j\}\) to avoid being \(b\) itself. This is possible exactly when \(d\ge2\) and at least one factor is nonbinary. The other single-adjacency cell is symmetric.

For the \((0,0)\) cell, if \(a\sim b\), a third vertex must agree with \(a\) in some coordinate and with \(b\) in another. This is possible exactly when \(d\ge2\): choose two different coordinates and interchange their prescribed values. If \(a\not\sim b\) and \(d\ge3\), select an index of agreement to ensure both adjacencies fail, and change another agreeing coordinate if available; when there is only one agreeing coordinate, mix the \(a\)- and \(b\)-values in two differing coordinates. This always gives a vertex distinct from both. If \(a\not\sim b\) and \(d=2\), the pair agrees in one coordinate and differs in the other, say \(j\). The \((0,0)\) cell exists **if and only if \(q_j\ge3\)**: the third choice in the differing coordinate provides it, while changing the shared coordinate forces adjacency to one endpoint unless the differing coordinate avoids both endpoints.

These constructions and the converse coordinate restrictions prove the four-cell criteria for every \(d\) and every vector \(\mathbf q\).

**Step 3: all records and their classes.** Let \(P=(0,1,1,0)\) indicate the presence flags for the ordered cells \((1,1),(1,0),(0,1),(0,0)\), and similarly define \(Q=(0,1,1,1)\), \(U=(1,1,1,1)\). The possible nonadjacent-pair profiles are:

- all binary, \(d=2\): only \(P\);
- all binary, \(d\ge3\): only \(Q\);
- mixed, \(d=2\): \(P\) and \(U\);
- mixed, \(d\ge3\): \(Q\) and \(U\);
- all nonbinary, \(d\ge2\): only \(U\).

For adjacent pairs, the corresponding four-cell records are, respectively, \((0,0,0,0)\) for \(K_2\); \((1,0,0,0)\) for larger complete graphs; \((0,0,0,1)\) for all-binary products of at least two factors; \((0,1,1,1)\) for mixed products; and \((1,1,1,1)\) for products with at least two nonbinary factors and no binary factor. All these entries refer only to possible third vertices, not to the two already selected vertices.

The joint adjacent/nonadjacent record sets yield precisely the seven classes in the table. In particular, all seven are distinct: the adjacent profiles separate complete, binary-only, mixed, and nonbinary-only situations, while the \(P\)-versus-\(Q\) nonadjacent records separate two-factor and higher-factor binary or mixed products. Each case is realized by the representative shown.

**Step 4: sharpness and rank two.** The seven representatives have orders \(2,3,4,6,8,9,12\). No member of C7 has fewer than three factors, and it must include both a factor of order two and one of order at least three; hence every C7 representative has at least \(2\cdot2\cdot3=12\) vertices. Since different classes cannot substitute for it, the global family bound of twelve is sharp. For two rounds, any complete member supplies a second vertex distinct from and adjacent to a first vertex but no nonadjacent second vertex. Every product with at least two factors has both adjacent and nonadjacent second vertices from every first vertex. Vertex transitivity therefore gives exactly the asserted two rank-two classes.

## Verification

Running `python3 verify.py` using the accompanying standalone Python file produces `VERIFY_OK`. The program constructs literal product graphs and exhaustively enumerates two-point/third-point adjacency records for 54 parameter vectors (factor alphabets in \(\{2,3,4,5\}\), up to five factors, with at most 100 vertices). It also checks the coordinate criterion for 494 vectors (up to eight factors with sizes in \(\{2,3,4,7\}\)); the latter is an independent finite stress-test, not an infinite proof. An independently implemented *recursive* three-round game checks all 28 unordered pairs of the seven representatives and eight further cross-size cases. `verification_output.txt` is the recorded stdout. The infinite proof is Steps 1–4 above.

## Relationship to prior work

The categorical-product graph construction is standard. Iswadi (2011) studies metric-location-total domination on exactly these complete-graph products, and cites earlier work on their ordinary domination numbers. Those numerical domination results supply important partial information (for example, the special two-factor dominating-pair threshold) but do not determine the seven complete rank-three theories. Klotz and Sander (2007), Theorem 6, determine pairwise common-neighbor counts for unitary Cayley graphs; for squarefree moduli those graphs are a prime-order subfamily of these products by the Chinese remainder theorem. Their common-neighbor and diameter results cover only some extension-profile flags and do not supply the full classification for arbitrary repeated factors or product dimension.

For exactly two factors, \(K_a\times K_b\) is the complement of the rook graph \(K_a\square K_b\). Thus a previously known rank-\(r\) rook-graph classification also implies the two-factor specialization: complementation preserves first-order quantifier rank. The present assertion is the **uniform arbitrary-number-of-factors theorem**, which additionally distinguishes the two- versus three-or-more-factor regimes, classifies products with multiple binary factors, and gives a sharp 12-vertex bound across all such products. The common-neighbor calculation is not presented as original by itself.

## Limitations

Only ordinary first-order sentences with the indicated pure adjacency signature are considered; the result does not classify products with named coordinates, counting logic, or higher quantifier rank. The sharp bound concerns representatives inside the product family. The exhaustive computations alone cannot establish the infinite theorem. Equivalent coverage in unindexed or inaccessible earlier literature remains possible, and no independent mathematical audit has been performed.

## References

1. H. Iswadi, *Locating and Total Dominating Sets of Direct Products of Complete Graphs*, 3rd International Conferences and Workshops on Basic and Applied Sciences (2011), pp. 585–589. Open full text: https://repository.ubaya.ac.id/274/1/hazrul_Locating%20and%20Total%20Dominating%20Sets_2011.pdf .
2. W. Klotz and T. Sander, *Some Properties of Unitary Cayley Graphs*, Electronic Journal of Combinatorics 14 (2007), R45; published 21 June 2007. DOI: https://doi.org/10.37236/963 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r45/pdf/ .
3. W. Wang and N.-N. Xue, *Connectivity of Direct Products of Graphs*, arXiv:1102.5180, publicly submitted 25 February 2011; https://arxiv.org/abs/1102.5180 .
