# An integral lattice obstruction behind the six-point exceptional symmetry

## Finding

Let \(X\) be a six-element set and let \(K\) be the simplicial complex whose vertices are the fifteen perfect matchings (one-factors) of the complete graph on \(X\). A collection of one-factors is a face precisely when its members are pairwise edge-disjoint. Write \(T\) for the six complete one-factorizations (sets of five one-factors partitioning all fifteen edges). The original-label permutation group \(S_X\) acts on \(T\) through the exceptional outer six-point action.

For any six-element set \(U\), write \(W_U=\ker(\epsilon:\mathbb Z^{U}\to\mathbb Z)\), with \(\epsilon\) summing coordinates. With the natural \(S_X\)-actions, the **integral equivariant identification** is

\[
\widetilde H_2(K;\mathbb Z)\cong \bigwedge{}^3 W_T\cong\mathbb Z^{10},\qquad
\widetilde H_i(K;\mathbb Z)=0\ (i\ne2).
\]

Over the rationals this representation is \(S^{(4,1,1)}\), hence is also isomorphic to \(\bigwedge^2(W_X\otimes\mathbb Q)\). The corresponding two *integral* lattices are **not isomorphic**. For a transposition \(\tau\in S_X\),

\[
\operatorname{rank}_{\mathbb F_2}\!\bigl((\tau-I)\mid \bigwedge^3(W_T\otimes\mathbb F_2)\bigr)=4,
\qquad
\operatorname{rank}_{\mathbb F_2}\!\bigl((\tau-I)\mid \bigwedge^2(W_X\otimes\mathbb F_2)\bigr)=3.
\]

The distinction is integral: it cannot be seen from the rational homology character or the underlying Betti number.

## Assumptions and scope

All simplicial chain complexes and homology groups use ordinary integral coefficients unless a field is specified. A one-factor is a partition of the original six vertices into three unordered pairs. A one-factorization is a set of five one-factors partitioning all fifteen original graph edges. The action is relabeling of the **original** six vertices, not arbitrary relabeling of the six factorizations. Exterior powers use the natural integral augmentation lattices; their reductions modulo two are reductions of these lattices, not exterior powers of arbitrary rational models. The theorem concerns this six-point complex and makes no assertion about larger even orders.

## Proof

**1. A canonical exceptional correspondence.** Elementary enumeration of partitions of six points gives fifteen one-factors and six one-factorizations. Each one-factor occurs in exactly two of the six factorizations, so it determines their unordered pair. Each pair of factorizations shares one one-factor. These assignments are mutually inverse and are equivariant for the original \(S_X\)-action. One-factorizations are called *synthematic totals* in classical terminology. A transposition of original labels exchanges three disjoint pairs of these six totals; thus the faithful degree-six permutation action on \(T\) is outer, not conjugate to the action on \(X\). Every one of these finite incidence assertions can be checked by direct generation as in the accompanying verifier.

**2. The topology and its integral action.** Regard one-factors as edges of the complete graph on vertex set \(T\). Two original one-factors are disjoint exactly when their corresponding edges of the new complete graph intersect. It follows that \(K\cong\operatorname{Cl}(L(K_T))\), equivariantly, where \(L\) is the line graph and \(\operatorname{Cl}\) is the flag-clique complex.

For \(t\in T\), let \(S_t\subseteq K\) be the full simplex on the five edges of \(K_T\) incident to \(t\), and set \(A=\bigcup_{t\in T}S_t\). For distinct \(t,u\), the intersection \(S_t\cap S_u\) is the single vertex corresponding to \(\{t,u\}\); triple intersections are empty. The cover's nerve is the ordinary graph \(K_T\). The canonical barycentric nerve construction yields an equivariant integral homology identification

\[
H_1(A;\mathbb Z)\cong H_1(K_T;\mathbb Z),\qquad H_j(A;\mathbb Z)=0\quad(j>1).
\]

Every clique of at least four edges of a complete graph has a common endpoint, hence lies in \(A\). Precisely twenty triangles remain, one for each three-element subset \(\{t,u,v\}\subseteq T\), represented by the three edges \(tu,tv,uv\) of \(K_T\). Thus the only nonzero relative chain group \(C_j(K,A;\mathbb Z)\) is

\[
C_2(K,A;\mathbb Z)\cong\mathbb Z^{\binom{T}{3}}\cong\bigwedge{}^3\mathbb Z^T.
\]

Orienting each of these triangles compatibly with its three vertices in \(T\), the connecting map of the long exact sequence for \((K,A)\) sends \(t\wedge u\wedge v\) to the triangular one-cycle \(uv-tv+tu\) in \(K_T\), with the usual coherent ordering. This can be seen by tracing the three boundary edges through the star cover; orientations may be chosen so that the map is exactly the simplicial boundary on three-element subsets. The construction is \(S_X\)-equivariant. Such triangles generate the integral cycle space of the complete graph, so this map is surjective. The long exact sequence gives

\[
\widetilde H_2(K;\mathbb Z)\cong
\ker\bigl(\partial:\bigwedge{}^3\mathbb Z^T\longrightarrow H_1(K_T;\mathbb Z)\bigr),
\qquad\widetilde H_1(K;\mathbb Z)=0.
\]

