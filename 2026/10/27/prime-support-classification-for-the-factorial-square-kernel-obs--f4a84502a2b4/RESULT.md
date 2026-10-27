# Prime-support classification for the factorial square-kernel obstruction

## Finding

Let \(s(n)\) denote the squarefree kernel (product of those distinct primes that occur with odd exponent) of a positive integer \(n\). Define the arithmetic obstruction set
\[
\mathcal R=\{a\ge1: a\text{ squarefree and }s(ac!)\ge a\text{ for every integer }c\ge0\}.
\]
For squarefree positive integers \(a\) with at most two distinct prime factors, membership in \(\mathcal R\) is completely classified:

1. \(1\in\mathcal R\).
2. For prime \(p\), \(p\in\mathcal R\) if and only if \(p\ge13\).
3. For distinct primes \(p<q\), \(pq\in\mathcal R\) if and only if \(p\ge13\) and
\[
(p,q)\notin\{(13,17),(13,19),(17,19),(17,23),(19,23)\}.
\]
In particular, for every pair of primes \(13\le p<q\) with \(q\ge29\), the product \(pq\) belongs to \(\mathcal R\). The threshold \(29\) is sharp for the uniform statement: \(19\cdot23\notin\mathcal R\). The set \(\mathcal R\) is not closed under multiplication, because \(13,17\in\mathcal R\) but \(13\cdot17\notin\mathcal R\).

## Assumptions and scope

All factorial arguments \(c\) range over the **entire infinite set** of nonnegative integers, with \(0!=1\). All primes are ordinary positive rational primes; the product \(pq\) uses distinct primes. The theorem concerns the auxiliary obstruction \(\mathcal R\), not the minimum number of factorials whose product is a square. These two predicates are not equivalent in general.

## Proof

**Square-kernel reduction.** Put \(s_c=s(c!)\). For squarefree \(a\), parity of each prime valuation yields
\[
s(ac!)=\frac{a\,s_c}{\gcd(a,s_c)^2}.
\]
Consequently,
\[
a\in\mathcal R\quad\Longleftrightarrow\quad
\gcd(a,s_c)^2\le s_c\quad\text{for all integers }c\ge0.
\tag{1}
\]
This also shows downward closure under squarefree divisibility: if a squarefree \(a\) fails (1), every squarefree multiple of \(a\) fails (1).

**Uniform bounds on the factorial squarefree kernel.** The exact values of \(s_c\) for \(12\le c\le16\) are, in order, \(231,3003,858,1430,1430\), all strictly larger than \(c^2\). For every integer \(c\ge17\), the third Ramanujan-prime threshold \(R_3=17\) guarantees at least three primes in \((c/2,c]\). Each occurs to exponent one in \(c!\), whence
\[
s_c> (c/2)^3>c^2\quad(c\ge17).
\]
Together with the five preceding exact values, this proves
\[
s_c>c^2\quad(c\ge12).
\tag{2}
\]
Likewise, the fifth Ramanujan-prime threshold \(R_5=41\) guarantees at least five primes in \((c/2,c]\) for every \(c\ge41\). They divide \(c!\) exactly once, so
\[
s_c>(c/2)^5>c^4\quad(c\ge41).
\tag{3}
\]
Both inequalities are strict because \(c\ge17>8\) and \(c\ge41>32\).

**Singletons and small primes.** For \(p=2,3,5,7,11\), the respective choices \(c=2,3,6,7,11\) yield \((s_c,\gcd(p,s_c))=(2,2),(6,3),(5,5),(35,7),(77,11)\), so (1) fails. The same holds for any squarefree multiple of these primes. If \(p\ge13\), then for \(c<p\) the gcd in (1) is one, while for \(c\ge p\), inequality (2) gives \(s_c>c^2\ge p^2\). Hence every prime \(p\ge13\) is in \(\mathcal R\).

