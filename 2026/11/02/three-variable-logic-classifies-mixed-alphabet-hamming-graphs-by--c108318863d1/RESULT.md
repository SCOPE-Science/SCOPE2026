# Three-variable logic classifies mixed-alphabet Hamming graphs by binary and nonbinary dimensions

## Finding

Let \(d\ge 1\), let \(q_1,\ldots,q_d\ge 2\) be integers, and define the unlabelled simple graph
\[
G(\mathbf q)=K_{q_1}\square\cdots\square K_{q_d}.
\]
Its vertices are the words \(x=(x_1,\ldots,x_d)\) with \(x_i\in\{0,\ldots,q_i-1\}\); distinct words are adjacent exactly when they differ in one coordinate. Write
\[
b(\mathbf q)=\#\{i:q_i=2\},\qquad s(\mathbf q)=\#\{i:q_i\ge 3\}.
\]
All graph structures below use only equality and the undirected adjacency predicate. For any two parameter lists with entries at least two,
\[
\boxed{G(\mathbf q)\equiv_{\mathrm{FO}^{3}}G(\mathbf r)
\quad\Longleftrightarrow\quad
(b(\mathbf q),s(\mathbf q))=(b(\mathbf r),s(\mathbf r)).}
\]
Here \(\mathrm{FO}^{3}\) uses at most three reusable variable names, has unrestricted quantifier depth, and has no counting quantifiers.

Consequently, among products with precisely \(d\) nontrivial complete-graph factors there are exactly \(d+1\) three-variable theories. The unique smallest representative *within this product family* of the class \((b,s)\) is \(K_2^{\square b}\square K_3^{\square s}\), having exactly \(2^b3^s\) vertices. In contrast, two-variable logic separates only the one-factor products from the products with at least two factors. When \(s\ge1\), replacing one ternary factor by a four-element factor leaves the three-variable theory unchanged but is detected by a four-variable sentence asserting the existence of a four-clique. Thus the three-to-four variable separation is sharp.

## Assumptions and scope

The number of factors is finite and positive, and every factor size is an integer at least two. No coordinate names, distance relations, graph products, counting predicates, or parameters are included in the logical signature. Cartesian product means adjacency by a change in exactly one coordinate. An empty product and unit factors are excluded; these are irrelevant to the stated nontrivial-factor classification. Equivalence is relative to the full family of these finite unlabelled graphs, not all finite graphs.

## Proof

**1. The two intrinsic edge types.** For any graph in the family, define the following formulas using the variable names \(x,y,z\):
\[
\begin{aligned}
B(x,y)&:=E(x,y)\land\neg\exists z\,[E(x,z)\land E(z,y)],\\
N(x,y)&:=E(x,y)\land\exists z\,[E(x,z)\land E(z,y)].
\end{aligned}
\]
An edge changing a coordinate of size \(q_i\) has exactly \(q_i-2\) common neighbors of its endpoints: any common neighbor must change that same coordinate and use a third value. Hence \(B\) consists precisely of edges changing binary coordinates, and \(N\) precisely of edges changing coordinates of size at least three. In particular \(E=B\lor N\) and the two predicates are disjoint.

For vertices \(u,v\), let \(d_B(u,v)\) count their differing binary coordinates and \(d_N(u,v)\) count their differing nonbinary coordinates. The graph formed by \(B\)-edges has connected components obtained by fixing the nonbinary coordinates, each a binary cube of dimension \(b\). Within a component, shortest \(B\)-path length equals \(d_B\). Similarly, the \(N\)-edge graph has components obtained by fixing the binary coordinates, and its shortest-path metric is \(d_N\). For endpoints in different components the corresponding edge-graph distance is infinite; the coordinate count remains defined and is used in the game below.

**2. Two-point extension-support lemma.** Fix two vertices \(u,v\) and put \(r_B=d_B(u,v)\), \(r_N=d_N(u,v)\). The set
\[
\mathscr S_{b,s}(r_B,r_N)=\{
(d_B(u,w),d_N(u,w),d_B(v,w),d_N(v,w)):w\in V(G)
\}
\]
depends only on the four integers \(b,s,r_B,r_N\), not on the individual alphabet sizes of the nonbinary coordinates and not on which coordinates differ.

To see this, consider each coordinate separately. If it is binary and the two anchors agree, the new symbol either agrees with both (increment \((0,0)\)) or differs from both (increment \((1,1)\)) in its two \(B\)-distances. If they differ, the new symbol equals exactly one anchor, with increment \((0,1)\) or \((1,0)\). If it is nonbinary and the anchors agree, the two \(N\)-distance increments are \((0,0)\) or \((1,1)\); if they differ, the choices are \((0,1)\), \((1,0)\), and \((1,1)\). The third choice exists for every alphabet of size at least three. Increments in the other color are zero. Since coordinates can be chosen independently, all support quadruples are exactly the componentwise sums of these local options. There are \(r_B\) binary differing coordinates, \(b-r_B\) binary agreeing coordinates, \(r_N\) nonbinary differing coordinates, and \(s-r_N\) nonbinary agreeing coordinates. This proves the lemma, including coincident anchors.

**3. A permanent three-pebble strategy.** Suppose the two graphs have the same pair \((b,s)\). Duplicator maintains, for every pair of currently pebbled positions, equality of both \(d_B\) and \(d_N\) between the two structures. Initially this is vacuous. When Spoiler moves a pebble, at most two anchors remain. Their colored distance pairs agree by induction. The extension-support lemma therefore supplies a response vertex with exactly the two prescribed colored distances to each anchor. If fewer than two distinct anchors remain, the same conclusion follows from the lemma with equal anchors, or by vertex transitivity when no anchor remains. This maintains the invariant regardless of which graph Spoiler chooses or how often a pebble is moved.

