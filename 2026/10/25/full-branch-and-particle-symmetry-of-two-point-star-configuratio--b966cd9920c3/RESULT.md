# Full branch-and-particle symmetry of two-point star configurations

## Finding
Let \(T_n\) be the metric star with \(n\ge3\) unit-length arms and let
\[
F_2(T_n)=\{(p,q)\in T_n\times T_n:p\ne q\}
\]
be its **ordered**, collision-free two-point configuration space. Arm permutations and exchange of the two points give a commuting action of \(S_n\times C_2\), where the nonidentity element of \(C_2\) is \(\tau\). The following assertions form one equivariant classification.

**Equivariant graph model and integral homology.** There is an explicit \(S_n\times C_2\)-equivariant strong deformation retraction of \(F_2(T_n)\) onto the crown graph \(\mathrm{Cr}_n=K_{n,n}\setminus M\). Its vertices are \(a_i,b_i\), \(1\le i\le n\), and its edges are \(a_ib_j\) for \(i\ne j\). Arm permutations relabel indices; \(\tau\) exchanges \(a_i\) with \(b_i\). In particular,
\[
H_1(F_2(T_n);\mathbb Z)\cong
\ker\!\left(\partial:\bigoplus_{i\ne j}\mathbb Z\,[a_i,b_j]
\longrightarrow \bigoplus_i(\mathbb Z\,a_i\oplus\mathbb Z\,b_i)\right),
\quad \partial[a_i,b_j]=b_j-a_i,
\]
canonically as an integral \(S_n\times C_2\)-lattice. It is free of rank \(n^2-3n+1\); all higher homology vanishes.

**Complete rational symmetry.** Let \(V_n=\{(z_1,\ldots,z_n)\in\mathbb Q^n:\sum z_i=0\}\) be the standard \(S_n\)-module. If \(n\ge4\), then
\[
H_1(F_2(T_n);\mathbb Q)\cong
\left(\bigwedge^2 V_n\right)\boxtimes\mathbf1_{C_2}
\ \oplus\ S^{(n-2,2)}\boxtimes\mathrm{sgn}_{C_2}.
\]
Thus each particle-exchange eigenspace is **irreducible as an \(S_n\)-representation**, of dimensions \(\binom{n-1}{2}\) and \(n(n-3)/2\), respectively. For \(n=3\), only the positive summand \(\bigwedge^2V_3\cong\mathrm{sgn}_{S_3}\) occurs.

Equivalently, if \(f(\sigma)\) is the number of fixed arms and \(t_2(\sigma)\) is the number of two-cycles of \(\sigma\in S_n\), the entire character for all \(n\ge3\) is
\[
\operatorname{tr}(\sigma\mid H_1)=f(\sigma)^2-3f(\sigma)+1,\qquad
\operatorname{tr}(\sigma\tau\mid H_1)=1-2t_2(\sigma).
\]
In particular, the rational first homology of the **unordered** two-point configuration space, with arm-permutation action, is \(\bigwedge^2V_n\).

## Assumptions and scope
Here \(T_n\) is a topological metric tree: the \(n\) copies of \([0,1]\) share precisely their zero endpoint, called the center. The two particles are ordered before the quotient by \(\tau\); collisions at the center or elsewhere are excluded. Equal arm lengths make the full arm-permutation action isometric. All claimed deformation retractions are in the ordinary topology of point configurations, not merely those configurations supported on graph vertices. The displayed irreducibility statements are over \(\mathbb Q\), not over an arbitrary finite field.

## Proof
**1. A simultaneous equivariant deformation retract.** Represent a point away from the center by its arm label and radius. When particles lie on distinct arms \(i\ne j\), their coordinates \((r,s)\) range over \([0,1]^2\setminus\{(0,0)\}\), with an arm label for each positive coordinate. Let \(m=\max\{r,s\}>0\). Define, for \(0\le u\le1\),
\[
H_u(r,s)=\left((1-u)+\frac{u}{m}\right)(r,s).
\]
The multiplier lies between one and \(1/m\). Hence this stays in the allowed square, fixes the locus \(m=1\), and at \(u=1\) reaches the union of the two outside edges \(r=1\) and \(s=1\).

When both points lie on the same arm, they have strictly unequal radii. If \(r>s\), put
\[
H_u(r,s)=\bigl((1-u)r+u,\ (1-u)s\bigr),
\]
and if \(s>r\), use its coordinate-exchanged formula. This preserves strict inequality, fixes the terminal configuration (outer tip, center), and reaches that terminal configuration when \(u=1\). At a shared boundary where exactly one coordinate is zero, the two formulas agree: the nonzero coordinate \(t\) becomes \((1-u)t+u\). Thus they glue continuously even though the center has no unique arm label; the excluded double-center point poses no continuity requirement. The homotopy is fixed on its final image, commutes with arbitrary relabeling of arms and with swapping the particle coordinates, and is therefore a strong equivariant deformation retraction.

For distinct arms, the retained L-shaped outside boundary runs from the configuration \(a_i\) (first particle at tip \(i\), second at the center) to \(b_j\) (first particle at center, second at tip \(j\)). There is one such interval exactly when \(i\ne j\). Same-arm configurations leave only the already present terminal vertices. The retained graph is therefore precisely \(\mathrm{Cr}_n\) with the claimed actions.

