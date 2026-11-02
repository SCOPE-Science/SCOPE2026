# Scientific review: exact radius-four flag-rank sphere

## Correctness

PASS. The all-prime-power proof partitions every weight-four matrix by whether any crossing rank is two, then by largest occupied superdiagonal when all four positive crossing ranks equal one. Rank two forces the consecutive profile \((1,2,1)\) and a two-by-two invertible middle crossing matrix, yielding \(q^2|\operatorname{GL}(2,q)|\) choices per placement. The remaining five matrix patterns have independently derived counts. Eight exhaustive finite-field tests verify both their disjoint partition and six category totals, including the nonprime field \(\mathbb F_4\). The tests are checks, not the basis of the infinite statement.

## Originality

PASS on available evidence, not a guarantee of global priority. The closest primary work [1], inspected in its original accessible full text, computes radius-zero-through-three spheres and general bounds, and its distance-nine discussion does not imply an exact radius-four sphere polynomial. The full-text structural and theorem material of [2] is about maximum-distance codes and does not give the claimed count. Focused queries for flag-rank radius-four spheres, rank distributions and alternative terminology yielded no dominating published result. Residual risk: an implicit formula in older geometric or quiver orbit-counting literature; the absence of a search hit does not prove uniqueness.

## Value

PASS. Radius four is the first flag-rank shell where a crossing submatrix of rank two occurs, so the six-pattern classification captures a structural change absent from the previous three shell formulas. The exact ball volume replaces an asymptotic bound with a finite-field parameter identity directly relevant to sphere-packing and minimum-distance-nine perfect-code obstructions. This is an all-length, all-field counting theorem, not an arbitrary isolated small computation.

## Scope and limitations

The field order is any prime power, the length satisfies \(n\ge3\), and the result is a sphere/ball cardinality statement, not a perfect-code existence theorem. The divisible-binomial condition for distance nine is necessary only. Independent review has not been performed. The principal sources are arXiv:2606.12934, arXiv:2303.16653, and DOI 10.3934/amc.2021027.

Self-review: passed. Independent audit: not yet performed.
