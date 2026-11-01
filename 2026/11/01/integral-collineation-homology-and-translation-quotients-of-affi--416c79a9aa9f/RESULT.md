# Integral collineation homology and translation quotients of affine-plane Rips complexes

## Finding

Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\). Let \(G=G_{\mathcal A}\) be the bipartite graph whose vertices are the points and lines, with an edge for every incidence. Equip its vertices with the shortest-path unit-edge metric and set \(X=\operatorname{VR}_{\le2}(G)\). Write \(\mathcal D\) for its set of \(q+1\) parallel directions, and \(L_d\) for the set of \(q\) lines of direction \(d\). Put
\[
A_d=\ker\big(\mathbb Z[L_d]\xrightarrow{\sum}\mathbb Z\big).
\]

**Integral equivariant theorem.** Under every collineation of \(\mathcal A\), the only nonzero reduced integral homology modules are
\[
\widetilde H_2(X;\mathbb Z)\cong H_1(G;\mathbb Z),\qquad
\widetilde H_q(X;\mathbb Z)\cong
\det\!\big(\mathbb Z[\mathcal D]\big)\otimes
\bigotimes_{d\in\mathcal D}A_d.
\]
A choice of ordering of \(\mathcal D\) identifies the last expression with an ordinary tensor product; changing the ordering changes the orientation of the determinant line. A collineation sends the direction factor for \(d\) to that for \(g(d)\), multiplied by the sign of its permutation of directions. Thus both isomorphisms are **integral** and **equivariant**. Their ranks are respectively \((q-1)^2(q+1)\) and \((q-1)^{q+1}\).

For a collineation \(g\), denote the numbers of fixed points, fixed lines and fixed incident point–line flags by \(P(g),L(g),F(g)\). Let \(\pi_g\) be the induced permutation of \(\mathcal D\); for each direction-cycle \(C\), choose \(d_C\in C\). Its two nonzero reduced homology traces are
\[
\chi_2(g)=F(g)-P(g)-L(g)+1,
\]
\[
\chi_q(g)=(-1)^{q+1-c(\pi_g)}
\prod_{C\in\operatorname{Cyc}(\pi_g)}
\Big(\#\operatorname{Fix}_{L_{d_C}}(g^{|C|})-1\Big).
\]
The cycle factor is independent of the selected representative direction.

**Translation-quotient transition.** If \(\mathcal A=\operatorname{AG}(2,q)\) over a finite field and \(T\cong(\mathbb F_q^2,+)\) is its translation group, then the rational homology of the geometric quotient \(X/T\) satisfies
\[
\widetilde H_2(X/T;\mathbb Q)=0,\qquad
\dim_{\mathbb Q}\widetilde H_q(X/T;\mathbb Q)=
\frac{(q-1)^{q+1}+(q^2-1)(q-1)(-1)^q}{q^2},
\]
with no other nonzero reduced rational groups. At \(q=3\) this quotient is rationally acyclic; at \(q=4\), its fourth rational Betti number is \(18\), and for every prime power \(q\ge4\) the displayed top rank is positive.

## Assumptions and scope

A finite affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q+1\) classes of mutually parallel lines, and \(q\) lines in each class. Each point lies on \(q+1\) lines and each line contains \(q\) points. This theorem is conditional only on existence of such a plane; it assumes no coordinates, Desarguesian property, or transitive automorphism group. A collineation is a permutation preserving the point–line incidence relation; it preserves parallelism. The affine incidence graph's two vertex degrees are different for \(q\ge3\), so its graph automorphisms preserve the two vertex parts. All homology groups in the theorem are reduced except \(H_1(G;\mathbb Z)\), which is ordinary graph homology. The graph-metric Vietoris–Rips threshold is **inclusive** and exactly two. For the translation statement only, \(q\) is a prime power and \(\mathcal A\) is the ordinary finite-field affine plane.

## Proof

**1. Exact clique cover.** Every pair of points is graph-distance two. Two lines have distance two precisely when their directions differ; parallel distinct lines have distance four. Point and line have distance one when incident and three otherwise. Consequently, every mixed clique in \(X\) lies in a point simplex \(\{\ell}\}*\Delta(P_\ell)\) around a line \(\ell\), or in a line simplex \(\{p}\}*\Delta(L_p)\) around a point \(p\): a mixed clique cannot contain two distinct points and two distinct lines because the distinct points share a unique line.

