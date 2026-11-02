# Three-round collapse for higher-dimensional Cartesian path grids

## Finding

Write \(P_n\) for the finite simple path on \(n\ge 2\) vertices. For every integer \(d\ge 3\) and every sequence \(n_1,\ldots,n_d\ge 2\), form the unmarked Cartesian product
\[
G(\mathbf n)=P_{n_1}\mathbin{\square}\cdots\mathbin{\square}P_{n_d}.
\]
In the first-order language consisting solely of undirected adjacency and equality, the entire family has **exactly two** equivalence classes at quantifier rank at most three:

* the exceptional three-cube \(Q_3=P_2\square P_2\square P_2\);
* every other member of the family, all of which are equivalent to the ordinary **seven-cycle** \(C_7\) at this rank.

In particular, for all admissible sequences \(\mathbf n,\mathbf m\),
\[
G(\mathbf n)\equiv_3 G(\mathbf m)
\quad\Longleftrightarrow\quad
\bigl(\mathbf n=(2,2,2)\ \Longleftrightarrow\ \mathbf m=(2,2,2)\bigr),
\]
where a sequence has its actual length \(d\ge3\), and \(\equiv_3\) means agreement on **all** first-order sentences of quantifier rank at most three. Thus
\[
P_2\square P_2\square P_3\ \equiv_3\ C_7\ \equiv_3\ P_2\square P_2\square P_2\square P_2.
\]
The two classes have smallest representatives *inside the stated path-product family* on eight and twelve vertices, respectively. Consequently twelve vertices is the sharp uniform representative bound within this family.

## Assumptions and scope

The product graph has vertex set \(\prod_i\{0,1,\ldots,n_i-1\}\). Two distinct vertices are adjacent precisely when their coordinate vectors differ by one in exactly one coordinate and agree in all others. There are no vertex colours, named origins, directions, coordinate labels, counting quantifiers, or additional graph relations. Every \(n_i\) is at least two, and \(d\) is any finite integer at least three; there is no upper bound on either parameter. The seven-cycle appears only as an *external logical representative*, not as a member of the path-product family.

## Proof

**Step 1: an exact three-round extension invariant.** For an ordered pair of selected vertices \((x,y)\) in a simple graph, the final third vertex \(z\) may repeat \(x\) or \(y\). For \(z\notin\{x,y\}\), its atomic adjacency pattern is one of \(00,10,01,11\), recording adjacency to \(x\) and to \(y\) in that order. Let \(\sigma(x,y)\) comprise equality/adjacency of the selected pair and the full set of realised patterns, including the special equality patterns for \(z=x\) and \(z=y\). After the first selected vertex \(x\), its two-round profile is the set \(\{\sigma(x,y):y\in V(G)\}\). The three-round type of the graph is the set of its vertex profiles. By backward induction on the three-round Ehrenfeucht--Fraïssé game, two finite simple graphs have the same three-round type exactly when they satisfy the same first-order sentences of quantifier rank at most three: the sets record both possible choices from either structure at each round. This construction allows repeated selections and works with equality.

**Step 2: local geometry of Cartesian path products.** Set \(N=\prod_i n_i\), and let \(b_i=1\) if \(n_i=2\), otherwise \(b_i=2\). Each vertex has degree between \(d\) and \(B=\sum_i b_i\). Graph distance is Manhattan distance, and the graph is bipartite, hence has no triangles. Two distinct nonadjacent vertices have a common neighbour if and only if their distance is two; they have either one or two common neighbours. Because \(d\ge3\), the neighbourhood of either vertex then has at least one other member. Pairs at distance at least three have no common neighbour, and adjacent pairs have no common neighbour.

**Step 3: a strict non-domination inequality.** Unless \(d=3\) and \(\mathbf n=(2,2,2)\),
\[
N>2+2B.
\]
Indeed, at \(d=3\) the all-binary point has \(N=8\), \(B=3\), and is the unique equality case. Replacing any binary factor by a factor of length at least three raises the product by at least four and raises \(B\) by at most one; increasing an already nonbinary length raises only the product. At \(d=4\), the smallest product is \(16\), while the all-binary right-hand side is \(10\); the same monotonic argument and adjoining further binary factors preserve the strict inequality for all \(d\ge4\). For any selected \(x,y\), the number of vertices different from both and adjacent to neither is at least \(N-2-\deg(x)-\deg(y)>0\) (when \(x=y\), the inequality is still sufficient). Therefore **every** selected pair in a nonexceptional product has a third vertex with pattern \(00\).

