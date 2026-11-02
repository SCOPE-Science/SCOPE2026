# Scientific review of the cyclic Rule-18 image classification

## Correctness

**PASS.** The local transition has the exact form \((1-b)(a\oplus c)\). Every positive-length zero run between input ones produces either no output ones (length one) or its two endpoint ones (length at least two). This establishes necessity. Conversely, an allowed alternating pairing gives the explicit input consisting of zero-valued pair arcs and one-valued separating arcs, establishing sufficiency for every ring length. Stars-and-bars and inclusion–exclusion count the indexed outputs without dividing by rotations, and two exactly stated cycle-counting series yield the logarithmic-derivative generating function. The dominant reciprocal roots establish the claimed asymptotic. Independent exhaustive checks of all inputs and outputs through length eighteen and the integer coefficient formulas through length seventy returned `VERIFY_OK`.

## Originality

**PASS, with residual historical risk.** Relevant full texts inspected include Hanson–Crutchfield (1991 working paper), Jen's 1987 preimage recurrence paper, Meunier's arXiv:1406.5306v1, and the accessible 2026 Sabrié–Törmä article. They respectively establish attractor/domain language techniques, general preimage recurrences, computational-complexity classification, and necessary local preimage obstructions. None of the inspected results directly states or implies the all-length cyclic predecessor construction together with exact fixed-density enumerations. Jen's 1988 paper on cyclic attractors is a close-boundary reference but its full text could not be obtained: its available abstract studies attractors and fixed-period limit cycles rather than the entire one-step image. No claim of independently certified priority is made; the possibility of an unindexed equivalent remains.

## Value

**PASS.** Reachability of a desired cyclic output and the size of the image after a single application are natural finite-state questions for a classical nonlinear cellular automaton. The result unifies a constructive recognition criterion, a count at every output Hamming weight, an exact full-length generating function and an exponential information-loss rate. These are all-length structural results, not an arbitrary isolated finite statistic or a routine restatement of general algorithmic decidability.

## Closest literature and limitations

Hanson and Crutchfield's Rule-18 attractor-domain analysis and Jen's general preimage methods are the closest archival conceptual antecedents. Sabrié and Törmä's later necessary obstruction for patterns `11v11` with odd one count is related but does not give the cyclic sufficiency or enumerator. The theorem does not count predecessor multiplicities or address multi-step images. Jen's cyclic-attractor article was available only in abstract/metadata form.

Self-review: passed. Independent audit: not yet performed.
