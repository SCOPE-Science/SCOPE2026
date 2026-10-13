# Prime and prime-power obstructions for weighted-power-mean amicable pairs
## Finding

Let \(\sigma(n)\) denote the sum of the positive divisors of \(n\), let \(s(n)=\sigma(n)-n\) be the proper-divisor sum, and let \(\omega(n)\) count distinct prime divisors. If positive integers \(a,b\) satisfy
\[
a\sigma(a)+b\sigma(b)=(a+b)^2,
\]
then neither coordinate is \(1\) or prime, and the two coordinates cannot both be prime powers. Consequently both coordinates are composite and
\[
\omega(a)+\omega(b)\ge 3.
\]
The bound is sharp because \((4,6)\) satisfies the equation and has total distinct-prime support \(3\).

## Assumptions and scope

A prime power means \(p^r\) with \(p\) prime and \(r\ge1\). The theorem concerns the exponent-one weighted-power-mean condition \(WPM(1)\); it does not claim an analogous result for \(WPM(p)\) with \(p\ge2\).

## Proof

Since \(\sigma(n)=n+s(n)\), the defining equation is equivalent to
\[
a s(a)+b s(b)=2ab. \tag{1}
\]

If \(a=1\), then \(s(b)=2\), impossible: a prime has proper-divisor sum \(1\), while a composite integer has proper divisors \(1\) and at least one divisor at least \(2\), so its proper-divisor sum is at least \(3\). Thus neither coordinate is \(1\).

Suppose \(a=p\) is prime. Since \(s(p)=1\), (1) gives
\[
b\bigl(2p-s(b)\bigr)=p.
\]
Hence \(b\mid p\), so \(b=1\) or \(b=p\). The first case was excluded; the second makes (1) read \(2p=2p^2\), impossible. By symmetry neither coordinate is prime.

Now suppose both coordinates are prime powers:
\[
a=p^r,\qquad b=q^t,
\]
with \(r,t\ge1\). Put
\[
S_p=s(p^r)=1+p+\cdots+p^{r-1},\qquad S_q=s(q^t)=1+q+\cdots+q^{t-1}.
\]
If \(p=q\), assume \(r\le t\). When \(r<t\), divide (1) by \(p^r\) and reduce modulo \(p\):
\[
S_p+p^{t-r}S_q\equiv1\pmod p,
\]
whereas the right side \(2p^t\) is \(0\pmod p\), contradiction. When \(r=t\), (1) forces \(S_p=p^r\), but \(S_p<p^r\).

If \(p\ne q\), reduction of (1) modulo \(p^r\) gives \(p^r\mid q^tS_q\), hence \(p^r\mid S_q\). Therefore \(a\le S_q<b\). Symmetrically \(b\le S_p<a\), giving \(a<b<a\), impossible.

Thus both entries are composite and cannot both have one distinct prime divisor, so \(\omega(a)+\omega(b)\ge3\). Finally,
\[
4\sigma(4)+6\sigma(6)=4\cdot7+6\cdot12=100=(4+6)^2,
\]
so the support bound is attained.

## Verification

The bundled verifier independently computes \(\sigma\) and \(\omega\) through \(3000\), scans every unordered pair in that range, checks the five \(WPM(1)\) examples in the source table, and separately tests every pair of prime powers through the same bound. It returns:

`VERIFY_OK bound=3000 pairs=9 source_examples=5 prime_power_pair_checks=108811`

The finite scan is regression evidence only; the universal theorem is proved symbolically above.

## Relationship to prior work

Dimitrov introduced \(WPM(p)\)-amicable tuples and, for \(p=1\) with two entries, listed \((4,6)\), \((10,16)\), \((34,68)\), \((60,81)\), and \((91,273)\). The inspected source does not state either the prime-coordinate obstruction or the two-prime-power obstruction. The example \((4,6)\) shows the support lower bound is best possible.

The closest indexed adjacent database entry found, OEIS A383714, concerns \(WPM(2)\), namely \(a\sigma(a)^2+b\sigma(b)^2=(a+b)^3\), so it does not imply the exponent-one theorem. A checked result on ordinary harmonious pairs uses the different condition \(a/\sigma(a)+b/\sigma(b)=1\).

## Limitations

The theorem does not classify all \(WPM(1)\)-amicable pairs, does not forbid one coordinate from being a composite prime power, and does not extend automatically to higher weighted-power exponents. An equivalent observation under substantially different terminology remains a residual bibliographic risk.

## References

1. S. I. Dimitrov, *Generalizations of amicable numbers*, arXiv:2408.07387v1, 14 August 2024. Section 7 defines \(WPM(p)\)-amicable tuples and Table 4 lists the \(WPM(1)\) examples. Primary MSC 2020: 11A25.
2. OEIS A383714, entry for \(WPM(2)\)-amicable pairs, used only as an adjacent database comparison.
