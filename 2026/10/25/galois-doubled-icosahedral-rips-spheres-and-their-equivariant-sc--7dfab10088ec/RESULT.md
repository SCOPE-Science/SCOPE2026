# Galois-doubled icosahedral Rips spheres and their equivariant scale map

## Finding

Let \(I\) be the edge graph of a regular icosahedron, let \(K_r=\operatorname{VR}_{\le r}(V(I))\) use shortest-path distance, and let \(G=\operatorname{Aut}(I)\cong A_5\times C_2\) act by vertex permutations. There is a natural orthogonal six-dimensional \(G\)-representation \(E\) and a canonical invariant decomposition \(E=U\oplus W\), where \(U\) is the ordinary three-dimensional geometric representation and, on the rotational \(A_5\), \(W\) is the other irreducible real three-dimensional representation. Central inversion acts as minus the identity on both summands.

**Theorem (equivariant scale map).** There are \(G\)-homeomorphisms \(|K_1|\cong S(U)\) and \(|K_2|\cong S(U\oplus W)\) under which the actual filtration inclusion \(|K_1|\hookrightarrow |K_2|\) is \(G\)-homotopic to the equatorial linear inclusion

\[
S(U)\longrightarrow S(U\oplus W),\qquad u\longmapsto(u,0).
\]

The characters of \(U\) and \(W\) are Galois conjugate over \(\mathbb Q(\sqrt5)\). Consequently, for **every** subgroup \(H\le G\), if \(d_H=\dim_{\mathbb R}U^H\), then \(\dim_{\mathbb R}W^H=d_H\). The induced fixed-point filtration from graph-distance threshold one to two is therefore, up to homeomorphism and homotopy of its map,

\[
\begin{cases}
\varnothing\longrightarrow\varnothing,&d_H=0,\\
S^{d_H-1}\longrightarrow S^{2d_H-1},&d_H>0,
\end{cases}
\]

where the second map is a standard equatorial inclusion. Thus all reduced integral homology maps between these two fixed-point stages are zero; no fixed-point homology class persists across the change from radius one to radius two. For \(r\ge3\), every \(|K_r|^H\) is contractible. The theorem includes the trivial subgroup and all noncyclic subgroups; it does **not** assert that the equivariant inclusion is itself equivariantly nullhomotopic.

In addition, the full group acts by the central-inversion sign on \(\widetilde H_2(K_1;\mathbb Z)\cong\mathbb Z\), but trivially on \(\widetilde H_5(K_2;\mathbb Z)\cong\mathbb Z\). Consequently, the quotients \(|K_1|/G\) and \(|K_2|/G\) have, respectively, zero and one-dimensional positive-degree reduced rational homology (the latter in degree five).

## Assumptions and scope

The metric is the **graph shortest-path metric**, with inclusive thresholds \(r=1,2,3\), rather than Euclidean intervertex distance. Normalize the twelve vertices to unit vectors. Explicit representatives are the sign choices of

\[
(0,1,\varphi),\quad(1,\varphi,0),\quad(\varphi,0,1),\qquad
\varphi=\frac{1+\sqrt5}{2},
\]

after division by \(\sqrt{1+\varphi^2}\). Choose exactly one unit vector \(v_i\) from each of the six antipodal pairs \(\{v_i,-v_i\}\), for \(1\le i\le6\). Define \(E=\mathbb R^6\), identifying graph vertices \(\pm v_i\) with signed coordinate vectors \(\pm e_i\). Then \(G\) acts on \(E\) by orthogonal signed-permutation matrices. Set

\[
A:E\to\mathbb R^3,\quad A(e_i)=v_i,\qquad
U=\operatorname{im}(A^*),\quad W=\ker A.
\]

The decomposition and theorem are independent, up to canonical signed coordinate identifications, of the choice of representatives. Sphere notation \(S(V)\) denotes the unit sphere of a real inner-product representation \(V\). Geometric fixed points always mean fixed points in the full geometric realization, not merely vertices fixed pointwise. The source homotopy types of the two individual stages were previously determined; the equivariant scale map, conjugate representation splitting, and simultaneous all-subgroup fixed-persistence result are the claims assessed here.

## Proof

