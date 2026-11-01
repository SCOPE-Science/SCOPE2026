# The Frucht graph matching complex and its complete edge-deletion homotopy profile

## Finding
Let \(F\) be the twelve-vertex cubic Frucht graph, with the explicit canonical labeling below. Let \(\mathcal M(G)\) be the **ordinary matching complex** of a finite simple graph \(G\): its simplices are the sets of pairwise vertex-disjoint graph edges. For all eighteen graph edges \(e\), deleting just that edge (not either endpoint) preserves the property of being a wedge of three-spheres. Precisely,
\[
\mathcal M(F)\simeq\bigvee^{20} S^3,\qquad
\mathcal M(F-e)\simeq\bigvee^{b(e)} S^3.
\]
In the fixed LCF labeling, the complete profile is:

| \(b(e)\) | Deleted edges \(e\) (vertex pairs) | Number of edges |
| --- | --- | ---: |
| 12 | \((0,1),(2,10),(9,10)\) | 3 |
| 13 | \((0,11),(6,8)\) | 2 |
| 14 | \((4,5),(6,7)\) | 2 |
| 15 | \((1,11),(2,3),(3,4),(3,5),(7,8)\) | 5 |
| 16 | \((1,2),(4,9)\) | 2 |
| 17 | \((8,9),(10,11)\) | 2 |
| 18 | \((0,7),(5,6)\) | 2 |

Thus the eighteen deletions yield **seven distinct homotopy types**, although the original graph has no nonidentity automorphism. The rank changes are not inferred solely from homology: the proof supplies a complete acyclic discrete-Morse matching for each complex and therefore its **integral homotopy type**.

## Assumptions and scope
The vertex set is \(\{0,1,\ldots,11\}\). Start with the twelve cycle edges \(\{i,i+1\}\) (indices modulo twelve) and add \(\{i,i+d_i\}\), where the classical order-one LCF jumps are
\[
(d_0,d_1,\ldots,d_{11})=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2).
\]
Remove repeated undirected edges. The resulting eighteen graph edges are, in the precise index order used by the certificate:

```python
EDGES = ((0,1),(0,7),(0,11),(1,2),(1,11),(2,3),(2,10),(3,4),(3,5),
         (4,5),(4,9),(5,6),(6,7),(6,8),(7,8),(8,9),(9,10),(10,11))
```

This is the standard Frucht graph, identifiable without relying on a drawing. The edge matching complex is the independence complex of the line graph, not the vertex-independence complex of the original graph. The empty simplex is included in the abstract simplicial complex but does not appear in the ordinary face-poset matching. Homotopy equivalences concern geometric realizations of these finite simplicial complexes; the homology conclusions are integral.

## Proof
**Complete finite cell model.** Encode the graph-edge subset \(\sigma\) by the nonzero 18-bit integer having bit \(j\) set precisely when the graph edge indexed \(j\) lies in \(\sigma\). The mask represents a simplex exactly when no two selected graph edges share an endpoint. Independent depth-first and exhaustive-mask enumerators produce the same \(1025\) nonempty faces, with dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,333,397,152,8).
\]
For a deleted graph edge indexed \(j\), retain exactly those faces whose masks have bit \(j\) unset. This constructs all eighteen deletion complexes without approximating their chain groups.

**Explicit Morse matching.** In every complex, process the graph-edge indices in the fixed order

```python
PIVOT_ORDER = (10,5,16,17,9,0,15,14,3,6,11,13,12,7,1,8,2,4)
```

For each index \(j\), skip it when that graph edge has been deleted. Among currently unmatched nonempty simplices, pair every \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\) whenever the latter is also currently unmatched. Remove both from consideration, then continue through the order. The deterministic source file `verify_morse.py` reconstructs these pairs; `morse_certificate.json` records the **complete** list of pairs and critical masks for each of the nineteen complexes.

