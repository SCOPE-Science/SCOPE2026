# Scientific review: threshold-triggered flood duration

## Correctness

**PASS.** The scalar threshold-recession clock \(\Phi_h\) loses precisely one unit per unit time whenever discharge exceeds the threshold. Its jumps telescope exactly to the full exceedance duration, including schedules with separated exceedance events. Strictly decreasing reciprocal recession rate proves each later pulse contributes at most \(\Phi_h(h+P)\), with equality only when the pre-pulse level is exactly \(h\). The total fixed-order bound is attained with finite, positive gaps. The first-pulse advantage is the strictly increasing function \(-\int_P^{P+h}1/f\), proving the largest-first rule. All specified boundaries and quantifiers are explicit. Exact rational checks for two recession laws passed 36,006 assertions; this is verification evidence, not a replacement for proof.

## Originality

**PASS under scoped best-knowledge comparison, with residual historical risk.** Targeted searches of related published mathematical findings and accessible hydrological literature found no statement covering the exact objective, arbitrary unequal individually threshold-crossing additive discharge impulses, all strictly increasing recession laws and equality classification. Harman et al. (2009) treat impulse and periodic-recharge recession shapes; Gnecco et al. (2018) optimize peak discharge under a different response; Lawson et al. (2025) characterize statistical threshold-event durations. The nearest related hydrological mathematical statement concerns periodic two-storm saturation-excess runoff *volume*, not maximum time above a threshold. General impulsive-control theory may imply the claim, and this is not a certified literature-exhaustive priority determination.

## Value

**PASS.** Duration above a flow threshold is a substantive hydrological risk metric distinct from peak discharge, as reflected in empirical duration-over-threshold modeling. The theorem provides a sharp, generally nonlinear, finite-multistorm adversarial bound and a complete extremal timing/ordering prescription without combinatorial schedule optimization. The largest-first rule for unequal event sizes and the threshold-triggering condition are both nontrivial structural predictions. The result is restricted to idealized additive discharge impulses and does not purport to forecast real storms or model finite-duration rainfall.

## Closest literature and limitations

Harman et al., *Water Resources Research* (2009), DOI 10.1029/2008WR007392; Gnecco et al., *Hydrology and Earth System Sciences* (2018), DOI 10.5194/hess-22-943-2018; Lawson et al., *Water Resources Research* (2025), DOI 10.1029/2023WR037022. The objective and assumption comparisons are documented in the structured audit. The unresolved risk is a stronger abstract rearrangement theorem in impulse control. The source papers do not validate the instantaneously additive nonlinear discharge-jump idealization for arbitrary catchments.

Self-review: passed. Independent audit: not yet performed.
