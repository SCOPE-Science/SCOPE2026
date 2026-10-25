# Two-independence homotopy distinguishes the Shrikhande and four-by-four rook graphs

## Finding

Let \(R=K_4\mathbin{\square}K_4\) denote the four-by-four rook graph and let \(\mathrm{Sh}\) denote the Shrikhande graph. For a finite simple graph \(G\), define \(\operatorname{Ind}_2(G)\) to be the abstract simplicial complex whose faces are exactly the vertex sets \(F\) such that every connected component of the induced graph \(G[F]\) contains at most two vertices. Then

\[
|\operatorname{Ind}_2(R)|\simeq\bigvee^{105}S^3,
\qquad
|\operatorname{Ind}_2(\mathrm{Sh})|\simeq\bigvee^{57}S^3.
\]

Both graphs have sixteen vertices, degree six at every vertex, and exactly two common neighbors for every pair of distinct vertices, whether adjacent or not. Consequently, both have the strongly regular parameters \((16,6,2,2)\) and the same adjacency spectrum, yet the homotopy types displayed above differ.

## Assumptions and scope

All graphs are finite, loopless and undirected. Let the sixteen vertices be \((x,y)\), where \(x,y\in\{0,1,2,3\}\) are interpreted modulo four, encoded by the integer \(4x+y\). The rook graph has an edge between two distinct vertices precisely when they share a first or second coordinate. The Shrikhande graph has an edge precisely when the coordinate difference belongs to

\[
\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\subset\mathbb Z_4^2.
\]

All homotopy types are geometric realizations over the integers, not merely statements about homology over a field. The subscript two means **connected-component cardinality at most two**, which is equivalent to forbidding a three-vertex path as a (not necessarily induced) subgraph on any chosen face.

## Proof

**1. Exhaustive characterization of the finite complexes.** A subset is a face if and only if its connected components are singletons or individual edges. This condition is checked in two logically separate constructions in the executable certificate: a subset recurrence based on adding its least vertex, and an independently implemented connected-component traversal for each of the \(2^{16}\) subsets. The two agree on all inputs. The numbers of nonempty faces, by dimensions beginning with zero, are respectively

\[
(16,120,384,528,144)
\quad\text{and}\quad
(16,120,384,544,240,32).
\]

Thus there are exactly \(1192\) and \(1336\) nonempty faces. In particular, higher-dimensional faces are not discarded from the complex or its matching.

**2. Specified acyclic matchings.** Apply consecutive element-matchings in the following vertex orders, with each vertex encoded as above:

- Rook graph: `6,13,1,5,9,8,12,0,10,3,4,14,7,2,11,15`.
- Shrikhande graph: `1,5,7,6,3,11,2,4,13,8,15,9,14,10,12,0`.

For each vertex \(v\) in the specified sequence, match all still-unmatched pairs \((F,F\cup\{v\})\) for which both sets are faces, then remove both members of every pair. Every such pair is a cover relation in the nonempty face poset. This rule gives \(543\) pairs for the rook graph, leaving a single zero-dimensional face and \(105\) three-dimensional faces; it gives \(639\) pairs for the Shrikhande graph, leaving a single zero-dimensional face and \(57\) three-dimensional faces. No other faces are critical.

**3. Acyclicity verification.** For every cover \(F\subset F'\) in the complete nonempty face poset, orient it from the larger face to the smaller face unless it is a matched pair; reverse the orientation for a matched pair. Exhaustive enumeration produces exactly \(4224\) oriented cover relations for the rook graph and \(4960\) for the Shrikhande graph. The included program constructs every relation, asserts matching compatibility and exhausts the entire directed graph by Kahn's topological ordering algorithm. In both cases the number of vertices removed from the directed graph equals the total number of faces. A directed cycle is therefore impossible, proving that the displayed matchings are acyclic over the **entire** respective complexes, not only sampled subcomplexes.

**4. Integral homotopy conclusion.** The discrete-Morse homotopy theorem yields, for each complex, a CW model having one zero-cell and respectively \(105\) or \(57\) three-cells, with no one-cells or two-cells and no cells above dimension three. Every three-cell has its attaching map into a point (the two-skeleton); hence each model is exactly a wedge of that many three-spheres. This is a homotopy equivalence and an integral statement, including absence of torsion. No unverified claim about higher graph sizes is used.

## Verification

Run `python3 verify_ind2.py` using a standard Python 3 installation. No external modules, input datasets, or network access are needed. Its output is reproduced in `verification_output.txt`.

The program independently checks all \(65,536\) vertex subsets for each graph, verifies regularity, common-neighbor counts and distinct local structures, enumerates all faces and matching pairs, reconstructs the complete directed Hasse graph, and proves acyclicity by exhaustive topological sort. Independently constructed simplicial boundary matrices over \(\mathbb F_2\) confirm that the only positive-dimensional Betti numbers are \(105\) and \(57\) in degree three. The mod-two calculations serve as a cross-check, not the proof of the integral homotopy classification.

## Relationship to prior work

The \(r\)-independence complex is part of the established theory of higher independence complexes. Deshpande and Singh determine homotopy types for complete multipartite and fully whiskered graphs, paths, cycles and certain trees; these graph classes do not contain either graph here. Ghosh and Selvaraja analyze chordality and shellability in other specified graph classes. Sawant's May 2026 theorem establishes vertex decomposability for the higher independence complexes of **trees** and motivates further concrete non-tree examples. The two graphs here have many cycles and are not trees.

A published comparison of the **ordinary** independence complexes of the same strongly regular graphs reports distinct two-sphere wedge ranks. That result concerns the condition that all induced components have at most **one** vertex, and does not imply the present two-independence homotopy types. Computations for a two-independence complex of the Petersen graph concern a different graph, and do not imply either of these statements.

## Limitations

This is a complete classification for these two specified sixteen-vertex graphs, not a theorem for all strongly regular graphs or higher values of the independence parameter. The executable certificate is finite and fully exhaustive for the given graph sizes, while the final homotopy equivalences follow from the discrete-Morse theorem. The search of the relevant published literature cannot exclude an unindexed independently discovered equivalent classification. The work has not undergone independent mathematical audit.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first public submission May 24, 2026, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
3. A. Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614, https://arxiv.org/abs/2505.06614.
4. *Independence complexes of the Shrikhande and four-by-four rook graphs have different sphere-wedge homotopy types*, published mathematical record, identifier ending `41bf4d1d3187` (ordinary independence, not two-independence).
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse homotopy theorem).
