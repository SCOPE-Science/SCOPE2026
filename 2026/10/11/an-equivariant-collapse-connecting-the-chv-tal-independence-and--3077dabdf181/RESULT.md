# An equivariant collapse connecting the Chvátal independence and neighborhood complexes

## Finding

Let \(G\) be the labeled Chvátal graph described below, \(K=\mathcal N(G)\) its ordinary **open-neighborhood** complex and \(L=\operatorname{Ind}(G)\) its independence complex. **The complex \(L\) simplicially collapses onto \(K\) by a single orbit of eight elementary collapses under the full graph automorphism group \(D_4\).** The collapse is equivariant: every pair has trivial stabilizer and all pairs form one free orbit. In particular, the inclusion is a \(D_4\)-equivariant homotopy equivalence, and

\[
K\simeq S^{2},\qquad \chi(G)=4.
\]

The full automorphism group is \(\operatorname{Aut}(G)\cong D_4\). For the specific generators \(r,s\) in the stated vertex labeling, the integral homology orientation character on \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z\) is

\[
\deg(r^a s^b)=(-1)^{a+b},\quad 0\le a<4,\quad b\in\{0,1\}.
\]

In particular, the Lovász connectivity lower bound is sharp: \(K\) is simply connected, hence \(\chi(G)\ge4\), with equality realized by an explicit four-coloring.

## Assumptions and scope

The graph is finite, simple and undirected, with vertices labeled `0` through `11` and precisely the following 24 unordered edges:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

A nonempty vertex set \(\sigma\) is a face of \(K\) precisely when there exists a vertex \(v\) adjacent to **every** vertex of \(\sigma\). The common neighbor need not lie in \(\sigma\), and loops are not admitted.

The automorphism generators, encoded as the images of vertices `0` through `11` in order, are

```text
r=(1,5,11,6,0,4,7,10,9,2,3,8)
s=(0,4,3,2,1,5,9,8,7,6,11,10)
```

Here \(r\) has order four, \(s\) has order two, and \(srs=r^{-1}\). The group acts simplicially on \(K\) by vertex relabeling. The degree formula concerns the induced action on integral top homology; it does **not** assert an equivariant homeomorphism or an equivariant homotopy model with a standard geometric sphere action.

## Proof

**Exact face model.** Take all nonempty subsets of the twelve four-element open neighborhoods and eliminate repetitions. The resulting finite simplicial complex has \(110\) nonempty faces, with face vector

\[
(f_0,f_1,f_2,f_3)=(12,42,44,12).
\]

Each face is represented by its twelve-bit characteristic mask. The certificate `MORSE_CERTIFICATE.json` contains every mask and each of the matching pairs.

**One-orbit equivariant simplicial collapse.** Since \(G\) is triangle-free, every open neighborhood is independent and \(K\subseteq L\). Exhaustive independent-set enumeration gives the full face vector of \(L\) as \((12,42,52,20)\). The set difference \(L\setminus K\) contains precisely eight triangles and eight tetrahedra. Each extra triangle has **exactly one** coface in \(L\), the indicated tetrahedron, and each tetrahedron contains exactly one extra triangle. The complete list is:

```text
free triangle       unique coface
(0,7,10)            (0,2,7,10)
(0,8,11)            (0,3,8,11)
(1,3,10)            (1,3,10,11)
(1,8,9)             (1,6,8,9)
(2,4,11)            (2,4,10,11)
(2,5,9)             (2,5,7,9)
(3,5,6)             (3,5,6,8)
(4,6,7)             (4,6,7,9)
```

Each free triangle/tetrahedron pair is an elementary simplicial collapse. Their sixteen simplices are mutually distinct; removing all eight pairs leaves precisely \(K\). An exhaustive adjacency/nonadjacency-preserving automorphism computation gives the eight-element dihedral group described below. Its action permutes these eight pairs transitively; the stabilizer of either simplex in every pair is trivial. Thus the eight ordinary collapses constitute one admissible *equivariant orbit* of elementary collapses, providing an equivariant homotopy equivalence \(K\hookrightarrow L\). This relative result is not implied by the previously known nonequivariant homotopy type of \(L\) without the new free-pair verification.

**Discrete Morse reduction.** For each pivot vertex, in increasing order, pair an as-yet-unmatched face lacking that vertex with the face obtained by adjoining it, whenever both faces are present. Process candidate lower faces in increasing dimension, then integer-mask order, and never include the empty face. This gives exactly 54 disjoint matched cover relations. The only unpaired faces are the singleton `0` (mask `1`) and the triangle `5,7,9` (mask `672`).

Direct every unmatched face-poset cover from its upper face downwards and every matched cover upwards. The resulting directed graph has 110 vertices and 264 directed cover incidences. An exhaustive topological sort visits all 110 vertices, so this is an acyclic Forman matching. The finite discrete-Morse theorem yields a CW model with exactly one zero-cell and one two-cell and no other cells. The two-cell attaches to the unique point, and the CW model is \(S^2\). This proves the claimed **integral homotopy type**, not just equality of Betti numbers.

