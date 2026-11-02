# Scientific review

## Correctness

**PASS.** The two-block decomposition \(\rho^k(0)=\rho^{k-1}(01)\) gives an exact cover of each admissible full-circle window by one of the two substituted three-block factors `010` and `101`, both present in the fixed point. This establishes factor containment at *all* lengths and ranks. Digrams of the four-letter fixed point form the exact eight-element substitution-closed set; the 8-by-16-by-16 finite supertile calculation is exhaustive at every length at most 16. The absence of length-15 and length-16 palindromes forces the absence of every longer palindrome by a centered-subword argument. Finally, complete finite-rank enumeration establishes the sharp first full language at rank 8, which persists through nested prefixes. The bundled checker independently verifies the finite ingredients and overlapping-`11` encoding. The infinite claim is proved, not inferred from examples.

## Originality

**PASS, with priority qualification.** Baake (arXiv:math-ph/9907011, inspected text) reports which lengths of ordinary Rudin–Shapiro palindromes may occur. Schaeffer–Shallit (arXiv:1508.02074, inspected relevant sections) studies ordinary palindromes and maximal palindromes of automatic sequences. Neither inspected statement asserts full-circle factor containment for complete dyadic Rudin–Shapiro prefixes or gives the exact sharp rank at which their circular palindrome languages become the 36-word infinite language. Checks against available prior mathematical findings found no implication of these results from an earlier record. A primary 1997 Allouche article was identified but was not accessible in full; historical priority cannot be guaranteed by search alone.

## Value

**PASS.** The central all-length cyclic-to-linear factor embedding resolves a nontrivial boundary issue for every complete dyadic Rudin–Shapiro word, with relevance to cyclic pattern matching and factor invariants. The consequent complete circular palindrome language has a sharp stabilization threshold and an explicit 36-string finite classification. It is stronger than a list of allowable infinite-word palindrome lengths and avoids arbitrary parameter slicing.

## Scope, evidence and limits

The checker uses only finite exact enumerations at the eight allowed 16-block digrams and at ranks 0–8. The proof handles the unbounded cases. This does not determine palindrome multiplicities or arbitrary-prefix circular languages. The two cited arXiv sources were examined in their relevant accessible text, and one historically relevant original publication remained inaccessible. Self-review is not external certification.

Self-review: passed. Independent audit: not yet performed.
