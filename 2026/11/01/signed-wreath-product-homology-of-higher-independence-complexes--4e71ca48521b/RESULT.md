# Signed wreath-product homology of higher independence complexes of two-level trees

## Finding
Let \(m\ge r\ge3\) and let \(s_1,\ldots,s_m\ge1\) be integers. Form the rooted tree \(T=T(m;s_1,\ldots,s_m)\) from a root \(c\), branch centers \(u_1,\ldots,u_m\) adjacent to \(c\), and disjoint leaf sets \(L_i\) of sizes \(s_i\), where each leaf of \(L_i\) is adjacent only to \(u_i\). The complex \(\operatorname{Ind}_r(T)\) consists of vertex subsets for which every connected component of the induced subgraph has at most \(r\) vertices.

**Theorem.** The root-deletion inclusion
\[
\operatorname{Ind}_r(T-c)\longrightarrow\operatorname{Ind}_r(T)
\]
is a homotopy equivalence. Writing \(B=\prod_{i=1}^m\binom{s_i-1}{r-1}\), the integral homotopy type is
\[
\operatorname{Ind}_r(T)\simeq\bigvee^{B}S^{rm-1}.
\]
The binomial coefficient vanishes outside its usual range; if \(B=0\), the complex is contractible. All reduced integral homology vanishes except possibly in degree \(rm-1\), where it is free of rank \(B\).

Put \(U_i=\ker(\mathbb Z^{L_i}\xrightarrow{\sum}\mathbb Z)\). Under every root-preserving tree automorphism, this integral homology group is naturally the graded-permutation tensor
\[
\widetilde H_{rm-1}(\operatorname{Ind}_r(T);\mathbb Z)
\cong \bigotimes_{i=1}^m\bigwedge^{r-1}U_i.
\]
A transposition of two branch factors contributes the Koszul sign \((-1)^r\), in addition to the natural leaf-permutation maps. These assertions do not require equal branch sizes.

In the uniform case \(s_i=s\ge r\), the full automorphism group is \(G\cong S_s\wr S_m\), and the rational top-homology representation is irreducible. For \(g=(\sigma_1,\ldots,\sigma_m;\pi)\in G\), let \(C\) range over the cycles of the branch permutation \(\pi\); let \(\rho_C\in S_s\) be the product of leaf permutations around \(C\); let \(a_j(\rho_C)\) count its length-\(j\) cycles. Its complete character is
\[
\chi(g)=\operatorname{sgn}(\pi)^r\prod_C[t^{r-1}]
\frac{\prod_{j\ge1}(1-(-t)^j)^{a_j(\rho_C)}}{1+t}.
\]
For example, the uniform case \(r=3\), \(m=s=4\) has exactly \(81\) spheres of dimension \(11\), and its \(81\)-dimensional rational top homology is irreducible under \(S_4\wr S_4\).

## Assumptions and scope
The complex is the ordinary higher independence complex, not the ordinary graph independence complex or a matching complex. All graph vertices are labeled for defining the construction; homotopy statements are independent of labels. We assume \(m\ge r\ge3\), every \(s_i\ge1\), and no edges other than those stated. Every equivalence is an ordinary topological homotopy equivalence of finite simplicial realizations. The module is an isomorphism of integral representations for the root-preserving automorphism group, with signed branch interchange; an equivariant homotopy equivalence is **not** claimed. The uniform case assumes \(s\ge r\) when asserting a nonzero irreducible module.

## Proof
**1. A collapsible root link.** Set \(X=\operatorname{Ind}_r(T)\), \(A=\operatorname{Ind}_r(T-c)\), and \(L=\operatorname{lk}_X(c)\). Then \(X=A\cup(c*L)\), with intersection \(L\). For each face \(F\in L\), let \(U(F)=\{i:u_i\in F\}\). Since \(F\cup\{c\}\) is admissible and its component containing \(c\) contains all chosen branch centers, \(|U(F)|\le r-1\). As \(m\ge r\), some branch center is not selected. Take the smallest such branch \(i(F)\), fix a distinguished leaf \(\ell_i\in L_i\) for each branch, and pair \(F\) with \(F\triangle\{\ell_{i(F)}\}\). This is a perfect matching on the augmented face poset of \(L\), including the empty face: toggling the leaf of an unselected branch preserves every induced component size because that leaf is isolated in the selected subgraph, both before and after adjoining \(c\).

To prove acyclicity, orient each unmatched cover relation downward and each matched one upward. Along a directed edge the center-index set \(U(F)\) can only decrease, and on a matched edge it stays constant. A directed cycle would therefore have constant \(U\), hence a fixed toggled leaf. Within this fiber, the corresponding leaf can only be added along a matched upward edge, and cannot be removed along a downward edge, so no directed cycle exists. Removing the empty-face pair from the augmented matching leaves a single critical vertex and no other critical simplex. Thus \(L\) is simplicially collapsible, in particular contractible. Since \(L\hookrightarrow A\) is a cofibration, attaching the cone \(c*L\) does not change the homotopy type of \(A\). Hence \(A\hookrightarrow X\) is a homotopy equivalence.

