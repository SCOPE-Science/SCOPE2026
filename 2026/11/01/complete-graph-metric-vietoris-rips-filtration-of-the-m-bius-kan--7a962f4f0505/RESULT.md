# Complete graph-metric Vietoris–Rips filtration of the Möbius–Kantor graph

## Finding
Let \(M=\mathrm{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph with shortest-path metric. For every real \(r\geq0\), define the inclusive Vietoris–Rips complex \(K_r\) on its vertices by declaring a nonempty subset a face exactly when every two of its vertices have graph distance at most \(r\). Then
\[
K_r\simeq
\begin{cases}
\bigvee^{15}S^0, & 0\leq r<1,\\
\bigvee^{9}S^1, & 1\leq r<2,\\
\bigvee^{9}S^2\vee\bigvee^{2}S^3, & 2\leq r<3,\\
S^7, & 3\leq r<4,\\
\ast, & r\geq4.
\end{cases}
\]
The reduced integral persistence barcode consists of fifteen intervals \([0,1)\) in degree zero, nine intervals \([1,2)\) in degree one, nine intervals \([2,3)\) in degree two, two intervals \([2,3)\) in degree three, and one interval \([3,4)\) in degree seven. In particular all integral homology groups are torsion-free.

More structurally, the two integral third-homology generators at \(r=2\) are the fundamental cycles of the induced crosspolytope-boundary subcomplexes on the two natural bipartition classes. These generators form an integral basis, not merely a rational basis.

## Assumptions and scope
Use vertices \(u_i,v_i\), \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\), with all indices modulo eight. The metric is intrinsic graph distance, **not** Euclidean distance in a geometric embedding. All scale inequalities are inclusive at the left endpoint. The assertion is for exactly this finite graph and all real nonnegative thresholds.

## Proof
**Distances and endpoints.** Exhaustive breadth-first searches from the explicitly specified sixteen vertices give pair-distance multiplicities \(24,48,40,8\) at distances \(1,2,3,4\), respectively. Thus the diameter is four and changes occur only at integer thresholds. The full distance-four relation is a matching of eight pairs covering all sixteen vertices. Consequently, the graph of pairs at distance at most three is the complete graph with a perfect matching removed, whose clique complex is the join of eight zero-spheres, hence \(K_3\cong S^7\). At radius four the complex is the full fifteen-simplex.

**The first two stages.** At radius zero the vertices are isolated. At radius one the complex is the original triangle-free connected graph, with sixteen vertices and twenty-four edges, so it is homotopy equivalent to a wedge of \(24-16+1=9\) circles.

**A finite acyclic matching at radius two.** Direct clique enumeration gives the face vector \((16,72,112,48)\); there are no faces above dimension three. The complete 130-step certificate `certificates/r2_matching.json` removes 118 free codimension-one face/coface pairs and declares twelve maximal faces critical. Independently checking every pair against the remaining down-closed face set, and topologically sorting the resulting oriented full Hasse graph, verifies the matching's acyclicity. The critical dimensions have multiplicities one in degree zero, nine in degree two, and two in degree three, with no critical one-cells. Forman's discrete-Morse theorem gives a CW model with exactly these cells. Its two-skeleton is a wedge of nine two-spheres.

**The integral third-homology generators.** The bipartition classes are \(A=\{u_i:i\text{ even}\}\cup\{v_i:i\text{ odd}\}\) and \(B=\{u_i:i\text{ odd}\}\cup\{v_i:i\text{ even}\}\). Each contains eight vertices. Within either class, exactly four disjoint pairs have distance four and every other distinct pair has distance two. Thus the induced subcomplex of \(K_2\) on each class is the join of four zero-spheres, i.e. a triangulated \(S^3\). The oriented fundamental cycles \(z_A,z_B\) each use sixteen tetrahedra with coefficients \(\pm1\), and their supports are disjoint. They are nonzero and independent in \(H_3(K_2;\mathbb Z)\), since \(K_2\) has no four-simplices. There are only two critical three-cells, so the Morse differential from degree three has rank zero and is identically zero over \(\mathbb Z\). Hence \(H_3(K_2;\mathbb Z)\cong\mathbb Z^2\) and \(H_2(K_2;\mathbb Z)\cong\mathbb Z^9\).

The two displayed third-homology cycles form an integral basis: rationally they span the rank-two kernel of the top simplicial boundary, and one pure tetrahedron from \(A\) and one from \(B\) have respective coefficients \(\pm1\) in their cycles and zero in the other. An integral cycle written as a rational combination must therefore have both coefficients integral. Since the Morse two-skeleton is \(\bigvee^9 S^2\), the Hurewicz map from its second homotopy group to its second integral homology is an isomorphism. The zero integral Morse differential implies the two three-cell attaching maps are null-homotopic. It follows that \(K_2\simeq\bigvee^9S^2\vee\bigvee^2S^3\).

**Persistence.** In consecutive stages the nonzero reduced homology occurs in disjoint degrees. Hence every nonzero bar starts at its respective integer threshold and ends at the next one. All groups and maps are integral, establishing the stated barcode without a field-coefficient substitution.

## Verification
Run `python3 verify.py` from the directory containing this file. The verifier uses only the Python standard library. It independently rebuilds the graph and all distance classes; tests all possible nonempty sixteen-vertex subsets for clique membership; replays each certificate step, checks the free-face and maximal-critical conditions, confirms down-closedness after every step, and independently tests directed Hasse-graph acyclicity. It also constructs and verifies the two oriented integral crosspolytope boundary cycles. A successful standalone run ends with `VERIFY_OK` and reproduces `verification_output.txt`. No exhaustive computation or mathematical step depends on files outside this package.

## Relationship to prior work
Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first submitted 2011-04-03), establishes the graph-power Rips viewpoint and general girth-stability criteria, and computes cycle-power cases. Its girth-at-least-seven stability result at scale two does **not** apply to this girth-six graph. Its stated graph-class results do not determine this mixed-dimensional example or its persistence barcode.

Marušič and Pisanski, *The remarkable generalized Petersen graph G(8,3)* (2000), identify the special graph, its incidence and Cayley interpretations, automorphisms and surface embeddings. Its inspected pages do not compute Rips homotopy or persistence. Other published calculations concerning the Möbius–Kantor **matching**, **independence** and **cut** complexes address different simplicial complexes. A published hexagon-packing theorem for scale-two Rips complexes assumes pairwise edge-disjoint six-cycles; this graph has twenty-four six-cycles and each of its twenty-four edges belongs to six of them, so that theorem's hypothesis fails.

## Limitations
The wedge equivalence is nonequivariant. No homotopy-coherent, symmetry-equivariant wedge splitting is claimed. The asserted barcode concerns the intrinsic graph metric only. The verification is a complete finite proof certificate for this particular graph; it does not imply a uniform theorem for arbitrary cubic graphs or generalized Petersen graphs. A bibliographically unindexed equivalent result may still exist; publication priority has not been independently certified.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (initial public preprint 2011-04-03), https://arxiv.org/abs/1104.0433 .
2. D. Marušič and T. Pisanski, *The remarkable generalized Petersen graph G(8,3)*, Mathematica Slovaca 50 (2000), 117–121; open text https://dmlcz-proxy.ics.muni.cz/handle/10338.dmlcz/133137 .
3. N. Bašić, G. Gévay and T. Pisanski, *The Möbius–Kantor graph is a faithful unit-distance graph*, arXiv:2508.06618 (2025); used only to distinguish Euclidean from intrinsic metrics.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; standard discrete-Morse framework.
