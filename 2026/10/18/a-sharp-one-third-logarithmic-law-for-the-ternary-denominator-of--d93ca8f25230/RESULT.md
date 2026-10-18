# A sharp one-third logarithmic law for the ternary denominator of the reciprocal-gcd sum

## Finding
For a positive integer \(n\), let
\[
\mathcal H(n)=\sum_{j=1}^{n}\frac{1}{\gcd(n,j)},
\]
and let \(\operatorname{den}(r)\) denote the positive denominator of a rational number \(r\) in lowest terms. For \(x\ge1\), put
\[
B_3(x)=\#\{1\le n\le x:3\mid\operatorname{den}(\mathcal H(n))\}.
\]
Then
\[
\boxed{B_3(x)\sim C_3\frac{x}{(\log x)^{1/3}}\quad(x\to\infty)},
\]
where \(C_3\) is the explicit, strictly positive constant
\[
\boxed{C_3=\frac{(2/3)^{2/3}}{2\Gamma(2/3)}
\left(\frac{\pi}{3\sqrt3}\right)^{1/3}
\prod_{\substack{p\ \mathrm{prime}\\p\equiv2\pmod3}}
\left(1-\frac1p\right)^{2/3}
\left(1+\frac1p\right)^{1/3}
\sum_{e=0}^{\infty}\frac{3^{-\nu_3(2e+1)}}{p^e}}.
\]
The Euler product converges absolutely, with local factors \(1+O(p^{-2})\). In particular, this natural local denominator obstruction has density zero and a precise logarithmic decay exponent.

## Assumptions and scope
All integers \(n\) are positive; \(\nu_3(t)\) is the exponent of \(3\) in a positive integer \(t\). The limit is as the real parameter \(x\) tends to infinity, with the prime \(3\) fixed. The result does not assert asymptotics for a varying denominator prime or characterize complete integrality of \(\mathcal H(n)\). The implied little-oh is unconditional.

## Proof
**1. Local arithmetic and an exact denominator criterion.** Counting indices with a given greatest common divisor yields
\[
\mathcal H(n)=\frac{h(n)}n,\qquad
h(n)=\sum_{d\mid n}d\varphi(d)
=\prod_{p^e\parallel n}\frac{p^{2e+1}+1}{p+1}.
\]
For \(p\equiv1\pmod3\) and for \(p=3\), the displayed prime-power factor has \(3\)-adic valuation zero. If \(p\equiv2\pmod3\), lifting the exponent in the odd power \(p^{2e+1}+1\) gives
\[
\nu_3\left(\frac{p^{2e+1}+1}{p+1}\right)=\nu_3(2e+1).
\]
Write \(n=3^a m\) with \(3\nmid m\), and define the nonnegative additive prime-power statistic
\[
K(m)=\sum_{\substack{p^e\parallel m\\p\equiv2\pmod3}}\nu_3(2e+1).
\]
The exact identity \(\nu_3(\mathcal H(n))=K(m)-a\) follows, including all boundary cases \(n=1\) and \(e=0\). Consequently,
\[
3\mid\operatorname{den}(\mathcal H(n))\quad\Longleftrightarrow\quad a>K(m).
\]

**2. Dirichlet series and cancellation of first-order prime terms.** For \(\Re s>1\), let \(F(s)=\sum_{n\ge1}\mathbf1_{3\mid\operatorname{den}(\mathcal H(n))}n^{-s}\). Summing the geometric tail over \(a>K(m)\) and using multiplicativity in \(m\) gives the exact identity
\[
F(s)=\frac{3^{-s}}{1-3^{-s}}
\prod_{p\equiv1\pmod3}(1-p^{-s})^{-1}
\prod_{p\equiv2\pmod3}E_p(s),
\quad E_p(s)=\sum_{e\ge0}3^{-s\nu_3(2e+1)}p^{-es}.
\]
Here \(E_p(s)=1+3^{-s}p^{-s}+O(p^{-2\Re s})\), uniformly when \(s\) ranges in a fixed vertical strip \(\Re s>1/2+\epsilon\), \(\Re s\) bounded above. Let \(\chi\) be the nonprincipal real character modulo \(3\), and put
\[
\alpha(s)=\frac{1+3^{-s}}2,\qquad
\beta(s)=\frac{1-3^{-s}}2.
\]
Comparing Euler factors with the Riemann zeta function and \(L(s,\chi)\) gives
\[
F(s)=\zeta(s)^{\alpha(s)}L(s,\chi)^{\beta(s)}G(s),
\]
where the analytic factor \(G\), defined initially on \(\Re s>1\), is
\[
G(s)=\frac{3^{-s}}{1-3^{-s}}(1-3^{-s})^{\alpha(s)}
\prod_{p\equiv2\pmod3}
(1-p^{-s})^{\alpha(s)}(1+p^{-s})^{\beta(s)}E_p(s).
\]
The factors at primes congruent to \(1\) modulo \(3\) cancel identically. At primes congruent to \(2\), the coefficient of \(p^{-s}\) in each factor of the remaining product is \(3^{-s}-\alpha(s)+\beta(s)=0\). Consequently those factors equal \(1+O(p^{-2\Re s})\) locally uniformly, and the product defining \(G\) is absolutely convergent and holomorphic near \(s=1\), with \(G(1)>0\). These estimates and convergence also hold in a fixed strip of real parts greater than \(1/2\), away from the isolated poles of the elementary prefactor.

