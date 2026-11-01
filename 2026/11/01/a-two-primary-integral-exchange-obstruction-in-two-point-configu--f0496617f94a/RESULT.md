# A two-primary integral exchange obstruction in two-point configurations on metric stars

## Finding
Let \(k\ge 3\), let \(S_k\) be a metric star with \(k\) equal arms of length \(L>0\), and let
\[
F_r(S_k)=\{(x,y)\in S_k\times S_k:d(x,y)\ge r\},\qquad 0<r\le L.
\]
The group of arm permutations acts on this ordered two-particle configuration space, and \(\tau(x,y)=(y,x)\) is the commuting exchange involution. Write \(H=H_1(F_r(S_k);\mathbb Z)\), and write \(H^+\) and \(H^-\) for the integral fixed and anti-fixed sublattices under \(\tau\).

**Theorem (integral exchange gluing).** There is a canonical exact sequence of \(\mathbb Z[S_k\times C_2]\)-modules
\[
0\longrightarrow H^+\oplus H^-
\longrightarrow H
\xrightarrow{\ p\ }
\mathcal E_k\longrightarrow0,
\]
where \(\mathcal E_k\) is the vector space over \(\mathbb F_2\) of even-cardinality Eulerian edge sets of the complete graph \(K_k\). Arm permutations act by relabeling the edge sets; the exchange involution acts trivially on this quotient. In particular,
\[
\mathcal E_k\cong(\mathbb Z/2\mathbb Z)^{k(k-3)/2},
\qquad
[H:H^+\oplus H^-]=2^{k(k-3)/2}.
\]
Thus the exchange eigensublattices span the integral first homology if and only if \(k=3\); for each \(k\ge4\) they **do not** span it, although they span after extension of scalars to \(\mathbb Q\). The obstruction is the complete even-Eulerian cycle space, not just an unspecified finite group.

More explicitly, with \(A_k=\ker(\mathbb Z^k\xrightarrow{\sum}\mathbb Z)\), there are natural integral arm-permutation isomorphisms
\[
H^+\cong\bigwedge^2 A_k,\qquad
H^-\cong\ker\!\left(\mathbb Z^{\binom{k}{2}}\xrightarrow{\ u\ }\mathbb Z^k\right),
\quad u(\{i,j\})=e_i+e_j.
\]
Their ranks are \(\binom{k-1}{2}\) and \(k(k-3)/2\), respectively, while \(H\) has rank \(k^2-3k+1\). The integral extension and its index are constant throughout \(0<r\le L\). For \(r>L\), \(H_1(F_r(S_k);\mathbb Z)=0\): the space is a disjoint union of \(k(k-1)\) contractible components when \(L<r\le2L\), and is empty when \(r>2L\).

## Assumptions and scope
Each arm is the interval \([0,L]\) with all zero endpoints identified as the hub, and distances are shortest-path distances. The two particles are **labeled**; \(r>0\) forbids collision. All homology is singular homology over \(\mathbb Z\), with natural actions induced by continuous arm permutations and label exchange. On \(\mathcal E_k\), an Eulerian set means every vertex of \(K_k\) has even degree, and *even-cardinality* additionally means the total number of edges is even. Its elements are added by symmetric difference. These two requirements are distinct: a triangle is Eulerian but has odd cardinality.

## Proof
**1. A symmetry-natural graph model.** Label the arms by \(1,\ldots,k\). For distinct arms \(i\ne j\), the configurations with first coordinate on arm \(i\) at radius \(s\) and second on arm \(j\) at radius \(t\) form the convex polygon
\[
D_{ij}=\{(s,t)\in[0,L]^2:s+t\ge r\}.
\]
For particles on the same arm \(i\), the two regions \(s-t\ge r\) and \(t-s\ge r\) are contractible triangles, each meeting the other-arm union only in the hub-axis segment \(t=0\) or \(s=0\), respectively. Collapse the triangle \(s-t\ge r\) by \((s,t)\mapsto(s,(1-\theta)t)\), and use the coordinate-exchanged formula on its mate. These maps fix their attaching intervals, preserve the separation inequality, and commute with relabelings and particle exchange. Thus this is an equivariant deformation retraction onto \(D=\bigcup_{i\ne j}D_{ij}\).

