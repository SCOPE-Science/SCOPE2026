# Symmetric-group homology of two adjacent Hamming-weight Rips layers

## Finding
For integers \(m\ge5\) and \(2\le k\le m-3\), let
\[
X_{m,k}=\operatorname{VR}_{\le2}\left(\binom{[m]}k\cup\binom{[m]}{k+1},d_\triangle\right),
\qquad d_\triangle(A,B)=|A\triangle B|.
\]
The symmetric group \(S_m\) acts by permuting the ground-set labels. Write \(S^\lambda\) for the rational Specht module indexed by a partition \(\lambda\), and set
\[
a=\min(k-1,m-k-1),\qquad
b=\min(k,m-k-2),\qquad
c=\min(k,m-k-1).
\]
Then its only nonzero reduced rational homology is in dimension two, and its **complete** \(S_m\)-module structure is
\[
\boxed{\widetilde H_2(X_{m,k};\mathbb Q)\cong
\bigoplus_{j=1}^{c} S^{(m-j-1,j,1)}
\;\oplus\;
\bigoplus_{j=1}^{a} S^{(m-j-2,j,1,1)}
\;\oplus\;
\bigoplus_{j=1}^{b} S^{(m-j-2,j,1,1)}.}
\]
The two four-row sums count multiplicities separately; their overlapping constituents occur twice. All partitions displayed above are valid in the stated parameter range. The three-row summands arise from the ordinary incidence graph between the two adjacent ranks, while the four-row summands arise from their respective single-rank Rips complexes. In particular, for both \(G=S_m\) and \(G=A_m\),
\[
\widetilde H_*(|X_{m,k}|/G;\mathbb Q)=0.
\]
The quotient statement concerns rational homology only, not contractibility or integral torsion.

## Assumptions and scope
A simplex is any nonempty collection of distinct \(k\)- and \((k+1)\)-subsets of \([m]\) with every pair at symmetric-difference distance at most two. This is the inclusive Vietoris–Rips convention. Distinct same-rank vertices are adjacent exactly when they differ by exchanging one element; opposite-rank vertices are adjacent exactly for containment. The range \(m\ge5\), \(2\le k\le m-3\) makes both constituent one-rank complexes nontrivial. Every homology representation is over \(\mathbb Q\) unless indicated otherwise.

## Proof
**1. Homological concentration.** Feng and Nukala, Theorem 13, show that \(X_{m,k}\) is homotopy equivalent to a wedge of two-spheres for \(1<k<m-1\). Their Corollary 11 gives the same concentration for either one-rank complex
\(L_q=\operatorname{VR}_{\le2}(\binom{[m]}q,d_\triangle)\), \(q=k,k+1\). We use these known **nonequivariant** homotopy statements solely to localize the homology degree. No equivariant equivalence is assumed.

**2. The signed cellular Euler class for one rank.** In the representation ring of \(S_m\), let \(M_{a_1,\ldots,a_t}\) be the permutation representation on ordered partitions of \([m]\) into labeled disjoint blocks of sizes \(a_1,\ldots,a_t\). Let \(A_{u,2,v}\) be the analogous induced representation with the sign character on the middle two-element block. Each clique of at least three vertices in the Johnson graph of \(q\)-subsets is uniquely either a *star* (all vertices contain one fixed \((q-1)\)-subset) or a *top* (all are contained in one fixed \((q+1)\)-subset): starting from two adjacent vertices with common intersection \(I\) and union \(U\), every other common neighbor is either an extension of \(I\) or a member of \(U\); mixing these types cannot form a clique of three or more. A star and a top cannot share three distinct vertices.

The oriented degree-one chains form \(A_{q-1,2,m-q-1}\). For each star or top, the alternating sum of its oriented simplices of dimensions at least two equals the trivial representation on its indexing block, minus the representations on its vertices, plus that on its oriented edges (the augmented chain complex of a simplex is exact). The Euler–Poincaré identity, together with the degree-two concentration, therefore gives
\[
[\widetilde H_2(L_q)]=-[\mathbf1]+[M_{q,m-q}]+[M_{q-1,m-q+1}]
+[M_{q+1,m-q-1}]-[M_{q-1,1,m-q}]
-[M_{q,1,m-q-1}]+[A_{q-1,2,m-q-1}].
\tag{1}
\]
Here brackets indicate representation-ring classes, not an asserted natural direct-sum splitting.

Under the Frobenius characteristic map, \(M_{a_1,\ldots,a_t}\) becomes \(h_{a_1}\cdots h_{a_t}\), the sign-twisted two-block module becomes \(h_u e_2h_v\), and \(\mathbf1\) becomes \(h_m\). Put \(r=\min(q-1,m-q-1)\). The four-row Jacobi–Trudi determinant yields, with \(p=m-j-2\),
\[
s_{(p,j,1,1)}=e_2(h_ph_j-h_{p+1}h_{j-1})
-h_1(h_ph_{j+1}-h_{p+2}h_{j-1})
+h_ph_{j+2}-h_{p+3}h_{j-1}.
\tag{2}
\]
Summing (2) for \(1\le j\le r\) telescopes and equals the Frobenius characteristic of the right-hand side of (1). Thus, using semisimplicity over \(\mathbb Q\),
\[
\widetilde H_2(L_q;\mathbb Q)\cong
\bigoplus_{j=1}^{\min(q-1,m-q-1)}S^{(m-j-2,j,1,1)}.
\tag{3}
\]
This single-rank decomposition is also known in prior work; its role here is as an input and independent derivation of the two-rank calculation.

