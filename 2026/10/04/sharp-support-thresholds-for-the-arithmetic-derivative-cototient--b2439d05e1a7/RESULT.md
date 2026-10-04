# Sharp support thresholds for the arithmetic-derivative cototient gap

## Finding
Define
\[
G(n)=D(n)-(n-\varphi(n)),
\]
where \(D\) is the arithmetic derivative and \(\varphi\) is Euler's totient function.

The first support thresholds of \(G\) are sharp:

* If \(n\) is a composite prime power, then \(G(n)\ge 2\), with equality only for \(n=4\).
* If \(\omega(n)=2\) and \(n\) is not squarefree, then \(G(n)\ge 8\), with equality only for \(n=12\).
* If \(\omega(n)\ge3\), then \(G(n)\ge9\), with equality only for \(n=30\).

The database entry for this function already records the complete fibers at \(0\) and \(1\): \(G(n)=0\) exactly for \(n=1\) and the primes, and \(G(n)=1\) exactly for squarefree semiprimes. Combining those known fibers with the sharp thresholds above gives the complete spectrum through \(9\):
\[
G^{-1}(2)=\{4\},\qquad G^{-1}(3)=\{9\},\qquad G^{-1}(4)=\varnothing,
\]
\[
G^{-1}(5)=\{25\},\qquad G^{-1}(6)=\varnothing,\qquad G^{-1}(7)=\{49\},
\]
\[
G^{-1}(8)=\{8,12\},\qquad G^{-1}(9)=\{18,30\}.
\]

## Assumptions and scope
For a positive integer
\[
n=\prod_{p\mid n}p^{e_p},
\]
the arithmetic derivative is
\[
D(n)=n\sum_{p\mid n}\frac{e_p}{p}.
\]
The cototient is \(n-\varphi(n)\), and \(\omega(n)\) denotes the number of distinct prime factors.

The theorem concerns all positive integers. The finite computation supplied with this package is a regression test only; the inequalities and equality cases are proved for arbitrary \(n\).

## Proof
Let
\[
R=\operatorname{rad}(n)=\prod_{p\mid n}p.
\]
From Euler's product formula and the arithmetic-derivative factorization formula,
\[
\frac{G(n)}{n}
=
\sum_{p\mid n}\frac{e_p}{p}-1+
\prod_{p\mid n}\left(1-\frac1p\right).
\]
Hence
\[
\frac{G(n)}{n}
=
\frac{G(R)}{R}+
\sum_{p\mid n}\frac{e_p-1}{p}.
\]
This identity isolates the contribution from repeated prime factors.

For a prime power \(n=p^e\),
\[
D(p^e)=e p^{e-1},\qquad p^e-\varphi(p^e)=p^{e-1},
\]
so
\[
G(p^e)=(e-1)p^{e-1}.
\]
For \(e\ge2\), the minimum is \(2\), attained only at \((p,e)=(2,2)\), namely \(n=4\). Moreover, the prime-power values at most \(9\) are
\[
2,3,5,7,8,
\]
coming respectively from
\[
4,9,25,49,8.
\]
Indeed, when \(e=2\) the value is \(p\); when \(e=3\), the only value at most \(9\) is \(2\cdot2^2=8\); and \(e\ge4\) gives at least \(3\cdot2^3=24\).

Now suppose \(n=p^a q^b\), where \(p<q\) are distinct primes. Direct calculation gives
\[
G(n)=p^{a-1}q^{b-1}
\left((a-1)q+(b-1)p+1\right).
\]
If \(a=b=1\), then \(G(n)=1\), the known squarefree-semiprime fiber. If \(n\) is not squarefree, then either \(a\ge2\) or \(b\ge2\). In the first case,
\[
G(n)\ge p(q+1)\ge2(3+1)=8,
\]
and equality forces \(p=2\), \(q=3\), \(a=2\), \(b=1\), giving \(n=12\). In the second case with \(a=1\),
\[
G(n)\ge q(p+1)\ge3(2+1)=9,
\]
and equality forces \(p=2\), \(q=3\), \(b=2\), giving \(n=18\). Thus the only two-prime-support values at most \(9\), apart from the squarefree value \(1\), are \(8\) at \(12\) and \(9\) at \(18\).

It remains to treat at least three distinct primes. First suppose \(m\) is squarefree. For a prime \(q\nmid m\), the Leibniz rule and multiplicativity of \(\varphi\) give
\[
G(qm)=qG(m)+(m-\varphi(m)).
\]
For three distinct primes \(p<q<r\), direct expansion gives
\[
G(pqr)=p+q+r-1.
\]
Therefore
\[
G(pqr)\ge2+3+5-1=9,
\]
with equality only for \(pqr=30\). Adding further squarefree prime factors strictly increases the value by the displayed recursion.

Finally, if \(\omega(n)\ge3\) and \(n\) is not squarefree, then the radical identity gives
\[
G(n)
=n\left(\frac{G(R)}R+
\sum_{p\mid n}\frac{e_p-1}{p}\right)
>\frac nR G(R)\ge G(R)\ge9.
\]
Thus \(9\) is the sharp threshold for three-or-more-prime support and is attained only at \(n=30\).

Collecting the prime-power, two-prime, and at-least-three-prime cases yields the complete fibers through \(9\) stated above.

## Verification
The accompanying `verify.py` independently constructs smallest-prime-factor data through \(10^6\), computes \(D(n)\), \(\varphi(n)\), \(G(n)\), and \(\omega(n)\), and checks every integer in that range against the claimed small-value fibers and sharp support bounds.

It also checks the exact algebraic formulas for prime powers and two-prime-support integers encountered in the range. A successful replay prints `VERIFY_OK`.

The finite replay is not used as proof for integers beyond the checked range.

## Relationship to prior work
OEIS A344178 is exactly the sequence
\[
G(n)=D(n)-(n-\varphi(n)).
\]
Its current entry records nonnegativity and gives complete descriptions only for the fibers \(G(n)=0\) and \(G(n)=1\). It does not state the support-stratified lower bounds or the complete fibers from \(2\) through \(9\).

The arithmetic derivative and the factorization formula
\[
D(n)=n\sum_{p\mid n}\frac{\nu_p(n)}p
\]
are standard in the arithmetic-derivative literature. Haukkanen, Merikoski, and Tossavainen treat arithmetic subderivatives in a paper classified primarily under MSC \(11A25\). That paper does not discuss the cototient or OEIS A344178.

Targeted searches for the exact function, the fibers through \(9\), and the support-threshold formulations did not locate a prior statement implying the theorem.

## Limitations
The result determines only the initial low-value spectrum and the first sharp threshold in each support regime. It does not classify the general fiber \(G^{-1}(k)\) for arbitrary \(k\), nor does it give an asymptotic distribution for \(G(n)\).

The main residual originality risk is an unindexed elementary note or database comment giving the same low-value classification. The current canonical database entry does not do so.

## References
1. OEIS A344178, “Difference between the arithmetic derivative of \(n\) and the cototient of \(n\),” authored May 23, 2021.
2. Pentti Haukkanen, Jorma K. Merikoski, and Timo Tossavainen, “Arithmetic Subderivatives: Discontinuity and Continuity,” Journal of Integer Sequences 22 (2019), Article 19.7.4; primary MSC 11A25.
