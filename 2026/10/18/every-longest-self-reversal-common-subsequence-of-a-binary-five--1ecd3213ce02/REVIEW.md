# Scientific review: sharp binary reversal-LCS run threshold

## Correctness — PASS

The result quantifies over **all** distinct maximum-length common subsequence words of a binary word and its reversal. For one through four runs, the proof analyzes every possible output run shape; for five runs, it excludes even-run outputs by strict extension, treats the unique five-run optimum, and partitions three-run outputs into all four earlier/later embedding combinations. The two same-side cases are strictly shorter than an explicit five-run palindrome; the two cross-side cases have independent, symmetric endpoint caps, so their unique maximum words are palindromes. The sharpness witness is a binary word of length seven with two explicit nonpalindromic optimal outputs; the six possible placements of a doubled run settle all length-seven exceptions. Both LCS dynamic programming and independent subsequence-set enumeration were executed on the packaged checker. The infinite assertion relies on the proof rather than finite sampling.

## Originality — PASS, with residual risk

Brodal, Fagerberg, and Rysgaard, *On Finding Longest Palindromic Subsequences Using Longest Common Subsequences* (ESA 2024, DOI: 10.4230/LIPIcs.ESA.2024.35), is the closest primary work. It proves general equality of LCS/LPS lengths and specifies which backtracking strategies always yield a palindrome; it exhibits nonpalindromic valid LCS outputs. These general results **do not imply** that every optimum output is palindromic for all binary five-run inputs, nor the sharp six-run failure and first-length-seven classification. The inspected main results, proofs, figures and examples do not state these restrictions. Chowdhury et al., *Computing a Longest Common Palindromic Subsequence* (arXiv:1110.5296), explicitly impose palindrome structure for two independent inputs, rather than classifying when every unrestricted LCS is already palindromic. Targeted web and mathematical-research-record queries for binary run-bounded reversal LCS and the explicit smallest witness returned no known dominating classification. Search absence is not uniqueness proof; the unindexed-literature risk remains.

## Mathematical value — PASS

The ESA 2024 phenomenon makes LCS backtracking choice relevant for palindromic-subsequence reconstruction. Here a natural structural parameter, the number of maximal constant runs in the binary input, yields an **algorithm-independent safety guarantee** for arbitrary run lengths. The threshold is optimal and its shortest failures form a unique labeled-symmetry orbit. This is a precise structural boundary rather than an arbitrary computation or a restatement of equality of LCS and LPS lengths.

## Limits

Only the binary alphabet and the first five runs are classified universally. Larger-alphabet counterexamples occur with fewer runs, and some binary words with six or more runs are still safe. The theorem does not enumerate all larger obstructions or all LCS alignments. Direct checks cover finite lengths and finite run tuples; the infinite statement uses a combinatorial proof. An equivalent previously unindexed theorem cannot be ruled out without independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
