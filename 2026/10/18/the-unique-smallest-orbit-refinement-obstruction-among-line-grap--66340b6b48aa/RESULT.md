# The unique smallest orbit-refinement obstruction among line graphs of trees

## Finding

Let \(T\) be a finite simple tree, and let \(L(T)\) be its ordinary uncoloured line graph: vertices of \(L(T)\) are edges of \(T\), with adjacency for shared endpoints. Start one-dimensional synchronous colour refinement with one common colour; at each round recolour every vertex by its old colour and the multiset of colours of its neighbours. Call \(L(T)\) *orbit-refinable* when its stable colour classes coincide with its automorphism orbits.

**Sharp finite classification.** Every tree \(T\) with at most eight vertices has orbit-refinable \(L(T)\). Among the nine-vertex trees there is precisely one isomorphism type whose line graph is not orbit-refinable: the tree with two vertices of degree three connected by a path of four edges, with two additional leaves incident to each degree-three vertex. Its eight-vertex line graph has two stable colour classes but three automorphism orbits. Individually marking *any one* of its eight line-graph vertices restores exact equality of the stable partition with the pointwise-stabilizer orbit partition.

The classification concerns all finite trees in the stated size ranges; it makes no assertion that the nine-vertex exception is the only obstruction among larger trees.

## Assumptions and scope

Trees are nonempty, simple, finite, connected, and acyclic. A single tree vertex produces the empty line graph, whose empty partition is considered orbit-refinable. Orbit partitions are taken under the *full automorphism group of the line graph*, not merely under a specified subgroup of automorphisms induced by the tree. Refinement colours are structural equivalence classes, not numerical labels; a round stabilizes when its vertex partition does not split. For marked cases, the marked line-graph vertex has one unique initial colour, all other vertices another colour.

## Proof

**1. Exhaustive tree generation.** The verification program `verify_census.py` constructs the complete set \(\mathcal T_n\) of unlabelled \(n\)-vertex trees for every \(1\le n\le9\). Its base set is the one-vertex tree. For every representative in \(\mathcal T_{n-1}\), it adds one leaf at each possible existing vertex and retains one representative of each resulting canonical code. This produces *every* tree on \(n\) vertices: remove any leaf from an arbitrary such tree, apply the induction hypothesis to the remaining tree, and attach the leaf at the corresponding vertex. No random sampling or bounded-search heuristic is involved.

For completeness, its `canonical_tree` code is a complete tree-isomorphism invariant, rather than merely a hash: for every root \(u\), recursively write a pair of parentheses around the lexicographically sorted rooted-child codes, then take the minimum across all vertices as roots. Rooted trees share a code if and only if they are root-preservingly isomorphic, by induction on their numbers of vertices. Consequently, two unrooted trees share the minimum code if and only if they are isomorphic. Deduplication discards exactly isomorphic repetitions.

**2. Exact orbit and refinement decision.** For an edge \(e=uv\), delete \(e\); encode each of the two rooted components at \(u\) and \(v\), and retain their unordered pair, together with any individual marker on \(e\). Two edges have the same pair exactly when a tree automorphism carries one to the other, by gluing the two rooted isomorphisms. For the trees examined, the full automorphism action on \(L(T)\) agrees with the induced action from \(T\): this follows from the standard line-graph reconstruction theorem, with the small star/triangle exception checked directly (the line graph of the three-leaf star is a triangle, and both relevant automorphism actions are \(S_3\)). The one-edge and path boundary cases are also direct. The program computes ordinary simultaneous colour refinement on the actual line graph until stabilization. Stable classes can never split automorphism orbits; equality is therefore equivalent to the absence of any stable colour containing two distinct edge-rooted codes.

**3. Complete evaluated census.** Execution produces the exact table below; the third column counts failures among *all* nonisomorphic trees of that order, not among tested samples.

| Tree vertices \(n\) | Tree types | Failures |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 1 | 0 |
| 3 | 1 | 0 |
| 4 | 2 | 0 |
| 5 | 3 | 0 |
| 6 | 6 | 0 |
| 7 | 11 | 0 |
| 8 | 23 | 0 |
| 9 | 47 | 1 |

