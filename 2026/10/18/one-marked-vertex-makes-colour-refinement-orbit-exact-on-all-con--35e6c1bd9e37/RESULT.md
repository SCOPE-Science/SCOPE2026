# One marked vertex makes colour refinement orbit-exact on all connected block graphs

## Finding

**Theorem.** Let \(G\) be any finite, nonempty, connected, simple **block graph**: every maximal two-connected block is a clique, and an edge by itself is a block. Give vertices arbitrary initial colours, subject only to the existence of one vertex \(r\) whose initial colour occurs nowhere else. Run ordinary synchronous counting colour refinement to stabilization, retaining the previous colour at each round. Then two vertices have the same final colour **if and only if** a colour-preserving automorphism of \(G\) carries one to the other. Thus any single vertex chosen as a landmark makes refinement recover the complete pointwise-stabilizer orbit partition, uniformly over all block sizes, the number of blocks, and all additional vertex colours.

The result concerns the **orbit partition within a given graph**, not isomorphism identification among arbitrary competitor graphs and not the exact number of rounds. The property is nonvacuous: an unmarked connected block graph can have a strictly coarser stable partition than its automorphism-orbit partition.

## Assumptions and scope

Graphs are finite, simple, undirected, and connected. The one-vertex graph is included. A block graph is a graph whose maximal nontrivial biconnected components are cliques. Write \(c_0:V(G)\to\mathcal C\) for any vertex colouring and assume \(c_0^{-1}(c_0(r))=\{r\}\). Synchronous counting refinement is defined recursively by

\[
 c_{t+1}(v)=\bigl(c_t(v),\operatorname{MSet}\{c_t(w):w\sim v\}\bigr).
\]

Colours here stand for equivalence types, not their arbitrary numeric encodings. Let \(c_\infty\) denote the stable partition. Every colour-preserving automorphism preserves each \(c_t\), so its orbits refine the stable classes. The theorem proves the reverse refinement.

For distance \(j\), let \(L_j=\{v:\operatorname{dist}(r,v)=j\}\). Every stable colour determines its distance layer. Indeed the unique initial colour marks \(L_0\), and each successive layer is recognized by the first occurrence of a neighbour in the preceding distance layer; induction proceeds from the root.

## Proof

**1. Geodetic block structure.** The bipartite block-incidence graph, having the vertices of \(G\) on one side and one vertex for each nontrivial block on the other, with membership edges, is a tree (the one-vertex case is immediate). Consequently every vertex \(v\ne r\) has a unique predecessor \(p(v)\in L_{j-1}\) for \(v\in L_j\); it is the preceding vertex on the unique shortest path to \(r\). All edges of \(G\) join vertices in consecutive layers or in the same layer. For any \(v\in L_j\) with \(j>0\), the neighbours of \(v\) in \(L_j\) are precisely the other members of the unique *child clique* in the block containing \(v,p(v)\). That clique consists of all vertices of this block at level \(j\); each such vertex has the same parent \(p(v)\). For a fixed vertex \(u\), its neighbours in \(L_{j+1}\) split into disjoint nonempty cliques, one for each block incident to \(u\) in the forward direction. Distinct forward cliques have no cross-edges or shared descendants. All these statements follow from the absence of cycles in the block-incidence tree.

**2. Stable colours reveal forward-clique signatures.** Write \(\chi=c_\infty\). For each nonroot vertex \(v\in L_j\), define its same-layer signature as the multiset

\[
 \sigma(v)=\{\!\{\chi(v)\}\!\}\uplus
 \operatorname{MSet}\{\chi(w):w\sim v,\ w\in L_j\}.
\]

Since \(\chi\) is stable and each stable colour determines the layer, \(\sigma(v)\) depends only on \(\chi(v)\). It is exactly the multiset of stable colours of the vertices in the forward clique of \(p(v)\) that contains \(v\). Therefore all vertices in one such clique have the same signature \(\beta\), and two vertices of the same stable colour cannot belong to forward cliques with different signatures.

For each \(u\in L_j\), its stable colour determines the full multiset of stable colours of its children in \(L_{j+1}\). Partition these children by their signatures \(\beta\). If \(a\) is any stable colour appearing with multiplicity \(\beta(a)>0\) in \(\beta\), and \(m_u(a)\) is the number of children of \(u\) of stable colour \(a\), then the number of forward cliques at \(u\) of signature \(\beta\) is exactly

\[
  m_u(a)/\beta(a).
\]

No other forward-clique signature contributes a child of colour \(a\), by the preceding paragraph. Thus \(\chi(u)\) determines the entire **multiset of its forward-clique signatures**, despite the refinement algorithm never being explicitly told which of its neighbours lie in a common block.

