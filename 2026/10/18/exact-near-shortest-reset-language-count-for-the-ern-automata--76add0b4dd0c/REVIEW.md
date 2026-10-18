# Mathematical assessment

## Correctness — PASS

The inverse-set action of the Černý letters preserves cyclic intervals on every successful preimage path. The gain/loss/no-op classification is obtained directly from the transition function. Each productive gain fixes a subsequent rotation gap of at least \(n-1\) symbols. Equation (1) in the main proof shows that a word of length at most \((n-1)^2+1\) cannot contain any inverse loss. At excess length one, the only remaining possibilities are two boundary inverse rotations or one harmless inverse merge step. Every permitted insertion location is enumerated and a corresponding reset word is constructed; the single excluded location causes a cardinality loss. These steps prove both completeness and disjointness for every integer \(n\ge3\).

A standalone checker independently verifies exact forward-image-subset counts for \(3\le n\le13\) and literal-word enumeration for \(n=3,4,5\). These finite checks are corroboration rather than a replacement for the proof.

## Originality — PASS, with residual risk

The closest primary works are Rodaro, arXiv:1708.04864, on minimal reset languages, Ferens and Szykuła, arXiv:2208.05956, on reaching bounds, and Ferens–Szykuła–Vorel, MFCS 2021, on avoiding thresholds. Their inspected claims do not state or imply the exact \(L+1\) word count. Two inspected prior results for the same Černý automaton concern worst-case avoiding thresholds and initial rank reduction, respectively; neither implies a count of distinct full-reset words at one unit above the minimum. Literature searches of near-optimal resets and exact word multiplicities identified related results for different automata but no covering theorem. Priority remains best-knowledge rather than a claim of proved uniqueness across the literature.

## Mathematical value — PASS

The reset-language spectrum is a natural refinement of reset threshold: two automata with the same shortest synchronizing length may have dramatically different counts of near-optimal words. The theorem determines the first coefficient beyond the minimum for an infinite extremal family, and locates all extra-letter insertions through a nontrivial forbidden phase in inverse arc dynamics. It is a complete classification, not a table extrapolation or a restatement of the shortest threshold.

## Boundaries and remaining risks

The exact formula is only for excess one and the specified binary family. Older sources in cyclic/one-cluster automata or minimal-reset-language enumeration could contain an equivalent unlabeled formulation not exposed in searched text. No external independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
