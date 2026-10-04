# Review of Weight-uniform Frazer bounds across the full weighted Bergman range

## Correctness

PASS. The only weight-sensitive loss in the inspected two-diameter proof is the lower estimate for
\[
\kappa_\alpha(\rho)
=
\int_\rho^1(1-u^2)^\alpha\,du.
\]
The replacement
\[
\kappa_\alpha(\rho)
\ge
\frac{(1-\rho^2)^{\alpha+1}}{2(\alpha+1)}
\]
is proved by differentiating the difference, whose derivative is exactly
\[
-(1-\rho)(1-\rho^2)^\alpha.
\]
The endpoint ratio shows that the kernel constant is optimal.

Substituting this estimate into the source's Fubini identity cancels the factor \(\alpha+1\) against the normalized weighted-area conversion and removes the factor \(2^\alpha\). The remaining two source ingredients—the angular Frazer reduction and the weighted harmonic Riesz inequality—apply unchanged. The same proof remains integrable for every \(-1<\alpha<0\), so the extension to the full weighted Bergman range is valid.

## Originality

PASS. The full 2026 primary source was inspected at the theorem and proof level. Its stated two-diameter result assumes nonnegative weight parameter and its proof explicitly uses the weaker kernel lower bound with \(2^{\alpha+1}\) in the denominator. The companion weighted Riesz–Fejér source covers the full weight range but only the one-diameter/Riesz setting.

Published-finding database searches used the exact source identifier together with weight-uniform Frazer, sharp radial-kernel, full \(-1<\alpha\) range, and removal-of-\(2^\alpha\) formulations. No covering result was found. General web searches likewise returned the 2026 source and its summaries rather than a sharper follow-up.

The main residual risk is that the elementary incomplete-beta kernel inequality may be known independently. That would not by itself cover the accepted theorem unless it had already been inserted into the weighted harmonic Frazer reduction.

## Value

PASS. The source's explicit constant deteriorates exponentially as the weight parameter grows and leaves out the negative part of the natural Bergman range. A sharp kernel estimate eliminates both artifacts at once: the new two-diameter constant is weight-uniform and the theorem now holds throughout \(-1<\alpha<\infty\).

This is a structural improvement to the paper's principal Frazer extension, not a cosmetic numerical gain. It isolates the exact radial mechanism responsible for the weight dependence and leaves only the genuinely harmonic and angular constants.

Same-model review: passed. Independent audit: not yet performed.
