# All one-coordinate extensions of Alderson’s \( (30,2,24)_{8/2} \) counterexample
## Finding

For Alderson’s explicit additive \( (30,2,24)_{8/2} \) code \(C\), every one-coordinate extension over an eight-symbol alphabet with minimum Hamming distance \(25\) is equivalent, under an automorphism of \(C\) in the unrestricted Hamming-isometry sense used by the source together with a permutation of the new alphabet, to the extension displayed in Proposition 7.6.

In the fixed message labeling by \(\mathbb F_2^6\), there are exactly \(240\) unordered fiber partitions. With
\[
T=\{0,e_1,\ldots,e_6,\mathbf 1\},
\]
they are precisely
\[
\bigl\{\,T+v:v\in a+W\,\bigr\},
\]
where \(W\) ranges over the \(30\) three-dimensional subspaces of \(\mathbb F_2^6\) whose seven nonzero vectors all have Hamming weight \(3\) or \(4\), and \(a+W\) ranges over the eight affine cosets of \(W\). Hence there are exactly
\[
240\cdot 8!=9{,}676{,}800
\]
labeled extension-coordinate functions. Every resulting extension is distance-invariant, with local distance enumerator
\[
1+35z^{25}+7z^{30}+21z^{31}.
\]

## Assumptions and scope

The base code is the code in Definition 7.3 of Alderson’s paper. Its \(64\) codewords are indexed by \(\lambda\in\mathbb F_2^6\). Proposition 7.4 gives the exact two-distance rule: for distinct messages \(\lambda,\mu\), the corresponding codewords have distance \(24\) exactly when \(\operatorname{wt}(\lambda+\mu)\in\{3,4\}\), and otherwise have distance \(30\).

The equivalence statement uses the source’s unrestricted code equivalence: coordinates may be permuted and an arbitrary alphabet bijection may be applied independently in each coordinate. The claim concerns only one-coordinate extensions over an eight-symbol alphabet. It does not assert uniqueness under a narrower monomial, semilinear, or additive equivalence.

## Proof

Put
\[
F=\{x\in\mathbb F_2^6\setminus\{0\}:\operatorname{wt}(x)\in\{3,4\}\}
\]
and let \(\Gamma\) be the Cayley graph on \(\mathbb F_2^6\) with connection set \(F\). By Proposition 7.4, two base-code words are at distance \(24\) exactly when their message labels are adjacent in \(\Gamma\). Therefore an added coordinate raises the minimum distance to \(25\) exactly when its fibers form a proper coloring of \(\Gamma\) with at most eight colors.

Let
\[
G=(\mathbb F_2^6\setminus\{0\})\setminus F.
\]
The \(28\) nonzero differences between distinct points of \(T\) are all different and equal exactly to \(G\). Label each \(g\in G\) by the unique edge of the complete graph on vertex set \(T\) whose endpoint difference is \(g\). A direct weight check gives, for distinct \(g,h\in G\),
\[
g+h\in G
\quad\Longleftrightarrow\quad
\text{the two corresponding edges meet}.
\]
Translate any independent set of \(\Gamma\) so that it contains \(0\). The edge labels of its nonzero elements then form a pairwise-intersecting edge family in \(K_8\), so there are at most seven of them; equality forces a star. Consequently \(\alpha(\Gamma)=8\), and every maximum independent set is a translate \(T+a\). The \(64\) such translates are distinct.

Thus any valid extension coloring of \(64\) vertices with at most eight colors must use exactly eight colors, each of size eight, and every fiber is a translate of \(T\). Two translates \(T+a\) and \(T+b\) are disjoint exactly when \(a+b\in F\). Hence a partition into eight translates is the same thing as an eight-clique in \(\Gamma\), indexed by the eight translation parameters.

To classify these cliques, embed \(\mathbb F_2^6\) linearly into the even-weight subspace of \(\mathbb F_2^7\) by
\[
(x_1,\ldots,x_6)\longmapsto
(x_1,\ldots,x_6,x_1+\cdots+x_6).
\]
Vectors of weight \(3\) or \(4\) map to weight \(4\). Translate an eight-clique to contain \(0\). Its seven nonzero images are weight-four words at mutual distance four. Their supports are seven four-subsets of a seven-set with pairwise intersection two; the complements are seven triples meeting pairwise in one point. Since these seven triples contain exactly \(7\binom32=21\) point-pairs, every pair occurs exactly once, so the triples form the Fano plane. The seven weight-four words therefore form the nonzero part of a binary \([7,3,4]\) simplex code. Pulling back shows that every eight-clique is an affine three-flat \(a+W\) whose seven nonzero direction vectors belong to \(F\).

