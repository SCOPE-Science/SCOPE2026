# Complete six-prime-support classification of the Dedekind–totient inequality
## Finding
Let \(\psi(n)=n\prod_{p\mid n}(1+1/p)\) denote Dedekind's psi function and let \(\omega(n)\) count distinct prime factors. Define
\[
Q=\{17,23,31,47,53,71,107,127,191,383\}.
\]
For every integer \(n>1\) with \(\omega(n)\le6\),
\[
\varphi(\psi(n))>n
\tag{1}
\]
if and only if, for some integers \(a,b\ge1\), either
\[
n=2^a3^b\cdot5\cdot7\cdot11\cdot q\qquad(q\in Q),
\tag{2}
\]
or
\[
n=2^a3^b\cdot5\cdot7\cdot17\cdot23.
\tag{3}
\]
Thus the least possible distinct-prime support of an exception to Sándor's proposed bound \(\varphi(\psi(n))\le n\) is exactly six. There are precisely eleven support templates at that level, each defining an infinite family by varying \(a,b\). Their least member is \(39270=2\cdot3\cdot5\cdot7\cdot11\cdot17\).

The largest allowed final prime in family (2) is \(383\), with the sharp near-equality
\[
\frac{\varphi(\psi(2^a3^b\cdot5\cdot7\cdot11\cdot383))}{2^a3^b\cdot5\cdot7\cdot11\cdot383}
=\frac{147456}{147455}>1.
\]

## Assumptions and scope
For all positive integers \(n\),
\[
\psi(n)=\prod_{p^e\parallel n}p^{e-1}(p+1),
\qquad
\frac{\psi(n)}n=\prod_{p\mid n}\left(1+\frac1p\right).
\tag{4}
\]
For \(m\ge1\), Euler's product gives
\[
\frac{\varphi(m)}m=\prod_{r\mid m}\left(1-\frac1r\right).
\tag{5}
\]
These products are over distinct prime divisors; \(\Omega(n)\), which counts multiplicity, is not the parameter used in the theorem.

The classification is global over all exponents and all primes, subject only to \(1\le\omega(n)\le6\). It does not classify any integer with more than six distinct prime factors.

## Proof
Write
\[
P(n)=\prod_{p\mid n}\left(1+\frac1p\right),
\qquad
R(n)=\frac{\varphi(\psi(n))}{\psi(n)}.
\]
By (4) and (5), the inequality (1) is exactly
\[
P(n)R(n)>1.
\tag{6}
\]
For a fixed number of prime factors, \(P(n)\) is maximized by choosing the smallest permitted distinct primes.

**Odd inputs.** If odd \(n>1\) is divisible by \(5\), the factor \(\psi(5^e)=6\cdot5^{e-1}\) ensures that \(2,3\mid\psi(n)\), so \(R(n)\le1/3\). With at most six distinct odd prime factors,
\[
P(n)\le\prod_{p\in\{3,5,7,11,13,17\}}\left(1+\frac1p\right)
=\frac{27648}{12155}<3.
\]
Thus (6) fails. If \(5\nmid n\), then \(\psi(n)\) is even (since \(n\) has an odd prime factor), so \(R(n)\le1/2\). Moreover,
\[
P(n)\le\prod_{p\in\{3,7,11,13,17,19\}}\left(1+\frac1p\right)
=\frac{92160}{46189}<2.
\]
Again (6) fails. Therefore \(n\) must be even. If \(n=2^a\), direct calculation gives \(\varphi(\psi(n))\le n\), so at least one odd prime also divides \(n\).

**Even inputs and the support threshold.** Now \(2\) and some odd prime divide \(n\). The factors \(\psi(2^a)=3\cdot2^{a-1}\) and \(\psi(p^e)=p^{e-1}(p+1)\) force both \(2,3\mid\psi(n)\), and hence \(R(n)\le1/3\). Therefore (6) requires \(P(n)>3\). If \(\omega(n)\le5\), however,
\[
P(n)\le\prod_{p\in\{2,3,5,7,11\}}\left(1+\frac1p\right)
=\frac{1152}{385}<3.
\]
So any exception in the stated range must have exactly six distinct prime factors. In that range,
\[
P(n)\le\prod_{p\in\{2,3,5,7,11,13\}}\left(1+\frac1p\right)
=\frac{2304}{715}<\frac{15}{4}.
\tag{7}
\]
If some prime \(r\ge5\) divided \(\psi(n)\), equation (5) would strengthen the bound to \(R(n)\le(1/3)(4/5)=4/15\), which together with (7) would give \(P(n)R(n)<1\). Consequently
\[
\{r:r\mid\psi(n),\ r\text{ prime}\}=\{2,3\},
\qquad R(n)=\frac13.
\tag{8}
\]
The original inequality is now equivalent to \(P(n)>3\).

**The forced first four primes.** Among six-prime supports containing \(2\), the largest products when omitting, respectively, \(3\), \(5\), or \(7\) are
\[
\frac{31104}{12155}<3,
\qquad
\frac{6912}{2431}<3,
\qquad
\frac{36288}{12155}<3.
\]
Their optimizing supports are \(\{2,5,7,11,13,17\}\), \(\{2,3,7,11,13,17\}\), and \(\{2,3,5,11,13,17\}\). Thus \(2,3,5,7\) are all mandatory.

