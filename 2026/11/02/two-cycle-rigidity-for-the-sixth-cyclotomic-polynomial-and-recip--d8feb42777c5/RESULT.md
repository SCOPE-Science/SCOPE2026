# Two-cycle rigidity for the sixth cyclotomic polynomial and reciprocal-gcd integrality

## Finding

**Theorem (complete two-cycle exclusion).** Let \(\Phi_6(z)=z^2-z+1\). For all positive integers \(a,b\),
\[
a\mid\Phi_6(b)\quad\text{and}\quad b\mid\Phi_6(a)
\iff a=b=1.
\]
In particular, the divisibility graph on primes, with an arrow from \(p\) to \(q\) when \(q\mid\Phi_6(p)\), has no directed loops or directed two-cycles.

**Reciprocal-gcd consequence.** Put
\[
\mathcal{H}(n)=\sum_{i=1}^n\frac{1}{\gcd(n,i)}.
\]
For every pair of distinct primes \(p,q\), the value \(\mathcal{H}(pq)\) is nonintegral. The same holds for prime squares. Consequently, the only squarefree integers \(n\) with \(\mathcal{H}(n)\in\mathbb Z\) and at most two prime factors are \(n=1\); every nontrivial squarefree solution has at least three distinct prime factors.

## Assumptions and scope

All variables in the two-cycle theorem are *positive integers*, not necessarily primes, and divisibility is ordinary integer divisibility. The two-cycle conclusion concerns the polynomial \(\Phi_6\), not general cyclotomic polynomials. For \(\mathcal H\), \(n\ge1\) and \(p,q\) are distinct primes unless explicitly indicated. No claim is made about numbers supported on exactly two primes when one or both exponents exceed one.

## Proof

1. If one of \(a,b\) equals \(1\), then the other divides \(\Phi_6(1)=1\), hence both equal \(1\). If \(a=b\), then \(a\mid\Phi_6(a)\equiv1\pmod a\), so again \(a=b=1\).

2. Otherwise suppose \(2\le a<b\), and assume both divisibilities. Any common divisor of \(a\) and \(b\) would divide \(\Phi_6(a)\equiv1\pmod a\), so \(\gcd(a,b)=1\). Since \(a\mid\Phi_6(b)\), \(b\mid\Phi_6(a)\), and \(\Phi_6(t)\equiv1\pmod t\), it follows by reducing modulo each factor that
\[
 ab\mid\Phi_6(a)+\Phi_6(b)-1.
\]
Write the quotient as a positive integer \(K\). The equation is
\[
 b^2-(Ka+1)b+\Phi_6(a)=0.
\]

3. The second root of this monic quadratic is the positive integer
\[
 r=(Ka+1)-b=\frac{\Phi_6(a)}{b}.
\]
Because \(b>a\ge2\) and \(\Phi_6(a)=a^2-a+1<a^2\), one has \(1\le r<a\). The root sum also yields \(r\equiv1-b\pmod a\). The identity \(\Phi_6(1-z)=\Phi_6(z)\) implies
\[
 a\mid\Phi_6(r),\qquad r\mid\Phi_6(a).
\]
Thus \((r,a)\) is another solution with strictly smaller sum than \((a,b)\). Choosing a nontrivial solution with minimal sum contradicts this descent. Hence only \((1,1)\) exists. Note that the end point \(r=1\) cannot occur with \(a>1\), because then \(a\mid\Phi_6(1)=1\).

4. For any prime-power factorization \(n=\prod_{p^e\parallel n}p^e\), grouping terms by \(\gcd(n,i)\) gives the exact multiplicative identity
\[
 n\mathcal{H}(n)=\prod_{p^e\parallel n}\frac{p^{2e+1}+1}{p+1}.
\]
Indeed, the factor at \(p^e\) is \(\sum_{j=0}^e p^j\varphi(p^j)\), which equals the displayed alternating quotient. For \(n=pq\), it specializes to \(pq\mathcal H(pq)=\Phi_6(p)\Phi_6(q)\). As \(\gcd(p,\Phi_6(p))=\gcd(q,\Phi_6(q))=1\), integrality would imply \(p\mid\Phi_6(q)\) and \(q\mid\Phi_6(p)\), contradicting the theorem. For \(n=p^2\), the numerator \((p^5+1)/(p+1)\equiv1\pmod p\), so \(\mathcal H(p^2)\) is nonintegral. For \(n=p\), the same follows from \(\Phi_6(p)\equiv1\pmod p\).

The graph statement follows immediately: \(p\mid\Phi_6(p)\) is impossible for prime \(p\), and two opposing edges between distinct primes violate the theorem.

## Verification

Run `python3 verify.py` with the standard Python library. The checker tests every unordered integer pair \(2\le a<b\le5000\), every prime pair with both primes at most \(5000\), and independently compares the product identity for \(\mathcal H(n)\) with the direct rational sum for \(1\le n\le600\). It also checks \(\mathcal H(614341)=486361\), showing the integer-valued problem itself is nonempty beyond \(1\). It contrasts \(\Phi_4(z)=z^2+1\), for which \((2,5)\) *does* form a two-cycle. These tests are finite sanity checks; the unrestricted proof is the descent above.

## Relationship to prior work

De Koninck and Letendre, *The Integer Values of \(\sum_{i=1}^n 1/\gcd(n,i)\)* (arXiv:2610.10572, first posted 2026-10-04), supply the multiplicative formula and a global thin-set counting bound. Section 5, Proposition 1, counts putative squarefree two-prime mutual-divisibility pairs of exactly the displayed type by a nonzero upper bound. The present theorem excludes that entire class, a stronger statement on the two-prime case, but does **not** improve the paper's global \(\ll X^{2/3+\varepsilon}\) bound for all integers. The paper's displayed small examples do not establish nonexistence at arbitrary prime sizes.

Vieta jumping is an established Diophantine proof technique; the contribution here is the specific complete \(\Phi_6\) two-cycle obstruction and its application to the reciprocal-gcd factor graph. A stronger general theorem might already imply this elementary case. No claim of independent external verification or of a new bound for arbitrary prime-power supports is made.

## Limitations

The nontrivial factor graph can have longer directed cycles, and this result does not exclude squarefree solutions with three or more primes. It also does not address mixed prime powers. Finite searches alone would not exclude large counterexamples; the proof does. Priority relative to all earlier Diophantine literature remains subject to independent checking.

## References

1. J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^n 1/\gcd(n,i)\)*, arXiv:2610.10572 (2026-10-04), https://arxiv.org/html/2610.10572v1 ; MSC2020 11N37, 11N64.
2. H. Nguyen and T. Nguyen, *Solving number theory problems with cyclic and symmetric variables* (2013), https://www.cs.cmu.edu/~hn1/documents/cyclic-number-theory/cyclic-number-theory.html (general Vieta-jumping method; no assertion of the above \(\Phi_6\) classification established from the inspected material).
