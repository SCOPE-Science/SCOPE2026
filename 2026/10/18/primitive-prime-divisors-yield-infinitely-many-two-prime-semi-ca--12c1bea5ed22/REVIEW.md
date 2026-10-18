# Scientific review: primitive-divisor construction for semi-Carmichael semiprimes

## Correctness — PASS

For each prime \(p\ge5\), the exponent \(h=p-1\ge4\) avoids both exceptions in the classical Bang–Zsigmondy theorem for \(p^h-1\). A primitive prime factor \(q\) has \(\operatorname{ord}_q(p)=p-1\); this order divides \(q-1\). Because \(q\ne p\) and \(q\equiv1\pmod{p-1}\), it satisfies \(q>p\). The two exact congruences defining a semi-Carmichael semiprime reduce to \(p^{p-1}\equiv1\pmod q\) and \(q^{q-1}\equiv1\pmod p\). The first follows by construction, the second from Fermat's theorem. A distinct smaller prime factor supplies injectivity. Moreover \(pq<p^p\), and the prime number theorem implies the stated explicit liminf at least one. No finite experiment is used as an infinite proof. The attached finite certificate checks seven example pairs and independently compares original and reduced tests for all 23,313 distinct-prime semiprimes not exceeding 100,000.

## Originality — PASS, with residual risk

The full relevant Section 5 of López, *Idempotence in Carmichael and Giuga numbers and its application to the Agoh–Giuga conjecture* (arXiv:2610.09129v1, 2026-10-06), defines semi-Carmichael integers and supplies properties and examples, but does not establish semiprime infinitude, universal smaller-prime support, or the quantitative lower bound. OEIS A294169 (2018) explicitly asks whether infinitely many of precisely the equivalent semiprimes exist; it already records the congruence criterion and first terms, so those are expressly not claimed as new. The classical Zsigmondy theorem furnishes a primitive divisor but does not itself state the semi-Carmichael connection. Published mathematical-result index searches for the combined property, equivalents, prime-order construction, and OEIS identifier returned no result with the theorem; closest hits concern different classes (weak Carmichael, Novák, Duffinian). This is not an assertion that index coverage is exhaustive, and there remains the possibility of a previously unindexed or implicitly equivalent construction. An independent originality assessment has not been performed.

## Mathematical value — PASS

The construction resolves the explicit natural infinitude question in OEIS A294169, strengthening mere existence to every prime \(p\ge5\) as the least factor and a rigorous counting lower bound \(S_2(X)\gg\log X/(\log\log X)^2\). The object is an arithmetic family defined in primary number-theoretic literature, not an arbitrary computational slice. The proof connects a classical primitive-divisor theorem to simultaneous modular restrictions in an unexpected but precise manner.

## Closest literature and limitations

López (2026), Definition 5.8 and Proposition 5.9, introduces the semi-Carmichael name and necessary properties; OEIS A294169 presents the older, equivalent two-prime problem and its open infinitude question. Bang–Zsigmondy supplies existence of primitive prime factors, and the prime number theorem supplies only the weak quantitative bound. The current evidence supports novelty to the extent searchable; old but not indexed results may exist. No claim is made about asymptotic density or an algorithm with guaranteed polynomial runtime.

Self-review: passed. Independent audit: not yet performed.
