# Exact collision fibers of \(n+\tau(n)\) on \(2\)-almost-primes

## Finding
Let \(\tau(n)\) denote the number of positive divisors of \(n\), and let \(\Omega(n)\) count prime factors with multiplicity. Define
\[
F(n)=n+\tau(n).
\]
For integers \(2\le m<n\) with \(\Omega(m)\le2\) and \(\Omega(n)\le2\),
\[
F(m)=F(n)
\]
holds if and only if exactly one of the following occurs:

1. \((m,n)=(4,5)\);
2. \(m=qr\) and \(n=qr+2\), where \(q<r\) are distinct odd primes and \(qr+2\) is prime.

Therefore every fiber of \(F\) on the \(2\)-almost-prime layer has cardinality at most two. Its non-singleton fibers are exactly
\[
F(4)=F(5)=7
\]
and
\[
F(qr)=F(qr+2)=qr+4
\]
for the prime pairs in item 2. For example, \(F(15)=F(17)=19\) and \(F(21)=F(23)=25\).

## Assumptions and scope
The domain is the set of integers \(n\ge2\) with \(\Omega(n)\le2\). Thus every input is either a prime \(p\), a prime square \(p^2\), or a product \(pq\) of two distinct primes. The theorem classifies collisions only when both inputs lie in this domain. It makes no claim about fibers containing an input with \(\Omega(n)\ge3\).

## Proof
Assume \(2\le m<n\), \(\Omega(m),\Omega(n)\le2\), and \(F(m)=F(n)\). Then
\[
n-m=\tau(m)-\tau(n)>0,
\]
so \(\tau(m)>\tau(n)\). On the stated domain the only possible divisor counts are
\[
2,\ 3,\ 4,
\]
corresponding respectively to a prime, a prime square, and a product of two distinct primes. Hence only the ordered divisor-count pairs \((3,2)\), \((4,2)\), and \((4,3)\) can occur.

For \((3,2)\), write \(m=p^2\) and let \(n\) be prime. Equality gives
\[
n=p^2+1.
\]
If \(p\) is odd then \(p^2+1\) is an even integer greater than \(2\), so it is not prime. Thus \(p=2\), giving exactly \((m,n)=(4,5)\).

For \((4,2)\), write \(m=qr\) with distinct primes \(q<r\), and let \(n\) be prime. Equality gives
\[
n=qr+2.
\]
Because \(qr+2>2\) is prime, it is odd; hence \(qr\) is odd and both \(q,r\) are odd. Conversely, whenever distinct odd primes \(q<r\) satisfy that \(qr+2\) is prime, \(\tau(qr)=4\) and \(\tau(qr+2)=2\), so
\[
F(qr)=qr+4=F(qr+2).
\]

For \((4,3)\), write \(m=qr\) with distinct primes and \(n=p^2\). Equality gives
\[
qr=p^2-1=(p-1)(p+1).
\]
If \(p=2\), then \(qr=3\), impossible for a product of two distinct primes. If \(p\) is odd, then \(p^2-1\) is divisible by \(8\), whereas the squarefree product \(qr\) has \(2\)-adic valuation at most \(1\). This is impossible.

The three possible divisor-count comparisons are exhausted. The displayed families are therefore necessary and sufficient. Because the product \(qr\) is determined by the larger prime \(qr+2\), two distinct pairs cannot create a third point in the same restricted fiber, so every restricted fiber has size at most two.

## Verification
The bundled `verify.py` independently enumerates every \(n\le10^6\) with \(\Omega(n)\le2\), computes \(F(n)=n+\tau(n)\), and checks every non-singleton fiber against the theorem. It also verifies the converse condition for every squarefree semiprime in the range. The recorded run returned:

`VERIFY_OK limit=1000000 low_omega_inputs=288533 nontrivial_fibers=21909 exceptional_4_5=True theorem_mismatches=0 max_fiber=2`

This finite enumeration is a regression check only. Exhaustiveness for all integers follows from the three symbolic divisor-count cases in the proof.

## Relationship to prior work
Pollack and Troupe explicitly treat the shifted divisor function \(n+\tau(n)\) in Section 4.2 of arXiv:2106.10756v1. Their result is an Erdős--Kac law for the number of prime factors of its values; it does not classify equal-value fibers. Gabdullin, Iudelevich, and Luca later study the image and additive energy of exactly the map \(k\mapsto k+\tau(k)\) in arXiv:2306.16035v1. Their Theorem 1.2 proves positive-density image bounds, and Section 3.1 estimates collisions on a dense family of odd squarefree integers, rather than determining the complete \(\Omega\le2\) fiber structure. OEIS A062249 tabulates \(n+\tau(n)\) and displays the first repeated values but does not state the classification above.

## Limitations
The theorem is deliberately restricted to inputs with at most two prime factors counted with multiplicity. It does not determine whether the prime condition \(qr+2\) holds for infinitely many distinct odd-prime products \(qr\), and it does not classify collisions once an input with \(\Omega\ge3\) is allowed. The computation through \(10^6\) is not used to support any infinite inference.

## References
1. P. Pollack and L. Troupe, “Sums of proper divisors follow the Erdős--Kac law,” arXiv:2106.10756v1, first submitted June 20, 2021; Section 4.2 treats \(n+\tau(n)\). Primary MSC 11N37.
2. M. R. Gabdullin, V. V. Iudelevich, and F. Luca, “Numbers of the form \(k+f(k)\),” arXiv:2306.16035v1, first submitted June 28, 2023; Theorem 1.2 and Section 3 treat \(k+\tau(k)\).
3. OEIS A062249, \(a(n)=n+\tau(n)\).
