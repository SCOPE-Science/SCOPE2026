# The complete eccentricity profile of the balanced \(K_{4,4}\) graph associahedron
## Finding
Let \(G=K_{4,4}\), with bipartition
\[
A=\{0,1,2,3\},\qquad B=\{4,5,6,7\}.
\]
The graph associahedron \(\mathcal A(G)\) is the simple seven-dimensional polytope whose vertices are maximal tubings of \(G\), and whose edges are flips exchanging exactly one proper tube.

A search tree \(T\) on \(G\) consists of a single chain of successive roots until the remaining induced graph consists of isolated vertices of a single color, which become leaf children of the last root. Let \(s(T)\) be the number of roots in that chain **through and including the root whose removal first exhausts either color class**. This definition works also when one isolated vertex remains, in which case the underlying rooted tree itself is a path. Necessarily
\[
4\le s(T)\le7.
\]

**The complete vertex-eccentricity law is**
\[
\boxed{\operatorname{ecc}_{\mathcal A(G)}(T)=15+s(T).}
\tag{1}
\]
In particular,
\[
\boxed{\operatorname{diam}(\mathcal A(K_{4,4}))=22.}
\tag{2}
\]
The one-skeleton has \(29{,}616\) vertices, \(103{,}656\) edges and constant degree \(7\). Its complete eccentricity multiplicities are

| Eccentricity | Vertices |
| ---: | ---: |
| \(19\) | \(48\) |
| \(20\) | \(768\) |
| \(21\) | \(5760\) |
| \(22\) | \(23040\) |

## Assumptions and scope
A **tube** is a nonempty vertex subset of \(G\) inducing a connected subgraph. Two tubes are compatible when they are nested or disjoint and nonadjacent. A **tubing** is a set of mutually compatible tubes, including the whole connected graph \(G\). A **maximal tubing** has precisely eight tubes including \(V(G)\); omission of the universal tube leaves seven proper tubes. Two maximal tubings are adjacent in the graph associahedron precisely when they have seven tubes in common, equivalently when one proper tube is exchanged. This is the standard nested-complex model of Padrol--Pilaud--Poullot, Section 2.1.

A **search tree** on a graph induced by \(S\) is recursively obtained by choosing a root \(r\in S\) and adjoining one search tree on each component of the graph induced by \(S\setminus\{r\}\). Its subtree vertex sets are precisely the tubes of its maximal tubing, including \(S\). Thus the two models agree without choosing coordinates for the polytope.

The eccentricity of a vertex \(T\) is the maximum, over all maximal tubings \(U\), of the shortest number of one-tube flips needed to go from \(T\) to \(U\). The diameter is the largest eccentricity. All statements are exact for the single canonical balanced graph \(K_{4,4}\), not an asymptotic claim.

## Proof
**Step 1: Exhaustive search-tree enumeration.** If both color classes in a nonempty induced subgraph of \(K_{4,4}\) are present, that subgraph is connected. Removing a root therefore leaves exactly one connected component until a color class is first exhausted. Once one class is exhausted, the remaining vertices form an independent set and are necessarily leaves in the search tree. Consequently every search tree consists of a labeled spine with a color word ending when the fourth vertex of one color is used, followed by the remaining opposite-colored leaves.

If \(j\in\{0,1,2,3\}\) opposite-colored vertices precede the fourth vertex of the exhausted color, there are \(2\binom{3+j}{j}\) possible words, each of length \(s=4+j\). Thus the number of patterns is
\[
2\sum_{j=0}^{3}\binom{3+j}{j}=70.
\tag{3}
\]
The group \(S_4\times S_4\) permuting vertices separately within each color class acts on all maximal tubings and on their flip graph by automorphisms. A pattern with \(4\) vertices of the exhausted color and \(j\) of the other color on its spine has orbit size
\[
4!\,\frac{4!}{(4-j)!},
\tag{4}
\]
with the remaining opposite-colored vertices forming an unordered set of sibling leaves. The four orbit-size sums are
\[
2\binom{3+j}{j}\,4!\frac{4!}{(4-j)!}
\quad(j=0,1,2,3),
\]
which evaluate to \(48,768,5760,23040\) and sum to \(29{,}616\). Every possible tree belongs to exactly one of these \(70\) orbits.

**Step 2: The exact flip graph.** The accompanying `verify.py` independently constructs all search trees by recursive root/component decomposition on induced subgraphs and directly constructs all labeled brooms from the \(70\) spine words. It asserts that the resulting sets of maximal tubings coincide. Each tubing is stored as a sorted tuple of eight integer bitmasks: a vertex \(i\) corresponds to bit \(2^i\), and the universal tube is bitmask \(255\).

For every tubing, delete one tube to obtain a seven-tube key. A key retaining \(255\) has exactly two maximal-tubing completions, which are the endpoints of one polytope edge. Deleting \(255\) instead gives a key with exactly one completion. All such keys are exhaustively processed, yielding an undirected graph with \(29{,}616\) vertices, degree \(7\) at every vertex, and \(103{,}656\) edges. These assertions are checked by exact integer and set operations, not floating point.