Let \(P\) and \(L\) denote the point and line sets and define
\[
U=\Delta(P)\cup\bigcup_{\ell\in L}(\{\ell}\}*\Delta(P_\ell)),
\quad
B=\bigast_{d\in\mathcal D} D(L_d),
\quad
V=B\cup\bigcup_{p\in P}(\{p}\}*\Delta(L_p)),
\]
where \(D(L_d)\) is the discrete vertex complex on \(L_d\). The clique classification gives simplicial identities \(X=U\cup V\) and \(U\cap V=G\), where \(G\) is regarded as the original one-dimensional incidence subcomplex. These are invariant under every collineation.

**2. The two equivariant homology inputs.** Each of the line-vertex cones in \(U\) meets the preceding pieces in a full simplex \(\Delta(P_\ell)\) inside \(\Delta(P)\). Attaching a cone on a contractible simplex changes no homotopy groups or homology. Thus \(U\) is contractible. Likewise the point-vertex cones of \(V\) attach to \(B\) along the full simplex \(\Delta(L_p)\), which is a simplex of \(B\) since the \(q+1\) lines through \(p\) have distinct directions. Hence the **inclusion** \(B\hookrightarrow V\) is a homotopy equivalence (in particular an equivariant map inducing an integral module isomorphism). These arguments do not need an equivariant choice of a collapse sequence.

There are \(q+1\) nonempty discrete factors in the join \(B\). Their reduced integral homology is concentrated in degree zero, with module \(A_d\). Integral join Künneth and freeness give \(\widetilde H_i(B)=0\) for \(i\ne q\) and
\[
\widetilde H_q(B;\mathbb Z)\cong\bigotimes_{d\in\mathcal D}A_d.
\]
Permuting the join factors changes the oriented join chain by the sign of that permutation: exchanging two degree-zero reduced factors entails exchanging two shifted degree-one factors. The orientation line \(\det(\mathbb Z[\mathcal D])\) records this sign canonically, yielding the claimed collineation action.

**3. Equivariant Mayer–Vietoris.** The reduced integral Mayer–Vietoris sequence for \(X=U\cup V\) is natural under collineations. For \(q\ge3\), \(G\) has no homology in dimensions at least two, and \(U\) has none. Thus inclusion \(H_q(V)\to H_q(X)\) is an isomorphism. Since \(V\) has reduced homology only in degree \(q\ge3\), the connecting map gives \(\widetilde H_2(X)\xrightarrow{\cong}H_1(G)\). Every other reduced group vanishes. Combining these **canonical equivariant maps** with Step 2 proves both integral module descriptions. The rank of graph cycle homology is \(|E(G)|-|V(G)|+1=q^2(q+1)-(2q^2+q)+1=(q-1)^2(q+1)\), since \(G\) is connected.

**4. Trace in degree two.** Orient every incidence edge from a point to a line. Every collineation preserves the orientation convention. As \(G\) is connected, its chain exact sequences give the equality of characters \([H_1(G)]=[C_1(G)]-[C_0(G)]+[\mathbb Z]\). The edge trace is the number of fixed flags, and the vertex trace the sum of fixed points and fixed lines. This gives \(\chi_2(g)=F(g)-P(g)-L(g)+1\), integrally after tensoring with \(\mathbb Q\) to take traces.

