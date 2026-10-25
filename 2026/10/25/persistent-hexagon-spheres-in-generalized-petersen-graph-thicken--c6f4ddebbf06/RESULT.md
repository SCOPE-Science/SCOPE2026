# Persistent hexagon spheres in generalized Petersen graph thickenings

## Finding

Let \(n\ge 19\) be an integer and let \(G_n=GP(n,3)\) be the generalized Petersen graph on vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). Give its vertex set the unit-edge shortest-path metric. For the **inclusive radius-two** Vietoris–Rips complex \(K_n=\operatorname{VR}_{\le 2}(V(G_n))\),
\[
\boxed{K_n\simeq S^1\vee\bigvee^{n}S^2.}
\]
The complete nonempty face vector is \((2n,9n,10n,2n)\). Thus \(\pi_1(K_n)\cong\mathbb Z\), \(\widetilde H_1(K_n;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_2(K_n;\mathbb Z)\cong\mathbb Z^n\), and all other reduced integral homology groups vanish.

More precisely, the map induced by the radius-one inclusion \(G_n\hookrightarrow K_n\) is a surjection \(H_1(G_n;\mathbb Z)\cong\mathbb Z^{n+1}\twoheadrightarrow H_1(K_n;\mathbb Z)\cong\mathbb Z\). Its kernel has the **primitive integral basis** given by the \(n\) six-edge loops
\[
\gamma_i=(u_i,u_{i+1},u_{i+2},u_{i+3},v_{i+3},v_i,u_i),\qquad i\in\mathbb Z/n\mathbb Z.
\]
Each \(\gamma_i\) supports an octahedral two-sphere in \(K_n\), and these \(n\) spheres represent an **integral basis** of \(H_2(K_n;\mathbb Z)\).

Let \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) act by \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\), \(s(u_i)=u_{-i}\), \(s(v_i)=v_{-i}\). With the explicit orientations in the proof, its actions on the integral bases satisfy
\[
\boxed{r[z_i]=[z_{i+1}],\qquad s[z_i]=[z_{-i-3}],}
\qquad
\boxed{r[a]=[a],\qquad s[a]=-[a]},
\]
where \([z_i]\) is the two-sphere basis and \([a]\) is the outer-circle generator. Therefore second homology is the **integral permutation lattice of the \(n\) hexagons**, while first homology carries the reflection-sign character.

The eventual range has a genuine boundary obstruction: for \(n=18\), exact simplicial boundary elimination over \(\mathbb F_2\) gives \(\widetilde\beta_1=0\) and \(\widetilde\beta_2=23\). Thus the above wedge assertion cannot be extended to \(n=18\) with the same formula. No integral homotopy classification at \(n=18\) is asserted.

## Assumptions and scope

All vertex subscripts are taken modulo \(n\), and every graph edge has unit length. The metric is defined **only on graph vertices**, not continuously along their incident edges. The inclusive radius-two complex consists of all nonempty subsets whose pairwise graph distances are at most two; it is the clique complex of the second graph power. The theorem concerns every integer \(n\ge19\), including multiples of three, and only scales one and two. The group \(D_n\) is the indicated natural dihedral subgroup of graph automorphisms, without any claim to determine the full graph automorphism group.

For a graph vertex \(w\), write \(N[w]\) for its closed graph neighborhood. Let \(\Delta[N[w]]\) denote the full simplex on that neighborhood. A simplicial collapse is an elementary free-face deletion. Homology is reduced only when the tilde is displayed; all assertions of integrality concern ordinary integral simplicial/cellular chains.

## Proof

