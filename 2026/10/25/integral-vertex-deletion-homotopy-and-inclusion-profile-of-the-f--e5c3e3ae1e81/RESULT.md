# Integral vertex-deletion homotopy and inclusion profile of the Frucht two-independence complex

## Finding
Let \(F\) be the twelve-vertex Frucht graph, labeled explicitly below. Let \(K=\operatorname{Ind}_{2}(F)\) and \(K_v=\operatorname{Ind}_{2}(F-v)\), where a simplex is a vertex subset whose induced connected components have at most two vertices. The inclusion \(j_v:K_v\hookrightarrow K\) is simplicial.

For each vertex \(v\), the integral homotopy type is \(K_v\simeq\bigvee^{b_v}S^3\), with
\[
(b_0,b_1,\ldots,b_{11})=(2,2,2,1,2,2,1,3,1,2,2,4).
\]
Here a one-fold wedge is a single three-sphere. The full complex is \(K\simeq S^3\). All other reduced integral homology groups of \(K_v\) vanish.

The induced map on integral third homology
\[
(j_v)_*:\widetilde H_3(K_v;\mathbb Z)\longrightarrow\widetilde H_3(K;\mathbb Z)\cong\mathbb Z
\]
is **zero precisely for** \(v\in\{0,6,8,9\}\), and is **surjective for each of the other eight vertices**. Thus equal homology ranks do not determine whether deletion preserves the generator: for instance, deleting vertex \(1\) gives a surjection and deleting vertex \(0\) gives the zero map, although both deletion complexes have two independent third-homology generators.

## Assumptions and scope
The labeled edge set of \(F\) is
\[
\begin{aligned}
E(F)=\{&(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),\\
&(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),\\
&(7,11),(8,11),(8,9),(10,11)\}.
\end{aligned}
\]
The accompanying verifier checks explicitly that this labeling is isomorphic to the standard Frucht LCF presentation with offsets \((-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)\). A subset \(\sigma\) of vertices is a face exactly when every vertex in \(\sigma\) has at most one neighbor in \(\sigma\). The empty face is included in the abstract complex and excluded from the computational Hasse-diagram list. The assertions are over \(\mathbb Z\), not merely over a finite field, and refer to these exact vertex labels.

## Proof
**Complete finite model.** Represent a face by the twelve-bit integer \(\sum_{v\in\sigma}2^v\). Directly enumerate all \(4095\) nonempty subsets, retaining those satisfying the induced-degree condition. This produces \(824\) faces with dimension-indexed face numbers \((12,66,190,293,209,53,1)\). For each deletion discard faces containing the deleted vertex. These are complete, not sampled, enumerations.

**Integral discrete-Morse reduction.** For a fixed vertex order \(w_1,\ldots,w_s\), process the vertices in that order; whenever a currently unmatched face \(\sigma\) omits \(w_i\) and both \(\sigma\) and \(\sigma\cup\{w_i\}\) are still unmatched faces, pair them. Use increasing order for the full graph and for all vertex deletions except \(v\in\{0,4,10,11\}\). For these four deletions use, respectively, the orders
\[
\begin{array}{c|l}
0&(4,3,2,5,6,10,7,1,9,11,8)\\
4&(3,11,9,1,5,0,8,10,7,2,6)\\
10&(5,6,2,4,3,7,1,9,8,11,0)\\
11&(8,6,3,4,5,7,1,10,0,9,2).
\end{array}
\]
Each resulting matching is acyclic: the script independently constructs every Hasse cover arrow, reverses each matched cover, and performs a successful topological ordering of the entire directed Hasse diagram. For the full complex, \(410\) pairs leave exactly one critical \(0\)-cell, two critical \(3\)-cells, and one critical \(4\)-cell. The exact integral boundary of the critical \(4\)-cell on the ordered critical \(3\)-cells is \((0,1)\). There are no other positive-dimensional critical cells.

