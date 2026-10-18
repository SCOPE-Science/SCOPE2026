# Complete face-lattice law for generic central sections of type-A root polytopes

## Finding
For every integer \(n\ge3\), let \(e_1,\ldots,e_n\) denote the standard unit vectors, and let
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\}
\subset E_n=\{x\in\mathbb R^n:\textstyle\sum_i x_i=0\}.
\]
Choose a linear functional \(u\in\mathbb R^n\) with pairwise distinct coordinates, and put \(Q_u=P_n\cap\{x:\langle u,x\rangle=0\}\). Index positions in increasing order of their \(u\)-coordinates. Then \(Q_u\) is an \((n-2)\)-dimensional polytope, whose entire face lattice depends only on this order and, up to relabeling, is independent of the values of \(u\).

For every \(0\le k\le n-3\), the number of proper nonempty \(k\)-faces is exactly
\[
\boxed{f_k(Q_u)=\binom{n}{k+3}\bigl(2^{k+3}-2(k+3)\bigr).}
\]
More precisely, its proper nonempty faces correspond uniquely to ordered pairs of disjoint nonempty index subsets \((I,J)\) satisfying
\[
\min\operatorname{rank}_u(I)<\max\operatorname{rank}_u(J),\qquad
\min\operatorname{rank}_u(J)<\max\operatorname{rank}_u(I).
\]
The corresponding face is the central section of \(F_{I,J}=\operatorname{conv}\{e_i-e_j:i\in I,\ j\in J\}\), has dimension \(|I|+|J|-3\), and the face-order relation is coordinatewise inclusion of the two index sets. In particular, \(Q_u\) has \(2\binom n3\) vertices and \(2^n-2n\) facets. The entire face-number profile obeys the compact generating identity
\[
\sum_{k=0}^{n-3} f_k(Q_u)z^{k+3}=(1+2z)^n-1-2nz(1+z)^{n-1}.
\]

Every section vertex comes from a unique ordered triple \(a<b<c\) in the \(u\)-order, with two opposite vertices on the edges joining the two roots that share the middle index. The vertices of the face indexed by \((I,J)\) correspond precisely to rank-ordered triples \(a<b<c\) for which the membership pattern in \(I\) and \(J\) alternates: \(I,J,I\) or \(J,I,J\). For \(n=5\) the three-dimensional section has face vector \((20,40,22)\); its 22 polygonal facets comprise ten triangles, ten quadrilaterals and two pentagons.

## Assumptions and scope
The statement covers all \(n\ge3\) and every real \(u\) with \(u_i\ne u_j\) for \(i\ne j\), with no genericity requirement beyond these inequalities. The hyperplane passes through the origin. All faces of the section are Euclidean convex faces. A rank is the position, from 1 to \(n\), of an index after sorting the coordinates of \(u\). The face-count convention counts only proper nonempty faces: the whole \(Q_u\) and the empty face are excluded. Zero-coordinate shifts of \(u\) do not change the hyperplane on \(E_n\).

## Proof
**1. Faces of the ambient polytope.** A linear form on \(E_n\) is represented by some \(p=(p_i)\). Let \(I\) be the positions of its maximum, and \(J\) those of its minimum. A nonconstant \(p\) has disjoint nonempty \(I,J\), and its maximizing roots are exactly \(e_i-e_j\) for \(i\in I,j\in J\). Conversely, every disjoint ordered pair of nonempty subsets is obtained by assigning value 1 on \(I\), value 0 on \(J\), and intermediate values elsewhere. Thus all proper nonempty faces are uniquely the \(F_{I,J}\). Under the affine mapping \((s,t)\mapsto s-t\) on disjoint coordinate sets, \(F_{I,J}\) is a product of simplices of dimension \(|I|+|J|-2\).

**2. Which ambient faces are cut.** On the vertices \(e_i-e_j\) of \(F_{I,J}\), the cutting form takes values \(u_i-u_j\), none zero. The hyperplane meets the relative interior of the face exactly when some such differences are positive and some negative. Since the smallest and largest index ranks in a set determine these signs, the condition is precisely the pair of strict interleaving inequalities in the statement. Such a crossing is transverse to the affine span and produces a face of dimension \(|I|+|J|-3\). A section of a polytope that avoids its vertices inherits all its proper faces by intersecting the section with the unique minimal ambient face whose relative interior it meets. Consequently no faces are omitted or multiply counted. An inclusion between section faces implies an inclusion between their minimal ambient faces (take a relative-interior point of the smaller face), giving the stated coordinatewise face order.

