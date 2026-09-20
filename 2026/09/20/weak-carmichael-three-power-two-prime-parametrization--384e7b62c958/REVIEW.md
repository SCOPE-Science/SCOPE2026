# Review: finite parametrization of weak Carmichael numbers \(3^a p q\)

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof starts from the established weak-Carmichael criterion \(r-1\mid n-1\) for each prime divisor \(r\). For \(n=3^apq\), the factor \(3\) contributes only the automatic parity condition, and the remaining two constraints reduce exactly to
\[
p-1\mid 3^a q-1,\qquad q-1\mid 3^a p-1.
\]
Introducing \(d=p-1\) and \(k=(3^ap-1)/(q-1)\) gives \(1\le k<3^a\). The identity
\[
k(3^a q-1)=3^{2a}d+(3^a-1)(3^a+k)
\]
is exact. Divisibility by \(d\) is therefore equivalent to the two stated divisor conditions after using integrality of \(q\). Both directions of the parametrization were checked explicitly.

The bounds follow directly from
\[
d\mid(3^a-1)(3^a+k),\qquad 1\le k\le3^a-1.
\]
No heuristic estimate is used. The \(a=2\) classification reduces to twelve displayed integer candidates, only two of which yield prime pairs, so the global \(9pq\) conclusion is independently human-checkable.

A standalone exact-integer verification implements both the divisor parametrization and a direct enumeration from the defining divisibilities. The methods agree for \(1\le a\le5\); the parametrization was also evaluated at \(a=6\). These computations are supporting checks rather than a substitute for the algebraic proof.

The exponent-period corollary follows from two multiplicative-order congruences once one solution exists. A solution forces \(p,q\equiv2\pmod3\), ensuring that \(3\) is invertible in both moduli; the required invertibility of \(p\) modulo \(q-1\) follows from the second defining congruence.

## Originality

**PASS, to the best of our knowledge.** The following coverage was checked:

- Borwein–Wong's Giuga-congruence work for the underlying divisibility characterization.
- Meštrović, arXiv:1305.1867 (2013), including the full statement of the weak Carmichael criterion and Remark 2.77 on the \(3^2p_2\cdots p_s\) family.
- Meštrović's 2026 *Weak Carmichael Numbers* manuscript, including its tables and its treatment of two-distinct-prime exponent families.
- OEIS A225498 and A087442.
- Searches using the terms "weak Carmichael", "pseudo-Carmichael", and "generalized Carmichael", together with the forms \(3^apq\), \(9pq\), and the known values 13833 and 321201.
- The current SCOPE archive by mathematical object, terminology, and the two numerical examples.

The 2013 Remark 2.77 is especially relevant: it explicitly lists 13833 and 321201 as members of the \(3^2p_2\cdots p_s\) family, then in the same remark displays an empty-intersection computation for \(9pq\) with \(q<10^5\). The present result does not merely point out that inconsistency; it proves globally that the two listed \(9pq\) examples are the only ones.

No prior exact finite parametrization for all \(3^apq\), no cutoff-free \(9pq\) classification, and no matching fixed-pair exponent-period statement were located.

The main residual originality risk is older terminology. E. Wong's 1997 M.Sc. thesis *Computations on Normal Families of Primes* calls these objects pseudo-Carmichael numbers and contains general normal-family constructions and a converse. An indexed excerpt was inspected and showed that general material, but the full thesis could not be directly inspected from the checked source. An equivalent specialized \(3^apq\) result hidden there or in closely related older literature cannot be completely excluded.

## Value

**PASS.** The result turns an infinite two-prime search for every fixed \(a\) into a finite divisor problem with explicit bounds. The \(a=2\) specialization gives a complete global answer to a family that older literature explicitly discussed computationally and for which the 2013 source contains a contradictory statement. The periodicity corollary also converts each admissible prime pair into a precisely described arithmetic progression of exponents.

The contribution is elementary rather than technically deep, but it supplies a clean structural theorem, a cutoff-free correction/classification, and reusable finite-search machinery for a named family in the literature.

## Scientific limitations

The odd part is required to be squarefree with exactly two primes. The result does not address \(3^ap^bq^c\) with larger \(p\)- or \(q\)-exponents, nor support containing additional distinct primes. The finite verification only checks small exponents; completeness for arbitrary \(a\) rests on the proof, not on those calculations. Originality remains subject to the older pseudo-Carmichael literature noted above.
