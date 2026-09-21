# Same-model review

## Verdict

**PASS.** The result gives an exact fixed-prime-support classification for primitive Pythagorean triangles with square perimeter and an explicit asymptotic count for every prescribed finite odd-prime support.

## Correctness

The proof was checked from the Euclidean parametrization rather than relying on the literature normal form as a black box.

- For a primitive Euclidean pair \((m,n)\), the perimeter is \(2m(m+n)\) with \((m,m+n)=1\). Squarehood forces \(m\) even, then uniquely \(m=2U^2\) and \(m+n=V^2\), with \(V\) odd and \((U,V)=1\).
- The positivity and ordering conditions are exactly \(\sqrt2 U<V<2U\), and the perimeter becomes \((2UV)^2\).
- Exact prime support \(\{2\}\cup S\) therefore partitions every odd prime-power block between the coprime integers \(U\) and \(V\), while the entire 2-power lies in \(U\). Taking logarithms converts the interval \(\sqrt2 U<V<2U\) into the stated fractional-part criterion. The boundary cannot occur by unique factorization.
- For counting, the exact identity \(P=2^{2(1-f)}V^4\), where \(f\in(1/2,1)\), shows that the height cutoff differs from \(V^4\le X\) only by a bounded logarithmic boundary strip.
- Multidimensional Weyl equidistribution applies to the signed logarithmic phase on lattice points in each expanding polytope. The relevant polytope volume is \(1/[r(k-1)!(r-k)!]\) for a subset of size \(k\), and summation over subsets gives \(\binom{2r-1}{r}/r!\) by Vandermonde's identity.
- The \(r=1\) specialization recovers the constant \(1/(8\log\ell)\), providing a direct check on the general coefficient.

Exact bounded verification checked 1,266,847 primitive Euclidean pairs with \(m\le2500\), including 150 square-perimeter cases, and found zero normal-form/support mismatches. A second construction check tested 140 bounded fixed-support instances for \(S=\{3\},\{3,5\},\{3,5,7\}\) with zero failures. Numerical counts for these supports trend toward the stated asymptotic constants. The computations are supporting evidence only; the theorem is proved independently.

## Originality

The closest located source is P. Yiu's *Recreational Mathematics*, §6.2. Its full relevant section was inspected. It derives the same square-perimeter normal form and lists examples, but does not state a classification by exact prime support or an asymptotic fixed-support counting theorem.

OEIS A120089 and A120090 were inspected in their current forms. They record square perimeters and square roots, cite Yiu, and give equivalent generation formulas, but do not state the fixed-support fractional-part criterion, infinitude for every finite prescribed odd-prime support, or the asymptotic constant in the result.

Searches covered the exact square-perimeter terminology together with `prime support`, `two prime factors`, `exactly two distinct prime factors`, `smooth`, `S-smooth`, `S-unit`, and asymptotic/counting formulations, as well as the current SCOPE archive. No exact or stronger coverage was located. No specific inaccessible paper emerged as a concrete likely source of the theorem. The principal residual risk is older recreational or problem literature using a different vocabulary, because the underlying square-perimeter parametrization is elementary and longstanding. Originality is therefore only to the best of our knowledge.

## Value

The result changes an unstructured list of square perimeters into a complete arithmetic description at every fixed prime support. It proves, in particular, that every finite set of odd primes occurs infinitely often as the odd part of the prime support of a square perimeter of a primitive Pythagorean triangle. The explicit leading constant depends on the chosen primes only through \(\prod\log p\), while the combinatorial factor depends only on the support size. The one-prime case becomes an irrational-rotation/Sturmian-type criterion with exponent density \(1/2\).

The method also isolates a reusable mechanism: coprime factor allocation turns support restrictions into a signed logarithmic lattice, and a narrow multiplicative window becomes a fractional-part condition whose density is controlled by Weyl equidistribution.

## Status

Same-model review: passed. Independent audit: not yet performed.
