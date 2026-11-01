# Exact Haar polygon-type law for diagonal stretches of the small rhombicuboctahedron

## Finding
Let \(r=1+\sqrt2\), and let \(K\subset\mathbb R^3\) be the convex hull of the 24 signed coordinate permutations of \((r,1,1)\), the small (regular) rhombicuboctahedron. For any \(s_1,s_2,s_3>0\), put \(K_s=\operatorname{diag}(s_1,s_2,s_3)K\). If \(U\) is uniform on the unit sphere and \(N_s(U)\) is the vertex count of the central polygon \(K_s\cap U^\perp\), then almost surely \(N_s(U)\in\{8,12\}\). More precisely, writing \(a\ge b\ge c\) for the decreasing rearrangement of \(s_1|U_1|,s_2|U_2|,s_3|U_3|\), one has
\[
 N_s(U)=8\quad\Longleftrightarrow\quad a>r b+c;
 \qquad N_s(U)=12\quad\Longleftrightarrow\quad a<r b+c.
\]
The equality locus has spherical measure zero.

For \(p,q>0\), define
\[
 \Omega(p,q)=2\arctan\frac{pq}{(r+\sqrt{r^2+p^2})\bigl(r+1+\sqrt{(r+1)^2+p^2+q^2}\bigr)+p^2}.
\]
For the six ordered triples \((i,j,k)\) of distinct indices in \(\{1,2,3\}\), the complete probability law is
\[
 \Pr\{N_s(U)=8\}=\frac2\pi\sum_{(i,j,k)}\Omega(s_i/s_j,s_i/s_k),\qquad
 \Pr\{N_s(U)=12\}=1-\Pr\{N_s(U)=8\}.
\]
For the regular solid, with
\[
 D=(r+\sqrt{r^2+1})\bigl(r+1+\sqrt{(r+1)^2+2}\bigr)+1,
\]
this becomes
\[
 \Pr\{N(U)=8\}=\frac{24}{\pi}\arctan(1/D)=0.20786393703415482\ldots,
 \quad\Pr\{N(U)=12\}=0.79213606296584518\ldots.
\]
The expected polygon side count is \(\mathbb E N=12-4\Pr\{N=8\}=11.16854425186338\ldots\).

## Assumptions and scope
The model uses genuinely central (origin-passing) sections, not translated planes or orthogonal shadows. All diagonal factors are positive, and the orientation law is the rotation-invariant probability measure on \(\mathbb S^2\), with unoriented planes counted only once. For generic normals no vertex is in the cutting plane and each intersected polyhedron edge contributes precisely one polygon vertex. Spherical tie loci and normals through a polyhedron vertex form a finite union of great circles and have probability zero. All formulas and inequalities refer to this almost-sure generic case.

## Proof
**1. Complete edge geometry.** Put \(V\) equal to the signed permutations of \((r,1,1)\), and let \(e_i\) be the coordinate unit vectors. The facets of \(K=\operatorname{conv} V\) are the six axial squares \(\pm x_i=r\), the twelve diagonal squares \(\pm x_i\pm x_j=r+1\) (the two signs are chosen independently), and eight triangular faces \(\pm x_1\pm x_2\pm x_3=r+2\). Their incidence gives 24 vertices, 26 faces, and 48 edges. Equivalently, two distinct vertices form an edge precisely when their squared distance is \(4\). There are exactly 24 edges within an axial square, joining vertices with the same position for the coordinate of absolute value \(r\), and 24 swap edges, joining vertices with the large coordinate in different positions. Explicitly, within-square edges flip one of the other two coordinate signs, with the other coordinates fixed; swap edges exchange the positions of the positive magnitudes \(r\) and \(1\), leaving signs fixed. These descriptions list all 48 edges and can be checked against the stated supporting facets.

Since positive diagonal stretching preserves the face lattice and sends a section with normal \(U\) to one of \(K\) with (unnormalized) normal \((s_1U_1,s_2U_2,s_3U_3)\), the section count depends only on these weighted normal coordinates. Reflections and coordinate permutations reduce the count to \(a>b>c>0\).

**2. Exhaustive sign-chamber count.** Define four expressions
\[
 A=rb-a-c,\qquad B=rb-a+c,\qquad C=rc-a-b,\qquad D=rc-a+b.
\]
The signs of all 24 vertex inner products are fixed by the signs of \(A,B,C,D\), together with the strict ordering of \(a,b,c\). The remaining inner products with the large coordinate along \(a\) have fixed signs. We have \(A<B\), \(C<D\), \(C<A\), and \(D<B\). Thus the only possible nonboundary patterns in the order \((A,B,C,D)\) are

| Signs | Within-square crossings | Swap-edge crossings | Total |
|---|---:|---:|---:|
| `----` | 8 | 0 | 8 |
| `-+--` | 8 | 4 | 12 |
| `-+-+` | 8 | 4 | 12 |
| `++--` | 4 | 8 | 12 |
| `++-+` | 4 | 8 | 12 |
| `++++` | 0 | 12 | 12 |