**Step 4: exhaustive remaining pair patterns.** Consider a nonexceptional product. Every adjacent pair has patterns \(00,10,01\) and not \(11\): the exclusive patterns exist because each endpoint has another neighbour, and a triangle is impossible. Every pair at distance two realises **all four** patterns: common neighbours exist, but each degree is at least three whereas there are at most two common neighbours. Every pair at distance at least three has precisely the three patterns \(00,10,01\), because there is no common neighbour. If \(x=y\), both a distinct neighbour and a distinct non-neighbour exist. Every \(x\) has neighbours at distances one, two, and three: for distance \(k\le3\), change one unit in each of \(k\) different coordinates. Consequently **each vertex has the same two-round profile**, consisting of exactly the equality type and these three distinct-pair types.

The seven-cycle \(C_7\) has exactly the same profile at each vertex: its pairs occur at circular distances one, two, and three; it is triangle-free; the distance-two pair has one common neighbour and other exclusive neighbours; and in every case a distinct vertex nonadjacent to both exists. Hence the exact extension invariant from Step 1 proves
\[
G(\mathbf n)\equiv_3 C_7
\]
for every nonexceptional product. This is a proof for **all** dimensions and lengths, not an inference from finite enumeration.

**Step 5: the exceptional cube is distinguished at rank three.** In \(Q_3\), choose two antipodal vertices. Every one of the other six vertices is adjacent to exactly one of these two. Thus the rank-three sentence
\[
\exists x\,\exists y\,\forall z\;
\bigl(z=x\lor z=y\lor E(x,z)\lor E(y,z)\bigr)
\]
is true in \(Q_3\). By Step 3, it is false in every other stated path product. Hence exactly two classes occur.

**Step 6: sharp representative bound.** The cube has eight vertices. Any other product in dimension three must have at least one factor length three, giving order at least \(2\cdot2\cdot3=12\), attained by \(P_2\square P_2\square P_3\). Any product of dimension at least four has at least \(2^4=16\) vertices. This proves that twelve is the smallest possible uniform representative bound among members of the stated family.

## Verification

The standalone program `check_profiles.py` constructs exact ordered-pair extension signatures using bitsets, then constructs the full graph three-round type as described in Step 1. It verifies agreement with \(C_7\) for 123 grid parameter tuples across dimensions three through six (up to 300 vertices), distinguishes \(Q_3\), and checks the order-twelve representative boundary. Its recorded output is `profile_output.txt`.

Independently, `check_game.py` computes nested complete atomic-tuple Hintikka types by directly enumerating choices on each of three rounds; it uses no pair-pattern shortcut. It checks seven nonexceptional examples of different dimensions and orders against \(C_7\) and verifies the exceptional cube is different. Its recorded output is `game_output.txt`. Both programs run with Python 3 standard library only: `python3 check_profiles.py` and `python3 check_game.py`. These finite tests independently corroborate the proof but do not replace the unbounded argument in Steps 2–5.

## Relationship to prior work

Brown and Hoshino (2007) determine the Ehrenfeucht--Fraïssé equivalence classes for ordinary finite paths and ordinary finite cycles. Their cycle classification supplies context for the seven-cycle as a depth-three representative, but does not establish equivalence between higher-dimensional Cartesian *path products* and that cycle. Existing work separately classifies two-factor rectangular path grids at depth three, and separate results classify Hamming graphs and hypercubes. The present assertion treats **three or more path factors of arbitrary lengths**, including mixed binary and longer path factors, and proves equivalence across dimension and between bipartite product graphs and an odd cycle. The proof gives its own exact three-round extension argument and does not infer the conclusion from the two-factor or pure-cube classifications.

## Limitations

The theorem does not classify the one- or two-factor path products (which have additional logical classes), does not address quantifier ranks four and higher, does not apply to counting or variable-restricted logics, and does not preserve equivalence when coordinates or directions are named. The rank-three result does not assert isomorphism, graph homomorphism equivalence, or elementary equivalence at unrestricted depth. A complete historical-priority survey and independent mathematical audit have not been performed.

## References

Jason Brown and Richard Hoshino, "The Ehrenfeucht-Fraïssé Game for Paths and Cycles", *Ars Combinatoria* **83** (2007), pp. 193–212, first publicly dated 2007-04-30. Official open-access PDF: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf ; article page: https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ .
