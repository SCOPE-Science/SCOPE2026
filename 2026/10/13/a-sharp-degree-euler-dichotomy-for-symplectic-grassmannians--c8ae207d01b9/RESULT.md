# A sharp degree–Euler dichotomy for symplectic Grassmannians
## Finding
Let
\[
X_{n,k}=\operatorname{IG}(k,2n)
\]
be the complex symplectic Grassmannian of isotropic \(k\)-planes in \(\mathbb C^{2n}\), where
\[
1\le k\le n,
\]
with its Plücker polarization. Put
\[
d=\dim X_{n,k}=\frac{k(4n-3k+1)}2.
\]

Then
\[
\boxed{
\deg X_{n,k}
=
2^{\binom{k}{2}}d!
\frac{\prod_{i=0}^{k-1}i!}
{\prod_{i=1}^{k}(2n-2i+1)!}
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(X_{n,k})
=
2^k\binom nk.
}
\]

There is no equality between these invariants. The complete ordering is
\[
\boxed{
\deg X_{n,k}<\chi_{\mathrm{top}}(X_{n,k})
}
\]
if and only if
\[
k=1
\]
or
\[
(n,k)=(2,2).
\]
In every other case with
\[
k\ge2,
\]
\[
\boxed{
\deg X_{n,k}>\chi_{\mathrm{top}}(X_{n,k}).
}
\]

Thus the unique non-projective degree-below-Euler member is
\[
\operatorname{LG}(2,4)=\operatorname{IG}(2,4),
\]
for which
\[
(\deg,\chi)=(2,4).
\]
Already
\[
\operatorname{IG}(2,6)
\]
has
\[
(\deg,\chi)=(14,12).
\]

## Assumptions and scope
The base field is \(\mathbb C\). The symplectic form is nondegenerate, and the Plücker line bundle is the ample generator associated with the \(k\)-th fundamental weight of type \(C_n\).

The Euler characteristic is the ordinary topological Euler characteristic of the complex projective homogeneous variety.

The statement compares only the standard Plücker degree with Euler characteristic. Other polarizations have different degrees.

## Proof
Write
\[
X_{n,k}=\operatorname{Sp}_{2n}/P_k.
\]
For the type-\(C_n\) positive coroots, use the basis \(e_1,\ldots,e_n\). The relevant coroots are
\[
e_i-e_j,\qquad e_i+e_j,\qquad e_i,
\]
and
\[
\rho=\sum_{i=1}^{n}(n-i+1)e_i,
\qquad
\omega_k=e_1+\cdots+e_k.
\]

Borel--Weil together with the Weyl dimension formula gives the leading coefficient of
\[
\dim H^0(X_{n,k},\mathcal O(q))
\]
as the product over positive coroots on which \(\omega_k\) is nonzero. Multiplying that leading coefficient by \(d!\) gives
\[
\deg X_{n,k}
=
d!\,
\frac{
2^{\binom{k}{2}}
}{
\left(\prod_{1\le i\le k<j\le n}(j-i)\right)
\left(\prod_{1\le i<j\le k}(2n-i-j+2)\right)
\left(\prod_{1\le i\le k<j\le n}(2n-i-j+2)\right)
\left(\prod_{i=1}^{k}(n-i+1)\right)
}.
\]
A direct factorial simplification yields
\[
\deg X_{n,k}
=
2^{\binom{k}{2}}d!
\frac{\prod_{i=0}^{k-1}i!}
{\prod_{i=1}^{k}(2n-2i+1)!}.
\]

The Bruhat decomposition has one affine cell for each element of the Weyl-group quotient
\[
W(C_n)/(W(A_{k-1})\times W(C_{n-k})).
\]
Therefore
\[
\chi_{\mathrm{top}}(X_{n,k})
=
\frac{2^n n!}{k!\,2^{n-k}(n-k)!}
=
2^k\binom nk.
\]

It remains to compare the two formulas.

For
\[
k=1,
\]
one has
\[
X_{n,1}\cong\mathbb P^{2n-1},
\]
so
\[
\deg X_{n,1}=1<2n=\chi_{\mathrm{top}}(X_{n,1}).
\]

Assume now
\[
k\ge2
\]
and set
\[
R_{n,k}
=
\frac{\deg X_{n,k}}{2^k\binom nk}.
\]
We first show that, for fixed \(k\), this ratio is strictly increasing in \(n\).