Write the two remaining primes \(7<u<v\). From (8) and (4), any prime factor \(p\ge5\) of \(n\) must occur to exponent one; otherwise the factor \(p^{e-1}\) would cause \(p\mid\psi(n)\). Moreover, \(p+1\) must be divisible by no primes except \(2,3\). The factors \(5+1=6\), \(7+1=8\), \(2^a\), and \(3^b\) already meet this condition. Hence the remaining conditions are that \(u+1\) and \(v+1\) are \(\{2,3\}\)-smooth, and
\[
\frac{96}{35}\left(1+\frac1u\right)\left(1+\frac1v\right)>3.
\tag{9}
\]
If \(u\ge23\), then \(v\ge29\), so the left side is at most
\[
\frac{96}{35}\cdot\frac{24}{23}\cdot\frac{30}{29}<3.
\]
For primes \(11\le u\le19\), only \(u=11\) and \(u=17\) have \(u+1\) supported on \(2,3\): the other candidates \(13,19\) have \(14,20\), respectively.

When \(u=11\), equation (9) becomes
\[
1+\frac1v>\frac{385}{384},
\quad\text{equivalently}\quad v<384.
\]
The primes \(11<v<384\) with \(v+1\) supported only on \(2,3\) are exactly
\[
17,23,31,47,53,71,107,127,191,383.
\]
They are exhaustively certified by `support_catalog.csv` and `verify.py`, which use exact trial division and a \(2,3\)-smoothness test on every candidate up to \(383\).

When \(u=17\), equation (9) becomes
\[
1+\frac1v>\frac{595}{576},
\quad\text{equivalently}\quad v<\frac{576}{19}.
\]
The only prime \(17<v<576/19\) with \(v+1\) supported on \(2,3\) is \(v=23\); \(v=19,29\) give \(20,30\), which have a prime divisor \(5\).

**Converse and exponents.** All eleven displayed supports have \(P(n)>3\) by the exact inequalities above, and every factor \(p+1\) for \(p\ge5\) is \(2,3\)-smooth. For \(n\) of either form (2) or (3), with arbitrary \(a,b\ge1\), equation (4) shows that \(\psi(n)\) has exactly the prime support \(\{2,3\}\). Thus (8) holds and \(\varphi(\psi(n))/n=P(n)/3>1\), proving the converse. The support catalog gives in particular
\[
\frac{P(2\cdot3\cdot5\cdot7\cdot11\cdot383)}3=\frac{147456}{147455}>1.
\]
This completes the classification.

## Verification
The standalone `verify.py`, requiring only the Python standard library, reconstructs the rational prime-support bounds, independently enumerates the ten \(u=11\) prime candidates through the exact bound \(v<384\), checks the sole \(u=17\) candidate, and compares all eleven exact rational values against `support_catalog.csv`.

It then directly computes \(\psi(n)\) and \(\varphi(\psi(n))\) for every integer \(2\le n\le400000\) from integer prime-factor sieves. Each comparison against the theorem's support-and-exponent predicate agrees, including the first exceptional value \(n=39270\).

This sweep is corroborative. The proof of exhaustiveness for arbitrarily large \(n\) is the sequence of symbolic support inequalities (7)–(9) plus the complete finite prime check below \(384\).

## Relationship to prior work
Sándor's full paper *On the Composition of Some Arithmetic Functions, II* studies the conjectured inequality \(\varphi(\psi(n))\le n\) and its failure. Theorem 3.23 reduces verification of the non-strict bound from a general integer to its squarefree radical. Remark 3.26 exhibits the six-prime counterexamples \(39270\) and \(82110\), several others, and a seven-prime Mersenne-based family. The paper does not characterize all violating six-prime supports or give the sharp upper prime cutoff \(383\). Its primary 2000 Mathematics Subject Classification is 11A25.

OEIS A196200 defines exactly the counterexample set \(\{n:\varphi(\psi(n))>n\}\). Its listed values begin \(39270,53130,71610,78540,82110,\ldots\) and its entry is dated 21 December 2012. These numerical terms are compatible with the theorem but do not establish uniqueness of the eleven support templates over unbounded exponents.

Guo, Liu, and Yang's paper *On the Composition of the Euler Function and the Dedekind Arithmetic Function* (arXiv:2506.14633v1) studies maximal and average order and densities for ratios of compositions such as \(\psi(\varphi(n))/\varphi(\psi(n))\), rather than the six-support exceptions to \(\varphi(\psi(n))\le n\).

Targeted searches under the exact inequality, the counterexample database identifier, radical reduction, six-prime support, \(2,3\)-smooth successors, and the prime \(383\) yielded no result implying the stated exhaustive classification.

## Limitations
The theorem treats \(\omega(n)\le6\), not larger prime supports. In particular, Sándor's seven-support Mersenne-prime family lies outside the theorem. Several individual counterexamples and the radical reduction are previously known; the new content is the complete necessary-and-sufficient eleven-template classification at the minimal support level.

An unindexed note may contain an equivalent elementary classification. The source date is the exact dated public entry for the defining counterexample sequence, not a fabricated day for the older paper.

## References
1. J. Sándor, “On the Composition of Some Arithmetic Functions, II,” *Journal of Inequalities in Pure and Applied Mathematics* **6** (2005), no. 3, Article 73, especially Theorem 3.23 and Remark 3.26.
2. OEIS Foundation, A196200, “Numbers \(k\) such that Euler phi(Dedekind psi(\(k\))) > \(k\),” original author line 21 December 2012.
3. L. Guo, H. Liu, and J. Yang, “On the Composition of the Euler Function and the Dedekind Arithmetic Function,” arXiv:2506.14633v1 (17 June 2025).
