# Scientific review of exact binary16 logistic expression-order dynamics

## Correctness

**PASS.** The two maps are defined down to bit-pattern interpretation, rounding locations and tie convention. Exact integer formulas generate all \(15{,}361\) values and both full transition graphs. The included standalone program independently validates cycle closure, basin labels, strictly decreasing entry lengths and every start state's reachability. Voronoi weights sum to \(2^{25}\), yielding exact rational ensemble Cesàro means. A separate native NumPy binary16 implementation reproduced all \(30{,}722\) transitions. This is an exhaustive proof for the finite stated domain; no evidence is claimed for an infinite-precision analogue.

## Originality

**PASS with residual priority risk.** The earliest inspected preprint from 2022 establishes the general finite-precision dynamical phenomenon; its original full-text methods and Bernoulli-map sections do not include this logistic comparison. The published 2023 expansion includes the logistic map and low-precision fixed points, but its logistic-map discussion does not give the two exact evaluation orders or their entire basin-weighted invariant statistics. Galias 2021 classifies logistic maps in single/double precision; Persohn–Povinelli 2012 studies different finite-precision pseudorandom settings. The exact binary16 comparison cannot be inferred from any of these qualitative or alternate-format results. Catalog searches, relevant prior claims, and variant phrasings produced no matching table. An overlooked implementation-specific supplementary table remains a genuine possible antecedent; no absolute uniqueness is asserted.

## Value

**PASS.** The result quantifies the effect of evaluation semantics on invariant numerical statistics for the paradigmatic chaotic logistic map. An exact \(15{,}361\)-state classification and input-ensemble weighting expose a nontrivial \(75\)-fold mean discrepancy and a change of long-cycle period from five to forty, establishing a reproducible benchmark beyond ordinary simulations or a few illustrative trajectories.

## Limits

The result is valid only for the two specified finite maps, including subnormals and ties-to-even, and for the initial ensemble defined by uniform real sampling before rounding. Both statements about novelty and mathematical correctness are awaiting an independent check.

Self-review: passed. Independent audit: not yet performed.
