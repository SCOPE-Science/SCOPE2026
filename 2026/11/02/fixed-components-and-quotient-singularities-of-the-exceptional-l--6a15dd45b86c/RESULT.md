# Fixed components and quotient singularities of the exceptional length-two Quot involution

## Finding
Let \(C\) be a smooth connected projective curve over \(\mathbb C\), of genus \(g\), and fix an integer \(r\ge2\). Set
\[
Q=\operatorname{Quot}^{2}_{C}(\mathcal O_C^{\oplus r}),
\]
whose points are coherent surjections from the trivial rank-\(r\) bundle to torsion sheaves of length two, modulo isomorphisms of the target. Let \(\alpha\) denote the involution constructed by Bansal--Sarkar--Vats from exchanging the two ordered points of the universal degree-two divisor. Its **scheme-theoretic** fixed locus is
\[
\boxed{Q^\alpha\cong(C^{(2)}\times\mathbb P^{r-1})\sqcup(C\times\operatorname{Gr}(2,r)).}
\]
The two connected components have dimensions \(r+1\) and \(2r-3\), respectively. Their normal bundles carry the negative involution character in ranks \(r-1\) and \(3\), respectively. Consequently, the quotient \(Y=Q/\langle\alpha\rangle\) has transverse local quotient types \(\mathbb A^{r-1}/\{\pm1\}\) and \(\mathbb A^3/\{\pm1\}\) along the images of these components. The latter is everywhere index-two non-Gorenstein; thus \(Y\) is never Gorenstein. The image of the first component is smooth in \(Y\) when \(r=2\), and lies in its singular locus when \(r\ge3\).

The topological Lefschetz number of this involution is exactly
\[
\boxed{L(\alpha)=r(1-g)(r+2-2g).}
\]

## Assumptions and scope
The base field is \(\mathbb C\); \(C\) is connected, smooth and projective, without any restriction on genus; the source bundle is explicitly trivial and framed, and the quotient has length exactly two. \(C^{(2)}\) means the symmetric square of \(C\). The Grassmannian \(\operatorname{Gr}(2,r)\) parametrizes two-dimensional quotients of \(\mathbb C^r\). All claims about fixed points are scheme-theoretic in characteristic zero. The singularity assertion describes analytic or completed local germs, not a claimed global product decomposition of the quotient.

## Proof
**1. The ambient space and involution.** A torsion quotient \(\mathcal O_C^{\oplus r}\twoheadrightarrow F\) of length two has a locally free kernel \(K\) of rank \(r\). Its tangent and obstruction spaces are \(\operatorname{Hom}(K,F)\) and \(\operatorname{Ext}^1(K,F)\), respectively. As \(F\) is zero-dimensional, the latter vanishes and the former has dimension \(2r\). Therefore \(Q\) is smooth of dimension \(2r\). Over the symmetric square \(C^{(2)}\), the universal effective divisor \(D\) is a finite flat double cover. Its deck involution \(\tau\) exchanges the two points, including its nontrivial action on the infinitesimal double point. The target of every length-two quotient is an \(\mathcal O_D\)-module: locally this follows directly from the characteristic polynomial of multiplication by a parameter. Pullback by \(\tau\) therefore defines the involution \(\alpha\).

**2. Cyclic chart, including collision.** Work near an effective divisor in a coordinate chart of \(C\), with local coordinate \(t\). Write the universal divisor as
\[
 D:\quad t^2-s_1t+s_2=0,
\]
and put \(w=t-s_1/2\). The involution exchanges the roots, so \(\tau(w)=-w\) while \(s_1,s_2\) are unchanged. If the image of one standard source generator generates the target as an \(\mathcal O_D\)-module, identify that image with \(1\). The other \(r-1\) images have unique expressions \(A_j+B_jw\), where \(2\le j\le r\). This is a smooth affine chart of \(Q\) with coordinates \(s_1,s_2,A_j,B_j\), hence dimension \(2r\). On this chart,
\[
 \alpha:(s_1,s_2,A_j,B_j)\longmapsto(s_1,s_2,A_j,-B_j).
\]
Therefore the fixed subscheme is cut out **scheme-theoretically** by \(B_j=0\) for every \(j\). Its points are precisely the quotients of \(\mathcal O_D\) induced by a constant line quotient of \(\mathbb C^r\). Such quotients assemble globally into \(C^{(2)}\times\mathbb P^{r-1}\), and the negative normal rank is \(r-1\).

