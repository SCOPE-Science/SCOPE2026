# Scientific review

## Correctness

**PASS.** A minimal unique cyclic factor cannot be a proper prefix of another, so there is at most one per start. Every nonsingleton minimal unique factor beginning with a given symbol has an alternative occurrence of its proper suffix preceded by a different symbol; these chosen contrasting positions are distinct, because coincident choices would force two minimal unique factors to be prefix-comparable. This is an all-length injection. Unique single-letter factors and absent letters are handled separately. De Bruijn factor multiplicities show equality at each order; the checker enumerates 80,825 small-word instances and ten explicit de Bruijn cycles. The mathematical proof is independent of the finite tests.

## Originality

**PASS under the available evidence, with residual historical-priority uncertainty.** The checked 2013 primary paper develops minimum/shortest unique substring theory for a linear string and its non-nesting structural property, not a cyclic bound dependent on each letter's frequency. The 2011 primary publication's accessible abstract establishes basic definitions and maximal-repeat duality, but its complete text was inaccessible. Comparisons with published summaries of sliding-window minimal unique substring algorithms, circular absent factors, and short-read reconstruction found different observables. Available record searches for circular minimal unique substrings, cyclic frequency bounds, and de Bruijn equality did not identify an implication that covers the per-letter bound. Failure to locate a result cannot establish historical uniqueness.

## Value

**PASS.** The alphabet-composition inequality strengthens the general circumference bound whenever one symbol is rare. For a binary word containing a fixed number of ones, it bounds the total number of minimal unique cyclic signatures independently of arbitrarily many inserted zeros. The proof gives a direct charging mechanism and establishes best-possible constant via an infinite natural equality family rather than an isolated small numerical gain.

## Closest literature and limitations

Ilie–Smyth (2011) and Pei–Wu–Yeh (2013) provide the closest foundational definitions and the non-nesting observation. The full 2013 article was accessible, with sections on minimum unique substrings and uniqueness constraints inspected. The full 2011 article was inaccessible; its publisher abstract and bibliographic information were read. The classical de Bruijn construction demonstrates sharpness but does not imply the per-symbol upper bound. Nothing here classifies all equality cases or certifies priority against all unpublished sources.

Self-review: passed. Independent audit: not yet performed.
