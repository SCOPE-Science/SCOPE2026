# Six-column stability for bidirected complete-bipartite multipath complexes

## Finding
Let \(D_{2,q}\) be the digraph obtained from the complete bipartite graph \(K_{2,q}\) by replacing every undirected edge with both opposing arcs. Let \(X_q\) be its multipath complex: vertices are directed arcs, and a set of arcs is a face exactly when it is a disjoint union of vertex-simple directed paths and isolated vertices. For **every integer \(q\ge6\)**,
\[
|X_q|\simeq\bigvee^{B_q}S^3,\qquad
B_q=q^4-8q^3+19q^2-14q+1.
\]
In particular \(X_q\) is \(2\)-connected, with torsion-free reduced integral homology concentrated in degree three. The cutoff is sharp: for \(q=2,3\) its first mod-two homology is nonzero, and for \(q=4,5\) its second mod-two homology is nonzero. The first stable multiplicities are \(B_6=169\), \(B_7=491\), and \(B_8=1105\).

## Assumptions and scope
The left bipartition class has two distinct vertices \(u_0,u_1\); the right class has \(q\) distinct vertices \(v_0,\ldots,v_{q-1}\). Both directed arcs \(u_i\to v_j\) and \(v_j\to u_i\) are present. Faces have in-degree and out-degree at most one at every vertex and contain no directed cycle, including directed two-cycles and directed four-cycles. Because the left class has only two vertices, every face contains at most four arcs. The homotopy equivalence is an integral topological statement, not merely an equality of Betti numbers or a rational equivalence.

## Proof
**1. A uniform finite-size bound and all face numbers.** An admissible arrow set contains at most two arrows departing from the left class and at most two entering it. For cardinalities one through four, direct enumeration according to the counts of left-to-right and right-to-left arrows gives
\[
(f_0,f_1,f_2,f_3)=\bigl(4q,\ 6q^2-4q,\ 4q(q-1)^2,\ q(q-1)^2(q-2)\bigr).
\]
For two-arcs, the all-forward and all-backward cases each have \(q(q-1)\) possibilities, whereas the one-each case has \(4q^2-2q\), excluding the two-cycles. For three arcs, the two orientation patterns contribute \(2q(q-1)^2\) apiece. For four arcs, choose the two distinct right endpoints of outgoing left arrows in \(q(q-1)\) ways; the incoming right sources must be distinct and avoid their corresponding opposite arrows and the four-cycle, leaving \((q-1)(q-2)\) possibilities. The Euler characteristic is therefore
\[
\chi(X_q)=4q-(6q^2-4q)+4q(q-1)^2-q(q-1)^2(q-2),
\]
so \(1-\chi(X_q)=q^4-8q^3+19q^2-14q+1\).

**2. The first six columns and the face-poset patchwork.** Fix six distinguished right vertices and call their \(24\) incident arcs *probe arrows*. All remaining arcs are *external*. For a nonempty face \(F\), put \(W(F)=F\cap E\), the set of selected external arrows. This is an order-preserving map from the nonempty face poset to the poset of external-arrow faces. For each fixed \(W\), represent the remaining probe arrows by a bit mask \(U\), subject precisely to the requirement that \(W\cup U\) is a multipath. On each fiber, run the deterministic sequential-toggle matching: in the fixed index order of the \(24\) probe arrows, pair every still-unmatched \(U\) without that arrow with its still-unmatched valid superset obtained by inserting the arrow. Disjoint matchings in fibers of an order-preserving poset map assemble to an acyclic matching whenever each fiber matching is acyclic (the poset patchwork lemma). The verifier also checks each finite fiber's acyclicity **directly** by topological sorting the reversed matched Hasse edges, so no unproved claim that sequential toggling always works on arbitrary complexes is required.

**3. Exhaustiveness of the finite certificate.** Every face has at most four arrows, hence every external configuration \(W\) uses at most four external right vertices. Because external vertices are interchangeable, the isomorphism type of its probe-compatible fiber is represented by a configuration on just four named external right vertices. Thus the checker exhaustively tests **all external configurations for every \(q\ge6\)** by using four symbolic external vertices, not by guessing from a few values of \(q\). There are exactly \(312\) nonempty valid configurations: \(16\) of size one, \(80\) of size two, \(144\) of size three, and \(72\) of size four. Applying the precisely specified toggle algorithm, constructing the entire fiber Hasse diagram, and checking directed acyclicity yields the following complete exhaustive critical-cell profiles:

| External arrows in \(W\) | Fiber patterns | Unmatched probe masks per fiber | Unmatched probe-mask size |
|---|---:|---:|---:|
| 1 | 16 | 71 | 3 |
| 2 | 56 | 19 | 2 |
| 2 | 24 | 25 | 2 |
| 3 | 144 | 5 | 1 |
| 4 | 72 | 1 | 0 |

