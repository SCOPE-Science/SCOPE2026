# Assessment of the exact length-thirteen one-gap three-deck census

## Correctness — PASS
The observation is fixed by fourteen exact integer counts of one-, two- and three-symbol spaced subsequences. The append-one-symbol recurrence is derived by partitioning witnesses according to whether they use the final index; it handles the index-separation requirement by using a prefix shortened by two. A full ordered-map classification across all \(8192\) possible length-thirteen words gives four doubletons, \(8184\) singleton classes, and no other fibers. An independent literal index-tuple enumeration verifies both the full histogram and the precise four pairs. A code chooses at most one representative from each fiber, so its maximum size is \(8188\), and the four independent binary choices give exactly \(16\) maximum labeled codebooks. There is no statistical sampling or incomplete search.

## Originality — PASS subject to bibliographic risk
The 2022 primary paper of Golm–Nahvi–Gabrys–Milenkovic already reports that the meaningful first one-gap three-deck collision occurs at length \(13\), and explicitly prints one pair. Those statements are **not** claimed as new. The published numerical table supplies example pairs, not an exhaustive count of all fibers, their cardinalities or the maximum one-per-fiber codes. The 2023 full-text Rigo–Stipulanti–Whiteland paper studies order-two equivalence and factor complexities of infinite words, rather than the unrestricted binary order-three fiber histogram at length \(13\). Searches of published mathematical records using deck/binomial aliases and the exact parameter did not identify this stronger classification. An unindexed full census may exist; independent bibliographic audit has not been performed.

## Mathematical value — PASS
The calculation is at the published first nontrivial reconstruction-ambiguity threshold for the natural one-gap length-three observation model. At that precise threshold, it determines the entire obstruction graph rather than merely exhibiting one collision: exactly four reversal pairs, two complement orbits, the sharp size \(8188\) of a zero-error reconstruction code, and the complete family of \(16\) maximum labeled codebooks. These exact invariants directly determine information distinguishability and optimal code design at the threshold. The statement is finite and does not purport to improve the known threshold or establish new asymptotic bounds.

## Boundaries
The published threshold is previous literature. There is a degenerate shorter collision at length \(2\), where no spaced length-two witness is available. The claim explicitly specifies the domain of lengths and all fourteen observed pattern counts. The two exhaustive programs are independent methods, not independent institutional validation.

Self-review: passed. Independent audit: not yet performed.
