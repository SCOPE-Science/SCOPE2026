# Complete natural symmetry character of balanced Johnson clique complexes

## Finding

For every integer \(k\ge4\), let \(J(2k,k)\) be the graph on the \(k\)-element subsets of \([2k]\), two vertices being adjacent when their intersection has size \(k-1\). Let \(X_k\) be its flag complex (equivalently, the inclusive scale-one graph-metric Vietoris–Rips complex). Coordinate permutations \(g\in S_{2k}\) act on \(X_k\). The complementation involution \(c:A\mapsto[2k]\setminus A\) commutes with these permutations; together they act as \(S_{2k}\times C_2\).

The reduced integral homology is free and concentrated in degree two:
\[
\widetilde H_i(X_k;\mathbb Z)=0\quad(i\ne2),\qquad
\operatorname{rank}\widetilde H_2(X_k;\mathbb Z)=B_k,
\]
where
\[
B_k=2\binom{2k}{k-1}+(1-2k)\binom{2k}{k}
+\binom{2k}{2}\binom{2k-2}{k-1}-1.
\]

The **complete rational character** of the natural \(S_{2k}\times C_2\)-representation on \(\widetilde H_2(X_k;\mathbb Q)\) has the following exact cycle-index formulas. For \(g\in S_{2k}\), let \(c_j=c_j(g)\) count its cycles of length \(j\), let
\[
P_g(z)=\prod_{j\ge1}(1+z^j)^{c_j},\qquad F_r(g)=[z^r]P_g(z).
\]
Let \(F_r^{11}(g)\) be the same coefficient after removing two fixed-point cycles if \(c_1\ge2\), otherwise zero; let \(F_r^{2}(g)\) be the coefficient after removing one two-cycle if \(c_2\ge1\), otherwise zero. Then
\[
\boxed{\chi_k(g)=F_{k-1}+F_{k+1}+(1-c_1)F_k
+\binom{c_1}{2}F_{k-1}^{11}-c_2F_{k-1}^{2}-1.}
\]
For the elements involving complementation, put \(e=\sum_{j\text{ even}}c_j\). The other half of the character is
\[
\boxed{\chi_k(gc)=
\begin{cases}
2^{e-1}(2-c_2)-1,&c_j=0\text{ for all odd }j,\\
2^e-1,&c_1=2\text{ and }c_j=0\text{ for odd }j\ge3,\\
-1,&\text{otherwise}.
\end{cases}}
\]
The first case automatically has \(e\ge1\). In particular \(\chi_k(c)=-1\) for every \(k\ge4\). Thus complementation has eigenspace dimensions \((B_k-1)/2\) and \((B_k+1)/2\) for eigenvalues \(+1\) and \(-1\), respectively. For \(k=4\), \(B_4=181\), and these dimensions are \(90\) and \(91\).

The formulas specify every rational irreducible multiplicity uniquely by character inner products. No claim is made of a canonical irreducible integral splitting.

## Assumptions and scope

All graphs are finite and simple; adjacency means one-element exchange. For a permutation \(g\), its action on an oriented simplex is the sign of the induced vertex permutation if the simplex is setwise fixed and zero otherwise. Homology is reduced simplicial homology, and its trace formula uses the reduced augmented chain complex, whose degree-minus-one trace is one. The theorem concerns the balanced weight layer \(k\) of the Boolean cube and exactly the scale at which two weight-\(k\) words with Hamming distance two become adjacent. It does not assert an extension to any other scale or to all weight layers. The restriction \(k\ge4\) excludes the previously described weight-three representation.

## Proof

**1. Facets and degree concentration.** Every maximal clique of \(J(2k,k)\) is either a star
\(A_S=\{S\cup\{x\}:x\notin S\}\), indexed by a \((k-1)\)-subset \(S\), or a top \(T_U=\{U\setminus\{x\}:x\in U\}\), indexed by a \((k+1)\)-subset \(U\). This follows by examining any adjacent pair: a third vertex must extend their intersection or lie inside their union, and the two types cannot mix. Two distinct stars meet in at most one vertex; two distinct tops do likewise; and a star and top meet in at most one edge. Thus every simplex with at least three vertices belongs to a **unique** maximal clique.

Independently for each maximal clique \(F\), pick an apex \(a\in F\) and pair every simplex \(\tau\subset F\setminus\{a\}\) of at least three vertices with \(\tau\cup\{a\}\), processing \(\tau\)'s in decreasing cardinality. Uniqueness of the supporting maximal clique makes every pair a legitimate free-face collapse. The resulting complex has dimension at most two and the same homotopy type as \(X_k\). Hence \(H_i(X_k;\mathbb Z)=0\) for \(i\ge3\).

The hypersimplex \(\Delta(2k,k)=\{x\in[0,1]^{2k}:\sum x_i=k\}\) has one-skeleton \(J(2k,k)\). Every two-dimensional face of this convex polytope is a triangle: at a two-face, precisely three coordinates vary, summing to either one or two. Such triangles are cliques of \(J(2k,k)\), so the cellular two-skeleton of the hypersimplex is a subcomplex of \(X_k\) containing the entire one-skeleton. Since the hypersimplex has dimension \(2k-1\ge7\) and its boundary is a sphere, its cellular two-skeleton is simply connected. Every simplicial edge loop in \(X_k\) is therefore null-homotopic inside that two-skeleton; consequently \(X_k\) is simply connected. The collapsed two-dimensional CW complex has \(H_2\) a subgroup of a free abelian two-chain group, hence free, with all other reduced homology zero.

**2. Signed Euler character for coordinate permutations.** Fix \(g\in S_{2k}\). A subset of \([2k]\) is \(g\)-invariant exactly when it is a union of cycles of \(g\), so the number of fixed \(r\)-subsets is \(F_r\). Write \(E_g\) for the signed trace of \(g\) on the oriented one-chain group of \(X_k\). An edge is uniquely the pair of vertices \(\{S\cup\{x\},S\cup\{y\}\}\) for a \((k-1)\)-subset \(S\). Its setwise invariance requires \(gS=S\), with \(x,y\) either individually fixed or transposed. Therefore
\[
E_g=\binom{c_1}{2}F_{k-1}^{11}-c_2F_{k-1}^{2}.
\]
For each fixed star or top \(F\), the signed alternating contribution of all its faces of dimensions at least two is \(1-V_F+E_F\): this is the reduced Euler identity for the simplex \(F\), with \(V_F\) the number of fixed vertices and \(E_F\) the signed trace on its edges. All high-dimensional faces have unique supporting maximal cliques, and the two collections of their edge traces each sum to \(E_g\). The total fixed-vertex count across all invariant stars and tops equals \(c_1F_k\), because it counts exactly the pairs \((x,A)\) in which \(x\) is a fixed ground point and \(A\) is a fixed \(k\)-subset: if \(x\in A\) this comes from the star \(A\setminus\{x\}\), otherwise from the top \(A\cup\{x\}\). Therefore the total reduced alternating chain trace is
\[
F_k-E_g+F_{k-1}+F_{k+1}-c_1F_k+2E_g-1.
\]
Because reduced rational homology is concentrated in even degree two, this is precisely \(\chi_k(g)\), proving the first boxed expression. Evaluation at the identity yields the rank formula \(B_k\).

**3. Fixed vertices and edges for twisted complementation.** Put \(h=gc\). Complementation exchanges star and top facets. Since a simplex with three or more vertices has a unique facet type, no such simplex is setwise fixed by \(h\). Therefore its reduced alternating trace is simply
\[\chi_k(h)=V_h-E_h-1.\]

A vertex \(A\) is fixed by \(h\) exactly when \(g(A^c)=A\). On each cycle of \(g\), membership in \(A\) must alternate. This is possible precisely when every cycle is even, in which case there are two choices per cycle and \(V_h=2^e\).

For an invariant edge described by \(S\) of size \(k-1\) and a two-element remainder \(R=\{a,b\}\), its associated top is \(S\cup R\). The complement map exchanges the star and top data. The edge is setwise fixed by \(gc\) if and only if
\[
g^2S=S,\qquad S\cap gS=\varnothing,\qquad R=[2k]\setminus(S\cup gS).
\]
The induced action on its two vertices has orientation sign opposite to the sign of \(g\) on \(R\). Indeed \(gc(S\cup\{a\})=(S\cup R)\setminus\{g(a)\}\); if \(g\) fixes both points in \(R\), it exchanges the edge's endpoints, while if \(g\) transposes them, it fixes the endpoints.

The conditions on \(S\) force it to be a union of parity halves of even cycles of \(g\), using neither point of any odd cycle. Its cardinality \(k-1\) means that the odd-cycle lengths plus the lengths of the even cycles omitted entirely add to **exactly two**. Hence there are only two possibilities. If all cycles are even, exactly one two-cycle is omitted and the edge trace is \(E_h=c_2 2^{e-1}\). If there are exactly two fixed points and all other cycles are even, both fixed points form \(R\), and \(E_h=-2^e\). In all other cycle types \(E_h=0\). Inserting these alternatives and the count of fixed vertices into \(V_h-E_h-1\) proves the second boxed formula.

**4. The eigenspaces.** The pure complement corresponds to \(g=1\); it has no fixed vertices or edges and has trace \(-1\). Since \(c^2=1\), rational homology splits into \(\pm1\)-eigenspaces. Their dimensions sum to \(B_k\) and differ by \(-1\), giving \((B_k-1)/2\) and \((B_k+1)/2\).

## Verification

The standalone file `verify_balanced_johnson.py` uses only Python 3's standard library. It constructs the Johnson graph and every face from the two independently defined star and top families, evaluates the signed augmented chain Lefschetz number from actual invariant faces, and compares it with the two closed cycle formulas. It checks all 22 partition classes of \(S_8\) for both the ordinary and complemented actions and eight representative classes of \(S_{10}\) for both actions. The exact run reported `VERIFY_OK cases=60 signed_face_tests=443240`. A separate bit-vector Gaussian elimination of every boundary matrix for \(X_4\) gave reduced mod-two Betti vector \((0,0,181,0,0)\). These are finite consistency checks; the four proof steps establish the infinite statement.

## Relationship to prior work

The published 2026 Johnson-graph scale-one sphere-wedge result computes nonequivariant homotopy and homology ranks but does not specify any nonidentity automorphism trace. The 2026 constant-weight-three representation theorem computes the \(S_n\)-character only when the layer weight is three, and does not cover the balanced layers \(k\ge4\) or their extra complement involution. Galetto–Montaño–Wellner study representation actions for the *entire* Boolean cube's Vietoris–Rips complexes; a representation of the full cube does not determine the representation on its induced balanced weight layer. Shuldiner–Oldford classify maximal Johnson cliques without calculating their resulting equivariant homology. The new contribution is the complete two-coset character of the balanced middle layer, including the exact parity/orbit classification of twisted complementations.

## Limitations

Only balanced weight layers with \(k\ge4\) at graph-Rips scale one are covered. The formulas determine rational representations, not their integral module decomposition. They do not imply a persistence classification. The 2026 full-cube representation preprint was available for scope comparison through its public abstract and descriptions but not for full-text inspection; unindexed or inaccessible equivalent work remains an originality risk. The finite verifier does not prove the universal quantifier or establish independent scientific validation.

## References

1. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first posted 2026-06-18).
2. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710v1 (2022).
3. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, published research record (2026-10-11), published-finding corpus record `c10287ed1518`.
4. *Symmetric-group homology character of constant-weight-three Hamming Rips complexes*, published research record (2026-10-11), published-finding corpus record `11db16b6cb70`.