The deletion complexes have just one critical vertex and \(b_v\) critical \(3\)-cells, except deletion \(v=8\), which has a critical vertex, two critical \(3\)-cells, and one critical \(4\)-cell. Its unique integral \(4\)-to-\(3\) incidence row is also \((0,1)\). In the two exceptional cases a unit Morse boundary cancels a critical \(3\)-/\(4\)-cell pair, leaving a CW model with one vertex and, respectively, one \(3\)-cell. For all remaining deletions the CW model already has just one vertex and \(b_v\) \(3\)-cells. No nontrivial attaching maps exist into the zero- and three-dimensional skeleta in these models: they have the claimed wedge-of-three-spheres homotopy types. The unit incidence and cancellations are over the integers, precluding hidden torsion.

**Naturality of the inclusion map.** In each deletion matching, every critical three-cell whose boundary contains a matched two-cell can be lifted to an explicit integral three-cycle by subtracting the signed boundaries of the matching partner three-cells; the elimination terminates by the verified acyclic matching. Regard the lifted cycle as a chain in \(K\). Reduce it by the signed boundaries of the full matching's \((3,4)\)-pairs, obtaining coefficients on the two full critical three-cells. Since the full four-cell differential is \((0,1)\), the first critical three-cell represents the integer generator of \(H_3(K;\mathbb Z)\). Exact integer coefficients for the deletion cycles vanish all together precisely at \(v\in\{0,6,8,9\}\); at every other vertex at least one coefficient has absolute value \(1\). For \(v=8\) the critical cycle not killed by the unit four-boundary is used. Therefore the inclusion images are zero or all of \(\mathbb Z\), respectively. The standalone checker reconstructs the cycle lifts and tests all these coefficients without relying on Betti numbers.

## Verification
Run \(`python3 frucht_two_independence_verify.py`\) using Python's standard library. The program rebuilds the Frucht graph from its edge list, checks the LCF isomorphism, enumerates each of the thirteen full/deletion complexes, constructs all matchings, and verifies their acyclicity against every face incidence. It checks exact signed incidence coefficients, integral three-cycle lifting and inclusion reduction, and also independently computes reduced homology for each complex directly from unreduced simplicial boundary matrices over \(\mathbb F_2\). A second independent direct mod-two kernel/image computation for the inclusion maps agrees at all twelve vertices. Mod-two computations corroborate but do not replace the exact integral Morse and map calculations. A normal successful run terminates with the line `PASS: acyclic matchings, integral incidence and inclusion maps, and independent F2 chain matrices for all 13 complexes`.

## Relationship to prior work
The definition and 2025 structural study of higher-independence complexes by Ghosh and Selvaraja (arXiv:2505.06614) motivate studying the first higher-independence parameter beyond trees and block graphs. Sawant (arXiv:2605.25150) gives newer structural results on trees. Neither paper's inspected main results determines these deletion complexes or their integral inclusion maps for the non-block, cyclic Frucht graph. Earlier computations establish the full \(\operatorname{Ind}_2(F)\simeq S^3\) homotopy type, which is **not** claimed as new here. Published ordinary-independence calculations determine \(\operatorname{Ind}_1(F)\) and its vertex-deletion profile, but that is a different simplicial complex and does not imply the present \(r=2\) deletion ranks or map images. The new contribution is the **complete twelve-vertex integral deletion-and-inclusion classification**.

## Limitations
This is an exact finite graph theorem, not an infinite-family classification. It gives homotopy types of the twelve deletion complexes and the maps on \(H_3\), not full homotopy classes of the twelve simplicial inclusions. It depends on a fully reproducible finite exact certificate, not an unaudited empirical inference. Equivalent calculations may exist outside the inspected literature; no independent external verification is asserted.

## References
1. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first publicly posted 2025-05-10; https://arxiv.org/abs/2505.06614 .
2. R. Sawant, research on higher independence complexes of trees, arXiv:2605.25150, 2026; https://arxiv.org/abs/2605.25150 .
3. Published Frucht-graph ordinary independence and deletion classification: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2 .
4. Standalone exact verifier supplied with this result: `frucht_two_independence_verify.py`.
