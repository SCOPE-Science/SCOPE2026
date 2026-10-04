# The four-point finite circle realizes both homotopy classes into a minimal projective plane
## Finding
Let \(C\) be the four-point minimal finite circle, with two minimal points \(\ell_0,\ell_1\), two maximal points \(u_0,u_1\), and \(\ell_i<u_j\) for every \(i,j\in\{0,1\}\). Let \(P=P_2^2\) be the 13-point minimal finite model of \(\mathbb{RP}^2\) described by Cianci and Ottina. Then the pointwise mapping poset \(P^C\) has exactly \(853\) elements and two homotopy components, of sizes \(721\) and \(132\).

The larger component contains all \(13\) constant maps and strongly deformation retracts onto the constant-map copy of \(P\). The smaller component consists exactly of the maps inducing a nonzero homomorphism
\[
H_1(C;\mathbf F_2)\longrightarrow H_1(P;\mathbf F_2).
\]
Therefore \([C,P]\) has exactly two elements. Under order complexes these two classes map to the two free-homotopy classes from \(S^1\) to \(\mathbb{RP}^2\), so the comparison is bijective without subdividing \(C\).

## Assumptions and scope
Finite \(T_0\)-spaces are written as their specialization posets. Continuous maps are therefore order-preserving maps. The source is specifically the four-point circle \(C=S^0\circledast S^0\).

The target is specifically the model \(P_2^2\) in Cianci--Ottina. Its points are minima \(c_1,c_2,c_3,c_4\), middle points \(b_1,\ldots,b_6\), and maxima \(a_1,a_2,a_3\). The middle-to-maximal incidences are
\[
\begin{aligned}
 b_1,b_2&<a_1,a_2,\\
 b_3,b_4&<a_1,a_3,\\
 b_5,b_6&<a_2,a_3,
\end{aligned}
\]
and the minimal points below the middle points are
\[
\begin{aligned}
 b_1&:\{c_1,c_2\},& b_2&:\{c_3,c_4\},& b_3&:\{c_1,c_3\},\\
 b_4&:\{c_2,c_4\},& b_5&:\{c_2,c_3\},& b_6&:\{c_1,c_4\}.
\end{aligned}
\]
All order relations are generated transitively from these cover relations.

The claim is an exact statement about this finite source and target. It does not assert the same component structure for every finite model of \(\mathbb{RP}^2\), nor for subdivided or larger finite circles.

## Proof
There are only \(13^4\) set maps \(C\to P\). A map is continuous exactly when the four inequalities \(f(\ell_i)\le f(u_j)\) hold. Exhaustive enumeration of those inequalities gives exactly \(853\) maps.

Order the maps pointwise: \(f\le g\) when \(f(x)\le g(x)\) for every \(x\in C\). For maps between finite spaces, two maps are homotopic exactly when they are joined by a finite fence of pointwise comparable maps. Thus the connected components of the comparability graph of \(P^C\) are precisely the finite-space homotopy classes. Exact enumeration gives two components, of sizes \(721\) and \(132\).

The order complex of \(P\) has \(13\) vertices, \(36\) comparable edges, and \(24\) three-element chains. Over \(\mathbf F_2\), the boundary maps have ranks \(12\) and \(23\), so
\[
\dim_{\mathbf F_2}H_1(P;\mathbf F_2)=36-12-23=1.
\]
The fundamental one-cycle of the order complex of \(C\) is the sum of its four comparable edges. For each of the \(853\) maps, its image is reduced modulo the span of the \(24\) triangle boundaries. Exactly \(132\) maps have a nonzero class, and these \(132\) maps are exactly one of the two mapping-poset components. A concrete essential witness is
\[
f(\ell_0)=c_1,\qquad f(\ell_1)=c_2,\qquad f(u_0)=b_1,\qquad f(u_1)=a_3.
\]
All constants lie in the other component.

