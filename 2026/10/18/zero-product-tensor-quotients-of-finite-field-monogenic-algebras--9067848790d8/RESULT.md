# Zero-product tensor quotients of finite-field monogenic algebras are products of fat plane jets

## Finding
Let \(K=\mathbb F_q\), where \(q\) is any **odd** prime power. Take a nonconstant monic polynomial
\[f=\prod_{i=1}^{r}f_i^{e_i}\in K[t],\qquad d_i=\deg(f_i),\quad e_i\ge1,\]
where the \(f_i\) are distinct monic irreducibles. Put \(A=K[t]/(f)\) and
\[Z(A)=\operatorname{span}_K\{a\otimes b\in A\otimes_K A:ab=0\}.\]
Then \(Z(A)\) is an ideal in the commutative tensor-product algebra, and there is a noncanonical isomorphism of \(K\)-algebras
\[
\boxed{(A\otimes_K A)/Z(A)\cong\prod_{i=1}^{r}\left(\mathbb F_{q^{d_i}}[u,v]/(u,v)^{e_i}\right)^{d_i}.}
\]
A superscript \(d_i\) outside parentheses denotes a product of \(d_i\) copies, not a power of an element. Every factor is a two-variable fat-point jet ring, of length \(e_i(e_i+1)/2\) over its coefficient field.

Let \(\mathcal B_0(A)\) be the vector space of all \(K\)-bilinear forms \(\beta:A\times A\to K\) satisfying \(\beta(a,b)=0\) whenever \(ab+ba=0\). Set
\[
N=\deg(f)=\sum_i d_i e_i,\qquad
D=\sum_i\frac{d_i^2e_i(e_i+1)}2,\qquad
\delta=D-N.
\]
Because \(A\) is commutative and \(2\) is invertible, \(ab+ba=0\) is equivalent to \(ab=0\). There are exactly \(q^D\) such bilinear forms. Precisely \(q^N\) arise as \(\beta(a,b)=\lambda(ab)\) for some \(\lambda\in A^*\), so their proportion within \(\mathcal B_0(A)\) is \(q^{-\delta}\). Moreover
\[
\boxed{\delta=0\ \Longleftrightarrow\ f\text{ splits into distinct linear factors over }K.}
\]
Thus the factorization degrees and nilpotent thicknesses control the **complete** space of zero-Jordan-product-vanishing bilinear forms, rather than merely whether all such forms factor through multiplication.

## Assumptions and scope
All tensor products, linear spans, duals and dimensions are taken over \(K\). The polynomial \(f\) is nonconstant and monic; repeated factors are allowed. The algebra \(A\) is commutative, associative, unital and finite-dimensional. The algebra isomorphism is not claimed canonical because it uses choices of residue-field lifts and a decomposition of finite-field tensor products. The Jordan interpretation requires odd characteristic; the tensor-quotient calculation itself works in characteristic two as well when the condition is \(ab=0\).

## Proof
**1. Zero-product tensors generate an ideal.** If \(ab=0\), then for arbitrary \(c,d\in A\), the product \((a\otimes b)(c\otimes d)=ac\otimes bd\) also has zero multiplication image, since \((ac)(bd)=abcd=0\). By bilinearity, the span \(Z(A)\) is an ideal.

**2. Reduction to local factors.** The Chinese remainder theorem supplies mutually orthogonal central idempotents and an algebra decomposition
\[A\cong\prod_{i=1}^{r} A_i,\qquad A_i=K[t]/(f_i^{e_i}).\]
The tensor algebra is the product of blocks \(A_i\otimes_K A_j\). For \(i\ne j\), every supported pure tensor \(a_i\otimes b_j\) has product zero in \(A\); hence every off-diagonal block lies in \(Z(A)\). In the diagonal block, the projection of \(Z(A)\) is exactly the span of \(a_i\otimes b_i\) with \(a_i b_i=0\), as follows by checking each component of \(ab=0\) and by extending supported factors by zero. Therefore it is enough to compute the ideal \(Z(A_i)\) for one primary factor.

