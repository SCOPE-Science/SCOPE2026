# Review: Exact ternary length-three strongly two-separable code size

## Correctness
PASS. The direct definition reduces any failure to at most five words. Complete enumeration shows the minimal obstructions are exactly \(891\) four-word sets; a ten-word witness avoids them. Symmetry normalization followed by exhaustive branch-and-bound rules out eleven words. The packaged verifier recomputes these facts from scratch.

## Originality
PASS. The primary same-object source constructs nine ternary words but does not determine the optimum. Searches under SSC, strongly separable, descendant, exact parameter and neighboring fingerprinting-code formulations found no implication-equivalent exact value. The closest later strongly separable paper treats the \(\overline{3}\) condition rather than this \(\overline{2}\) instance. Residual risk remains for unindexed finite computations.

## Value
PASS. This settles the natural smallest nonbinary length-three instance left sharper than the foundational construction, improving its ternary lower bound from nine to the exact value ten.

## Closest literature and limitations
Jiang–Cheng–Miao, arXiv:1412.6128, is the closest source. The result is finite and parameter-specific; it does not classify all optimal codes or extend the exact formula to larger alphabets.

Same-model review: passed. Independent audit: not yet performed.