**3. The two-rank mixed-face Euler class.** Let \(B_{m,k}\) be the connected bipartite incidence graph whose vertices are all \(k\)-subsets and \((k+1)\)-subsets, with an edge for each inclusion. Every mixed simplex has either exactly one lower-rank vertex or exactly one upper-rank vertex. Indeed, two distinct lower vertices contained in two different upper vertices would force both upper vertices to equal the same \((k+1)\)-set, an impossibility. Fixing one lower vertex \(A\), all its mixed simplices with that unique lower vertex are the nonempty upper faces in the simplex on \(A\)'s \(m-k\) immediate supersets, coned off at \(A\). Their alternating signed chain sum is \(-[A]\), since the augmented chain complex of that upper simplex is exact. Summing over \(A\) gives \(-M_{k,m-k}\). The analogous sum over unique upper vertices gives \(-M_{k+1,m-k-1}\). Each mixed edge, and only a mixed edge, was counted twice; correcting its degree-one sign adds \(M_{k,1,m-k-1}\). Hence
\[
\sum_{i\ge1}(-1)^i[C_i^{\mathrm{mixed}}]
=-[M_{k,m-k}]-[M_{k+1,m-k-1}]+[M_{k,1,m-k-1}]
=[\widetilde H_1(B_{m,k})]-[\mathbf1].
\tag{4}
\]
The last equality follows from the equivariant Euler relation for the connected incidence graph. Adding the Euler classes of both single-rank complexes and (4), then subtracting the trivial \(H_0\)-representation of \(X_{m,k}\), gives
\[
[\widetilde H_2(X_{m,k})]=
[\widetilde H_2(L_k)]+[\widetilde H_2(L_{k+1})]+[\widetilde H_1(B_{m,k})].
\tag{5}
\]
This is an equality of rational representation classes; all three terms on the right are honest representations, hence it becomes an isomorphism by Maschke's theorem.

**4. The new incidence module.** The bipartite incidence graph is connected: two \(k\)-sets differing by one exchange are connected through their union, and these exchanges connect the Johnson graph. Its oriented edges, directed from the lower to the upper rank, form the *unsigned* module \(M_{k,1,m-k-1}\). The Euler identity gives
\[
\operatorname{ch}\widetilde H_1(B_{m,k})
=h_kh_1h_{m-k-1}-h_kh_{m-k}-h_{k+1}h_{m-k-1}+h_m.
\tag{6}
\]
For \(p=m-j-1\), the three-row Jacobi–Trudi determinant reads
\[
s_{(p,j,1)}=h_1(h_ph_j-h_{p+1}h_{j-1})-h_ph_{j+1}+h_{p+2}h_{j-1}.
\tag{7}
\]
Summing (7) for \(1\le j\le c=\min(k,m-k-1)\) telescopes exactly to (6), giving
\[
\widetilde H_1(B_{m,k};\mathbb Q)\cong\bigoplus_{j=1}^{c}S^{(m-j-1,j,1)}.
\tag{8}
\]
Substitution of (3) and (8) into (5) proves the asserted complete Specht decomposition.

**5. Quotients.** The displayed partitions have three or four rows, so none is either \((m)\) or \((1,\ldots,1)\). Thus the module contains neither the trivial nor the sign representation of \(S_m\). The invariant subspaces for both \(S_m\) and its index-two subgroup \(A_m\) vanish (by Frobenius reciprocity, invariants for \(A_m\) can only come from those two constituents). Finite-group rational averaging, after equivariant subdivision if needed, identifies the quotient's rational homology with invariants. This proves the quotient conclusion.

## Verification
The accompanying standalone Python 3 program `verify_two_rank.py` constructs every simplex from pairwise symmetric-difference distances without using the star/top classification. For each conjugacy class in \(S_m\), it calculates the signed fixed-simplex Lefschetz number and compares it with the proposed Specht character evaluated independently by Jacobi–Trudi and exact ordered-block cycle assignments. It checks all conjugacy classes for \((m,k)=(5,2),(6,2),(6,3),(7,3),(8,3),(8,4)\). The checker prints `TWO_RANK_BOOLEAN_EQUIVARIANT_OK`. For the central example \((m,k)=(8,3)\), there are \(126\) vertices, \(6{,}930\) nonempty faces and \(\dim\widetilde H_2=461\). These are finite checks; the all-parameter theorem follows from the proof above and the published nonequivariant concentration theorem.

## Relationship to prior work
Ziqin Feng and Naga Chandra Padmini Nukala, *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (first public 2023-02-28), Corollary 11 and Theorem 13, establish the nonequivariant wedge-of-two-spheres types for one and two consecutive ranks. The present theorem does not re-claim those sphere multiplicities: it computes the missing ground-label \(S_m\)-representation, including the new three-row incidence-graph constituents and its quotient consequences. Prior calculations of the equivariant homology of a *single* constant-weight layer do not imply the two-layer module, because the mixed faces contribute the nonzero incidence-graph representation. Related full-cube symmetry results concern a different complex and do not by themselves give the stated restricted two-layer action.

## Limitations
This is rational equivariant homology, not an integral equivariant decomposition or an equivariant wedge-of-spheres equivalence. The quotient's vanishing rational homology neither proves contractibility nor excludes torsion. The proof uses Feng–Nukala's nonequivariant homotopy theorem as a stated literature premise. No claim is made about other distances, nonconsecutive ranks or persistence maps. Bibliographic searches cannot establish absolute priority against inaccessible or unindexed sources.

## References
- Z. Feng and N. C. P. Nukala, *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, first submitted 2023-02-28. Particularly Corollary 11 (one rank) and Theorem 13 (two consecutive ranks), https://arxiv.org/abs/2302.14664 .
- W. Fulton, *Young Tableaux*, London Mathematical Society Student Texts 35, Cambridge University Press, 1997, for standard Frobenius-characteristic, Pieri, and Jacobi–Trudi identities.
