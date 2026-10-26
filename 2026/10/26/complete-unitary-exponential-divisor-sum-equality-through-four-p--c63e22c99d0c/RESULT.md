# Complete unitary–exponential divisor-sum equality through four prime factors

## Finding
For every integer \(n>1\), let \(\Omega(n)\) be the total number of prime factors of \(n\), counted with multiplicity. Let \(\sigma^*(n)\) denote the sum of its unitary divisors and \(\sigma^{(e)}(n)\) the sum of its exponential divisors. Then
\[
\Omega(n)\le4\quad\text{and}\quad\sigma^*(n)=\sigma^{(e)}(n)
\quad\Longleftrightarrow\quad n\in\{20,45\}.
\]
The structural step is that no product \(pqr^2\), for pairwise distinct primes \(p,q,r\), can satisfy the equality. Both listed values actually do satisfy it: the common divisor sums are respectively \(30\) and \(60\). Under the usual convention \(\sigma^*(1)=\sigma^{(e)}(1)=1\), the additional equality value \(1\) appears when \(n=1\) is included.

## Assumptions and scope
The unitary divisors of \(n\) are the divisors \(d\) with \(\gcd(d,n/d)=1\). For \(n=\prod_i p_i^{a_i}\), an exponential divisor takes exponent \(b_i\) satisfying \(b_i\mid a_i\) at each prime \(p_i\). Thus both divisor-sum functions are multiplicative and
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
All primes are positive rational primes; all exponents are positive integers. There is no bound on the magnitudes of the primes or on \(n\), only the stated restriction \(\Omega(n)\le4\). The result is a complete classification within that unrestricted infinite domain, not a finite-range census.

## Proof
**1. Prime-exponent shapes.** At a prime occurring to exponent \(1\), \(\sigma^*(p)=p+1>p=\sigma^{(e)}(p)\). For any exponent \(a\ge2\), the exponential sum contains at least \(p+p^a\), so \(\sigma^{(e)}(p^a)>\sigma^*(p^a)=p^a+1\). Since both functions are positive and multiplicative, equality for \(n>1\) requires at least one prime occurring once and at least one occurring more than once. If \(\Omega(n)\le4\), the only possible shapes, up to renaming distinct primes, are \(p^2q\), \(p^3q\), and \(pqr^2\).

**2. Two-prime shapes.** For \(a\in\{2,3\}\), the positive divisors of \(a\) are \(1,a\), so equality at \(p^a q\) reduces exactly to
\[
(p^a+1)(q+1)=q(p^a+p)
\quad\Longleftrightarrow\quad
q(p-1)=p^a+1.
\]
Reduction modulo \(p-1\) gives \(p-1\mid2\), hence \(p=2\) or \(p=3\). If \(a=2\), then \((p,q)=(2,5)\) or \((3,5)\), giving \(20\) and \(45\). If \(a=3\), the prospective values of \(q\) are \(9\) and \(14\), neither prime. There are no other cases.

**3. Three-prime shape.** Suppose distinct primes \(p<q\) and \(r\) satisfied \(\sigma^*(pqr^2)=\sigma^{(e)}(pqr^2)\). The equality is
\[
(p+1)(q+1)(r^2+1)=pqr(r+1). \tag{1}
\]
Dividing by \(pq(r^2+1)\) yields
\[
\left(1+\frac1p\right)\left(1+\frac1q\right)
=1+\frac{r-1}{r^2+1}.
\]
If either \(p\le r\) or \(q\le r\), then the left side exceeds \(1+1/r\), whereas the right side is less than \(1+1/r\). Consequently \(r<p<q\).

Reducing (1) modulo \(q\), and using \(p+1<q\), proves \(q\mid r^2+1\). If also \(p\mid r^2+1\), then \(pq\mid r^2+1\), impossible since \(p,q>r\) imply \(pq>(r+1)^2>r^2+1\). Reducing (1) modulo \(p\) therefore proves \(p\mid q+1\).

