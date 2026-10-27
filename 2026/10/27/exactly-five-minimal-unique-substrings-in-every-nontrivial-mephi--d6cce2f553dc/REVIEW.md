# Scientific assessment of the Mephisto–Waltz MUS classification

## Correctness — PASS

The exact base case on `001001110` has five singleton length-three factors, and every length-four factor contains a singleton triple. For arbitrary source words, the four crossing-image pairs prove unique phase decoding from length five onward. Occurrences of a decoded factor biject with occurrences of its covering source factor. The proof uses this to lift the five shortest unique intervals by an exact affine position transformation and to exclude longer minimal unique intervals through both endpoint deletions. The checker independently confirms the resulting spectra for lengths \(3^2\) through \(3^9\), and exhaustive brute factor counting to \(3^5\). Infinite correctness rests on the written induction, not enumeration.

## Originality — PASS within examined evidence

The most relevant primary source, Kishi–Guo–Urbina–Bannai, arXiv:2605.18034v1 (May 18, 2026), explicitly lists the morphism among strongly interference-free examples and derives MUS formulas for Fibonacci and Thue–Morse words, but does not provide this formula for its Mephisto–Waltz iterates. Indexed research-record searches for both the named word and the numeric morphism found no covering statement; the earlier accessible research ledger contains no overlapping claim. The sequence entry OEIS A064990 identifies the word but does not imply its complete minimal-unique spectrum. Unindexed equivalent work is a residual priority risk.

## Mathematical value — PASS

The result is an exact all-iterate classification of a standard substring uniqueness invariant for a natural automatic morphic word highlighted in recent occurrence-preservation literature. It explains a nontrivial stabilization: **five** distinct minimal unique occurrences at every level despite exponential growth of the words and of their common minimal-unique length. The source's conclusion proposes investigating fixed points of strongly interference-free morphisms; this gives a complete, concrete example rather than a routine finite census. The result does not generalize to all morphisms.

Self-review: passed. Independent audit: not yet performed.
