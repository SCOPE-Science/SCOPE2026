# Research review

## Correctness
PASS. The source's scoring rule is reproduced without normalization changes. A score-gap lemma handles all reports and all candidates with arbitrary other-voter ballots; a lattice argument excludes strict profitable deviations for at most three candidates and any electorate. For four candidates with at most three voters, every ordered opponent profile, sincere ballot and deviation is enumerated by the included exact-rational code, with zero qualifying events in \(256+4096+65536=69888\) checks. The four-voter witness independently has strict score maxima and exact totals \((14/3,10/3,0,0)\) and \((14/3,6,4,4)\). The scope excludes tied endpoints and arbitrary numbers of candidates or electors beyond the stated bounds.

## Originality
PASS within a documented priority risk. Section 2.5 of the first-public 2025 paper establishes optimal FVR guarantees for the chosen weighting rule and Section 2.6 proves uniqueness in a scoring-rule class; these statements do not imply the presented strategic threshold. Its disapproval-score dual form was explicitly compared. Searched prior records for FVR manipulation, ballot-size weights, strategic padding and strict-winner boundaries; closest returned findings concern Baldwin/Kemeny ranked voting, probabilistic serial assignment and matching, none implying this result. Endriss analyzes strategic ballots in a different scoring regime; Alcalde-Unzu–Vorsatz use size approval weighting with a different monotonicity and the complete text was not available. Priority risk remains for unindexed or inaccessible strategic-voting literature. No search is claimed to prove uniqueness of this finding.

## Value
PASS. FVR-optimality is a natural proportional-veto guarantee, yet its ballot-size weight induces an incentive to approve candidates one dislikes. The all-electorate small-candidate obstruction, the first exact critical electorate and a tie-independent witness sharply locate that defect in the exact one-winner model. The result is a structural interpretive boundary, not just an arbitrary numerical example: with three candidates the available score increments lie on a lattice that makes strict manipulation impossible.

## Scientific limitations and nearby literature
The source's representation theorems do not address this sharp strategic property. Ordinary strategyproofness and tie-sensitive manipulation remain outside the result; candidate counts greater than four are not classified. A potentially relevant size-approval source was inspected only by abstract, with residual full-text priority risk. Exhaustive finite checking is used only at the stated fixed candidate and voter sizes.

Self-review: passed. Independent audit: not yet performed.
