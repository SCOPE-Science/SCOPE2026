# Exact binary quartet-shattering dimensions on seven phylogenetic leaves

## Finding

Let \(X=\{0,1,2,3,4,5,6\}\), and let \(\mathcal{T}_7\) be the class of all unrooted, leaf-labeled, fully binary phylogenetic trees with leaf set \(X\). The instance domain consists of the \(3\binom{7}{4}=105\) resolved quartet constraints \(ab\mid cd\) (unordered within each pair and between the pairs). A tree returns label \(1\) on a query when its restriction to the four named leaves realizes precisely the indicated split, and label \(0\) otherwise.

For this Boolean concept class,

\[
\boxed{\operatorname{VCdim}(\mathcal{T}_7)=6,\qquad \operatorname{Ldim}(\mathcal{T}_7)=9.}
\]

In particular, the adaptive-versus-static gap is three, and the adaptive dimension attains the hypothesis-cardinality bound:

\[
\operatorname{Ldim}(\mathcal{T}_7)
=\lfloor\log_2(945)\rfloor=9.
\]

## Assumptions and scope

The trees are unrooted, every internal vertex has degree exactly three, and all seven leaves carry distinct prescribed labels. No unresolved quartet outcomes are admitted. Query \(ab\mid cd\) means that the two paths from \(a\) to \(b\) and from \(c\) to \(d\) are vertex-disjoint after suppressing degree-two vertices. Equivalently, some tree edge separates \(\{a,b\}\) from \(\{c,d\}\) without prescribing where the other three leaves lie. The VC dimension uses one fixed set of distinct Boolean quartet queries, whereas the Littlestone dimension allows different queries at different vertices of a complete binary mistake tree.

## Proof

**Complete hypothesis census.** Start with the unique three-leaf star. Insert leaf \(k\), for each \(k\in\{3,4,5,6\}\), by subdividing one existing edge and attaching the new leaf to the subdivision vertex. A binary unrooted tree on \(k\) leaves has \(2k-3\) edges. Conversely, every tree on \(k+1\) named leaves has a unique predecessor after deleting leaf \(k\) and suppressing its degree-two neighbor. Hence this construction enumerates each topology exactly once and produces \(3\cdot5\cdot7\cdot9=945\) distinct hypotheses. The quartet domain has \(\binom{7}{4}\) choices of four leaves and three pairings per choice.

**VC lower bound.** In the canonical quartet indexing of `construct.py`, the six queries with zero-based indices \((0,21,42,54,76,82)\) are, in order,

\[
01\mid23,\quad 01\mid45,\quad02\mid46,\quad03\mid56,\quad15\mid26,\quad14\mid36.
\]

For each of the \(2^6=64\) possible answer patterns, `quartet_certificate.json` gives the index of a different tree realizing that pattern on those six queries. The standalone `verify.py` checks all \(384\) query-answer incidences, establishing \(\operatorname{VCdim}\ge6\).

**VC upper bound.** Permuting leaf labels acts transitively on the \(105\) possible quartet queries. If any seven-query set were shattered, it would have an isomorphic shattered set containing the first canonical query \(01\mid23\). Thus fix query index \(0\) and enumerate, in increasing index order, every possible sequence of another six distinct queries. For every current answer-pattern class, adding a query must split that class into both nonempty positive and negative subfamilies; if one class fails to split, no extension can be shattered. This is an exact, lossless backtracking test. The complete search in `construct.py`, repeated on an independently constructed concept matrix by `verify.py`, visits exactly \(206{,}992\) recursion nodes and finds **no** shattered seven-query support. Therefore \(\operatorname{VCdim}\le6\).

**Littlestone lower bound.** The certificate supplies all \(511\) internal quartet queries of a complete binary tree of depth nine in binary-heap order, together with one of the original \(945\) tree indices for each of its \(512\) leaves. A left/zero branch requires the queried split not to be displayed, while a right/one branch requires it to be displayed. The verifier follows every root-to-leaf path and independently checks all nine required answers against the corresponding tree. All \(512\) witnesses are distinct. Thus \(\operatorname{Ldim}\ge9\).

**Littlestone upper bound.** In every complete depth-\(d\) shattered tree, distinct leaves must have distinct witnessing concepts, because two diverging paths require opposite answers at their first divergence. Therefore \(2^d\le|\mathcal{T}_7|=945\). Since \(2^{10}=1024>945\), \(\operatorname{Ldim}\le9\). Together these bounds prove the stated equalities.

## Verification

Run `python construct.py` to regenerate `quartet_certificate.json` deterministically, or `python verify.py` to check the supplied certificate without regeneration. Both use only Python's standard library. The checker enumerates the tree class a second way: it constructs every rooted full binary hierarchy on leaves \(0,\ldots,5\), attaches leaf \(6\) at the root, and determines quartet displays by the four-point distance criterion rather than by edge splits. The independently generated \(945\) response vectors coincide exactly with the split-based census. It also checks the exhaustive static upper bound, all \(64\) VC witnesses and all \(512\) adaptive witnesses. The displayed test transcript is in `VERIFICATION.md`.

## Relationship to prior work

Hirai and Iwamasa introduced tractable multipartite quartet-compatibility systems; their 2018 conference paper and expanded text supply the quartet-display definition, not these Boolean shattering dimensions. Avdiukhin and collaborators (2023) give asymptotic multiclass online-learning bounds for hierarchical tree queries and a reduction for constant-sized tuples. Their dimensions use a different multiclass label model and do not state the present exact seven-leaf Boolean values. Arvanitakis and collaborators (2026) bound the Natarajan dimension of phylogenetic quartet reconstruction asymptotically; their relevant Section 5 does not supply exact Boolean VC and Littlestone dimensions for seven leaves. A single fixed quartet split versus all other splits is a binary one-versus-rest predicate and is not identical to requiring one of two fixed distinct multiclass labels.

The adjacent rooted six-leaf triplet concept and clade-membership concept are different: those ask rooted ternary restrictions or clade inclusion, not the exact displayed split on four leaves of an unrooted tree. No independent priority audit has been performed, and a different terminology or unpublished computation could cover the finite values.

## Limitations

The claim is **only** for unrooted fully binary trees on exactly seven labeled leaves and for the specified binary one-versus-rest quartet queries. It does not determine the dimensions for larger taxa sets, for unresolved trees, or for a multiclass classifier that must output one of three quartet resolutions. The computation exhausts a finite, explicitly specified class; it is not an unrestricted infinite-family theorem. Verified reproducibility and a literature search do not prove historical uniqueness.

## References

1. H. Hirai and Y. Iwamasa, *Reconstructing Phylogenetic Tree From Multipartite Quartet System*, ISAAC 2018, published 2018-12-06, doi:10.4230/LIPIcs.ISAAC.2018.57. Expanded manuscript arXiv:1904.01914.
2. D. Avdiukhin, G. Yaroslavtsev, D. Vainstein, O. Fischer, S. Das and F. Mirza, *Tree Learning: Optimal Sample Complexity and Algorithms*, AAAI 2023; arXiv:2302.04492 (first posted 2023-02-09).
3. D. Arvanitakis, V. Chatziafratis, Y. Luo and K. Makarychev, *Optimal Phylogenetic Reconstruction from Sampled Quartets*, arXiv:2604.17461 (first posted 2026-04-19).
