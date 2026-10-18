# Review of the exact stationary pair law

## Correctness
**PASS.** The result is a single complete pair-covariance classification for the stationary product-start broadcast-voter law on an infinite regular tree. The critical joint midpoint event is of rate \(q\), the two single midpoint moves have rate \(1-q\), and the remaining pair-distance motion is a one-dimensional outward-drifting birth-and-death chain. Its eventual collision probability solves two local equations and an exact gambler's-ruin tail; the stated rational solution satisfies each generator equation. Moment duality turns meeting probability into the stationary covariance. Strict parameter monotonicity and inversion follow by algebra, not simulation. The exact-rational checker passes 2430 finite recurrence/truncation tests; these are only consistency checks of the analytic proof.

## Originality
**PASS, with residual risk.** The main primary paper [1] establishes broadcast dynamics, their coordinated dual, stationary existence, and full-law moment-profile identification on trees. Its pertinent primary full-text sections do not state the regular-tree two-point profile, its distance-two coordination correction, or recovery of \(q\) from a single pair covariance. Classical tree collision probabilities [2] address only the uncoordinated case. A related 2026 voter-variant paper uses different dynamics, and the named targeted mathematical-record/public searches did not show a covering formula. A yet-unlocated general explicit-coalescence theorem could imply the calculation, and independent priority checking remains necessary.

## Mathematical value
**PASS.** The formula completely describes the natural two-point stationary dependence of the new model on a homogeneous nonamenable network, including exact spatial-decay universality and identifiable broadcast coordination from minimal observable data. The single density and pair covariance do not identify the entire broadcast distribution; higher moments can matter for higher-order statistics. This is an exact structural benchmark rather than a code-only finite census.

## Limitations and sources
The domain is \(d\ge3\), fixed homogeneous finite nonzero \(\Lambda\), and stationary laws formed from Bernoulli\((p)\) product initial data with \(0<p<1\). The calculation does not treat irregular graphs or all invariant measures. The principal comparison is [1] Astoquillca, González Casanova and dos Santos, arXiv:2610.04530v1 (2026-10-03); additional context is [2] Durrett, *Dynamics on Graphs*, Chapter 7, Example 7.4.3; [3] Aldous and Fill, Section 14.3; and [4] Astoquillca, *Journal of Theoretical Probability* 39:34 (2026).

Self-review: passed. Independent audit: not yet performed.
