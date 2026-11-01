# The co-Heawood two-independence complex: eight four-spheres and irreducible symmetry

## Finding
Let \(\Delta\) be the co-Heawood graph, the bipartite point-line nonincidence graph of the Fano plane, and let \(K=\operatorname{Ind}_2(\Delta)\) be its two-independence (dissociation) simplicial complex. There is an integral homotopy equivalence
\[
K\simeq\bigvee^{8} S^{4}.
\]
Thus \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^8\), with all other reduced integral homology zero. Moreover, the natural eight-dimensional rational representation of the full graph automorphism group \(G=\operatorname{Aut}(\Delta)\) on \(\widetilde H_4(K;\mathbb Q)\) is absolutely irreducible and has no invariant vector. Its complete character is given by the table below, where \(e=0\) means that an automorphism preserves the point and line classes and \(e=1\) means it interchanges them.

| \(e\) | Element order | Number of elements | Trace on \(\widetilde H_4(K;\mathbb Q)\) |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 8 |
| 0 | 2 | 21 | 0 |
| 0 | 3 | 56 | \(-1\) |
| 0 | 4 | 42 | 0 |
| 0 | 7 | 48 | 1 |
| 1 | 2 | 28 | \(-2\) |
| 1 | 6 | 56 | 1 |
| 1 | 8 | 84 | 0 |

## Assumptions and scope
All complexes are finite abstract simplicial complexes and all homotopy equivalences refer to their geometric realizations. Write \(P=\{p_i:i\in\mathbb Z/7\mathbb Z\}\) and \(L=\{\ell_j:j\in\mathbb Z/7\mathbb Z\}\). The seven projective lines have point sets \(\{j,j+1,j+3\}\) for \(j\in\mathbb Z/7\mathbb Z\). The graph \(\Delta\) has vertices \(P\sqcup L\) and edges
\[
p_i\ell_j\quad\Longleftrightarrow\quad i-j\notin\{0,1,3\}\pmod 7.
\]
There are no edges within either vertex class. A face of \(K\) is a selected vertex set whose induced graph has all degrees at most one; equivalently, every induced connected component has one or two vertices. This face condition forbids any three-vertex path as a (not necessarily induced) subgraph. These definitions specify the graph and complex without graph-library conventions.

## Proof
**1. A complete acyclic matching.** Number the point vertices \(0,\ldots,6\), and line vertices \(7,\ldots,13\). For each nonempty face mask, in ascending order of the vertex index \(v\) from \(0\) through \(13\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both are still unmatched. This is a deterministic sequential element matching. The general acyclicity of sequential element matchings is established in Deshpande and Singh, Proposition 2.10; here acyclicity is also checked independently by enumerating and topologically sorting the entire oriented face Hasse graph.

The full complex has \(1116\) faces including the empty face, and its counts by face cardinality from zero through seven are
\[
(1,14,91,280,420,266,42,2).
\]
The matching contains exactly \(553\) distinct face pairs. The remaining \(9\) nonempty faces consist of one vertex and eight faces of cardinality five. Directly orienting every cover relation downward except the matched relations, which are oriented upward, gives \(4298\) directed edges on the \(1115\) nonempty faces; exhaustive topological sorting visits all \(1115\) vertices and leaves no directed cycle. No partial numerical sampling is used.

**2. Integral homotopy type.** By Forman's discrete Morse theorem the complex has the homotopy type of a CW complex with one zero-cell, eight four-cells and no other cells. Every four-cell attaches to the zero-skeleton, a point. Hence the CW model is the indicated wedge of eight four-spheres, over the integers and up to actual homotopy equivalence (not merely equal field Betti numbers).

**3. All automorphisms.** The nonneighbors of any line vertex within the point class are precisely its three incident points. Thus a bipartition-preserving graph automorphism is determined by a permutation of the seven points carrying the family of seven three-element line sets to itself. Exhausting the \(7!\) point permutations yields exactly \(168\) such permutations, each with a unique induced permutation of the lines. The graph is connected and bipartite: any two points have two common nonincident lines, and every line has four neighbors. Thus every automorphism preserves or exchanges the two classes. The involution \(p_i\mapsto\ell_{-i}\), \(\ell_j\mapsto p_{-j}\) is a graph automorphism interchanging classes, giving precisely \(336\) automorphisms altogether.

**4. Rational character.** For an automorphism \(g\), compute the orientation sign of its permutation of the vertices of each setwise-fixed nonempty face \(\sigma\). The reduced signed simplicial Lefschetz formula is
\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(K;\mathbb Q)\bigr)
=-1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
The identity holds since all reduced rational homology except degree four vanishes. Exhausting all \(336\) automorphisms and all \(1115\) nonempty faces produces the character table above. Summing its squared values gives \(336\), so the ordinary complex-character inner product is \(1\); therefore the rational representation is absolutely irreducible. Summing all character values gives zero, so it has no invariant rational vector.

