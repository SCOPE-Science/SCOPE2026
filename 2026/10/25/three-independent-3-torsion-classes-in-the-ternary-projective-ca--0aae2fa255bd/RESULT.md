# Three independent 3-torsion classes in the ternary projective cap complex

## Finding

Let \(P=\operatorname{PG}(2,\mathbb F_3)\) be the plane of thirteen projective points. Its **cap complex** \(X\) is the abstract simplicial complex whose faces are the subsets of points containing no three collinear points (projective arcs). There is an exact integral homology classification
\[
\widetilde H_i(X;\mathbb Z)\cong
\begin{cases}
(\mathbb Z/3\mathbb Z)^3,&i=2,\\
\mathbb Z^{66},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, \(X\) has exactly three independent order-three homology classes in degree two, while its top homology is free.

Let \(K=X^{(2)}\), the independence complex of the rank-three projective-geometry matroid. It has \(H_2(K;\mathbb Z)\cong\mathbb Z^{168}\). Every four-point projective quadrangle (every four-element arc) supports the oriented two-cycle given by the boundary of its abstract tetrahedron. The 234 such cycles generate a full-rank sublattice \(L\subset H_2(K;\mathbb Z)\), with
\[
H_2(K;\mathbb Z)/L\cong(\mathbb Z/3\mathbb Z)^3,
\qquad [H_2(K;\mathbb Z):L]=27.
\]
Their supports are minimal among nonzero two-cycles of \(K\). The full projective group \(\operatorname{PGL}_3(\mathbb F_3)\), of order 5616, acts transitively on all 234 quadrangles.

## Assumptions and scope

The vertices are the one-dimensional subspaces of \(\mathbb F_3^3\). Choose the unique representative of each such subspace whose first nonzero coordinate equals \(1\), and order the resulting thirteen representative triples lexicographically. For distinct vertices \(i,j,k\), their triple is a face of \(K\) exactly when the determinant of their representative vectors is nonzero modulo three. A four-set belongs to \(X\) exactly when all four of its constituent triples belong to \(K\); no five-set has this property. Boundary chains are integral and every simplex is oriented by increasing vertex index. The result concerns this finite, explicitly defined simplicial complex; it does not assert an analogous statement for arbitrary projective-plane order.

## Proof

**1. Exhaustive face model.** There are \((3^3-1)/(3-1)=13\) projective points, and every pair is independent. Direct determinant enumeration gives face numbers \((f_0,f_1,f_2,f_3)=(13,78,234,234)\). Enumeration of all \(\binom{13}{5}=1287\) candidate five-sets verifies that each contains a collinear triple; hence no higher face exists. Every noncollinear triple extends to a quadrangle. The accompanying standalone program executes these exhaustive tests with exact arithmetic over \(\mathbb F_3\).

**2. Integral boundary certificates.** Enumerate the faces in increasing lexicographic order. Write \(\partial_k\) for the integral simplicial boundary from oriented \(k\)-faces to oriented \((k-1)\)-faces, with entry \((-1)^j\) for deleting the vertex in position \(j\). The matrices have dimensions \(13\times78\), \(78\times234\), and \(234\times234\). Direct multiplication verifies \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\). Exact integer Smith diagonalization gives
\[
\operatorname{SNF}(\partial_1)=(1^{12},0^{1}),\qquad
\operatorname{SNF}(\partial_2)=(1^{66},0^{12}),
\]
where these notations specify the nonzero invariant factors and the remaining zero *row* positions (not the total number of zero columns). The nonzero invariant factors of \(\partial_3\) are precisely \(1^{165},3^3\), with sixty-six additional zero diagonal positions. The complete executable calculation, rather than any log alone, is the finite certificate. It reconstructs the entries and tests the asserted Smith invariants.

