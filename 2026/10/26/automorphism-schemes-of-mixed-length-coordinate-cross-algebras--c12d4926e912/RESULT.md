# Automorphism schemes of mixed-length coordinate-cross algebras

## Finding

Let \(k\) be any field, let \(n\ge 1\), and choose integers \(d_1,\ldots,d_n\ge 2\). Define the finite-dimensional commutative algebra

\[
A_{\mathbf d}(k)=k[x_1,\ldots,x_n]/(x_ix_j\ (i\ne j),\ x_i^{d_i}\ (1\le i\le n)).
\]

For \(n\ge2\), put \(S=\{i:d_i=2\}\), \(L=\{i:d_i\ge3\}\), \(r=|S|\), and \(s=|L|\). For each integer \(e\ge3\), let \(m_e=|\{i\in L:d_i=e\}|\), and set

\[
N=rs+s(n-1)+\sum_{i\in L}(d_i-2).
\]

Then the automorphism group scheme \(\mathbf{Aut}(A_{\mathbf d})\) is smooth over \(k\). As a \(k\)-scheme, it is a disjoint union of

\[
\prod_{e\ge 3}m_e!
\]

copies of

\[
\mathrm{GL}_r\times\mathbb G_m^s\times\mathbb A_k^N,
\]

where \(\mathrm{GL}_0\) is interpreted as a point. In particular, \(\dim\mathbf{Aut}(A_{\mathbf d})=r^2+s+N\).

The one-branch boundary is also explicit. If \(n=1\), write \(d=d_1\). When \(\operatorname{char}k=0\), or when \(\operatorname{char}k=p>0\) does not divide \(d\), the automorphism scheme is \(\mathbb G_m\times\mathbb A_k^{d-2}\). If \(p=\operatorname{char}k\) divides \(d\) and \(e=v_p(d)\), it is, as a scheme,

\[
\alpha_{p^e}\times\mathbb G_m\times\mathbb A_k^{d-2}.
\]

Thus every algebra with at least two branches has a smooth automorphism scheme in every characteristic, while the one-branch case is non-smooth exactly when the characteristic divides the truncation length.

## Assumptions and scope

The algebra is unital and commutative, the base field is arbitrary, and all branch lengths satisfy \(d_i\ge2\). The group scheme is the functor sending a commutative \(k\)-algebra \(R\) to the group of \(R\)-algebra automorphisms of \(A_{\mathbf d}(k)\otimes_k R\). The theorem classifies the underlying scheme and its smoothness; it does not assert a direct-product decomposition of the group law.

## Proof

**The one-branch case.** Let \(A=k[x]/(x^d)\), and write an endomorphism as \(x\mapsto f(x)=c+a_1x+\cdots+a_{d-1}x^{d-1}\). On the automorphism locus, \(a_1\) is a unit: after reducing the base modulo its nilradical, the induced map on the cotangent space is multiplication by \(a_1\). Conversely, when \(a_1\) is a unit and \(f^d=0\), the induced linear map on the finite free algebra is invertible, since its determinant reduces to \(a_1^{d(d-1)/2}\) modulo the nilradical.

If the characteristic is zero or is a prime \(p\) not dividing \(d\), the coefficient of \(x^{d-1}\) in \(f(x)^d\) is \(c(d a_1^{d-1}+cQ)\) for a polynomial \(Q\) in the coefficients. The constant-term equation makes \(c\) nilpotent, and the parenthesis is a unit, so \(c=0\). The remaining coefficients are unrestricted apart from \(a_1\) being invertible; hence the scheme is \(\mathbb G_m\times\mathbb A_k^{d-2}\).

Now suppose \(\operatorname{char}k=p\) divides \(d\), and write \(d=p^e m\) with \(p\nmid m\). In characteristic \(p\),

\[
f(x)^d=\bigl(c^{p^e}+a_1^{p^e}x^{p^e}+a_2^{p^e}x^{2p^e}+\cdots\bigr)^m.
\]