Equality of vertices is equivalent to having both colored distances zero. Adjacency is equivalent to the sum of the colored distances being one. Consequently every resulting pebble placement is a partial isomorphism in the original adjacency/equality language. Duplicator wins every finite three-pebble game, with no fixed round bound. By the standard finite-variable pebble-game equivalence, the structures satisfy the same \(\mathrm{FO}^{3}\) sentences.

**4. Three variables recover both dimensions.** For either definable binary edge relation \(R\in\{B,N\}\), define \(P_{R,0}(x,y):=(x=y)\) and, for fixed \(k\ge0\),
\[
P_{R,k+1}(x,y):=P_{R,k}(x,y)\vee\exists z\,[P_{R,k}(x,z)\land R(z,y)].
\]
This is a formula for the existence of an \(R\)-walk of length at most \(k+1\). Every formula uses only three variable names: when a binary subformula has free variables \(x,z\), its bound variables can be renamed to \(y\), and similarly for the other pairs. This innocuous but essential alpha-renaming avoids introducing a fourth name even though the edge predicate itself uses three names.

For each positive integer \(k\), the three-variable sentence
\[
\Psi_{R,k}:=\exists x\exists y\,[P_{R,k}(x,y)\land\neg P_{R,k-1}(x,y)]
\]
asserts the existence of two vertices at *finite* \(R\)-edge-graph distance exactly \(k\). The binary-edge components have diameter \(b\) and realize every distance from zero to \(b\); the nonbinary-edge components have diameter \(s\) and realize every distance from zero to \(s\). Therefore \(\Psi_{B,k}\) holds precisely when \(1\le k\le b\), and \(\Psi_{N,k}\) holds precisely when \(1\le k\le s\). In particular the complete three-variable theory determines \(b\) and \(s\), proving necessity.

**5. Representatives and width boundary.** Every product with dimensions \((b,s)\) has at least \(2^b3^s\) vertices, with equality at precisely \(b\) factors of size two and \(s\) factors of size three. By necessity no other parameter class can supply a smaller equivalent product. There are \(d+1\) pairs of nonnegative integers with sum \(d\).

For two variables, in the one-factor case all graphs are complete and have at least two vertices; with two or more factors every vertex has a distinct neighbor and a nonneighbor. In each case Duplicator wins the two-pebble game by preserving the sole currently anchored vertex's equality and adjacency/nonadjacency relation to the moved pebble. Completeness, expressible with two variables, separates the cases. Finally, for \(s\ge1\), the representative with every nonbinary factor of size three has no four-clique, whereas replacing one such factor by \(K_4\) creates a four-clique. A graph clique of size at least four lies within a single Cartesian factor layer, because pairwise adjacent words must vary the same coordinate. Thus the four-variable four-clique formula separates these two graphs, which the main theorem proves three-variable equivalent. This concludes the proof.

## Verification

Two reproducible programs accompany this document and use Python 3 standard library only. Run \(\texttt{python3 verify_support.py}\) and \(\texttt{python3 verify_logic.py}\). The first independently compares the local-option formula above with direct enumeration of all third vertices for every ordered anchor pair in 15 finite products (5,670 anchor pairs). The second builds the *unlabelled* adjacency graphs and performs full stabilized, set-based three-variable logical-type refinement, checking 12 positive/negative inter-graph comparisons. Its existential transitions use sets rather than counts. Recorded outputs are in \(\texttt{verify_support.txt}\) and \(\texttt{verify_logic.txt}\). Finite checks support, but do not replace, the arbitrary-parameter proof.

## Relationship to prior work

Klavžar and Peterin (2005) explicitly define mixed-factor Hamming graphs and characterize their subgraph, induced-subgraph, and isometric-subgraph embeddings. Their article concerns edge-labeling and embeddings, not unrestricted finite-variable equivalence. Grohe and Otto (2012, arXiv version) give the general noncounting pebble-game equivalence used in Step 3; their result alone does not determine the present family-specific invariant. Pikhurko and Verbitsky (2010 preprint) survey graph logical width and distance games without giving this classification.

Related previously developed statements about distance-regular graphs reduce noncounting three-variable equivalence to distance-intersection *support*, recovering the **uniform** Hamming-graph dichotomy between binary and alphabets of size at least three. The present mixed-factor result is not an instance of that distance-regular theorem when the factors have unequal sizes: those products are generally not distance-regular, and the proof here separates binary and nonbinary coordinate contributions and defines the two resulting edge relations inside ordinary three-variable logic. Earlier fixed-quantifier-rank results for rectangular rook graphs and uniform Hamming graphs address a different resource restriction and do not by themselves imply this unrestricted-depth statement.

## Limitations

The logical language is pure unlabelled adjacency plus equality, without counting. Stronger languages with named coordinate relations, fixed distance predicates, or counting quantifiers can distinguish more. The classification is of finite products of complete graphs with nontrivial factors only; it is not a characterization of those graphs among arbitrary graph structures. The comparison establishes originality relative to inspected accessible sources and recoverable prior statements, not global historical priority. No independent mathematical audit has been carried out.

## References

1. S. Klavžar and I. Peterin, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory 49 (2005), 302–312, DOI: 10.1002/jgt.20084; author-hosted full text: https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf (online publication dated 2005-04-08).
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first public version 2012-04-09; Section 2 on noncounting pebble games.
3. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first public version 2010-03-25; Sections 1, 3, and 4.
