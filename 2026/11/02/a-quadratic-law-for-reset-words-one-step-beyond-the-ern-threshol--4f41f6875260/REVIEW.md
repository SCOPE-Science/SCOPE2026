# Scientific review of the one-step Černý reset-word law

## Correctness — PASS

The inverse-image construction proves a sharp count of the required rotation and merge letters for each terminal state. Its first-appearance argument is valid even if intermediate inverse images shrink, and the one-letter slack precludes a shrink. For fixed minimal rotation count, the lone extra merge letter is neutral exactly at the positions listed in the theorem. Summing the disjoint word families proves the quadratic count. An independent forward-subset program checks shortest and next-shortest target counts for \(2\le n\le13\), and compares literal exhaustive reset-word sets to the complete classification for \(2\le n\le8\). The all-parameter conclusion rests on the proof, not the finite tests.

## Originality — PASS, with residual risk

Szykuła's 2017 treatment of avoiding words and general reset-threshold upper bounds includes the classical Černý example but not an enumeration at one additional letter. Szykuła–Zyzik (2022) provides exact algorithms for shortest reset lengths but no closed formula for the second-shortest layer of this family. Rodaro's 2017 ideal-language treatment concerns factor-minimal reset words and general regular ideals rather than the precise boundary-language coefficient proved here. Relevant published research records on short reset words in other automata and early-rank thresholds for the Černý family do not imply this exact second-shortest count. Searches did not locate an equivalent formula; a previously unlocated specialization is the principal residual risk. Some relevant online research repositories exposed only result summaries, not complete manuscripts, so conclusions about those particular sources are limited accordingly.

## Mathematical value — PASS

The number of reset words with just one letter of slack is a natural measure of rigidity near the extremal reset threshold. The theorem supplies both the sharp \((n-2)^2+3\) count and the complete location-level classification for every state size, distinguishing a quadratic boundary layer from the unique optimal word. The explicit family provides mathematical structure and reference instances for algorithms that recognize or enumerate synchronization words; this is more than a finite table or trivial rewriting of the known threshold.

## Closest literature and limits

- Szykuła, arXiv:1702.05455 (2017): reset-threshold and avoiding-word bounds, not second-layer counting.
- Rodaro, arXiv:1708.04864 (2017): abstract minimal-reset-word ideals, not this labeled coefficient.
- Szykuła and Zyzik, arXiv:2207.05495 (2022): algorithms to compute the reset threshold, not an all-\(n\) near-threshold spectrum.
- Published research records on the Černý early deficiency profile and near-extremal reset words of different automata were checked at the statement level only; they do not state the present claim, but full manuscript comparisons for some records remain unavailable.

The theorem does not characterize longer reset words or general synchronizing automata. Self-review cannot substitute for an independent audit.

Self-review: passed. Independent audit: not yet performed.