The unique exceptional representative has the edge list, using vertices numbered \(0\) through \(8\),

```text
(0,1), (0,2), (0,3), (1,4), (4,5), (5,6), (6,7), (6,8).
```

**4. Independent structural witness.** In this line graph the two edges incident to the degree-three vertices *on the joining path* have line-graph degree three; the other six edges have degree two. Every degree-three line-graph vertex has three degree-two neighbours, and every degree-two vertex has one neighbour of each degree. Hence the degree partition into sizes \(2\) and \(6\) is equitable, with quotient neighbour-count matrix \(\begin{pmatrix}0&3\\1&1\end{pmatrix}\) when the degree-three class is listed first. Ordinary colour refinement cannot split it after its first degree-sensitive round. But the six degree-two vertices comprise two different automorphism-invariant kinds: four vertices lie in triangles (edges ending in leaves of \(T\)), whereas two do not (the two internal edges of the joining path). Reflection along the connecting path and swapping the twin leaves at each endpoint show that the three sets, of sizes \(2,4,2\), are precisely the automorphism orbits.

**5. One-landmark repair.** The exceptional line graph has only three kinds of edges under its unmarked automorphism group: the two endpoint connecting-path edges, the four leaf edges, and the two internal connecting-path edges. For one marked representative of each kind, the marked refinement produces, respectively, six, seven, and six final classes, exactly the pointwise-stabilizer orbit numbers. The census program checks all eight individual markings directly, while the independent witness checker enumerates the *actual line-graph automorphisms* among all permutations of its eight vertices and verifies the same equality. This proves the statement for any choice of one individually marked vertex.

The finite classification is thus a constructive exhaustive proof whose coverage rests on the induction and canonicalization arguments above, not on extrapolating from samples.

## Verification

Run `python3 verify_census.py` with Python 3 and no third-party packages. It must print the complete nine-row census, the unique edge list, the partition sizes, successful verification of all eight individual markings, and `VERIFY_OK`. Independently run `python3 verify_witness.py`; it must print `AUTOMORPHISM_ENUMERATION_OK`. Both programs were executed from the exact files included here; `verification_output.txt` contains the observed output. The second checker uses brute-force graph automorphism testing and does not use tree-edge canonical codes.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015, arXiv:1502.01255) prove that forests are amenable, and hence refinable, and analyze Tinhofer/refinable graph classes. Their example of Johnson graphs \(J(n,2)\) is a result about line graphs of *complete* graphs, not line graphs of trees. The present exact minimal obstruction shows that the graph-property implication 'refinable tree implies refinable line graph' fails. Kiefer, Schweitzer and Selman (2015, arXiv:1503.08792) provide the general two-variable counting-logic framework, not this explicit complete small-tree census or its landmark repair. The finite result is independent of any assumption that arbitrary line graphs of trees satisfy a hereditary property. No novelty claim is made for the standard rooted-tree isomorphism algorithm or for the equivalence between stable refinement and equitable partitions.

## Limitations

The uniqueness assertion is *only* among trees of at most nine vertices. No all-size characterization of exceptional line graphs is provided. The finite exhaustive programs are inspectable mathematical certificates, but not independently audited formal proofs. They calculate automorphism-orbit recovery *within a fixed graph*, not graph identification against arbitrary competitors. Earlier specialized literature on equitable partitions of claw-free block graphs may imply the statement; this priority risk remains.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky. *Graph Isomorphism, Color Refinement, and Compactness*. arXiv:1502.01255, first submitted 2015-02-04. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer and E. Selman. *Graphs Identified by Logics with Counting*. arXiv:1503.08792, first submitted 2015-03-30. https://arxiv.org/abs/1503.08792
3. H. Whitney. *Congruent graphs and the connectivity of graphs*. American Journal of Mathematics 54 (1932), 150–168. Classical line-graph reconstruction theorem.