Every unmatched total face with nonempty \(W\) therefore has **four** arrows, i.e. dimension three, independent of \(q\). To make this a fully checkable mathematical certificate, the complete standalone program `verify.py` generates the valid faces from the directed-graph definition, computes each greedy pair, explicitly constructs every fiber's Hasse orientations, checks for directed cycles by an exact integer topological sort, and asserts each entry of the displayed table. No external package, file, or precomputed opaque dataset is needed. The finite enumeration covers all possibilities by the four-external-vertex argument above.

**4. The empty external configuration.** For \(W=\varnothing\), all nonempty faces of the six-column probe complex are enumerated, totaling \(1416\) simplices. The same explicitly defined toggle matching contains \(623\) disjoint pairs, and its complete Hasse orientation is verified acyclic. The \(170\) unmatched faces comprise **exactly one vertex and \(169\) tetrahedra**. Therefore the patched matching on all nonempty faces of \(X_q\) has exactly one critical zero-cell, no critical one- or two-cells, and all remaining critical cells in degree three. The patchwork lemma applies since the external-set projection is order preserving and each fiber check is exact; no unexamined higher-cardinality external face exists.

**5. Integral homotopy and multiplicities.** Discrete Morse theory converts this acyclic face matching into a CW homotopy model with one zero-cell and only three-cells otherwise. All three-cell attaching maps into the single point are constant, so its homotopy type is a wedge of three-spheres. The reduced Euler characteristic of that CW complex is \(-B_q\); Step 1 determines the number of three-cells as exactly the displayed quartic polynomial. This proves the full integral classification for all \(q\ge6\).

**6. Sharp cutoff.** Separate exact simplicial boundary calculations over \(\mathbb F_2\), directly from the original digraph definition, give the ordinary Betti vectors in degrees zero through three as follows: \(q=2\): \((1,3,2,0)\); \(q=3\): \((1,1,6,0)\); \(q=4\): \((1,0,8,1)\); \(q=5\): \((1,0,1,32)\); \(q=6\): \((1,0,0,169)\). Hence none of \(q=2,3,4,5\) is two-connected; together with Step 5 this makes six the sharp threshold for \(q\ge2\). The low-parameter calculations are finite exact conclusions, while the all-parameter theorem comes from Steps 2–5.

## Verification
Execute `python3 verify.py` with Python's standard library. A successful fresh replay reports `BASE_OK`, `UNIVERSAL_FIBERS_OK`, five `LOW_BOUND_OK` lines, and `VERIFY_OK`. The checker generates every accepted arrow subset for the six-column base, the complete set of \(312\) possible nonempty external fiber patterns, all matching pairs and Hasse edges, and exact binary ranks for the low-parameter boundary. The universal part is a finite **symbolic case certificate** because every external face uses at most four columns; it is not a finite-data extrapolation from tested alphabet sizes. The code checks exactly the nonstandard combinatorial critical-cell and acyclicity assertions used in the proof.

## Relationship to prior work
Caputi–Collari–Smith (2026) compute homotopy and homology of multipath complexes of bidirected paths and polygons, motivating the study of other bidirected graph families. Those sparse path and polygon classifications do not cover the dense bidirected \(K_{2,q}\) family, which contains many four-cycles for \(q\ge3\). Caputi–Collari–Di Trani–Smith (2022/2024) analyze multipath complexes of several digraph classes; their "complete bipartite graph" example is an **alternating, one-way orientation** with arrows from one bipartition class to the other and does not include reverse arrows. Its Euler polynomial does not imply the present multipath homotopy theorem. Indexed related results on bidirected double-star trees, polygonal dihedral homology, ordinary discrete-Morse matching complexes and bounded-degree matching complexes likewise concern different admissibility conditions or different graphs. The new statement is the sharp, all-\(q\) integral sphere-wedge classification for bidirected \(K_{2,q}\), not the general definition of multipaths, the existing alternating-digraph Euler calculation, or the standard patchwork theorem.

## Limitations
The result covers the two-vertex left class for \(q\ge6\), plus an exact non-two-connectivity boundary for \(2\le q\le5\); it does not claim homotopy types for those four smaller cases, larger left classes, other orientations, or equivariant actions. The finite certificate is exact for the stated symbolic cases, but independent external replication and formal proof-assistant certification have not been performed. Previously unindexed equivalent literature cannot be ruled out. This is a mathematical argument and reproducibility package, not a claim of independent audit or publication priority.

## References
1. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public 2026-01-09, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public 2022-08-09; Mathematika 70 (2024), e12235, https://arxiv.org/abs/2208.04656.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Standard acyclic-matching and discrete-Morse CW reduction.
4. The acyclic-matching patchwork (cluster) lemma for an order-preserving poset map; see D. Kozlov, *Combinatorial Algebraic Topology*, Springer (2008), chapter on discrete Morse matchings.