**2. Integral chain model.** Orient every crown edge from \(a_i\) to \(b_j\). The integral cellular complex is \(C_1\xrightarrow{\partial}C_0\), with boundary as stated. For \(n\ge3\), any pair of distinct \(a\)-vertices shares a neighboring \(b\)-vertex, and all \(b\)-vertices are adjacent to an \(a\)-vertex; hence the crown graph is connected. It has \(2n\) vertices and \(n(n-1)\) edges. Its first integral homology is precisely the kernel of the displayed boundary, of rank \(n(n-1)-2n+1=n^2-3n+1\), free as a subgroup of a free abelian group. No cells in dimensions two or higher occur. The chain identification respects the group: \(\sigma[a_i,b_j]=[a_{\sigma(i)},b_{\sigma(j)}]\), and \(\tau[a_i,b_j]=-[a_j,b_i]\).

**3. Character from the chain exact sequence.** Over \(\mathbb Q\), the connected graph gives an equivariant exact sequence
\[
0\longrightarrow H_1\longrightarrow C_1\longrightarrow C_0
\longrightarrow\mathbb Q\longrightarrow0.
\]
For \(\sigma\in S_n\), the trace on oriented edges is \(f(f-1)\), and on vertices it is \(2f\). For \(\sigma\tau\), there are no fixed vertices; an edge is fixed as an unoriented edge precisely when its endpoints' arm indices form a two-cycle of \(\sigma\), giving \(2t_2\) fixed edges, each with orientation reversed. Substituting in the exact-sequence Euler character identity gives the two displayed traces.

**4. Irreducible eigenspaces.** The \(\tau\)-positive and \(\tau\)-negative characters are the half-sum and half-difference of the two traces. Since \(f(\sigma^2)=f(\sigma)+2t_2(\sigma)\), the familiar exterior-square trace identity gives
\[
\chi_{+}(\sigma)=\frac{f^2-3f+2-2t_2}{2}
=\chi_{\wedge^2V_n}(\sigma).
\]
On the other hand,
\[
\chi_{-}(\sigma)=\frac{f^2-3f+2t_2}{2}
=\left(\binom f2+t_2\right)-f.
\]
The first parenthesis is the permutation character on the two-element subsets of \([n]\). For \(n\ge4\), this permutation module decomposes as \(\mathbf1\oplus V_n\oplus S^{(n-2,2)}\), whereas the point-permutation module is \(\mathbf1\oplus V_n\). Their character difference is the irreducible \(S^{(n-2,2)}\). Also \(\bigwedge^2V_n\cong S^{(n-2,1,1)}\) is irreducible for \(n\ge4\). For \(n=3\), the two-subset and point-permutation modules coincide, so the negative summand vanishes and the positive summand is the one-dimensional sign module. Semisimplicity over \(\mathbb Q\) and equality of characters establish the claimed decomposition. Finally, rational transfer for the free particle-swap action identifies the homology of the unordered quotient with the \(\tau\)-invariant summand.

## Verification
The supplied `check.py` constructs the crown graph, forms a spanning tree and its integral fundamental-cycle basis, and directly computes the induced signed homology action for **every** arm permutation and both particle-swap choices for each \(3\le n\le7\). It checks the traces against the two formulas on \(11{,}820\) group elements. The computed first Betti ranks for \(n=3,4,5,6,7\) are \(1,5,11,19,29\), respectively. This finite check is supplementary; all general assertions follow from the explicit deformation and exact-sequence argument above.

## Relationship to prior work
Wawrykow's *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph* (arXiv:2401.13821, first publicly posted 2024-01-24) establishes representation stability **as the number of particles changes** with the underlying star fixed. The inspected introduction, Theorems 1.1–1.3 and two-particle appendix give, for example, the particle-swap action for the three-arm case and the five-dimensional first homology for the four-arm case. Those assertions are consistent with, but do not state, the uniform \(S_n\times C_2\) **arm-and-particle** decomposition proved here.

Li and Özaydın's *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs* (arXiv:2603.00914, posted 2026-03-01) gives an explicit weighted bipartite model for ordered configurations under a positive separation constraint; its small-separation equal-arm specialization supplies essentially the underlying graph model. **The bare crown-graph reduction and its cycle rank are not claimed as new.** The inspected model and persistence sections do not calculate the joint arm-permutation and particle-exchange character or the two irreducible eigenspaces. A published mathematical finding on the neighborhood complex of the two-row rook graph also identifies the crown graph as an intersection and computes its ordinary cycle rank; that result concerns a different complex and does not specify the crown graph's equivariant cycle lattice. Other published calculations for metric stars concern **unordered separation persistence**, not this full representation. The contribution here is the complete natural symmetry module, including its integral chain realization, for every number of arms.

## Limitations
The claim concerns exactly two ordered particles and equal-length arms. It does not compute arbitrary numbers of particles, unequal-arm automorphism subgroups, or equivariant homotopy fixed-point spaces. The integral chain lattice is explicit, but no irreducible decomposition over positive-characteristic fields is asserted. Known combinatorial graph reductions make the representation calculation accessible once the equivariant action is recognized; there remains a genuine risk that equivalent character formulas exist in literature indexed under crown-graph cycle spaces or graph-braid symmetries. The literature searches are evidence, not a proof of global priority.

## References
1. N. Wawrykow, *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph*, arXiv:2401.13821v1 (first submitted 2024-01-24), https://arxiv.org/abs/2401.13821.
2. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1 (first submitted 2026-03-01), https://arxiv.org/html/2603.00914v1.
3. *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, published research record, 2026-10-11, identifier `SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620`.
4. *Exact persistence of two unordered separated particles on metric stars*, published research record, 2026-10-11, identifier `SCOPE-exact-persistence-of-two-unordered-separated-particles-on-metric--ce01bbf73bfa`.
