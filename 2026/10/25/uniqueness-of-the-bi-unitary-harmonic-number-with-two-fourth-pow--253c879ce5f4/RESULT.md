# Uniqueness of the bi-unitary harmonic number with two fourth-power prime factors and a singleton prime

## Finding
For pairwise distinct primes \(p,q,r\), put \(n=p^4q^4r\). Its bi-unitary harmonic mean is an integer if and only if
\[
\{p,q\}=\{2,3\}\quad\text{and}\quad r=7.
\]
Equivalently, **the unique bi-unitary harmonic number of this prime-exponent pattern is**
\[
n=2^4\cdot3^4\cdot7=9072,\qquad H^{**}(9072)=12.
\]
The example itself was already known; the assertion of uniqueness among *all* primes of this pattern is the finding.

## Assumptions and scope
For positive integers \(m\), a divisor \(d\mid m\) is bi-unitary if the greatest common unitary divisor of \(d\) and \(m/d\) is \(1\). Write \(\sigma^{**}(m)\) for the sum and \(\tau^{**}(m)\) for the number of bi-unitary divisors. Define
\[
H^{**}(m)=\frac{m\tau^{**}(m)}{\sigma^{**}(m)}.
\]
The number \(m\) is bi-unitary harmonic precisely when this quotient is a positive integer. Multiplicativity and the prime-power definitions imply
\[
\sigma^{**}(x^4)=x^4+x^3+x+1,\quad \tau^{**}(x^4)=4,
\qquad\sigma^{**}(x)=x+1,\quad \tau^{**}(x)=2
\]
for every prime \(x\). Consequently \(\tau^{**}(n)=32\), without any restrictions on the relative sizes of \(p,q,r\). The proof covers every order of these three primes and all three placements of the singleton exponent in increasing-prime order.

## Proof
For \(e\in\{1,4\}\), define the increasing rational functions
\[
g_1(x)=\frac{x}{x+1},\qquad
 g_4(x)=\frac{x^4}{x^4+x^3+x+1}
 =\frac1{1+x^{-1}+x^{-3}+x^{-4}} \quad(x>0).
\]
Both functions are strictly increasing, strictly between \(0\) and \(1\). Order the primes as \(a<b<c\), with the corresponding exponent triple \((e_1,e_2,e_3)\) one of \((1,4,4),(4,1,4),(4,4,1)\). Then
\[
H^{**}(n)=32g_{e_1}(a)g_{e_2}(b)g_{e_3}(c).\tag{1}
\]
**First-prime bound.** If \(a\ge97\), monotonicity and (1) give
\[
32g_1(97)g_4(97)^2>31,
\qquad H^{**}(n)<32.
\]
No integer lies strictly between \(31\) and \(32\), so \(a\le89\) (the preceding prime).

**Second-prime bound.** Fix an eligible prime \(a\le89\) and exponent triple. Put
\[
U=32g_{e_1}(a),\qquad L=U g_{e_2}(397)g_{e_3}(397).
\]
If \(b\ge397\), since \(c>b\), monotonicity gives \(L\le H^{**}(n)<U\). A finite set of **72 exact rational interval checks** (the 24 primes \(a\le89\) times three exponent placements) establishes
\[
\lceil L\rceil\ge \lceil U\rceil
\]
in every case. This means the half-open interval \([L,U)\) contains no integer. The standalone checker implements these comparisons by integer numerator/denominator operations without floating-point approximations. Thus \(b\le389\).

