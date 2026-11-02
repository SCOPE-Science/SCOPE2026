# Scientific review: binary block-power palindrome spectra

## Correctness — PASS

The claim covers all positive integer run lengths and repetition counts, including one repetition and equal run lengths. A mixed palindrome must be centered at the midpoint of a complete run, and its maximal symmetric radius is exactly the minimum of the remaining lengths on its left and right. Maximizing these integer radii yields the two stated parity-dependent cutoffs. These exhaust all nonunary palindromes; unary factors are straightforward. Every palindrome of length at least two is in bijection with an occurring palindromic interior and a two-sided letter choice, giving the exact polynomial identity for missing extensions. The cardinality and maximum length then follow algebraically. A standalone literal-factor checker agrees for 392 parameter triples and 14,504 coefficient checks; these finite tests supplement, rather than replace, the general proof.

## Originality — PASS, with specific residual risk

Mieno et al., arXiv:2006.02134 (first posted 2020-06-03), introduce minimal absent palindromic words and prove their general eertree-edge characterization in Section 5.2. The present calculation uses that principle and does not claim the general extension identity as new. Glen et al., arXiv:0801.1656, establish richness properties of periodic words; their general theory, combined with the missing-edge principle, explains why the total number is the word length plus four. The total alone is **not** asserted to be a new theorem. The claim assessed here is the complete two-ray classification of occurring palindromes in finite powers with arbitrary unequal run lengths, the exact per-length MAPW polynomial including endpoint parity effects, and the longest-MAPW boundary. These extra claims are not stated in the inspected portions of either primary source and do not follow solely from the total-richness result. The superficially related earlier finite-power findings concern different predicates and, where relevant, at least three distinct period letters. Published-record searches and comparisons did not identify an equivalent length spectrum. An equivalent derivation in less accessible specialized literature remains possible.

## Mathematical value — PASS

A complete length-resolved antidictionary for a natural, two-parameter run-length-encoded periodic family is a useful exact benchmark for palindrome-indexing and absent-palindrome algorithms. The result gives an explicit compressed description of every occurring palindromic factor, determines all MAPW lengths and multiplicities in one polynomial, and identifies the exact longest forbidden palindrome. The dependence of the radii on the parity of the repetition count and on the two distinct run lengths captures the finite-endpoint behavior that general rich-word cardinality formulas suppress. The contribution is modest and specific, not a general algorithmic improvement or an asymptotic breakthrough.

## Scope and literature limitations

The result treats only finite binary powers with a two-run primitive period and the MAPW interior-occurrence definition. General eertree characterization, periodic richness, and ordinary minimal-absent-factor algorithms are background. The RLE absent-factor paper by Akagi et al. (CPM 2022) was considered from its abstract only and is not treated as full-text evidence of noncoverage. Neither searches nor single-source inspections establish absolute priority; an independently checked literature review remains desirable.

Self-review: passed. Independent audit: not yet performed.
