# Sharp \(\Lambda(6)\) constant and rigidity for the Boolean rectangular spectrum

## Finding
Let \(d\ge1\), let \(c_\varepsilon\in\mathbb C\) for \(\varepsilon\in\{0,1\}^d\), and define
\[
F(z_1,\ldots,z_d)=\sum_{\varepsilon\in\{0,1\}^d}c_\varepsilon\prod_{j=1}^d z_j^{\varepsilon_j}
\]
on \(\mathbb T^d\) with normalized Haar measure. Then
\[
\|F\|_6^6\le\left(\frac52\right)^d\left(\sum_{\varepsilon}|c_\varepsilon|^2\right)^3.
\]
Hence the exact \(\Lambda(6)\) constant of the Boolean rectangular spectrum \(\{0,1\}^d\subset\mathbb Z^d\) is
\[
K_6(\{0,1\}^d)=\left(\frac52\right)^{d/6}.
\]
For a nonzero coefficient family, equality holds if and only if there are \(\lambda\ne0\) and \(|\eta_j|=1\) such that
\[
c_\varepsilon=\lambda\prod_{j=1}^d\eta_j^{\varepsilon_j}
\quad\text{for every }\varepsilon\in\{0,1\}^d.
\]
Equivalently, every nonzero extremizer and only every extremizer factors as
\[
F(z)=\lambda\prod_{j=1}^d(1+\eta_j z_j).
\]

## Assumptions and scope
The spectrum is the full Cartesian Boolean rectangle \(\{0,1\}^d\) in the dual group \(\mathbb Z^d\). The result is for the sixth moment and arbitrary complex coefficients. It does not assert the same tensor law for other exponents, for proper subsets of the rectangle, or for general products of thin sets.

## Proof
The proof is based on one exact Hilbert-valued two-term identity. Let \(H\) be a complex Hilbert space, let \(x,y\in H\), put \(A=\|x\|^2+\|y\|^2\), and integrate over normalized Haar measure on \(\mathbb T\). Since
\[
\|x+zy\|^2=A+2\operatorname{Re}\bigl(z\langle y,x\rangle\bigr),
\]
the constant Fourier coefficient of the cube is
\[
\int_{\mathbb T}\|x+zy\|^6\,dm(z)
=A^3+6A|\langle x,y\rangle|^2.
\]
Consequently the sharp deficit is
\[
\frac52A^3-\int_{\mathbb T}\|x+zy\|^6\,dm(z)
=\frac32A\left[(\|x\|^2-\|y\|^2)^2
+4\bigl(\|x\|^2\|y\|^2-|\langle x,y\rangle|^2\bigr)\right].
\]
Both terms in brackets are nonnegative. Thus
\[
\int_{\mathbb T}\|x+zy\|^6\,dm(z)\le\frac52(\|x\|^2+\|y\|^2)^3,
\]
and for \((x,y)\ne(0,0)\), equality holds exactly when \(y=\eta x\) for some \(|\eta|=1\).

We now prove the theorem by induction in the following Hilbert-valued form: if \(P\) is a multilinear polynomial on \(\mathbb T^d\) with coefficients \(x_\varepsilon\in H\), then
\[
\int_{\mathbb T^d}\|P(z)\|_H^6\,dm(z)
\le\left(\frac52\right)^d
\left(\sum_\varepsilon\|x_\varepsilon\|_H^2\right)^3.
\]
For the induction step write \(P(z',z_d)=A(z')+z_dB(z')\). Applying the two-term inequality pointwise in \(z'\) gives
\[
\int_{\mathbb T^d}\|P\|^6
\le\frac52\int_{\mathbb T^{d-1}}
\bigl(\|A(z')\|_H^2+\|B(z')\|_H^2\bigr)^3\,dm(z').
\]
The integrand is the sixth power of the \(H\oplus H\)-norm of the multilinear polynomial \(Q(z')=(A(z'),B(z'))\). The induction hypothesis applied to \(Q\) gives the factor \((5/2)^{d-1}\) and preserves exactly the coefficient-square sum. This proves the sharp upper bound.

For equality, the Hilbert-valued induction simultaneously gives rigidity. In dimension one the exact deficit above forces the two coefficients to be unimodular multiples of one another. Assuming the rigidity statement in dimension \(d-1\), equality for \(Q=(A,B)\) makes all coefficient pairs proportional to one fixed vector \((u,v)\in H\oplus H\) with the lower-dimensional product-phase pattern. Equality in the final two-term step then forces \(v=\eta_d u\) with \(|\eta_d|=1\). Iterating yields
\[
x_\varepsilon=h\prod_{j=1}^d\eta_j^{\varepsilon_j}.
\]
For scalar coefficients this is exactly the claimed factorization. Conversely that factorization separates the variables, and each factor \(1+\eta_jz_j\) attains the sharp one-dimensional ratio \(5/2\), so equality is attained in every dimension.

## Verification
The accompanying `verify.py` uses exact rational complex arithmetic. It independently checks the Hilbert-valued two-term deficit identity on several rational complex vector pairs, computes sixth moments by exact triple convolution for deterministic Boolean-cube coefficient arrays, verifies the sharp inequality in dimensions up to three for those cases, and verifies exact equality for factorized extremizers in dimensions one through four. These finite checks corroborate the algebra; the theorem for every dimension is supplied by the analytic induction above.

## Relationship to prior work
The \(\Lambda(p)\) framework for sets of characters is classical. Michels formulates \(K_p(\Lambda)\) for character sets on compact abelian groups and studies structural operator-ideal characterizations rather than this finite Boolean-rectangle constant. Bakas studies multiparameter thin sets in \(\mathbb Z^d\), including Cartesian products of lacunary sets, and records the expected \(p^{d/2}\) growth of their \(\Lambda(p)\) constants as \(p\to\infty\); the inspected paper does not provide this exact finite \(p=6\) tensor constant or the complete extremizer classification for \(\{0,1\}^d\). Targeted database searches also returned nearby Boolean-cube and rectangle results concerning additive energy, Fourier zeros, and support geometry, not the arbitrary-coefficient \(L^6/L^2\) norm proved here.

## Limitations
The result is exact only for the full Boolean rectangle and the sixth moment. The literature comparison does not establish logical uniqueness in the entire historical literature; an equivalent theorem could be implicit in older tensor-product, hypercontractive, or thin-set work under different language. The proof itself does not depend on computational search.

## References
1. C. Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30.
2. O. Bakas, *A multiplier inclusion theorem on product domains*, Proceedings of the Edinburgh Mathematical Society 62 (2019), DOI:10.1017/S0013091519000087.
