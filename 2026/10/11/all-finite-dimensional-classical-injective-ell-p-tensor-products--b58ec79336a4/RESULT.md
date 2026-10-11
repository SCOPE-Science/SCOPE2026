# All finite-dimensional classical injective \(\ell_p\)-tensor products have maximal von Neumann--Jordan constant
## Finding
For \(\mathbb K\in\{\mathbb R,\mathbb C\}\), every \(1\le p,q\le\infty\), and all integers \(m,n\ge2\),
\[
C_{\mathrm{NJ}}\!\left(\ell_p^m(\mathbb K)\widehat\otimes_\varepsilon \ell_q^n(\mathbb K)\right)=2.
\]
Thus every finite-dimensional classical injective tensor product with both factors of dimension at least two has the maximal von Neumann--Jordan constant, for every exponent pair.

## Assumptions and scope
The scalar field is \(\mathbb K\in\{\mathbb R,\mathbb C\}\). The exponents satisfy \(1\le p,q\le\infty\), with \(1/\infty=0\), and \(p'\) denotes the Hölder conjugate of \(p\). The dimensions satisfy \(m,n\ge2\). The von Neumann--Jordan constant is
\[
C_{\mathrm{NJ}}(X)=\sup_{(x,y)\ne(0,0)}
\frac{\|x+y\|^2+\|x-y\|^2}{2(\|x\|^2+\|y\|^2)}.
\]
Only the canonical injective tensor norm is considered here. The proof is finite-dimensional and works identically over the real and complex scalar fields.

## Proof
Use the canonical identification of the first two coordinate tensor factors with operators
\[
\ell_p^2\widehat\otimes_\varepsilon\ell_q^2
\cong \mathcal L(\ell_{p'}^2,\ell_q^2).
\]
Embedding this \(2\times2\) corner into the first two coordinates of \(\ell_p^m\widehat\otimes_\varepsilon\ell_q^n\) is isometric, because the coordinate projection in the domain and the coordinate inclusion in the range both have norm one. It therefore suffices to construct an extremal operator pair in dimension two.

Put
\[
s=\frac1p+\frac1q.
\]
First suppose \(s\le1\). Then \(p'\le q\), so the coordinate identity \(I:\ell_{p'}^2\to\ell_q^2\) and the diagonal sign operator \(D(a,b)=(a,-b)\) both have norm \(1\). Moreover,
\[
(I+D)(a,b)=(2a,0),\qquad (I-D)(a,b)=(0,2b),
\]
so \(\|I+D\|=\|I-D\|=2\). The defining quotient of the pair \((I,D)\) is therefore \(2\).

Now suppose \(s>1\). Then \(q<p'\). The exact two-dimensional norm comparison gives
\[
\|I:\ell_{p'}^2\to\ell_q^2\|=2^{1/q-1/p'}=2^{s-1}.
\]
Let \(S(a,b)=(b,a)\). Since \(S\) is an isometry for every \(\ell_r^2\) norm,
\[
\|S:\ell_{p'}^2\to\ell_q^2\|=2^{s-1}.
\]
The sums are rank-one operators:
\[
(I+S)(a,b)=(a+b,a+b),\qquad
(I-S)(a,b)=(a-b,b-a).
\]
For a rank-one operator \(x\mapsto\varphi(x)v\), the operator norm is \(\|\varphi\|\,\|v\|\). Here the functionals \((a,b)\mapsto a+b\) and \((a,b)\mapsto a-b\) have \(\ell_p^2\)-norm \(2^{1/p}\), while \((1,1)\) and \((1,-1)\) have \(\ell_q^2\)-norm \(2^{1/q}\). Hence
\[
\|I+S\|=\|I-S\|=2^{1/p+1/q}=2^s=2\,2^{s-1}.
\]
After normalizing \(I\) and \(S\) by \(2^{s-1}\), both have norm one and both their sum and difference have norm two. Their von Neumann--Jordan quotient is exactly \(2\).

Since every normed space satisfies \(C_{\mathrm{NJ}}\le2\), the lower bounds in the two cases prove equality for all \(p,q\).

## Verification
Every norm used above is exact. For \(r\le t\), the coordinate inclusion \(\ell_r^2\to\ell_t^2\) has norm \(1\); for \(t<r\), the identity \(\ell_r^2\to\ell_t^2\) has norm \(2^{1/t-1/r}\), attained at the vector with two equal-modulus coordinates. The rank-one norms are exact by Hölder duality and are attained by phase-aligned equal-modulus vectors. Therefore the two displayed operator squares are exact, not asymptotic or computational witnesses.

The boundary \(s=1\) belongs to the first case and gives \(\|I\|=1\). Endpoint exponents \(p=1\) and \(p=\infty\), and similarly for \(q\), are included by the same finite-dimensional norm formulas. No limiting argument is needed.

## Relationship to prior work
Zhang--Xu--Liu--Li, arXiv:2609.37503v1, prove for finite-dimensional classical sequence spaces that the injective tensor product has von Neumann--Jordan constant \(2\) under the sufficient condition \(p^-1+q^-1\le1\), while the projective tensor product has constant \(2\) for all exponents. Their proof uses a diagonal sign pair in the injective region. The identity/swap pair above supplies the complementary region \(p^-1+q^-1>1\), so together the two elementary operator squares cover every exponent pair.

A published comparison record, `2026/10/4/SCOPE-maximal-von-neumann-jordan-constant-for-injective-ell-p-tensor-p--5f2cf20451d2`, proves the injective conclusion whenever \(\max\{p,q\}\ge2\). That result does not cover the open square \(1<p,q<2\). The present identity/swap argument covers that entire square and, combined with the source theorem, yields the all-exponent classification stated here.

## Limitations
The result concerns finite-dimensional classical sequence spaces and the canonical injective tensor norm. It does not classify extremizing pairs, quantify stability of near-extremizers, or extend the statement to arbitrary finite-dimensional Banach factors. The originality comparison is necessarily limited by indexing and terminology: an older operator-space source could encode the same two-by-two identity/swap square without using tensor-product or von Neumann--Jordan language.

## References
1. W. Zhang, Y. Xu, Q. Liu, and Y. Li, *Von Neumann--Jordan Constants in Banach Tensor Products*, arXiv:2609.37503v1, first submitted 2026-09-27.
2. Classical finite-dimensional \(\ell_r\)-norm comparison and Hölder duality, used only in the explicit \(2\times2\) operator calculation above.
