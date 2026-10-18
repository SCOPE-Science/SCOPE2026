# Independent mathematical audit

## correctness

PASS

The pseudoperiod equation is checked only for i<n−12, and the forbidden exponent threshold includes equality. Every newly created forbidden factor must be a suffix; it has some period p and at least L_p=ceil(55p/21) letters, so checking the last L_p letters for period p is equivalent to the full new-factor condition. Both constraints are prefix-closed, hence binary extension from the empty word without pruning any valid prefix is exhaustive. A separately implemented C++ depth-first enumerator visited exactly 202253 valid prefixes through length 201, with exactly 2 at length 200 and 0 at length 201, and reproduced the source certificate count tail. The two 200-bit words are complements and individually palindromes; there cannot be a longer valid word because every 202-bit word would have a 201-bit valid prefix, which does not exist.

## originality

PASS

Meleshko–Ochem–Shallit–Shan Table 1 already establishes the optimal critical exponent 55/21 and maximum length 200, and their public data provides one 200-bit witness. Complementation of that witness yields at least two; neither the inspected primary article nor the companion table states exactly two and both palindromic. The new finding is exhaustive classification of equality cases, not the length-200 cutoff or exponent. Searches for equivalent extremizer counts did not identify coverage; source-author unpublished search records remain a real priority risk.

## value

PASS

The (9,12) instance is the longest finite cutoff in the published pseudoperiod table, making classification of the extreme boundary a natural finite combinatorics-on-words problem. Exactly two complementary palindromes is a complete and surprisingly rigid equality classification; it is not an arbitrary slice or reproduction of the already-known scalar bound. A correct exhaustively certified finite fact can be mathematically useful without a general theorem for other pseudoperiods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