The coefficient of \(x^{(m-1)p^e}\) is \(c^{p^e}(m a_1^{p^e(m-1)}+c^{p^e}Q')\) for a polynomial \(Q'\). The parenthesis is a unit because \(m\) and \(a_1\) are units and \(c\) is nilpotent. Thus \(f^d=0\) forces \(c^{p^e}=0\). Conversely, this condition makes every term of \(f(x)^d\) have degree at least \(d\), so it is sufficient. Therefore the automorphism scheme has coordinate ring \(k[c,a_1,a_1^{-1},a_2,\ldots,a_{d-1}]/(c^{p^e})\), giving the stated scheme \(\alpha_{p^e}\times\mathbb G_m\times\mathbb A_k^{d-2}\), which is non-smooth.

**The case of at least two branches.** Let \(R\) be a commutative \(k\)-algebra and let \(\varphi\) be an \(R\)-algebra automorphism. Initially write

\[
\varphi(x_i)=c_i+\sum_{j=1}^n f_{ij}(x_j),
\]

where each \(f_{ij}\) has zero constant term. Let \(\mathfrak m=(x_1,\ldots,x_n)\). After reducing the base to \(R_{\mathrm{red}}=R/\sqrt{0}\), the nilradical of \(A_{\mathbf d}\otimes_k R_{\mathrm{red}}\) is exactly \(\mathfrak m\otimes_k R_{\mathrm{red}}\), since this ideal is nilpotent and its quotient is reduced. Hence every \(c_i\) is nilpotent in \(R\), and the matrix \(B=(a_{ij})\) of linear coefficients is invertible: its reduction is the induced automorphism of \(\mathfrak m/\mathfrak m^2\). Its determinant is therefore a unit in \(R\), because an element that is a unit modulo the nilradical differs from a unit by a nilpotent element.

For \(i\ne h\), the defining relation \(\varphi(x_i)\varphi(x_h)=0\) has degree-one part

\[
c_i B_h+c_h B_i=0,
\]

where \(B_i\) and \(B_h\) are rows of \(B\). Those rows are linearly independent because \(B\) is invertible, so \(c_i=c_h=0\). Since \(n\ge2\), every index occurs in such a pair and all constants vanish. Thus every automorphism over every base algebra preserves the augmentation ideal; this step rules out infinitesimal translations.

Now fix a long branch \(j\in L\), so \(d_j\ge3\). For distinct rows \(i,h\), the coefficient of \(x_j^2\) in \(\varphi(x_i)\varphi(x_h)=0\) gives \(a_{ij}a_{hj}=0\). Locally on the base, each column of an invertible matrix has a unit entry. Therefore each long column has exactly one unit linear coefficient and all its other linear coefficients vanish. Its matched row cannot lie in \(S\), because \(\varphi(x_i)^2=0\) for \(i\in S\) would force the square of that unit coefficient to vanish while \(x_j^2\ne0\). Distinct long columns have distinct matched rows, so the matching is a permutation \(\sigma:L\to L\).

If \(i=\sigma(j)\), the relation \(\varphi(x_i)^{d_i}=0\) forces \(d_i\ge d_j\): otherwise the coefficient of the nonzero basis monomial \(x_j^{d_i}\) is the unit \(a_{ij}^{d_i}\). Since \(\sigma\) permutes \(L\), these inequalities must all be equalities. Consequently \(\sigma\) permutes branches only within equal-length classes, giving \(\prod_{e\ge3}m_e!\) possible patterns. These finitely many patterns define disjoint open-and-closed subschemes: the unique unit coefficient in each long column is locally constant, and every other entry in that column is forced to vanish.

For a matched branch \(j\), write \(f_{\sigma(j),j}(t)=t u(t)\), where \(u(t)\) is a unit modulo \(t^{d_j}\). For every other row \(h\ne\sigma(j)\), the cross relation gives

\[
t u(t)f_{hj}(t)=0\pmod{t^{d_j}}.
\]

Multiplication by \(u(t)\) is invertible, so \(t f_{hj}(t)=0\pmod{t^{d_j}}\); hence \(f_{hj}(t)\) is a scalar multiple of \(t^{d_j-1}\). The matched polynomial has one invertible linear coefficient and \(d_j-2\) free higher coefficients. In the square-zero branches, the \(S\)-by-\(S\) linear block is an arbitrary element of \(\mathrm{GL}_r\), the \(L\)-by-\(S\) block is arbitrary, and the \(S\)-by-\(L\) linear block is zero.

The remaining independent parameters are: \(rs\) entries in the \(L\)-by-\(S\) block; \(s(n-1)\) top-degree shear coefficients, one for each long branch and each nonmatched row; and \(\sum_{i\in L}(d_i-2)\) higher coefficients in the matched branch polynomials. There are also \(s\) invertible leading coefficients and the block \(\mathrm{GL}_r\). These parameters give each permutation component the scheme

\[
\mathrm{GL}_r\times\mathbb G_m^s\times\mathbb A_k^N.
\]

Conversely, every such parameter choice satisfies the defining relations. Its induced map on each graded piece of the augmentation filtration is a length-preserving permutation with unit diagonal coefficients, while the degree-one block is invertible. Thus the map on the full monomial basis is invertible. The coefficient coordinates and their inverse are regular maps, yielding the asserted scheme decomposition. Every component is smooth, proving the theorem.

## Verification

The proof is functorial in the commutative base algebra \(R\); it is not an inference from field-valued points alone. No finite enumeration or numerical experiment is used. As a consistency check, the uniform-length case has \(m_d=n\) and all other \(m_e=0\), so the component count is \(n!\), as expected from branch permutations. In the one-branch case, the coordinate calculation gives \(\mathbb G_m\times\mathbb A_k^{d-2}\) when the characteristic does not divide \(d\), and \(\alpha_{p^{v_p(d)}}\times\mathbb G_m\times\mathbb A_k^{d-2}\) when it does; the latter is non-smooth because its coordinate ring contains a nonzero nilpotent.

## Relationship to prior work

Recent work develops scheme-theoretic automorphism groups and shows that positive-characteristic automorphism schemes can contain Frobenius-thickened, non-smooth structure. Separate monomial-algebra work computes ordinary automorphism groups in characteristic zero. A field-valued normal form for coordinate-cross algebras, even when it gives exact finite-field orders, does not determine the scheme structure: nilpotent base rings can reveal infinitesimal automorphisms invisible on field-valued points. The present result gives the mixed-length scheme decomposition and proves that, once there are at least two branches, the cross relations eliminate those infinitesimal translations.

## Limitations

The theorem concerns only the displayed coordinate-cross algebras and does not classify automorphism schemes of arbitrary monomial algebras. The closest uniform-length comparison was available only as a search-result summary; a full-text comparison of that record remains a residual literature risk. No independent audit has been performed.

## References

1. A. Elduque, “Automorphism group schemes and Weyl groups of gradings,” arXiv:2507.12321, first posted 2025-07-16. https://arxiv.org/abs/2507.12321
2. C. Ma, “Extremal Derived Length in the Unipotent Radicals of Cartan-Type Automorphism Groups,” arXiv:2609.31711, first posted 2026-09-20. https://arxiv.org/abs/2609.31711
3. R. Díaz, A. Liendo, G. Manzano-Flores, and A. Regeta, “The Automorphism groups of zero-dimensional monomial algebras,” arXiv:2408.02197, first posted 2024-08-05. https://arxiv.org/abs/2408.02197
