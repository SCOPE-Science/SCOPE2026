# A sharp three-prime-factor barrier for almost Lehmer numbers

## Finding
A composite positive integer \(n\) is called almost Lehmer when there is a squarefree divisor \(\ell\mid n-1\) such that
\[
\varphi(n)\mid \ell(n-1).
\]
Every almost Lehmer number has at least three distinct prime factors:
\[
\omega(n)\ge 3.
\]
The bound is sharp. The first listed almost Lehmer number is
\[
1729=7\cdot13\cdot19,
\]
and it is already \(1\)-nearly Lehmer because \(3\mid1728\) is squarefree and
\[
\varphi(1729)=1296\mid 3\cdot1728=5184.
\]

## Assumptions and scope
Here \(\varphi\) is Euler's totient function and \(\omega(n)\) is the number of distinct prime divisors of \(n\). The multiplier \(\ell\) is required to be squarefree and to divide \(n-1\), exactly as in the published definition of an almost Lehmer number. The result is unconditional and covers every composite positive integer satisfying that definition; no numerical bound is imposed.

## Proof
Let \(n\) be almost Lehmer and fix an admissible squarefree \(\ell\mid n-1\) with \(\varphi(n)\mid\ell(n-1)\). Because \(\ell(n-1)\) is coprime to \(n\), the divisibility implies
\[
\gcd(n,\varphi(n))=1.
\]
If \(p^2\mid n\), then \(p\mid\varphi(n)\), contradicting this coprimality. If \(n\) is even and composite, then both \(n\) and \(\varphi(n)\) are even, again a contradiction. Hence every almost Lehmer number is odd and squarefree.

It remains to exclude exactly two prime factors. Suppose for contradiction that
\[
n=pq
\]
with distinct odd primes \(p<q\). Put
\[
h=\gcd(p-1,q-1),\qquad p-1=ha,\qquad q-1=hb,
\]
so \(\gcd(a,b)=1\).

Since \(p-1\mid\ell(pq-1)\) and
\[
pq-1\equiv q-1=hb\pmod{p-1},
\]
we have \(a\mid\ell b\), hence \(a\mid\ell\). Symmetrically \(b\mid\ell\). Therefore \(ab\mid\ell\). As \(\ell\) is squarefree, write
\[
\ell=abs,
\]
where \(\gcd(ab,s)=1\).

The condition \(\ell\mid pq-1\) gives \(ab\mid pq-1\). Expanding,
\[
pq-1=(ha+1)(hb+1)-1=h(hab+a+b).
\]
Set \(K=hab+a+b\). For every prime divisor of \(a\), \(K\equiv b\), and for every prime divisor of \(b\), \(K\equiv a\). Since \(\gcd(a,b)=1\), this yields
\[
\gcd(ab,K)=1.
\]
Thus \(ab\mid hK\) forces \(ab\mid h\).

Finally,
\[
\varphi(pq)=h^2ab
\]
and
\[
\ell(pq-1)=abshK.
\]
The defining divisibility therefore gives \(h\mid sK\). Since \(ab\mid h\), we obtain \(ab\mid sK\). Together with \(\gcd(ab,K)=1\), this forces \(ab\mid s\), contradicting \(\gcd(ab,s)=1\) unless \(ab=1\). Hence \(a=b=1\), which gives \(p=q\), contrary to the assumption that the primes are distinct. No semiprime can therefore be almost Lehmer, and \(\omega(n)\ge3\).

The example \(1729\) proves sharpness.

## Verification
The symbolic proof is bound-free. As an independent regression check of the semiprime reduction, `verify.py` tests every pair of distinct odd primes \(p<q\le5000\) using the equivalent reduced-denominator criterion
\[
d=\frac{\varphi(n)}{\gcd(\varphi(n),n-1)}.
\]
An admissible squarefree multiplier exists exactly when \(d\) is squarefree and \(d\mid n-1\). The check finds no semiprime witness among \(222778\) pairs and separately verifies the sharp witness \(1729\) with \(d=3\). This finite computation is corroborating evidence only; it is not used to infer the universal theorem.

## Relationship to prior work
Yamada introduced the almost Lehmer condition as an intermediate notion between Lehmer-type divisibility and broader multiplied variants, and proved asymptotic counting results for almost and nearly Lehmer numbers. The paper also notes the odd squarefree restriction and lists the first examples, beginning with \(1729\), but does not state the sharp support bound \(\omega(n)\ge3\) or exclude the complete semiprime case.

OEIS A337316 records the exact almost Lehmer definition and the initial sequence beginning with \(1729\). OEIS A338998 records the \(1\)-nearly Lehmer sequence and explicitly exhibits the multiplier \(3\) for \(1729\). For comparison, OEIS A238575 lists \(k\)-Lehmer numbers with two prime factors; hence semiprimes do occur for the broader condition in which the multiplier is not constrained to be a squarefree divisor of \(n-1\). The present obstruction therefore uses the defining extra structure of the almost Lehmer class.

## Limitations
The theorem determines the minimum possible number of distinct prime factors but does not classify the three-prime almost Lehmer numbers, determine all admissible multipliers, or sharpen the asymptotic counting results. The originality search cannot rule out an older statement under substantially different terminology outside the checked primary source, exact sequence databases, and semantic literature searches.

## References
1. T. Yamada, “On Almost Lehmer Numbers,” Journal of Integer Sequences 24 (2021), Article 21.5.5; primary MSC 11A25; published April 25, 2021.
2. OEIS A337316, “Almost Lehmer numbers,” with the exact defining condition; public sequence entry dated September 28, 2020.
3. OEIS A338998, “1-nearly Lehmer numbers,” including the witness \(1729\) with multiplier \(3\).
4. OEIS A238575, \(k\)-Lehmer numbers with two prime factors, used only for comparison with the broader multiplied condition.
