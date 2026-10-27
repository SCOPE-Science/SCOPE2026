# Scientific review: prefix-free divisor codebooks

## Correctness — PASS
For every fixed integer base \(b\ge2\) and prime-support size \(r\ge1\), choose an odd prime \(\ell\) not dividing the gcd of the exponents in the prime decomposition of \(b\). Every nonempty subset sum of \(\ell^{-1},\ldots,\ell^{-r}\) is distinct and lies strictly between zero and one. Its associated mantissa \(b^{t_S}\) is irrational, because a prime exponent of \(b\) not divisible by \(\ell\) would otherwise give a nonintegral rational valuation. Thus the finite set of subset products belongs to separate interior digit cylinders of some common depth. A fixed neighborhood of the individual mantissas preserves that separation. Primes in scaled copies of those neighborhoods then give squarefree integers for which no two nonunit-divisor words share the same leading digit block. The prime number theorem supplies \(\gg_{b,r} (b^L/L)^r\) such integers per scale, and choosing \(L\) from \(X\) proves the asserted counting bound. Boundaries \(r=1\), perfect-power bases, and arbitrary large real \(X\) are accounted for. The included executable checks explicit families, not the general theorem.

## Originality — PASS under the inspected evidence
OEIS A090335 and A088862 explicitly ask for existence for each prime-factor count; A090332 defines the underlying property. Their inspected records do not state a general existence proof or the quantitative all-base result. Ahlswede, Khachatrian and Sárközy (2000) consider a mathematically different notion of an integer prefix involving lists of prime factors rather than leading base-\(b\) digits of divisors. Generic existence of prefix codes with selected word lengths is not sufficient to force the actual divisor strings to be prefix-free. Targeted searches for the two sequence IDs, their aliases, strong quantitative all-base equivalents, and relevant research records found no statement implying the present theorem. Priority remains provisional because unindexed or inaccessible stronger results could exist.

## Value — PASS
The two 2003 conjectures ask whether the admissible sets are nonempty at each prescribed prime-factor count. The result supplies infinitely many squarefree examples in each layer, a nontrivial quantitative lower bound of \(X/(\log X)^r\), and the additional entire family of integer bases. The proof identifies a structural explanation—separation of finitely many subset-product mantissas into disjoint digit cylinders—that applies uniformly to arbitrary fixed support size. This is a natural resolution of explicitly posed arithmetic questions, not an isolated numerical witness or routine code-word renaming.

## Closest literature and remaining limitations
- OEIS A090335 and A088862 (November 26, 2003): finite-value tables and the unresolved existence questions. https://oeis.org/A090335 and https://oeis.org/A088862.
- OEIS A090332 (November 26, 2003): ambient binary-divisor prefix condition. https://oeis.org/A090332.
- Ahlswede, Khachatrian and Sárközy (2000), *On prefix-free and suffix-free sequences of integers*: a different, ordered prime-list notion of prefix, not the present digit-string relation. https://www.math.uni-bielefeld.de/ahlswede/homepage/public/151.pdf.
- The constants are not optimized. The least admissible integer and a full asymptotic for all qualifying integers are open in this argument. The proof uses the standard prime number theorem. Unseen stronger priority coverage cannot be excluded. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
