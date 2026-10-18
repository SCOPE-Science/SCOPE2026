# Scientific review: Exact complement spectra for alternating binary deletions

## Correctness — PASS
The claim is an exact equality of **sets** of residual words for all integers \(n\ge0\) and \(0\le k\le n\). In any embedding, the parity of the selected positions equals the parity of their selected-word indices, so selected positions have an even number of unselected predecessors. Consequently the residual letters pair into consecutive alternating dominoes. To change a domino phase requires a selected letter; each maximal `ba` run requires entering and leaving odd parity, using at least two selected letters. Conversely, selecting exactly one letter per phase change and adding the remaining even number at the end constructs the prescribed source and deleted subsequence. Standard endpoint counting gives the binomial formula. These steps cover the empty cases and avoid relying on finite checks for the general statement. Two distinct exact test programs validate the small cases described in `VERIFICATION.md`.

## Originality — PASS within examined evidence
The nearest primary source is Adamson–Fleischmann–Huch, arXiv:2603.20790v1 (2026-03-21), read through its arXiv full-text HTML. It defines complement sets, develops general computation methods, treats uniqueness and perfect-shuffle behavior, and in the conclusion explicitly invites closed formulas in special cases. It does **not** state the run characterization or the closed two-parameter formula above. Search comparisons for deletion words, shuffle decompositions and binomial tables identified numerical binomial sums and broadly related deletion/channel results but no exact implication of this complement-set identity. The previously considered deletion pattern \(a^kb^k\) on an alternating source is distinct; swapping it for \((ab)^k\) is not a corollary of the earlier statement. Unindexed historical work remains a priority risk.

## Value — PASS
This addresses a specifically identified structural counting gap in a newly defined word invariant. It gives a normal form for **all** distinct complements in a fundamental periodic family, an exact infinite two-parameter enumeration and a sharp phase boundary \(n\le3k\) at which every possible domino pattern first appears. It distinguishes exponential output growth in the saturated region from polynomial count for a fixed deletion budget. The claim is more than a small parameter table or the bare observation that a familiar binomial sequence occurs.

## Limits
No result is asserted for arbitrary source words or alternate phase choices. The comparison with numerical sequence databases cannot by itself certify originality, and an unindexed equivalent argument could exist. The review verifies the proof as written and the supplied reproducibility checks, not any external certification.

Self-review: passed. Independent audit: not yet performed.
