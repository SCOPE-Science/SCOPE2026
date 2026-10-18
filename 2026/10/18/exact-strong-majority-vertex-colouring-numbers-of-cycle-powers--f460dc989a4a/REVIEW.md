# Scientific review of cycle-power strong-majority colourings

## Correctness

**PASS.** Two colours are equivalent to open-neighbourhood sign balance because every degree is \(2k\). The factored cyclic-shift adjacency operator, \(BD\), proves the two-adic obstruction for odd powers; explicit alternating and block-alternating sign words prove the converse. The three-colour construction is checked using exact per-arc bounds, with all exceptional five-letter windows at \(\(k=2\)\) listed in the proof. When \(\gcd(n,k)=1\), injectivity of \(B\) and the permutation cycles of the shift by \(k+1\) give the exact count. Small-case exhaustive checks and thousands of constructive checks support, but are not substituted for, the proof.

## Originality

**PASS with bibliographic limitations.** Strong-majority colouring was introduced in the 2026 motivating paper, which proves the ordinary-cycle case but not arbitrary noncomplete powers. The mathematically equivalent two-colour notion, neighbourhood-balanced colouring, predates it: Freyberg--Marr (2024) covers the entire quartic circulant case, hence the two-colour criterion for the second power of a cycle. That known special case is expressly excluded from the novelty claim. The sharp higher odd-power divisibility theorem, uniform three-colour construction, and coprime enumerator are not covered by the inspected texts or the retrieved mathematical-record matches. Perfect-colouring and circulant-kernel terminology pose residual unindexed-priority risks. The close comparisons are mathematical implications rather than title differences.

## Value

**PASS.** This is a complete exact evaluation of a new colouring invariant on an infinite natural graph family of unbounded degree, with a sharp arithmetic distinction between even and odd powers. The constructive upper bound is uniform and optimal, and the coprime fibre count supplies information beyond the extremal number. The result resolves every permissible order and exponent in the noncomplete range rather than an arbitrary isolated small parameter.

## Verification and limits

The stand-alone verifier enumerates every candidate two-colouring for tested orders, checks local junction patterns, and confirms the constructive formula on thousands of cycle powers. It does not independently prove statements for unbounded order, and an external independent audit remains outstanding. Previously known base cases are credited, and equivalent unindexed literature cannot be excluded absolutely.

Self-review: passed. Independent audit: not yet performed.
