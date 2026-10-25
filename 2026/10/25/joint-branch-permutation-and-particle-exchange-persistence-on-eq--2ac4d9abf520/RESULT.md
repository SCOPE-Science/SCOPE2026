# Joint branch-permutation and particle-exchange persistence on equilateral metric stars

## Finding
Let \(m\ge3\), and consider two *ordered* particles on an equal-arm metric star \(T_m\) with each arm of length \(1\). For clearance \(a>0\), put
\[
F_a=\{(x,y)\in T_m\times T_m:d(x,y)\ge a\}.
\]
The group \(\Gamma=S_m\times C_2\) permutes the arms and interchanges the particle labels. There is a \(\Gamma\)-equivariant strong deformation retraction, for every \(0<a\le1\), onto the crown graph with vertices \(A_i=(\mathrm{tip}_i,o)\), \(B_i=(o,\mathrm{tip}_i)\) and edges \(e_{ij}\) for \(i\ne j\), where \(o\) denotes the star center. Orient \(e_{ij}\) from \(A_i\) to \(B_j\). Consequently the **full integral first-homology lattice and its action** are
\[
H_1(F_a;\mathbb Z)=\ker\!\left(\partial:\mathbb Z\langle e_{ij}:i\ne j\rangle\longrightarrow\mathbb Z\langle A_i,B_i\rangle\right),
\qquad \partial e_{ij}=B_j-A_i,
\]
\[
\sigma e_{ij}=e_{\sigma(i),\sigma(j)},\qquad \tau e_{ij}=-e_{ji}.
\]
This lattice is free of rank \(m^2-3m+1\), and it is the entire positive-degree homology. If \(f(\sigma)\) denotes the number of fixed arms and \(t_2(\sigma)\) the number of two-cycles of \(\sigma\), its rational character is
\[
\chi(\sigma,1)=1-2t_2(\sigma),\qquad \chi(\sigma,0)=f(\sigma)^2-3f(\sigma)+1,
\]
where the second group argument is \(1\) for particle exchange and \(0\) for no exchange. For \(m\ge4\), the rational representation decomposes as
\[
H_1(F_a;\mathbb Q)\cong S^{(m-2,1,1)}\boxtimes\mathbf1\ \oplus\ S^{(m-2,2)}\boxtimes\varepsilon,
\]
with \(\varepsilon(\tau)=-1\). For \(m=3\), only \(\operatorname{sgn}_{S_3}\boxtimes\mathbf1\) occurs.

For \(1<a\le2\), the configuration space \(F_a\) \(\Gamma\)-equivariantly strongly retracts onto the discrete set of ordered *distinct-arm tip pairs*. It has \(m(m-1)\) connected components, so \(H_0\) is the corresponding integral permutation lattice, while \(H_j=0\) for \(j>0\). For \(a>2\), \(F_a\) is empty. All restriction maps within each of the two nonempty clearance regimes induce equivariant isomorphisms. Crossing from \(a>1\) to \(a\le1\), the degree-zero map is the augmentation \(\mathbb Z[\{(i,j):i\ne j\}]\to\mathbb Z\); there are no higher-degree cross-regime classes. These formulas determine the integral equivariant clearance-persistence system.

## Assumptions and scope
The star has exactly \(m\ge3\) edges, each isometrically a closed unit interval sharing a common origin and otherwise disjoint. Distance is the shortest-path metric. The particle positions are ordered (labeled). Clearance satisfies \(a>0\), so collisions are excluded. Arm permutations and label exchange commute; the representation assertions refer to the whole \(S_m\times C_2\) action. The graph edge \(e_{ij}\) consists of the two straight segments \((\mathrm{tip}_i,\mathrm{point\ on\ arm}_j)\) and \((\mathrm{point\ on\ arm}_i,\mathrm{tip}_j)\), joined at the ordered tip pair \((\mathrm{tip}_i,\mathrm{tip}_j)\). There is no edge with \(i=j\). All claimed integral groups and persistence maps use unreduced homology. The rational splitting does not assert an integral decomposition by the two particle-exchange eigenspaces.

## Proof
**1. Equivariant retraction for \(0<a\le1\).** Write the two particle radii as \(u,v\in[0,1]\), with branch labels only where the radii are nonzero. Put \(M=\max(u,v)\); since \(a>0\), \(M>0\). Multiply both radii at homotopy time \(t\) by \(c_t=((1-t)+tM)^{-1}\). The multiplier never exceeds \(1/M\), so both radii remain within the star. The path distance between the particles is multiplied by the same \(c_t\ge1\), whether the particles lie on one arm or on two, so the clearance inequality persists. The procedure is continuous, equivariant and fixed wherever \(M=1\). It retracts \(F_a\) to the locus \(M=1\).

Within the latter locus, if the particles occupy the same arm, their outer radius equals \(1\) and the inner radius \(v\) (or \(u\)) satisfies \(v\le1-a<1\); continuously shrink that inner radius to zero. For particles on different arms, leave their radii unchanged. This operation is continuous even as the inner particle reaches the center, increases the mutual separation, commutes with arm permutations and particle interchange, and fixes its eventual target pointwise. On different arms, \(M=1\) is exactly the union of two sides of the unit square, a path from \(A_i\) to \(B_j\) via the pair of tips. On the same arm only the vertex \(A_i\) or \(B_i\) survives. This proves the claimed strong equivariant deformation retraction. Since the target is the connected crown graph \(K_{m,m}\) minus the perfect matching, it has \(2m\) vertices and \(m(m-1)\) edges, hence cycle rank \(m(m-1)-2m+1=m^2-3m+1\). The retractions for different clearances in this range fix the same crown pointwise, so all inclusion-induced homology maps here are the canonical isomorphisms on this lattice.