**Chromatic sharpness.** The second verifier enumerates all proper three-colorings by exact backtracking and finds none. It provides the proper four-coloring (in vertex order)

```text
0,1,0,1,2,0,1,0,1,2,3,3
```

and directly verifies that the graph is four-regular and triangle-free. The sphere is one-connected, so the Lovász inequality implies \(\chi(G)\ge4\), and the displayed coloring implies equality.

**Full dihedral homology character.** An adjacency-preserving backtracking census tests injective maps against both edges and nonedges and finds exactly eight automorphisms. The permutations \(r,s\) preserve edges and generate eight distinct permutations with the relations of \(D_4\), hence generate the full automorphism group.

For an automorphism \(g\), the alternating trace on reduced simplicial chains is

\[
-1+\sum_{\substack{\emptyset\ne\sigma\in K\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]

By the Hopf trace formula and the already proved sphere homotopy type, this is the trace, hence the degree, of \(g\) on \(\widetilde H_2(K;\mathbb Q)\). Exhaustive signed fixed-face enumeration gives

\[
\deg(r)=-1,\quad \deg(s)=-1,\quad \deg(rs)=1.
\]

The integral group \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z\) is rank one, so these rational traces determine its integral action. Multiplicativity and the dihedral relations yield the stated formula for all eight elements.

## Verification

Run `python verify_morse.py`, `python verify_independent.py`, and `python verify_equivariant.py` from the same directory as `MORSE_CERTIFICATE.json`; all three scripts use only Python's standard library. The third enumerates every independent set, proves the list of eight free-face/coface pairs, and verifies their transitive free orbit under all eight graph automorphisms. The first independently rebuilds the neighborhood faces from the edge list and checks every certificate pair, its critical cells, the oriented Hasse graph and its topological sort. It reports \(54\) pairs, critical masks `1` and `672`, and \(264\) oriented incidences. The second uses a separate explicit neighborhood table and tests all 12, 42, 44 and 12 simplices by direct subset conditions; over characteristics \(2,3,5,101\), the three unreduced boundary ranks are \((11,31,12)\). It also checks graph coloring, all graph automorphisms and the signed fixed-face character.

The modular homology computations are consistency checks; the acyclic Morse matching is the proof of the integral homotopy statement. The finite permutation census is exhaustive because it tests all possible vertex images under a complete adjacency/nonadjacency backtracking tree.

## Relationship to prior work

The Chvátal graph's four-chromaticity and smallest-four-regular-triangle-free extremality are classical. **The nonequivariant homotopy equivalence \(\operatorname{Ind}(G)\simeq S^2\) is also already established in a separate exact same-graph calculation, which includes a vertex-deletion classification.** Neither that sphere homotopy type nor its vertex-deletion data is claimed as new here. The new assertion is the *explicit relative, equivariant simplicial collapse* of the independence complex onto the distinct open-neighborhood complex, with one orbit of eight certified free-face pairs. Combining the pre-existing sphere result with this new collapse would yield the neighborhood sphere, but the present proof also provides an independently checked Morse reduction of the neighborhood complex.

Barmak's star-cluster approach supplies general connectivity methods for independence complexes and an independence-complex-based chromatic lower bound. It does not give this graph's relative collapse or dihedral top-homology character. In particular, knowing the homotopy type of the independence complex does not by itself provide the sharp Lovász bound from the neighborhood complex. Kahle's probabilistic neighborhood-complex results do not compute this graph. Shukla's classification treats graphs of maximum degree at most three and four-regular *circulant* graphs, whereas \(G\) has degree four and two vertex orbits, so it is non-circulant. The standard equivalence of the ordinary neighborhood and graph-Hom complexes changes presentation but does not compute the specific relative collapse.

The group character and sharp topological chromatic bound are natural structural consequences of the certified neighborhood complex. No general relation between independence and neighborhood complexes of arbitrary triangle-free graphs is asserted, and absolute publication priority is not claimed.

## Limitations

The statement concerns precisely this graph, the actual inclusion of its two named complexes, and its full graph-automorphism action; no general theorem for four-chromatic graphs or four-regular graphs is claimed. The character gives the action on homology, not a classification of equivariant sphere actions or of the canonical involution on a graph box complex. The original short graph-construction article was not fully retrievable for bibliographic comparison; the graph combinatorics used in the proof are defined explicitly and verified independently. Possible equivalent calculations in unindexed literature remain an originality risk.

## References

1. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory **9** (1970), 93–94, DOI: 10.1016/S0021-9800(70)80057-6.
2. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first posted 2005-12-04; Journal of Combinatorial Theory A **114** (2007), 380–387.
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first posted 2018-02-13.
4. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first posted 2010-07-02.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
