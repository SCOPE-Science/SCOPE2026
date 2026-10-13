# Irreducible components of commuting tuples in the four-strand unitriangular group

## Finding
Let \(K\) be an algebraically closed field of **any** characteristic, and let \(r\geq2\). Let \(U_4(K)\) be the algebraic group of upper-unitriangular \(4\times4\) matrices. The reduced affine variety \(\mathcal C_r\) of ordered, pairwise commuting \(r\)-tuples in \(U_4(K)\) has exactly two irreducible components of dimension \(9\) when \(r=2\). It has exactly three components of dimensions \(4r\), \(3r+3\), and \(3r+3\) when \(r\geq3\). Thus, for \(r=3\), all three components are equidimensional; for \(r\geq4\), one is larger.

Here are explicit descriptions. Encode a tuple by six vectors \(a,d,f,b,e,c\in K^r\), giving the entries \((1,2),(2,3),(3,4),(1,3),(2,4),(1,4)\) of its constituent matrices. Put
\[
\mathcal A_r=\{a=f=0\},\qquad
\mathcal B_r=\overline{\{d\ne0,\ (a,f)\ne(0,0)\}\cap\mathcal C_r},\qquad
\mathcal D_r=\{d=0,\ a\wedge e+b\wedge f=0\}.
\]
For \(r\geq3\), the three components are \(\mathcal A_r,\mathcal B_r,\mathcal D_r\), respectively. For \(r=2\), they are \(\mathcal B_2,\mathcal D_2\), and \(\mathcal A_2\subset\mathcal B_2\).

## Assumptions and scope
An ordered tuple consists of \(r\) labelled group elements, not conjugacy classes or unordered sets. Coordinates are taken over an algebraically closed field, with no restriction on its characteristic. A component is a maximal irreducible closed subset of the **reduced underlying affine algebraic set**; no scheme-theoretic primary decomposition is asserted. The wedge is the exterior product in \(\bigwedge^2 K^r\). The central-entry vector \(c\) is unrestricted throughout.

## Proof
**1. Exact commuting equations.** Write each element as identity plus a strictly upper-triangular matrix. Two such group elements commute if and only if their strictly upper-triangular parts commute. Comparing the \((1,3),(2,4),(1,4)\) entries, pairwise commutation across all coordinates is equivalent to
\[
 a\wedge d=0,\qquad d\wedge f=0,\qquad a\wedge e+b\wedge f=0.
\tag{1}
\]
There are no other nonautomatic equations; \(c\) never appears. Equation (1) is valid even in characteristic \(2\).

**2. The stratum with \(d\ne0\).** Since \(d\) is a nonzero vector, the first two wedge equations uniquely give \(a=\alpha d\) and \(f=\varphi d\) for scalars \(\alpha,\varphi\). On the open set \((\alpha,\varphi)\ne(0,0)\), the last equation becomes
\[
\alpha e-\varphi b\in Kd.
\tag{2}
\]
For fixed \(d,\alpha,\varphi\), this is a linear condition of rank \(r-1\) on the \(2r\) entries of \((b,e)\). Hence the open stratum is a vector bundle of relative dimension \(r+1\), with additional unrestricted \(r\)-vector \(c\), over the irreducible base \((K^r\setminus\{0\})\times(K^2\setminus\{0\})\). It is irreducible, with dimension
\[
r+2+(r+1)+r=3r+3.
\]
Its closure \(\mathcal B_r\) is therefore irreducible of that dimension. It satisfies \(a\wedge f=0\) and all \(3\times3\) minors of the matrix \([d\ b\ e]\) vanish, because (2) makes these three vectors dependent. These closed restrictions also hold on its boundary.

**3. The stratum with \(d=0\).** We establish that \(\mathcal D_r\) is irreducible of dimension \(3r+3\). For any solution of \(a\wedge e+b\wedge f=0\), the span of \(a,b,e,f\) has dimension at most \(2\). Indeed, if \(a,f\) are independent, reducing modulo their two-dimensional span first forces \(b,e\) into that span; if they are dependent but not both zero, write \(a=\alpha u, f=\varphi u\) and use \(\alpha e-\varphi b\in Ku\); if both vanish the conclusion is immediate. Therefore these four vectors lie in some two-plane \(U\leq K^r\).

Consider the incidence variety over the Grassmannian \(\operatorname{Gr}(2,r)\) of choices of \(U\), with \(a,b,e,f\in U\) satisfying one scalar equation \(a\wedge e+b\wedge f=0\) in \(\bigwedge^2 U\). Its fiber is the irreducible seven-dimensional affine quadric in \(U^4\): in any basis its polynomial is \(a_1e_2-a_2e_1+b_1f_2-b_2f_1\), whose associated bilinear pairing has full rank and hence cannot factor into linear factors (also in characteristic \(2\)). The base and fibers are irreducible, so the incidence variety is irreducible. Projection onto the coordinates is surjective by the preceding span argument. Its image \(\{a\wedge e+b\wedge f=0\}\) is therefore irreducible. On the dense locus where \(a,f\) are independent, \(U\) is their span, so the projection is generically one-to-one. Its dimension is
\[
\dim\operatorname{Gr}(2,r)+7=2(r-2)+7=2r+3.
\]
Adding the free central vector \(c\) gives \(\dim \mathcal D_r=3r+3\). This includes \(r=2\), where the Grassmannian has one point.

