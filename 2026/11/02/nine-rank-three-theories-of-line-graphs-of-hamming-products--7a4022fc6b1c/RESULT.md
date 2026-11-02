# Nine rank-three theories of line graphs of Hamming products

## Finding

For a nonempty list of integers \(\mathbf q=(q_1,\ldots,q_d)\), with \(d\ge1\) and each \(q_i\ge2\), put
\[
H(\mathbf q)=K_{q_1}\square\cdots\square K_{q_d},\qquad X(\mathbf q)=L(H(\mathbf q)).
\]
The vertices of the simple undirected line graph \(L(H)\) are the edges of \(H\); two are adjacent exactly when they share an endpoint. Use first-order logic with equality and this single, unlabelled adjacency predicate. All \(X(\mathbf q)\) belong to **exactly nine** quantifier-rank-three equivalence classes:

| Class | Necessary and sufficient parameters | One smallest representative | Its number of vertices |
|---|---|---|---:|
| A | One factor of order two | \(L(K_2)\) | 1 |
| B | One factor of order three | \(L(K_3)\) | 3 |
| C | One factor of order four | \(L(K_4)\) | 6 |
| D | One factor of order five | \(L(K_5)\) | 10 |
| E | One factor of order at least six | \(L(K_6)\) | 15 |
| F | Exactly two factors, both binary | \(L(K_2\square K_2)\) | 4 |
| G | Exactly two factors, of orders two and three | \(L(K_2\square K_3)\) | 9 |
| H | Exactly two factors, of orders two and at least four | \(L(K_2\square K_4)\) | 16 |
| I | All remaining cases: at least three factors, or two factors each of order at least three | \(L(K_2\square K_2\square K_2)\) | 12 |

Two structures are equivalent at quantifier rank three if and only if their parameter tuples fall in the same table row. Every member has a rank-three equivalent representative on at most **16 vertices**, sharply so: class H has no smaller representative in this family.

In particular, even in the presence of arbitrarily unequal alphabet sizes and unbounded dimension,
\[
L(K_2\square K_2\square K_2)\equiv_3
L(K_3\square K_3)\equiv_3
L(K_2\square K_3\square K_4)\equiv_3
L(K_2^{\square d})\quad(d\ge3).
\]

## Assumptions and scope

A Hamming product is the graph on \(\prod_i\{0,\ldots,q_i-1\}\) in which distinct words are adjacent exactly when they differ at one coordinate. All factors are nontrivial; a product has at least one factor. Superscript \(\equiv_3\) means agreement on **all first-order sentences of quantifier rank at most three**, without counting, edge colours, coordinate predicates, or additional constants. The line graph is interpreted in the usual simple-graph sense, with distinct edges meeting at one endpoint giving one adjacency.

## Proof

**Three-round extension principle.** For any finite graph \(G\), an ordered pair \(x\ne y\) determines
\[
\sigma_G(x,y)=\left(\mathbf1_{E(x,y)},\ \{(\mathbf1_{E(z,x)},\mathbf1_{E(z,y)}):z\notin\{x,y\}\}\right).
\]
Write \(P_G(x)=\{\sigma_G(x,y):y\ne x\}\) and \(\mathcal T(G)=\{P_G(x):x\in V(G)\}\). For nonempty finite simple graphs, equality of the sets \(\mathcal T(G)\) is equivalent to rank-three elementary equivalence: in the three-round Ehrenfeucht--Fraïssé game, match the first chosen vertex by its \(P\)-type, the second (including repetitions) by its pair signature, and the last by one of the four listed fresh-vertex patterns. Conversely, differing \(\mathcal T\)-types can be expressed by a rank-three sentence specifying one vertex, all or some of its possible second-vertex signatures, and the existence or absence of third vertices realizing each pattern. Repeated choices are handled by equality. This argument also works when the graph is not vertex transitive.

For brevity, denote the fresh-third-vertex pattern sets by
\[
U=\{00,01,10,11\},\quad V=\{00,01,10\},\quad W=\{01,10,11\},\quad T=\{01,10\},\quad S=\{11\}.
\]
The pair signature \((e,Q)\) has adjacency bit \(e\) and pattern set \(Q\). The explicit finite profile table is:

