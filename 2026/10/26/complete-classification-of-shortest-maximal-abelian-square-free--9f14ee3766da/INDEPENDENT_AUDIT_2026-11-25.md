# Independent mathematical audit

## correctness

PASS

A missing alphabet symbol extends the word without a square because it has odd multiplicity in any new factor. All new forbidden factors touch the extended end, and first-occurrence normalization is unique; these facts justify the source recursion and tests. I independently enumerated all continuations after the fixed first two letters 01, without normalizing any continuation before the terminal test. A square-free word of length ≥2 starts with different letters, and a labeled word can be normalized to this first pair with exactly three remaining freely permutable letters. For packed prefix Parikh vectors P[k], right-blocking letters of a length-n word are exactly the one-letter vectors among 2P[n+1−h]−P[n+1−2h]−P[n], and left-blocking letters among P[2h−1]−2P[h−1], for 1≤h≤floor((n+1)/2). Base 32 is exact: after subtracting a letter unit, each coefficient has absolute value smaller than 32; successive reduction modulo 32 therefore makes scalar equality equivalent to vector equality. Values fit the signed integer type. Branching on all other right extensions enumerates every square-free word starting 01 through depth 16. There are no hits below 16 (lengths 0 and 1 lack full support); at 16 there are 24 with first pair 01, six in each of the listed four canonical classes. There are 20 first ordered distinct pairs, thus 480 labeled words. Reversing and renormalizing gives the two pairs (1,3) and (2,4) in the frozen order. All 40 explicit CSV boundary witnesses also pass sorted-block comparisons.

## originality

PASS

The closest checked exact maximal-word table is on four symbols. On five symbols the inspected two-sided bound supplies an example of length 19, while the known shorter one-sided minimum is for an inequivalent extension condition. Neither yields the five-letter lower cutoff or census. This is a scoped pass, not a priority proof.

## value

PASS

Five letters is the next alphabet after the published four-letter exact census. The result closes the gap between the known one-sided lower bound and two-sided construction, and classifies all shortest obstructions under the natural alphabet and reversal symmetries. Those small exact classes and the proven cutoff are usable for testing constructions and comparing small alphabets; the cutoff is not an arbitrary computation limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
