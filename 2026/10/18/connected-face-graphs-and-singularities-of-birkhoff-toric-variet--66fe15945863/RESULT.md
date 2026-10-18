# Connected face graphs and singularities of Birkhoff toric varieties

## Finding

Let \(k\) be an algebraically closed field and let \(n\ge4\). Write \(B_n\) for the \(n\times n\) Birkhoff polytope of nonnegative matrices with every row and column sum equal to one. Let \(X_n\) be the normal projective toric variety with fan the normal fan of \(B_n\), with the lattice of integer matrices whose row and column sums vanish as its character lattice. The torus orbits of \(X_n\) correspond to nonempty faces \(F\subseteq B_n\).

For a face \(F\), define its support graph \(G_F\) to be the bipartite graph on the \(n\) row and \(n\) column vertices with an edge \((i,j)\) precisely when the \((i,j)\) entry is nonzero at some point of \(F\). Let \(c(F)\) be its number of connected components. Then the orbit indexed by \(F\) is smooth in \(X_n\) if and only if \(c(F)=1\). At a point of that orbit the local Weil divisor class group is free of rank \(c(F)-1\). In particular the singular locus equals the non-\(\mathbb Q\)-factorial locus, set-theoretically.

The irreducible components of the reduced singular locus are indexed by pairs \((R,C)\) of proper, nonempty subsets of the row and column sets satisfying \(|R|=|C|=a\), modulo simultaneous complementation \((R,C)\sim(R^c,C^c)\). The indexed component is the torus-orbit closure attached to the block face
\[
F_{R,C}=\{A\in B_n:A_{ij}=0\text{ if exactly one of }i\in R,\ j\in C\},
\]
which is affinely the product \(B_a\times B_{n-a}\). There are exactly
\[
\boxed{\frac12\left(\binom{2n}{n}-2\right)}
\]
such components, of dimension \((a-1)^2+(n-a-1)^2\) and codimension \(2a(n-a)-1\) in \(X_n\).

Put \(q=a(n-a)\). A normal toric slice transverse to the dense orbit of this component is the affine variety of rank-at-most-one \(q\times q\) matrices, equivalently the cone over \(\mathbb P^{q-1}\times\mathbb P^{q-1}\) in its Segre embedding. Its local divisor class group is \(\mathbb Z\), and its Hilbert--Samuel multiplicity at the vertex is \(\binom{2q-2}{q-1}\).

For example, \(X_4\) has precisely \(34\) singular components: \(16\) components of dimension \(4\) with transverse \(3\times3\) rank-one cones of multiplicity \(6\), and \(18\) components of dimension \(2\) with transverse \(4\times4\) rank-one cones of multiplicity \(20\).

## Assumptions and scope

All varieties and local structures are taken over the algebraically closed field \(k\), without a characteristic restriction. The term singular locus refers to its reduced underlying subvariety, not to the Jacobian subscheme. Normal toric slices mean the transverse factors obtained by localizing an affine toric orbit chart at its orbit; the assertion is not that the entire projective component has a globally trivial normal bundle. The result concerns \(n\ge4\). The classical \(n=3\) Birkhoff toric cubic, with nine singular lines, is used only as a consistency check, not as a new case.

## Proof

**1. Lattices, face graphs and dimensions.** Let
\[
M=\{u\in\mathbb Z^{n\times n}:\sum_j u_{ij}=0\ (1\le i\le n),\quad\sum_i u_{ij}=0\ (1\le j\le n)\}.
\]
This is saturated of rank \((n-1)^2\). Let \(E=E(G_F)\) and \(T=([n]\times[n])\setminus E\). Every edge of \(G_F\) occurs in a perfect matching because \(F\) is a face of the convex hull of permutation matrices. Each connected component \(G_\nu\) therefore has equal row and column vertex counts. The affine span of \(F\) is the doubly stochastic affine system supported on \(E\). Within each connected component there is one dependent row/column sum equation, so the rank of the constraints is \(2n-c(F)\). Every edge in \(E\) is positive at the average of all perfect matchings of \(G_F\). Thus
\[
\dim F=|E|-2n+c(F).
\]
For \(n\ge3\), the \(n^2\) coordinate inequalities of \(B_n\) are its distinct facets. Therefore the normal cone \(\sigma_F\) has exactly \(|T|=n^2-|E|\) extremal rays, the coordinate functionals restricted to \(M\), and dimension
\[
\dim\sigma_F=(n-1)^2-\dim F=n^2+1-|E|-c(F).
\]
Its ray excess is therefore exactly \(c(F)-1\).

