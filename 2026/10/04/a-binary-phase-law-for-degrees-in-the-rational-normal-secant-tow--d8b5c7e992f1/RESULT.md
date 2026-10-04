# A binary phase law for degrees in the rational-normal secant tower
## Finding
Let
\[
C_d\subset\mathbb P^d_{\mathbb C},
\qquad d\ge2,
\]
be the rational normal curve. For
\[
0\le k\le\left\lfloor\frac{d-2}{2}\right\rfloor,
\]
let \(S^k(C_d)\) be the \(k\)-th secant variety in the convention that \(S^k(C_d)\) is swept out by \((k+1)\)-secant \(\mathbb P^k\)'s and \(S^0(C_d)=C_d\). These are exactly the proper members of the secant tower before it fills the ambient projective space.

Write
\[
D_{d,k}=\deg S^k(C_d).
\]
Then
\[
D_{d,k}=\binom{d-k}{k+1}.
\]
For every prime \(p\), the exact valuation is
\[
\nu_p(D_{d,k})
=
\frac{s_p(k+1)+s_p(d-2k-1)-s_p(d-k)}{p-1},
\]
where \(s_p(m)\) denotes the sum of the base-\(p\) digits of \(m\). Equivalently, \(\nu_p(D_{d,k})\) is the number of carries in the base-\(p\) addition
\[
(k+1)+(d-2k-1)=d-k.
\]

The binary specialization gives a sharp phase law for the whole tower:
\[
D_{d,k}\text{ is even for every proper }S^k(C_d)
\quad\Longleftrightarrow\quad
d+2\text{ is a power of two}.
\]
If \(d+2\) is not a power of two, the first odd degree occurs exactly at
\[
k_{\min}=2^{\nu_2(d+2)}-1.
\]
Thus the ambient degrees
\[
d=2,6,14,30,62,\ldots
\]
are precisely those for which every proper member of the rational-normal secant tower has even projective degree.

For example, when \(d=10\), the first odd degree is at \(k=3\):
\[
D_{10,3}=\binom{7}{4}=35.
\]
When \(d=14\), all seven proper degrees, from \(k=0\) through \(k=6\), are even.

## Assumptions and scope
The ground field is \(\mathbb C\). The secant indexing is fixed explicitly above because the literature also uses conventions in which the subscript counts points rather than projective dimension.

Only proper secant varieties are included. For a rational normal curve, \(S^k(C_d)\) has dimension \(2k+1\) until it fills the ambient space, so properness is exactly
\[
2k+1<d.
\]
The endpoint \(k=0\) is included and equals the original curve; this is essential for the stated whole-tower parity classification.

## Proof
Ciliberto and Russo prove a lower bound for the degree of a proper \(k\)-th secant variety of codimension \(h\):
\[
\deg S^k(X)\ge\binom{h+k+1}{k+1}.
\]
They call equality minimal \(k\)-secant degree and show in their rational-normal-scroll example that rational normal scrolls attain equality. A rational normal curve is the one-dimensional scroll \(S(d)\). For \(C_d\),
\[
h=d-(2k+1)=d-2k-1,
\]
so their formula specializes to
\[
D_{d,k}
=
\binom{h+k+1}{k+1}
=
\binom{d-k}{k+1}.
\]

Now apply Kummer's theorem to this binomial coefficient. Set
\[
a=k+1,
\qquad
b=d-2k-1.
\]
Then \(a+b=d-k\), and Kummer's theorem says that
\[
\nu_p\binom{a+b}{a}
\]
is exactly the number of carries when adding \(a\) and \(b\) in base \(p\). Legendre's digit-sum form of the same valuation is
\[
\nu_p\binom{a+b}{a}
=
\frac{s_p(a)+s_p(b)-s_p(a+b)}{p-1},
\]
which gives the asserted formula.