**Step 3: Complete shortest-path certificate.** Select the canonical representative of each of the \(70\) spine patterns by taking the lowest unused label of the required color at each step. For each representative, run breadth-first search over the entire graph constructed in Step 2, recording the maximum exact distance and one farthest vertex. The complete `orbit_certificate.json` records each color word, orbit size, representative tube tuple, maximum distance and farthest tube tuple. The standalone verifier recomputes the entire graph, runs all \(70\) breadth-first searches, and compares every certificate entry exactly, obtaining
\[
\operatorname{ecc}(T_{w})=15+|w|
\quad\text{for every one of the }70\text{ patterns }w.
\tag{5}
\]
Since each search tree is in the orbit of exactly one representative and the group acts by graph automorphisms, (5) proves (1) for every one of the \(29{,}616\) vertices. Combining with the orbit sizes of Step 1 gives the multiplicities and (2).

For a concrete diametral pair, the bitmask tubings
\[
(128,136,200,232,248,252,254,255)
\]
and
\[
(1,17,19,23,31,63,127,255)
\]
are at exact graph distance \(22\). The first is the representative of the pattern `AAABBBA`; its farthest partner is recorded in the certificate.

**Why finite enumeration is a proof here.** The mathematical model contains finitely many vertices; Step 1 proves that every vertex is enumerated, and Step 2 proves that every flip edge is enumerated. Breadth-first search computes exact shortest-path distances in a finite unweighted graph, and checking one representative of each exhaustive automorphism orbit covers every vertex. Thus the executable result is a complete finite proof of the stated \(K_{4,4}\) claim, not an inference from partial sampling.

## Verification
The files `verify.py` and `orbit_certificate.json` form the standalone checking package. From their directory run `python verify.py` with Python 3 and no third-party dependencies. The verifier independently compares the generic recursive search-tree enumeration with direct colored-broom enumeration, checks vertex/edge counts and every degree, exhaustively searches from every orbit representative, asserts the formula (1), and matches the full orbit certificate. The expected terminal confirmation includes

`VERIFY_OK K4,4 vertices=29616 edges=103656 degree=7 orbits=70 diameter=22`

and

`VERIFY_OK ecc=19:48,20:768,21:5760,22:23040 generic_vs_broom=yes certificate_replayed=yes`.

Each recorded eccentricity has an exact farthest witness; an upper bound for each representative is established because breadth-first search reaches every possible vertex. The argument requires the standard equivalence of maximal tubings and graph-associahedron vertices, and of one-tube flips and polytope edges, which is proved in the cited sources.

## Relationship to prior work
Padrol, Pilaud and Poullot describe the graphical nested complex and its polytope, and explicitly define maximal-tubing adjacency by a one-tube exchange. Their work concerns deformation cones, not this particular shortest-path metric.

Cardinal, Pournin and Valencia-Pabon give exact graph-associahedron diameters for *unbalanced* complete bipartite graphs, and ask for the balanced regime containing \(K_{4,4}\). Gargantini, Pastine and Torres sharpen the lower bound for balanced complete bipartite graph associahedra and determine the special family \(K_{2,q}\) for \(q\in\{3,4,5,6,7,8\}\), without an exact value for \(K_{4,4}\). Their Corollary 4.8 gives \(19\) as a lower bound in the present case, while the earlier general upper bound is \(32\). The exact value \(22\) and the complete eccentricity law distinguish this result from the existing estimates.

The statement is also not implied by known metric formulas for hypersimplices or other generalized permutahedra: graph associahedra of \(K_{4,4}\) have a different vertex set and flip adjacency. Eccentricity classes are indexed here by the length of the colored search-tree spine, not merely by a coordinate or vertex count.

## Limitations
Only \(K_{4,4}\) is classified; there is no claim for arbitrary balanced \(K_{p,q}\), nor any formula for all pairwise distances in \(K_{4,4}\). The proof is an exhaustive finite computation with a fully specified enumeration and source-code checker; the orbit table alone is not an independent conceptual derivation of the eccentricity formula. This finite result is reproducible without specialized numerical libraries.

A literature-indexing risk remains: the same small case could have been computed in an obscure or unpublished table under rotation-distance terminology without appearing in the checked sources. No claim of a globally certified novelty search is made.

## References
1. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public version 2021-09-19; *European Journal of Combinatorics* 107 (2023), article 103594. Primary MSC 52B05 in indexed mathematical bibliography. Section 2.1 gives maximal-tubing adjacency and graph-associahedron definitions.
2. Jean Cardinal, Lionel Pournin, Mario Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130, first public version 2021-06-30. Sections 1 and 7 discuss search trees, flips, bipartite bounds, and the balanced case as an open diameter problem.
3. Ana Gargantini, Adrián Pastine, Pablo Torres, *Effect of graph operations on graph associahedra*, arXiv:2406.06317, first public version 2024-06-10, revised 2024-10-10. Section 4, including Corollary 4.8, gives improved balanced-family bounds and exact cases for \(K_{2,q}\).