For \(0<r\le L\), all \(D_{ij}\) are nonempty and convex. Distinct polygons intersect precisely when their first arm labels agree, along the common nonempty segment with second point at the hub, or when their second labels agree, along the analogous first-point-at-hub segment. The two sorts of shared segments cannot meet because \((0,0)\) violates \(r>0\). Every nonempty multiple intersection is likewise a contractible segment (possibly a point at \(r=L\)). The cellular Cech/Mayer--Vietoris double complex for this finite polyhedral cover has no positive-degree homology in intersections; its zeroth-intersection row is the simplicial nerve, canonically and equivariantly, because the cover is permuted by \(S_k\times C_2\). Consequently \(H_1(D;\mathbb Z)\) is the integral first homology of that nerve, with the same group action.

The nerve is the union of a row simplex on \(\{D_{ij}:j\ne i\}\) for each \(i\), and a column simplex on \(\{D_{ij}:i\ne j\}\) for each \(j\). Two distinct row simplices never meet, and neither do two distinct column simplices; row \(i\) meets column \(j\) in the single vertex \(D_{ij}\) when \(i\ne j\). Applying the same natural intersection-complex argument to the row/column simplex cover identifies its first integral homology, equivariantly, with that of the **crown graph** \(B_k=K_{k,k}\setminus\{U_iV_i:1\le i\le k\}\). This two-stage Cech argument does not require choosing a symmetry-breaking homotopy retraction.

**2. The exact integral cycle lattice.** Orient every edge of \(B_k\) from \(U_i\) to \(V_j\), for \(i\ne j\). The first integral homology of this connected graph is exactly
\[
Z_k=\left\{C=(c_{ij})\in\mathbb Z^{k\times k}:
 c_{ii}=0,\ \sum_jc_{ij}=0,\ \sum_ic_{ij}=0\ \text{for all }i,j\right\}.
\]
There are \(k(k-1)\) edges and \(2k\) vertices, and \(B_k\) is connected for \(k\ge3\), so its cycle lattice has rank \(k(k-1)-2k+1=k^2-3k+1\). The swap \(\tau\) interchanges the two vertex parts and reverses the chosen orientations, hence acts by \(C\mapsto-C^{\mathsf T}\). Simultaneous arm permutation relabels rows and columns.

**3. Integral eigenlattices.** The \(+1\)-fixed cycles are precisely the skew-symmetric matrices \(C=-C^{\mathsf T}\) with vanishing row sums. The canonical exterior embedding \(\bigwedge^2 A_k\hookrightarrow\bigwedge^2\mathbb Z^k\) identifies these with \(\bigwedge^2 A_k\): indeed the primitive augmentation summand decomposition \(\mathbb Z^k=A_k\oplus\mathbb Z e_k\) makes the contraction against the sum functional surjective, with kernel exactly \(\bigwedge^2 A_k\). The \(-1\)-eigenlattice consists of symmetric matrices \(C=C^{\mathsf T}\) with zero diagonal and row sums, namely the kernel of the unsigned incidence map \(u\) displayed in the theorem. The underlying complete graph contains a triangle, so \(u\) has rank \(k\) over \(\mathbb Q\), proving both claimed eigenspace ranks.

**4. The parity obstruction.** Define a natural \(S_k\times C_2\)-equivariant map
\[
p:Z_k\longrightarrow \mathbb F_2^{E(K_k)},\qquad
p(C)_{\{i,j\}}=c_{ij}+c_{ji}\pmod2.
\]
Every vertex of \(p(C)\) has even degree because both the corresponding row and column sums vanish. The total edge count of \(p(C)\) is even because \(\sum_{i\ne j}c_{ij}=0\). Thus \(p(C)\in\mathcal E_k\). In characteristic two, transpose together with a sign has the same effect on \(p\), so \(\tau\) acts trivially on the image.

If \(p(C)=0\), then each \(c_{ij}\) has the same parity as \(c_{ji}\), so
\[
C_+=(C-C^{\mathsf T})/2,\qquad C_-=(C+C^{\mathsf T})/2
\]
are both integer matrices. They belong to \(Z_k\), satisfy \(\tau C_+=C_+\) and \(\tau C_-=-C_-\), and sum to \(C\). Conversely any sum of an integral skew and integral symmetric cycle has vanishing \(p\). Therefore \(\ker p=Z_k^+\oplus Z_k^-\).

