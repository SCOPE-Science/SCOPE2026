# Exact two-adic valuation of Pluecker degrees of symplectic Grassmannians
## Finding
Let
\[
X_{n,k}=\operatorname{IG}(k,2n),
\qquad
1\le k\le n,
\]
be the complex symplectic Grassmannian of isotropic \(k\)-planes in \(\mathbb C^{2n}\), in its Pluecker embedding. Its dimension is
\[
d=\frac{k(4n-3k+1)}2.
\]

Its projective degree is
\[
D_{n,k}
=
2^{\binom{k}{2}}d!\,
\frac{\displaystyle\prod_{i=0}^{k-1}i!}
{\displaystyle\prod_{i=1}^{k}(2n-2i+1)!}.
\]

Write \(s_2(m)\) for the number of ones in the binary expansion of \(m\). Then the exact two-adic valuation is
\[
\boxed{
\nu_2(D_{n,k})
=
\frac{k(k+1)}2
-s_2(d)
+\sum_{j=n-k}^{n-1}s_2(j)
-\sum_{j=1}^{k-1}s_2(j)
}.
\]

This interpolates two familiar boundaries. For \(k=2\),
\[
D_{n,2}=C_{2n-2},
\]
where \(C_r\) is the \(r\)-th Catalan number, and the valuation collapses to
\[
\nu_2(D_{n,2})=s_2(n-1).
\]
For the maximal isotropic case \(k=n\),
\[
\nu_2(D_{n,n})
=
\frac{n(n+1)}2
-
s_2\!\left(\frac{n(n+1)}2\right).
\]