**3. Splitting one primary factor.** Fix \(i\), write \(d=d_i\), \(e=e_i\), \(L=\mathbb F_{q^d}\), and let \(\alpha\) be the image of \(t\) in \(L=K[t]/(f_i)\). Irreducibility over a finite field implies \(f_i'(\alpha)\ne0\). The simple root \(\alpha\) lifts in the nilpotent thickening \(A_i\twoheadrightarrow L\), so \(L\) embeds as a coefficient field in \(A_i\). Set \(u=t-\widetilde\alpha\) inside \(A_i\). The factorization
\[f_i(t)=f_i(\widetilde\alpha+u)=u\,g(u),\qquad g(0)=f_i'(\widetilde\alpha)\ne0\]
shows that \(u\) has exact nilpotency order \(e\). Comparing \(K\)-dimensions yields an algebra isomorphism
\[A_i\cong L[u]/(u^e).\]
This is a finite-length form of separable Hensel lifting, requiring no completion or extension of scalars outside \(A_i\).

**4. Exact local zero-product ideal.** Under this presentation,
\[A_i\otimes_K A_i\cong(L\otimes_K L)[u,v]/(u^e,v^e),\]
where \(u=u\otimes1\) and \(v=1\otimes u\). Any nonzero \(a\in A_i\) is uniquely of the form \(a=u^s a_0\), where \(0\le s<e\) and \(a_0\) is a unit; similarly \(b=u^t b_0\). Hence \(ab=0\) if and only if \(s+t\ge e\). In that case \(a\otimes b\) belongs to the ideal \((u,v)^e\). Conversely, each monomial \(u^s v^t\) with \(s+t\ge e\) is the zero-product pure tensor \(u^s\otimes u^t\), and multiplication by arbitrary coefficient tensors keeps it in \(Z(A_i)\). Consequently
\[Z(A_i)=(u,v)^e\quad\text{inside }A_i\otimes_K A_i.\]
The criterion is valid for zero factors as well, using valuation \(e\) for zero.

**5. Finite-field tensor splitting.** The separable extension \(L/K\) is cyclic Galois of degree \(d\), so
\[L\otimes_K L\cong\prod_{\sigma\in\operatorname{Gal}(L/K)}L\cong L^d.\]
Combining this with step 4 gives
\[(A_i\otimes_K A_i)/Z(A_i)\cong\left(L[u,v]/(u,v)^e\right)^d,\]
and combining all diagonal blocks gives the claimed product of jet rings.

**6. Counting and the sharp vanishing criterion.** Monomials \(u^s v^t\) with \(s,t\ge0\) and \(s+t<e\) form an \(L\)-basis of \(L[u,v]/(u,v)^e\), of cardinality \(e(e+1)/2\). Each of the \(d\) copies contributes \(d\,e(e+1)/2\) dimensions over \(K\). Summing gives \(D\).

The bilinear forms vanishing on zero products are canonically the dual of \((A\otimes_K A)/Z(A)\). This identifies the vector space and gives exactly \(q^D\) forms. Multiplication \(m:A\otimes_K A\to A\) is surjective because \(m(1\otimes a)=a\), and \(Z(A)\subseteq\ker m\). Thus its dual injects \(A^*\) as an \(N\)-dimensional subspace of \(\mathcal B_0(A)\). The count, codimension and proportion follow. Finally, each local summand
\[\frac{d^2e(e+1)}2-de=de\left(\frac{d(e+1)}2-1\right)\]
is nonnegative and vanishes precisely when \(d=e=1\), yielding the equivalence for \(\delta=0\). This completes the proof.

## Verification
An independent finite-field linear algebra program, `verify.py`, constructs \(A\) from explicit monic polynomials, enumerates **every** pair \((a,b)\in A^2\) over small prime fields, forms all pure tensors with zero product, and computes their exact span rank by modular Gaussian elimination. Fourteen test configurations passed. They include irreducible quadratic residue fields, repeated quadratic factors, mixtures of distinct factors, and characteristics two, three and five. This finite enumeration checks small instances of the formula; the proof above establishes all finite fields and all polynomial degrees.

For example, \(K=\mathbb F_3\) and \(f=(t^2+1)^2\) give \(d=2\), \(e=2\), \(N=4\), \(D=12\), \(\delta=8\): the universal quotient is two copies of \(\mathbb F_9[u,v]/(u,v)^2\), and only the proportion \(3^{-8}\) of qualifying bilinear forms factors through multiplication. In contrast, for \(f=t(t-1)\), all such forms factor through multiplication.

To reproduce the checks, run `python3 verify.py` with Python 3.8 or later. The program uses only the standard library and prints `VERIFY_OK 14 exhaustive configurations` on success.

## Relationship to prior work
Jia and Xiao (2026, arXiv:2607.05941v1) prove a qualitative characterization: a finite-dimensional unital algebra in odd characteristic is zero Jordan product determined precisely when its algebra is generated by idempotents. For the commutative algebras studied here, this decides only whether \(\delta=0\); it does not specify the exact obstruction vector space or universal quotient.

Brešar's earlier finite-dimensional zero-product work gives the analogous qualitative criterion and recognizes the general span of pure zero-product tensors. Gardella and Thiel's work on zero-product balanced algebras defines the universal tensor quotient and relates it to zero-product determined properties. Those foundational constructions are explicitly used and are **not** claimed as novel. The present computation instead identifies the quotient as a product of fat two-variable jets, determining the complete dimension and the exact number of bilinear forms for every finite-field monogenic quotient. Searches for equivalent local-algebra, tensor, and zero-product-preserver formulations found no published formula establishing this precise family-wide decomposition; this negative search result is not proof of uniqueness.

## Limitations
This theorem concerns only monogenic finite commutative algebras, not arbitrary finite-dimensional algebras or multilinear forms. Its Jordan interpretation is restricted to odd characteristic; in characteristic two, \(ab+ba\) is identically zero and is not equivalent to \(ab=0\). The jet decomposition is noncanonical. An equivalent enumeration under a different tensor-ideal or local-ring terminology may exist outside the inspected literature; no independent mathematical audit has been performed.

## References
1. H. Jia and Z. Xiao, *Finite dimensional zero Jordan product determined algebras are generated by idempotents*, arXiv:2607.05941v1, publicly posted 7 July 2026; https://arxiv.org/abs/2607.05941.
2. M. Brešar, *Finite dimensional zero product determined algebras are generated by idempotents*, *Expositiones Mathematicae* 34 (2016); author's available manuscript: https://users.fmf.uni-lj.si/bresar/documents/zpdidemp.pdf.
3. E. Gardella and H. Thiel, *Zero-product balanced algebras*, *Linear Algebra and its Applications* (2023); arXiv:2210.07891, https://arxiv.org/abs/2210.07891.