**3. Enumeration.** Fix the union \(S=I\cup J\) of size \(m\ge3\). There are \(2^m-2\) ordered nonempty bipartitions of \(S\). The noninterleaved assignments are exactly the \(m-1\) initial-versus-terminal cuts and their \(m-1\) reversals, for \(2(m-1)\) excluded assignments. Therefore exactly \(2^m-2m\) mixed assignments remain. Since a face with such a union has dimension \(m-3\), multiplying by \(\binom nm\) gives the formula. Taking \(m=3\) and \(m=n\) yields the vertex and facet counts, respectively.

**4. Explicit section vertices and local sizes.** Write the indices of a triple in increasing \(u\)-order as \(a<b<c\). The roots \(e_b-e_a\) and \(e_b-e_c\) have opposite \(u\)-values. Their edge crosses the hyperplane at
\[
x=e_b-\frac{u_c-u_b}{u_c-u_a}e_a-\frac{u_b-u_a}{u_c-u_a}e_c.
\]
The opposite edge gives \(-x\), and the first three steps prove that these exhaust the vertices. A face \(F_{I,J}\) contains these crossed edges exactly when the middle index belongs to one of the two sets and both endpoints belong to the other; hence the alternating-triple rule. For \(n=5\), applying this rule to the 22 facet bipartitions yields the \(10+10+2\) distribution recorded above.

## Verification
Run the self-contained standard-library checker by placing `check_root_section.py` beside this document and invoking `python3 check_root_section.py`. It calculates exact rational intersection vertices, rechecks all Boolean root-polytope support inequalities on the vertices, verifies affine dimensions of every facet for three independent coordinate-order permutations in each size \(n=3,4,5,6,7\), compares all face counts to independent ordered-partition enumeration, and checks the exact facet-size spectrum at \(n=5\). Its expected terminal markers are `ROOT_CENTRAL_SECTION_OK cases=15` and `A4_SECTION_FACET_SIZE_SPECTRUM_OK {3: 10, 4: 10, 5: 2}`. These finite checks corroborate, but do not replace, the argument for arbitrary \(n\).

## Relationship to prior work
The type-A root polytope and its full original face structure are classical: Ardila, Beck, Hoşten, Pfeifle and Seashore describe its facets as products of simplices and develop boundary triangulations [1]. Cellini and Marietti present a general face description and \(f\)-polynomial for the *unsectioned* root polytope, and investigate arrangements of hyperplanes spanned by its codimension-two faces [2]. Those facts are used as background, not asserted as new. Neither inspected statement gives the interleaving face poset of **all** generic central sections or its \(\binom n{k+3}(2^{k+3}-2(k+3))\) face-number law. The derivation requires identifying which root faces are crossed by the central hyperplane and showing that these crossings give every section face without duplications. Zhang develops regular *central subdivisions* of this root polytope and generic alcoved polytopes, not sections by one hyperplane [3]. General work on vertex counts of unrestricted hyperplane sections is related; its abstract does not supply the present type-A face-poset formula [4].

## Limitations
The claim is restricted to **central** hyperplanes, to the complete type-A root configuration, and to distinct entries of the cutting normal. Noncentral sections and normals with tied entries can have different face lattices. Numerical checks only cover \(n\le7\). The exact statement follows from the proof, which is independent of any exhaustive computation. A mathematically equivalent historical theorem under a different name remains a priority risk; no independent mathematical review has been performed.

## References
[1] F. Ardila, M. Beck, S. Hoşten, J. Pfeifle and K. Seashore, “Root polytopes and growth series of root lattices,” arXiv:0809.5123v1 (first public 2008-09-30), https://arxiv.org/abs/0809.5123.

[2] P. Cellini and M. Marietti, “Root polytopes and abelian ideals,” arXiv:1207.3429v1 (first public 2012-07-14), https://arxiv.org/abs/1207.3429.

[3] Y. Zhang, “A Correspondence between Generic Alcoved Polytopes and Subdivisions of the Root Polytope of Lie Type A,” 2016 SPUR final paper, 2016-08-03, https://math.mit.edu/documents/spur/2016ZhangY.pdf.

[4] J. A. De Loera, G. Lopez-Campos and A. J. Torres, “On the Number of Vertices in a Hyperplane Section of a Polytope,” arXiv:2412.12419 (first public 2024-12-17), https://arxiv.org/abs/2412.12419.