This is an exhaustive finite sign enumeration: for each of the two explicit edge families above, the endpoints have opposite signs in exactly the numbers displayed. Equivalently, throughout every chamber,
\[
 N_{\mathrm{within}}=4\mathbf1_{A<0}+4\mathbf1_{C<0},\qquad
 N_{\mathrm{swap}}=4\mathbf1_{B>0}+4\mathbf1_{A>0}+4\mathbf1_{C>0}.
\]
The sum is \(8+4\mathbf1_{B>0}\). In particular, since \(B=rb-a+c\), the eight-vertex condition is precisely \(a>rb+c\). Direct integer representatives of the six chambers, in the same sign order, are \((100,2,1)\), \((100,30,28)\), \((100,30,29)\), \((100,42,1)\), \((100,51,21)\), and \((100,73,72)\), respectively. They are for checking existence; the formulas above, not testing only those representatives, establish the universal count.

**3. Haar measure as six exact solid angles.** Reflection symmetry permits restriction to the positive normal octant. The event \(a>rb+c\) has a unique ordering \((i,j,k)\) such that
\[
 s_iU_i>r s_jU_j+s_kU_k,\qquad s_jU_j>s_kU_k>0.
\]
These six disjoint simplicial cones partition the eight-vertex event, up to null boundaries. Their rays, after a common positive rescaling, are
\[
 v_0=e_i,\quad v_1=re_i+pe_j,\quad v_2=(r+1)e_i+pe_j+qe_k,
 \qquad p=s_i/s_j,\ q=s_i/s_k.
\]
The standard solid-angle identity for three linearly independent ray vectors is
\[
 \operatorname{area}_{\mathbb S^2}\operatorname{cone}(v_0,v_1,v_2)
 =2\arctan\frac{\lvert\det(v_0,v_1,v_2)\rvert}{\|v_0\|\|v_1\|\|v_2\|+(v_0\cdot v_1)\|v_2\|+(v_1\cdot v_2)\|v_0\|+(v_2\cdot v_0)\|v_1\|}.
\]
Here the absolute determinant is \(pq\), and the denominator factors as
\[
 (r+\sqrt{r^2+p^2})\bigl(r+1+\sqrt{(r+1)^2+p^2+q^2}\bigr)+p^2.
\]
Therefore each positive-octant cone has area \(\Omega(p,q)\). There are eight sign octants; division by the full sphere area \(4\pi\) gives the prefactor \(2/\pi\) and proves the complete probability law. When all stretch factors equal one, the six summands coincide and yield the displayed closed form. The expectation follows since there are only two possible vertex counts.

## Verification
A standalone standard-library Python program `verify.py` reproduces the 24 vertices and 48 edges using exact arithmetic in \(\mathbb Q(\sqrt2)\), enumerates the six feasible normal-sign chambers and confirms the edge-crossing table. It checks 3916 nonboundary ordered integer-normal examples by exact sign comparisons; verifies the exact solid-angle probability against a separate gnomonic-coordinate quadrature in the regular case; and compares the analytic distribution with 80,000 sampled Haar normals for each of four stretch vectors. Run it from this package with `python verify.py`. These finite checks cannot prove the all-direction claim; that follows from the edge-list/chamber enumeration and spherical-cone proof above.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg, and Prün (2026) study the combinatorial information contained in central sections and show reconstruction theorems for sufficiently generic simple polytopes, as well as failures of broad slicing analogues. The rhombicuboctahedron is a non-simple polytope; that work does not give its exact random-orientation section counts or a Haar law for its diagonal stretches. Brandenburg, De Loera, Luo, and Meroni (2026) construct a framework for computing moments of polyhedral slices and slabs, including cube applications; their general algorithm is not an evaluated eight-versus-twelve polygon law for this Archimedean solid. Brandenburg, De Loera, and Meroni (2023) give general section-combinatorics chamber methods and optimize sections of several polytopes; the present evaluated distribution uses related standard geometric ideas rather than claiming a new general algorithm. Classical formulas for simplicial solid angles are used as a standard ingredient.

## Limitations
No independently verified publication priority is claimed: an equivalent evaluated law could exist in older stereology, Archimedean-solid section tables, or under polarity as a shadow-vertex distribution for the dual deltoidal icositetrahedron. The theorem applies only to central sections of the specified solid and its positive diagonal stretches. It gives neither noncentral sections nor section-area distributions. Finite numerical experiments are consistency tests, not a substitute for the exact geometric argument. Independent mathematical audit has not been performed.

## References
1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first posted 2026-09-14). https://arxiv.org/abs/2609.16195
2. M.-C. Brandenburg, J. A. De Loera, Y. Luo, C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643 (first posted 2026-03-26). https://arxiv.org/abs/2603.25643
3. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first posted 2023-04-27). https://arxiv.org/abs/2304.14239
4. E. W. Weisstein, *Small Rhombicuboctahedron*, MathWorld, geometry reference for the vertex and facet presentation. https://mathworld.wolfram.com/SmallRhombicuboctahedron.html