Here \(\partial\) is contraction by the augmentation \(\epsilon:\mathbb Z^T\to\mathbb Z\) (followed by inclusion of cycles into edge chains). As the sequence \(0\to W_T\to\mathbb Z^T\overset{\epsilon}{\to}\mathbb Z\to0\) splits over \(\mathbb Z\), its exterior powers show

\[
\ker\bigl(\iota_\epsilon:\bigwedge{}^3\mathbb Z^T\to\bigwedge{}^2\mathbb Z^T\bigr)=\bigwedge{}^3W_T
\]

**integrally**. This isomorphism is equivariant because all maps are natural, even though the chosen splitting need not be equivariant. The group is free of rank \(\binom53=10\). There is no remaining relative homology in other positive degrees, and \(K\) is connected. Hence all other reduced integral homology vanishes, with no torsion.

**3. Rational equality and integral inequality.** Every \(g\in S_X\) acts as a permutation on the six-element set \(T\). Exterior characters of the associated five-dimensional augmentation action, computed using

\[
\sum_{j\ge0}\operatorname{tr}(g\mid\bigwedge^jW_U)t^j
=\frac{\prod_{c\text{ a cycle of }g\text{ on }U}(1-(-t)^{|c|})}{1+t},
\]

show that the character of \(\bigwedge^3(W_T\otimes\mathbb Q)\) equals that of \(\bigwedge^2(W_X\otimes\mathbb Q)\) on all eleven cycle types in \(S_X\). The latter is the irreducible hook Specht character \(S^{(4,1,1)}\), giving the rational identification.

For an original transposition \(\tau\), its induced permutation of \(T\) is three disjoint transpositions. Reducing the five-dimensional augmentation actions modulo two gives Jordan types \(J_2\oplus J_2\oplus J_1\) on \(W_T\otimes\mathbb F_2\) and \(J_2\oplus J_1^{\oplus3}\) on \(W_X\otimes\mathbb F_2\). Computing the two exterior-power actions gives ranks \(4\) and \(3\), respectively, for \(\tau-I\). Such ranks are invariant under integral equivariant isomorphism; therefore the two integral lattices cannot be isomorphic. The finite-checker computes these ranks directly from ten-by-ten exterior minor matrices over \(\mathbb F_2\), without requiring the Jordan-form argument.

## Verification

The accompanying standalone Python 3 program `check.py` enumerates the fifteen one-factors and six factorizations, proves every claimed incidence equality by exhaustive inspection, enumerates all faces with face vector \((15,60,80,30,6)\), and verifies the decomposition into 171 star-covered nonempty faces and twenty exterior triangles. It checks reduced boundary ranks over the three primes \(2,3,101\); their common positive-dimensional ranks are \((14,46,24,6)\), leaving ten independent degree-two classes. These field computations corroborate **but do not replace** the preceding integral argument.

It separately checks that each of the 720 original-label permutations gives the requisite signed action, compares all 720 Lefschetz traces with the two exterior-character formulas, and verifies the triangle-orientation compatibility. Finally it builds the integral augmentation matrices, reduces exterior minors modulo two and computes the claimed invariant ranks of four and three. The packaged `verification-output.json` is a reproducible output record, not a substitute for the proof.

## Relationship to prior work

The classical six-factorization construction and its exceptional symmetric-group action are long known; the explicit combinatorics is not claimed as novel. Linusson–Shareshian–Welker (2004) established homotopy information for complexes of graphs avoiding matchings; under the present identification their results overlap the nonequivariant topology. Goyal–Shukla–Singh (2020) proved the general nonequivariant homotopy reduction \(\operatorname{Cl}(L(G))\simeq\operatorname{sk}_2\operatorname{Cl}(G)\). Its canonical construction is relevant to, and broadly motivates, the integral equivariant description above.

The new, more specific arithmetic assertion is the obstruction to identifying two natural **integral** lattices that have the same irreducible rational character under the exceptional degree-six action. A general rational character formula or a nonequivariant sphere count does not determine that obstruction. The distinction is proved by a mod-two invariant rather than inferred from an absence of published notation.

## Limitations

The result is confined to six original labels and the specified simplicial complex. It does not classify all integral lattices in the rational representation, and it does not calculate minimal determinant indices of all equivariant intertwiners. The proof of nonisomorphism does not assert that any abstract non-equivariant homology groups differ. A naturality argument building on the published line-graph result supplies part of the structural mechanism; equivalent unindexed expositions of the specific integral discrepancy cannot be excluded. Independent validation has not been performed.

## References

1. S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, first public preprint 15 October 2004, https://arxiv.org/abs/math/0410345.
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, first public preprint 25 September 2020, https://arxiv.org/abs/2009.12130 (especially Lemma 3.2 and its proof).
3. J. Baez, *Some Thoughts on the Number 6*, 2 September 2015, https://math.ucr.edu/home/baez/six.html (synthemes, totals, outer permutation action).
4. A. Nikseresht, *Algebraic Properties of Clique Complexes of Line Graphs*, https://arxiv.org/abs/2007.13082 (related algebraic properties).
5. Q. Wang and W. Li, *Integral homology lattices of matching and circulant complexes*, 15 October 2026, https://arxiv.org/abs/2610.22082 (different matching-complex objects; useful methodological comparison).
