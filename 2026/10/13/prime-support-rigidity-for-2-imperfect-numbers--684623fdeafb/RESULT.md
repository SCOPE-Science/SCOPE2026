# Prime-support rigidity for 2-imperfect numbers

## Finding
For the multiplicative alternating divisor-sum function \(\beta\), define \(\beta(1)=1\) and, at every prime power,
\[
\beta(p^a)=p^a-p^{a-1}+p^{a-2}-\cdots+(-1)^a
=\frac{p^{a+1}+(-1)^a}{p+1}.
\]
An integer \(n\ge1\) is called *2-imperfect* when \(2\beta(n)=n\). The complete classification at prime support at most two is
\[
\boxed{\ 2\beta(n)=n\ \text{ and }\ \omega(n)\le2\ \Longleftrightarrow\ n\in\{2,12,40\}.\ }
\]
Here \(\omega(n)\) counts distinct prime divisors, with \(\omega(1)=0\). The support boundary is attained: \(252=2^2\cdot3^2\cdot7\) is 2-imperfect, so three distinct primes are possible.

## Assumptions and scope
The result holds for all positive integers without a magnitude or exponent cutoff. All prime bases are ordinary positive primes. The claim makes no assertion that the full set of 2-imperfect numbers is finite. The underlying function is also written \(\rho\) in earlier literature; it is not the nonmultiplicative alternating sum over numerically ordered divisors.

## Proof
**1. Reduction to an even integer.** Since \(2\beta(n)\) is even, every solution is even and thus \(n>1\). If \(\omega(n)\le2\), then \(n=2^a\) or \(n=2^a p^b\), where \(a,b\ge1\) and \(p\) is an odd prime. We have
\[
U_a:=\beta(2^a)=\frac{2^{a+1}+(-1)^a}{3},
\]
which is a positive odd integer. The equality \(2U_a=2^a\) for a pure power of two is equivalent to \(2^a+2(-1)^a=0\), forcing \(a=1\), namely \(n=2\).

**2. Local-ratio bound.** Suppose \(n=2^a p^b\). Multiplicativity makes the defining equality equivalent to
\[
R_{p,b}:=\frac{\beta(p^b)}{p^b}=T_a:=\frac{2^{a-1}}{U_a}
=\frac{3}{4+(-1)^a2^{1-a}}.
\]
For \(a=1\), \(T_a=1\), whereas \(\beta(p^b)<p^b\); hence \(a\ge2\). At these exponents,
\[
T_a\le\frac45,
\quad T_a<\frac34\ \text{if }a\text{ is even},
\quad T_a>\frac34\ \text{if }a\text{ is odd}.
\]
Equality \(T_a=4/5\) occurs only at \(a=3\). Indeed, on odd exponents \(a\ge3\) the displayed denominator strictly increases with \(a\), while on even exponents \(T_a<3/4\).

For every odd prime \(p\) and integer \(b\ge1\), the prime-power formula yields
\[
R_{p,b}=\frac{p+(-1)^b p^{-b}}{p+1}\ge\frac{p-1}{p}.
\]
The inequality is equality only for \(b=1\). Thus \(p\ge7\) is impossible, because \(R_{p,b}\ge6/7>4/5\ge T_a\).

**3. The prime \(5\).** If \(p=5\), then \(R_{5,1}=4/5\), whereas \(R_{5,b}>4/5\) for every \(b\ge2\): for even \(b\) it is greater than \(5/6\), while for odd \(b\ge3\) its negative correction \(5^{-b}\) is smaller than at \(b=1\). Therefore \(b=1\) and \(T_a=4/5\). The unique possibility is \(a=3\), which gives \(n=40\).

**4. The prime \(3\).** If \(p=3\) and \(b\) is even, then \(\beta(3^b)\) is odd, as is \(U_a\). Consequently the left side of \(2U_a\beta(3^b)=2^a3^b\) has 2-adic valuation exactly one, forcing \(a=1\), already excluded. Hence \(b\) is odd. Now
\[
R_{3,b}=\frac{3-3^{-b}}4<\frac34,
\]
so \(a\) is even. Inserting the prime-power formulas into \(2U_a\beta(3^b)=2^a3^b\) gives
\[
(2^{a+1}+1)(3^{b+1}-1)=2^{a+1}3^{b+1},
\]
and hence
\[
3^{b+1}=2^{a+1}+1.
\]
Write \(c=(b+1)/2\), a positive integer. Then
\[
(3^c-1)(3^c+1)=2^{a+1}.
\]
The two positive even factors on the left are powers of two that differ by exactly two; they must therefore be \(2\) and \(4\). Thus \(3^c=3\), \(c=1\), \(b=1\) and \(a=2\), giving \(n=12\).

**5. Converse and boundary.** Direct evaluation gives \(\beta(2)=1\), \(\beta(12)=\beta(4)\beta(3)=3\cdot2=6\) and \(\beta(40)=\beta(8)\beta(5)=5\cdot4=20\). All three satisfy the required equation. Finally \(\beta(252)=\beta(4)\beta(9)\beta(7)=3\cdot7\cdot6=126\), and \(252\) has three distinct prime factors. This completes the classification and establishes the sharp support boundary.

## Verification
The included `verify.py` implements the prime-power definition twice, by trial factorization and by a smallest-prime-factor sieve. Running `python3 verify.py` checks all positive integers up to \(300000\) and independently tests the exponential reduction at even \(2\le a\le118\) and odd \(1\le b\le99\). The exact run output was:

```text
VERIFY_OK limit=300000 support_le2_count=119838 all_hits=[2, 12, 40, 252, 880, 10880, 75852] two_support_hits=[2, 12, 40] sharp_boundary=252 checked_power_box=a2..118_even_b1..99_odd
```

These finite checks are corroboration only; all unbounded quantifiers are settled by the argument in the Proof section.

## Relationship to prior work
Iannucci (2006) uses the same arithmetic function under the name \(\rho\), defines 2-imperfect integers and tabulates initial examples, including \(2,12,40\). Zhou and Zhu (2009) establish that the only squarefree \(k\)-imperfect integers are \(2\) and \(6\), together with broader necessary conditions and finite calculations, but do not state the full 2-imperfect classification for arbitrary two-prime exponents. Tóth (2013/2014) surveys the arithmetic function and gives a sufficient Fermat-number construction, without establishing the converse here. OEIS A127725 records the known witnesses; a numerical list does not imply the unbounded classification proved above.

## Limitations
The proof restricts only the number of distinct prime factors. It does not classify 2-imperfect numbers with three or more distinct primes, nor does it resolve their infinitude. The originality comparison covers the inspected primary sources and database but cannot exclude unindexed prior elementary arguments. Computational agreement below the stated cutoff is not an infinite proof.

## References
1. Douglas E. Iannucci, *On a Variation of Perfect Numbers*, **Integers** 6 (2006), A41, published 2006-12-20. https://math.colgate.edu/~integers/g41/g41.pdf
2. Weiyi Zhou and Long Zhu, *On k-Imperfect Numbers*, **Integers** 9 (2009), A01. https://math.colgate.edu/~integers/j1/j1.pdf
3. László Tóth, *A Survey of the Alternating Sum-of-Divisors Function*, **Acta Universitatis Sapientiae, Mathematica** 5 (2013), 93–107; arXiv:1111.4842, first submitted 2011. https://arxiv.org/abs/1111.4842
4. OEIS A127725, *2-imperfect numbers*, originating 2007. https://oeis.org/A127725
