# Translation-subgroup geometric fixed spaces of scale-two hypercube Rips complexes

## Finding

Let \(V_n=\mathbb F_2^n\) with Hamming metric \(d(x,y)=\operatorname{wt}(x+y)\), and let \(X_n=\operatorname{VR}_{\le2}(V_n)\). The translation group \(T_n=V_n\) acts on the simplicial complex by \(h\cdot x=x+h\). For every integer \(n\ge3\) and every **nonzero** linear subspace \(H\le V_n\), the *geometric*, not homology-invariant, fixed point space satisfies

\[
|X_n|^H\cong_{\mathrm{PL}}
\begin{cases}
\varnothing,&\exists h\in H:\ \operatorname{wt}(h)\ge3,\\
|Q_{n-1}|,&\max_{h\in H}\operatorname{wt}(h)\le2\ \text{and }\dim H=1,\\
\{1,\ldots,2^{n-2}\}\text{ discrete},&\max_{h\in H}\operatorname{wt}(h)\le2\ \text{and }\dim H=2.
\end{cases}
\]

There is no nonzero subgroup of dimension greater than two satisfying the weight bound. Every admissible rank-two subgroup is, after relabeling coordinates, either \(\langle e_1,e_2\rangle\) or \(\langle e_1+e_2,e_1+e_3\rangle\). The fixed graph in the rank-one case is connected, has \(2^{n-1}\) vertices and \((n-1)2^{n-2}\) edges, and therefore

\[
|X_n|^H\simeq\bigvee^{1+(n-3)2^{n-2}} S^1\qquad(\dim H=1,\ \max\operatorname{wt}H\le2).
\]

In the admissible rank-two case its only nonzero reduced integral homology is \(\widetilde H_0\cong\mathbb Z^{2^{n-2}-1}\). In the rank-one case its only nonzero reduced integral homology is \(\widetilde H_1\cong\mathbb Z^{1+(n-3)2^{n-2}}\). The empty case uses the standard convention that empty fixed spaces have no points; no assertion about reduced degree minus one is needed.

## Assumptions and scope

The scale is **inclusive**: a finite subset \(S\subset V_n\) is a face exactly when all pairwise Hamming distances are at most two. A fixed point means a point of the geometric realization whose entire barycentric coordinate vector is fixed by each translation in \(H\). It does *not* mean a vertex fixed by a translation (there are no such vertices for nonzero translations), and it is not the invariant subspace of rational homology. All homotopy and PL homeomorphism assertions are for the geometric fixed spaces of nontrivial *translation* subgroups, not arbitrary elements of the larger cubical isometry group. For \(H=0\), the previously established nonequivariant homotopy classification applies [1]; that case is not a new claim.

## Proof

**Orbit-simplex lemma.** For a finite simplicial complex whose vertices are permuted by a finite group, a fixed barycentric vector is constant on each vertex orbit. Consequently, its support is a disjoint union of full vertex orbits, and the fixed set is canonically PL homeomorphic to the orbit-vertex complex: vertices are group orbits whose union is a face, and any collection of orbit vertices spans a face precisely when the union of its full orbits is a face. The map sends each orbit vertex to the barycenter of that vertex orbit. The Hamming translations act freely on \(V_n\), so the orbit vertices here are exactly the cosets \(x+H\).

**The diameter obstruction and subgroup classification.** Every coset \(x+H\) contains \(x\) and \(x+h\) for all \(h\in H\). If some \(h\) has weight at least three, no coset spans a face, so the fixed space is empty. Suppose henceforth every element has weight at most two. If \(H\) contains a weight-one vector, relabel so it contains \(e_1\). Any independent weight-at-most-two vector \(v\), for which \(v+e_1\) must also have weight at most two, yields a second coordinate vector \(e_j\in H\). The span of \(e_1,e_j\) consists of all bit patterns in those two coordinates. Any independent third vector has at least one nonzero coordinate outside this pair, and adding an appropriate member of the two-plane makes the result have weight at least three. Hence \(H\) is a coordinate two-plane or has rank one. If \(H\) contains no weight-one vector, all its nonzero elements have weight two. Two independent such vectors must have supports meeting in exactly one coordinate (their sum also has weight two); they generate the three even-weight vectors on a triple of coordinates. Any third vector outside this plane has a translate by one of these four plane vectors of weight at least three: if its restriction to the triple is odd, choose the translate whose three triple bits are all one; if even and not in the plane, an outside bit is nonzero and some translate has two triple bits equal to one. Thus \(H\) has rank at most two and is one of the two asserted rank-two types.

