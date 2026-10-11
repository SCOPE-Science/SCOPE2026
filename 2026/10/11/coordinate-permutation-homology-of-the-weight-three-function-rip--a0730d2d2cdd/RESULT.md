# Coordinate-permutation homology of the weight-three function–Rips sublevel on Boolean cubes

## Finding

Let \(n\geq3\), let \(Q_n=\{0,1\}^n\) carry Hamming distance, and let \(B_{n,3}=\{x\in Q_n:\operatorname{wt}(x)\leq3\}\). At inclusive distance scale \(2\), put \(K_n=\mathrm{VR}(B_{n,3};2)\). The symmetric group \(S_n\) acts by permutation of coordinates. As a rational \(S_n\)-representation,

\[
\widetilde H_i(K_n;\mathbb Q)\cong
\begin{cases}
\bigwedge^3\mathbb Q^n\oplus\bigwedge^4\mathbb Q^n,&i=3,\\
0,&i\ne3,
\end{cases}
\]

where \(\mathbb Q^n\) is the **coordinate permutation representation**, and exterior powers of degree greater than \(n\) are zero. In particular \(K_n\simeq\bigvee^{\binom{n+1}{4}}S^3\). For any coordinate permutation \(g\), with cycles of lengths \(\ell_1,\ldots,\ell_s\), its degree-three homology trace is the sum of the coefficients of degrees \(3\) and \(4\) in

\[
\prod_{j=1}^{s}\bigl(1-(-t)^{\ell_j}\bigr).
\]

The representation decomposition, not the nonequivariant sphere count, is the new assertion.

## Assumptions and scope

A Rips simplex is any finite subset whose **pairwise** Hamming distances are at most \(2\), including equality. The function is the integer-valued Hamming weight relative to the distinguished zero vector, with sublevel cutoff exactly \(3\). The coefficient field is \(\mathbb Q\). Coordinate permutations preserve this sublevel; arbitrary Hamming-cube translations do not. At each cutoff \(0\leq k\leq2\), the Rips complex of the weight-\(\leq k\) sublevel is a cone on the zero vector.

For clarity, identify binary vectors with subsets of \(\{0,1,\ldots,n-1\}\), and write \(\Lambda(S)\) for their integer binary encodings. Ordering these integers induces the filtration used in the nonequivariant proof below; the resulting representation theorem itself is independent of this ordering.

## Proof

**1. The local attachment and the homology rank.** Start with the contractible weight-\(\leq2\) complex and add vertices corresponding to all three-element subsets in increasing binary-encoding order. Consider a new triple \(T=\{a,b,c\}\) with \(0\leq a<b<c<n\). The vertices of its link among earlier vertices are precisely the three singletons in \(T\), the three pairs in \(T\), and earlier triples obtained by replacing one coordinate \(i\in T\) by a coordinate \(j<i\) outside \(T\).

If such a replacement coordinate satisfies \(j>a\), its triple \(U\) contains \(a\). In the link graph, the closed neighborhood of \(U\) is contained in the closed neighborhood of the singleton \(\{a\}\): original neighboring singles and pairs are adjacent to \(\{a\}\), and an earlier triple omitting \(a\) is of the form \(\{b,c,h\}\) with \(h<a\), hence cannot be adjacent to \(U\). Therefore \(U\) is a dominated vertex in this flag complex and can be deleted without changing homotopy type. Remove all such vertices. The remaining triples are exactly

\[
\{a,b,j\},\quad\{a,c,j\},\quad\{b,c,j\}\qquad(0\leq j<a).
\]

Let \(G_a=K_3\vee I_{a+1}\), the join of a triangle and an independent set of \(a+1\) vertices. Label the three vertices of the triangle by the pairs \(ab,ac,bc\). The outside vertex labeled zero corresponds to the original pair vertices; each other outside vertex, labeled by \(j<a\), corresponds to the three replacement triples listed above. The three edges of the original triangle correspond to the three singleton vertices. Two link vertices are adjacent exactly when the corresponding edges of \(G_a\) meet. Thus the reduced link is the clique complex of the line graph of \(G_a\).

