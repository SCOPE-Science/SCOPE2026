# Scientific review

## Correctness (C): PASS
The finite witness has length \(106\) over the stated four-letter alphabet. Both standalone programs inspect every cyclic length-four window including wraparound indices; a direct pairwise check covers all \(5565\) unordered distinct window pairs and rejects any palindromic window. The Python verifier independently enumerates all nonpalindromic reversal orbits, obtaining \(120\) total, \(106\) present and \(14\) absent. The only conclusion is the existence lower bound \(M_4(4)\ge106\). Computation is complete for that finite witness, not an asymptotic extrapolation.

## Originality (O): PASS, subject to residual priority risk
Mitchell and Wild (arXiv:2507.02526v1, full text Section 6 Table 7) explicitly state a largest known period \(88\) and upper bound \(112\) at alphabet size four, order four. Their Sections 4–5 constructions and Table 6 attain \(88\), not \(106\). The complete 2024 Gabrić–Sawada and Alhakim et al. accounts address broader constructions and bounds but do not state this particular \(106\)-symbol certificate. Comparisons covered reversal equivalence, constructive lower bounds, and upper bounds; an unindexed or later construction with period at least \(106\) remains possible. The assertion is novelty relative to inspected literature, not proof of global priority.

## Value (V): PASS
This is an exact, independently replayable construction for a specifically unsettled extremal finite parameter. The documented interval \(88\) through \(112\) is narrowed to \(106\) through \(112\), closing \(18\) of its \(24\) length units, or \(75\%\) of the open numerical gap. Orientable sequences support bidirectional position sensing with a fixed-size observation window. The magnitude of the improvement makes this more than a routine reformulation or single-unit numerical increment.

## Literature and limitations
Gabrić–Sawada (2024): arXiv:2407.07029v1; Alhakim et al. (2024): arXiv:2407.14866v1; Mitchell–Wild (2025): arXiv:2507.02526v1 (especially Table 7). No upper-bound improvement or maximality conclusion is claimed. There is no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
