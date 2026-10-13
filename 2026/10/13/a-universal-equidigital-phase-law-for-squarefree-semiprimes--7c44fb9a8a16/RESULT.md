# A universal equidigital phase law for squarefree semiprimes
## Finding
Fix an integer base \(B\ge2\). Let
\[
\delta_B(m)=\lfloor\log_B m\rfloor+1
\]
be the number of base-\(B\) digits of \(m\).

For distinct primes \(p,q\), put
\[
a=\delta_B(p),\qquad b=\delta_B(q).
\]
Then the squarefree semiprime \(pq\) is equidigital exactly when
\[
pq\ge B^{a+b-1}.
\]
If this inequality fails, the prime factorization of \(pq\) uses exactly one
more digit than \(pq\). In particular, no squarefree semiprime is frugal.

There is also a universal limiting law inside prime digit blocks. Define
\[
\mathcal P_a(B)=\{p\text{ prime}:B^{a-1}\le p<B^a\}.
\]
Among ordered pairs of distinct primes
\[
(p,q)\in\mathcal P_a(B)\times\mathcal P_b(B),
\]
the proportion for which \(pq\) is equidigital tends, as
\[
\min(a,b)\to\infty,
\]
to
\[
\rho_B=
\frac{B(B-1-\log B)}{(B-1)^2}.
\]
For example, in base \(10\),
\[
\rho_{10}=0.8268413465\ldots.
\]

## Assumptions and scope
For a squarefree integer, the factorization-digit count is the sum of the
digit counts of its distinct prime factors, because exponents equal to \(1\)
are omitted. Thus for \(pq\) with distinct primes, the factorization-digit
count is
\[
\delta_B(p)+\delta_B(q)=a+b.
\]

The word equidigital means equality between the digit count of the integer and
the digit count of its prime factorization. Following the inclusive convention
used by Pinch, an economical number may be equidigital or frugal; a frugal
number has strictly fewer factorization digits than integer digits.

The asymptotic statement concerns prime pairs drawn from complete base-\(B\)
digit blocks. It is not a density statement for all semiprimes ordered by
magnitude.

## Proof
Since
\[
B^{a-1}\le p<B^a,\qquad B^{b-1}\le q<B^b,
\]
their product satisfies
\[
B^{a+b-2}\le pq<B^{a+b}.
\]
Therefore
\[
\delta_B(pq)\in\{a+b-1,a+b\}.
\]
The factorization of the squarefree semiprime \(pq\) uses exactly \(a+b\)
digits. Hence \(pq\) is equidigital precisely when
\[
\delta_B(pq)=a+b,
\]
which is equivalent to
\[
pq\ge B^{a+b-1}.
\]
Otherwise
\[
\delta_B(pq)=a+b-1,
\]
so the factorization uses exactly one extra digit. This proves the exact
classification and also shows that a squarefree semiprime can never be
frugal.

For the limiting law, put
\[
X_a=B^{a-1},\qquad X_b=B^{b-1},
\]
and normalize
\[
u=\frac p{X_a},\qquad v=\frac q{X_b}.
\]
Then
\[
1\le u<B,\qquad1\le v<B,
\]
and the exact equidigital condition becomes
\[
uv\ge B.
\]

