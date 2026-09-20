# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked against the full statement of the synchronized-code reduction in Baláž--Popa, arXiv:2609.17353v1, Section 3.2. The proposed binary code has four properties needed by that reduction: fixed length and injectivity; synchronized occurrence of codewords; exclusion of codewords from every penalty word `g t g`; and exclusion of the guard from encoded source strings.

The synchronization argument is local and exhaustive in form: `001` can occur only at aligned starts because the post-marker encoding has no `00`, and the only boundary triples before the aligned marker are `100` and `000`. The guard argument uses the first and last codeword bits: a candidate starting in `1^k` cannot begin with the required zero, while a candidate starting strictly inside the middle non-codeword block must end in the trailing guard and therefore ends in one rather than zero. The longest run of ones in one codeword is `2 beta + 2`, strictly less than `k=2 beta+5`, and zeroes at boundaries prevent longer runs.

The finite verifier independently enumerates all relevant windows for beta through 6 and agrees with each structural claim. It is supporting evidence, not a substitute for the general proof.

The NP-membership argument is standard: a selected trigger set has polynomial representation using only occurring k-mers, and the induced partition, dictionary, and path contributions can be computed in polynomial time.

## Originality

PASS, qualified to the best of our knowledge.

The motivating paper is a very recent first complexity study of MPFG. Its full text was inspected at the relevant theorem statements. It proves NP-hardness over an alphabet of size three via the code `2 e(a) 2`; it does not state a binary-alphabet hardness theorem. Its fixed-k hardness construction instead introduces fresh source-dependent symbols. Searches using “prefix-free graph”, “minimum prefix-free graph”, “MPFG”, “binary alphabet”, “alphabet size two”, “synchronized code”, and trigger-selection variants found no prior binary MPFG hardness result. The current SCOPE archive was also searched by the object name and acronym, with no overlapping record found before publication.

The binary code is elementary and may be recognizable as a self-synchronizing coding device; no claim of novelty is made for self-synchronizing codes themselves. The originality claim is restricted to the binary instantiation of the MPFG reduction and its complexity consequence.

The principal residual risk is recency: arXiv:2609.17353v1 was submitted on 15 September 2026, so a near-simultaneous note, an author revision, or an as-yet unindexed observation could contain the same tightening. No specifically identified inaccessible paper was found that is especially likely to contain this exact MPFG result.

## Value

PASS.

Alphabet size two is the minimum nontrivial alphabet, so reducing the published hardness from three symbols to two closes the alphabet-size question for unrestricted MPFG. The consequence is structurally informative rather than merely cosmetic: on a fixed binary alphabet, every constant trigger length has only finitely many possible triggers and is polynomial by the existing `O(2^q N)` exact algorithm, yet the problem is already NP-complete when the trigger length is only logarithmic in the input length. This isolates growing trigger length, rather than alphabet growth, as sufficient for intractability.

## Limitations

The result does not establish a sharp threshold in the growth of `k`, does not address approximation hardness, and does not strengthen the fixed-k binary case, which is polynomial by finite candidate enumeration. independent audit has not been performed.