For example,
\[
\deg\operatorname{IG}(3,8)=2112=2^6\cdot33,
\]
and the digit formula gives
\[
\nu_2(2112)=6.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The symplectic form on \(\mathbb C^{2n}\) is nondegenerate, and \(X_{n,k}\) parametrizes \(k\)-dimensional isotropic subspaces.

The embedding is the Pluecker embedding associated with the fundamental weight \(\omega_k\). The statement covers every rank
\[
1\le k\le n.
\]
The endpoint \(k=1\) is projective space and has degree \(1\).

The theorem concerns the exact exponent of \(2\) in the projective degree. It does not give corresponding closed formulas for odd-prime valuations.

## Proof
View
\[
X_{n,k}=Sp_{2n}/P_k
\]
as the type-\(C_n\) rational homogeneous variety associated with the fundamental weight
\[
\omega_k=e_1+\cdots+e_k.
\]
For the Pluecker line bundle, Borel--Weil identifies the degree-\(m\) homogeneous coordinate representation with highest weight
\[
m\omega_k.
\]
The Weyl dimension formula therefore makes the Hilbert polynomial a product of linear factors. Taking its leading coefficient and multiplying by
\[
d!
\]
gives the degree.

Use the positive roots
\[
e_i-e_j,\qquad e_i+e_j,\qquad 2e_i
\]
of type \(C_n\), with
\[
\rho=\sum_{i=1}^{n}(n-i+1)e_i.
\]
Only roots not belonging to the Levi of \(P_k\) contribute to the leading coefficient.

For roots
\[
e_i-e_j,
\qquad
1\le i\le k<j\le n,
\]
the numerator contribution is \(1\) and the denominator is \(j-i\).

For roots
\[
e_i+e_j,
\qquad
1\le i<j\le n,\quad i\le k,
\]
the denominator is
\[
2n-i-j+2.
\]
The numerator is \(2\) when \(j\le k\) and \(1\) when \(j>k\). Hence these roots contribute the factor
\[
2^{\binom{k}{2}}.
\]

For long roots
\[
2e_i,
\qquad
1\le i\le k,
\]
the numerator contribution is \(1\) and the denominator is
\[
n-i+1.
\]

Multiplying all root contributions gives
\[
D_{n,k}
=
d!\,
\frac{2^{\binom{k}{2}}}
{
\displaystyle
\prod_{i=1}^{k}\prod_{j=k+1}^{n}(j-i)
\prod_{\substack{1\le i<j\le n\\i\le k}}(2n-i-j+2)
\prod_{i=1}^{k}(n-i+1)
}.
\]
The denominator products telescope into factorial blocks, yielding
\[
D_{n,k}
=
2^{\binom{k}{2}}d!\,
\frac{\displaystyle\prod_{i=0}^{k-1}i!}
{\displaystyle\prod_{i=1}^{k}(2n-2i+1)!}.
\]

Now apply Legendre's formula
\[
\nu_2(m!)=m-s_2(m).
\]
Taking the valuation of the factorial expression gives
\[
\nu_2(D_{n,k})
=
\binom{k}{2}
+d-s_2(d)
+\sum_{i=0}^{k-1}\bigl(i-s_2(i)\bigr)
-\sum_{i=1}^{k}\left((2n-2i+1)-s_2(2n-2i+1)\right).
\]
All linear terms simplify to
\[
\frac{k(k+1)}2.
\]
Also
\[
s_2(2r+1)=s_2(r)+1.
\]
Writing
\[
r=n-i
\]
in the last sum gives
\[
\nu_2(D_{n,k})
=
\frac{k(k+1)}2
-s_2(d)
+\sum_{j=n-k}^{n-1}s_2(j)
-\sum_{j=1}^{k-1}s_2(j),
\]
as claimed.

For \(k=2\), the factorial degree formula simplifies to the Catalan number
\[
C_{2n-2},
\]
and the standard Catalan valuation formula gives
\[
\nu_2(C_{2n-2})=s_2(n-1).
\]
For \(k=n\), the two digit-sum ranges cancel, leaving the displayed Lagrangian specialization.

## Verification
The bundled checker independently evaluates the degree in two forms: from the positive-root product in type \(C_n\), and from the simplified factorial formula. It compares both exact integers for every pair
\[
1\le k\le n\le60.
\]

For the same \(1830\) parameter pairs, it verifies the digit-sum valuation against direct exact division by powers of \(2\). It separately checks the Catalan specialization for
\[
2\le n\le500
\]
and the maximal Lagrangian specialization for
\[
1\le n\le200.
\]

These finite calculations are regression evidence only. The infinite theorem follows from the Weyl-product calculation and Legendre's formula.

## Relationship to prior work
Buch, Kresch, and Tamvakis develop integral Schubert calculus for the full family of symplectic isotropic Grassmannians and explicitly place the maximal Lagrangian Grassmannian and the non-maximal varieties in one type-\(C\) framework.

The projective degree itself is a classical consequence of Borel--Weil and the Weyl dimension formula for the homogeneous embedding. The new statement isolated here is the closed binary-digit expression for the exact two-primary content uniformly for every
\[
\operatorname{IG}(k,2n).
\]

The maximal boundary \(k=n\) is not claimed as new; its valuation formula was already known in searchable degree arithmetic. The present formula extends beyond that boundary to every non-maximal isotropic rank and recovers the Catalan edge \(k=2\).

Targeted searches using symplectic Grassmannian, isotropic Grassmannian, Pluecker degree, parity, divisibility, binary digit sum, and two-adic valuation formulations did not locate the displayed all-\(k\) valuation formula.

## Limitations
Only the prime \(2\) is simplified to the displayed digit-sum form. The factorial degree formula permits odd-prime valuation calculations, but no analogous closed classification is asserted here.

The result is for the nondegenerate symplectic Grassmannian, not the odd symplectic or orthogonal Grassmannians.

The valuation simplification is elementary once the factorial degree formula is in hand, so an unindexed representation-theoretic or Schubert-calculus source could contain the same identity.

## References
Anders S. Buch, Andrew Kresch, and Harry Tamvakis, *A Giambelli formula for isotropic Grassmannians*, arXiv:0811.2781, first submitted 17 November 2008.

J. M. Landsberg and L. Manivel, *Representation theory and projective geometry*, arXiv:math/0203260, first submitted 25 March 2002.