**3. Homology deduction.** Since \(\partial_1\) has rank 12 and \(\partial_2\) has rank 66 with all nonzero Smith factors equal to 1, \(\ker\partial_1/\operatorname{im}\partial_2=0\). Also \(\ker\partial_2\) is a primitive rank-168 lattice in \(\mathbb Z^{234}\), and \(\operatorname{im}\partial_3\) is a full-rank sublattice of it. The exact sequence
\[
0\longrightarrow\ker\partial_2/\operatorname{im}\partial_3
\longrightarrow\operatorname{coker}\partial_3
\longrightarrow\operatorname{im}\partial_2\longrightarrow0
\]
identifies the torsion subgroup of \(\operatorname{coker}\partial_3\) with that of \(H_2(X;\mathbb Z)\), because the quotient \(\operatorname{im}\partial_2\) is free. The invariant factors of \(\partial_3\) give exactly three independent order-three torsion factors and no free part for \(H_2\), since both \(\ker\partial_2\) and \(\operatorname{im}\partial_3\) have rank 168. Finally, \(H_3=\ker\partial_3\) is free of rank \(234-168=66\); connectedness of the complete one-skeleton gives \(\widetilde H_0=0\).

**4. The quadrangle-cycle lattice.** Removing the tetrahedra gives \(K=X^{(2)}\), whose second homology is \(\ker\partial_2\cong\mathbb Z^{168}\). Every column of \(\partial_3\) is the oriented tetrahedral boundary on a four-point quadrangle. Their span is \(\operatorname{im}\partial_3\) and the just-computed quotient is \((\mathbb Z/3\mathbb Z)^3\), of order 27. On at most three vertices, no nonzero two-cycle exists. Among four-vertex induced subcomplexes, a nonzero two-cycle requires all four triangles: otherwise an edge belongs to precisely one available triangle and forces its coefficient to vanish. Hence the quadrangle boundaries give exactly the minimum-support nonzero two-cycles. For group transitivity, any ordered quadrangle is a projective frame. Sending its first three points to coordinate axes and rescaling them to send its fourth point to \((1,1,1)\) shows that a unique projective linear transformation sends any ordered quadrangle to the standard frame. The order of the group is \(|\operatorname{GL}_3(\mathbb F_3)|/2=5616=234\cdot4!\).

## Verification

Run `python verify_pg3_arc.py` with Python 3.11+ and SymPy 1.13+; see `requirements.txt`. The verifier constructs all faces and signed boundary matrices from finite-field determinants, checks the chain identities and five-arc nonexistence, then computes Smith normal forms exactly over \(\mathbb Z\). It exits with an exception on any mismatch. The expected deterministic marker is `VERIFY_OK_PROJECTIVE_TERNARY_QUADRANGLE_HOMOLOGY`; the recorded output is supplied as `verification_output.txt`. Independent of the Smith calculation, the face counts and the projective-frame argument explain the symmetry claim. No large black-box topological classification is invoked.

## Relationship to prior work

General matroid-independence-complex shellability gives the sphere-wedge topology of the two-skeleton \(K\), but does not imply that the integral sublattice generated by all quadrangle boundaries has index 27. The work of Ranade–Sadanand–Sullivan develops general methods for integral top-homology cycle bases, but does not identify this projective-geometry instance or its quotient. The work of Ardila–Castillo–Samper concerns matroid activity and shellings, not the present cap-complex three-boundary. Superdock constructs distinct projective-plane simplicial complexes whose facets come from copies of the plane's line design; at order three these have 26 facets, whereas the cap complex here has 234 tetrahedra. Previously reported neighborhood complexes of ternary projective nonincidence graphs likewise have different vertices/faces and do not imply this homology calculation. This comparison is a best-knowledge originality assessment, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The exact Smith calculations are finite, reproducible mathematical computations and establish only this specific projective plane of order three. They are not an infinite-family proof. This result determines homology and a homology-sublattice index, but neither a homotopy decomposition of \(X\) nor an integral equivariant module structure for its projective automorphism group. Unindexed or inaccessible related literature might give an equivalent computation; no independent scientific audit has been performed.

## References

- N. Ranade, C. Sadanand, D. Sullivan, *Structure on the Top Homology and Related Algorithms*, arXiv:1203.5288 (first publicly posted 23 March 2012), https://arxiv.org/abs/1203.5288 .
- F. Ardila, F. Castillo, J. A. Samper, *The Topology of the External Activity Complex of a Matroid*, Electronic Journal of Combinatorics **23** (2016), paper P3.8, https://doi.org/10.37236/5042 .
- M. Superdock, *Simplicial complexes from finite projective planes and colored configurations*, arXiv:2110.12314, https://arxiv.org/abs/2110.12314 .
