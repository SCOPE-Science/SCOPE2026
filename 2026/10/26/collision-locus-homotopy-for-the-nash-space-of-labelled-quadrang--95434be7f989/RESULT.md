# Collision-locus homotopy for the Nash space of labelled quadrangles

## Finding

Let \(\mathcal Q\) be the real Nash manifold of *labelled quadrangles*: ordered vertices \(v_1,v_2,v_3,v_4\in\mathbb R^2\) and six incident pair-lines \(L_{ij}\), with at least three of those lines forming a nondegenerate triangle, as in Olberding–Walker [1, Definition 2.1]. Let \(G=\operatorname{Sim}^{+}(\mathbb R^2)\) be the group of orientation-preserving similarities. Define the **vertex-collision locus**
\[
B=\{[Q]\in\mathcal Q/G: v_i=v_j\text{ for some }i\ne j\}.
\]
Then \(B\) has exactly three connected components, distinguished by the partitions \(12\mid34\), \(13\mid24\), and \(14\mid23\), and each component is homotopy equivalent to a wedge of seven circles:
\[
B\simeq\coprod_{j=1}^{3}\bigvee^{7}S^1.
\]
Consequently its integral homology is \(H_0(B;\mathbb Z)\cong\mathbb Z^3\), \(H_1(B;\mathbb Z)\cong\mathbb Z^{21}\), and \(H_i(B;\mathbb Z)=0\) for every \(i\ge2\). The fundamental group of each component is free of rank seven.

## Assumptions and scope

The vertices are labelled and the lines are part of the quadrangle data; coincident vertices are allowed subject to the nondegenerate-triangle condition. The acting group is **orientation preserving** and includes translations, positive scalings, and rotations. This is the ordinary topological homotopy type of the real semialgebraic collision locus, not of the entire moduli manifold, a complexification, an unordered quotient, or a Fulton–MacPherson boundary. All six lines belong to the affine real plane. Distinct collision pairs that share a label would produce three coincident vertices, which a quadrangle excludes.

## Proof

**1. Three disjoint pieces.** Every collision has either precisely one coincident pair or precisely two disjoint coincident pairs: three coincident vertices are excluded by the triangle condition [1, Proposition 2.2]. For a pair \(ij\), let \(E_{ij}\subseteq B\) denote the locus \(v_i=v_j\). For each pairing \(\{ij,kl\}\) of the four labels, set \(B_{ij\mid kl}=E_{ij}\cup E_{kl}\). These three pairwise disjoint subsets exhaust \(B\). Each \(E_{ij}\) is closed in \(B\), because coincidence of labelled vertices is closed and invariant under \(G\); hence each \(B_{ij\mid kl}\) is both closed and open in \(B\). It remains to determine the homotopy type of one such piece, say \(B_{12\mid34}\).

**2. A global chart for a single-pair collision locus.** In \(E_{12}\), write \(v_1=v_2=p\), \(v_3=q\). These points are distinct; normalize uniquely by an orientation-preserving similarity to \(p=0\), \(q=1\) in the complex plane. Let \(\alpha\in\mathbb R/\pi\mathbb Z\) be the unoriented direction of the free side \(L_{12}\). The side \(L_{34}\) cannot be horizontal: if \(v_4\ne v_3\) were collinear with \(0,1\), only the horizontal line and \(L_{12}\) could occur, and if \(v_4=v_3\), the triangle condition excludes a horizontal \(L_{34}\). Thus the direction of \(L_{34}\) has a unique representative \(\beta\in(0,\pi)\). There is a unique real \(r\) such that
\[
v_4=1+r e^{i\beta}.
\]
For \(r\ne0\), the vertices \(0,1,v_4\) are noncollinear, so every \(\alpha\) is allowed. For \(r=0\), there are two double vertices and the only possible triangle is formed by the horizontal joining line, \(L_{12}\), and \(L_{34}\). Thus exactly \(\alpha\ne0\) and \(\alpha\ne\beta\) are required (angles here are modulo \(\pi\)). The continuous inverse recovers the normalized points and every pair-line. Therefore
\[
E_{12}\cong\bigl\{(r,\beta,\alpha)\in\mathbb R\times(0,\pi)\times(\mathbb R/\pi\mathbb Z):
 r\ne0\ \text{or}\ (\alpha\ne0\ \text{and}\ \alpha\ne\beta)\bigr\}.
\]
The homeomorphism is a global quotient chart, since the normalization of the ordered distinct vertices \(p,q\) is unique and depends continuously on the quadrangle.

