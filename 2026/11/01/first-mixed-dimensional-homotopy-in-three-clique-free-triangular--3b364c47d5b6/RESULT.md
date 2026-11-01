# First mixed-dimensional homotopy in three-clique-free triangular graphs

## Finding

For each integer \(3\le n\le 7\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph on the edges of the complete graph \(K_n\). Let \(X_n=\mathrm{CF}_3(T_n)\) be the simplicial complex whose faces are vertex subsets of \(T_n\) containing no triangle. Then, as ordinary **integral homotopy types**,

\[
X_3\simeq S^1,\quad X_4\simeq S^1,\quad
X_5\simeq\bigvee^9 S^3,\quad
X_6\simeq\bigvee^{26}S^4,
\]
\[
\boxed{X_7\simeq S^4\vee\bigvee^{146}S^5.}
\]

For \(n=2\) the complex is contractible. Thus \(n=7\) is the first member starting from \(n=2\) with nonzero reduced integral homology in two different dimensions. In particular, \(\widetilde H_4(X_7;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_5(X_7;\mathbb Z)\cong\mathbb Z^{146}\), with all other reduced groups zero.

## Assumptions and scope

All graphs are finite and simple. The vertices of \(X_n\) are the \(\binom n2\) two-element subsets of \(\{0,\ldots,n-1\}\); two of these vertices are adjacent in \(T_n\) exactly when their corresponding edges of \(K_n\) intersect. A set of vertices spans a face of \(X_n\) exactly when it has no three pairwise adjacent vertices in \(T_n\). Three pairwise intersecting distinct edges of a simple graph form either a three-star or a triangle. Therefore faces of \(X_n\) are **precisely the triangle-free simple two-matchings of \(K_n\)**: edge sets of maximum degree at most two containing no three-cycle.

The theorem concerns only \(2\le n\le7\), with a homotopy classification for \(3\le n\le7\). It asserts no formula for larger \(n\), no equivariant homotopy type and no shellability classification.

## Proof

**Exhaustive face characterization.** Order the edges of \(K_n\) lexicographically, assigning indices \(0,\ldots,\binom n2-1\). Represent their subsets by binary masks. A forbidden mask has three bits corresponding to three mutually intersecting edges. There are exactly
\[
 n\binom{n-1}{3}+\binom n3
\]
forbidden triples, because each is either a three-star (with a unique center) or the edge set of a triangle. A mask belongs to \(X_n\) if and only if none of these triples is contained in it. The included verifier builds every face inductively by adding one edge at a time, rejecting any set completing a forbidden triple. For \(n=7\) the face counts, indexed by cardinality (empty face included), are
\[
(1,21,210,1155,3570,5607,3507,360).
\]
Thus \(X_7\) has exactly \(14{,}430\) nonempty simplices. The corresponding face counts for all smaller parameters are reproduced by the verifier.

**Explicit discrete-Morse matching.** For each \(n\), consider the fixed ordering of edge indices recorded in `ORDERS` in `verify.py`. Visit those indices in the indicated order. At each step, among currently unmatched nonempty faces, pair every face \(a\) not containing the selected edge with \(a\cup\{e\}\) whenever both are present. Process candidate faces in ascending order of cardinality and then numerical mask. This deterministic procedure produces the following numbers of matched pairs and critical cell dimensions:

| \(n\) | Matched pairs | Critical cells by dimension |
| --- | ---: | --- |
| 3 | 2 | one in dimension 0; one in dimension 1 |
| 4 | 17 | one in dimension 0; one in dimension 1 |
| 5 | 111 | one in dimension 0; nine in dimension 3 |
| 6 | 839 | one in dimension 0; one in dimension 3; twenty-seven in dimension 4 |
| 7 | 7106 | one in dimension 0; thirty-six in dimension 4; 181 in dimension 5 |

For each matched cover \(a\prec b\), reverse the ordinary boundary arrow \(b\to a\) to \(a\to b\), keeping all unmatched boundary arrows downward. The verifier constructs **all** arrows, not just the matched ones, and topologically sorts the entire directed Hasse graph. It verifies that all vertices are removed from the topological-sort queue: there are \(69{,}762\) codimension-one incidences at \(n=7\), and no directed cycle. Every listed matching is therefore acyclic and yields a homotopy-equivalent CW model with exactly the indicated critical cells by Forman's discrete Morse theorem.

**Signed integer Morse differentials.** Orient each face by increasing edge indices, so deleting its \(j\)-th indexed vertex has incidence \((-1)^j\), starting with \(j=0\). To compute the surviving boundary after cancellation, recursively project a lower-dimensional face \(a\) as follows. A critical face projects to its corresponding basis vector; a noncritical face not serving as the lower element of a matched pair projects to zero. If \(a\) is matched upward to \(b\), with \(\epsilon(a,b)\in\{\pm1\}\), project by
\[
P(a)=-\epsilon(a,b)\sum_{a'\prec b,\;a'\ne a}\epsilon(a',b)P(a').
\]
Acyclicity ensures that this recursion terminates. The coefficient of critical \(a\) in the boundary of critical \(b\) is the signed sum of the projections of all facets of \(b\). This is precisely the integral cellular Morse differential obtained by cancelling unimodular face/coface pairs.

At \(n=6\), the only potentially nonzero differential is a \(1\times27\) integer matrix from critical dimension four to critical dimension three. Its Smith invariant factors consist of a single \(1\), so the Morse CW complex is homotopy equivalent to \(\bigvee^{26}S^4\).

At \(n=7\), the only potentially nonzero differential is a \(36\times181\) integer matrix from critical dimension five to critical dimension four. Its full Smith diagonal is
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{35\ \mathrm{times}},0),
\]
with all remaining rectangular entries zero. The verifier constructs the complete integer matrix from faces and signed gradient paths and computes its Smith normal form by exact integer arithmetic; there are \(801\) nonzero matrix entries. This is not a rational-rank or modular-rank inference. Consequently the reduced Morse homology has ranks one in dimension four and 146 in dimension five, with no torsion.

