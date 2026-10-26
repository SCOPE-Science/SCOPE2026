# Scientific review

## Correctness

**PASS.** The exact histogram follows from a marked-run bijection: the local update flips exactly singleton runs, ordered one-run and zero-run compositions have the stated binomial counts, and division by the number of possible marks removes overcounting. The sharp minimal-support theorem follows from the inequalities \(t\le r-1\) and \(s\ge\max(0,2r-h)\), together with explicit extremal run constructions. Complete enumeration of the five possible critical cases in the \(n\equiv1\pmod6\) class and of two or one cases in the remaining residue classes yields the multiplicity formulas. Independent direct simulation of all configurations through length 18 and exact-formula checks through length 101 reproduce the assertions. Finite checks corroborate rather than replace the combinatorial proof.

## Originality

**PASS, subject to bibliographic risk.** Chebotarev and Peleg's 2022 study treats small winning coalitions on classes of regular graphs; it motivates, but does not directly give, the full input-support/output-support enumerator or count the winning configurations at the minimum on one fixed cycle. Broere and collaborators' majority-domination concept covers the *type* of extremal support question, so the minimum-support threshold by itself is not claimed as an original mathematical invariant. Nakar and Ron's 2022 automaton work studies eventual configurations and periods, not the joint distribution after one update. The new joint histogram and its sharp coalition multiplicity specialize the model in a nontrivial way. The possibility of an equivalent formula in older combinatorics or cellular-automaton literature remains; the full 1986 Fishburn–Hwang–Lee paper was not available for complete-text comparison.

## Value

**PASS.** A two-tier vote is sensitive both to the initial number of supporters and to *their placement*. Exact counts by both quantities quantify that spatial sensitivity across every finite cycle rather than only exhibiting isolated examples or providing existence bounds. The closed form at the sharp passage boundary identifies how many of the sparsest winning arrangements exist, distinguishing the three residue classes modulo six. The work is exact for arbitrary sizes and usable for probability calculations when coalitions are sampled uniformly subject to size. It does not address repeated updates or heterogeneous network structures.

## Remaining limitations

Classical run-counting and the one-step majority map are known; neither is presented as a new technique. The distinction between a new application and an overlooked existing formula depends on further domain-expert bibliographic checking. The analytical claim is for labeled binary configurations on cycles, not for eventual consensus or strategic stability.

Self-review: passed. Independent audit: not yet performed.
