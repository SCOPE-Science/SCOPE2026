# Exactly five three-prime Lucas–Carmichael numbers with shifted-factor gcd four

## Finding
A Lucas–Carmichael number is an odd squarefree composite integer \(n\) satisfying \(\ell+1\mid n+1\) for every prime \(\ell\mid n\). For three distinct primes \(3\le p<q<r\), put \(n=pqr\) and \(G=\gcd(p+1,q+1,r+1)\). Then
\[
G=4\quad\Longleftrightarrow\quad (p,q,r)\in\{(3,7,19),(7,19,43),(11,31,67),(19,83,787),(23,67,139)\},
\]
provided \(n\) is Lucas–Carmichael. Hence the complete \(G=4\) stratum is \(\{399,5719,22847,214199,1241099\}\). The argument also gives a general effective finiteness principle for every fixed positive even value of \(G\).

## Assumptions and scope
All primes are positive, odd, distinct and strictly ordered. The shift gcd is the ordinary greatest common divisor of the three integers one larger than each prime; this is **not** the gcd of the prime factors themselves. The theorem concerns numbers with exactly three distinct prime factors, not those with four or more.

## Proof
**1. Normalized shifted factors and an integer gap.** Let \(g=G\), \(p+1=ga\), \(q+1=gb\), \(r+1=gc\), so \(1\le a<b<c\) and \(\gcd(a,b,c)=1\). The Lucas–Carmichael property implies \(p+1\mid qr-1\), \(q+1\mid pr-1\), and \(r+1\mid pq-1\). If \(d\mid a,b\), then \(gd\mid p+1,q+1\) and \(qr\equiv1\pmod{gd}\). Since \(q\equiv-1\pmod{gd}\), also \(r\equiv-1\pmod{gd}\), hence \(d\mid c\). Thus \(a,b,c\) are pairwise coprime, and \(\operatorname{lcm}(p+1,q+1,r+1)=gabc\). Consequently the positive integer
\[
T=\frac{pqr+1}{gabc}=g^2-g\left(\frac1a+\frac1b+\frac1c\right)+\frac1{ab}+\frac1{ac}+\frac1{bc}
\]
exists. Write \(\lambda=g^2-T\); because \(g\ge2\) and \(a<b<c\), \(0<\lambda<3g/a\), so the positive integer \(\lambda\) forces \(a<3g\). Hence fixing \(g\) bounds the smallest prime by \(p<3g^2\). The effective upper bounds on \(q,r\) below then prove finiteness of every fixed-g stratum.

**2. A sharp bound at \(g=4\).** As \(b\ge a+1\), \(c\ge a+2\), and the formula for \(\lambda\) strictly decreases when any one coordinate grows (holding the other two fixed),
\[
\lambda\le4\left(\frac1a+\frac1{a+1}+\frac1{a+2}\right)-\left(\frac1{a(a+1)}+\frac1{a(a+2)}+\frac1{(a+1)(a+2)}\right).
\]
The right-hand side decreases with \(a\) and at \(a=11\) equals \(422/429<1\). Since \(\lambda\) is a positive integer, \(a\le10\). Thus \(p=4a-1\) must be one of exactly six primes \(3,7,11,19,23,31\). This is an *unbounded theorem*: it excludes every possible larger least prime before any finite computation.

**3. Exhaustive finite parametrization for each permitted \(p\).** Define \(h=(pq-1)/(r+1)\). By the third shifted-factor divisibility, \(h\) is a positive integer, and \(r>q\) implies \(1\le h<p\). The second divisibility \(q+1\mid pr-1\), multiplied by \(h\), gives
\[
h(pr-1)=p^2(q+1)-(p+1)(p+h),\qquad q+1\mid(p+1)(p+h).
\]
Consequently every triple is obtained by iterating \(h=1,\ldots,p-1\), every positive divisor \(d\mid(p+1)(p+h)\), setting \(q=d-1\) and, if \(h\mid pq-1\), \(r=(pq-1)/h-1\), and retaining only strictly ordered odd primes satisfying the **original three** shifted divisibilities and the exact gcd condition \(G=4\). The final direct divisibility checks cannot be dropped: \(q+1\mid(p+1)(p+h)\) alone is only a necessary condition.

