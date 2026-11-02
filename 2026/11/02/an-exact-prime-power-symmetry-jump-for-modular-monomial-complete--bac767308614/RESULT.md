# An exact prime-power symmetry jump for modular monomial complete intersections

## Finding

Fix a prime \(p\), a positive integer \(f\), and \(q=p^f\). For any integers \(d\ge2\), \(e\ge1\), let \(h=p^e\) and write
\[
A_n=\mathbb F_q[x_1,\ldots,x_d]/(x_1^n,\ldots,x_d^n),\qquad
\mathfrak m_n=(x_1,\ldots,x_d)A_n.
\]
Let \(\tau_n:\operatorname{Aut}_{\mathbb F_q}(A_n)\to\operatorname{GL}(\mathfrak m_n/\mathfrak m_n^2)\cong\operatorname{GL}_d(q)\) denote the tangent representation. Then:

**Prime-power exponent.** \(\tau_h\) is onto \(\operatorname{GL}_d(q)\). Arbitrary \(d\) elements of \(\mathfrak m_h\) give an automorphism precisely when their linear coefficient matrix is invertible. Therefore
\[
|\operatorname{Aut}_{\mathbb F_q}(A_h)|=|\operatorname{GL}_d(q)|\,q^{d(h^d-d-1)},
\qquad |\operatorname{GL}_d(q)|=\prod_{j=0}^{d-1}(q^d-q^j).
\]

**Immediately succeeding exponent.** \(\tau_{h+1}\) has image exactly the invertible monomial matrices \((\mathbb F_q^\times)^d\rtimes S_d\). Every automorphism is, uniquely at the image level, a substitution
\[
x_i\longmapsto x_{\sigma(i)}u_i\quad(1\le i\le d),
\]
where \(\sigma\in S_d\), \(u_i\in A_{h+1}^{\times}\), and different choices of units defining the same images are identified. Conversely every such substitution is an automorphism. Its order is
\[
|\operatorname{Aut}_{\mathbb F_q}(A_{h+1})|
=d!(q-1)^d q^{d(h(h+1)^{d-1}-1)}.
\]
In particular, the dimension of the permitted linear symmetry group falls sharply from full general linear to monomial at two consecutive exponents, even though both rings have the same embedding dimension \(d\).

## Assumptions and scope

The ground field is the finite field \(\mathbb F_q\), where \(q\) is a power of the same prime \(p\) appearing in \(h=p^e\). The variables commute; the truncated monomials with individual exponents less than \(n\) are a basis. The statement concerns **algebra automorphisms fixing the ground field**, not derivations, abstract group automorphisms, or automorphism group schemes over nonreduced base rings. The exponent \(e\) is positive, so \(h\ge2\). The count is of distinct substitutions, not of choices of representing units.

## Proof

**1. Invertibility is detected on tangent space.** Every algebra automorphism preserves the unique maximal ideal \(\mathfrak m_n\). Conversely, any \(d\) images in \(\mathfrak m_n\) respecting the defining relations determine an algebra endomorphism. If their images in \(\mathfrak m_n/\mathfrak m_n^2\) are a basis, the endomorphism is surjective: its images generate the maximal ideal by the finite-dimensional Nakayama lemma, so together with constants they generate the algebra. A surjective endomorphism of a finite-dimensional vector space is invertible.

**2. Exponent \(h\).** In characteristic \(p\), the \(h\)-th power map is additive. Every monomial belonging to \(\mathfrak m_h\) has at least one positive exponent; its \(h\)-th power therefore has some exponent at least \(h\) and vanishes. Thus \(f^h=0\) for all \(f\in\mathfrak m_h\). There are no restrictions on a substitution beyond invertibility of its linear coefficient matrix. The \(\mathbb F_q\)-dimension of \(\mathfrak m_h\) is \(h^d-1\). Once \(d\) linear coefficients of each image are fixed, \(h^d-d-1\) coefficients remain free. Multiplying by the number of invertible linear matrices proves the first count.

**3. Linear rigidity at exponent \(h+1\).** Let \(f\in\mathfrak m_{h+1}\) obey \(f^{h+1}=0\), and write \(f=\ell+r\) with linear part \(\ell=\sum_i a_i x_i\) and \(r\in\mathfrak m_{h+1}^2\). Since the Frobenius power of \(r\) has total degree at least \(2h\), the homogeneous part of total degree \(h+1\) of \(f^hf\) equals
\[
\ell^h\ell=\sum_{i,j} a_i^h a_j x_i^h x_j.
\]
Terms with \(i=j\) vanish. For \(i\ne j\), the monomials \(x_i^h x_j\) survive and are pairwise distinct, because \(h\ge2\). Hence \(a_i^h a_j=0\) for every ordered pair \(i\ne j\). Each nonzero tangent vector of an admissible image is therefore supported on exactly one coordinate. In an invertible tangent matrix these coordinates must be different across the \(d\) generators, so the matrix is monomial.

