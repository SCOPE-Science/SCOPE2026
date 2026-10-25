# Complete coprime two-cycles for the first positive shift of a reciprocal quadratic divisibility system

## Finding
Let \(F_c(t)=t^2-t+c\) for positive integers \(c\). For distinct, coprime positive integers \(a<b\),
\[
a\mid F_2(b),\quad b\mid F_2(a)
\]
holds exactly when, for a unique positive integer \(d\) that is odd or divisible by \(4\),
\[
a=\frac{d^2-d+2}{2},\qquad b=\frac{d^2+d+2}{2}.
\]
In particular these conditions have infinitely many coprime solutions. The distinct-prime pairs are precisely the specializations
\[
(a,b)=(8m^2-2m+1,\ 8m^2+2m+1),\qquad m\ge1,
\]
for which both entries are prime. Explicit examples are \((7,11)\), \((29,37)\), \((67,79)\), and \((191,211)\). The infinitude of such prime specializations is not established.

## Assumptions and scope
The result concerns positive integer pairs satisfying \(\gcd(a,b)=1\) and \(a<b\). Reversing coordinates gives the corresponding \(a>b\) case. For \(a=b\), coprimality forces \(a=b=1\), which satisfies both divisibilities. Noncoprime pairs are not classified. The source polynomial with constant \(1\), \(F_1(t)=t^2-t+1\), is the prime-value polynomial in De Koninck–Letendre (2026). Its reciprocal system has only \((1,1)\) among positive pairs by Mills (1953). Replacing the constant by the next positive integer \(2\) is the precise change studied here.

## Proof
**Step 1 (an integral invariant).** Put \(d=b-a>0\). Reducing the hypotheses modulo the two entries gives
\[
a\mid d^2-d+2,\qquad b\mid d^2+d+2.
\]
Write \(ka=d^2-d+2\) and \(\ell b=d^2+d+2\) with \(k,\ell\) positive integers. Subtraction gives \(ka-\ell b=-2d\), equivalently \((k-\ell)a=(\ell-2)d\). Since \(\gcd(a,d)=\gcd(a,b)=1\), there is an integer \(t\) with \(\ell=2+ta\), and consequently \(k=2+tb\). Thus
\[
d^2-a-b+2=tab.
\]
As \(d^2-a-b+2+ab=d^2+(a-1)(b-1)+1>0\), the integer \(t\) is nonnegative. This is an *exact* algebraic consequence, with no numerical assumption.

**Step 2 (strict descent).** Rewriting the invariant as a quadratic equation in \(b\) gives
\[
b^2-((t+2)a+1)b+(a^2-a+2)=0.
\]
The other root is the positive integer \(b'=(a^2-a+2)/b\), by the original divisibility. For \(a\ge2\), because \(b>a\) and \(a^2-a+2\le a^2\), one has \(0<b'<a\). Vieta's formulas show that \((b',a)\) satisfies the **same integer-parameter equation**
\[
(b'-a)^2-b'-a+2=t ab'.
\]
This descent does not require that subsequent pairs remain coprime: integrality of \(t\) was proved before the first step, and the invariant itself is preserved. Each step strictly decreases the larger entry. It stops with \(a=b\) or with a smaller entry equal to \(1\). A diagonal positive pair satisfies \(2-2a=t a^2\), so with \(t\ge0\) it must have \(a=1\), \(t=0\). For the remaining case \((1,b)\), the invariant reduces to \((b-1)(b-2)=tb\). Since \(b\mid2\), one has \(b=1\) or \(2\), and either choice forces \(t=0\). Hence the original invariant always has \(t=0\).

**Step 3 (parameterization and converse).** Consequently \(d^2-a-b+2=0\). Combining this with \(b-a=d\) determines \(a=(d^2-d+2)/2\), \(b=(d^2+d+2)/2\). Conversely, for any integer \(d\ge1\), these two values are positive integers and satisfy
\[
d^2-d+2=2a,\quad d^2+d+2=2b.
\]
Reducing \(F_2(b)\) modulo \(a\), and \(F_2(a)\) modulo \(b\), proves the two divisibilities. Their gcd equals \(\gcd(a,d)\). For odd \(d\), reduction of \(2a=d^2-d+2\) modulo \(d\) gives \(a\equiv1\pmod d\), so the gcd is \(1\). For \(d=2k\), \(a=2k^2-k+1\), hence \(\gcd(a,k)=1\) and \(\gcd(a,2k)\) is \(1\) when \(k\) is even, and \(2\) when \(k\) is odd. Therefore coprimality holds exactly for odd \(d\) or multiples of \(4\). Uniqueness of \(d\) follows from \(d=b-a\).

**Step 4 (prime specialization).** If \(a<b\) are primes, both must be odd: \(a=2\) requires \(d^2-d+2=4\), whose only positive integer solution is \(d=2\), giving \((2,4)\) rather than a prime pair. For odd \(d\), the entries have opposite parity and both entries exceed \(2\) once \(d\ge3\); at \(d=1\) the smaller entry is \(1\). Therefore \(d\) must be even. The exact coprimality criterion forces \(4\mid d\), so \(d=4m\) with \(m\ge1\), yielding exactly the displayed quadratic prime-pair family, conditional on both polynomial values being prime.

## Verification
The standalone program `verify_reciprocal2.py` checks the reciprocal identities for \(7{,}999\) consecutive positive parameters, directly enumerates all coprime reciprocal pairs with smaller coordinate under \(3{,}000\) by exact divisors, verifies their parameterization, and checks four displayed prime examples by trial division. Its execution yields `VERIFY_OK coprime_pairs=58 parameter_cases=7999 prime_examples=4`. These finite checks are consistency tests; the infinite assertions follow from Steps 1–4.

## Relationship to prior work
De Koninck and Letendre, *The Integer Values of a Reciprocal-GCD Sum* (arXiv:2610.10572v1, first posted 2026-10-04), use \(F_1(t)=t^2-t+1\) in their reciprocal-prime divisor graph and establish quantitative bounds for possible two-cycles. Mills, *A system of quadratic Diophantine equations* (1953), Theorem 3, already rules out all positive nontrivial reciprocal two-cycles for \(F_1\). The present theorem concerns instead the first positive constant perturbation \(F_2\) and gives its exact **coprime** solution set, including an infinite quadratic integer family and an explicit characterization of prime specializations. Mills's broader classification fixes constant term \(1\) and varies the linear coefficient, so its stated results do not imply the constant-term-\(2\) classification. Standard Vieta jumping is a proof method, not itself an instance of this arithmetic classification.

## Limitations
The theorem does not classify pairs with \(\gcd(a,b)>1\), does not assert infinitely many prime specializations, and gives no quantitative prime-pair density. It does not change the conclusions of the originating reciprocal-gcd paper for its original constant-\(1\) polynomial. Priority remains subject to independent bibliographic review for less-indexed related quadratic congruences.

## References
1. J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^{n}1/\gcd(n,i)\)*, arXiv:2610.10572v1 (2026-10-04), https://arxiv.org/html/2610.10572v1.
2. W. H. Mills, *A system of quadratic Diophantine equations*, Pacific Journal of Mathematics **3** (1953), 209–220, especially Theorem 3, https://msp.org/pjm/1953/3-1/pjm-v3-n1-p15-p.pdf.
3. General methodological comparison: Vieta jumping (root-flip descent) in simultaneous quadratic divisibility systems; the precise constant-term-\(2\) parameterization is established above.