Finally, the verifier removes \(708\) nonconstant beat points from the \(721\)-map component. Each removal is checked at the moment it is made: an up-beat point has a least strict upper neighbor in the current induced subposet, and a down-beat point has a greatest strict lower neighbor. The terminal \(13\)-point subposet is exactly the constant maps, whose inherited order is exactly \(P\). Each beat-point deletion is a strong deformation retraction, proving that the null component strongly deformation retracts onto the constant-map copy of \(P\).

For the classical comparison, \(|\mathcal K(C)|\cong S^1\), while \(|\mathcal K(P)|\) is homotopy equivalent to \(\mathbb{RP}^2\). Free-homotopy classes \(S^1\to\mathbb{RP}^2\) are conjugacy classes in \(\pi_1(\mathbb{RP}^2)\cong\mathbf Z/2\), hence there are exactly two. The zero and nonzero maps on mod-two first homology distinguish them. Since the two finite homotopy components exhibit exactly those two behaviors, passage to order complexes is bijective on these homotopy sets.

## Verification
The standalone script `verify.py` reconstructs the Cianci--Ottina incidence data, computes its transitive closure, enumerates every set map \(C\to P\), and filters by order preservation. It then constructs the pointwise mapping poset, computes all comparability components, computes the mod-two first homology of the target order complex, classifies all maps by the induced class of the source fundamental cycle, and validates every beat-point deletion used in the strong deformation retraction.

Replaying the packaged script prints:

`VERIFY_OK maps=853 components=721,132 essential=132 H1dim=1 null_deletions=708 up=184 down=524 witness=('c1', 'c2', 'b1', 'a3')`

These are exhaustive finite calculations, not samples. The computation proves only the stated finite enumeration and certificate facts; the general finite-space homotopy and beat-point implications used above are standard theorems.

## Relationship to prior work
Cianci and Ottina prove that \(13\) points are minimal for a finite model of \(\mathbb{RP}^2\) and classify the two \(13\)-point minimal models; their proof gives the incidence description used here. They do not enumerate maps from the four-point finite circle or determine the mapping-poset components.

May's notes record Stong's mapping-space description: homotopies of maps into a finite space are detected by fences of comparable maps, and mapping-space components correspond to homotopy classes. The same notes also explain the finite-space simplicial approximation theorem, under which barycentric subdivision of the source is generally available to realize classical maps. The finding above is a sharp positive instance at subdivision depth zero for the fundamental loop classes of a minimal projective-plane model.

Hardie, Vermeulen, and Witbooi construct a nontrivial pairing of finite \(T_0\)-spaces and are part of the literature surrounding finite models and subdivision. Their article is relevant context but does not, in the material inspected, state the exact \(853\)-map enumeration, the \(721/132\) component decomposition, or the homology characterization proved here.

## Limitations
The exact claim is for \(P_2^2\), not simultaneously for its opposite partner \(P_1^2\). The exact component cardinalities depend on the chosen finite models even though the two resulting order-complex homotopy classes agree with the classical pair of free-homotopy classes. No claim is made about higher homotopy groups of the mapping space, about based mapping spaces, or about minimal subdivision depth for arbitrary source spaces.

The originality comparison is literature-based rather than a formal proof of absence from all publications. The full text of the Hardie--Vermeulen--Witbooi article was not available in the inspected source; its metadata and topic were checked, so a residual access risk remains.

## References
1. N. Cianci and M. Ottina, *Poset splitting and minimality of finite models*, arXiv:1512.06088v1, first public 2015-12-18; later Journal of Combinatorial Theory, Series A. In particular, Section 5 and Theorem 5.10 classify the 13-point projective-plane models.
2. J. P. May, *Finite Spaces and Simplicial Complexes*, notes for the REU, Summer 2003, revised 2008 and 2010. Sections 7--8 discuss mapping spaces and finite-space simplicial approximation.
3. K. A. Hardie, J. J. C. Vermeulen, and P. J. Witbooi, *A nontrivial pairing of finite T0 spaces*, Topology and its Applications 125, 533--542; DOI:10.1016/S0166-8641(01)00298-X.
