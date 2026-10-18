# The integral \(S_n\)-module of the two-matching-avoidance complex

## Finding
For every integer \(n\ge4\), let \(X_n=\mathrm{NM}_2(n)\) be the simplicial complex on the \(\binom n2\) unordered edges of the complete graph on \([n]\), with a set of edges a face exactly when no two of those edges are disjoint. Let \(V_n=\mathbb Z^{[n]}\), with basis \(e_1,\ldots,e_n\), and let \(U_n=\ker(\epsilon:V_n\to\mathbb Z)\), where \(\epsilon(e_i)=1\). The symmetric group acts by permuting labels. There is a natural integral equivariant isomorphism
\[
\boxed{\widetilde H_2(X_n;\mathbb Z)\cong_{\mathbb Z[S_n]}\bigwedge^3 U_n.}
\]
All other reduced integral homology groups vanish. The \(\binom{n-1}{3}\) classes corresponding to
\[
(e_i-e_1)\wedge(e_j-e_1)\wedge(e_k-e_1),\qquad 2\le i<j<k\le n,
\]
form an integral basis under the isomorphism. In particular this determines the exact, not just rational, integral lattice on which the natural symmetries act.

If a permutation \(\sigma\in S_n\) has cycle lengths \(\ell_1,\ldots,\ell_s\), its rational second-homology character is
\[
\boxed{\chi_n(\sigma)=[t^3]\frac{\prod_{a=1}^s(1-(-t)^{\ell_a})}{1+t}.}
\]
Over \(\mathbb Q\) this is the irreducible hook Specht representation of partition \((n-3,1,1,1)\); in particular the quotient \(|X_n|/S_n\) has no positive-degree rational homology. No irreducibility assertion is made over \(\mathbb Z\).

## Assumptions and scope
Here \(\mathrm{NM}_2(n)\) is the *nonmatching* (bounded-matching-number) complex of edge subsets, **not** the ordinary matching complex. A simplex is an edge family with matching number at most one. Homology is ordinary singular or simplicial homology with integer coefficients; \(\widetilde H_2\) is the unique positive-degree group. The action on chains includes simplicial orientation signs. The result holds for every \(n\ge4\), with no generic-position or field assumption; it does not determine the representations in the higher-bounded-matching cases \(\mathrm{NM}_k(n)\) for \(k\ge3\).

## Proof
**1. Two kinds of facets.** Any pairwise-intersecting family of edges of a simple complete graph is either a star (all edges incident to one graph vertex) or the three edges of a triangle. Indeed, if edges \(\{i,j\}\) and \(\{i,k\}\) belong to the family and another edge avoids \(i\), then the other edge must be \(\{j,k\}\), and no fourth distinct edge can intersect all three. Consequently \(X_n=B_n\cup\bigcup_{i<j<k}T_{ijk}\), where \(B_n\) is the union of the \(n\) simplex-stars \(A_i\) indexed by common endpoint \(i\), and \(T_{ijk}\) is the additional two-simplex on \(\{ij,jk,ik\}\). Every boundary edge of \(T_{ijk}\) lies in \(B_n\); two different such two-simplices meet only inside \(B_n\). Thus the relative cellular complex \((X_n,B_n)\) has only one nonzero chain group, in dimension two, and
\[
H_2(X_n,B_n;\mathbb Z)\cong \bigwedge^3V_n,
\]
by orienting \(T_{ijk}\) as \([ij,jk,ik]\) and identifying it with \(e_i\wedge e_j\wedge e_k\). This identification is \(S_n\)-equivariant because permutations of the three original vertex labels and of the three opposite edge-vertices have the same sign.

**2. The star core is a subdivided complete graph.** Let \(b_i\) be the barycenter of the simplex \(A_i\). In \(B_n\), join \(b_i\) to every singleton vertex \(ij\) in that star. The resulting \(S_n\)-invariant graph \(E_n\) is the barycentric subdivision of the complete graph on \([n]\): the path \(b_i-ij-b_j\) is its edge \(ij\). Each simplex \(A_i\) intersects \(E_n\) in the contractible tree formed by its barycenter arms. Attaching the contractible simplex along this contractible tree is a homotopy equivalence of CW pairs. Attaching all \(A_i\) in this way shows \(E_n\hookrightarrow B_n\) induces integral homology isomorphisms, naturally with respect to every label permutation. Hence
\[
H_1(B_n;\mathbb Z)\cong H_1(K_n;\mathbb Z),\quad H_2(B_n;\mathbb Z)=0,
\]
and \(B_n\) is connected. The integral graph cycle lattice of \(K_n\) is canonically \(\bigwedge^2 U_n\): use \(\bigwedge^2V_n\) as the oriented-edge group, with incidence differential \(\partial(e_i\wedge e_j)=e_j-e_i\). Its kernel is exactly \(\bigwedge^2U_n\), because \(V_n=\mathbb Ze_1\oplus U_n\) and \(\partial(e_1\wedge u)=u\).