**3. The logarithmic singularity and coefficient extraction.** Since
\[
\alpha(1)=2/3,\quad\beta(1)=1/3,\quad
L(1,\chi)=\frac{\pi}{3\sqrt3},
\]
and \(\alpha(s)-2/3=O(s-1)\), the standard zero-free neighborhoods of \(\zeta\) and the fixed-conductor \(L\)-function supply, on a slit neighborhood of \(s=1\),
\[
F(s)=(s-1)^{-2/3}\left(
G(1)L(1,\chi)^{1/3}
+O\bigl(|s-1|\log(1/|s-1|)\bigr)\right).
\]
This expansion is not asserted to be holomorphic after removing the fractional power: the variable exponent produces the explicit logarithmic remainder. Applying the standard Selberg--Delange Perron/Hankel-contour argument in its locally varying-exponent form proves
\[
\sum_{n\le x}\mathbf1_{3\mid\operatorname{den}(\mathcal H(n))}
\sim\frac{G(1)L(1,\chi)^{1/3}}{\Gamma(2/3)}
\frac{x}{(\log x)^{1/3}}.
\]
For completeness, the contour argument uses a standard zero-free strip to move the truncated Perron contour to a Hankel contour around \(1\). On its main scale \(s=1+w/\log x\), the preceding error is \(O((\log\log x)/\log x)\) relative to the leading singularity; it therefore contributes \(o(x(\log x)^{-1/3})\). Away from that neighborhood, the usual zero-free-strip bounds and polynomial growth of the Euler and \(L\)-factors give a smaller contribution. The main Hankel integral is \(\Gamma(2/3)^{-1}\). This is an asymptotic theorem, not an inference from finite computation.

**4. Identification and positivity of the constant.** Evaluating the prime \(3\) factor gives
\[
\frac{1/3}{1-1/3}(1-1/3)^{2/3}
=\frac12(2/3)^{2/3}.
\]
The factors at every \(p\equiv2\pmod3\) are exactly those in the boxed Euler product, and each is positive. First-order cancellation makes their deviations from \(1\) of order \(p^{-2}\); their absolutely convergent product is therefore finite and strictly positive. Substitution of \(L(1,\chi)=\pi/(3\sqrt3)\) establishes the stated formula for \(C_3\).

## Verification
An included standalone standard-library Python program (`verify.py`) reconstructs \(\mathcal H(n)\) as exact rational gcd sums for every \(1\le n\le1000\), verifies the prime-power product and exact ternary denominator criterion in the same range, independently counts the criterion for all \(n\le500000\), and evaluates a truncated version of the convergent Euler product. The observed counts are \(B_3(10000)=1479\), \(B_3(100000)=13507\), and \(B_3(500000)=64093\). Using primes below \(20000\) gives \(C_3\approx0.284087846498\); this number is only a truncation, not a rigorously bounded decimal value. The infinite asymptotic is proved by the analytic argument above, not by these tests.

## Relationship to prior work
De Koninck and Letendre introduced the same reciprocal-gcd sum and its multiplicative numerator and studied the much more restrictive condition that the *entire* sum be integral, proving an upper bound for the number of such integers. Their paper does not give the local \(3\)-denominator criterion or the fractional-logarithm counting asymptotic. OEIS A070999 and A071000 distinguish whether the *complete* reduced denominator equals \(n\); they do not provide the prime-specific asymptotic here. Classical Selberg--Delange theory provides the analytic coefficient-extraction method, not this application or its arithmetic Euler factors. The arithmetic identity and the pre-existing general method are not claimed as new independently.

## Limitations
The result concerns only divisibility by \(3\) of the reduced denominator, not its exact exponent, other primes, or full rational integrality. The Euler product is given as an exact constant; the displayed numerical approximation is truncated. Literature discovery cannot exclude unpublished or unindexed equivalent statements. No independent audit of this finding has been performed.

## References
1. J.-M. De Koninck and P. Letendre, *The Integer Values of the Reciprocal-GCD Sum*, arXiv:2610.10572v1, first made public October 4, 2026; original title: *The Integer Values of* \(\sum_{i=1}^n1/\gcd(n,i)\). https://arxiv.org/abs/2610.10572
2. R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929, 2020. https://arxiv.org/abs/2010.12929
3. OEIS A070999, *Numbers for which the denominator of the reciprocal-gcd sum is not equal to the input*. https://oeis.org/A070999
4. OEIS A071000, *Numbers for which the denominator of the reciprocal-gcd sum equals the input*. https://oeis.org/A071000