**2. An integral exact sequence.** Consider the restriction map \(\rho:M\longrightarrow\mathbb Z^T\). For each connected component \(G_\nu\), put
\[
\delta_\nu(v)=\sum_{i\in R_\nu,\ j\notin C_\nu}v_{ij}-\sum_{i\notin R_\nu,\ j\in C_\nu}v_{ij},\qquad v\in\mathbb Z^T.
\]
The \(\delta_\nu\) sum to zero. Their combined map \(\delta:\mathbb Z^T\to\{(z_1,\ldots,z_c)\in\mathbb Z^c:\sum z_\nu=0\}\) is surjective: every directed edge across two components is in \(T\), and its basis vector maps to a root \(e_\nu-e_\mu\). Also \(\delta\rho=0\). Conversely, if \(\delta(v)=0\), then inside each connected support component the desired row and column corrections have equal totals. They can be filled integrally along a spanning tree of that connected bipartite graph, since the oriented incidence matrix of a tree maps integer edge flows onto all zero-total integer vertex demands. Hence
\[
0\longrightarrow \ker\rho\longrightarrow M\xrightarrow{\rho}\mathbb Z^T\xrightarrow{\delta}\mathbb Z^{c(F)-1}\longrightarrow0
\]
is exact. In particular \(\rho(M)=\mathbb Z^T\) when \(G_F\) is connected.

**3. Smoothness and divisor classes.** The cone \(\sigma_F\) is generated by the coordinate facet normals indexed by \(T\), and its dual semigroup in \(M\) is described by nonnegativity of the \(T\)-coordinates (replacing every coordinate by its negative merely changes the sign convention). After inverting \(\ker\rho\), its transverse character semigroup is \(\rho(M)\cap\mathbb N^T\). If \(c(F)=1\), step 2 identifies this with a free coordinate monoid \(\mathbb N^T\); the cone is unimodular and the orbit is smooth. If \(c(F)>1\), step 1 gives more rays than the dimension, so the normal cone is nonsimplicial and the orbit is singular and non-\(\mathbb Q\)-factorial. The affine toric divisor exact sequence gives
\[
\operatorname{Cl}(\mathcal O_{X_n,O_F})\cong\mathbb Z^T/\rho(M)\cong\mathbb Z^{c(F)-1};
\]
here the local notation denotes the class group at a point of the orbit, equivalently that of the orbit's transverse affine chart. This calculation holds integrally and contains no hidden torsion.

**4. Inclusion-maximal singular faces.** Suppose \(c(F)\ge2\). Group the connected components of \(G_F\) into two nonempty collections. Their combined row and column vertex sets each have equal cardinalities. Enlarge \(G_F\) by inserting every within-block edge for these two collections, obtaining the complete disjoint union \(K_{a,a}\sqcup K_{n-a,n-a}\). This is a face graph and defines \(F_{R,C}\supseteq F\). Conversely, any proper face graph containing this complete two-block graph and still disconnected would have to preserve the two components, but all within-block edges have already been inserted; hence it cannot be strictly larger. The block faces are therefore exactly the maximal disconnected-support faces. Toric orbit-closure order is face containment, so they index the irreducible components of the singular locus. There are \(\sum_{a=1}^{n-1}\binom na^2\) ordered choices, each counted twice by complementary blocks. Vandermonde's identity gives the claimed total. The block face is \(B_a\times B_{n-a}\), so its dimension and codimension follow from \(\dim B_s=(s-1)^2\).