**1. The two simplicial stages.** The icosahedral graph is a maximal planar triangulation with twenty triangular faces, no four-cliques, graph diameter three, and a unique vertex at distance three from each vertex: its antipode. Therefore \(K_1\) is exactly the boundary triangulation of the regular icosahedron, while \(K_2\) consists of all subsets that avoid antipodal pairs. It is exactly the boundary of the six-dimensional cross-polytope with vertices \(\pm e_i\). Both identifications are \(G\)-equivariant because they respect the labeled vertex actions. Radial projection from either convex boundary gives \(G\)-homeomorphisms to the corresponding unit sphere. At radius three the complex is the entire simplex, whose contraction to the uniform barycenter is equivariant for every subgroup.

**2. The invariant splitting and characters.** Directly from the normalized vertex coordinates,

\[
AA^*=\sum_{i=1}^{6}v_i v_i^{\mathsf T}=2I_3.
\]

Consequently, \(U=\operatorname{im}(A^*)\) is isomorphic as an orthogonal \(G\)-module to the geometric \(\mathbb R^3\), and \(E=U\oplus W\) is an orthogonal invariant splitting. The six-axis signed-permutation representation has character on the rotational classes of \(A_5\)

\[
\begin{array}{c|ccccc}
\text{order/class}&1&2&3&5_a&5_b\\\hline
\chi_E&6&-2&0&1&1\\
\chi_U&3&-1&0&\varphi&1-\varphi\\
\chi_W&3&-1&0&1-\varphi&\varphi
\end{array}
\]

(the two order-five columns can be exchanged by relabeling their conjugacy classes). For order two, two antipodal axes are individually reversed and the others are exchanged; order three permutes axes in two cycles; order five fixes one oriented axis and cycles the others. The \(\chi_U\) row is \(1+2\cos\theta\) for each spatial rotation. Subtracting gives \(\chi_W\), the other real degree-three irreducible character of \(A_5\), Galois conjugate under \(\sqrt5\mapsto-\sqrt5\). The central inversion acts as \(-I_3\) on \(U\) and \(W\), so the Galois-conjugacy assertion holds on all of \(G\), including improper symmetries.

**3. Straightening the actual filtration map.** Embed \(|K_2|\) as the boundary of the six-dimensional cross-polytope in \(E\) and regard \(|K_1|\) as its icosahedral two-dimensional subcomplex. A point \(x\in |K_1|\) is a convex combination of the signed coordinate vectors corresponding to the vertices of one triangular face. Its image \(Ax\) is the corresponding convex combination of the three physical vertices. All three vertices lie in a common supporting plane of the icosahedron, strictly separated from the origin. Therefore \(Ax\ne0\) for every \(x\in|K_1|\). Orthogonal projection to \(U\) is

\[
P_U=\tfrac12A^*A,
\]

so \(P_Ux\ne0\). The formula

\[
H_t(x)=\frac{(1-t)x+tP_Ux}{\lVert(1-t)x+tP_Ux\rVert},\qquad0\le t\le1,
\]

is everywhere defined: its \(U\)-component is always the nonzero vector \(P_Ux\). It is a \(G\)-equivariant homotopy within \(S(E)\) from the radial form of the actual inclusion to the normalized projection \(P_Ux/\lVert P_Ux\rVert\). Under the radial homeomorphism \(|K_1|\to S(\mathbb R^3)\), given by \(x\mapsto Ax/\lVert Ax\rVert\), the latter is precisely the linear equatorial inclusion of \(S(U)\) into \(S(E)\), using the isometry \(A^*/\sqrt2\). This proves the map statement with its full equivariance, not merely its nonequivariant homotopy class.

**4. All subgroup fixed spaces and persistence.** For any \(H\le G\), fixed points of an orthogonal representation sphere satisfy \(S(V)^H=S(V^H)\). The character formula for fixed-vector dimension gives

\[
d_H=\frac1{|H|}\sum_{h\in H}\chi_U(h)\in\mathbb Z_{\ge0}.
\]

Galois conjugation sends this integer to \(\dim W^H\), hence \(\dim W^H=d_H\). Restricting the equivariant straightening homotopy to \(H\)-fixed points gives the claimed sphere-dimension doubling and the standard equatorial map. When \(d_H>0\), the source has reduced integral homology concentrated in degree \(d_H-1\), while the target has it concentrated in degree \(2d_H-1\); these degrees are different, so all reduced homology maps vanish. When \(d_H=0\), both fixed spaces are empty. No enumeration of subgroups is needed for this universal deduction.

