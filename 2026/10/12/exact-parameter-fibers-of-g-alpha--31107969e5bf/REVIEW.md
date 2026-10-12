# Review: Exact parameter fibers of \(g_\alpha\)

## Correctness
**PASS.** The proof reduces equality of \(g_\alpha(n)\) and \(g_\beta(n)\) to equality of lcm exponents and then works prime by prime. The minimum exponent valuation \(v_\ell(h)\) is exactly the threshold below which the parameter valuation is invisible; above it, a coordinate attaining the minimum recovers the parameter valuation. This proves both directions of the normalized-parameter criterion. The exact fiber formula is then a direct solution of the resulting valuation constraints. The embedded verifier is regression evidence only and agrees with the theorem on the stated finite ranges.

## Originality
**PASS.** The closest primary result is Mittou's 2023 Theorem 2.2, which identifies only the fiber of the original value \(n\): \(g_\alpha(n)=n\) exactly when \(\alpha\mid h\). The inspected 2025 follow-up treats compositions and an equivalence relation between different base integers. Neither source states or implies the complete fixed-base parameter equivalence \(g_\alpha(n)=g_\beta(n)\) iff the normalized parameters agree, nor the explicit fiber cardinalities. Targeted scholarly and semantic searches did not locate a stronger statement. The previously checked gcd-exponent companion theorem has a different invariant and finite periodic image, so it does not imply this result.

## Value
**PASS.** The source itself motivates the parameter equation by proving finiteness of one distinguished fiber. Determining all fibers, their exact sizes, and the injectivity boundary is a natural completion of that structural question. The result is narrow but exact and reusable for any fixed factorization pattern; it is not a routine increment of a cutoff or a recomputation of a table.

## Closest literature and limitations
The strongest checked overlap is the \(s=1\) special case in the 2023 paper. The 2025 paper is broader in other directions but asks a differently quantified equivalence problem. The remaining originality risk is notation mismatch in uninspected literature. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
