# Review

## Correctness
PASS. For \(2\le q<p\), the base-\(p\) expansions
\[
(p+1)q=qp+q,\qquad (p+1)d=dp+d
\]
show that every selected split has no carry, so every selected binomial coefficient has \(p\)-adic valuation \(0\). At \(q=p\), every selected split has exactly two carries: one from the units column and one from the \(p\)-column. Kummer's theorem therefore gives valuation exactly \(2\) for every selected coefficient. Since \(p<p+1<p^2\), the extremal target is \(r_p(p+1)=2\), and minimality follows because every smaller admissible multiplier has already been excluded.

## Originality
PASS. The motivating source arXiv:2610.01328v1 proves \(T_p(p^a+1)=p^{3a}+1\) only for \(a\ge2\), explicitly says the \(a=1\) regime is not included, and identifies only the known \(p=2\) instance \(T_2(3)=6\). McTague's full theorem applies to valuation primes congruent to \(1\) modulo the restriction parameter and therefore does not cover the present \(p<p+1\) family; it likewise records only the \(p=2\) valuation-two example. Semantic searches over published findings, exact web searches, and OEIS searches found no statement implying the uniform formula \(T_p(p+1)=p(p+1)\).

## Value
PASS. This is the natural missing boundary of the paper's exact least-row classification for \(m=p^a+1\). It completes that family by showing that \(a=1\) behaves qualitatively differently from \(a\ge2\): the least extremal row is \(p(p+1)\), not the extrapolated cubic-scale row. The result also gives the exact valuation profile for every admissible multiplier through the first extremal row.

The main limitation is scope: no assertion is made for general restriction parameters outside \(m=p+1\).

Self-review: passed. Independent audit: not yet performed.