**2. Root-deleted factors.** The graph \(T-c\) is the disjoint union of stars \(K_{1,s_i}\), so
\[
A=\bigast_{i=1}^m B_i,\qquad B_i=\operatorname{Ind}_r(K_{1,s_i}).
\]
Let \(D_i\) be the full simplex on leaves \(L_i\), and let \(K_i=\operatorname{skel}_{r-2}D_i\). Then \(B_i=D_i\cup(u_i*K_i)\), with intersection \(K_i\). Both pieces are contractible; the homotopy pushout gives \(B_i\simeq\Sigma K_i\). The skeleton of the \((s_i-1)\)-simplex has reduced integral homology only in degree \(r-2\), of rank \(\binom{s_i-1}{r-1}\), and is homotopy equivalent to a wedge of spheres of that dimension whenever noncontractible. This includes \(s_i<r\), when \(B_i\) is a simplex and is contractible. The join formula gives \(A\simeq\bigvee^{B}S^{rm-1}\), with the specified zero-wedge convention. Combining with Step 1 proves the homotopy claim.

**3. Integral symmetry lattice.** The reduced chain complex of the full leaf simplex is the exterior-algebra complex with differential given by contraction by the all-ones augmentation covector. Its degree-\((r-2)\) skeleton cycles identify, naturally under leaf permutations, with \(\bigwedge^{r-1}U_i\). In the Mayer–Vietoris sequence for \(B_i=D_i\cup(u_i*K_i)\), the connecting map identifies \(\widetilde H_{r-1}(B_i;\mathbb Z)\) with \(\widetilde H_{r-2}(K_i;\mathbb Z)\) equivariantly. The join Künneth isomorphism over \(\mathbb Z\), using free homology, yields exactly the tensor lattice in the theorem. Interchanging two join factors whose reduced homology is in degree \(r-1\) gives graded sign \((-1)^{((r-1)+1)^2}=(-1)^r\). The root-deletion inclusion is canonical and root-automorphism-equivariant and induces a homology isomorphism, even though its homotopy inverse need not be equivariant.

**4. Character and irreducibility.** For \(s_i=s\ge r\), \(\bigwedge^{r-1}(U_s\otimes\mathbb Q)\) is the irreducible hook Specht module of shape \((s-r+1,1^{r-1})\). Its external tensor power is irreducible under the normal subgroup \((S_s)^m\); hence it remains irreducible under the larger wreath product. For \(\rho\in S_s\), the characteristic polynomial on the leaf permutation module is \(\prod_{j\ge1}(1-(-t)^j)^{a_j(\rho)}\). Dividing by the trivial eigenvalue factor \(1+t\) gives the generating function of exterior-power characters of \(U_s\). Tracing the graded permutation tensor around each cycle of \(\pi\) gives one leaf-monodromy trace per cycle and the global sign \(\operatorname{sgn}(\pi)^r\). This proves the stated character formula. No field-dependent extrapolation is needed for the integral lattice isomorphism.

## Verification
The standalone file `verify.py` reconstructs actual induced-subgraph admissibility and every root-link face. For \((r,m,s)=(3,3,3)\), it enumerates \(4679\) faces, the \(1304\)-face augmented link, \(652\) link-matching pairs, and all \(6036\) link incidences, and verifies the directed Hasse graph is acyclic. Exact mod-two reduction gives one degree-eight class. It tests the complete signed Lefschetz character against the wreath-product formula for all \(1296\) group elements. For \((3,3,4)\), it enumerates \(27667\) faces and finds \(27\) degree-eight classes, checks the entire link acyclic and compares \(26\) selected wreath elements. For unequal sizes \((3,3,4)\), it independently enumerates \(8475\) faces, checks a \(2400\)-face link matching acyclic, and finds three degree-eight classes.

Run `python3 verify.py` using Python 3. No third-party package is needed. These finite checks corroborate but do not establish the infinite-parameter theorem; Steps 1–4 are its proof.

## Relationship to prior work
Sawant (arXiv:2605.25150v1, publicly posted May 24, 2026) proves vertex decomposability of \(\operatorname{Ind}_r(T)\) for every tree and threshold. That general structural theorem implies a sphere-wedge homotopy type, but not these sphere multiplicities or the integral automorphism representation. Deshpande and Singh (arXiv:2001.05448v2, Theorem 5.6) give the **nonequivariant** sphere-wedge classification for perfect regular rooted trees; in particular, the equal-branch-size subfamily's ordinary homotopy ranks are not claimed novel. The present theorem supplies all unbalanced sizes and, decisively, the integral full-wreath action and its parity-twisted irreducible rational representation. Existing special calculations at threshold two and for double-star trees do not imply the threshold-at-least-three multi-branch representation.

## Limitations
No claim is made for \(m<r\), for arbitrary-depth rooted trees, for an equivariant homotopy inverse to root deletion, or for a new nonequivariant theorem about the already-classified perfect regular subfamily. An equivalent unindexed result or a representation calculation not located in the inspected sources remains a literature risk. The finite checks are not a substitute for the all-parameter argument. The review of this result has not been independently validated.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (May 24, 2026), https://arxiv.org/html/2605.25150v1.
- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2, Theorem 5.6, https://arxiv.org/html/2001.05448v2.
- Standard simplicial discrete Morse theory, join Künneth formula, and the exterior-power construction of hook Specht representations.
