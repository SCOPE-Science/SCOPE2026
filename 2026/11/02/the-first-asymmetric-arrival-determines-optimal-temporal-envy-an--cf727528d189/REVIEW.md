# Scientific review

## Correctness — PASS

The exact prefix expression follows from an integer-parity lower bound before the first privately valued good. Assign private goods to their unique valuers and alternate common goods starting on the side opposite the first private good's valuer. The identity \(E_t=\max\{0,-A_t-X_t,X_t-B_t\}\) proves all later envy vanishes, and before that point the magnitude is precisely the parity indicator. This explicitly covers zero-valued goods, no private goods, a private first good, arbitrarily separated common goods, and every finite horizon. The online lower bounds use two fixed valuation sequences with the same first good and offline optimum \(1\); the coin-flip policy attains the bound on this family. A genuinely separate state-space dynamic program checked all \(87{,}381\) valuation sequences through length \(8\), and a second family calculation checked horizons \(2\) through \(30\). These finite tests are corroborative, not substitutes for the proof.

## Originality — PASS, with documented residual risk

The closest full text [1, Section 4, Proposition 1, Theorem 4.1, Appendix 0.B.1] proves the simultaneous lower-bound property for **identical** binary valuations and supplies a general dynamic program, but not the heterogeneous two-agent formula or the exact foresight gap. Its discussion distinguishes fully informed temporal and unknown-future online models. The primary [2, Theorem 3.7, Appendix B.2] guarantees temporal EF1 for generalized binary values, not minimum numeric envy at every prefix. Works [3–4] study distinct binary online efficiency or EF1 objectives. Actual mathematical-record and literature searches for parity, first asymmetric/private arrival, and oblivious-online competitive ratios found no statement implying the complete result. The full text of [1] and the relevant sections/proof of [2] were examined; [3–4] were assessed from their available abstracts. A differently named folklore balancing lemma or unpublished online lower bound remains possible. Missing matches do not prove novelty.

## Value — PASS

The motivating paper [1] formulates optimizing the area under the worst-envy curve, notes the stronger question of optimizing every prefix simultaneously, and provides a general fixed-agent dynamic program. The theorem supplies a structural exact answer for all heterogeneous binary two-agent instances, where the identity of the **first** asymmetric good entirely determines the unique positive-cost region. It simultaneously optimizes all nonnegative prefix weightings and exposes a sharp, unbounded information gap against an oblivious adversary despite complete offline solvability in linear time. This distinguishes mere computational tractability from the temporal information requirements of fairness. It does not claim extensions to nonbinary utilities or three agents.

## Closest scientific sources and limits

[1] Goldberg, Robinson, Teh, arXiv:2610.09843v1, especially §4/Appendix 0.B.1 (identical binary benchmark) and §1.2 (online comparison); [2] Elkind et al., arXiv:2410.14593v1, Theorem 3.7/Appendix B.2 (generalized binary TEF1); [3] Wang and Wei, AAAI 2026, DOI:10.1609/aaai.v40i20.38778 (online binary EF1/MMS); [4] Cookson et al., AAAI 2025, DOI:10.1609/aaai.v39i13.33500 (temporal EF1). The quantitative online minimax values apply only to the displayed pair of adversarial inputs, and prior-work coverage remains an uncertainty rather than a certification of priority.

Self-review: passed. Independent audit: not yet performed.
