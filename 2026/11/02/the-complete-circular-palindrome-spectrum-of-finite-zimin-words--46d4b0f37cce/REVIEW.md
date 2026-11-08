# Independent mathematical audit

## correctness

PASS

PASS: For Z_n=Z_(n−1)a_nZ_(n−1), length N=2^n−1, one-based position j has letter a_(1+ν2(j)). An odd center of rank r supports exactly radii t<2^(r−1); at the next step, adjacent multiples of 2^r or the wrap seam cause mismatched ranks. Internal adjacent symbols never coincide, whereas the unique cyclic seam abuts two a1 symbols, so each permitted even length has exactly one seam-centered palindrome. Thus the odd 2t+1 length count is n−ceil(log2(t+1)); total odd N and even (N−1)/2 gives (3N−1)/2. Independently enumerated literal circular factors for every length, all n=1..8, matching counts 1,4,10,22,46,94,190,382. This finite corroboration does not replace the ruler identity and center bounds.

## originality

PASS

PASS (qualified): Głowinski–Rytter analyze Zimin compressed pattern matching and ruler structure; Glen–Justin–Widmer–Zamboni study richness of palindromes; Simpson proves general circular-word upper bounds. These are genuine antecedents, but no inspected accessible statement implies the explicit all-rank Zimin circular spectrum. Simpson full text unavailable (OA access failure and protected retrieval vpn_disconnected), so potential hidden special-case discussion is retained as a priority risk.

## value

PASS

PASS: Zimin words are canonical self-similar unavoidable-pattern witnesses. A letter-by-letter and lengthwise circular-palindrome language, distinguishing seam-created even palindromes from all nonwrapping odd palindromes, is a complete natural word-complexity invariant; not merely a new general upper bound or integer sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
