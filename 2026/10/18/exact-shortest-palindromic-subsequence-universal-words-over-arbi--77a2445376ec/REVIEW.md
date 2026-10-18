# Self-review

**Claim reviewed:** The complete minimum-length, extremal-word normal form, and labeled count for palindromic scattered-subsequence-universal words over every \(q\ge2\) and \(k\ge1\).

**Correctness — PASS.** The greedy full-alphabet-block equivalence follows directly by forcing an initial letter that first completes the alphabet. Parity of letter multiplicities gives the sharp length lower bound. Mirrored permutations construct matching words. For odd \(k\), greedy partitions on both ends trap a full-alphabet middle factor; equality in the length estimate forces the claimed unique central shape. Counting follows from uniquely readable blocks. Exhaustive independent direct-subsequence tests support (but do not replace) the proof. Risk: no external formal proof validation.

**Originality — PASS, with limitations.** Lagoutte–Tavenas treat complexity of restricted SCS; Uznański treats supersequences of all permutations, not all \(k\)-words. Adamson explicitly counts all universal words by dynamic programming and recalls the classical arch criterion; that result covers the unconstrained framework but not the palindrome fixed points or their sharp odd-parity census. Later automata-language and Simon-congruence work also does not report the precise constrained extremal classification in inspected full texts. Distinct-scientific-statement comparisons and closest published-record searches are detailed in `AUDIT.json`. Residual risk: an elementary unindexed equivalent derivation is possible; search results cannot certify priority.

**Value — PASS.** This is a complete exact natural class of shortest common supersequences under reversal symmetry, not an arbitrarily selected small length. The parity penalty of \(q-1\), the forced middle-block structure, and the all-parameter factorial count characterize optimal symmetric templates, with no reliance on a larger conjecture or downstream paper-sized application.

**Scope and limits.** Literal palindromes only; all target words have the same length and are embedded noncontiguously; arbitrary alphabet and target-set variants are not solved. The central arch factorization is established literature, not a novelty claim. Finite tests do not prove the universal theorem. Independent bibliographic and proof assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