**3. Semisimple chart at a collided divisor.** Suppose instead that two chosen source generators map to a basis of the two-dimensional complex vector space \(H^0(F)\). The target is then specified by multiplication by \(t\), a matrix
\[
 T=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
and by the vectors \(v_3,\ldots,v_r\in\mathbb C^2\) representing the remaining generators. The local chart has \(4+2(r-2)=2r\) coordinates, and its support divisor has polynomial \(\det(tI-T)\). In particular, \(s_1=\operatorname{tr}(T)\). Pulling the module back through \(t\mapsto s_1-t\) gives the **exact** action
\[
 \alpha:(T,v_3,\ldots,v_r)\longmapsto
 \bigl(\operatorname{tr}(T)I-T,v_3,\ldots,v_r\bigr).
\]
Write \(T=\lambda I+S\) with \(\operatorname{tr}(S)=0\). The involution fixes \(\lambda\) and the vectors, and sends \(S\mapsto-S\). Since the space of traceless \(2\times2\) matrices has dimension three, the fixed scheme in this chart is **exactly** \(S=0\), with negative normal rank three. At a fixed point \(T=\lambda I\), multiplication by \(t-\lambda\) is zero on \(F\), so \(F\cong k_x^{\oplus2}\). The quotient is then parametrized by the support point \(x\in C\) and a two-dimensional quotient of \(\mathbb C^r\), giving \(C\times\operatorname{Gr}(2,r)\). Conversely every such skyscraper quotient is fixed.

**4. Exhaustion and disjointness.** If the support divisor has two distinct points, a length-two target is a direct sum of two length-one quotients; fixing the transposition forces the two quotient lines to coincide, so the target lies in the cyclic chart. Over a doubled point \(2x\), any length-two module over the completed discrete valuation ring is either cyclic of length two or a direct sum of two residue fields. The cyclic type belongs to the first chart, the semisimple type to the second. Thus these charts classify every geometric fixed point and identify the *entire fixed scheme*, not merely its reduced support. The two global smooth projective parameter spaces are closed in \(Q\), disjoint, and connected; the chart descriptions identify them isomorphically with the two connected components of \(Q^\alpha\).

**5. Local quotients.** The two charts linearize \(\alpha\) as identity in the tangent directions of each fixed component and negation on \(r-1\) or three transverse variables. Taking invariants gives precisely the stated transverse quotient germs. The three-variable sign quotient is singular and non-Gorenstein of canonical index two: the sign involution has determinant \(-1\) on its three-dimensional space, has no pseudoreflections, and its square acts trivially on a local top differential form. Therefore the quotient has a non-Gorenstein locus along the image of \(C\times\operatorname{Gr}(2,r)\) for every \(r\ge2\).

**6. Lefschetz number.** For a finite-order automorphism of a compact complex variety, its topological Lefschetz number equals the Euler characteristic of its fixed locus. Put \(\chi(C)=2-2g\). Then
\[
\begin{aligned}
L(\alpha)&=r\,\chi(C^{(2)})+\binom r2\chi(C)\\
&=\frac r2\chi(C)\bigl(\chi(C)+1\bigr)+\binom r2\chi(C)\\
&=r(1-g)(r+2-2g),
\end{aligned}
\]
where \(\chi(C^{(2)})=\chi(C)(\chi(C)+1)/2\) follows from the symmetric-product Euler series. This completes the proof.

## Verification
The affine formulas are exact identities. In the cyclic chart, \(w\mapsto-w\) fixes precisely the zero odd coefficients. In the semisimple chart, the action on \(T\) is its adjugate, and fixing it forces \(a=d\), \(b=c=0\). These are three independent linear equations, so the transverse negative eigenspace really has dimension three. The accompanying standalone standard-library program `verify_local.py` verifies the involution, trace and determinant preservation for 625 small integer matrices, 2401 centered substitutions, and the Euler and codimension identities in a grid of ranks and genera. Running `python3 verify_local.py` returned `VERIFY_OK`. These finite checks only sanity-test the symbolic identities; the exhaustive geometric proof is the chart argument above.

## Relationship to prior work
Bansal, Sarkar and Vats construct the non-natural involution and prove that it exhausts the exceptional factor in automorphism groups of length-two Quot schemes of trivial bundles (arXiv:2609.14283v1, Section 2.7 and Theorem B). Their construction explicitly identifies the swap on the reduced two-point fibre; the present result identifies **both complete fixed components at and away from the diagonal** and computes the resulting quotient singularities and Lefschetz number. The 2026 study of \(\mu_2\)-fixed punctual Quot schemes in arXiv:2610.17737v1, Section 8.2, involves sign actions on ambient affine-space coordinates and fixed character multiplicities, not this global involution over \(C^{(2)}\). Monavari and Ricolfi (arXiv:2404.17942) analyze smoothness, motivic classes and torus-fixed loci of hyperquot schemes; those torus-fixed formulae do not state or imply the scheme-theoretic fixed components of the specified exchange involution without the new local comparison.

## Limitations
The theorem is restricted to the length-two Quot scheme of a trivial bundle over a smooth complex curve and to the particular exchange involution. It does not classify the fixed loci for other automorphisms, for arbitrary source bundles, or for larger lengths. The quotient statement is local and does not assert a global quotient presentation. Independent mathematical validation and exhaustive priority assessment have not been performed; implicit equivalent calculations in unlocated literature remain a possibility.

## References
- A. Bansal, S. Sarkar and S. Vats, *Torelli theorems for Quot schemes of vector bundles on curves*, arXiv:2609.14283v1 (first public version 2026-09-13), especially Sections 2.4 and 2.7 and Theorem B. https://arxiv.org/abs/2609.14283
- S. Monavari and A. T. Ricolfi, *Hyperquot schemes on curves: virtual class and motivic invariants*, arXiv:2404.17942. https://arxiv.org/abs/2404.17942
- *Dimensions and maximal-dimensional components of higher commuting varieties of symmetric pairs*, arXiv:2610.17737v1, especially Section 8.2. https://arxiv.org/abs/2610.17737