**4. Covering.** If \(d=0\), a solution lies in \(\mathcal D_r\). If \(d\ne0\) and \((a,f)\ne(0,0)\), it belongs to the open dense stratum of \(\mathcal B_r\). All remaining solutions have \(a=f=0\), so lie in \(\mathcal A_r\). Thus
\[
\mathcal C_r=\mathcal A_r\cup\mathcal B_r\cup\mathcal D_r.
\tag{3}
\]
The linear family \(\mathcal A_r\) is irreducible of dimension \(4r\).

**5. Component distinction for \(r\geq3\).** The families in (3) are closed and irreducible. A point of \(\mathcal A_r\) with \(d,b,e\) independent is outside \(\mathcal B_r\); it is outside \(\mathcal D_r\) when \(d\ne0\). The dense open part of \(\mathcal B_r\) has \(d\ne0\) and at least one of \(a,f\) nonzero, so is in neither other family. Finally \(\mathcal D_r\) has points with independent \(a,f\), whereas \(a\wedge f=0\) on \(\mathcal B_r\) and \(a=f=0\) on \(\mathcal A_r\). Thus none of these three irreducible closed sets is contained in the union of the other two. They are exactly the maximal irreducible components.

**6. The exceptional pair case \(r=2\).** If \(a=f=0\) and \(d\ne0\), the one-dimensional quotient \(K^2/Kd\) forces the classes of \(b,e\) to be linearly dependent. Choose nonzero \((\alpha,\varphi)\) satisfying (2), then replace it by \((t\alpha,t\varphi)\) for nonzero \(t\) and send \(t\) to zero. This shows the given point is in \(\mathcal B_2\). If \(d=0\) and \(a=f=0\), choose \(u=b\) when \(b\ne0\), and any nonzero \(u\) otherwise; the family \(d=tu, a=0,f=tu\), with \(b,e,c\) fixed, lies in the open stratum of \(\mathcal B_2\) for \(t\ne0\) and approaches the given point. Hence \(\mathcal A_2\subset\mathcal B_2\). By (3), \(\mathcal C_2=\mathcal B_2\cup\mathcal D_2\); the two irreducible sets are distinct, since the former has points with \(d\ne0\) and the latter has points with independent \(a,f\). Both have dimension \(9\). This completes the proof.

## Verification
The standalone script `verify.py` independently enumerates the noncentral coordinate vectors and checks the wedge equations and finite-field counts. It verifies all \(2^{5r}\) five-vector assignments for \(r=1,2,3,4\) over \(\mathbb F_2\), and all \(3^{10}\) assignments for \(r=2\) over \(\mathbb F_3\), grouping results only after testing the exact equations. The resulting full commuting-tuple counts are, respectively, \(64,1024,12160,138496,41553\). It also checks all \(1024\) ordered noncentral matrix-pair products over \(\mathbb F_2\) directly.

For reference, counting the cases \(d\ne0\), \(d=0\) with \(\dim\langle a,f\rangle=0,1,2\), gives the finite-field identity
\[
\#\mathcal C_r(\mathbb F_q)=q^r\bigl[q^{3r}+(q+1)q^{r+2}(q^r-1)+q^3(q^r-1)(q^r-q)\bigr].
\]
This identity supplies a cross-check on the defining equations, but finite enumeration is **not** a proof of the irreducible-component classification. The latter follows from the geometric argument above.

## Relationship to prior work
Majeed and Ramkumar (arXiv:2608.09235, first submitted August 10, 2026) study the commuting graph of the same group over prime fields and provide explicit two-element commutation relations. The graph invariants in their abstract do not supply the all-length component classification above; full text was not accessible during the comparison. Kaur, Sharma, and Singh (arXiv:2006.01493v1) compute branching rules for commuting tuples in finite unitriangular groups of odd characteristic. These yield finite-field tuple counts, so **counting commuting tuples alone is not asserted as the original contribution**. Li (arXiv:2403.13953v3) proves a complete-intersection statement for the commuting-pair scheme of the four-strand group in characteristic zero, but does not state the all-length component classification. Levy, Ngo, and Šivic (doi:10.1112/jlms.12650) treat tuple varieties in the full nilpotent cone, rather than the fixed strictly-upper-triangular subgroup. Basili (doi:10.1080/00927872.2016.1178272) studies pairs of upper-triangular matrices; that setup alone does not imply the classification for every number of matrices.

## Limitations
The theorem classifies **reduced irreducible components**, not scheme structures, primary ideals, multiplicities, singular strata, or cohomology. It does not claim the finite-field count is historically new. Exact historical equivalence under a different matrix-variety formulation remains a possibility, especially because the full 2026 motivating preprint could not be accessed; no independent validation has been performed.

## References
1. M. Majeed and P. B. Ramkumar, *Commuting Graph of Unitriangular Group UT(4; p)*, arXiv:2608.09235v1 (2026-08-10), https://arxiv.org/abs/2608.09235.
2. D. Kaur, U. B. Sharma, and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1 (2020), https://arxiv.org/html/2006.01493v1.
3. G. Li, *Commuting Schemes of Upper Triangular Matrices and Representation Homology*, arXiv:2403.13953v3, https://arxiv.org/pdf/2403.13953.
4. P. D. Levy, N. V. Ngo, and K. Šivic, *Commuting varieties and cohomological complexity theory*, J. London Math. Soc. (2022), https://doi.org/10.1112/jlms.12650.
5. R. Basili, *On commuting varieties of upper triangular matrices*, Commun. Algebra 45 (2017), https://doi.org/10.1080/00927872.2016.1178272.
