# The thirty-vertex Schrijver independence complex is a wedge of four three-spheres

## Finding
Let \(G=SG_{3,3}\) be the Schrijver stable Kneser graph on the cyclically stable three-subsets of a nine-element set, with edges joining disjoint triples. Then its ordinary independence complex satisfies the **integral homotopy equivalence**
\[
\operatorname{Ind}(G)\simeq\bigvee^{4}S^3.
\]
Equivalently, \(\widetilde H_3(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z^4\), and all its other reduced integral homology groups vanish. The original simplicial complex has dimension nine, despite admitting a CW reduction with only one vertex and four three-dimensional cells. This is an exact finite-case calculation; no statement about all Schrijver parameters is made.

## Assumptions and scope
Write \(\mathbb Z/9\mathbb Z=\{0,\ldots,8\}\). A three-subset \(A\) is *cyclically stable* if no two of its members differ by one modulo nine. In particular, \(\{0,8\}\) is forbidden. List all such stable three-subsets in increasing lexicographic order \(A_0,\ldots,A_{29}\). The graph \(G\) has these thirty triples as vertices and an edge \(A_iA_j\) exactly when \(A_i\cap A_j=\varnothing\). An independent set of \(G\) is consequently a pairwise-intersecting family of stable triples, and is encoded by the thirty-bit integer \(F=\sum_{i:A_i\text{ occurs}}2^i\). The empty family is included only in the augmented face-poset matching.

## Proof
**Complete face enumeration.** For every graph vertex \(i\), define \(N_i\) as the bit mask of vertices corresponding to stable triples disjoint from \(A_i\). Starting with the empty mask and the set of all thirty available indices, recursively branch on the least available index \(i\): add the current face, then extend by \(i\) and forbid all indices in \(N_i\). By induction on the least available vertex, this enumerates each independent set exactly once and no dependent set. It produces **15,292 augmented faces**, including the empty face. The nonempty face numbers in dimensions zero through nine are
\[
(30,297,1311,3054,4212,3639,1974,648,117,9).
\]
A second algorithm, successively adjoining each of the thirty vertices to every previously generated admissible face, reproduces the identical complete face set. Its ordinary Euler characteristic is \(-3\).

**A finite acyclic Morse matching.** Use the following zero-based indices in the fixed lexicographic ordering:
```
(3,22,17,15,0,25,4,7,14,16,20,24,12,18,10,13,23,28,
 6,19,8,9,21,5,11,26,2,1,29,27)
```
For each pivot \(i\) in this sequence, simultaneously match every as-yet-unmatched augmented face \(F\) with \(F\cup\{i\}\) whenever both are still available; remove those two faces before proceeding. This gives precisely **7,644** pairs in the augmented face poset, including one pair involving the empty face. Exactly four faces remain unmatched, all three-dimensional. Their thirty-bit integer masks, in increasing order, are
```
20768, 25559040, 134217778, 268699664
```
Every matched pair differs by one vertex, so these are valid covering incidences.

**Exact acyclicity certificate.** For each augmented covering incidence \(B\subset F\) differing by one vertex, orient it from \(F\) to \(B\), except reverse the orientation when it belongs to a matching pair. The complete set of **79,812** directed incidences is constructed directly from all enumerated faces. Kahn's topological-sort algorithm processes all **15,292** face masks. Hence the directed graph has no cycle, verifying the entire matching rather than a sample of gradient paths. Deleting the matched pair containing the empty face leaves an ordinary acyclic matching of **7,643** pairs, with one critical zero-dimensional face and the four critical three-dimensional faces.

**Integral homotopy conclusion.** Forman's discrete-Morse theorem supplies a homotopy-equivalent CW complex with precisely one zero-cell and four three-cells, and no cells in dimensions one, two, or at least four. Each three-cell is attached by a map \(S^2\to\{\mathrm{point}\}\), necessarily constant. The CW complex is therefore homeomorphic to a wedge of four three-spheres. This proves the integral homotopy statement, not merely homology over a chosen field.

## Verification
Run the self-contained standard-library script `python3 verify_sg33.py` (Python 3.9 or later) from the same directory. It independently generates the graph and the face set by two distinct algorithms; checks the graph definition, face count and complete face vector; reconstructs each pivot match, the exact critical masks and dimensions; lists every augmented Hasse incidence; and topologically sorts the entire oriented Hasse graph. It additionally checks the Euler characteristic. The final success message includes counts, critical dimensions and the asserted wedge type. All quantities are integer or finite-set computations. The complete script is part of the package and contains no external data dependencies.

## Relationship to prior work
Braun [1] introduced the relevant independence-complex problem for Schrijver graphs. His Theorem 1.4 classifies \(\operatorname{Ind}(SG_{2,k})\), while Theorem 1.5 concerns auxiliary graphs \(E_{2n+2}\) related to \(SG_{n,2}\); neither gives \(\operatorname{Ind}(SG_{3,3})\). Braun and Zeckner [2] study *neighborhood* complexes, an inequivalent simplicial functor. Nilakantan and Singh [3] likewise determine neighborhood-complex topology for Kneser and Schrijver graphs; their statements do not classify the ordinary independence complex here. A distinct exact reduction for \(SG_{4,2}\) [4] gives \(S^3\vee S^4\vee S^4\), but its 25-vertex graph is not the present 30-vertex graph, and neither calculation implies the other. A separate study [5] addresses two-subset stable Kneser dihedral homology; its domain likewise excludes this case.

## Limitations
The theorem concerns exactly the ordinary independence complex of \(SG_{3,3}\), not the neighborhood complex, not the full Kneser graph, and not any higher-parameter family. The proof is an exhaustive, replayable finite matching computation; it is not an abstract closed-form family reduction. An unindexed equivalent finite computation might exist despite targeted searches. No claim of equivariant homology, integral group actions or higher-parameter recurrence is made.

## References
[1] Benjamin Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (first submitted 2009-12-03), https://arxiv.org/abs/0912.0720 . Full text, Introduction, Theorems 1.4–1.5 and Sections 3–5.

[2] Benjamin Braun and Mandy Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs*, arXiv:1102.1984v1 (first submitted 2011-02-09), https://arxiv.org/abs/1102.1984 .

[3] N. Nilakantan and A. Singh, *Neighborhood Complexes of Kneser Graphs*, arXiv:1807.11732v1 (first submitted 2018-07-31), https://arxiv.org/abs/1807.11732 .

[4] *Simple-homotopy reduction of the twenty-five-vertex Schrijver independence complex*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-simple-homotopy-reduction-of-the-twenty-five-vertex-schrijver-in--4b6155858ecc .

[5] *The dihedral character of stable Kneser independence-complex homology*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-dihedral-character-of-stable-kneser-independence-complex-hom--8af1ffc8127a .

[6] Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