**Weight-one rank-one groups.** After a coordinate permutation take \(H=\langle e_1\rangle\). Cosets are labeled by \(z\in\mathbb F_2^{n-1}\), and two distinct cosets labeled by \(z,z'\) can coexist in a face precisely when
\[
\max_{u\in z+H,\,v\in z'+H}d(u,v)=1+\operatorname{wt}(z+z')\le2.
\]
Thus the orbit-vertex complex is the clique complex of the cube graph \(Q_{n-1}\), whose lack of triangles shows that this clique complex is exactly the graph.

**Weight-two rank-one groups.** Relabel to \(H=\langle e_1+e_2\rangle\). Label each coset by \((a,z)\in\mathbb F_2\times\mathbb F_2^{n-2}\), where \(a=x_1+x_2\) and \(z=(x_3,\ldots,x_n)\). For distinct cosets, the maximal cross distance is \(2+\operatorname{wt}(z+z')\) if \(a=a'\), and \(1+\operatorname{wt}(z+z')\) if \(a\ne a'\). Hence cosets are adjacent exactly when \(a\ne a'\) and \(\operatorname{wt}(z+z')\le1\). The invertible linear relabeling
\[
(a,z)\longmapsto\bigl(a+z_1+\cdots+z_{n-2},z\bigr)
\]
turns this adjacency into Hamming distance exactly one in \(\mathbb F_2^{n-1}\). Again the clique complex is precisely \(Q_{n-1}\).

**Rank-two groups.** For the coordinate plane \(H=\langle e_1,e_2\rangle\), two distinct cosets have different outside-coordinate labels, and their maximal cross distance is at least three. For the even-weight plane on three coordinates, two distinct cosets have either distinct outside-coordinate labels (so an even-weight difference of weight two on the triple gives distance at least three) or opposite parity on the triple (so the difference can have weight three on the triple). Thus no two cosets are compatible. There are \(|V_n/H|=2^{n-2}\) cosets, each a legal face by the weight bound, so the fixed set is precisely that many isolated points.

The final homology ranks follow from graph Euler characteristic \(|E(Q_{n-1})|-|V(Q_{n-1})|+1\) and the reduced degree-zero homology of a finite nonempty discrete space. These arguments handle all \(n\ge3\) without extrapolating from finite tests. \(\square\)

## Verification

The self-contained checker `verify_translation_fixed_scale2.py` independently enumerates admissible nontrivial translation subgroups and complete orbit compatibility relations for every \(2\le n\le6\). It verifies that each rank-one orbit graph is the \((n-1)\)-cube by an explicit coset-coordinate relabeling, that rank-two fixed sets have no orbit edges, and that weight-at-least-three translation orbits cannot be faces. The actual test completed with marker `TRANSLATION_FIXED_RIPS2_VERIFIED 125 nontrivial_subgroups`. This is a finite corroboration of the preceding proof, not a finite-to-infinite inference.

## Relationship to prior work

Adamaszek and Adams [1] classified the **ordinary** homotopy type of the inclusive scale-two hypercube Rips complex as a wedge of three-spheres; their theorem does not classify any of its geometric subgroup-fixed spaces. Galetto, Montaño, and Wellner [2] subsequently determined the rational homology representations of the full cubical isometry group, including the translation action. Knowing traces on ordinary homology can recover certain fixed-point **Euler characteristics** via the Lefschetz formula, but it does not identify fixed-point homotopy types, nor the simultaneous fixed sets of every rank-two subgroup. In particular, these new fixed spaces can contain one-dimensional cycles even though the underlying complex has reduced homology concentrated in dimension three.

The general framework of metric thickenings with group actions [3] studies quotients and metric thickenings; its accessible abstract does not establish this exact Hamming-subgroup classification. Its full text was not accessible during this comparison, so potential stronger implications of that source remain an acknowledged limitation.

## Limitations

This theorem is limited to inclusive radius two, binary Hamming cubes, and nontrivial translation subgroups. It makes no classification of all nontranslation isometry-subgroup fixed sets, no claim of a new ordinary homotopy type, and no claim that an equivariant homotopy equivalence between the ambient complex and a wedge of spheres has been constructed. Literature searches cannot rule out differently indexed or unpublished equivalent results. The independent mathematical audit has not been performed.

## References

[1] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first public version 2021-03-01, Theorem 1 and Sections 2–4. https://arxiv.org/pdf/2103.01040

[2] F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public version 2026-06-18, Section 5 and Theorem 5.4. https://arxiv.org/abs/2606.20784

[3] H. Adams, M. Heim, and C. Peterson, *Metric thickenings and group actions*, arXiv:1911.00732, 2019-11-02; only the abstract was available for inspection. https://arxiv.org/abs/1911.00732
