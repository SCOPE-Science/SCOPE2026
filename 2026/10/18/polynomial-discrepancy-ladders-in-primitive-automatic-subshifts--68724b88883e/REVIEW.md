# Review: Polynomial discrepancy ladders in primitive automatic subshifts

## Correctness — PASS

For all positive integers \(r,d\), the substitution has \(r\) identity columns, a successor, and a reset. Exact enumeration of compositions without resets proves the binomial depth profile; compositions with resets give the complete constant kernel, including the all-successor constant that first appears at depth \(d+1\). The fixed-point column identity identifies formal maps with actual two-sided progressions. The primitive, height-one and aperiodic hypotheses are checked, and the discrepancy operator has diagonal \(r\) plus a nilpotent successor component. The published Theorems A/B then yield the dynamical classification. A standalone program passed 1,822 sampled integer assertions; the infinite assertions rely on the proof.

## Originality — PASS under examined evidence

Closest work: Gröger–Krawczyk (arXiv:2602.23267), in particular Example 5.3 and Proposition 5.6, provides a single linear example and the general qualitative law \(\Theta(m^{d_s}\lambda_s^m)\); Theorems A/B establish nullness/tameness and amorphic complexity in general. Fuhrmann–Gröger, *Math. Z.* (2020), supplies earlier general bounds. Those existing results are not claimed as discoveries. Neither examined source states the uniform explicit two-parameter construction, the exact binomial progression profile at every depth, nor the full finite-kernel census. Searches of published mathematical records and known prior claims did not identify the same specialization. An equivalent historical reset-counter construction remains a priority risk.

## Mathematical value — PASS

The general literature exposes a polynomial/exponential dichotomy but does not realize all polynomial degrees in a single elementary uniform construction with exact finite-scale data. The family separates two independent controls: the discrepancy base \(r\), which governs the known tame/null boundary, and the exponent \(d\), which can be made arbitrarily large without changing amorphic complexity when \(r=1\). The finite-depth formulas refine an entire infinite family, not an arbitrary fixed small case, and distinguish systems the coarse invariant collapses.

## Scientific limits

No assertion about arbitrary substitutions or non-power progression steps. The dynamical characterization is used from the cited literature, not newly proved. Historical priority uncertainty and lack of independent audit remain.

Self-review: passed. Independent audit: not yet performed.