| Class | The set \(\mathcal T(G)\) of pointed profile sets |
|---|---|
| A | \(\{\varnothing\}\) |
| B | \(\{\{(1,S)\}\}\) |
| C | \(\{\{(1,W),(0,S)\}\}\) |
| D | \(\{\{(1,U),(0,W)\}\}\) |
| E | \(\{\{(1,U),(0,U)\}\}\) |
| F | \(\{\{(1,T),(0,S)\}\}\) |
| G | \(\{\{(1,U),(0,U)\},\{(1,U),(0,U),(0,W)\}\}\) |
| H | \(\{\{(1,U),(0,U)\},\{(1,U),(0,U),(0,V)\}\}\) |
| I | \(\{\{(1,U),(0,U),(0,V)\}\}\) |

We derive every entry, uniformly in the unbounded parameters. The cases with one factor are the triangular graphs \(L(K_q)\), whose vertices are two-element subsets of a \(q\)-set. Two distinct such subsets meet or are disjoint; choosing an additional two-set realizes exactly the patterns in rows A--E. The cutoffs occur because a fresh two-set disjoint from the union of an adjacent pair needs two outside points (\(q\ge5\)), while for a disjoint pair it needs two points outside four (\(q\ge6\)). More explicitly: \(q=2\) gives one vertex; \(q=3\) a triangle; \(q=4\) yields adjacent \(W\) and disjoint \(S\); \(q=5\) adjacent \(U\) and disjoint \(W\); \(q\ge6\) both \(U\).

Now assume \(d\ge2\). Set \(N=\prod_iq_i\) and \(D=\sum_i(q_i-1)\). The underlying Hamming product is \(D\)-regular on \(N\) vertices, so its line graph has \(ND/2\) vertices, each of degree \(2(D-1)\). If \(N\ge8\), then for every two distinct line-graph vertices \(x,y\), at least one line-graph vertex is adjacent to neither: the union of their two closed neighborhoods contains at most \(4D-2\) vertices, strictly fewer than \(ND/2\ge4D\). Thus pattern \(00\) always occurs.

For \(d\ge2,D\ge3\), patterns \(01\) and \(10\) occur for every distinct line-graph pair. For intersecting original edges \(uv,vw\), an edge from \(u\) to a neighbor other than \(v,w\) gives pattern \(10\); use \(D\ge3\). For disjoint original edges \(uv,wx\), failure of pattern \(10\) would force all \(D-1\) other incident edges at each of \(u\) and \(v\) to terminate in \(\{w,x\}\). Thus \(D=3\) and \(u,v\) would have two common neighbors, impossible because adjacent vertices of the Hamming product have exactly \(q_i-2\le D-2\) common neighbors in the coordinate \(i\) of their difference; with two factors and \(D=3\), this number is at most one. The argument for \(01\) is symmetric. If the original edges intersect, a third edge at their shared endpoint gives pattern \(11\) because \(D\ge3\). If they are disjoint, pattern \(11\) exists precisely when a connecting edge between their endpoint sets exists in the Hamming product.

Consequently for \(d\ge2\), \(D\ge3\), \(N\ge8\), **every adjacent line-graph pair has signature \((1,U)\)**, and every nonadjacent pair has signature either \((0,U)\) or \((0,V)\), depending exactly on the existence of a connecting original edge. For every original edge \(e\), an edge opposite it in a four-cycle using a second coordinate is disjoint from \(e\) but connected to its endpoint set. Hence \((0,U)\) is always present in \(P(x)\).

It remains to decide whether \((0,V)\) can appear for each line-graph vertex \(x\), corresponding to a chosen original edge \(e\). If \(d\ge3\), choose a parallel edge \(f\) after changing two other coordinates: all endpoint distances from \(e\) to \(f\) are at least two, so no endpoint-connecting edge exists. This works for **every** axis of \(e\), and yields row I. If \(d=2\) and both factors have at least three points, take \(f\) along the other coordinate at a third value of the coordinate of \(e\), with both endpoints of \(f\) differing in the other coordinate from the fixed value of \(e\); again there is no endpoint-connecting edge. This gives the same row I.

