# A sphere quotient and equivariant torus retraction for square-cycle neighborhood complexes

## Finding
For every integer \(n\ge9\), let \(G_n=C_n^2\) be the graph with vertex set \(\mathbb Z/n\mathbb Z\) and edges at cyclic distance one or two. Write \(K_n=\mathcal N(G_n)\) for its **open** neighborhood complex: a nonempty vertex set is a face if all its members are adjacent to some common vertex. The graph's entire automorphism group is the dihedral group \(D_n\) of order \(2n\), acting by \(r(i)=i+1\) and \(s(i)=-i\).

Define the simplicial subcomplex \(T_n\) by the \(2n\) triangles
\[
 A_i=\{i,i+1,i+3\},\qquad B_i=\{i,i+2,i+3\},\quad i\in\mathbb Z/n\mathbb Z.
\]
Then \(T_n\) is a triangulated torus and \(K_n\) admits a **\(D_n\)-equivariant strong deformation retraction** onto \(T_n\). Its ordinary symmetry quotient satisfies
\[
\boxed{|T_n|/D_n\cong S^2,\qquad |K_n|/\operatorname{Aut}(G_n)\simeq S^2.}
\]
More precisely, \(|T_n|/\langle r\rangle\) is a torus, on which the residual reflection is an orientation-preserving involution with exactly four fixed points. On rational homology, every rotation acts trivially, every reflection negates both generators of \(H_1(K_n;\mathbb Q)\), and every dihedral element fixes the orientation class in \(H_2(K_n;\mathbb Q)\):
\[
H_1(K_n;\mathbb Q)\cong\varepsilon^{\oplus2},\qquad H_2(K_n;\mathbb Q)\cong\mathbf1,
\]
where \(\varepsilon\) is the rotation-trivial, reflection-sign character of \(D_n\). The f-vectors (numbers of vertices, edges, triangles, tetrahedra) are respectively \((n,4n,4n,n)\) for \(K_n\), and \((n,3n,2n)\) for \(T_n\).

## Assumptions and scope
All indices are modulo \(n\), and \(n\ge9\) throughout. Geometric realizations use ordinary simplicial topology; quotient means the **ordinary orbit space**, not a Borel construction. A dihedral action is the natural graph automorphism action, not an action on a different combinatorial model. The theorem gives an honest equivariant strong deformation retraction, followed by the classification of its orbit surface.

## Proof
**1. Full automorphism group.** The two graph edge types have different numbers of common neighbors: an edge joining \(i\) and \(i+1\) has two common neighbors, while one joining \(i\) and \(i+2\) has one. This holds without short-cycle wraparound for \(n\ge9\). Hence every automorphism preserves the distance-one edges, which form the cycle \(C_n\); it belongs to \(D_n\). Conversely every rotation and reflection preserves cyclic distance, so \(\operatorname{Aut}(G_n)=D_n\).

**2. Explicit equivariant strong deformation retraction.** The maximal simplices of \(K_n\) are the \(n\) tetrahedra
\[
\Delta_i=N(i)=\{i-2,i-1,i+1,i+2\}.
\]
Each tetrahedron meets \(T_n\) in its two triangular faces obtained by deleting \(i-2\) or \(i+2\). On \(\Delta_i\), write barycentric coordinates \((a,b,c,d)\) against the displayed ordered vertices. Put \(m=\min(a,d)\) and define
\[
\rho_i(a,b,c,d)=(a-m,b+m,c+m,d-m),\quad
H_t(x)=(1-t)x+t\rho_i(x),\quad0\le t\le1.
\]
These coordinates remain nonnegative and sum to one. The map lands in the union of the two retained faces, and fixes that union pointwise. For \(n\ge9\), two distinct tetrahedra intersect, if at all, in a face of \(T_n\). Indeed their sole non-retained edge is \(\{i-2,i+2\}\), of cyclic distance four, and this edge belongs to no other tetrahedron: among differences of two elements of \(\{-2,-1,1,2\}\), only the extreme pair has difference four, and no other difference is congruent to four modulo \(n\). Thus the local homotopies agree on intersections and assemble into a global strong deformation retraction. The reflection interchanges outer coordinates \(a,d\) and the inner coordinates \(b,c\); \(\min(a,d)\) is unchanged. Rotations merely shift indices. Therefore the retraction is \(D_n\)-equivariant. Alternatively the usual nonequivariant simplicial collapse uses two ordinary codimension-one elementary pairs per tetrahedron.

**3. The torus.** The triangles are distinct, and every edge in \(T_n\) has circular difference one, two, or three. There are \(3n\) edges; each lies in precisely two triangles. Each vertex link is a connected six-cycle, and the edge set of length one makes \(T_n\) connected. Thus \(|T_n|\) is a closed connected surface. The integral 2-chain
\[
z=\sum_{i\in\mathbb Z/n\mathbb Z}\bigl([i,i+1,i+3]-[i,i+2,i+3]\bigr)
\]
is a cycle, nonzero as a 2-chain, consistently orienting every triangle. (The two triangle types occur with opposite relative signs along shared edges.) Hence the surface is orientable. Its Euler characteristic is \(n-3n+2n=0\), so the classification of closed orientable surfaces gives \(|T_n|\cong T^2\). This directly establishes integral homology \(H_1\cong\mathbb Z^2\) and \(H_2\cong\mathbb Z\).

