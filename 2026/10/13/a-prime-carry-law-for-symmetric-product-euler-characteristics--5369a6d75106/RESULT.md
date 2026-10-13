# A prime-carry law for symmetric-product Euler characteristics
## Finding
Let \(X\) be a complex quasi-projective variety with finite compactly supported Euler characteristic
\[
c=\chi_c(X),
\]
and define
\[
E_n=\chi_c(\operatorname{Sym}^n X),
\qquad n\ge0.
\]

For every prime \(p\), every nonzero \(E_n\) has an exact base-\(p\) carry description.

If
\[
c>0,
\]
then
\[
E_n=\binom{c+n-1}{n}
\]
and
\[
\boxed{
\nu_p(E_n)
=
\frac{s_p(n)+s_p(c-1)-s_p(c+n-1)}{p-1}
},
\]
where \(s_p(a)\) denotes the sum of the base-\(p\) digits of \(a\). Equivalently, \(\nu_p(E_n)\) is the number of carries when adding
\[
n+(c-1)
\]
in base \(p\).

If
\[
c=-m<0,
\]
then
\[
E_n=(-1)^n\binom{m}{n}
\qquad
(0\le n\le m),
\]
while
\[
E_n=0
\qquad
(n>m).
\]
For \(0\le n\le m\),
\[
\boxed{
\nu_p(E_n)
=
\frac{s_p(n)+s_p(m-n)-s_p(m)}{p-1}
},
\]
equivalently the number of carries in the base-\(p\) addition
\[
n+(m-n).
\]

Thus, for every nonzero symmetric-product Euler characteristic,
\[
p\nmid E_n
\]
if and only if the corresponding addition is carry-free.

For a smooth projective complex curve \(C\) of genus
\[
g\ge2,
\]
put
\[
m=2g-2.
\]
Then
\[
\chi_{\mathrm{top}}(\operatorname{Sym}^n C)
=
(-1)^n\binom{m}{n}
\]
for
\[
0\le n\le m,
\]
and it vanishes for \(n>m\). The common divisor of all intermediate nonzero Euler characteristics is
\[
\boxed{
\gcd_{1\le n\le 2g-3}
\left|
\chi_{\mathrm{top}}(\operatorname{Sym}^n C)
\right|
=
\begin{cases}
2,&g=2^r+1\text{ for some }r\ge0,\\
1,&\text{otherwise}.
\end{cases}
}
\]

In particular, a nontrivial prime divides every intermediate symmetric-power Euler characteristic of \(C\) precisely at the dyadic genera
\[
2,3,5,9,17,\ldots,
\]
and that universal common divisor is always exactly \(2\).

## Assumptions and scope
The symmetric power is
\[
\operatorname{Sym}^n X=X^n/S_n.
\]
The invariant used for a general quasi-projective variety is the compactly supported Euler characteristic. For smooth projective varieties it agrees with the ordinary topological Euler characteristic.

The prime-adic valuation formula concerns nonzero Euler characteristics. When \(c=0\), the symmetric-product generating function is \(1\), hence
\[
E_n=0
\]
for all \(n\ge1\).

The curve gcd excludes the two endpoint coefficients \(n=0\) and \(n=2g-2\), both of absolute value \(1\), because including either would force the gcd to be trivial for every genus. It also excludes the later vanishing range.

## Proof
The power structure on the Grothendieck ring of complex quasi-projective varieties has
\[
(1-t)^{-[X]}
=
\sum_{n\ge0}[\operatorname{Sym}^n X]t^n.
\]
The Euler characteristic is a homomorphism of these power structures. Therefore
\[
\sum_{n\ge0}E_nt^n
=
(1-t)^{-c}.
\]

If \(c>0\), the binomial expansion gives
\[
E_n=\binom{c+n-1}{n}.
\]
If \(c=-m<0\), then
\[
(1-t)^{-c}=(1-t)^m,
\]
so
\[
E_n=(-1)^n\binom{m}{n}
\]
for \(0\le n\le m\), followed by zero coefficients.

It remains to determine the prime-adic valuation of the binomial coefficients. For a prime \(p\), Legendre's formula can be written
\[
\nu_p(N!)
=
\frac{N-s_p(N)}{p-1}.
\]
Applying it to
\[
\binom{N}{K}
=
\frac{N!}{K!(N-K)!}
\]
gives
\[
\nu_p\binom{N}{K}
=
\frac{s_p(K)+s_p(N-K)-s_p(N)}{p-1}.
\]
Digit-by-digit addition shows that this quotient is exactly the number of base-\(p\) carries in
\[
K+(N-K).
\]

