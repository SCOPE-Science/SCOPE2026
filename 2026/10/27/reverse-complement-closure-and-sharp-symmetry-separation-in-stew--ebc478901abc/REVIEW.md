# Scientific review: Stewart-word factor symmetries

## Correctness — PASS
The claim quantifies over arbitrary infinite Stewart directives, including an optional exceptional-hole filling. The proof reconstructs the base-three Toeplitz skeleton, proves the involutive reflection \(i\mapsto2H_r-i\pmod{3^r}\) exchanges every assigned bit, and proves that every finite factor can be relocated to wholly assigned positions. The independent local decomposition at length eight is exhaustive: the only possible hole subsequences have lengths two or three, whose complete languages are proved directly. Those three residue classes yield exactly sixteen factors in either orientation, with no complementary pair, and exact counts at shorter lengths. The finite checker independently passes all listed local/skeleton checks. No infinite result is inferred from enumeration alone.

## Originality — PASS, with identified residual risks
Fici–Shallit, arXiv:2112.12125v1, §§6 and 10, classify ordinary palindromes and complexity but do not state this reversal-versus-complement overlap spectrum or prove language-wide reverse-complement invariance. Currie et al., arXiv:2209.09598, §§2–3, investigate complementary-factor avoidance across binary word classes, without a theorem specializing to every Stewart directive or relating this property to the reverse-complement antimorphism. The closest retrieved public comparison was a different cyclic Sturmian lifting result; none implies the current statement. Search is not a uniqueness certificate. Earlier generalized choral-sequence literature could conceal equivalent observations and remains a residual risk.

## Mathematical value — PASS
This supplies a complete qualitative and quantitative symmetry classification for an uncountable, established Toeplitz family: all lengths admit the *combined* antimorphism, whereas neither constituent involution survives as a co-occurrence beyond the sharp length-seven boundary. The short-factor spectrum gives the exact transition, and the base-three reflection explains it structurally for every directive. This is not a length-specific isolated count or a rephrasing of the already-known palindrome list: it distinguishes pairs of different factors and an infinite-language involution.

## Relationship to sources and limits
The factor-complexity identity \(2n\) and finite ordinary-palindrome list are credited to Fici–Shallit. The complementary-factor avoidance setting is credited to Currie et al. The proof does not classify all long factors or determine the fixed-point count of reverse-complement, and unlocated equivalent Toeplitz-symmetry literature remains possible. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
