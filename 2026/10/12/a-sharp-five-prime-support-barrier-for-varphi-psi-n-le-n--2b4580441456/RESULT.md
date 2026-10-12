# A sharp five-prime-support barrier for \(\varphi(\psi(n))\le n\)
## Finding
Let \(\varphi\) be Euler's totient function, \(\psi(n)=n\prod_{p\mid n}(1+1/p)\) Dedekind's psi function, and \(\omega(n)\) the number of distinct prime divisors. For every integer \(n\ge2\) with \(\omega(n)\le5\), one has \(\varphi(\psi(n))\le n\), with equality if and only if \(n=2\). The support bound is sharp: \(39270=2\cdot3\cdot5\cdot7\cdot11\cdot17\) has \(\omega(39270)=6\) and \(\varphi(\psi(39270))=41472>39270\).

Thus every counterexample to the inequality \(\varphi(\psi(n))\le n\) has at least six distinct prime divisors, and this lower bound on prime support is attained.

## Assumptions and scope
For an integer \(n\ge2\), write \(\omega(n)\) for the number of distinct prime divisors. Euler's totient is \(\varphi\), and Dedekind's function is
\[
\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right).
\]
The claim is unconditional and covers arbitrary prime-power exponents; it is not restricted to squarefree integers. It asserts a sharp threshold in the number of distinct prime divisors, not a classification of all counterexamples with six or more prime divisors.

## Proof
Set
\[
R(n)=\frac{\varphi(\psi(n))}{n}
=\frac{\varphi(\psi(n))}{\psi(n)}\prod_{p\mid n}\left(1+\frac1p\right).
\]
If \(n=2\), then \(\psi(2)=3\) and \(\varphi(3)=2\), so \(R(2)=1\).

Assume next that \(n\) is even and \(n\ne2\). Then \(6\mid\psi(n)\). Indeed, the prime \(2\) contributes a factor \(3\) to \(\psi(n)\); if \(4\mid n\), it also contributes a factor \(2\), while if \(n\) has an odd prime divisor, the corresponding factor \(p+1\) is even. Hence
\[
\frac{\varphi(\psi(n))}{\psi(n)}\le\left(1-\frac12\right)\left(1-\frac13\right)=\frac13.
\]
When \(\omega(n)\le5\), the support product is maximized by the five smallest primes:
\[
\prod_{p\mid n}\left(1+\frac1p\right)
\le \frac32\frac43\frac65\frac87\frac{12}{11}
=\frac{1152}{385}<3.
\]
Therefore \(R(n)<1\) for every even \(n\ne2\) with \(\omega(n)\le5\).

Now let \(n\) be odd. Then every factor \(p+1\) occurring in \(\psi(n)\) is even, so \(2\mid\psi(n)\) and
\[
\frac{\varphi(\psi(n))}{\psi(n)}\le\frac12.
\]
If \(5\nmid n\), the largest possible support product with at most five odd prime divisors is obtained from \(3,7,11,13,17\):
\[
\prod_{p\mid n}\left(1+\frac1p\right)
\le \frac43\frac87\frac{12}{11}\frac{14}{13}\frac{18}{17}
=\frac{4608}{2431}<2.
\]
Thus again \(R(n)<1\).

Finally suppose that \(n\) is odd and \(5\mid n\). Since \(5+1=6\), both \(2\) and \(3\) divide \(\psi(n)\), so \(\varphi(\psi(n))/\psi(n)\le1/3\). The support product is bounded by
\[
\frac43\frac65\frac87\frac{12}{11}\frac{14}{13}
=\frac{1536}{715}<3,
\]
which gives \(R(n)<1\). These cases prove the asserted inequality and its unique equality case.

For sharpness, direct factorization gives
\[
39270=2\cdot3\cdot5\cdot7\cdot11\cdot17,
\qquad
\psi(39270)=124416=2^9 3^5,
\]
and therefore
\[
\varphi(\psi(39270))=2^8\cdot2\cdot3^4=41472>39270.
\]
Hence six distinct prime divisors are already enough for failure.

## Verification
The symbolic proof uses only the product formulas for \(\varphi\) and \(\psi\), divisibility of \(\psi(n)\) by \(2\) and \(3\) in the stated cases, and the three exact rational bounds
\[
\frac{1152}{385}<3,\qquad
\frac{4608}{2431}<2,\qquad
\frac{1536}{715}<3.
\]
The bundled `verify.py` checks these exact inequalities, verifies the displayed counterexample, and independently scans every \(2\le n\le200000\). In that finite range it finds no violation with \(\omega(n)\le5\), finds equality only at \(n=2\), and finds \(39270\) as the first numerical failure. This finite scan is regression evidence only; it is not used to prove the unbounded theorem.

## Relationship to prior work
Sándor's 2005 paper studies the exact composition \(\varphi\circ\psi\), proves that validity for the squarefree kernel implies validity for the original integer, records \(39270\) among counterexamples, and proves an asymptotic density-zero result for large values of \(\varphi(\psi(n))/n\). It does not give a bound on the minimum number of distinct prime divisors in a counterexample. Das's 2023 paper gives another sufficient family for the inequality, again without a prime-support threshold. Alzer and Kwong's 2020 paper provides modern inequalities for the same classical Euler and Dedekind functions and has primary MSC 11A25; it is the dated middle-window source used for scope placement. OEIS A196200 and A364932 record counterexamples and the first numerical failure but do not supply the infinite support theorem.

The new statement is not implied by the known squarefree-kernel reduction: that reduction converts the problem to squarefree supports but still leaves infinitely many five-prime supports to control. The proof above closes all of them simultaneously by forcing small prime factors into \(\psi(n)\) and comparing the maximal possible Dedekind support product.

## Limitations
The result does not classify the six-prime counterexamples, does not determine the density or growth of the exceptional set, and does not improve the quantitative exceptional-set estimates known for unrestricted integers. It establishes only the exact minimum possible value of \(\omega(n)\) for failure and the equality locus inside the safe range.

## References
1. J. Sándor, “On the Composition of Some Arithmetic Functions, II,” Journal of Inequalities in Pure and Applied Mathematics 6 (2005), Article 73. Theorem 3.23 and Remark 3.26 are directly relevant.
2. H. Alzer and M. K. Kwong, “Inequalities for the arithmetical functions of Euler and Dedekind,” Czechoslovak Mathematical Journal 70 (2020), 781–791. DOI: 10.21136/CMJ.2020.0530-18. Published online 2020-01-27; MSC 11A25.
3. B. Das, “On Sandor’s conjecture,” Spectrum: Science and Technology 10 (2023), 9–12. DOI: 10.54290/spect/2023.v10.1.0002. AMS classification 11A25, 11N37.
4. OEIS A196200, “Numbers \(k\) such that Euler \(\varphi(\psi(k))>k\).”
5. OEIS A364932, “\(a(n)=\varphi(\psi(n))\).”