For any finite simple graph \(G\), the clique complex of its line graph is homotopy equivalent to the two-skeleton of the clique complex of \(G\). Here is a direct argument. Every family of pairwise incident edges either has a common endpoint or comprises the edges of one graph triangle. The union of simplices from stars at graph vertices deformation-retracts to the barycentric subdivision of \(G\): contract each star simplex onto the tree of spokes from its barycenter to its edge-vertices, fixing common edge-vertices. The only remaining simplices are the filled graph triangles; their attaching boundaries retract to their corresponding three-edge loops in \(G\). This produces the two-skeleton of the clique complex of \(G\), up to homotopy.

Since \(G_a\) consists of \(a+1\) tetrahedra sharing a common triangular face after taking its clique complex, its two-skeleton is a union of \(a+1\) tetrahedral boundaries joined along that contractible face. Consequently the link of \(T\) is homotopy equivalent to \(\bigvee^{a+1}S^2\).

At every stage the previously built complex is a wedge of three-spheres (initially a point), hence is two-connected. Every map from the link wedge of two-spheres into it is nullhomotopic. Coning off the link therefore adds \(a+1\) three-sphere summands. Summing over all triples gives

\[
\sum_{0\leq a<b<c<n}(a+1)=\binom{n+1}{4}.
\]

This establishes the homotopy type and degree concentration. The link-counting part can also be obtained from the nonequivariant link analysis in Adamaszek–Adams; it is included here to make the equivariant argument self-contained.

**2. Three-coordinate classes.** For every three-element coordinate set \(S\), the coordinate-supported subcomplex \(K_S\) is the complete three-cube Rips complex at scale \(2\), namely the boundary of a four-dimensional cross-polytope and therefore a three-sphere. A permutation of the three coordinates acts on its top homology by its sign: a coordinate transposition exchanges two of the four antipodal-vertex pairs and preserves the other pairs' chosen positive representatives. Coordinate projection \(p_S\), setting coordinates outside \(S\) to zero, is a simplicial retraction of the inclusion \(K_S\hookrightarrow K_n\). For distinct triples \(S,T\), projection \(p_S(K_T)\) lies in the contractible subcomplex supported on \(S\cap T\), of size at most two. Hence the \(\binom n3\) top classes from distinct triples are independent. Their invariant span \(A_n\) is the induced sign representation on oriented three-subsets, canonically isomorphic to \(\bigwedge^3\mathbb Q^n\).

**3. The four-coordinate quotient.** The preceding homotopy calculation gives \(\dim H_3(K_4;\mathbb Q)=5\); its four three-coordinate classes form a four-dimensional invariant subspace \(A_4\cong\bigwedge^3\mathbb Q^4\). The residual quotient is one-dimensional. Its \(S_4\)-character is determined by the *exact* signed fixed-simplex Lefschetz calculation on the fifteen vertices and 317 simplices (including the empty face) of \(K_4\). In the conjugacy-class order \((1^4),(2,1^2),(2^2),(3,1),(4)\), the resulting traces on \(H_3(K_4;\mathbb Q)\) are \((5,-3,1,2,-1)\). Subtracting the exterior-cube character \((4,-2,0,1,0)\) gives \((1,-1,1,1,-1)\), exactly the sign character. A standard-library, exhaustive implementation for all 24 permutations is provided in `verify.py`.

**4. Four-coordinate classes and the global representation.** For each four-element set \(S\), let \(A_S\) be the subspace of \(H_3(K_S;\mathbb Q)\) generated by its four three-coordinate sphere classes. Its quotient \(Q_S=H_3(K_S;\mathbb Q)/A_S\) is the sign line just calculated. The inclusion into \(K_n\) maps a nonzero lift of \(Q_S\) to a class modulo \(A_n\). For any four-element \(T\), coordinate projection \(p_T\) maps \(A_n\) into \(A_T\). Moreover, when \(S\ne T\), the composite of inclusion from \(K_S\) and projection to \(K_T\) factors through the subcomplex supported on \(S\cap T\), with at most three coordinates, so its induced image lies in \(A_T\). For \(S=T\) it is the identity. Thus the images of the \(\binom n4\) local quotient lines in \(H_3(K_n;\mathbb Q)/A_n\) are independent. The dimension identity