**3. Downward subtree reconstruction.** For a vertex \(u\), let \(T_u\) be the induced graph on \(u\) and those vertices whose unique root-to-vertex shortest path passes through \(u\), with \(u\) distinguished and the initial vertex colours retained. We prove by reverse induction on \(j\) that \(\chi(u)\) determines the root-preserving, colour-preserving isomorphism type of \(T_u\) for every \(u\in L_j\). At the maximum distance layer there are no forward neighbours, so this type is just the initial colour of \(u\). Assume the assertion for layer \(j+1\). By step 2, \(\chi(u)\) determines all forward-clique signatures with their multiplicities. Each signature lists the stable colours of its members. By induction each such colour determines the corresponding attached rooted descendant graph. Reconstruct the block by making its listed child roots pairwise adjacent, attaching their independently determined descendant graphs, and adjoining the parent \(u\). Distinct child blocks meet only at \(u\), so the resulting multiset determines \(T_u\). This closes the induction. In particular, stable colour equality implies equality of all attached rooted subtree types.

**4. Constructing orbit witnesses.** Fix \(u,v\) with \(\chi(u)=\chi(v)\). They lie in the same layer. We induct outward from \(r\) to construct a colour-preserving automorphism carrying \(u\) to \(v\). The case of the root is trivial. For nonroot \(u,v\), their stable neighbour multisets restricted to the preceding layer each consist of exactly one colour, so \(\chi(p(u))=\chi(p(v))\). By the outward induction, an automorphism fixing the uniquely coloured root maps \(p(u)\) to \(p(v)\). Its image of \(u\) is a child of \(p(v)\) with stable colour \(\chi(v)\) and signature \(\sigma(v)\). The forward block decomposition at \(p(v)\) has independent attached pieces; blocks with the same signature can be exchanged, and within such a block children with the same stable colour can be exchanged because their rooted descendant graphs have the same colour-preserving isomorphism type by step 3. Compose with a suitable automorphism fixing \(p(v)\) and all its ancestors to send this image to \(v\). Thus every stable colour class lies in a single orbit. Together with automorphism invariance of refinement, this proves equality of the two partitions.

**5. Why a landmark is needed in general.** A connected eight-vertex block graph is formed by two triangles, joining one chosen vertex of each triangle by a path of three edges. Its two triangle attachment vertices have degree three; the six other vertices have degree two. The unmarked degree partition is equitable: every degree-three vertex has three degree-two neighbours; every degree-two vertex has one neighbour of each degree. Thus unmarked refinement stabilizes at two classes, while automorphisms have three orbits (the degree-three pair, the two interior path vertices, and the four remaining triangle vertices). This shows that the singleton-landmark hypothesis cannot simply be omitted from a theorem covering *all* connected block graphs.

## Verification

`check_small.py` constructs, by attaching a clique along one existing vertex, all nonisomorphic connected block graphs on at most nine vertices. Generation is exhaustive because any block graph with more than one block has a leaf block, whose removal reverses this operation. Graphs are deduplicated using an isomorphism-invariant hash followed by exact graph-isomorphism tests. The counts for orders one through nine are \(1,1,2,4,9,22,59,165,496\). For every graph, every possible singleton landmark is marked and its stable colour classes are checked against explicit colour-preserving isomorphism witnesses. Additional randomized precolourings retain one unique landmark. The same program checks that precisely one connected block graph on at most eight vertices violates orbit refinement when left entirely unmarked.

`check_block_tree.py` independently constructs each graph's block-incidence tree and compares the stable classes of the original graph with those induced on its vertex nodes from ordinary refinement on the bipartite incidence tree. It tests 1,200 sampled rooted, additional-coloured block graphs of orders up to 80. These computations support the theorem but are not substitutes for steps 1–4 of the proof. Both programs require Python 3 and NetworkX (tested on NetworkX 3.5); deterministic seeds are included.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255, first posted 4 February 2015) develop the refinable/Tinhofer hierarchy, prove general connections between colour refinement and automorphism orbits, and recall orbit recovery for trees. Their general implications from amenability to refinability do not directly give the present rooted theorem for block graphs, which can fail unmarked orbit refinement.

Kiefer, Schweitzer and Selman (arXiv:1503.08792, first posted 30 March 2015) classify graphs globally identified by two-variable counting logic. Global identification is a stronger, different question than orbit exactness inside an individually marked graph; the inspected text does not state this all-connected-block-graph rooted orbit theorem.

Bhattacharjee, Panse and Sarma (arXiv:2605.19702, first posted 19 May 2026) characterize an individualization-refinement hierarchy in general. Their group-theoretic conditions offer a relevant equivalent viewpoint, but do not state a block-graph special case in the inspected material. The block-incidence-tree reconstruction in steps 2 and 3 is the claimed contribution. Literature search is not an exhaustive priority certificate.

## Limitations

The graph must be connected and a uniquely marked vertex must be present. The result does not cover all chordal graphs, all disconnected unions of block graphs, unmarked block graphs, or graph identification among arbitrary competitor graphs. It gives no sharp round count. Previous block-graph and line-graph observations motivated the structural question, and independent historical priority assessment remains necessary.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (2015), https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (2015), https://arxiv.org/abs/1503.08792.
3. S. Bhattacharjee, A. Panse, J. Sarma, *A Hierarchy of Tinhofer Graphs: Separations and Membership Testing*, arXiv:2605.19702 (2026), https://arxiv.org/abs/2605.19702.