**2. High-clearance topology and persistence.** If \(1<a\le2\), the particles cannot lie on the same arm or at the center: the maximal within-arm distance is \(1\). Therefore they occupy two distinct arms with positive radii \(u,v\) satisfying \(u+v\ge a\). On each such component, linearly increase both radii to \(1\). This preserves clearance, fixes the ordered pair of tips, and commutes with all symmetries. There is one component for each ordered pair of distinct arms, giving exactly the claimed permutation lattice in degree zero. For \(a>2\), the diameter bound makes the space empty. Inclusions at and below clearance \(1\) connect every tip pair via the crown; thus the crossing degree-zero map is the ordinary augmentation. Higher-degree maps from the discrete regime are zero. This proves the entire equivariant persistence description.

**3. Integral action and full character.** The cellular edge action is \(\sigma e_{ij}=e_{\sigma(i),\sigma(j)}\), whereas particle exchange interchanges the endpoints of \(e_{ij}\) and therefore acts by \(\tau e_{ij}=-e_{ji}\). The boundary formula follows from the prescribed orientation. Connectedness gives the short exact integral cellular sequence
\[
0\to H_1(F_a;\mathbb Z)\to C_1\xrightarrow{\partial} C_0\to\mathbb Z\to0.
\]
For a branch permutation \(\sigma\), the trace on \(C_0\) is \(2f(\sigma)\), and the trace on \(C_1\) is \(f(\sigma)(f(\sigma)-1)\). For \(\sigma\tau\), no vertex is fixed, while each two-cycle of \(\sigma\) contributes exactly two orientation-reversed fixed edges, giving trace \(-2t_2(\sigma)\) on \(C_1\). Additivity of traces in the exact sequence now yields the stated character formulas.

**4. Irreducible decomposition.** Over \(\mathbb Q\), take the \(+1\) particle-exchange eigenspace. It is generated on edges by \(e_{ij}-e_{ji}\), with boundary equal to the difference of the vertex sums \((A_j+B_j)-(A_i+B_i)\). Its kernel is the standard cycle lattice of the complete graph \(K_m\), hence as a rational \(S_m\)-module is \(\bigwedge^2 U_m\cong S^{(m-2,1,1)}\), where \(U_m\) is the augmentation representation of \(S_m\). In the \(-1\) eigenspace, the edge generators are \(e_{ij}+e_{ji}\), and the boundary is \((B_i-A_i)+(B_j-A_j)\). Thus the odd eigenspace is the kernel of the \(S_m\)-equivariant map from the permutation module on unordered arm pairs to \(\mathbb Q^m\), sending \(\{i,j\}\mapsto v_i+v_j\). This map is surjective for \(m\ge3\), because three distinct indices give \(2v_i=(v_i+v_j)+(v_i+v_k)-(v_j+v_k)\). The standard pair-permutation decomposition \(\mathbb Q\binom{[m]}2\cong\mathbf1\oplus U_m\oplus S^{(m-2,2)}\) for \(m\ge4\) identifies its kernel with \(S^{(m-2,2)}\). For \(m=3\) this kernel is zero and the even cycle module is \(\operatorname{sgn}_{S_3}\). The two dimensions add up to \(m^2-3m+1\), as required.

## Verification
The accompanying standalone script `starpair_equivariant_verify.py` constructs the integral cellular chain data of the crown graph, an independent spanning-tree basis for its first homology, and the induced signed action of every branch permutation and both particle-exchange choices for each \(m\in\{3,4,5,6,7\}\). It tests all 11,820 group actions, checking the homological trace directly in the cycle basis against the character formula and the cellular trace identity. It also checks connectedness, the exact rank, and the dimensions of both rational particle-exchange eigenspaces. This is finite verification only; the homotopy constructions and representation arguments above prove the universal statements.

## Relationship to prior work
Wawrykow, *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph* (first posted 2024-01-24), develops ordered star configuration-space homology and stability with respect to increasing particle number. Li–Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs* (first posted 2026-03-01), develops an explicit nonequivariant weighted-graph model and associated homological persistence for general positive arm lengths. Their foundational results motivate this complete joint arm-permutation/particle-exchange integral representation and its symmetry-sensitive clearance maps. Nonequivariant Betti numbers do not identify the two Specht modules or their opposite exchange parities. The proposed explicit equivariant retraction retains both symmetries pointwise and the proof computes the resulting integral lattice. The character and rational splitting could conceivably be implicit consequences of prior general graph models; no claim is made to a new nonequivariant homotopy rank.

## Limitations
The arms have equal lengths; arbitrary unequal-arm geometries generally break full arm-permutation symmetry. Exactly two ordered particles are considered, with strictly positive clearance. The rational irreducible decomposition does not by itself decompose the integral lattice, though its explicit boundary-kernel description determines that lattice completely. This is a mathematical proof with computational corroboration, not a claim of independent external validation. Exhaustive searches cannot exclude an unindexed equivalent equivariant formulation.

## References
- Nicholas Wawrykow, *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph*, arXiv:2401.13821v1 (first posted 2024-01-24). https://arxiv.org/abs/2401.13821
- Wenwen Li and Murad Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1 (first posted 2026-03-01). https://arxiv.org/abs/2603.00914
- Wenwen Li, *Persistent Homology of Configuration Spaces of Trees*, arXiv:2310.05303v1 (first posted 2023-10-08). https://arxiv.org/abs/2310.05303