**5. Full-symmetry rational quotient.** Spatial rotations preserve orientation of \(U\) and \(E\). Central inversion has determinant \(-1\) on the three-dimensional \(U\) and determinant \(+1\) on the six-dimensional \(E\). Therefore the top integral homology characters of the two representation spheres are respectively the central-inversion sign and the trivial character. Rational homology of a quotient by a finite simplicial group is the invariant part of rational homology after barycentric subdivision; hence the stated quotient calculation follows.

## Verification

The accompanying self-contained executable `verify_icosahedron.py` reconstructs the regular icosahedral graph from normalized golden-ratio coordinates. It checks twelve vertices, thirty edges, twenty triangular faces, graph diameter three with unique antipodes, and the absence of four-cliques; enumerates all 120 graph automorphisms; verifies their orthogonal geometric and six-axis signed-permutation realizations; and checks \(AA^*=2I_3\), all character rows and the positive supporting-halfspace condition on the twenty faces.

It independently enumerates the complete lattice of 164 subgroups by finite closure under right multiplication, and for each one checks that the six-dimensional invariant subspace dimension is twice the three-dimensional invariant dimension. The observed counts by \(d_H\) are \(86,62,15,1\) for dimensions \(0,1,2,3\), respectively. This computation is finite corroboration; the mathematical proof of the all-subgroup theorem is the character/Galois argument above. The code uses floating-point tolerance for coordinate equalities, not a formal exact arithmetic certificate; the relevant exact identity \(AA^*=2I_3\) and the global nonvanishing are proved algebraically above.

Reproduce with `python verify_icosahedron.py`, using Python 3, NumPy and NetworkX. No external input file is required.

## Relationship to prior work

Saleh, Titz Mite and Witzel, *Vietoris–Rips complexes of Platonic solids* (first arXiv version 2023-02-28, arXiv:2302.14388), Lemmas 2.2 and 2.3, establish the cross-polytope and polyhedral-boundary descriptions used in Step 1. Their Remark 4.5 gives an equivariant homology module for a **different**, dodecahedral radius-three stage. The associated thesis of Saleh, *On Vietoris-Rips Complexes of the 2-Sphere* (2023), Chapter 3, also supplies the nonequivariant icosahedral sphere stages. These pre-existing results are explicitly not claimed as new.

Adams, Lagoda, Moy, Sadovek and De Saha, *Persistent equivariant cohomology* (arXiv:2408.17331), develop persistent equivariant cohomology and calculate the continuous-circle case, not the concrete icosahedral subgroup fixed-point scale map. The new part here is the canonical \(3\oplus3'\) action, the **equivariant homotopy class of the actual radius-one-to-two inclusion**, and the uniform subgroup-by-subgroup fixed-space and integral persistence consequence.

## Limitations

The result concerns the regular icosahedron's graph metric and its thresholds one through three. It does not classify Rips complexes for perturbed or arbitrary twelve-point configurations, nor claim a full integral Borel-equivariant cohomology-ring calculation. At radius zero, subgroup-fixed vertices and their attaching maps to radius one can be read directly from the group action, but are not part of the stated fixed-map classification. The originality comparison cannot exclude unpublished or unindexed equivalent statements. Independent mathematical validation has not been performed.

## References

1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first posted 2023-02-28), especially Lemmas 2.2–2.3 and Remark 4.5. https://arxiv.org/abs/2302.14388
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral thesis (2023), Chapter 3, especially Theorem 3.2.1 and Lemmas 3.2.3–3.2.4. https://doi.org/10.22029/jlupub-17950
3. H. Adams, E. Lagoda, M. Moy, N. Sadovek, A. De Saha, *Persistent equivariant cohomology*, arXiv:2408.17331 (2024). https://arxiv.org/abs/2408.17331
4. M. Varisco, M. C. B. Zaremsky, *Equivariant Morse theory on Vietoris–Rips complexes and universal spaces for proper actions*, arXiv:1909.04487 (2019). https://arxiv.org/abs/1909.04487