Put
\[
a=n-k,
\qquad
K=\frac{k(k+1)}2,
\qquad
d=2ka+K.
\]
From the degree product,
\[
\frac{\deg X_{n+1,k}}{\deg X_{n,k}}
=
\frac{(d+1)(d+2)\cdots(d+2k)}
{(2a+2)(2a+3)\cdots(2a+2k+1)}.
\]
Every individual factor is greater than \(1\). Moreover the first two factors alone satisfy
\[
\frac{(d+1)(d+2)}
{(2a+2)(2a+3)}
>
\frac{a+k+1}{a+1}
=
\frac{\binom{n+1}{k}}{\binom nk}.
\]
Indeed this is equivalent to
\[
(d+1)(d+2)>2(2a+3)(a+k+1).
\]
After substituting \(d=2ka+K\), the difference between the two sides is
\[
4a^2(k^2-1)
+
2a(k^3+k^2+k-5)
+
\frac{k^4+2k^3+7k^2-18k-16}{4}.
\]
For
\[
k\ge2
\]
this is strictly positive: the first two coefficients are nonnegative, and after writing
\[
u=k-2
\]
the constant numerator becomes
\[
u^4+10u^3+43u^2+66u+8.
\]
Thus
\[
R_{n+1,k}>R_{n,k}.
\]

For
\[
k=2,
\]
the boundary value is
\[
R_{2,2}=\frac{2}{4}=\frac12,
\]
whereas
\[
R_{3,2}=\frac{14}{12}=\frac76>1.
\]
Strict growth in \(n\) therefore proves the claimed comparison for every two-plane case.

It remains only to treat
\[
k\ge3.
\]
At the boundary \(n=k\), write
\[
L_k=\deg\operatorname{LG}(k,2k).
\]
If
\[
K=\frac{k(k+1)}2,
\]
then the degree formula gives
\[
\frac{L_{k+1}}{L_k}
=
2^k
\frac{\binom{K+k+1}{k+1}}
{\binom{2k+1}{k+1}}.
\]
For
\[
k\ge2,
\]
\[
K+k+1=\frac{(k+1)(k+2)}2>2k+1,
\]
so the binomial quotient is strictly greater than \(1\). Hence
\[
\frac{L_{k+1}}{2^{k+1}}
>
\frac{L_k}{2^k}.
\]
Since
\[
L_3=16>8=2^3,
\]
we obtain
\[
L_k>2^k
\qquad(k\ge3).
\]
Finally the already-proved strict growth of \(R_{n,k}\) in \(n\) gives
\[
R_{n,k}>1
\]
for every
\[
n\ge k\ge3.
\]

This proves the complete dichotomy and shows that equality never occurs.

## Verification
The bundled checker evaluates the factorial degree formula with exact rational arithmetic for
\[
1\le n\le40,
\qquad
1\le k\le n.
\]

Independently, it evaluates the Weyl-root product before factorial simplification and verifies equality with the closed degree formula.

It also verifies the Weyl-group cell count
\[
2^k\binom nk,
\]
the complete strict degree-versus-Euler classification, the fixed-\(k\) adjacent-ratio identity, and the Lagrangian boundary recurrence throughout the test range.

These finite checks are regression evidence only. The all-parameter result follows from the symbolic product identities and inequalities above.

## Relationship to prior work
Buch, Kresch, and Tamvakis develop the integral Schubert calculus of symplectic isotropic Grassmannians, including the indexing of Schubert classes and the type-\(C\) Weyl-group description. The projective degree formula used here is independently recovered from the Weyl dimension formula.

Existing nearby work studies the arithmetic of isotropic-Grassmannian degrees, special Lagrangian degree identities, and Schubert-calculus formulas. Targeted searches in geometric, Weyl-theoretic, and degree-versus-Euler terminology did not locate the complete strict comparison above.

The present result isolates a particularly rigid phase diagram: after projective space, only the smallest Lagrangian quadric remains below its Schubert-cell count, and every other symplectic Grassmannian has larger Plücker degree.

## Limitations
The result is specific to type \(C\) symplectic Grassmannians and the Plücker polarization.

The proof compares two global numerical invariants. It does not construct a direct geometric correspondence between a generic complementary Plücker section and the Bruhat cells.

Both formulas entering the comparison are classical or follow from standard homogeneous-space representation theory. Consequently an older unindexed source may contain the same inequality even though targeted searches did not locate it.

## References
Anders S. Buch, Andrew Kresch, and Harry Tamvakis, *A Giambelli formula for isotropic Grassmannians*, arXiv:0811.2781, first submitted 17 November 2008; *Selecta Mathematica* 23 (2017), 869--914, DOI 10.1007/s00029-016-0250-1.