The prime number theorem implies that primes become uniformly distributed
after this fixed multiplicative rescaling inside a digit block. More
explicitly, for fixed
\[
1\le r<s\le B,
\]
one has
\[
\frac{\#\{p\in\mathcal P_a(B):rX_a\le p<sX_a\}}
{\#\mathcal P_a(B)}
\longrightarrow
\frac{s-r}{B-1}.
\]
Indeed, applying
\[
\pi(x)\sim\frac{x}{\log x}
\]
to the two endpoints shows that the numerator is asymptotic to
\[
\frac{(s-r)X_a}{\log X_a},
\]
while the denominator is asymptotic to
\[
\frac{(B-1)X_a}{\log X_a}.
\]
The same statement holds independently for the \(b\)-block.

It follows, first for finite unions of rectangles and then by upper and lower
rectangle approximation, that the normalized prime-pair distribution tends to
uniform area measure on
\[
[1,B]^2.
\]
The boundary curve
\[
uv=B
\]
has area zero, so it causes no ambiguity in the limiting proportion. If
\(a=b\), deleting the diagonal \(p=q\) removes only
\[
\#\mathcal P_a(B)
\]
pairs out of order
\[
\#\mathcal P_a(B)^2,
\]
and therefore does not affect the limit.

The desired proportion is consequently the area fraction of
\[
\{(u,v)\in[1,B]^2:uv\ge B\}.
\]
For fixed \(u\in[1,B]\), the allowed interval is
\[
B/u\le v\le B,
\]
so its length is
\[
B-\frac Bu.
\]
Thus the numerator area is
\[
\int_1^B\left(B-\frac Bu\right)\,du
=
B(B-1-\log B).
\]
Dividing by the square's area
\[
(B-1)^2
\]
gives
\[
\rho_B=
\frac{B(B-1-\log B)}{(B-1)^2}.
\]

## Verification
The accompanying checker verifies the exact digit criterion for prime pairs in
several bases and independently counts all ordered distinct-prime pairs in the
decimal digit blocks through six digits.

For equal decimal blocks, the observed equidigital proportions for prime
lengths \(2,3,4,5,6\) are approximately
\[
0.7333,\ 0.7810,\ 0.7981,\ 0.8046,\ 0.8080,
\]
while the proved limiting constant is
\[
\rho_{10}=0.8268413465\ldots.
\]
The slow finite convergence is consistent with the logarithmic error scale in
prime counting.

These finite checks are corroborative only. The limiting theorem uses the
prime number theorem and the area computation above.

## Relationship to prior work
Recamán introduced equidigital representation in 1995. Pinch developed the
base-\(B\) framework, proved the basic product digit inequalities, constructed
squarefree economical and extravagant numbers, and reported finite global
statistics for the factorization-digit excess. His paper does not state a
semiprime classification or a limiting semiprime phase law.

De Koninck and Luca later proved unconditional results on arbitrarily long
strings of consecutive economical numbers. Their complete 2005 paper develops
global structural criteria in terms of the number of prime factors, but does
not state a squarefree-semiprime digit-block law.

Subsequent work studies the global counting and central distribution of the
number of digits needed to write an integer's factorization. In particular,
De Koninck, Doyon and Letendre prove a Gaussian limiting law for the
factorization-digit count over all integers. That ambient distribution is
different from conditioning on squarefree semiprimes in two prescribed prime
digit blocks.

OEIS A046758 records equidigital numbers and OEIS A046759 records the strict
economical/frugal sequence in decimal. Neither entry states the prime-block
limit above.

## Limitations
The limiting law is conditional only on the standard prime number theorem, but
it is local to complete prime digit blocks. It does not directly give the
natural density of equidigital squarefree semiprimes ordered by their product.

The 2006 paper *Counting the number of economical numbers* was available here
only through its abstract, which describes global lower and upper bounds for
strongly economical numbers. No whole-document noncoverage claim is made for
that source.

Recamán's 1995 problem predates the exact-day source used for date metadata,
but the inspected bibliographic record supplies only the journal year and
issue, not an exact public calendar day. The earliest exact public date
verified here is the 9 February 1998 release of Pinch's paper.

## References
1. R. G. E. Pinch, "Economical numbers", arXiv:math/9802046v1,
   submitted 9 February 1998. Primary MSC 11A63; secondary 11A25, 11A51.
2. J.-M. De Koninck and F. Luca, "On strings of consecutive economical
   numbers of arbitrary length", *Integers* 5(2) (2005), Article A05,
   published 1 September 2005. AMS classification 11A63, 11A25.
3. J.-M. De Koninck and F. Luca, "Counting the number of economical
   numbers", *Publicationes Mathematicae Debrecen* 68 (2006), 97--113.
4. J.-M. De Koninck, N. Doyon and P. Letendre, "On the distribution of the
   number of digits needed to write the factorization of an integer".
5. OEIS Foundation, A046758, "Equidigital numbers".
6. OEIS Foundation, A046759, "Economical numbers".
