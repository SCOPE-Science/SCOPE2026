# Maximal von Neumann--Jordan constant for injective \(\ell_p\)-tensor products when one exponent is at least \(2\)
## Finding
For \(\mathbb K\in\{\mathbb R,\mathbb C\}\), integers \(m,n\ge2\), and \(1\le p,q\le\infty\) with \(\max\{p,q\}\ge2\), the injective tensor product satisfies \[C_{\mathrm{NJ}}\!\left(\ell_p^m(\mathbb K)\widehat\otimes_\varepsilon \ell_q^n(\mathbb K)\right)=2.\] Thus the finite-dimensional classical injective case has maximal von Neumann--Jordan constant throughout the entire parameter region where at least one exponent is at least \(2\).

This strictly enlarges the finite-dimensional injective region stated in Zhang--Xu--Liu--Li, arXiv:2609.37503v1: their displayed classical-sequence-space result gives the maximal value under \(p^{-1}+q^{-1}\le1\), whereas the statement above includes, for example, \(p=2\) and \(1\le q<2\).

## Assumptions and scope
The scalar field is \(\mathbb K\in\{\mathbb R,\mathbb C\}\). The dimensions satisfy \(m,n\ge2\). The exponents satisfy \(1\le p,q\le\infty\), with the convention \(1/\infty=0\). The von Neumann--Jordan constant is
\[
C_{\mathrm{NJ}}(X)=\sup_{x,y\in X,\ (x,y)\ne(0,0)}
\frac{\|x+y\|^2+\|x-y\|^2}{2(\|x\|^2+\|y\|^2)}.
\]
The injective tensor norm is the canonical one. No assertion is made here for the remaining square \(1\le p,q<2\).

## Proof
By symmetry of the injective tensor product, interchange the factors if necessary and write the exponents so that \(p\ge q\). The hypothesis then gives \(p\ge2\). Coordinate embeddings reduce the lower-bound construction to the first two coordinates, so it is enough to work in
\[
\ell_p^2(\mathbb K)\widehat\otimes_\varepsilon\ell_q^2(\mathbb K)
\cong \mathcal L(\ell_{p'}^2(\mathbb K),\ell_q^2(\mathbb K)),
\]
where \(1/p+1/p'=1\).

Let
\[
H(a,b)=(a+b,a-b).
\]
At the interpolation endpoints,
\[
\|H\|_{\ell_1^2\to\ell_\infty^2}=1,
\qquad
\|H\|_{\ell_2^2\to\ell_2^2}=\sqrt2.
\]
Indeed, the first identity is the triangle inequality and the second follows from \(H^*H=2I\). Riesz--Thorin interpolation with parameter \(\theta=2/p\) therefore gives
\[
\|H\|_{\ell_{p'}^2\to\ell_p^2}\le2^{1/p}.
\]
Because \(q\le p\), the two-dimensional norm comparison
\[
\|z\|_q\le2^{1/q-1/p}\|z\|_p
\]
implies
\[
\|H\|_{\ell_{p'}^2\to\ell_q^2}\le2^{1/q}.
\]
The two coordinate vectors attain this bound, since
\[
\|He_1\|_q=\|He_2\|_q=2^{1/q}.
\]
Hence
\[
A=2^{-1/q}H
\]
has operator norm \(1\). Let \(R(a,b)=(a,-b)\), which is an isometry of \(\ell_{p'}^2\), and put \(B=AR\). Then \(\|B\|=1\), while
\[
(A+B)e_1=2Ae_1,\qquad (A-B)e_2=2Ae_2.
\]
Consequently
\[
\|A+B\|=\|A-B\|=2.
\]
The pair \(A,B\) therefore realizes
\[
\frac{\|A+B\|^2+\|A-B\|^2}{2(\|A\|^2+\|B\|^2)}=2.
\]
Since every Banach space satisfies \(C_{\mathrm{NJ}}(X)\le2\), equality follows in dimension \(2\). The coordinate copy of the two-dimensional tensor product is isometric inside the \(m\)-by-\(n\) tensor product, so the same witness proves the statement for all \(m,n\ge2\).

## Verification
The proof uses only exact norm identities, the endpoint form of Riesz--Thorin interpolation, and the standard isometric identification of a finite-dimensional injective tensor product with the corresponding operator space. The interpolation exponents are explicit:
\[
\frac1{p'}=1-\frac1p=1-\frac\theta2,\qquad
\frac1p=\frac\theta2,\qquad \theta=\frac2p.
\]
Thus the interpolated norm factor is
\[
(\sqrt2)^\theta=2^{1/p}.
\]
The witness is explicit, and both endpoint norms of \(A\pm B\) are attained on coordinate vectors. No numerical experiment, finite enumeration, or asymptotic argument is used.

## Relationship to prior work
Zhang--Xu--Liu--Li, arXiv:2609.37503v1, study von Neumann--Jordan constants of injective and projective Banach tensor products. Their finite-dimensional classical-sequence-space theorem states the injective maximal-value conclusion under \(p^{-1}+q^{-1}\le1\) and gives the projective maximal value for all exponents. The result here concerns only the injective product and replaces that sufficient region by the larger condition \(\max\{p,q\}\ge2\). The two statements are not equivalent: \(p=2\) and \(q=3/2\) lies in the new region but violates \(p^{-1}+q^{-1}\le1\).

The mechanism is also different from a title-level parameter match: the proof constructs an explicit operator square from the two-point Walsh--Hadamard transform and a coordinate reflection. Searches for the same claim under operator-space, uniformly non-square, Walsh--Hadamard, and classical sequence-space formulations found no statement implying this broader region.

## Limitations
The argument depends on choosing the larger exponent \(p\ge2\), so that interpolation controls \(H:\ell_{p'}^2\to\ell_p^2\), followed by the monotone embedding into \(\ell_q^2\). It does not settle the parameter square \(1\le p,q<2\). No claim of optimality for that remaining region is made.

Originality is supported by direct comparison with the focal full text and targeted database/literature searches, but literature may encode the same operator-square witness under different terminology. This is the principal residual originality risk.

## References
1. W. Zhang, Y. Xu, Q. Liu, Y. Li, *Von Neumann--Jordan Constants in Banach Tensor Products*, arXiv:2609.37503v1, first submitted 2026-09-27.
2. The Riesz--Thorin interpolation theorem, applied here only to the explicit two-point transform \(H\).
