# Scientific review

**Correctness — PASS.** The exhaustive search has a complete combinatorial reduction: every maximal word uses all five symbols; first-occurrence normalization is unique; and only new terminal Abelian squares need to be tested at each extension. The attached direct-integer-Parikh checker explores all surviving canonical prefixes through length \(16\), rejects all shorter possible maxima, finds exactly four length-\(16\) witnesses, and confirms their left and right extension obstructions. An independent packed-prefix implementation reproduced the counts and witnesses. The proof is finite and exact, not based on unbounded extrapolation.

**Originality — PASS (best-knowledge historical assessment).** The closely related published four-letter classification of Cummings and Mays (2001) does not imply a five-letter count, and their construction gives a five-letter bound of \(19\). Accessible full texts of Bullock (2004) and Glen–Halldórsson–Kitaev (2009) discuss general bounds and one-sided crucial words without supplying this exact enumeration. Searches for five-symbol, length-\(16\), bicrucial/maximal Abelian-square-free classifications and corresponding results identified no covering statement. The 2003 Korn article is relevant but its full text could not be obtained, so prior-priority uncertainty remains; no categorical uniqueness assertion is made.

**Value — PASS.** The five-letter case is a natural next finite extremal classification after the established four-letter case: it closes an exact minimum at \(16\) and determines *all* extremizers, their labeled count, and reversal pairings. The result strengthens a general-length construction and gives a checkable census of natural objects, not an arbitrary chosen parameter slice or a routine substitution.

A direct finite checker constitutes a finite exhaustive proof only in conjunction with its branch-completeness and sound-pruning arguments, both provided in RESULT.md. No independent external mathematical audit has been performed. Scientific risk concerns possible earlier coverage in Korn (2003) or another unindexed source.

Self-review: passed. Independent audit: not yet performed.
