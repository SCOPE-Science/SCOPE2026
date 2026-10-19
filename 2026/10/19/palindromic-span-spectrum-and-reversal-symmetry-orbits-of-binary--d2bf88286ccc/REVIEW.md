# Scientific review

## Correctness — PASS

Every binary order-five de Bruijn cycle gives a unique Boolean successor rule on sixteen four-bit suffixes. The direct exhaustive traversal checks all \(65536\) successor rules and accepts exactly the \(2048\) rules with a single state cycle; an independent Euler-circuit enumeration yields identical palindrome-span frequencies. The bounds are valid even for the infinite cyclic repetition: the unavoidable factor `1000001` establishes a minimum of \(7\), while a separate exact residual-graph Euler-completion test excludes all possible centered length-\(14\) and length-\(17\) palindromes, and therefore all palindromes exceeding \(15\). A separate full-class symmetry traversal reproduces the exact orbit counts. The combinatorial exhaustiveness arguments, not just console outputs, support the claim. Reproducibility is documented in `VERIFICATION.md`.

## Originality — PASS, with residual risk

The complete primary texts of Gabrić–Sawada (2024), Chang–Wang (2024), and Burris–Motta–Shipman (2016) were compared on their actual invariants. The first studies orientable words lacking reversal-paired windows, the second complement/reversal-symmetric constructions and linear complexity, and the third unoriented coverings of fixed-length reversal classes. None of those inspected results determines the distribution of the *largest palindromic factor* of all standard binary order-five de Bruijn cycles or its symmetry-conditioned orbit counts. Keyword searches for the exact data and the underlying equivalences yielded no covering result. This is evidence of a literature gap, not proof against an unpublished or unindexed prior calculation. References are recorded in `RESULT.md`.

## Mathematical value — PASS

Maximum palindromic-window length is a natural quantitative measure of a reversal obstruction in shortest universal cyclic words. The result supplies its entire sharp finite spectrum, shows that the inevitable palindrome length \(7\) is attainable, identifies the extreme length \(15\), and reveals how the entire distribution splits under the two principal involutions. The invariant is different from merely counting rotation classes or from the standard complement/reversal symmetry census. The result is intentionally an exact first finite case, not an unsupported general-order theorem.

## Boundaries and risks

The statement is binary and order-five only. The priority assessment has residual risk from unindexed work and has not undergone independent scholarly validation. The executable finite proof does not imply a formula at higher orders.

Self-review: passed. Independent audit: not yet performed.
