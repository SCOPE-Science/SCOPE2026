# Zero-product bilinear forms on socle-degree-two Gorenstein algebras

## Finding

Let \(k\) be any field, let \(d\ge 2\), and let \(\beta:V\times V\to k\) be a nondegenerate symmetric bilinear form on a \(d\)-dimensional vector space. Consider the unital commutative graded algebra
\[
A=k1\oplus V\oplus kz,\qquad uv=\beta(u,v)z,\qquad zV=z^2=0.
\]
Define \(\mathcal Z(A)\) to be the vector space of \(k\)-bilinear maps \(F:A\times A\to k\) such that \(F(x,y)=0\) whenever \(xy=0\). **Every** such form is uniquely
\[
F(s1+u+tz,\ s'1+v+t'z)
=a ss'+s\ell(v)+s'r(u)+c st'+e ts'+\lambda\beta(u,v),
\]
with arbitrary \(a,c,e,\lambda\in k\) and \(\ell,r\in V^*\). Consequently
\[
\dim_k\mathcal Z(A)=2d+4.
\]
The forms \(F(x,y)=\varphi(xy)\), \(\varphi\in A^*\), have dimension \(d+2\). They are exactly the displayed forms for which \(\ell=r\) and \(c=e=\lambda\). All symmetric members of \(\mathcal Z(A)\) have \(\ell=r\) and \(c=e\), so
\[
\dim_k\mathcal Z(A)^{\mathrm{sym}}=d+3,\qquad
\dim_k\bigl(\mathcal Z(A)^{\mathrm{sym}}/\{\varphi\circ m:\varphi\in A^*\}\bigr)=1,
\]
where \(m(x,y)=xy\). More generally the unrestricted quotient has dimension \(d+2\).

When \(k=\mathbb F_q\), a form in the normal form is nondegenerate exactly when \(ce\lambda\ne0\). The exact numbers of nondegenerate zero-product forms and nondegenerate symmetric zero-product forms are, respectively,
\[
q^{2d+1}(q-1)^3,\qquad q^{d+1}(q-1)^2.
\]
Of the symmetric forms, precisely \(q^{d+1}(q-1)\) are nondegenerate product-factor forms, leaving
\[
q^{d+1}(q-1)(q-2)
\]
nondegenerate symmetric forms that do not factor through multiplication. Thus the last type exists over every finite field except \(\mathbb F_2\). These formulas do not depend on the isometry class of \(\beta\).

## Assumptions and scope

The algebra is defined from a **nondegenerate symmetric** \(\beta\); the result includes characteristic two, including alternating and nonalternating symmetric forms. Its unique maximal ideal is \(\mathfrak m=V\oplus kz\), with \(\mathfrak m^2=kz\), \(\mathfrak m^3=0\), and socle \(kz\). Thus it is a standard graded commutative Artinian Gorenstein algebra with Hilbert vector \((1,d,1)\). Conversely every such graded algebra with fixed coefficient-field splitting arises from a nondegenerate symmetric form by its degree-one multiplication. The statement concerns **scalar-valued bilinear forms**; no claims are made about nonlinear maps or every higher-socle-degree algebra. For characteristic different from two, zero products here coincide with zero Jordan products for this commutative algebra; this identification is **not** made in characteristic two.

## Proof