**From the differential to the claimed homotopy types.** All Morse models have exactly one zero-cell and no cells in dimensions one or two, except the circle cases \(n=3,4\), where there is one one-cell. At \(n=5\) and the circle cases, there are no possible attaching maps between positive-dimensional cells, giving the displayed wedges immediately. For \(n=6,7\), the lower positive skeleton is a wedge of spheres of dimension three or four, respectively, and every next-dimensional attaching map is classified by its integer degrees since \(\pi_d(\bigvee S^d)\cong\mathbb Z^{\oplus r}\) for \(d\ge2\). Integral unimodular changes of bases of domain and target, realized by cellular changes of generators, turn the attaching-degree matrix into its Smith diagonal. Each unit entry cancels an adjacent cell pair, and the remaining zero maps attach spheres trivially. There are 26 uncancelled dimension-four spheres at \(n=6\) and one dimension-four plus 146 dimension-five spheres at \(n=7\). This proves the asserted integral homotopy equivalences. Finally, \(X_2\) is a single vertex, hence contractible.

## Verification

Run `python verify.py` from the package's directory after installing the exact-integer `sympy` dependency listed in `requirements.txt`. The program builds all forbidden triples and all faces; checks the complete face vectors and forbidden-triple counts; constructs every pairing and every Hasse arrow and verifies global acyclicity; computes complete integral signed Morse boundaries and their Smith diagonals; and independently computes all mod-two boundary ranks from the **original**, uncollapsed simplicial chain complexes. It prints `ALL_VERIFY_OK triangle_free_2_matching_homotopy_n_3_to_7` only if every assertion passes. For \(n=7\), the mod-two calculation independently returns reduced Betti numbers one in dimension four and 146 in dimension five. Finite exhaustive verification is a proof for the five finite cases specified; no larger-parameter extrapolation is asserted.

## Relationship to prior work

Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (first public 2026-02-10, arXiv:2602.09623), give the general \(t\)-clique-free construction and shellability criteria for particular classes, including chordal graphs without suitable diamonds and clique-attachment constructions. They do not classify these \(X_n\) homotopy types. The triangular graph \(T_7\) has induced four-cycles and is not chordal, so their chordal-graph theorem does not give this result.

The same faces are known in combinatorial optimization as triangle-free simple two-matchings; Paluch, *Triangle-free 2-matchings* (arXiv:2311.13590, first public 2023-11-22), studies algorithms for maximizing their cardinality, not their integral homotopy type. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs* (arXiv:2006.13632, first public 2020-06-24), and Vega, *2-Matching Complexes* (arXiv:1909.10406, first public 2019-09-23), concern the **ordinary** bounded-degree complexes without the prohibition on triangles. Neither ordinary complex contains enough information to imply the present restricted-complex classification.

A published computation of mixed-dimensional mod-two **open-neighborhood** homology for \(T_7\) concerns a different complex; its numbers are not the present homotopy groups. The theorem above claims neither priority over the definitions nor any result about those different complexes.

## Limitations

The range is finite: \(2\le n\le7\). The classification and its transition do not imply a general closed form for \(n\ge8\). The homotopy equivalence is ordinary, not equivariant under \(S_n\). An unindexed equivalent finite computation may exist. These conclusions depend on the correctness of the explicit reproducible integer Morse reduction, rather than on an independently audited proof. No external independent validation has been performed.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623 (first posted 2026-02-10), https://arxiv.org/abs/2602.09623.
2. K. Paluch, *Triangle-free 2-matchings*, arXiv:2311.13590 (first posted 2023-11-22), https://arxiv.org/abs/2311.13590.
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first posted 2020-06-24), https://arxiv.org/abs/2006.13632.
4. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first posted 2019-09-23), https://arxiv.org/abs/1909.10406.
5. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
