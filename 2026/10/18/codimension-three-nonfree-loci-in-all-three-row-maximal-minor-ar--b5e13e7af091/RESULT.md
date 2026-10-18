# Codimension-three nonfree loci in all three-row maximal-minor arrangements

## Finding
For every integer \(n\ge5\), let \(V_n=\mathbf A^{3n}_{\mathbf C}\) parametrize ordered complex three-by-\(n\) matrices \(M\), and define the reduced divisor \(D_{3,n}=V(f_n)\) by
\[
f_n(M)=\prod_{\substack{I\subset\{1,\ldots,n\}\\|I|=3}}\det(M_I).
\]
Here \(M_I\) denotes the three-column submatrix indexed by \(I\). For every set \(J\subset\{1,\ldots,n\}\) with \(|J|=5\), put
\[
Z_J=\{M\in V_n:\operatorname{rank}(M_J)\le2\}.
\]
Then **every \(Z_J\) is contained in the nonfree locus of \(D_{3,n}\)**. Each \(Z_J\) is an irreducible subvariety of codimension three. Furthermore, there is a nonempty dense Zariski-open subset \(W_J\subset Z_J\) on which the logarithmic derivation stalk requires exactly \(3n+1\) generators, although it has generic rank \(3n\).

Consequently, the full maximal-minor divisor \(D_{3,n}\) is nonfree for every \(n\ge5\), confirming the entire three-row slice of the nonfreeness part of the conjecture of Janasz (Conjecture 7.4). For every \(n\ge6\), the nonfree locus meets the **full-rank matrix stratum** in codimension three. In contrast, \(D_{3,5}\) is free on its full-rank stratum, as the source establishes.

## Assumptions and scope
All varieties and local analytic rings are over \(\mathbf C\); \(n\) is an arbitrary integer at least five. Freeness refers to local freeness of the logarithmic derivation sheaf \(\operatorname{Der}_{V_n}(-\log D_{3,n})\), not to singularity or smoothness of the individual determinant hypersurfaces. We use the published Theorem B(3) of Janasz (2026), which gives exactly \(16\) minimal generators for the logarithmic derivation stalk of \(D_{3,5}\) at any rank-two matrix. This source theorem is a computationally supported external premise; the new extension is proved formally below.

For a five-element subset \(J\), define \(W_J\) inside \(Z_J\) by the two requirements \(\operatorname{rank}(M_J)=2\) and \(\det(M_I)\ne0\) for every three-element index set \(I\) not contained in \(J\). These are algebraic open conditions.

## Proof
**1. The basic codimension-three locus and its nonempty open part.** Because the standard determinantal rank-at-most-two locus in \(\mathbf A^{3\cdot5}\) is irreducible of codimension \((3-2)(5-2)=3\), its inverse image under the coordinate projection \(V_n\to\mathbf A^{15}\) is exactly the irreducible codimension-three variety \(Z_J\).

Permute columns to take \(J=\{1,\ldots,5\}\). Choose five vectors in the plane \(z=0\) of the form \(v_j=(1,j-1,0)^T\), for \(1\le j\le5\). They span a plane, and every two are independent. Choose the remaining vectors successively, generically in \(\mathbf C^3\). Each determinant containing an added column is a nonzero polynomial in the additional column coordinates: if it contains two distinguished columns, this follows from their independence; if it contains at most one, choose the other independent vectors to complete a basis. Because there are finitely many such determinant polynomials, their common nonvanishing open is nonempty over the infinite field \(\mathbf C\). Thus \(W_J\) is nonempty. Since \(Z_J\) is irreducible, it is also dense. For \(n\ge6\), any matrix in \(W_J\) has full matrix rank three, since a mixed three-by-three minor is nonzero.

**2. Exact local product.** Fix \(p\in W_J\). Every determinant whose three-column index set is not contained in \(J\) is nonzero at \(p\), hence is a unit in the analytic local ring \(\mathcal O_{V_n,p}\). Writing \(\pi_J:V_n\to\mathbf A^{15}\) for the five-column projection, the complete defining product satisfies locally
\[
f_n=u\cdot (f_5\circ\pi_J),\qquad u\in\mathcal O_{V_n,p}^{\times}.
\]
Multiplication by a unit does not change the logarithmic derivation sheaf. Because the extra \(3(n-5)\) coordinates are independent smooth parameters, the divisor germ is the product of the germ of \(D_{3,5}\) at \(\pi_J(p)\) with a smooth affine factor of dimension \(3(n-5)\). Consequently, with local stalks understood, 
\[
\operatorname{Der}(-\log D_{3,n})_p\cong
\bigl(\operatorname{Der}(-\log D_{3,5})_{\pi_J(p)}\widehat\otimes\mathcal O_{V_n,p}\bigr)
\oplus\mathcal O_{V_n,p}^{\,3(n-5)}.
\]
Here the completed tensor notation encodes the analytic smooth extension, without asserting a global module decomposition. Freeness and the minimal number of local generators are preserved under this faithfully flat smooth extension, apart from the exactly added free summand.

