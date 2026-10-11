# Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs

## Finding

For each integer \(m\ge 3\), form the graph \(\Theta_m^{(3)}\) from \(m\) internally vertex-disjoint, length-three paths between two poles. Its inclusive graph-metric Vietoris–Rips filtration has exactly the following homotopy types for all real \(r\ge0\):

\[
\operatorname{VR}_{\le r}(\Theta_m^{(3)})\simeq
\begin{cases}
\bigsqcup^{2m+2}\{*\}, &0\le r<1,\\
\bigvee^{m-1}S^1, &1\le r<2,\\
\bigvee^{m-1}S^2, &2\le r<3,\\
\{*\}, &r\ge3.
\end{cases}
\]

Its **reduced integral persistent homology** consists of \(2m+1\) bars in degree \(0\) on \([0,1)\), \(m-1\) bars in degree \(1\) on \([1,2)\), and \(m-1\) bars in degree \(2\) on \([2,3)\), without any further bars or torsion.

There is also an exact **integral equivariant refinement**. Put \(\Lambda_m=\{(z_1,\ldots,z_m)\in\mathbb Z^m:\sum_i z_i=0\}\), with the natural coordinate-permutation action of \(S_m\); denote by \(\varepsilon\) the sign representation of the group \(C_2\) that interchanges the poles. The full graph automorphism group for \(m\ge3\) is \(S_m\times C_2\), and its homology modules are

\[
\widetilde H_1(\operatorname{VR}_{\le1};\mathbb Z)\cong\Lambda_m\boxtimes\varepsilon,
\qquad
\widetilde H_2(\operatorname{VR}_{\le2};\mathbb Z)\cong\Lambda_m\boxtimes\mathbf1.
\]