**Exhaustive acyclicity proof.** For each complex, construct every codimension-one face incidence \(\tau\subset\sigma\). Orient an incidence from the upper to the lower face except for a matched incidence, which is oriented from lower to upper. A complete Kahn topological sort of this finite directed Hasse graph visits every face in all nineteen cases: there is no directed cycle. The verifier also checks that the listed pairs are genuine codimension-one incidences, disjoint, and cover the noncritical cells. The only unmatched cells are exactly one 0-simplex and, respectively, \(20\) or \(b(e)\) simplices of dimension three, with **no other unmatched dimensions**. The exhaustiveness follows from enumeration of all \(2^{18}-1\) possible nonempty masks and the incidence construction, not from random samples.

**Topological consequence.** Forman's acyclic-matching theorem gives a CW complex homotopy equivalent to the relevant matching complex, having one critical cell of dimension zero and exactly the stated number of critical cells of dimension three. Its two-skeleton is a point, so every three-cell has a constant attaching map from \(S^2\); consequently it is the indicated wedge of three-spheres. This rules out integral torsion and hidden attaching obstructions. Each deletion is proved independently under the same prescribed rule; none is inferred from symmetry.

## Verification
Run the following two standard-library Python programs alongside the included JSON certificate:

```sh
python3 verify_morse.py
python3 verify_chains.py
```

The first checks all nineteen acyclic matchings against every nonempty face and directed incidence and validates all stored certificates, returning `FRUCHT_EDGE_MATCHING_MORSE_OK`. The second independently enumerates the face families by brute-force edge-subset masks and computes boundary ranks over \(\mathbb F_2\). It verifies that the full complex has ranks \((17,100,233,144,8)\) in boundary degrees one through five and that every deletion has mod-two Betti vector concentrated in degree three with the stated rank; it returns `FRUCHT_EDGE_MATCHING_CHAINS_OK`. These field-rank checks corroborate the exhaustive Morse homotopy proof but are not offered as an integral proof by themselves. The exact console output is reproduced in `checks.txt`.

## Relationship to prior work
The graph originates in Frucht's work on cubic graphs with prescribed automorphism groups (1949). Classical matching-complex theory, including Wachs's 2003 survey and Jonsson's 2008 monograph, supplies the framework and general techniques, but their accessible descriptions and the checked topical sources do not give this exact graph-specific profile. The published result titled *The Frucht graph independence complex and its complete vertex-deletion classification* studies **vertex-independent sets of the original graph**, rather than disjoint **graph edges**, and its numerical homotopy statement does not imply this theorem. The record titled *Edge-orbit matching-complex splitting for the Franklin graph* deals with a distinct twelve-vertex cubic graph with two edge automorphism orbits, not the asymmetric Frucht graph; its profile cannot be transported to this graph. General results about matchings of complete graphs, chessboards, forests, small grids, and outerplanar graphs do not immediately settle these nineteen fixed complexes. The comparison is a claim of no identified implication in the examined sources, not of exhaustive publication priority.

## Limitations
This is an exact finite classification for the Frucht graph and its eighteen one-edge deletions, not a universal theorem for cubic, planar, or asymmetric graphs. The simplicial complexes may have faces of dimension five even though the Morse CW models have only zero- and three-cells. The chosen edge labels are necessary to interpret the deletion profile; the homotopy types themselves are label-independent. No independent external mathematical audit or definitive bibliographic uniqueness determination has been performed.

## References
1. R. Frucht, *Graphs of Degree Three with a Given Abstract Group*, Canadian Journal of Mathematics 1 (1949), 365–378, DOI:10.4153/CJM-1949-033-6 (journal issue dated 1 August 1949).
2. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385, DOI:10.1007/s00012-003-1825-1.
3. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer (2008), DOI:10.1007/978-3-540-75859-4; chapter on matchings, pp. 127–149.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
5. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first submission 17 December 2005).
6. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, Mathematika 66 (2020), 973–1002, DOI:10.1112/mtk.12049.
7. Public research records *The Frucht graph independence complex and its complete vertex-deletion classification* (2026) and *Edge-orbit matching-complex splitting for the Franklin graph* (2026); their scientific statements and full result documents were compared.