**3. One extra generator.** The five-column submatrix \(\pi_J(p)\) has rank two. Theorem B(3) of Janasz gives \(\mu=18-2=16\) for its rank-fifteen logarithmic derivation stalk. By the decomposition just established and Nakayama's lemma,
\[
\mu\bigl(\operatorname{Der}(-\log D_{3,n})_p\bigr)
=16+3(n-5)=3n+1.
\]
Its generic rank is \(3n\). A locally free sheaf of that rank would need exactly \(3n\) generators over the local ring. Hence \(D_{3,n}\) is nonfree at every \(p\in W_J\).

**4. Passing from an open locus to all of \(Z_J\).** The locally free locus of a coherent sheaf is Zariski-open; the complement, the nonfree locus of \(D_{3,n}\), is Zariski-closed. Since this closed locus contains the dense subset \(W_J\) of the irreducible \(Z_J\), it contains all of \(Z_J\). This holds for each \(J\), proving the claimed union of codimension-three nonfree subvarieties. The special case \(n=5\) is Janasz's theorem; for \(n\ge6\), step 1 ensures a nonfree point of full matrix rank. \(\square\)

## Verification
The companion file `verify.py` (Python standard library only) performs exact integer determinant checks of the five-column rank-two construction for \(n=6,7,8,9,10\) and of the particularly simple six-column witness with first five columns \((1,j,0)^T\), \(j=0,\ldots,4\), and last column \((0,0,1)^T\). It verifies that precisely the ten minors using only the distinguished five columns vanish, while every other maximal minor is nonzero. It also checks the arithmetic identity for the claimed number of local generators. The infinite theorem does not follow from these finite checks; it follows from the generic-open proof and the source's Theorem B(3).

## Relationship to prior work
Janasz, *Geometry of some determinantal arrangements* (first arXiv version, October 9, 2026), Theorem B, established the full \(D_{3,5}\) logarithmic derivation module, and Table 1 separately recorded nonfreeness of \(D_{3,6}\) using a rank-two chart. Its Conjecture 7.4 still proposed nonfreeness for arbitrary widths. The present result uses its five-column theorem as an external input to settle every width at once and locates nonfreeness on full-rank matrices for widths at least six; neither the table of finite cases nor the stated conjecture gives those conclusions. Yim's earlier work establishes the two-row case and posed the general freeness question. Janasz and Wiśniewska (2023) treat selected subproducts for five columns, not the all-maximal-minor arrangement for arbitrary width.

## Limitations
This is a theorem for **three-row** matrices over \(\mathbf C\); it does not resolve the remaining higher-row instances of Conjecture 7.4 or completely classify the nonfree locus outside the asserted union. The rank-three phenomenon is proved on explicit nonempty dense open strata, while closedness extends the nonfreeness assertion to all of each \(Z_J\). The local generator formula is asserted only on \(W_J\), not on its boundary. The source's Theorem B(3), including its computer-assisted calculation of the five-column module, is used as published mathematical input and was not independently recomputed here. An unindexed equivalent formulation in other literature cannot be excluded by bibliographic searches alone.

## References
1. M. Janasz, *Geometry of some determinantal arrangements*, arXiv:2610.13291v1 (October 9, 2026), Theorem B(3), Lemma 2.1(d), Table 1, Conjecture 7.4. https://arxiv.org/html/2610.13291v1
2. A. Yim, *Homological Properties of Determinantal Arrangements*, arXiv:1506.05145 (2015), published in Journal of Algebra 471 (2017), 220–239. https://arxiv.org/abs/1506.05145
3. M. Janasz and P. Wiśniewska, *A note on free determinantal hypersurface arrangements in \(\mathbf P^{14}_{\mathbf C}\)*, Proyecciones 42 (2023), 1093–1104. https://doi.org/10.22199/issn.0717-6279-5780
