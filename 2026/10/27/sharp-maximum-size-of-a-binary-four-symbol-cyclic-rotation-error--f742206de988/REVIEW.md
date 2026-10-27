# Scientific review

## Correctness (C): PASS
The exact claim specifies the binary alphabet, nonwrapping length-four cyclic rotations, at most one error, and every integer length at least four. The proof assigns every nonidentity output to its earliest generating window, shows that windows separated by at least three positions cannot produce the same changed word, and derives a 32-state max-plus recurrence. The componentwise identity between lengths six and eleven, checked by two finite enumeration methods, induces an exact all-length five-step recursion. The periodic word supplies matching witnesses. The included standalone source returned `VERIFY_OK`.

## Originality (O): PASS, with residual literature risk
Chen–Milenkovic (2026), Definition 3, has the same exact-window cyclic channel. Their Theorems 2–3 address asymptotic bounds for window length at least nine, Theorem 4 estimates ball sizes for variable window length, and their Example 1 evaluates a particular length-five input at window length four. None of those statements implies the exact maximization formula for all binary lengths. Searches for four-symbol cyclic burst ball volumes, periodic witnesses, aliases, and broader code-ball identities did not identify an equivalent formula. The nearest indexed findings concern different burst/deletion channels. The possibility of an unindexed independent exact calculation remains.

## Value (V): PASS
Four-symbol windows are singled out in the source's nanopore readout motivation, while source bounds for cyclic burst code redundancy are general/asymptotic. The exact coefficient \(11/5\), nontrivial period-five extremizer and short finite-state proof replace a window-counting upper bound of asymptotic coefficient three in this natural, practically motivated error-ball invariant. The statement applies at every blocklength, and can be used to sharpen finite neighborhood-counting and greedy bounds for this precisely specified channel. No code-optimum claim is made.

## Limitations
The proof does not classify all maximizing words. It concerns only exactly-four-position rotations, not arbitrary permutations or a mix of window lengths. No external audit was undertaken.

Self-review: passed. Independent audit: not yet performed.