For any four distinct labels \(i,j,a,b\), the integer cycle with entries
\[
c_{ia}=1,\quad c_{ib}=-1,\quad c_{ja}=-1,\quad c_{jb}=1
\]
and all other entries zero lies in \(Z_k\), and its parity image is the four-cycle with edges \(\{i,a\},\{i,b\},\{j,a\},\{j,b\}\). The even-cardinality Eulerian subspace of \(K_k\) is spanned by its four-cycles: all Eulerian edge sets are sums of triangles, any even-cardinality one uses an even number of triangles, and the difference (modulo two) of any two triangles sharing an edge is a four-cycle. The graph whose vertices are triangles and edges join triangles sharing an edge is connected for \(k\ge4\), allowing any even sum of triangles to be expressed as a sum of four-cycles. For \(k=3\), the even-cardinality Eulerian subspace is zero. Thus \(p\) is surjective for every \(k\ge3\).

Finally, the binary Eulerian cycle space has dimension \(\binom{k}{2}-k+1\). Requiring even total edge count imposes one additional independent condition, since a triangle has odd edge count. Thus
\[
\dim_{\mathbb F_2}\mathcal E_k=\binom{k}{2}-k=\frac{k(k-3)}2.
\]
Exactness and the index follow; for \(k\ge4\) this dimension is positive.

**5. Thresholds.** If \(L<r\le2L\), each polygon \(D_{ij}\) remains convex and nonempty but has no hub-axis points, so the \(k(k-1)\) polygons are disjoint; there are no same-arm configurations. For \(r>2L\), no pair can achieve the separation. For \(0<r\le L\), all the nerve incidence relations above persist, and all inclusion-induced first-homology maps across these thresholds identify the same cycle lattice by naturality of the two covers. This proves the claimed persistence and complete boundary behavior.

## Verification
The standalone `check_integral_exchange.py` computes an exact oriented spanning-tree cycle basis of the crown graph over \(\mathbb Z\), verifies both row and column boundary conditions, calculates the mod-two rank of the parity quotient, and verifies that four-cycle images span it. It also checks the cell-character identities for an arm permutation and for that permutation followed by exchange, using one representative of every conjugacy type. Executing it under standard Python 3 passed all tests for \(k=3,4,5,6,7,8\). The respective quotient dimensions were \(0,2,5,9,14,20\), and the corresponding indices are \(1,4,32,512,16384,1048576\). These tests corroborate, but do not replace, the all-\(k\) proof above.

## Relationship to prior work
Li--Özaydın (2026, arXiv:2603.00914) provide the weighted-graph model for **ordered** restricted configurations and determine field-valued persistence. The crown-graph reduction and the ordinary first Betti number are not new. Ramos--Yun (2026, arXiv:2606.13813, Theorem 3.3) already determine the rational arm-permutation decomposition of the usual two-particle star configuration space, and its unordered counterpart; that rational decomposition and the corresponding exchange-eigenvalue multiplicities are **not claimed as new**. A published note on unordered separated metric-star persistence likewise supplies complete unordered barcodes, but does not give the integral ordered exchange-gluing sequence. The new assertion here is the natural **integral** quotient by the two exchange eigensublattices, its even-cycle-space structure and exact exponentially growing index, which are not implied by a rational decomposition. The earlier Li (2023) treatment is relevant background; its full text was not fully compared, so possible implicit coverage remains a residual risk.

## Limitations
The integral exchange extension applies to exactly two **labeled** particles on a metric star with identical arm lengths. It is not a classification of unequal-length equivariant persistence, three-particle configurations, other graphs, or higher homology operations. The theorem concerns homology modules, not an equivariant homotopy splitting. The rational Specht decomposition has already appeared in earlier literature and is not part of the novelty claim. Reproducibility tests are finite; the infinite assertion rests on the Cech/graph and parity arguments. Independent mathematical verification and comprehensive exclusion of all unindexed equivalent literature have not been performed.

## References
1. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1, publicly submitted 2026-03-01, https://arxiv.org/html/2603.00914, §3 and Appendix A.
2. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1, publicly submitted 2026-06-11, https://arxiv.org/abs/2606.13813, especially Theorem 3.3 (star graphs) and §3.4 (configurations on crown graphs).
3. W. Li, *Persistent Homology of Configuration Spaces of Trees*, arXiv:2310.05303v1, 2023-10-08, https://arxiv.org/abs/2310.05303.
4. *Exact persistence of two unordered separated particles on metric stars*, publicly available result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-persistence-of-two-unordered-separated-particles-on-metric--ce01bbf73bfa/RESULT.md.
