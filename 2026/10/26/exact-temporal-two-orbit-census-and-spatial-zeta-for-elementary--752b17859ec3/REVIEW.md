# Scientific review: temporal-two configurations of elementary cellular automaton 18

## Correctness — PASS

The statement is restricted to elementary rule 18, its exact second iterates on cyclic spatial rings, and the spatial shift on the corresponding finite-type subshift. The proof derives the 20 admissible five-bit windows directly from the eight-case local rule, so that the trace of the 16-state de Bruijn adjacency matrix counts the exact configurations for every ring length. The recurrent cycle census comprises the zero loop and six nontrivial elementary cycles of lengths 4, 5, 5, 6, 10, 10; two disjoint-pair terms cancel the two length-ten terms in the finite determinant. The resulting zeta, recurrence, missing ring lengths, and two-cycle counts follow algebraically. The root-modulus separation establishes the entropy and asymptotic. The standalone verifier replays the critical finite cycle certificate and independently brute-forces rings 1 through 15. Finite replay is not substituted for the all-length transfer-matrix proof.

## Originality — PASS under examined evidence

Zhu–Richard (arXiv:2610.10967v1, October 2026) analyzes Koopman spectra and specifically discusses the family containing elementary rule 18, using finite spatial sizes; its spectral taxonomy does not imply a formula for every temporal two-cycle count or the exact spatial zeta. Stricker's 2023 complete paper analyzes *maximal temporal cycle length* and reports tabulated size-limited rule-18 data, not all-size multiplicities of two-cycles. Sabrié–Törmä (arXiv:2308.12744, earliest preprint August 2023) studies kink and limit-set behavior; its explicit spatial period-four point satisfying the second-iterate condition gives one witness already known and is not claimed new. Searches for the recurrence, rational denominator, equivalent spatial two-cycle census, and missing-length classification found no directly covering theorem. The old four-periodic example and general finite-type transfer machinery are credited. Priority risk remains from older non-indexed cellular-automaton literature or equivalent spectral tables.

## Mathematical value — PASS

Rule 18 is a standard interacting-defect cellular automaton investigated both via limit-set theory and a new finite-ring Koopman-spectrum classification. The exact enumeration is an all-ring dynamical invariant unavailable from maximum cycle lengths alone. The unexpected numerical-semigroup existence set \(\langle4,5,6\rangle\) (including the isolated exclusion at seven), the full rational spatial zeta, and the plastic-constant growth rate classify its entire temporal-two sector, enabling principled tests of finite ring-size and time-two spectral multiplicities. This is a complete natural subproblem, not merely a short table of small simulations.

## Limits and comparison risk

No statement is made about periods greater than two, the full time-direction dynamical zeta, or periodic points of the full cellular automaton. Historical priority remains subject to further independent review. The published finite-ring data could contain some individual counts without implying the all-length classification.

Self-review: passed. Independent audit: not yet performed.