Thus the pole-exchange involution reverses each scale-one cycle class but fixes every scale-two homology class. For any arm permutation \(\sigma\in S_m\), the trace in the nonzero scale-two homology group is \(\#\operatorname{Fix}(\sigma)-1\).

## Assumptions and scope

The graph has distinct vertices \(p,q,a_1,\ldots,a_m,b_1,\ldots,b_m\), and precisely the edges \(pa_i\), \(a_ib_i\), \(b_iq\) for \(1\le i\le m\). It is an unweighted, finite, simple graph with \(2m+2\) vertices, diameter \(3\), and girth \(6\). Distance always means shortest-path distance **between graph vertices**, not distance between arbitrary points on a continuous metric-graph realization. The complex \(\operatorname{VR}_{\le r}\) includes a simplex precisely when every pair of its vertices is at distance at most \(r\). There is no factor-of-two convention in the parameter. All statements concern \(m\ge3\); the tested six-cycle case \(m=2\) has a larger graph automorphism group and is not included in the full-group assertion.

## Proof

**Step 1 (distance classification).** The poles have distance \(d(p,q)=3\). Each internal point is at distance at most \(2\) from each pole. Within each of the two layers \(A=\{a_i\}\) and \(B=\{b_i\}\), distinct points have distance \(2\). Across layers, \(d(a_i,b_j)=1\) when \(i=j\) and \(d(a_i,b_j)=3\) when \(i\ne j\). These formulas follow by the only available three-edge routes through the poles or within an arm and exhaust all unordered pairs.

**Step 2 (small and large scales).** For \(0\le r<1\), no distinct vertices span an edge, leaving \(2m+2\) points. For \(1\le r<2\), the complex is exactly the original triangle-free graph, with \(3m\) edges and \(2m+2\) vertices. It is connected and has cycle rank \(3m-(2m+2)+1=m-1\). For \(r\ge3\), all pairs are adjacent in the threshold graph, so the entire complex is a simplex.

**Step 3 (an exact join at scale two).** Denote by \(S^0\) the zero-dimensional simplicial complex on the two poles, which are not adjacent at scale \(2\). The distance classification implies every pole is connected to every internal vertex. The induced complex on the internal vertices is

\[
L_m=\Delta(A)\ \cup\ \Delta(B)\ \cup\ \bigcup_{i=1}^m [a_i,b_i],
\]

where \(\Delta(A)\) and \(\Delta(B)\) are full simplices and the only cross-layer edges are the \(m\) disjoint matching edges. The flag property therefore proves the **simplicial identity**

\[
\operatorname{VR}_{\le2}(\Theta_m^{(3)})=S^0*L_m.
\]

**Step 4 (integral homotopy type).** Geometrically, each of the two disjoint simplices in \(L_m\) is a contractible CW subcomplex. Collapsing them to separate points is a homotopy equivalence because the inclusions are cofibrations and each collapsed subcomplex is contractible. The quotient is the connected graph with two vertices and \(m\) parallel edges, which is homotopy equivalent to \(\bigvee^{m-1}S^1\). Hence \(L_m\simeq\bigvee^{m-1}S^1\). Its simplicial join with \(S^0\) is its (unreduced) suspension; the suspension of a connected based graph is homotopy equivalent to \(\bigvee^{m-1}S^2\). This establishes the all-parameter scale-two assertion and integral torsion-freeness. The four threshold complexes are constant between the integers \(0,1,2,3\), proving the displayed persistent intervals and their integer endpoints.

**Step 5 (integral symmetry).** The two poles are exactly the degree-\(m\) vertices when \(m\ge3\). Every graph automorphism thus permutes the \(m\) arms and either fixes or swaps both poles. This gives exactly \(S_m\times C_2\). Orient every three-edge path from \(p\) to \(q\). Integral graph cycles are precisely sums of these paths with total coefficient zero, and so give \(\Lambda_m\); swapping poles reverses every such path. At scale two orient each bridge in \(L_m\) from \(a_i\) to \(b_i\). Contracting the two simplex pieces, or equivalently applying Mayer–Vietoris, identifies \(H_1(L_m;\mathbb Z)\) with the same sum-zero bridge-coefficient lattice \(\Lambda_m\). Here swapping the two internal layers reverses every bridge, acting by minus the identity. Finally, the natural reduced-join isomorphism

\[
\widetilde H_2(S^0*L_m;\mathbb Z)\cong
\widetilde H_0(S^0;\mathbb Z)\otimes\widetilde H_1(L_m;\mathbb Z)
\]

has no Tor term. The pole interchange acts by minus the identity on the first factor and also by minus on the second, so their product is plus the identity. Arm permutations act as standard coordinate permutations. This proves the claimed integral representations and character.

## Verification

The accompanying standalone, Python-standard-library script `theta_rips_verifier.py` independently constructs the graph metric using breadth-first search, enumerates all simplices at scales one and two, and checks the exact internal-simplex/matching description for \(2\le m\le8\). Complete mod-two boundary elimination confirms the Betti-number predictions throughout this range. For \(2\le m\le5\), all \(608\) signed simplicial Lefschetz traces arising from the permutations of the arms and the pole involution are checked against the equivariant formulas. Running `python3 theta_rips_verifier.py` terminates with `VERIFY_OK`. The finite computations are **checks**, not a substitute for Steps 1–5, which prove the statements for every integer \(m\ge3\).

## Relationship to prior work

Saleh, Titz Mite, and Witzel calculate complete Vietoris–Rips filtrations for the five Platonic-solid vertex sets under several natural metrics [1]. Their Remark 4.5 also derives an equivariant kernel representation for the dodecahedron, but for neither this parallel-path graph nor the pole-exchange sign transition. The present family is different: its \(m\) hexagonal subcycles overlap along entire length-three paths, and the number of such hexagons is \(\binom m2\). Adamaszek's graph-power theorem [2, Proposition 2.2] proves stabilization at scale two under girth at least seven, but the present graphs have girth six. His separate result for **one-edge subdivisions** [2, Theorem 5.1] concerns an entirely different construction and does not contain the three-edge parallel-path family. The metric-gluing theorem of Adamaszek et al. [3, Theorem 10] requires each shared gluing path of length at most one third of the smallest containing loop; the shared three-edge paths here exceed one third of a six-cycle. Feng and Nukala [4] study symmetric-difference subset metrics, not this shortest-path family.

The previously described girth-six result under **edge-disjoint six-cycles** does not imply the present conclusion: every pair of hexagons here that shares an arm violates that hypothesis. Neither an absence of exact search hits nor different titles alone proves novelty; the comparisons above identify the actual differences in hypotheses and objects.

## Limitations

The theorem is restricted to internally disjoint length-three paths with common poles, to **finite vertex-set** graph distances, and to the inclusive convention. It does not describe unequal path lengths, graphs with added chords, metric-graph points on edges, other coefficient systems, or a universal classification of girth-six graphs. The claim of full symmetry applies only for \(m\ge3\). An unindexed or implicit equivalent theorem in the literature remains possible; no independent audit has been performed.

## References

[1] N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (initial public version 2023-02-28), https://arxiv.org/abs/2302.14388.

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, especially Proposition 2.2 and Theorem 5.1, https://arxiv.org/abs/1104.0433.

[3] M. Adamaszek et al., *Vietoris–Rips and Čech complexes of metric gluings*, SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3, Theorem 10 and Section 4.2, https://doi.org/10.4230/LIPIcs.SoCG.2018.3.

[4] Z. Feng, N. C. P. Nukala, *On Vietoris–Rips complexes of finite metric spaces with scale 2*, arXiv:2302.14664, https://arxiv.org/abs/2302.14664.