For \(d=2\) and side sizes \((2,q)\) with \(q\ge4\), an edge \(e\) in the binary-factor direction spans both rows at one column. Every disjoint edge \(f\) has an endpoint joined to an endpoint of \(e\), so no \((0,V)\) is available. An edge in the other direction uses two columns in one row. Because \(q\ge4\), a parallel edge in the other row can use two columns outside these two; it has no endpoint joined to \(e\). The two axis types therefore have exactly the two pointed spectra in row H, and both are realized.

The only remaining two-factor graphs are \(K_2\square K_2\) and \(K_2\square K_3\), with fewer than eight underlying vertices. The first is a four-cycle; its line graph is another four-cycle, directly giving row F. The second is a triangular prism; its nine-edge line graph has two edge-axis orbits. Directly list the six neighboring and nonneighboring edges of an anchor of either axis: for the binary-axis anchor every distinct second edge has signature \((1,U)\) or \((0,U)\); for an anchor in the three-valued axis, a parallel edge in the opposite row realizes \((0,W)\), and the other disjoint configurations realize \((0,U)\). Both orbits have adjacent signature \((1,U)\), yielding precisely row G. This is an exhaustive small-graph check, independently reproducible from the literal adjacency construction in the verification programs.

The nine displayed sets \(\mathcal T\) are distinct. The extension principle proves both directions of the classification. Finally, the number of vertices of \(L(H(\mathbf q))\) is \(\frac12 (\prod_i q_i)(\sum_i(q_i-1))\). Within each table class, the stated representative has the least permissible parameters and therefore the least vertex count. In particular class H requires factor sizes \((2,q)\) with \(q\ge4\), whence its minimum is \(q(q-1+1)=q^2\ge16\). This proves the sharp uniform bound.

## Verification

Two standalone programs accompany the theorem. `check_line_hamming_orbits.py` constructs actual edges and incident-edge neighborhoods, computes every pair-extension signature at one edge of each coordinate-axis orbit, and confirms the nine table classes on 234 parameter tuples in dimensions one through five. `check_line_hamming_literal.py` separately constructs the complete adjacency matrix of the line graph and recursively enumerates all atomic triple types, two-point extension types, and one-point extension types. It finds nine distinct theories on the displayed representatives and matching types on ten additional examples. These finite checks corroborate the boundary cases and implementation but are **not used as a substitute for the uniform infinite proof above**. The accompanying `.out` files are recorded outputs of these executable scripts.

## Relationship to prior work

Klavžar and Peterin (2005) define and characterize Hamming graphs as Cartesian products of complete graphs, including factors of unequal sizes; their results concern graph embeddings, not these logical theories. Brown and Hoshino (2007) study Ehrenfeucht--Fraïssé games on paths and cycles, not line graphs of mixed Hamming products. Fish, Key, and Mwambene (2010) study codes derived from the incidence matrices and line graphs of Hamming graphs. That article's public abstract concerns codes and permutation decoding; its full text was not inspected, so its complete logical coverage is not certified here. The already-established depth-three classification of the triangular graphs \(L(K_q)\) supplies the one-factor component of this theorem and is **not claimed as a new independent contribution**. Earlier exact results on the Hamming products themselves, and on the color refinement of several line-graph families, do not imply the stated nine-class theorem for line graphs: adjacency between original **edges** is a changed signature and their three-round theories are not determined by the original graphs' three-round theories. The new content is the all-dimension, unequal-factor line-graph classification and the sharp exceptional binary-factor boundary.

## Limitations

This result is restricted to graph adjacency and equality at quantifier rank three. It does not give the rank-four or counting-logic classification; it does not treat arbitrary Cartesian products or hypergraph line graphs. Finite programs are corroborative only. The literature search and accessible full-text inspection do not establish exhaustive historical priority; an inaccessible code-focused line-Hamming paper leaves a stated residual coverage risk.

## References

1. S. Klavžar and I. Peterin, *Characterizing Subgraphs of Hamming Graphs*, Journal of Graph Theory **49** (2005), 302–312, published online 2005-04-08. DOI: 10.1002/jgt.20084. Public full text: https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf.
2. E. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/.
3. W. Fish, J. D. Key, and E. Mwambene, *Codes from incidence matrices and line graphs of Hamming graphs*, Discrete Mathematics **310** (2010), 1884–1897. DOI: 10.1016/j.disc.2010.02.010 (public abstract examined; full text unavailable).