Alderson’s Lemma 7.2 classifies exactly \(30\) such three-spaces \(W\). Each has eight affine cosets, giving exactly \(30\cdot8=240\) cliques and hence \(240\) unordered fiber partitions. Assigning eight distinct new symbols to a partition contributes \(8!\) labelings, which gives \(9{,}676{,}800\) labeled extension-coordinate functions.

It remains to compare the \(240\) extensions up to the source equivalence. Translation of message labels is realized by adding a fixed base-code word, which acts as an allowed coordinatewise alphabet permutation. Permuting the six message coordinates is also realized by a coordinate permutation together with coordinatewise alphabet bijections in the construction. Lemma 7.2 identifies the \(30\) direction spaces with the \(30=6!/24\) edge-labelings of \(K_4\), so these message-coordinate permutations act transitively on them. Translation then acts transitively on affine cosets. Thus every fiber partition is carried to the one from the displayed space in Proposition 7.6; a final permutation of the added alphabet aligns the fiber labels.

For the distance profile, every word has \(35\) neighbors at base distance \(24\), and all receive a different new symbol, so these become distance \(25\). Of the \(28\) words at base distance \(30\), exactly the other seven words in its fiber keep the same new symbol, while the remaining \(21\) receive a different symbol. This proves the local enumerator \(1+35z^{25}+7z^{30}+21z^{31}\).

## Verification

The bundled standard-library verifier reconstructs \(F\), \(G\), \(T\), and the Cayley graph directly from the definitions. It verifies the spectrum \(35^1,3^{35},(-5)^{28}\) and the strongly regular common-neighbor counts, enumerates all maximal cliques and cocliques by exact bitset search, and finds exactly \(64\) maximum cocliques, all translates of \(T\), exactly \(30\) special direction spaces, and exactly \(240\) maximum cliques, all affine cosets of those spaces. It constructs every resulting partition and checks the local distance distribution for every word. Successful replay ends with `VERIFY_OK`.

## Relationship to prior work

Alderson constructs this two-distance additive code as a nonmaximal counterexample and gives one explicit extension in Proposition 7.6. Lemma 7.2 identifies the \(30\) special three-dimensional direction spaces, and the paper remarks that any one of them can be used in that construction. The paper does not classify all proper eight-colorings of the minimum-distance graph, count all affine-coset fiber partitions, or state that all one-coordinate minimum-distance-\(25\) extensions form a single equivalence class.

The graph \(\Gamma\) is not new: under the standard parity embedding it is the even-weight component of the binary Hamming distance-four graph, a strongly regular graph with parameters \((64,35,18,20)\) and spectrum \(35^1,3^{35},(-5)^{28}\), as recorded by Brouwer, Cioabă, Ihringer, and McGinnis. The new assertion is the coding-theoretic classification of the extension colorings/fiber partitions and their equivalence, not the graph identification or its spectrum.

## Limitations

The uniqueness statement is for the broad Hamming-isometry equivalence explicitly used by the source. It does not claim uniqueness under narrower additive, monomial, or semilinear equivalence. The count \(240\) is for unordered fiber partitions in the fixed \(\mathbb F_2^6\) message labeling; the count \(9{,}676{,}800\) additionally labels the eight fibers by the new alphabet. The result concerns one-coordinate extensions only.

A residual originality risk is that an unindexed graph-theory classification of maximum cocliques or optimal colorings of the same strongly regular graph could contain an equivalent finite classification. No such statement was found in the checked primary graph source or the focused exact-parameter, coloring, coclique, extension, and numerical searches.

## References

1. Tim L. Alderson, *On the Maximality of Additive Codes*, arXiv:2607.22297v1, first public version 2026-07-24.
2. Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer, and Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, Journal of Combinatorial Theory, Series B 133 (2018), 88–121, DOI 10.1016/j.jctb.2018.04.005.