**Step 1 (zero-product pairs).** The elements with a nonzero coefficient of \(1\) are units because \(\mathfrak m\) is nilpotent. Therefore, if \(xy=0\) and both \(x,y\ne0\), both lie in \(\mathfrak m\). For \(u+tz,v+t'z\in\mathfrak m\), their product is \(\beta(u,v)z\). Hence zero products in the maximal ideal are exactly the pairs satisfying \(\beta(u,v)=0\).

**Step 2 (forced coefficients).** Since \(z\mathfrak m=0\), any \(F\in\mathcal Z(A)\) obeys \(F(z,z)=F(z,V)=F(V,z)=0\). Write \(b=F|_{V\times V}\). Then \(b(u,v)=0\) whenever \(\beta(u,v)=0\). For nonzero \(u\), the functional \(b(u,-)\) vanishes on the hyperplane \(u^\perp=\ker\beta(u,-)\). Thus there exists \(\lambda_u\in k\) with \(b(u,-)=\lambda_u\beta(u,-)\). If \(u,w\) are independent, nondegeneracy makes \(\beta(u,-)\) and \(\beta(w,-)\) independent. Comparing \(b(u+w,-)\) with \(b(u,-)+b(w,-)\) gives \(\lambda_u=\lambda_w=\lambda_{u+w}\). Dependent nonzero vectors also have the same scalar by bilinearity. Because \(d\ge2\), this yields one scalar \(\lambda\) for all nonzero \(u\), so \(b=\lambda\beta\). No other coefficients are constrained by zero products, proving both necessity and sufficiency of the normal form, uniqueness, and \(\dim\mathcal Z(A)=2d+4\).

**Step 3 (factorization and symmetry).** For \(\varphi\in A^*\), expanding \(\varphi(xy)\) in the direct decomposition gives \(a=\varphi(1)\), \(\ell=r=\varphi|_V\), and \(c=e=\lambda=\varphi(z)\). Conversely those equations exactly characterize factorization. As \(1\) is a unit, \(\varphi\mapsto\varphi\circ m\) is injective. Symmetry imposes \(\ell=r\) and \(c=e\), with no additional condition because \(\beta\) is symmetric. This proves the dimensions and the one-dimensional symmetric obstruction.

**Step 4 (nondegenerate counts).** Choose a basis of \(V\), with invertible symmetric Gram matrix \(B\). The matrix of \(F\), ordered by \((1,V,z)\), is
\[
\begin{pmatrix}
a&\ell&c\\ r&\lambda B&0\\ e&0&0
\end{pmatrix}.
\]
Expanding first along the last row and then along the last column gives
\[
\det F=-ce\lambda^d\det B
\]
(the sign is irrelevant). Thus \(F\) is nondegenerate exactly when \(c,e,\lambda\ne0\). There are \(2d+1\) unrestricted field coordinates \((a,\ell,r)\), yielding \(q^{2d+1}(q-1)^3\) forms. A symmetric form has \(c=e\) and \(\ell=r\), giving \(q^{d+1}(q-1)^2\). A symmetric factor form requires \(c=e=\lambda\), giving \(q^{d+1}(q-1)\) nondegenerate possibilities, and subtraction establishes the sharp \(q=2\) boundary.

**Step 5 (tensor interpretation).** Let \(Z_2(A)\subset A\otimes_k A\) be the span of tensors \(x\otimes y\) with \(xy=0\). By linear duality, \(\mathcal Z(A)=((A\otimes A)/Z_2(A))^*\). Consequently
\[
\dim_k Z_2(A)=d^2+2d,\quad
\dim_k\bigl(\ker(m:A\otimes A\to A)/Z_2(A)\bigr)=d+2.
\]
Here the tensor map is surjective because the algebra is unital. The latter equals the unrestricted zero-product-determination defect, matching Step 3.

## Verification

The standalone standard-library Python script `verify.py` derives the zero-product tensor constraints from multiplication, computes their ranks, verifies the proposed parameter basis and the product-factor and symmetric subspace dimensions, and enumerates all candidate parameters to test nonsingularity. It checks \((q,d)=(2,2),(3,2),(2,3)\). Running `python3 verify.py` in the package directory prints `VERIFY_OK`. These are finite consistency tests; arbitrary-field validity follows from the preceding proof.

## Relationship to prior work

Jia and Xiao (2026), Theorem 1.2 and Lemma 2.5, show a qualitative criterion for finite-dimensional zero Jordan product determined algebras in characteristic different from two and construct a nonsymmetric obstruction for nontrivial local algebras. Their full seven-page preprint does **not** state the normal form, the uniform one-dimensional symmetric defect, or the finite-field nondegeneracy counts above. The local nonsymmetric obstruction itself is **not claimed as new**. Gardella and Thiel (2023) establish the general zero-product tensor quotient framework used in Step 5, but their structural results and examples do not give the displayed family-wide computations. These broad prior criteria do not imply the exact new multiplicities without the normal-form analysis. Earlier classifications of orthogonality-preserving bilinear maps, possibly under different terminology, remain a historical overlap risk.

## Limitations

The classification is for a fixed split graded \((1,d,1)\) Gorenstein algebra and scalar-valued bilinear maps. It does not classify arbitrary zero-product preserving (possibly nonlinear) maps; nor does it extend automatically to degenerate \(\beta\), other Hilbert vectors, or characteristic-two Jordan-zero products. Exhaustive enumeration verifies only the three finite prime-field cases stated above. Literature searches cannot establish absolute novelty; equivalent older orthogonality-preserver formulations remain possible.

## References

1. H. Jia and Z. Xiao, *Finite dimensional zero Jordan product determined algebras are generated by idempotents*, arXiv:2607.05941v1, 7 July 2026; Theorem 1.2 and Lemma 2.5. https://arxiv.org/abs/2607.05941
2. E. Gardella and H. Thiel, *Zero-product balanced algebras*, Linear Algebra and its Applications **670** (2023), 121–153, DOI:10.1016/j.laa.2023.04.015; especially Definition 2.1, Proposition 2.4, and Examples 2.16–2.17. https://research.chalmers.se/publication/535620/file/535620_Fulltext.pdf