**5. Exact transverse singularities.** For \(F_{R,C}\), the zero positions \(T\) are the two off-diagonal rectangles, each containing \(q=a(n-a)\) cells. The exact sequence in step 2 specializes to
\[
\rho(M)=\{(u,v)\in\mathbb Z^q\oplus\mathbb Z^q:\sum_i u_i=\sum_j v_j\}.
\]
The nonnegative part is generated by the \(q^2\) vectors \((e_i,e_j)\): any nonnegative pair with equal total can be paired as a sum of such vectors. Its semigroup algebra is the subalgebra \(k[s_i t_j]\subset k[s_1,\ldots,s_q,t_1,\ldots,t_q]\), namely
\[
k[z_{ij}:1\le i,j\le q]/I_2(z),
\]
where \(I_2(z)\) is the ideal of all \(2\times2\) minors. This is the stated normal rank-one determinantal cone. Its projective base is the Segre variety \(\mathbb P^{q-1}\times\mathbb P^{q-1}\), which has degree \(\binom{2q-2}{q-1}\) by the binomial expansion of \((H_1+H_2)^{2q-2}\). The cone's vertex has that Hilbert--Samuel multiplicity. The class group follows also from step 3 with two components.

## Verification

Execute `python3 verify_birkhoff.py` using only the Python standard library. The program independently enumerates every intersection of coordinate facets for \(B_3\) and \(B_4\), using all permutation matrices, deduplicates the resulting faces, counts connected components of their support graphs, checks the exact ray-excess formula on every face, and verifies that the inclusion-maximal singular faces are precisely the balanced two-block faces. It returns `VERIFY_OK` after checking the component formula and dimension/codimension conditions for block faces through \(n=7\).

The complete calculations gave \(49\) nonempty faces and \(9\) maximal singular faces for \(B_3\), and \(7443\) nonempty faces, \(658\) disconnected-support faces and \(34\) maximal singular faces for \(B_4\), distributed as \(16\) of dimension \(4\) and \(18\) of dimension \(2\). These computations are finite corroboration; the all-\(n\) proof is the integral sequence and graph argument above.

## Relationship to prior work

Paffenholz, *Faces of Birkhoff Polytopes* (initial public preprint 2013), develops the face-graph correspondence, the product decomposition of disconnected face graphs, and the face dimension formula. These foundational face-combinatorial facts are used explicitly here and are not claimed as new. His paper studies combinatorial types and low-dimensional face classifications; it does not state the all-rank toric singular-component count, the local divisor-group formula, or the transverse Segre cones. Lenz, *Toric Ideals of Flow Polytopes* (2010), treats degree-three generators and Gröbner bases for the Birkhoff toric ideals, not the present local geometry. General toric smoothness and divisor-sequence criteria are standard and acknowledged. The small \(n=3\) cubic singular scheme (nine lines and ordinary-double-point transverse germs) is already available and excluded from the novelty claim.

## Limitations

The classification is set-theoretic for the singular locus; its possibly nonreduced singular scheme, component intersection schemes, and resolutions are not computed. A transverse cone is identified at the generic orbit, not at every point of its closure. The result gives no global identification of completed local rings at intersections of distinct singular components beyond the orbitwise class-group formula. Originality was checked against accessible primary sources and searchable records, but an equivalent statement under different terminology could remain unindexed.

## References

1. A. Paffenholz, *Faces of Birkhoff Polytopes*, arXiv:1304.3948, initial version April 14, 2013, especially Section 2.2 and Equation (2.2); journal version *Electronic Journal of Combinatorics* 22(1), P1.67 (2015). https://arxiv.org/pdf/1304.3948
2. M. Lenz, *Toric Ideals of Flow Polytopes*, *Discrete Mathematics & Theoretical Computer Science Proceedings*, FPSAC 2010, pp. 889--896. https://dmtcs.episciences.org/en/articles/2837/download
3. D. A. Cox, J. B. Little, and H. K. Schenck, *Toric Varieties*, American Mathematical Society, 2011. Standard cone smoothness and toric divisor exact sequences; bibliographic background only.