**4. No off-coordinate terms.** Fix a generator image \(f\) whose nonzero linear coefficient is \(a x_j\). Write uniquely \(f=x_j u+b\), where \(u\) has constant coefficient \(a\ne0\), and \(b\) involves only variables other than \(x_j\), with no terms of degree less than two. Suppose \(b\ne0\); let \(s\ge2\) be its smallest total degree and \(b_s\) its nonzero degree-\(s\) homogeneous part. By Frobenius,
\[
f^{h+1}=x_j^h u^h b+b^h x_j u+b^{h+1}.
\]
The first summand has degree-\((h+s)\) initial part \(a^h x_j^h b_s\), which is nonzero since each monomial of \(b_s\) has all exponents at most \(h\) and avoids \(x_j\). The other summands have total degree at least \(hs+1\) and \((h+1)s\), respectively; both exceed \(h+s\) because \(h,s\ge2\). Cancellation is impossible. Thus \(b=0\), and \(f=x_j u\) is divisible by its unique tangent coordinate. Conversely \((x_j u)^{h+1}=0\) for every unit \(u\). The tangent matrix is monomial precisely when these \(j\)'s form a permutation of the coordinates, and step 1 completes the classification.

**5. Counting images without overcounting units.** In \(A_{h+1}\), the ideal \((x_j)\) has dimension \(h(h+1)^{d-1}\), since the exponent of \(x_j\) ranges from one through \(h\), while every other exponent ranges from zero through \(h\). Requiring the coefficient of \(x_j\) to be nonzero leaves exactly \((q-1)q^{h(h+1)^{d-1}-1}\) distinct possible images. Each permutation has \(d\) independent image choices. Multiplication by \(d!\) yields the second formula.

## Verification

The accompanying `verify.py` independently constructs monomial bases, multiplies truncated polynomials coefficientwise, and tests powers of candidate generator images. It exhaustively counts the compatible substitution pairs for \(d=2\), \((p,n)=(2,2),(2,3),(3,3)\), obtaining \(24\), \(2048\), and \(25,509,168\) automorphisms, respectively. It separately exhausts all individual generator images in the case \(d=3,p=2,n=2\). Reproducible seeded finite tests additionally cover \(d=3,p=2,n=3\), \(d=2,p=3,n=4\), and \(d=3,p=3,n=4\). The exhaustive enumerations prove the formulas only in those particular finite cases; all arbitrary-parameter conclusions follow from the preceding argument.

Run `python verify.py` using Python 3; no external libraries are required.

## Relationship to prior work

Díaz, Liendo, Manzano-Flores, and Regeta, arXiv:2408.02197 (first posted August 5, 2024), study automorphism groups of zero-dimensional monomial algebras over **characteristic-zero** fields. Their classification via locally nilpotent derivations does not establish the prime-characteristic Frobenius jump, and the present result does not claim their general characteristic-zero classification. Their Example 4.25 treats \((x^2,y^2)\) in characteristic zero, a useful contrast with the characteristic-two exception here. Díaz and Lucchini Arteche, arXiv:2409.15081, likewise assume characteristic zero and address reconstruction of the algebra from the automorphism group, not this finite-field count. A nearby result on truncated coordinate-cross algebras concerns an algebra with mixed-variable products killed, not these complete intersections whose mixed monomials survive.

## Limitations

Only the adjacent exponents \(p^e\) and \(p^e+1\) are classified. No claim is made for intermediate positive multiples of the characteristic that are not prime powers; their automorphism substitutions can have additional forms. This theorem classifies rational points over finite fields, not the scheme-theoretic infinitesimal structure of the automorphism group. Exhaustive checks are finite illustrations, not a substitute for the proof. No claim of comprehensive literature priority or independent mathematical validation is made.

## References

1. R. Díaz, A. Liendo, G. Manzano-Flores, and A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1 (2024-08-05), https://arxiv.org/abs/2408.02197 .
2. R. Díaz and G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081v1 (2024-09-23), https://arxiv.org/abs/2409.15081 .
