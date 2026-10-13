# Self-review

## Correctness — PASS
The stated alphabet is unambiguous for every \(n\ge2\) and every nonempty marked set \(J\). The inverse-set proof tracks exact preimages of every proper cyclic interval: an inverse idempotent can enlarge it only by adding the immediate predecessor of its left endpoint at a marked site. Every reset requires at least \(n-1\) marked enlargements; the matching scan builds exactly that many. The even- and odd-state two-marker formulas follow from cyclic visit counts, not finite extrapolation. A separate exhaustive forward-subset search, constructive witness replay and interval case enumeration reproduce all selected finite tests. The proof does not claim a result for arbitrary directed unitary letters.

## Originality — PASS, qualified by priority risk
The single-marker \((n-1)^2\) instance is a known Černý fact and explicitly credited. Relevant accessible original articles on primitive automata with unitary letters and completely reachable automata address existence, orbital criteria or quadratic bounds, rather than the exact arbitrary-mark scan and two-site parity gap. Their general results cannot be substituted for equality of shortest reset lengths. A 2022 simple-idempotent article was compared at abstract level only; an earlier unindexed derivation cannot be excluded. No independence or comprehensive publication-priority certificate is claimed.

## Value — PASS
The theorem provides an exact natural invariant for every placement of chosen neighboring unitary mergers on a cycle, with an explicit constructive optimal word. The two-marker law distinguishes even state counts from odd counts and quantifies circular separation in the odd case, a structural feature absent from generic quadratic upper bounds.

## Closest prior results and limits
Volkov (arXiv:2306.13317) treats primitivity and synchronization for defect-one transformations; Rystsov–Szykuła (arXiv:2307.01302) give the unitary-letter orbital-graph criterion; Ferens–Szykuła (arXiv:2208.05956) treat complete reachability and quadratic reaching bounds. These are not claimed as new. This is a self-review of the stated theorem only; literature priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