**Finite and exhaustive third-prime reduction.** Fix primes \(a<b\) below these respective bounds and one exponent placement. Reduce
\[
U_2=32g_{e_1}(a)g_{e_2}(b)=\frac AB
\]
to lowest terms, where \(A,B\) are positive integers. If the harmonic mean in (1) equals an integer \(h\), then \(1\le h<U_2\), and, writing \(s_e(x)=x^e+x^{e-1}+x+1\) when \(e=4\), and \(s_1(x)=x+1\), its defining equation becomes
\[
hB\,s_{e_3}(c)=A c^{e_3}.\tag{2}
\]
Here \(s_4(c)=c^4+c^3+c+1\) and \(s_1(c)=c+1\). In each case \(s_{e_3}(c)\equiv1\pmod c\); reducing (2) modulo the prime \(c\) yields
\[
c\mid hB.\tag{3}
\]
Hence every possible final prime \(c\) is a prime factor of \(h\) or of \(B\): **there is no unbounded search over final primes**.

The accompanying standard-library Python program performs the resulting finite enumeration exactly. It enumerates every prime \(a\le89\), every prime \(a<b\le389\), all three exponent patterns, every integer \(1\le h<U_2\), and every prime divisor of \(hB\) with \(c>b\). It first rejects pairs whose exact enclosing interval cannot contain an integer, then tests equation (1) using exact fractions. Every integer denominator and candidate level is factored completely; the program explicitly asserts that no residual unfactored cofactor remains. Its verified output has precisely one accepted solution:
\[
(a,b,c,e_1,e_2,e_3,h)=(2,3,7,4,4,1,12).
\]
Finally, at this candidate, the bi-unitary divisor sum is
\[
(2^4+2^3+2+1)(3^4+3^3+3+1)(7+1)
=27\cdot112\cdot8=24192,
\]
and \(9072\cdot32=12\cdot24192\). Thus the candidate is harmonic, and the exhaustive reduction excludes all others. \(\square\)

## Verification
Run `python3 verify_biharmonic.py` with Python 3 and its standard library; no downloads, special packages, external data or probabilistic tests are needed. The code uses exact `fractions.Fraction` arithmetic, an elementary complete prime sieve, explicit certificate assertions and the terminating bounds established above. It reports 72 exact second-prime cutoff checks, 4,644 ordered first-two-prime pattern branches, 44,193 finite candidate harmonic means and 36,313 eligible last-prime tests. Its unique output is \(n=9072\) with harmonic mean \(12\). This is an exhaustive finite proof component **only because** the analytic bounds and congruence reduction above prove it covers every possible prime triple; an arbitrary initial-range search alone would not.

## Relationship to prior work
Sándor introduced bi-unitary harmonic numbers and recorded \(9072\) as an example in the initial census, along with prime-power formulas and several other low-support classifications. The known example is not claimed as a discovery. Manea and Minculete subsequently classified structured families with a squarefree odd part, \(pqt^2\), and \(p^2q^2t\); these exponent patterns do not imply the complete \(p^4q^4r\) assertion. OEIS A286325 likewise tabulates examples but does not establish that this infinite three-prime pattern has no other members. The contribution is the precise all-primes **uniqueness assertion and its exhaustive finite reduction**, not an extension to arbitrary prime exponents.

## Limitations
This theorem is restricted to exactly three distinct primes with exponent multiset \(\{4,4,1\}\). It does not classify general three-prime bi-unitary harmonic numbers, or the full sequence. The computer-assisted portion is finite and auditable but remains a necessary part of the supplied proof; the displayed statistics alone are not a mathematical certificate, whereas the checked exact finite program together with the bounds is. The comparison with accessible named primary sources and mathematical research records does not rule out unindexed equivalent work or settle publication priority. No independent mathematical audit has been performed.

## References
1. J. Sándor, *On bi-unitary harmonic numbers*, arXiv:1105.0294v1 (first publicly posted 2011-05-02), https://arxiv.org/abs/1105.0294 .
2. A. Manea and N. Minculete, *Types of integer harmonic numbers (II)*, Bulletin of the Transilvania University of Brașov, Series III, 9(58) (2016), 67–82, https://webbut.unitbv.ro/index.php/Series_III/article/download/1820/1566/3270 .
3. OEIS A286325, *Bi-unitary harmonic numbers*, https://oeis.org/A286325 .
