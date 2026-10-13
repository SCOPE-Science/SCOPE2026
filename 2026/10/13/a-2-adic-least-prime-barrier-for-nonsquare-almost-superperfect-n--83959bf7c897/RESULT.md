# A 2-adic least-prime barrier for nonsquare almost superperfect numbers
## Finding
Let \(n>1\) be an almost superperfect integer, meaning
\[
\sigma(\sigma(n))=2n-1.
\]
Assume that \(n\) is not a perfect square. Put
\[
b=v_2(\sigma(n)),
\]
and let \(P\) be the least prime divisor of \(n\). Then \(b\) is a positive even integer and
\[
\prod_{p\mid n}\left(1+\frac1p\right)
<\frac{2^{b+1}}{2^{b+1}-1}.
\]
Consequently,
\[
P>2^{b+1}-1.
\]
If
\[
n=\prod_p p^{a_p},
\]
then the exponent \(b\) is given explicitly by
\[
b=\sum_{a_p\text{ odd}}
\bigl(v_2(p+1)+v_2(a_p+1)-1\bigr).
\]
In particular \(b\ge2\), so every nonsquare almost superperfect integer has
\[
P\ge11
\]
and hence is coprime to \(210\).

## Assumptions and scope
The function \(\sigma\) is the ordinary sum-of-positive-divisors function, and \(v_2(m)\) is the exponent of \(2\) in \(m\). The theorem concerns only the nonsquare branch of the equation. It uses two established facts from Fang's treatment of almost superperfect numbers: every such number is odd, and \(\sigma(n)\) is a perfect square.

The factorization \(n=\prod_p p^{a_p}\) ranges over the prime divisors of \(n\). No existence of an almost superperfect integer greater than \(1\) is assumed.

## Proof
Fang proved that every almost superperfect integer is odd and that \(\sigma(n)\) is a square. Since \(n\) is odd but not a square, at least one exponent \(a_p\) is odd. For odd \(n\), the standard parity criterion says that \(\sigma(n)\) is odd exactly when \(n\) is a square. Therefore \(\sigma(n)\) is even. Because it is also a square,
\[
b=v_2(\sigma(n))
\]
is a positive even integer, so \(b\ge2\).

Write the abundancy index as
\[
I(m)=\frac{\sigma(m)}m.
\]
The defining equation gives the exact identity
\[
I(n)I(\sigma(n))
=\frac{\sigma(\sigma(n))}{n}
=2-\frac1n<2.
\]
For each prime divisor \(p\) of \(n\),
\[
I(p^{a_p})=1+\frac1p+\cdots+\frac1{p^{a_p}}
\ge1+\frac1p.
\]
Also \(2^b\) is the exact power of \(2\) dividing \(\sigma(n)\), so
\[
I(\sigma(n))\ge I(2^b)
=1+\frac12+\cdots+\frac1{2^b}
=2-2^{-b}.
\]
Combining these lower bounds with the preceding strict inequality yields
\[
\left(\prod_{p\mid n}\left(1+\frac1p\right)\right)
(2-2^{-b})<2,
\]
hence
\[
\prod_{p\mid n}\left(1+\frac1p\right)
<\frac{2}{2-2^{-b}}
=\frac{2^{b+1}}{2^{b+1}-1}.
\]
Since the product on the left is at least \(1+1/P\),
\[
1+\frac1P<1+\frac1{2^{b+1}-1},
\]
which gives
\[
P>2^{b+1}-1.
\]

It remains to compute \(b\) from the factorization of \(n\). If \(a_p\) is even, then \(\sigma(p^{a_p})\) is a sum of an odd number of odd terms, so it is odd. If \(a_p\) is odd, then \(a_p+1\) is even and the standard \(2\)-adic lifting-the-exponent identity gives
\[
\begin{aligned}
v_2(\sigma(p^{a_p}))
&=v_2(p^{a_p+1}-1)-v_2(p-1)\\
&=v_2(p+1)+v_2(a_p+1)-1.
\end{aligned}
\]
Multiplicativity of \(\sigma\) on the coprime prime-power factors of \(n\) therefore gives
\[
b=\sum_{a_p\text{ odd}}
\bigl(v_2(p+1)+v_2(a_p+1)-1\bigr).
\]
Finally \(b\ge2\) implies \(P>7\), and since \(P\) is prime, \(P\ge11\). Thus no prime among \(2,3,5,7\) divides a nonsquare almost superperfect integer.

## Verification
The proof is unrestricted and symbolic. The accompanying checker verifies the stated \(2\)-adic prime-power formula on a broad finite grid of odd primes and exponents, verifies the algebraic threshold calculation for even \(b\), and independently searches the defining equation through \(200000\). The finite search finds no solution greater than \(1\), which is corroborative only and is not used in the proof.

## Relationship to prior work
Guy's problem book records the almost-superperfect equation as an open problem. Fang's full paper is the closest primary source. It proves that \(\sigma(n)\) is a square, that no even almost superperfect integer exists, that a prime-power solution is impossible, and that divisibility by \(3\) forces \(n\) to be a square. Fang also proves the exact abundancy-product lemma
\[
I(n)I(\sigma(n))=2-\frac1n<2.
\]

The present result combines the square conclusion with the full \(2\)-power contribution inside \(I(\sigma(n))\). For a nonsquare solution, the exponent of \(2\) in \(\sigma(n)\) is not merely positive: it is even, so the local factor is at least \(I(2^2)=7/4\). This yields the uniform support inequality and excludes \(5\) and \(7\) as least prime divisors as well as \(3\), while retaining the exact dependence on \(v_2(\sigma(n))\).

Targeted searches for a least-prime bound, a \(v_2(\sigma(n))\) bound, a coprimality-with-\(210\) statement, and equivalent formulations of the almost-superperfect equation did not locate a published statement implying this result. The full four-page Fang paper was inspected; it states only the divisor-\(3\) square criterion at this point.

## Limitations
The theorem does not prove that an almost superperfect integer greater than \(1\) exists or does not exist. It applies only to a hypothetical nonsquare solution; square solutions require different arguments. The least-prime inequality is necessary, not sufficient.

The original problem predates the exact-day bibliographic source used for metadata. Fang reports that it appeared in Guy's first edition in 1981, while the inspected historical editions do not supply an exact public day for that first appearance. The exact metadata date therefore uses the verified publication day of Guy's third edition, \(13\) July \(2004\). A short equivalent observation in older informal literature remains a residual originality risk.

## References
1. Richard K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, published 13 July 2004, ISBN 978-0-387-20860-2.
2. Jin-Hui Fang, "On Almost Superperfect Numbers", *The Fibonacci Quarterly* 46/47 (2008/2009), no. 2, 111--114, DOI 10.1080/00150517.2008.12428167. MSC2000: 11A25, 11A51, 11D41.