\[
\dim\bigl(H_3(K_n;\mathbb Q)/A_n\bigr)
=\binom{n+1}{4}-\binom n3=\binom n4
\]

shows that they form a basis. Coordinate permutations send each four-set line to the corresponding four-set line, and its stabilizer acts on the line by the sign of the permutation of those four coordinates. Therefore this quotient is \(\bigwedge^4\mathbb Q^n\).

We have an exact sequence of rational \(S_n\)-modules

\[
0\longrightarrow\bigwedge^3\mathbb Q^n
\longrightarrow H_3(K_n;\mathbb Q)
\longrightarrow\bigwedge^4\mathbb Q^n\longrightarrow0.
\]

By semisimplicity of rational representations of finite groups, it splits. Finally \(\sum_k\operatorname{tr}(g\mid\bigwedge^k\mathbb Q^n)t^k=\det(I+tP_g)=\prod_j(1-(-t)^{\ell_j})\), yielding the character formula.

## Verification

From the package directory run `python3 verify.py`. The program uses only the Python standard library. It enumerates every simplex of \(K_n\) for \(n=3,4,5,6\) and verifies the signed fixed-simplex character for all \(6,24,120,720\) coordinate permutations respectively, comparing it to the two exterior-power character. It separately checks every new triple's link for \(3\leq n\leq7\), verifies that all discarded neighbors are dominated, and checks the remaining graph's exact line-graph adjacency and total predicted sphere multiplicity. It prints `VERIFY_OK` on success. These finite tests validate the complete finite \(S_4\) character certificate used in the proof; they are not used as substitutes for the uniform link and projection arguments.

## Relationship to prior work

Oudot and Waas (2026) introduce and study function–Rips complexes, where a fixed Rips scale is combined with a sublevel filtration. Adamaszek and Adams (2021) prove the non-equivariant sphere-wedge theorem for the full Hamming cube and, in their Lemma 7, provide the binary-order vertex-link analysis that also yields the **nonequivariant** rank used here; no originality is claimed for that rank. Galetto, Montaño and Wellner (2026) determine hyperoctahedral homology representations of the **untruncated full-cube** Rips complexes, whose group translations do not preserve this Hamming-weight sublevel. Their full-cube character does not determine the representation on this truncated complex. Briggs, Feng and Wells (2024) analyze full-cube facets and exact Hamming-weight layers, not the coordinate-permutation action on the **cumulative** weight-\(\leq3\) sublevel. The contribution here is the complete rational \(S_n\)-representation for that sublevel, uniformly in \(n\).

## Limitations

This theorem treats the single function–Rips cutoff at Hamming weight \(3\), not the entire persistence barcode or later cutoffs. The representation decomposition is over characteristic zero; no integral lattice decomposition or equivariant wedge-of-spheres splitting is asserted. The coordinate-permutation action is smaller than the full hyperoctahedral action, which does not preserve the chosen weight function. The overlap assessment is based on inspected public sources and indexed records; an unindexed equivalent result remains possible.

## References

1. S. Oudot and L. Waas, *Function-Rips complexes in persistent homotopy theory: Stability and persistent Latschev theorems*, arXiv:2603.23460, first public 2026-03-24. Related conference paper: *A Persistent Version of Latschev's Theorem*, DOI:10.4230/LIPIcs.SoCG.2026.82 (2026).
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021), especially Lemma 7 and Theorem 1.
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (2026), especially Sections 1, 4, 5.
4. J. Briggs, Z. Feng and C. Wells, *Facets in the Vietoris–Rips complexes of hypercubes*, arXiv:2408.01288 (2024), especially Sections 1 and 4.2.