**1. Girth and the only hexagons.** The graph has no cycle of lengths three, four, or five. Indeed a simple cycle with no spokes lies entirely on the outer ring (length \(n\)) or an inner ring (length \(n/\gcd(n,3)\ge7\)). A simple cycle using spokes uses an even positive number; between any consecutive spokes it must contain a horizontal edge, hence a cycle of at most six edges has exactly two spokes. Such a cycle consists of an outer path of \(a\ge1\) edges and an inner path of \(b\ge1\) edges, with total length \(a+b+2\). Along a simple path of length at most four, all outer steps have the same direction, as do all inner steps (no backtracking). Its endpoints coincide modulo \(n\) only if \(\pm a\pm3b\equiv0\pmod n\). For total length at most six, \(a+b\le4\), so \(|\pm a\pm3b|\le12<n\). Equality to zero is possible only for \((a,b)=(3,1)\), with opposite signs. Consequently the only simple hexagons are precisely the \(n\) cycles \(\gamma_i\) above. In particular, the girth is six. They **are not edge-disjoint**: every outer edge belongs to three distinct \(\gamma_i\).

**2. Classify all cliques in the graph square.** Set
\[
B_n=\bigcup_{w\in V(G_n)}\Delta[N[w]]\subseteq K_n.
\]
The graph has no four-cycles, so a pair of vertices at distance two has a unique common neighbor. The absence of cycles of lengths three and five implies that any triple of pairwise distance at most two which is not contained in one closed neighborhood consists of three distance-two pairs having three distinct intermediates. Those vertices and their intermediates form a simple hexagon. Conversely, alternating vertices of a hexagon are at pairwise distance two and have no common neighbor, by uniqueness of midpoints. The triangles outside \(B_n\) are therefore exactly the \(2n\) triangles
\[
T_i^+=\{u_i,u_{i+2},v_{i+3}\},\qquad T_i^-=\{u_{i+1},u_{i+3},v_i\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
None extends to a four-vertex clique. To verify this without relying on finite enumeration, the radius-two balls are, for all indices \(j\),
\[
\begin{aligned}
B_2(u_j)&=\{u_{j-2},u_{j-1},u_j,u_{j+1},u_{j+2}\}\cup\{v_{j-3},v_{j-1},v_j,v_{j+1},v_{j+3}\},\\
B_2(v_j)&=\{v_{j-6},v_{j-3},v_j,v_{j+3},v_{j+6}\}\cup\{u_{j-3},u_{j-1},u_j,u_{j+1},u_{j+3}\}.
\end{aligned}
\]
The modular offset sets do not acquire extra equalities in the relevant intersections when \(n\ge19\). Direct intersection yields
\[
B_2(u_j)\cap B_2(u_{j+2})\cap B_2(v_{j+3})=\{u_j,u_{j+2},v_{j+3}\},
\]
\[
B_2(u_j)\cap B_2(u_{j+2})\cap B_2(v_{j-1})=\{u_j,u_{j+2},v_{j-1}\}.
\]
The second covers \(T_i^-\) after substituting \(j=i+1\). Thus exceptional triangles are maximal. Finally, every clique not contained in \(B_n\) contains an exceptional triangle: choose any distance-two pair and its unique midpoint; a third vertex not in its closed neighborhood gives such a triple. Thus **the only simplices outside \(B_n\) are these \(2n\) triangles**. The \(2n\) neighborhood tetrahedra each contribute four distinct centered triangles, and the \(6n\) distance-two edges have unique midpoints. This gives the full face vector \((2n,9n,10n,2n)\).

**3. The centered subcomplex collapses to the original graph.** For each \(w\), list its three neighbors \(a,b,c\). In \(B_n\), the triangle \(abc\) is a free face of the tetrahedron \(wabc\): its distance-two pairs have unique center \(w\). Remove this pair. Then, in any order, remove the three pairs \((ab,wab)\), \((ac,wac)\), \((bc,wbc)\). Each distance-two edge is contained in exactly one remaining triangle and no higher simplex. All these removals are compatible across centers, precisely because a distance-two pair has a unique midpoint. After \(4(2n)=8n\) elementary pairs, the remaining simplicial complex is exactly \(G_n\). Hence \(B_n\searrow G_n\), relative to the original edges. In particular, the distance-two edge \(ab\) retracts homotopically onto the two-edge path \(a-w-b\) through its unique midpoint.

**4. Attach paired hexagonal disks.** The complex \(K_n\) is obtained from \(B_n\) by adjoining the two two-simplices \(T_i^+,T_i^-\) for each \(i\). Under the equivalence \(B_n\searrow G_n\), the boundary of either special simplex maps to the same six-edge loop \(\gamma_i\), up to orientation and free parametrization. For \(T_i^+\), the three distance-two edges have respective midpoints \(u_{i+1}\), \(u_{i+3}\), \(v_i\); for \(T_i^-\), they have midpoints \(u_{i+2}\), \(v_{i+3}\), \(u_i\). Homotopy invariance of cellular attachment therefore replaces \(K_n\), up to homotopy, by \(G_n\) with **two two-disks attached to each** \(\gamma_i\).

First attach one disk along every \(\gamma_i\), obtaining a two-dimensional CW complex \(W_n\). The second disk of each pair now attaches along a nullhomotopic loop (nullhomotopic using its companion disk) and therefore adds a wedge summand \(S^2\). Thus \(K_n\simeq W_n\vee\bigvee^nS^2\). Each loop \(\gamma_i\) traverses the inner edge \(v_iv_{i+3}\), which appears in **no other** \(\gamma_j\). Consequently \(W_n\) admits \(n\) cellular elementary collapses removing each chosen disk with its unique inner edge. The remaining graph is the outer \(n\)-cycle together with all \(n\) pendant spokes and their inner endpoints, which collapses to the outer circle. Therefore \(W_n\simeq S^1\), proving the integral homotopy assertion.

The inner-edge coordinates also prove that the \(n\) classes \([\gamma_i]\) are primitive and independent in \(H_1(G_n;\mathbb Z)\): their coefficients on the \(n\) oriented inner edges form an identity matrix, and removing the inner edges leaves a connected unicyclic graph. Thus they form exactly the kernel of the induced map to \(H_1(K_n;\mathbb Z)\).

**5. Integral octahedral basis and symmetry.** In the hexagon \(\gamma_i\) order the six vertices as
\[
(w_0,w_1,w_2,w_3,w_4,w_5)
=(u_i,u_{i+1},u_{i+2},u_{i+3},v_{i+3},v_i).
\]
Its induced radius-two complex is the boundary of an octahedron: the only nonedges join the opposite pairs \((w_0,w_3)\), \((w_1,w_4)\), \((w_2,w_5)\). Define the oriented integral cycle, with the displayed triple order specifying orientation,
\[
z_i=\sum_{a,b,c\in\{0,1\}}(-1)^{a+b+c}
[w_{3a},w_{1+3b},w_{2+3c}].
\]
It is the join of the three oriented zero-spheres \((w_0-w_3)*(w_1-w_4)*(w_2-w_5)\); its simplicial boundary vanishes term by term. In the paired-disk CW model, it is the generator supplied by the **difference of the two disk fillings** of \(\gamma_i\), so the \([z_i]\) form a primitive integral basis of second homology, not merely a rational basis.

Rotating all indices carries each ordered hexagon to the next with the same axis order, hence \(r[z_i]=[z_{i+1}]\). Reflection carries the ordered six vertices of \(\gamma_i\) into those of \(\gamma_{-i-3}\) by the position map \(j\mapsto3-j\pmod6\). This swaps the two members of the first opposite pair, contributing sign \(-1\), and exchanges the other two opposite pairs, also contributing sign \(-1\). Their product is \(+1\), yielding \(s[z_i]=[z_{-i-3}]\). The outer-circle generator is preserved by rotation and reversed by reflection. These calculations prove the claimed integral \(D_n\)-modules.

**6. The sharp finite obstruction at eighteen.** At \(n=18\), the inner graph consists of three additional six-cycles. Exhaustive clique enumeration gives nonempty face counts \((36,162,186,36)\). Binary simplicial boundary elimination in positive degrees yields ranks \((35,127,36)\), so reduced mod-two Betti numbers are \((0,0,23,0)\). In particular its first mod-two Betti number is zero, ruling out the proposed stable one-circle wedge at that value. The complete finite routine is supplied separately and checks these ranks using exact bit-vector elimination.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The verifier builds shortest-path square graphs directly from adjacency, enumerates every clique, and compares the resulting simplicial complex with the stated centered tetrahedra and exceptional triangles for **every integer** \(19\le n\le72\). It independently enumerates all simple six-cycles in this range. For eight sample sizes it replays all centered free-face collapses and constructs the complete signed octahedral cycles, checks their integral boundaries, and checks rotation/reflection signs on every sphere; for nine sample sizes it computes mod-two boundary ranks. It separately certifies the exact \(n=18\) rank obstruction. The companion `verification_output.txt` records the actual successful run.

The finite tests are checks, not proofs for infinitely many \(n\); Steps 1–5 give the uniform argument. Neither a complete higher-scale persistence classification nor the integral homotopy type for \(n=18\) is claimed.

## Relationship to prior work

Adamaszek's *Clique complexes and graph powers* [1, Proposition 2.2] collapses scale-two Rips complexes when girth is at least seven. Here girth is **six**, so its hypotheses fail. Theorem 3.1 of [1] requires every clique of the graph square to lie in a closed original-graph neighborhood, but the two explicit triangles per \(\gamma_i\) violate that requirement. Its cycle-power calculation explains the isolated six-cycle octahedron, not the attachment interactions or integral dihedral structure for \(GP(n,3)\).

The published hexagon-packing statements [3,4] require **pairwise edge-disjoint six-cycles**. In \(GP(n,3)\), every outer edge belongs to three hexagons, so their theorems cannot be applied, and their conclusions do not imply the present theorem. The published generalized-Petersen scale-two result [5] concerns \(GP(n,2)\), whose stable complex is a circle; it does not determine \(GP(n,3)\), which has different short-cycle and sphere-generation mechanisms.

Metric-gluing results [2] apply to wedge and sufficiently short path gluings under additional incidence conditions. The mutually overlapping length-three outer paths and 3-regular structure here do not satisfy the cited direct decomposition hypotheses; [2] does not supply this classification. Searches under graph-square, generalized Petersen, hexagonal graph, radius-two Rips, homotopy, and dihedral-module formulations did not identify a result implying the above combined homotopy, persistence, and integral representation. An unindexed equivalent statement remains possible.

## Limitations

The proof does not classify \(GP(n,k)\) for arbitrary \(k\), the whole Rips filtration, Euclidean metrics, or the full automorphism action. The threshold claim at eighteen is a mod-two obstruction only. The integral dihedral representation uses the explicitly specified subgroup and orientation convention. A negative bibliographic search is not a uniqueness theorem; overlap with unindexed literature remains an originality risk. No independent mathematical audit has been performed.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (public 3 April 2011), especially Proposition 2.2, Theorems 3.1–3.2 and Section 6; full text https://arxiv.org/html/1104.0433v3.
2. M. Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224v1 (public 18 December 2017), especially Theorem 3.15 and Section 4; full text https://arxiv.org/html/1712.06224v5.
3. *A hexagon-packing classification of scale-two graph Rips complexes*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb.
4. *Scale-two Rips complexes of graphs with edge-disjoint hexagons*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-two-rips-complexes-of-graphs-with-edge-disjoint-hexagons--3e8f2e09a00a.
5. *A sharp twelve-to-thirteen Rips collapse transition in generalized Petersen graphs*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-twelve-to-thirteen-rips-collapse-transition-in-generaliz--7ffdbeea612d.