**3. Punctured-cylinder topology.** For each \(\beta\in(0,\pi)\), define a circle homeomorphism \(h_\beta:\mathbb R/\pi\mathbb Z\to\mathbb R/\pi\mathbb Z\) fixing \(0\) and taking \(\beta\) to \(\pi/2\). One explicit choice is the increasing piecewise-linear map on \([0,\pi]\):
\[
h_\beta(a)=\begin{cases}\dfrac{\pi a}{2\beta},&0\le a\le\beta,\\[2mm]
\dfrac\pi2+\dfrac{\pi(a-\beta)}{2(\pi-\beta)},&\beta\le a\le\pi.
\end{cases}
\]
It varies continuously with \(\beta\), including its inverse. The change of variables \(w=\exp(r+2i h_\beta(\alpha))\) gives an explicit homeomorphism
\[
E_{12}\cong(0,\pi)\times\bigl(\mathbb C\setminus\{0,1,-1\}\bigr).
\]
Indeed, the two excluded possibilities at \(r=0\) map to \(w=1\) and \(w=-1\), while \(w=0\) is omitted by the exponential. A plane punctured three times has the homotopy type \(\bigvee^3 S^1\), hence so does \(E_{12}\). Relabelling gives \(E_{34}\simeq\bigvee^3 S^1\).

**4. Double-pair intersection.** The intersection \(I=E_{12}\cap E_{34}\) consists of double collisions \(v_1=v_2=0\), \(v_3=v_4=1\). The only free parameters are the two nonhorizontal and nonparallel directions of \(L_{12}\) and \(L_{34}\); equivalently
\[
I\cong\{(\alpha,\beta)\in(0,\pi)^2:\alpha\ne\beta\}.
\]
It has precisely two contractible connected components, the open triangles \(\alpha<\beta\) and \(\beta<\alpha\). Within the chart of Step 2, \(I\) is the closed embedded locus \(r=0\). Thus its inclusion into \(E_{12}\) is a cofibration, by a local tubular collar (also obtainable by semialgebraic triangulation). The same applies to \(I\hookrightarrow E_{34}\).

**5. Gluing.** The union \(B_{12\mid34}=E_{12}\cup_I E_{34}\) is therefore a homotopy pushout. Both pieces are connected three-circle wedges up to homotopy. Each of the two components of \(I\) is contractible, so its attaching maps are nullhomotopic in each piece. The homotopy pushout is a union of two three-circle wedges joined by two distinct edges: choosing one edge to connect the two wedges leaves the other as an additional independent circle. Therefore
\[
B_{12\mid34}\simeq\bigvee^{3+3+1}S^1=\bigvee^7 S^1.
\]
The same argument, after relabelling the vertices, treats the other two pairings. Each \(B_{ij\mid kl}\) is connected, and the three are clopen in \(B\); they are exactly the connected components. The homology and fundamental-group assertions follow.

## Verification

The proof is self-contained once the published incidence definition is fixed. It uses an explicit global quotient normalization, an explicit homeomorphism to a thrice-punctured plane, a direct identification of the two double-collision chambers, and the homotopy-pushout property of collared closed embeddings. No sampling or finite enumeration is used in place of an infinite topological argument. The elementary consistency checks are \(\chi(E_{12})=1-3=-2\), \(\chi(I)=2\), and \(\chi(B_{12\mid34})=(-2)+(-2)-2=-6=1-7\), agreeing with the wedge description. No numerical program is needed.

## Relationship to prior work

Olberding–Walker [1] establish the Nash-manifold structure, proper similarity quotient, and geometry of degenerate quadrangles; their Proposition 2.2 supplies the key exclusion of triple vertices. The present result instead computes the homotopy type of the entire vertex-collision locus in the oriented-similarity quotient. Martin's graph picture spaces [2] accommodate the same incidence data in a different algebraic setting but do not supply this real oriented-similarity quotient calculation in the material examined. Fulton–MacPherson configuration-space compactification [3] retains more degeneration data and is not the moduli object computed here.

## Limitations

The conclusion concerns the *collision locus*, not the full Nash moduli space. It does not identify the inclusion-induced maps from the collision locus to the ambient moduli space, nor does it compute the homotopy type for unoriented similarities or unordered vertices. The classification is mathematically proved here but has not undergone independent external auditing. An unpublished manuscript on related quadrangle geometry mentioned in [1] could contain an overlapping result; its contents were not available for full comparison.

## References

[1] B. Olberding and E. A. Walker, *The Nash manifold of four-point configurations modulo similarity subgroups*, arXiv:2610.02087v1 (first posted 2026-10-01), Definition 2.1, Proposition 2.2, Theorem 3.6, and Section 6. https://arxiv.org/html/2610.02087v1

[2] J. L. Martin, *Geometry of graph varieties*, arXiv:math/0302089 (2003), especially the definition of picture spaces and discussion of the complete graph. https://arxiv.org/pdf/math/0302089

[3] W. Fulton and R. MacPherson, *A compactification of configuration spaces*, Ann. of Math. 139 (1994), 183–225. (Background reference cited in [1]; not independently inspected in full.)