**4. Quotient by rotations.** No nonidentity rotation stabilizes a vertex, edge, or triangle setwise, because the edge differences are at most three and \(n\ge9\), and the triangles have unequal cyclic gaps. Consequently \(|T_n|\to|T_n|/C_n\) is a regular covering. The quotient has one vertex, three oriented loop edges \(e_1,e_2,e_3\), and two triangles giving the attaching words \(e_1e_2e_3^{-1}\) and \(e_2e_1e_3^{-1}\). Eliminating \(e_3\) gives the standard torus presentation \(\langle e_1,e_2\mid[e_1,e_2]\rangle\). It is also a closed orientable surface by local covering and the invariant orientation chain, and has Euler characteristic zero; hence it is a torus.

**5. Quotient by reflections.** In the preceding two-triangle torus, the residual reflection fixes the unique vertex and reverses each of the three loop edges, fixing its midpoint. It exchanges the two distinct open triangular faces, so these are **all four** fixed points. The orientation cycle \(z\) is preserved by reflections, since \(s(A_i)=-B_{-i-3}\) and \(s(B_i)=-A_{-i-3}\) as oriented simplices. Thus the residual involution is orientation-preserving. Its quotient is a closed connected orientable surface: away from fixed points it is locally a two-sheeted covering, and at an isolated fixed point an orientation-preserving involution has local half-turn type, whose quotient is a disk. Its Euler characteristic is
\[
\chi((|T_n|/C_n)/(D_n/C_n))=\frac{\chi(T^2)+4}{2}=2.
\]
The orientable surface classification yields \(|T_n|/D_n\cong S^2\). Since the retraction is equivariant, it descends to a strong deformation retraction on orbit spaces and proves the stated homotopy type.

**6. Homology representation.** The deck rotations on the oriented torus are orientation-preserving, and their induced maps on \(H_1\) are trivial: their nonidentity maps on the quotient covering have Lefschetz number zero, and the identity has trace two. More explicitly, each generator \(r\) acts trivially on the pullback of the two rational \(H^1\) generators from \(T_n/C_n\); the finite covering transfer is a rational isomorphism because both first Betti numbers equal two. The reflected loop generators \(e_1,e_2\) are reversed, so reflection acts as \(-I_2\) on first homology; it preserves the fundamental class. This gives the asserted character without inferring an infinite statement from finite calculations.

## Verification
The standalone `verify_square_cycle.py` deterministically reconstructs the full neighborhood complex, the proposed subcomplex and all dihedral permutations at each \(n\) from 9 through 64. It verifies both exact f-vectors, every tetrahedral overlap, the unique deleted outer edge of each tetrahedron, six-cycle vertex links, edge incidence counts, the integral oriented two-cycle, and all dihedral cellular Lefschetz traces. The recorded completed run ends in `CYCLE_SQUARE_DIHEDRAL_VERIFY_OK`. Finite checks illustrate and check the local combinatorics; steps 1–6 above give the proof for every \(n\ge9\).

## Relationship to prior work
Matsushita's 2014 preprint studies neighborhood complexes and graph double covers, providing an earlier topological context for symmetry-sensitive questions. Shukla's 2018 preprint, especially Theorem 2.5(C), Theorem 4.4 and its proof, already treats four-regular circulant neighborhood complexes and covers the underlying nonequivariant connected-sum-of-tori classification. In the present special case the surface is one torus, and **this nonequivariant fact is not claimed as new**. The new claim is the explicit *full dihedral-equivariant* retraction, exact dihedral homology representation, and identification of the ordinary full-automorphism quotient as a sphere. Shukla's inspected text does not discuss group quotients, reflections, or equivariant deformation retractions. Indexed mathematical records were compared for stronger coverage and equivalent formulations; this search does not prove exhaustive priority.

## Limitations
The restriction \(n\ge9\) avoids exceptional collisions of cyclic offsets; no claim about smaller values is made. The underlying orbit space of the original three-dimensional complex is only claimed **homotopy equivalent**, not homeomorphic, to \(S^2\). No Borel-equivariant or integral equivariant-cohomology assertion is made. The construction is an explicit proof but has not received independent mathematical audit, and an equivalent nonindexed observation may exist.

## References
- Takahiro Matsushita, *Neighborhood complexes and Kronecker double coverings*, initial arXiv submission 2014-04-06, arXiv:1404.1549, https://arxiv.org/abs/1404.1549.
- Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, initial arXiv submission 2018-02-13, arXiv:1802.04526, https://arxiv.org/html/1802.04526v2.