**5. Trace in top degree.** Let \(C=(d,g(d),\ldots,g^{\ell-1}(d))\) be a cycle of the action on directions. In the tensor product over the factors of \(C\), the trace of the cyclic factor permutation with the individual linear maps equals the trace of the monodromy \(g^\ell\) on \(A_d\). Since \(A_d\) is the sum-zero sublattice of the line permutation module, this trace is \(\#\operatorname{Fix}_{L_d}(g^\ell)-1\). Multiply over independent direction cycles and by the determinant sign \((-1)^{q+1-c(\pi_g)}\). This yields the formula for \(\chi_q\).

**6. The translation quotient.** Now let \(\mathcal A=\operatorname{AG}(2,q)\). Each nonzero translation fixes no point and exactly the \(q\) lines parallel to its direction. It fixes no incident flag, so its degree-two trace equals \(1-q\). For the identity the degree-two trace is \((q-1)^2(q+1)=(q^2-1)(q-1)\). Averaging over the \(q^2\) translations shows \(\dim H_2(X;\mathbb Q)^T=0\).

A nonzero translation fixes every parallel class setwise. It fixes all \(q\) lines in its own direction and no line in the other \(q\) directions. Its trace in top homology is therefore \((q-1)(-1)^q\); the identity's trace is \((q-1)^{q+1}\). Averaging gives the displayed top invariant dimension. For a finite simplicial group action, barycentric subdivision removes inversions; averaging rational chains yields \(H_*(X/T;\mathbb Q)\cong H_*(X;\mathbb Q)^T\), even though the action need not be free. This proves the geometric quotient assertion. The top formula is zero at \(q=3\), equals \(18\) at \(q=4\), and is strictly positive at every prime power \(q\ge4\), since \((q-1)^q>q^2-1\) for \(q\ge5\). The complex and quotient are connected, so there are no other reduced rational homology groups.

## Verification

The standalone Python-standard-library script `verify_affine.py` exhaustively builds the order-three affine-plane incidence graph with 21 vertices and its scale-two complex with 949 nonempty faces. An independent mod-two simplicial boundary elimination yields Betti vector \((1,0,16,16,0,0,0,0,0)\) in degrees zero through eight. The script then constructs every one of the \(432\) affine collineations in \(\operatorname{AGL}_2(\mathbb F_3)\), and computes the **signed simplicial Lefschetz number** by enumerating their invariant simplices with orientation signs. It independently evaluates the incidence-flag trace and parallel-direction monodromy trace, checking the identity \(\widetilde L(g)=\chi_2(g)-\chi_3(g)\) for all \(432\) maps. The final output is `VERIFY_OK affine maps 432`. These finite calculations are consistency checks, not an infinite proof or integral classification; Steps 1–6 provide the complete integral proof for all existing finite affine planes.

## Relationship to prior work

The publicly indexed 2026 result *Affine-plane incidence Rips complexes have two sphere dimensions* proves the nonequivariant homotopy type \(\bigvee^{(q-1)^2(q+1)}S^2\vee\bigvee^{(q-1)^{q+1}}S^q\) for all finite affine planes. Its full mathematical statement and proof were inspected: although its exact clique cover provides essential input, it does not state integral collineation modules, signed permutation actions, the two full character formulas, or the translation-quotient transition. Ordinary homotopy type does not determine these group actions. The present theorem is explicitly an **equivariant refinement**, not a second claim of the previous nonequivariant classification.

The published *Complete Rips barcodes and top-dimensional symmetry of multipartite prisms* computes an integral augmentation-tensor module for a different family of graph products. That class does not include affine-plane incidence graphs with unequal point and line degrees and affine parallelism. The *Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs* result computes a representation for a graph with two high-degree poles and disjoint length-three paths, not an affine incidence graph. Galetto, Montaño and Wellner's 2026 paper treats hypercube Rips automorphism representations, not affine incidence structures. These specific comparisons and a targeted indexed and web search found no theorem implying the present all-collineation, all-plane result; unindexed equivalences and implicit deductions from prior proofs remain a genuine risk.

## Limitations

The theorem is restricted to the inclusive graph-metric radius-two complex of a finite affine plane of order at least three, and collineations thereof. It does not classify arbitrary incidence designs, metric scales, cohomology rings, equivariant homotopy types, or quotients by general non-translation subgroups. The rational quotient ranks do not imply integral homology or absence of quotient torsion. No claim is made for nonexistent plane orders. The step from the prior homotopy calculation to these group-action modules is based on the exact invariant cover, so implicit coverage in unindexed or unpublished equivariant treatments remains possible. Independent mathematical validation has not been performed.

## References

1. *Affine-plane incidence Rips complexes have two sphere dimensions*, public mathematical research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4, complete result and proof inspected.
2. *Complete Rips barcodes and top-dimensional symmetry of multipartite prisms*, public mathematical research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-rips-barcodes-and-top-dimensional-symmetry-of-multipart--8573c09b40de, complete result and proof inspected.
3. *Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs*, public mathematical research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-and-symmetry-of-three-edge-th--c282838fbdca, complete result and proof inspected.
4. F. Galetto, J. Montaño, Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first public 2026-06-18), https://arxiv.org/abs/2606.20784 (different metric family; published abstract reviewed).
5. H. Adams et al., *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v1 (first public 2025-02-10), https://arxiv.org/abs/2502.07134 (different graph family and metric).