Put \(t=(r^2+1)/q\ge1\) and \(k=(q+1)/p\ge2\). Substitution into (1), cancelling \(pq\), gives \(kt(p+1)=r(r+1)\). But
\[
kt(p+1)=t(q+1+k)=r^2+1+t(k+1),
\]
so
\[
t(k+1)=r-1. \tag{2}
\]
Because \(t\) divides both \(r^2+1\) and \(r-1\), it divides their gcd, which equals \(\gcd(r-1,2)\). For \(r=2\), equation (2) forces \(t=1\) and \(k=0\), contrary to \(k\ge2\). For odd \(r\), the number \(r^2+1\) is even and \(q\) is odd, so \(t\) is even; consequently \(t=2\). Equation (2) gives \(k=(r-3)/2\ge2\), and hence \(r\ge7\). Finally,
\[
q=\frac{r^2+1}{2},\qquad
p=\frac{q+1}{k}=\frac{r^2+3}{r-3}=r+3+\frac{12}{r-3}.
\]
Since \(p\) is an integer, \(r-3\mid12\). With \(r\ge7\) an odd prime, the only possible \(r\) is \(7\): indeed \(r-3\) must be an even divisor of \(12\) at least \(4\), giving \(r\in\{7,9,15\}\). But \(r=7\) gives \(q=25\), not a prime. This contradiction eliminates the three-prime shape, proving the classification.

## Verification
The standard-library Python program `verify.py` independently computes both divisor sums from prime factorizations for every integer \(2\le n\le10^6\) with \(\Omega(n)\le4\). It checks \(737448\) such integers and finds equality only at \(20\) and \(45\). It separately scans the necessary algebraic reductions for all \(2262\) primes \(r\le20000\), with the only putative odd-prime divisibility candidate \((r,p,q)=(7,13,25)\) rejected because \(25\) is composite. Run `python verify.py` with Python 3; expected final output begins `VERIFY_OK:`. These calculations corroborate, but do not replace, the unbounded divisibility proof in the preceding section.

## Relationship to prior work
Trudgian's *The sum of the unitary divisor function* (arXiv:1312.4615, first submitted 2013-12-17) explicitly asks whether equality of the unitary and exponential divisor sums occurs infinitely often and records sparse examples. OEIS A236474 lists known equality values but gives no exhaustive theorem for a prescribed total number of prime factors. A separate result, *The first 49 exponent layers of the unitary–exponential divisor-sum equality* (2026), treats only the two-prime form \(p^a q\) with \(2\le a\le49\); it covers the two-prime cases here but not the three-distinct-prime obstruction \(pqr^2\). Minculete's 2013 inequalities concern different relationships among exponential and unitary divisor functions. Lelechenko's 2014 paper treats the mean values and extremal orders of exponential and infinitary divisor functions, rather than the stated equality classification. The structural obstruction and the resulting \(\Omega(n)\le4\) classification were not found in the inspected sources.

## Limitations
This theorem makes no assertion about equality for \(\Omega(n)\ge5\), the total infinitude question, or modifications of either divisor-sum definition. It does not claim the values \(20\) and \(45\) were previously unknown. Literature coverage is necessarily incomplete, so an equivalent classification in an unlocated source remains possible. Independent mathematical validation has not been performed.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615 (initial submission 2013-12-17); *Publications de l'Institut Mathématique* 97(111) (2015), 175–180, DOI: 10.2298/PIM140617001T.
2. OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*, https://oeis.org/A236474.
3. N. Minculete, *A note about properties of exponential divisors*, *Applied Mathematics & Information Sciences* 7 (2013), 319–322, https://www.naturalspublishing.com/download.asp?ArtcID=2200.
4. A. V. Lelechenko, *Exponential and infinitary divisors*, arXiv:1405.7597, first submitted 2014-05-29.
5. *The first 49 exponent layers of the unitary–exponential divisor-sum equality* (2026), public research record identifier 59314f8e910e.
