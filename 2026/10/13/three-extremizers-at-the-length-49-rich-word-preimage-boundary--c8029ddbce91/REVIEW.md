# Self-review

## Correctness
PASS. The finite search is exhaustive because both defining failures are permanent under extension: a forbidden power persists, and palindromic defect cannot return to zero after a non-rich prefix. Two exact richness tests—direct distinct-palindrome counting and the unioccurrent longest-palindromic-suffix criterion—produce identical prefix-tree levels. The final four levels have \(11,6,3,0\) survivors at ternary lengths \(47,48,49,50\), and exact least-period scans directly recheck every binary boundary image.

## Originality
PASS. The 2020 source publishes the scalar cutoff \(49\) for the \(\mathtt{0121012}\) row but not its equality cases. A 2024 follow-up reuses the same obstruction and length-\(50\) backtracking cutoff without a boundary census. Exact-string, equivalent-formulation, broader-coverage, and record-overlap searches found no publication or indexed data source stating the three length-\(49\) preimages.

Residual risk remains that unpublished source-author backtracking output or an unindexed auxiliary file already contains the same three words.

## Value
PASS. This is the complete equality classification at the largest finite cutoff in the source's obstruction table, hence at the bottleneck of a structure theorem proving the binary-rich repetition threshold. The three extremizers' shared length-\(47\) prefix supplies a rigid boundary description rather than an arbitrary finite census.

Self-review: passed. Independent audit: not yet performed.
