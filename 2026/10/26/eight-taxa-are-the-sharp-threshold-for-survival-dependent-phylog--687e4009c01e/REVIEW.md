# Scientific review

## Correctness — PASS

The model specifies an unordered rooted full binary tree, unit branch lengths, independent identical tip survival, rooted PD, and protection of exactly one taxon. An ancestral edge is added by protection exactly when all of its descendant tips otherwise fail, producing the exact \(\sum q^{m_e}\) benefit. Cumulative clade-size dominance implies polynomial dominance for the full open probability interval by summation by parts. The recursion enumerates every unordered rooted full binary shape through eight leaves, tests all leaf profiles, and identifies exactly one shape lacking a cumulative-dominant leaf at eight, none below. The exception is handled by four explicit profiles and the exact factorization \(q^3(q^2+q-1)\). Direct subset enumeration at three rational probabilities checks all eight exceptional-tree leaves independently. These finite computations are exhaustive for the stated cutoff, not an extrapolation to arbitrarily many taxa; the analytic inequalities cover every real parameter in the stated range.

## Originality — PASS, with bibliographic risk

Steel, Mimoto and Mooers (2007), Theorems 3.1 and 4.1, establish the rooted HED and HEDGE formulas; Martyn et al. (2012) establish efficient general HED evaluation and discuss changing conservation priorities. These earlier results encompass the baseline expected-diversity identity but do not state the exact eight-leaf least-size threshold, its exceptional topology uniqueness, or the exact survival switch. Hartmann and Steel (2006) supplies earlier relevant optimization context, but full-text inspection was unavailable; only its detailed public abstract and publisher metadata could be inspected. Searches under HED, HEDGE, uniform extinction, phylogenetic priority ranking reversals and binary-tree clade-size profiles did not reveal a dominating theorem or existing exact table; absence from search is not proof of publication novelty. The residual risk is earlier equivalence under phylogenetic distinctiveness, probability-polynomial ordering, or combinatorial binary-tree rankings.

## Mathematical value — PASS

The question asks whether a single species chosen for protection remains best when the common background extinction rate is uncertain. Equal risks and branch weights isolate topology as the cause of a conservation-priority reversal. The theorem identifies a sharp minimum tip count and classifies *all* shapes at that first failure size, giving a unique normal form and exact switch. This is a natural finite structural cutoff for a standard biodiversity objective rather than an arbitrary score computation. It is a baseline mathematical model, not an empirical prediction: unit branch lengths need not be clocklike, and taxon-specific risks, heterogeneous branch lengths, and multi-taxon budgets are excluded.

Self-review: passed. Independent audit: not yet performed.
