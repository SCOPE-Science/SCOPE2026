# Scientific review — cyclic inverse monoid rank–nilpotency spectra

## Correctness — PASS

The enumerated objects are unambiguous: the zero partial map is counted once, and every nonempty restriction has a unique rotation extension. For a rotation of order \(d\), the domain decomposes into \(n/d\) independently selected cyclic binary words of length \(d\). A restriction's \(t\)-th power is zero exactly when none of these words has \(t\) consecutive ones in its periodic extension. The stated weighted transition matrix counts these words by a trace, including the \(t>d\) boundary, and summation over rotation orders gives the bivariate polynomial. The exact upper tail follows because \(t>n/2\) forces a primitive rotation and a unique maximal run. The logarithmic limit is proved with disjoint-block lower-tail and union-bound upper-tail estimates, including the small-order rotations. An independent implementation of finite partial maps and polynomial matrix traces agrees coefficientwise in all exhaustively checked cases \(2\le n\le10\); the general proof, not these tests, certifies the theorem's mathematical scope.

## Originality — PASS against inspected sources

Fernandes (arXiv:2211.02155, 2022-11-03) defines and presents the same cyclic inverse monoid, proves its size and rank, but does not state the joint rank–nilpotency-index census or the totient-controlled high-index law in the inspected full text. Elliott–Levine–Mitchell (arXiv:2303.12387, 2023-03-22) enumerate isomorphism types of monogenic (inverse) submonoids, not numbers of restricted cyclic partial permutations at a given rank and least zero power. OEIS A261764 tabulates analogous index counts for all nilpotent partial permutations, without the cyclic restriction; its size-four count \(73\) differs from \(37\) here. Analogous chain-based restricted-partial-isometry enumerations are not implications for modulo-\(n\) cyclic rotations, whose orbit lengths vary arithmetically. The novelty claim is the assembled bivariate enumerator and exact Euler-totient upper tail, not the general facts that partial injections decompose into paths and cycles or that cyclic binary words admit transfer matrices.

A residual priority risk remains: a specialized treatment under cyclic restriction, orbitwise run avoidance, or monogenic inverse-semigroup terminology could contain an equivalent formula outside the inspected sources. Bibliographic search does not establish exhaustive uniqueness.

## Value — PASS

Least zero power and rank are intrinsic finite-semigroup invariants. Fernandes's cyclic inverse monoids form a natural rank-two-generated family distinct from unrestricted partial permutations and line-isometry restrictions. The complete joint spectrum gives all rank/index counts with a finite transfer matrix and divisor sum, separates the asymptotic typical \(\log_2n\) scale from the rare linear-size upper tail, and shows that the exact upper tail exposes Euler's totient \(\varphi(n)\). The binomial rank law is valid uniformly for every composite or prime \(n\), providing a meaningful arithmetic characterization not supplied by the total monoid size or by generic nilpotent-injection counts. The asymptotic is deliberately first order; no centered limit distribution or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