The attached self-contained integer-arithmetic verifier executes this finite enumeration, reproducing for \(p=3,7,11,19,23,31\) respectively \(1,3,9,9,10,5\) unrestricted three-prime Lucas–Carmichael triples, of which \(1,1,1,1,1,0\) have \(G=4\). A second, independent enumeration loops through every prime \(p<q\le2p^2+p-2\) and every positive divisor \(r+1\mid pq-1\), testing the original divisibilities. The two algorithms agree for all six \(p\), and the five surviving triples are those in the statement. This is a finite exhaustive certificate coupled to the proved global reduction, not an experiment extrapolated beyond its range.

To justify the independent upper bound, the preceding identity and \(h<p\) give \(q+1\le(p+1)(p+h)\le(p+1)(2p-1)\), so \(q\le2p^2+p-2\). Also \(r+1\le pq-1\), hence \(r\le pq-2\). No prime or integer parameter is omitted from either bounded enumeration. The five displayed products directly satisfy every defining condition.

## Verification
Run `python3 artifacts/verify_g4.py` from the extracted package directory. No optional packages or external services are required; every primality decision is exact integer trial division and all potential divisor cases are enumerated. Expected output begins `VERIFY_OK: 6 possible smallest primes` and ends with the five factor triples and their integer products.

## Relationship to prior work
The archival Lucas–Carmichael criterion and example \(399\) were already publicly documented by January 2015. Wright later proved general infinitude (arXiv:1609.00231v1, September 2016). Tamilvanan–Muthukrishnan (arXiv:2311.08012v3, Proposition 3.3) prove polynomial bounds on the last two prime factors for a prescribed first factor; their proof contains the precursor divisibility identity. Neither that result nor the known sequence entries constitutes a proof that *exactly five* triples have common shifted-factor gcd four. A separately published fixed-gcd result settles \(G=2\), with only \(2015=5\cdot13\cdot31\), and a classification of equally spaced prime factors applies only to an arithmetic-progression subfamily. This finding treats the next possible shifted gcd, without imposing arithmetic progression.

## Limitations
The five numerical values themselves are not claimed as newly discovered and are recorded in existing tables. What is claimed here is the global *exhaustiveness* of the natural \(G=4\) class using a proved reduction and an exact finite certificate. This is a computationally assisted classification, not a purely handwritten enumeration. The general fixed-\(g\) finiteness corollary uses elementary bounds and does not classify the strata \(g\ge6\). A disguised equivalent theorem could exist in unlocated historical literature; no independent mathematical audit has been performed.

## References
1. *Lucas-Carmichael Numbers*, Programming Praxis, 2015-01-06. https://programmingpraxis.com/2015/01/06/lucas-carmichael-numbers/
2. T. Wright, *There are infinitely many elliptic Carmichael numbers*, arXiv:1609.00231v1 (2016). https://arxiv.org/abs/1609.00231
3. S. Tamilvanan and S. Muthukrishnan, *A new characterization for the Lucas-Carmichael integers and sums of base-p digits*, arXiv:2311.08012v3 (2024), Proposition 3.3. https://arxiv.org/pdf/2311.08012
4. OEIS A006972, *Lucas-Carmichael numbers*. https://oeis.org/A006972
5. *Uniqueness of the primitive three-prime Lucas-Carmichael number*, published 2026: https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-lucas-carmichael-primitive-three-prime-uniqueness--fd644204c2f1
6. *Lucas–Carmichael prime triples in arithmetic progression*, published 2026: https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-lucas-carmichael-ap-prime-triple-parametrization--0e46ab047f14