For \(c>0\), take
\[
N=c+n-1,
\qquad
K=n.
\]
For \(c=-m<0\), take
\[
N=m,
\qquad
K=n.
\]
This proves the prime-carry formulas.

Now let \(C\) have genus \(g\ge2\), so
\[
m=2g-2.
\]
The curve Euler characteristics are the signed row
\[
(-1)^n\binom{m}{n}.
\]
We determine the gcd of the interior entries.

Fix a prime \(p\). If \(m=p^a\), then every interior binomial coefficient
\[
\binom{m}{n},
\qquad
1\le n\le m-1,
\]
is divisible by \(p\): in base \(p\), the addition \(n+(m-n)\) must cross the unique nonzero digit of \(m\). Moreover,
\[
\nu_p\binom{p^a}{p^{a-1}}=1,
\]
so the common \(p\)-power is exactly \(p\).

Conversely, suppose \(p\) divides every interior coefficient. If the base-\(p\) expansion of \(m\) has either two nonzero digits or one nonzero digit larger than \(1\), choose \(n=p^j\) at a nonzero digit position that does not equal \(m\). Then the base-\(p\) addition
\[
n+(m-n)=m
\]
is carry-free, so
\[
p\nmid\binom{m}{n},
\]
a contradiction. Hence \(m\) must be a power of \(p\).

Therefore the gcd of all interior coefficients is \(p\) exactly when \(m\) is a prime power, and is \(1\) otherwise. Since
\[
m=2g-2
\]
is even, its only possible prime-power form is a power of \(2\). Thus
\[
2g-2=2^a
\]
if and only if
\[
g=2^{a-1}+1,
\]
which proves the stated dyadic-genus classification.

## Verification
The bundled checker independently expands the symmetric-product Euler generating function for a large finite range of positive and negative Euler exponents.

For every tested prime, it compares the direct valuation of each nonzero binomial coefficient with both the digit-sum formula and an independent digit-by-digit carry counter.

For curves, it computes the full intermediate gcd for genera through \(500\) and checks that it is \(2\) exactly when the genus is one more than a power of two. It also verifies the carry-free criterion coefficient by coefficient.

These finite checks are regression evidence only. The theorem for all parameters follows symbolically from the power-structure identity, Legendre's factorial valuation formula, and the base-\(p\) digit argument above.

## Relationship to prior work
Gusein-Zade, Luengo, and Melle-Hernández describe the power structure on the Grothendieck ring of complex quasi-projective varieties by the identity
\[
(1-t)^{-[X]}
=
\sum_{n\ge0}[\operatorname{Sym}^n X]t^n
\]
and state that Euler characteristic is a homomorphism of power structures. This gives the generating function used here.

Recent work on quadratic Euler characteristics of symmetric powers of curves records the classical complex topological specialization
\[
\chi_{\mathrm{top}}(\operatorname{Sym}^n C)
=
(-1)^n\binom{2g-2}{n}
\]
while refining it to Grothendieck--Witt-valued invariants.

The result here extracts the complete prime-adic carry profile of the ordinary Euler coefficients and then uses it to classify the common divisor across the entire intermediate symmetric-power tower of a curve. Targeted searches in symmetric-product, Macdonald-formula, prime-divisibility, carry, parity, gcd, and dyadic-genus language did not locate either the all-prime carry statement in this geometric form or the sharp curve gcd classification.

## Limitations
The theorem concerns Euler characteristics only. It does not determine prime divisibility of individual Betti or Hodge numbers.

The all-variety statement depends only on the single motivic measure \(\chi_c(X)\), so varieties with the same Euler characteristic have the same Euler sequence even when their finer geometry is very different.

The arithmetic reduction is concise after the symmetric-product Euler generating function is known. An older or unindexed source may contain the same prime-adic consequence in purely binomial language.

## References
S. M. Gusein-Zade, I. Luengo, and A. Melle-Hernández, *Power structure over the Grothendieck ring of varieties and generating series of Hilbert schemes of points*, arXiv:math/0407204, first submitted 12 July 2004.

L. F. Bröring and A. M. Viergever, *Quadratic Euler Characteristic of Symmetric Powers of Curves*, arXiv:2404.16378, first submitted 25 April 2024; *Manuscripta Mathematica* 176 (2025), article 26, DOI 10.1007/s00229-025-01623-0.