**Reduction of two-prime products to a finite check.** Now let \(13\le p<q\). For \(c<q\), \(\gcd(pq,s_c)\le p\); when that gcd exceeds one, \(c\ge p\ge13\) and (2) shows \(s_c>p^2\). Thus (1) holds whenever \(c<q\). For \(c\ge q\) and \(c\ge41\), (3) gives \(s_c>c^4\ge(pq)^2\), so (1) holds there as well. If \(q\ge41\), these cases exhaust every \(c\) and establish membership.

Only \(q\le37\) remains. The possible primes are \(13,17,19,23,29,31,37\), yielding exactly \(\binom72=21\) unordered pairs. For each, criterion (1) only needs to be tested at integers \(q\le c\le40\). An exhaustive exact-integer computation of the \(s_c\) values by Legendre valuations (independently checked by direct factorization of \(c!\)) finds failures for precisely five pairs:

| \((p,q)\) | First failing \(c\) | \(s_c\) | \(\gcd(pq,s_c)\) |
| --- | ---: | ---: | ---: |
| \((13,17)\) | 17 | 24310 | 221 |
| \((13,19)\) | 20 | 46189 | 247 |
| \((17,19)\) | 20 | 46189 | 323 |
| \((17,23)\) | 26 | 104006 | 391 |
| \((19,23)\) | 26 | 104006 | 437 |

In every table row the square of the last column strictly exceeds the third. All remaining 16 pairs satisfy (1) at each required integer \(c\). The standalone verifier implements the exhaustive check without a search cutoff on primes beyond that justified by (2) and (3). This proves the classification, including the unit case \(a=1\). \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program computes \(s(c!)\) for \(0\le c\le40\) by Legendre valuations and, separately, by factoring the actual factorial integers; checks \(s_c>c^2\) for \(12\le c\le40\); tests all 21 pairs of primes in \(\{13,17,19,23,29,31,37\}\) for each necessary \(c\); and reproduces the five first witnesses. It prints `VERIFY_OK` on success. The infinite ranges \(c\ge41\) and \(q\ge41\) are covered by the proved inequalities (2)–(3), **not** by the finite program.

## Relationship to prior work

Yudin (2026), Section 7.1, introduces precisely this square-kernel obstruction \(\mathcal R\) and proves that it has positive lower density, using the gcd reformulation and exponential lower bounds for \(s(c!)\). That theorem does not enumerate its members with one or two prime factors or identify the five exceptional products. Erdős and Graham (1976) give five-factor square-product examples for several semiprimes, including all five exceptional products (their Table 1, p. 353), and establish classical qualitative results for products of factorials. **Those five-factor examples are not equivalent to failures of the \(\mathcal R\) condition**, since the same table contains semiprimes that do satisfy the condition. Sondow (2009) documents the Ramanujan-prime thresholds used to make the infinite classification finite.

## Limitations

This is an exact classification only for the stratum \(\omega(a)\le2\), with \(a\) squarefree. Nothing here classifies products of three or more primes, gives a density formula for the full set \(\mathcal R\), or determines the least factorial count \(F(n)\) for a specific semiprime. The finite calculation covers only the mathematically proved residual range; its correctness can be checked from the standalone code. Bibliographic priority is subject to independent literature review, because equivalent characterizations could occur in sources not indexed under the same terminology.

## References

1. Fedir Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899, first posted 2026-10-01, especially Section 7.1. https://arxiv.org/abs/2610.01899
2. P. Erdős and R. L. Graham, *On products of factorials*, Bulletin of the Institute of Mathematics, Academia Sinica **4** (1976), 337–355, especially pp. 346–347, 353–354. https://fanchung.ucsd.edu/ron/papers/76_12_factorial_products.pdf
3. Jonathan Sondow, *Ramanujan primes and Bertrand's postulate*, American Mathematical Monthly **116** (2009), 630–635; arXiv:0907.5232. https://arxiv.org/abs/0907.5232
