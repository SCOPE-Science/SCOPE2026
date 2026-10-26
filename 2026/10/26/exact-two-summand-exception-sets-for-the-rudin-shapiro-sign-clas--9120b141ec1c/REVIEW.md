# Mathematical review

## Correctness — PASS

The 32-state machine tracks ordinary binary addition carry, both previous summand bits and both adjacent-\(11\) parities. Its transition invariant proves equivalence between acceptance and a two-summand representation. Saturating the binary-value accumulator at 21 exactly recognizes the proposed finite exception sets, whose greatest element is 20. Exhaustive breadth-first reachability over the machine-subset/value product checks all finite binary digit strings, with 88 reachable product states in each of the three parity cases and no mismatched accept predicate. The actual packaged Python checker reproduces these conditions without external data. Direct arithmetic below 3000 provides a distinct finite sanity check only. No experiments are substituted for the complete finite-state argument.

## Originality — PASS within inspected evidence

Shallit's 2021 paper treats the two-summand evil/odious (Thue–Morse) parity problem, whereas the current claim treats overlapping-\(11\) (Rudin–Shapiro) parity. Rampersad and Shallit's 2023 work treats summatory signed sequence functions, which are different objects. Dombi and Konieczny give general representation-count/pseudorandomness context, not exact threefold pairwise two-summand exception lists. A particularly relevant 2019 paper by Rajasekaran–Shallit–Smith contains a figure on **mixed Thue–Morse/Rudin–Shapiro** sums; its abstract and figure labels were accessible but its whole article was not, so the comparison is limited and an unreported implication remains a genuine risk. Targeted external searches and mathematical-record comparisons located no matching classification; lack of hits is not uniqueness proof. Publication priority is not independently guaranteed.

## Value — PASS

The result completely settles the natural order-two additive representation problem for both sign classes of the classical Rudin–Shapiro sequence, including their mixed sumset and all finite exceptions. It distinguishes the full additive basis property of the nonnegative-sign class from the exact finite obstructions of the negative-sign class. The explicit exceptions are not automatic consequences of the literature's generic decidability or asymptotic coverage conclusions, and a complete classification is useful for subsequent arithmetic questions about this automatic sequence.

## Residual risks and limitations

Earlier automata constructions may contain unreported derivations of the lists, especially the incompletely accessible 2019 mixed-sum study. No claims are made about pair-representation multiplicities, alternative digit blocks or moduli, or independently certified publication precedence. The attached verifier implements a finite-state proof; independent code review has not occurred.

Self-review: passed. Independent audit: not yet performed.
