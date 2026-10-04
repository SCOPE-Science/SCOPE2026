# Same-model review

## Correctness

PASS. Equations (4.3) and (4.4) are exact evaluations of one Volterra identity. Subtracting them requires a minus sign before the earlier-time integral. The constant-forcing test gives the exact increment
\[
\frac{\Lambda^{1-h}\Delta^h}{\Gamma(h+1)}\left((v+1)^h-v^h\right),
\]
while the printed parent relation gives the same expression with a plus sign. At \(h=1\), \(v=1\), and \(\Delta=1\), this is the exact contradiction \(1\) versus \(3\). Summing the printed increments at fixed terminal time proves divergence proportional to \(1/\Delta\).

## Originality

PASS. Fractional Adams and Volterra-history methods are established prior art and are treated as such. The accepted contribution is the source-specific correction to equation (4.5), together with the exact constant-forcing and mesh-refinement certificates. Exact DOI, title, equation-number, sign, correction, and erratum searches did not locate an existing published correction of this article.

## Value

PASS. The source uses the derived numerical scheme to support its graphical conclusions about fractional order and delay. A sign error in the exact pre-discretization identity is therefore substantive: as printed, the parent recurrence is not merely lower order but inconsistent. The result is useful even without access to code because it precisely separates the invalid published derivation from the unresolved question of what implementation generated the figures.

## Closest literature and limitations

Diethelm, Ford, and Freed provide the closest standard numerical-analysis comparison: their Caputo Adams method is derived from the nonlocal Volterra equation and retains history weights over all previous nodes. That work is methodological prior art, not a correction of this COVID model.

The present finding does not claim that unavailable simulation code contained the same sign error, and it does not reassess unrelated analytical results in the article.

Same-model review: passed. Independent audit: not yet performed.
