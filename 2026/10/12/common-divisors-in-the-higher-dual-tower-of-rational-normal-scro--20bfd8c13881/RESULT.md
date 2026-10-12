# Common divisors in the higher-dual tower of rational normal scrolls
## Finding
Let
\[
X=S(d_1,\ldots,d_n)
=
\mathbb P\!\left(\bigoplus_{i=1}^{n}\mathcal O_{\mathbb P^1}(d_i)\right)
\]
be a smooth rational normal scroll with
\[
n\ge2,
\qquad
2\le d_1\le\cdots\le d_n,
\]
and total degree
\[
d=d_1+\cdots+d_n.
\]
For every
\[
1\le k\le d_1,
\]
let
\[
D_k=\deg_k X^{(k)}
\]
be the standard higher-dual degree associated with order-\(k\) osculating hyperplanes.

The higher-dual degrees satisfy
\[
D_k=kd-nk(k-1).
\]
Their common divisor has the exact closed form
\[
\gcd(D_1,\ldots,D_{d_1})
=
\gcd(d,2n).
\]

Equivalently, for every prime \(p\),
\[
\nu_p\!\left(\gcd(D_1,\ldots,D_{d_1})\right)
=
\min\{\nu_p(d),\nu_p(2n)\}.
\]
Thus the complete higher-dual degree tower is primitive exactly when
\[
d\text{ is odd}
\quad\text{and}\quad
\gcd(d,n)=1.
\]
In particular, all of the higher-dual degrees are even exactly when
\[
d\text{ is even}.
\]
For an odd prime \(p\), every higher-dual degree is divisible by \(p\) exactly when
\[
p\mid d
\quad\text{and}\quad
p\mid n.
\]

The common divisor therefore depends only on the dimension and total degree, not on the individual splitting type, provided the smallest twist is at least two.

## Assumptions and scope
The ground field is \(\mathbb C\). The scroll is embedded by its tautological line bundle as a smooth rational normal scroll.

The quantity \(\deg_k X^{(k)}\) is the higher-dual degree used in higher-order projective duality. In the rational-normal-scroll range
\[
1\le k\le d_1,
\]
the degree formula is
\[
\deg_k X^{(k)}=kd-nk(k-1).
\]

The hypothesis
\[
d_1\ge2
\]
is essential for the stated gcd reduction because it guarantees that both \(D_1\) and \(D_2\) belong to the tower. If \(d_1=1\), the tower in this range has only \(D_1=d\), so its gcd is simply \(d\).

## Proof
For
\[
1\le k\le d_1,
\]
the higher-dual degree is
\[
D_k=kd-nk(k-1).
\]
Set
\[
g=\gcd(d,2n).
\]
Because
\[
k(k-1)
\]
is even for every integer \(k\), the quantity
\[
nk(k-1)
\]
is divisible by \(2n\). Hence \(g\) divides both terms in
\[
D_k=kd-nk(k-1),
\]
and therefore
\[
g\mid D_k
\]
for every \(k\) in the tower. Thus
\[
g
\mid
\gcd(D_1,\ldots,D_{d_1}).
\]

Conversely,
\[
D_1=d
\]
and, since \(d_1\ge2\),
\[
D_2=2d-2n.
\]
Therefore
\[
\gcd(D_1,D_2)
=
\gcd(d,2d-2n)
=
\gcd(d,2n).
\]
Any common divisor of the whole tower divides the first two terms, so
\[
\gcd(D_1,\ldots,D_{d_1})
\mid
\gcd(d,2n).
\]
Combining the two divisibilities proves
\[
\gcd(D_1,\ldots,D_{d_1})
=
\gcd(d,2n).
\]

The prime-adic statement follows immediately by taking valuations. The primitivity criterion is equivalent to
\[
\gcd(d,2n)=1,
\]
which holds exactly when \(d\) is odd and \(\gcd(d,n)=1\).

## Verification
The bundled checker enumerates dimensions
\[
2\le n\le30,
\]
smallest twists
\[
2\le d_1\le12,
\]
and every realizable total degree in a broad range. For each parameter triple it constructs
\[
D_k=kd-nk(k-1),
\qquad
1\le k\le d_1,
\]
and verifies the exact gcd identity and its prime-wise valuation consequence.

It also checks representative scrolls, including
\[
S(2,2,2),
\qquad
S(2,2,3),
\qquad
S(3,3),
\]
whose higher-dual degree towers begin respectively as
\[
(6,6),
\qquad
(7,8),
\qquad
(6,8,6).
\]
Their gcds are \(6\), \(1\), and \(2\), exactly as predicted by \(\gcd(d,2n)\).

These finite checks are regression evidence only. The infinite theorem is proved by the two divisibility arguments above.

## Relationship to prior work
Dickenstein, Di Rocco, and Piene study higher-order projective duality for toric embeddings and treat rational normal scrolls as the principal non-jet-spanned family. Their Proposition 4.1 gives, for
\[
1\le k\le d_1,
\]
the formula
\[
\deg_k X^{(k)}=kd-nk(k-1).
\]
The same paper explains the osculating-geometric meaning of the higher dual varieties and records examples in which the formula recovers higher dual scrolls explicitly.

Later work on higher-order polar and reciprocal polar loci again emphasizes that higher-dual degrees are natural top polar invariants. The present result extracts a new whole-tower arithmetic invariant: the common divisor of every available higher-dual degree before the first osculating break.

Searches using higher dual degree, rational normal scroll, common divisor, gcd, primitive degree tower, osculating degree divisibility, and the explicit quadratic formula did not locate the identity
\[
\gcd(D_1,\ldots,D_{d_1})=\gcd(d,2n)
\]
or its prime-adic reformulation.

## Limitations
The theorem covers the initial higher-dual range
\[
1\le k\le d_1,
\]
where the closed scroll formula above is valid. Beyond the smallest twist, the geometry and degree formulas change and are not included.

The statement concerns common divisibility of the full available tower in this range. It does not classify gcds of arbitrary proper subcollections.

Because the arithmetic proof is short after the higher-dual degree formula is known, an unindexed source could contain the same gcd consequence.

## References
Alicia Dickenstein, Sandra Di Rocco, and Ragni Piene, *Higher order duality and toric embeddings*, arXiv:1111.4641, first submitted 20 November 2011; Annales de l'Institut Fourier 64 (2014), 375--400.

Ragni Piene, *Higher order polar and reciprocal polar varieties*, arXiv:2002.03691, first submitted 10 February 2020.