**3. The exact connecting map and its integral kernel.** In the pair long exact sequence, the connecting homomorphism \(H_2(X_n,B_n;\mathbb Z)\to H_1(B_n;\mathbb Z)\) sends the oriented triangle \([ij,jk,ik]\) to the oriented graph cycle \(ij+jk-ik\). Under the identifications above this map is the augmentation contraction
\[
\iota_\epsilon:\bigwedge^3V_n\longrightarrow\bigwedge^2U_n,
\]
\[
\iota_\epsilon(a\wedge b\wedge c)=\epsilon(a)b\wedge c-\epsilon(b)a\wedge c+\epsilon(c)a\wedge b.
\]
For instance \(\iota_\epsilon(e_i\wedge e_j\wedge e_k)=e_j\wedge e_k-e_i\wedge e_k+e_i\wedge e_j\). The map is **integrally surjective**: for \(u,v\in U_n\), \(\iota_\epsilon(e_1\wedge u\wedge v)=u\wedge v\). The integral decomposition
\[
\bigwedge^3V_n=(e_1\wedge\bigwedge^2U_n)\oplus\bigwedge^3U_n
\]
therefore identifies its kernel, *without torsion or index loss*, with \(\bigwedge^3U_n\). As \(H_2(B_n)=0\), the long exact sequence embeds \(H_2(X_n)\) as exactly this kernel, and surjectivity gives \(H_1(X_n)=0\). All relative groups above degree two vanish and \(B_n\) has no higher homology, proving the claimed concentration. The construction and contraction commute with every label permutation; using \(e_1\) only to exhibit a splitting does not spoil equivariance of the kernel.

The integral basis follows by taking \(e_2-e_1,\ldots,e_n-e_1\) as a basis of \(U_n\). At the level of relative oriented triangles, a generator expands into the alternating four-face combination supported on the four labels \(\{1,i,j,k\}\). Exactness proves each has a unique associated absolute second-homology class; the required filling of its boundary in \(B_n\) exists since its homology boundary vanishes. No chosen filling is needed to define the canonical relative-coordinate identification.

**4. Character and quotient.** The permutation module \(V_n\otimes\mathbb Q\) decomposes as the trivial line plus the standard representation \(U_n\otimes\mathbb Q\). For an \(\ell\)-cycle, the characteristic generating polynomial \(\det(1+t\sigma\mid V_n)\) equals \(1-(-t)^\ell\). Dividing by \(1+t\) and taking the degree-three coefficient gives the displayed character. The standard hook representation identity \(\bigwedge^3U_n\otimes\mathbb Q\cong S^{(n-3,1,1,1)}\) gives the irreducible identification. It is nontrivial for \(n\ge4\), so its \(S_n\)-fixed part is zero. Over \(\mathbb Q\), homology of a finite-group quotient agrees with invariant homology, proving the quotient conclusion.

## Verification
The standalone `verify_nm2_module.py` uses only Python's standard library. For every conjugacy cycle type in \(S_n\) and every \(4\le n\le8\), it constructs the complete simplicial clique complex, computes the signed fixed-simplex Lefschetz trace, and checks it against the exterior-cube character. It independently checks every integral triangle-incidence boundary, the unimodular star-triangle surjectivity pattern, and each four-label kernel generator. Its output includes `VERIFY_OK_NONMATCHING_K2_INTEGRAL_EXTERIOR_CUBE` and `CYCLE_TYPES_CHECKED 60 RANGE_n_4_TO_8`. These tests are finite corroboration only; the all-parameter proof is the exact sequence and contraction argument.

## Relationship to prior work
Linusson, Shareshian and Welker established the nonequivariant sphere-wedge homotopy type of \(\mathrm{NM}_k(n)\), and explicitly asked in Question 1.13 for the \(S_n\)-module of its homology. The result here determines the **entire natural integral lattice** for the first nontrivial bounded-matching case \(k=2\). It does not claim the known wedge rank as new, and does not assert the general question for \(k\ge3\) is settled. Goyal, Shukla and Singh independently studied clique complexes of line graphs, including the nonequivariant complete-graph case. The published all-parameter Johnson-graph scale-one result for \(3\le k\le n-3\) deliberately excludes \(J(n,2)=L(K_n)\), and concerns nonequivariant homotopy rather than this integral \(S_n\)-module.

## Limitations
The theorem makes no statement about the equivariant *homotopy type* (as opposed to the explicitly determined integral homology module), about general \(k\ge3\), or about torsion in other graph families. The classical statements inspected do not imply the module from Betti ranks alone. An equivalent representation calculation in additional unindexed literature or an alternative published chain model remains a bibliographic risk; priority has not been independently certified.

## References
1. S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first publicly posted 2004-10-15; J. Algebraic Combin. **27** (2008), 331–349, Theorem 1.1 and Question 1.13.
2. S. Goyal, S. Shukla, A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first posted 2020-09-25, Introduction and Section 3.
3. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, publicly available result `c10287ed1518`, 2026-10-11; theorem explicitly restricts to \(3\le k\le n-3\).