## Verification
The included standalone `verify.py` uses only the Python standard library. It checks membership using both induced degrees and explicit forbidden triples on all \(2^{14}=16384\) vertex subsets, regenerates every Morse pair, checks every Hasse cover edge and the complete acyclic topological sort, and independently reduces all augmented simplicial boundary matrices over \(\mathbb F_2\). The resulting reduced mod-two Betti vector in dimensions zero through six is \((0,0,0,0,8,0,0)\). It also enumerates the point-preserving and class-exchanging automorphisms, verifies adjacency preservation for each, computes the signed Lefschetz character, and checks its exact orthogonality and invariants sums. `verification_output.txt` contains the actual program output. The Morse argument, rather than the mod-two ranks, supplies the integral homotopy conclusion.

## Relationship to prior work
Taylan's work on devoid complexes supplies the archive-period framework for forbidden-path complexes and matching constructions but treats paths, cycles and forests, not this co-Heawood graph. Deshpande and Singh's full treatment of higher independence complexes provides the sequential element matching proposition and classifies complete multipartite, whiskered, path, cycle and perfect-tree families; none of those hypotheses gives the present graph. Brouwer, Fon-der-Flaass and Shpectorov identify the co-Heawood graph as the point-line nonincidence graph of the Fano plane (also the incidence graph of the unique seven-point biplane), and study graphs locally isomorphic to it, not this two-independence complex. The ordinary Heawood incidence graph has valency three rather than four, so higher-independence results for that graph do not classify its bipartite complement. Ordinary independence, edge matching, neighborhood and graph-metric complexes have different face sets and do not imply this homotopy classification or character. No covering theorem was identified in the investigated literature; that statement is not a claim of exhaustive publication priority.

## Limitations
This is an exact finite-graph result, not a classification of all projective-plane nonincidence graphs or of higher independence parameters. Absolute irreducibility concerns the rational homology representation; an equivariant homotopy equivalence is not asserted. The certificate uses exhaustive computation on a fully specified finite complex and is independently reproducible, but its existence does not settle possible unindexed prior work or replace external mathematical review. This proof does not assert any uncomputed homotopy group or quotient torsion.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly posted 2015-01-27, https://arxiv.org/abs/1501.06754.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first publicly posted 2020-01-15, especially Proposition 2.10 and Theorems 3.5, 3.8, 4.6 and 5.6, https://arxiv.org/abs/2001.05448.
3. A. E. Brouwer, D. G. Fon-der-Flaass and S. V. Shpectorov, *Locally co-Heawood graphs*, in *Finite Geometries and Combinatorics*, pp. 59–68, Cambridge University Press, print 1993, https://doi.org/10.1017/CBO9780511526336.008 (introductory graph description and automorphism-group identification).
4. A. E. Brouwer's distance-regular graph tables, *Heawood graph / co-Heawood graph*, https://jaanos.github.io/tables/graphs/Heawood.html (graph nomenclature and structural comparison).