It remains to classify when all proper degrees are even. Put
\[
x=d+1,
\qquad
 a=k+1.
\]
Then
\[
D_{d,k}=\binom{x-a}{a},
\qquad
1\le a\le\left\lfloor\frac d2\right\rfloor.
\]
Lucas's theorem modulo two says that this binomial coefficient is odd exactly when every binary one-bit of \(a\) is also a one-bit of \(x-a\).

Suppose first that
\[
d+2=2^m.
\]
Then
\[
x=2^m-1
\]
has all its first \(m\) binary digits equal to one. For every admissible positive \(a\), subtraction gives
\[
x-a
\]
as the \(m\)-bit complement of \(a\). Hence no one-bit of \(a\) occurs in \(x-a\), so every \(D_{d,k}\) is even.

Conversely, suppose \(d+2\) is not a power of two and set
\[
t=\nu_2(d+2)=\nu_2(x+1).
\]
The binary expansion of \(x\) has exactly \(t\) trailing ones, followed by a zero, and at least one higher one-bit. Take
\[
a=2^t.
\]
Subtracting \(a\) from \(x\) borrows from a higher one-bit and turns bit \(t\) of \(x-a\) into one. Since \(a\) has no other one-bits, Lucas's criterion shows
\[
\binom{x-a}{a}\equiv1\pmod2.
\]
This \(a\) lies in the proper range.

To prove minimality, let
\[
1\le a<2^t.
\]
The lowest \(t\) bits of \(x\) are all one, so the lowest \(t\) bits of \(x-a\) are the bitwise complement of those of \(a\). Because \(a>0\), at least one one-bit of \(a\) is absent from \(x-a\), and Lucas's criterion makes the binomial coefficient even. Therefore the first odd degree occurs at
\[
a=2^t,
\]
that is,
\[
k_{\min}=2^t-1.
\]

## Verification
The bundled exact checker evaluates the secant degree formula for every
\[
2\le d\le500
\]
and every proper \(k\). It verifies the binary phase law, the formula for the first odd index, and Kummer's carry count for the primes
\[
2,3,5,7,11,13.
\]

The checker also confirms the small boundary cases \(d=2\), \(d=3\), and the first several all-even dimensions
\[
2,6,14,30,62.
\]
These finite computations are regression evidence only. The infinite theorem is proved by the degree formula, Kummer's theorem, and the Lucas-theorem binary argument above.

## Relationship to prior work
Ciliberto and Russo establish the sharp degree bound for higher secant varieties and show that rational normal scrolls attain it. Specializing their formula to the one-dimensional scroll yields
\[
\deg S^k(C_d)=\binom{d-k}{k+1}.
\]
Their paper also characterizes rational normal curves through minimal secant-degree properties.

The arithmetic statement here is different: it determines every prime-adic valuation of every proper secant degree and then classifies the complete binary behavior of the tower. Claim-specific literature searches using parity, odd degree, powers of two, binary carries, and two-adic valuation formulations did not locate the whole-tower theorem or the exact first odd index.

A later work of Nogueira studies characteristic classes and secants of rational normal curves, including Hilbert series and invariants of secant hypersurfaces. Only its abstract was used in the comparison, so it is retained as a residual literature risk rather than treated as evidence of whole-document noncoverage.

## Limitations
The result concerns projective degrees only; it does not determine singularities, characteristic classes, or defining equations of the secant varieties.

The all-even classification deliberately includes \(S^0(C_d)=C_d\). Removing the curve from the tower changes the global parity question for small dimensions and would be a different statement.

The valuation theorem is a concise consequence of a classical binomial degree formula and Kummer's theorem. An older unindexed source may therefore contain the same arithmetic observation even though no covering statement was located in the inspected literature.

## References
Ciro Ciliberto and Francesco Russo, *Varieties with minimal secant degree and linear systems of maximal dimension on surfaces*, arXiv:math/0406494, first submitted 24 June 2004.

Ernst Eduard Kummer, the classical theorem identifying the prime-adic valuation of a binomial coefficient with the number of carries in base \(p\).

Jefferson Nogueira, *Classes características e secantes de curvas racionais normais*, arXiv:2309.09254, 2023.
